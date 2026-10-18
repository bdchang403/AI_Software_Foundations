# Module 1: Validation Contracts & Invariant Assertion Directives

## 🧠 Theory: Epistemic Isolation — Test the Contract, Not the AI's Code

In software development assisted by autonomous AI agents, the single most dangerous failure mode is **Circular Verification** (often described as "the AI grading its own homework"). When an engineering team instructs an AI agent with a naive directive such as:
> *"Write unit tests for `execution_gateway.py` to ensure high test coverage."*

The model parses the implementation code written by the builder agent and reverse-engineers assertions to match whatever the code currently executes. If the builder agent silently introduced a synthetic default in an exception handler (`except Exception: return 0.50`), the test-generation agent will enthusiastically write:
```python
def test_execution_gateway_error_handling():
    # Flawed assertion confirming synthetic poison!
    assert gateway.calculate_ratio(invalid_input) == 0.50
```
Both the implementation and the test pass with 100% green status, yet the system has codified a catastrophic architectural violation into production CI.

To eliminate this circular failure mode, Quality Engineers must enforce **Epistemic Air-Gapping**: the AI test author must be provided the **Semantic Blueprint** and the **System Invariants** as the authoritative source of truth, while being strictly air-gapped from the implementation source code until after the test suite is generated.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   EPISTEMIC AIR-GAPPING IN TEST SUITE GENERATION                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ❌ NATIVE CONVERSATIONAL (CIRCULAR VERIFICATION)                                               │
│   ┌──────────────┐         ┌──────────────┐         ┌─────────────────────────┐                  │
│   │ Implementation│ ──────► │ AI Test      │ ──────► │ Tests match buggy code! │                  │
│   │ Code (Buggy) │         │ Generator    │         │ False Sense of Security │                  │
│   └──────────────┘         └──────────────┘         └─────────────────────────┘                  │
│                                                                                                  │
│   ✅ EPISTEMICALLY AIR-GAPPED (CONTRACT-FIRST VALIDATION)                                        │
│   ┌──────────────┐         ┌──────────────┐         ┌─────────────────────────┐                  │
│   │ Semantic     │         │ AI Test      │         │ Adversarial Tests Assert│                  │
│   │ Blueprint &  │ ──────► │ Generator    │ ──────► │ Blueprint Invariants    │ ──► Breaks Buggy │
│   │ Invariants   │         │ (Isolated)   │         │ (Zero Implementation)   │     Code in CI!  │
│   └──────────────┘         └──────────────┘         └─────────────────────────┘                  │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📐 Anatomy of the Quality Engineering 3-Part Directive

Every directive authored by a Validation Lead or Quality Engineer must follow the **3-Part Structure for Validation**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                       ANATOMY OF THE QE 3-PART DIRECTIVE                                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   PART 1: CONTEXT BOUNDARY (The Ground-Truth Specification)                                      │
│   • Authoritative specification document (e.g., `SEMANTIC_BLUEPRINT_SPECIFICATION.md`).          │
│   • Binding System Invariants (e.g., Invariant $I_{01}$, Invariant $I_{02}$, Invariant $I_{09}$).  │
│   • Explicit exclusion: FORBIDDEN from reading target implementation files in `src/`.             │
│   • Test suite budget: target ~400 lines per test module (Architectural Modularity Heuristic for SRP & cognitive bounds). │
│                                                                                                  │
│   PART 2: TASK INSTRUCTION (Adversarial Edge-Case Generation)                                    │
│   • Precise failure paths, negative boundaries, and edge cases to target.                        │
│   • Conformal fuzzing permutations: $\{\text{NaN}, +\infty, -\infty, \text{None}, \text{Empty}\}$. │
│   • Verification of fail-closed semantics: asserting raised exceptions or `None` returns.        │
│   • Mandatory cryptographic anchor checks: asserting SHA1 checksum validity.                     │
│                                                                                                  │
│   PART 3: FORMAT & ARCHITECTURAL CONSTRAINTS (Zero-Mock Mandate)                                 │
│   • Hermetic Socket Isolation: all tests must execute under `pytest-socket`.                     │
│   • Zero Synthetic Mocks in Prod: zero fail-soft stubs or synthetic data in production modules.  │
│   • AST Zero-Mock compliance: zero ZM001–ZM009 violations in source; contract test doubles only. │
│   • Deterministic execution: test must complete in $<5\text{ms}$ without thread sleeping.       │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Role-Based Operational Playbook: Before vs. After Across Domains

### Domain A: Quantitative Asset Management (Order Guardrail Validation)

#### ❌ The Naive Test Directive (Failure Mode)
> *"Write pytest tests for `src/execution/execution_guardrails.py` to test the execution price checks."*
* **The Failure**: The AI inspects `execution_guardrails.py`, observes that missing price feeds return a default spot of `\$200.00`, and writes tests asserting that `validate_order(None)` succeeds with price `200.0`. This codifies Crisis 3 (Synthetic Poison) directly into CI.

#### ✅ The Validation Lead 3-Part Directive (Production Standard)
```markdown
### 1. CONTEXT BOUNDARY
- SPECIFICATION: `docs/specs/ORDER_EXECUTION_BLUEPRINT.md` (Section 3: Pre-Trade Plausibility Band).
- BOUNDING INVARIANTS: 
  * Invariant $I_{01}$ (Zero-Simulated-Data): Unverified feeds must return `None` or raise `UnverifiedDataError`.
  * Invariant $I_{02}$ (Execution-Price Guardrail): $|P_{\text{exec}} - \text{EMA}_5| \le \max(3.0 \cdot \text{ATR}_{14}, \; 0.08 \cdot \text{EMA}_5)$.
- FORBIDDEN PATHS: Do not inspect `src/execution/execution_guardrails.py`. Design tests strictly from the blueprint mathematical equations.
- TARGET FILE: `tests/unit/test_execution_guardrails.py` (Target ~350 LOC, adhering to the 400-LOC modularity heuristic).

### 2. TASK INSTRUCTION
Generate an adversarial pytest suite targeting `ExecutionGuardrails.validate_order()`:
1. Normal Case: Assert order approval when execution price is within dynamic bounds.
2. Breach Case: Assert `ExecutionGuardrailViolation` when $|P_{\text{exec}} - \text{EMA}_5| > \max(3\text{ATR}, 0.08\text{EMA})$.
3. Weekend Mark Case: Assert order rejection when weekend execution drifts $>1.0\%$ from Friday close.
4. Telemetry Fault Case: Assert `InvalidTelemetryError` when `spot_price` is `None`, `NaN`, `Inf`, or boolean (`True`/`False`).
5. Missing ATR Case: Assert fail-closed rejection when historical bars $< 15$.

### 3. FORMAT & ARCHITECTURAL CONSTRAINTS
- HERMETIC ISOLATION: Tests must execute cleanly with network sockets disabled (`pytest-socket`).
- ZERO-MOCK MANDATE: Do not mock internal system logic in production; in test suites, pass pure numerical inputs directly into the public class interface or use deterministic contract-bound test doubles without unanchored mocks.
- AST SCANNER COMPLIANCE: Zero ZM001–ZM009 violations. Do not use `MOCK_` variable prefixes.
- MODULARITY HEURISTIC: Target file sizing should respect the ~400 LOC modularity heuristic for single-responsibility focus.
- OUTPUT FORMAT: Emit pure executable Python test code in a single file.
```

---

### Domain B: FDA Class III Medical Device (Closed-Loop Insulin Delivery)

#### ❌ The Naive Test Directive (Failure Mode)
> *"Generate unit tests for the insulin titration controller in `controller.c`."*
* **The Failure**: The AI writes tests asserting that when the continuous glucose monitor (CGM) disconnects, the controller injects a default glucose reading of `100\,\text{mg/dL}`. In a live patient, injecting insulin based on a hallucinated normal reading during acute hypoglycemia causes fatal insulin shock.

#### ✅ The Validation Lead 3-Part Directive (FDA 21 CFR Part 820.30 Standard)
```markdown
### 1. CONTEXT BOUNDARY
- SPECIFICATION: `docs/regulatory/PMA_CLINICAL_ALGORITHM_SPEC.md` (Section 4: Sensor Anomaly Mitigation).
- REGULATORY COMPLIANCE TARGET: Objective evidence supporting FDA 21 CFR Part 820.30(g) Design Validation and IEC 62304 Class C Medical Device Software Verification.
- BOUNDING INVARIANTS:
  * Invariant $I_{01}$ Equivalent: Zero Simulated Biosensor Telemetry. No imputed glucose readings.
  * Invariant $I_{02}$ Equivalent: Maximum Basal Plausibility Envelope:
    $$|\text{Dose}_{\text{proposed}} - \text{Basal}_{\text{baseline}}| \le \min(2.5 \cdot \text{IOB}_{\text{decayed}}, \; 0.15 \cdot \text{TotalDailyDose})$$
- FORBIDDEN PATHS: Do not read `firmware/src/titration_controller.c`.
- TARGET FILE: `firmware/tests/test_titration_controller.py`.

### 2. TASK INSTRUCTION
Generate rigorous fault-injection tests targeting `TitrationController.calculate_bolus()`:
1. Probe Loss: When CGM sensor stream emits packet drop, CRC error, or `telemetry_source != CGM_DEXCOM_G7_BLE`, assert that controller halts bolus delivery, sounds high-priority acoustic alarm, and reverts to hardwired safe basal rate ($0.05\,\text{U/hr}$).
2. Glucose Smuggling: Inject `NaN`, `-1.0`, `99999.0`, and boolean `True` as glucose readings. Assert controller raises `SensorIntegrityException` and latches valve shut.
3. Plausibility Band Breach: Request a bolus of $10.0\,\text{U}$ when insulin-on-board (IOB) indicates active saturation. Assert immediate clamping to the plausibility ceiling.

### 3. FORMAT & ARCHITECTURAL CONSTRAINTS
- HERMETIC ISOLATION: Socket and hardware communication must be air-gapped; tests must run on headless CI runners.
- ZERO IMPUTATION: Assert that under no condition does the controller synthesize a synthetic glucose reading.
- TRACEABILITY TAG: Every test must include the requirement trace decorator `@pytest.mark.trace("FDA-PMA-ANOMALY-04")`.
```

---

## 🛠️ Hands-On Exercise: Authoring the Invariant-Bound Test Directive

### The Scenario
The engineering team is deploying a new service: `CorporateDebtSolvencyService`. This service computes the **Weighted Average Floating Coupon Debt (WAFCD)** and the **Refinancing Stress Score (RSS)** based on discrete SEC Form 10-K disclosures (Discrete Debt Solvency & Refinancing Stress Guardrail).

Under Invariant $I_{01}$, if an SEC filing contains a floating-rate debt tranche with a redacted or missing coupon spread, the service **must fail closed** (`stated_coupon = None`), rather than imputing a synthetic benchmark rate (such as assuming SOFR + 200 bps). Under Invariant $I_{03}$, if $\text{RSS} \ge 1.20$, the service must emit a hard `DISTRESS_INSOLVENCY_VETO`.

### Your Task
Draft the complete 3-Part Directive instructing an AI agent to author the test suite for this service. Ensure:
1. **Context Boundary**: Directs the agent to `docs/specs/DEBT_SOLVENCY_BLUEPRINT.md` and explicitly forbids reading `src/solvency/`.
2. **Task Instruction**: Explicitly requires tests for redacted coupon spreads, zero imputation, RSS calculation boundaries at $1.19$ vs $1.20$, and division-by-zero protection when FCF is zero ($I_{07}$).
3. **Format Constraints**: Enforces zero ZM001–ZM007 violations, hermetic execution, and test file line bounds.

---

## Production Reality & Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)
In the mid-2026 median engineering baseline (the 75\%--84\% ad-hoc adoption mean), automated testing functions as an exercise in **Circular Verification** (the 2026 Google DORA Verification Trap). After prompting an AI assistant to generate a feature implementation, developers issue unstructured test requests: *"Write unit tests for `execution_gateway.py` to get code coverage above 85\%."*

The model inspects the implementation code it just synthesized, reverse-engineers assertions to match whatever the code currently emits, and generates tests that pass immediately. If the implementation silently swallowed an exception and returned `0.50`, the generated test asserts `assert calculate_risk() == 0.50`. Test pipelines report 100\% pass rates and SonarQube dashboards display elevated line coverage, but the system has merely codified self-reinforcing tautologies. The AI grades its own implementation without reference to independent architectural specifications. No invariants are validated, negative boundary conditions remain unexercised, and catastrophic logic flaws are codified into regression suites.

### Failure Modes & Drift Dynamics in Ungoverned Production
Operating under circular test generation without contract-first validation leads to three severe production failure modes:
1. **Codification of Regressions into CI**: When an AI agent introduces a subtle logic defect (e.g., failing open on missing authentication headers), conversational test generation authors tests asserting that failing open is expected behavior. When production is breached, automated test suites remain green.
2. **The High-Coverage Illusion**: Management relies on 90\% code coverage metrics that provide zero fault-detection capability. The first real-world edge case (e.g., null payloads, NaN floats, expired tokens) triggers critical system outages across paths deemed fully covered.
3. **Review Fatigue from Tautological Boilerplate**: Senior engineers spend excessive hours forensically parsing hundreds of lines of AI-generated mock boilerplate that tests trivial syntactic accessors rather than domain invariants, driving PR review times up by +91\% (Faros AI telemetry).

### Deterministic Engineering Defenses & Operational Takeaways
To permanently eliminate circular verification and enforce contract-first validation, engineering teams enforce these operational invariants:
- **Enforce Strict Epistemic Air-Gapping**: Forbid test-generation prompts from ingesting implementation source files in `src/`. Test-generating models must be provided exclusively with Closed-World Semantic Blueprints, ADRs, and Invariant predicates, forcing validation against specifications rather than implementation artifacts.
- **Mandate QE 3-Part Directives**: Require all automated test authoring to employ the QE 3-Part Directive, explicitly enumerating negative boundary cases ($\text{NaN}$, $\pm\infty$, `None`, missing fields) and invariant bindings ($I_{01}$--$I_{22}$).
- **Enforce Fail-Closed Test Assertions**: Require test suites to assert that missing or corrupted external inputs fail closed (raising explicit domain exceptions or returning `None`) rather than defaulting to synthetic constants.
- **Measure Mutation Score Over Raw LOC Coverage**: Retire raw line coverage as an authoritative quality gate. Require mutation testing or fault-injection verification to confirm that test suites reliably detect injected regressions and boundary anomalies.

