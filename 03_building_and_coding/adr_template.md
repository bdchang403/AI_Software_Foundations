# Architecture Decision Record (ADR) Template: Enterprise Context Standard

*Authoring Directive for AI & Human Architects: Generate an ADR following this exact template. Every decision must define machine-enforceable constraints, invariant bindings, and SHA1 code anchor specifications so future autonomous agents cannot silently violate or erase the decision.*

---

## Metadata
* **ADR-ID:** `ADR-[0-9]{3}` *(e.g., ADR-016, ADR-029)*
* **Title:** `[Short, imperative noun phrase describing architectural decision]`
* **Status:** `[Proposed | Accepted | Deprecated | Superseded by ADR-XXX]`
* **Date:** `[YYYY-MM-DD]`
* **Authors / System Architects:** `[Names / Autonomous Agent IDs]`
* **Governing Enterprise Invariant(s):** `[$I_{01}$ through $I_{22}$ | None]`
* **Regulated Domain Classification:** `[FDA Class III SaMD | RTCA DO-178C Level A | FinTech Critical | Core Banking]`

---

## 1. Context and Problem Statement
*Describe the physical, economic, or mathematical constraints driving this decision. Identify the specific failure mode or crisis archetype that necessitates this architectural change (e.g., Crisis 1 Monolithic Cron Poller, Crisis 2 Context Drift, Crisis 3 Synthetic Poison).*

* **Observed Failure Mode:** `[Detail the observed latency, token burn, race condition, or context degradation]`
* **Working Memory / Attention Implications:** `[Attention entropy $\mathcal{H}(A_i)$, U-curve retrieval loss $F(x)$, or prompt token overhead]`
* **Economic / Spend Budget:** `[Micro-USD cost impact against the \$0.40/day rolling spend cap]`

---

## 2. Decision Drivers
*What physical, regulatory, or operational constraints strictly govern the acceptable solutions?*
1. **D1 (Deterministic Reproducibility):** Output must be reproducible across local and remote CI without stochastic drift.
2. **D2 (Modularity & Working Memory):** Implementations must adhere to Architectural Modularity Heuristics (target <= 400 LOC) and Semantic AST Structural Scoping.
3. **D3 (Fail-Closed Safety):** Failure states must halt execution or return `None`; zero synthetic fallbacks permitted (Invariant $I_{01}$).
4. **D4 (Regulatory Auditability):** Full 1:1 bidirectional traceability from requirements to code-adjacent invariant anchors.

---

## 3. Considered Architectural Options
*Document the rejected patterns so autonomous AI agents do not re-propose previously invalidated workarounds.*

### Option 1: [The Naive / Conversational Approach]
* **Description:** `[e.g., Unbounded markdown specifications, naive vector RAG, prompt-based token restraint]`
* **Why Rejected:** `[Detail mathematical failure mode: e.g., cosine similarity sign-blindness ($\cos \ge 0.94$), attention entropy dilution, silent feature erasure]`

### Option 2: [Alternative Modern Architecture]
* **Description:** `[e.g., Heavyweight distributed graph database, external third-party microservice]`
* **Why Rejected:** `[e.g., Exceeds daily micro-USD spend quota, introduces non-hermetic network socket dependencies violating test isolation]`

### Option 3: [Selected Production Mechanism]
* **Description:** `[e.g., Deterministic AST Registries with Living Context compilation and SHA1 invariant anchors]`
* **Why Chosen:** `[Solves failure mode at zero marginal compute cost, fully verifiable in local memory in <2 seconds]`

---

## 4. Decision Outcome & Systemic Invariant

**Chosen Option:** `[Option 3: Name]`, because it guarantees fail-closed deterministic execution while respecting working memory and spend limits.

### Formal Mathematical Predicate (If Applicable)
$$\text{Predicate Formula (in standard LaTeX)}$$

### Machine Contract & Invariant Binding
* **Invariant ID:** `[e.g., I02, I07, I16, I22]`
* **Target Source Modules:** `[e.g., src/execution/execution_gateway.py]`
* **Enforcing AST Rules / Unit Tests:** `[e.g., test_tier2_boundary_invariants.py, ZM001–ZM009]`

---

## 5. Code-Adjacent SHA1 Invariant Anchor Specification

Any module implementing this ADR must embed the following machine-parseable anchor block immediately preceding the primary implementation function or class:

```python
# === INVARIANT-BLOCK v1 ===
# INVARIANT: [INV_ID]
# ADR: [ADR-ID]
# PREDICATE: [Exact single-line mathematical or logical predicate string]
# /INVARIANT [sha1:[8-character-hex]]
# === /INVARIANT-BLOCK ===
```

### Deterministic Hash Calculation
$$\text{Checksum} = \mathrm{SHA1}\left(\text{INV-ID} \;\|\; \text{ADR-ID.strip()} \;\|\; \text{PREDICATE.strip()}\right)[:8]$$

---

## 6. Consequences & Agentic Constraints

### Positive Consequences
* `[e.g., Eliminates schema hallucinations by injecting minified living context]`
* `[e.g., Saves ~10,000 prompt tokens per multi-agent session, keeping spend under \$0.40/day]`

### Negative Consequences / Trade-offs
* `[e.g., Developers must run atomic pre-commit command chain before merging to prevent CI drift failure]`
* `[e.g., Source files approaching 350 physical lines should be evaluated for modular decomposition]`

### Explicit Agentic Machine Constraints (Injected into System Prompts)
1. **Rule 14 Anti-Feature-Erasure:** Autonomous agents refactoring code under this ADR are FORBIDDEN from deleting fallback cascades, retry logic, or telemetry assertions to satisfy line limits.
2. **Zero-Mock Enforcement:** Autonomous agents are FORBIDDEN from providing positive numeric defaults in function arguments (ZM005) or returning fallback constants in `except` blocks (ZM001).
3. **AST Freshness Assertion:** Any modification to files governed by this ADR must execute `scripts/update_state_registry.py` and `scripts/update_math_registry.py` with zero git diff.

---

## 7. Dual-Use Regulated Impact Assessment

::: tip DUAL-USE APPLICATION MATRIX
| High-Stakes Domain | Architectural Equivalent & Direct Translation |
| :--- | :--- |
| **Quantitative Asset Management** | `[e.g., Enforcing pre-trade plausibility bounds to prevent market spike liquidations]` |
| **FDA Class III Medical Devices** | `[e.g., Enforcing closed-loop drug infusion limits to prevent fatal over-titration]` |
| **Aerospace Avionics (DO-178C)** | `[e.g., Enforcing flight envelope control surface deflection clamping during turbulence]` |
| **Mission-Critical Banking** | `[e.g., Enforcing dual-custody approval holds on wire transactions deviating from baseline]` |
:::
