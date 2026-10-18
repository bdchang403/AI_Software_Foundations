# Requirements Lead Lab Workbook: Semantic Contracts & Boundary Invariants

Welcome to the Requirements Lead & Business Analyst Lab. In the enterprise Context Pipeline, you are the **Translator and Adversarial Red-Teamer**. Your mission is to take high-level strategic blueprints from the Product Owner and translate them into **machine-executable interface contracts** that autonomous AI builders cannot misinterpret or bypass.

This workbook contains four practical, high-stakes lab exercises with complete answer keys.

---

## 🧪 Lab 1: Transforming Ambiguous PRDs into 3-Part Directives (Module 1)

### The Scenario
You receive an informal Product Requirement Document (PRD) excerpt for a high-stakes banking ledger:
> *"Build an automated wire transfer validation service. The service should verify that the account has sufficient funds, calculate transaction fees, and ensure the wire amount is not abnormal. If the upstream fraud API fails, make sure the customer doesn't get blocked."*

### Adversarial Red-Team Analysis
If fed directly to an AI agent, this requirement will induce catastrophic vulnerabilities:
1. *"Ensure the wire amount is not abnormal"*: The AI will invent an arbitrary constant threshold (e.g., `amount > 10000`) or omit the check entirely.
2. *"If the upstream fraud API fails, make sure the customer doesn't get blocked"*: The AI will write `except Exception: return {"fraud_score": 0.0, "approved": True}`, allowing sanctioned or fraudulent transfers during network blips (violating Invariant $I_{01}$).
3. *"Calculate transaction fees"*: Missing division-by-zero checks when computing tiered basis point percentages (violating Invariant $I_{07}$).

### Your Task
Rewrite this requirement into a rigorous **3-Part Directive**:
1. Define the isolated **Role** and epistemic tool boundaries (Role-Based Epistemic Slicing Guardrail).
2. Formulate the deterministic mathematical **Task** with typed schemas.
3. Bind the directive to Canonical Invariants ($I_{01}, I_{02}, I_{04}, I_{07}, I_{15}$).

### Answer Key (Compare Your Work)

```markdown
### 3-Part Directive: Wire Transfer Authorization Service (STORY-BANK-101)
- **Role**: You are the Wire Transfer Pre-Execution Gating Worker. Your scope is bounded to verified core ledger balances and the compliance sanction screener. You have zero access to marketing or customer communication tools.
- **Task**: Ingest `WireRequestDTO(account_id: str, amount_cents: int, currency: str, beneficiary_routing: str, trace_id: UUIDv4)`.
  1. Verify available settled balance: $\text{Balance} - \text{Hold} \ge \text{amount-cents} + \text{Fee}$.
  2. Compute fee: $\text{Fee} = \max(2500, \text{round}(\text{amount-cents} \times 0.0015))$.
  3. Emit `WireAuthorizationVerdict(approved: bool, reason: str, trace_id: UUIDv4)`.
- **Constraint**:
  1. Bind to $I_{01}$ (Zero-Simulated-Data): If the compliance sanction API times out, FAIL CLOSED: return `approved = False, reason = "SANCTION_SCREENER_UNAVAILABLE"`. Fallback approvals are strictly prohibited.
  2. Bind to $I_{02}$ (Execution Plausibility): If $\text{amount-cents} > 3 \times \mu_{\text{history}}(account)$, flag transaction for dual-custody approval (`MANUAL_CUSTODY_HOLD`).
  3. Bind to $I_{04}$ (Immutable Quarantine): Rejected or suspicious transfer attempts must be persisted to `wire_quarantine_ledger`. Hard deletes are banned.
  4. Bind to $I_{07}$ (Div-by-Zero Safety): Ratio calculations must assert non-zero balance baselines.
  5. Bind to $I_{15}$ (UUID Traceability): Every verdict must preserve the inbound UUIDv4 trace identifier.
```

---

## 🧪 Lab 2: Generating the 20 Pre-condition Boundary Edge Cases (Module 2)

### The Scenario
You are specifying `STORY-QUANT-104`: *"Implement Ledoit-Wolf analytical covariance shrinkage and symmetrical ZCA whitening for 4-pillar portfolio scores"*.

### Your Task
Populate the 20 pre-condition boundary edge cases for this quantitative mathematical function, defining the exact error handling behavior for:
- Case #1 (Empty Input Matrix)
- Case #3 (Division-by-Zero in variance trace)
- Case #4 (NaN Smuggling in pillar scores)
- Case #6 (Boolean Smuggling)
- Case #12 (Ill-conditioned covariance matrix where $\text{cond}(\Sigma) > 10^{12}$)

### Answer Key (Compare Your Work)

| # | Edge Case Category | Input Pre-condition Boundary | Expected Deterministic Output / Error Behavior | Governing Invariant |
|---|---|---|---|---|
| **1** | **Empty Input** | Input score matrix is empty: `X.shape[0] == 0`. | Return empty decorrelated matrix or raise `InsufficientDataError`. Never return mock scores. | $I_{01}$ |
| **3** | **Division-by-Zero** | Trace of covariance matrix $\text{Tr}(S) == 0.0$. | Regularize trace: floor $\mu = \max(\text{Tr}(S)/p, \; 10^{-6})$. Prevent division-by-zero. | $I_{07}$ |
| **4** | **NaN Smuggling** | Element $X_{ij}$ is `np.nan` or `float('nan')`. | Intercept via `np.isnan(X).any()`; raise `CorruptedMatrixTaintError`. Fail closed. | $I_{01}, I_{11}$ |
| **6** | **Boolean Smuggling** | Pillar vector contains boolean `True` in place of float. | Intercept via `isinstance(val, bool)`; reject payload immediately. | $I_{01}$ |
| **12**| **Ill-Conditioned Matrix** | Condition number $\text{cond}(\Sigma) > 10^{12}$. | Apply regularized Ledoit-Wolf shrinkage floor $\Lambda_{\text{safe}} = \max(\Lambda_i, 10^{-6} \Lambda_{\max})$. Stabilize condition number. | $I_{11}$ |

---

## 🧪 Lab 3: Epistemic Air-Gap & 80% Commercial Discount Remediation (Module 4)

### The Scenario
You are auditing an automated requirements intake workflow that ingested a vendor marketing report titled: *"Autonomous ICU Patient Monitor Slashes Alarm Fatigue by 95%"*. The vendor report includes links to schedule a sales demo and purchase hospital enterprise licenses (`commercial_conflict: true`).
- The un-discounted extracted efficacy polarity is $+8.50$.
- The vendor baseline credibility score is $W_{\text{Brier}} = 0.50$.

### Your Task
1. Calculate the stored polarity $\text{Polarity}_{\text{stored}}$ and effective credibility weight $W_{\text{eff}}$ using the 80% Commercial Funnel Discount:
   $$W_{\text{eff}} = W_{\text{Brier}} \times 0.20, \quad \text{Polarity}_{\text{stored}} = \text{round}(\text{Polarity}_{\text{raw}} \times 0.20, \; 2)$$
2. Formulate the Unidirectional Epistemic Air-Gap Guardrail negative air-gap constraint.

### Answer Key (Compare Your Work)

#### Mathematical Calculation:
$$\text{Polarity}_{\text{stored}} = \text{round}(+8.50 \times 0.20, \; 2) = \mathbf{+1.70}$$
$$W_{\text{eff}} = 0.50 \times 0.20 = \mathbf{0.10}$$

#### Unidirectional Epistemic Air-Gap Guardrail Negative Air-Gap Constraint:
```markdown
CONSTRAINT: Unidirectional Epistemic Air-Gap Guardrail Active.
1. The extraction agent MUST NOT receive internal hospital clinical trial results or current ICU mortality benchmarks.
2. The extracted finding is classified as SPONSORED_CLAIM (Weight = 0.10, Polarity = +1.70).
3. The claim is contractually prohibited from updating clinical alarm threshold algorithms without independent FDA 510(k) cleared peer-reviewed evidence.
```

---

## 🧪 Lab 4: Authoring a Semantic Blueprint with Closed-World Fallback (Module 4 & Master Spec)

### The Scenario
You are the BA for an FDA Class III Automated External Defibrillator (AED) advisory pipeline. You are authoring the specification for `STORY-MED-204`: *"Ventricular Fibrillation Electrocardiogram Rhythm Classifier"*.

### Your Task
Draft the **Context-Enriched Semantic Blueprint**, incorporating:
1. Bounded Subsystem Execution Map (`src/clinical/ecg_classifier.py`).
2. Closed-World Fallback Contract ($I_{05}$) when electrode impedance exceeds safe thresholds.
3. Invariant Anchor Block for Invariant $I_{03}$ (Fatal-Contagion Veto).

### Answer Key (Compare Your Work)

```markdown
# Context-Enriched Semantic Blueprint: ECG Shock Advisory (STORY-MED-204)

## 1. Execution Metadata
- **Story ID**: `STORY-MED-204`
- **Epic ID**: `EPIC-AED-01`
- **Bounded Subsystem**: `src/clinical/ecg_classifier.py`
- **Max Token Budget**: `3,000 tokens`
- **Target File LOC**: `260 lines of code (Architectural Modularity Ceiling <= 400)`
- **Governing Invariants**: `I01, I03, I05, I07, I15`

## 2. Bounded Subsystem Execution Map
| Business Domain Concept | Canonical Implementation Path | Restricted Search Sandbox | Forbidden Traversal Paths |
| :--- | :--- | :--- | :--- |
| **"ECG Waveform Classifier"** | `src/clinical/ecg_classifier.py` | `src/clinical/*` | `src/audio/*`, `legacy/*` |
| **"Electrode Impedance Checker"**| `src/hardware/pad_impedance.py` | `src/hardware/*` | `tests/mocks/*` |

## 3. Closed-World Fallback Schema (Invariant I05)
If electrode pad contact impedance $> 300\,\Omega$ or signal is saturated:
```json
{
  "rhythm_verdict": "SHOCK_ADVISED_UNKNOWN",
  "confidence": 0,
  "shock_decision_blocked": true,
  "hardware_status": "PAD_CONTACT_POOR",
  "clinical_action": "PROMPT_USER_CHECK_PADS"
}
```
*Zero synthetic rhythm interpolation is permitted.*

## 4. Invariant Anchor Block
```python
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: I03
# NAME: Fatal-Contagion Veto
# GUARDRAIL: Compensatory 4-Pillar Confluence (Invariant I09)
# CLASS: HARD-SAFETY
# ROLE: CANONICAL_IMPL
# PREDICATE: Fatal telemetry corruption or pad fault vetos shock authorization
# ASSERT: tests/unit/test_ecg_safety_invariants.py
# /INVARIANT [sha1:xxxxxxxx]
# === /INVARIANT-BLOCK ===
```
```

---

## Production Reality & Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)
In median mid-2026 engineering organizations, requirements artifacts and lab exercises are frequently treated as theoretical compliance burdens rather than binding operational contracts. Business analysts continue authoring ambiguous bullet points in Jira tickets (*"Ensure user receives an alert when sensor contact is poor"*), while developers use inline AI autocomplete to construct synthetic unit tests (`mock_sensor.get_impedance.return_value = 50.0`). In the absence of an empirical edge-case matrix and closed-world schemas, tests report nominal 100% coverage while leaving production systems entirely unprotected against real-world sensor dropouts, IEEE 754 non-finite floats, or packet corruption.

### Failure Modes & Drift Dynamics in Ungoverned Production
Failing to enforce structured requirements engineering and closed-world schemas in hands-on workflows triggers three severe failure patterns:
1. **The Phantom Coverage Mirage**: Developers leverage generative AI to generate suites of unit tests that mock away physical failure boundaries. When sensor disconnects or network jitter occur in clinical or financial environments, systems execute un-gated actuations because test suites only verified synthetic happy paths.
2. **Review Gridlock (Faros +91% Review Tax)**: Pull request review cycles expand exponentially when senior reviewers must reconstruct unstated assumptions, missing null checks, and unhandled non-finite float conditions by hand.
3. **Regulatory Non-Compliance & Audit Failure**: Under FDA 21 CFR 820.30(g) and EU AI Act Articles 10/13, lack of verifiable pre-condition matrices and traceable invariant anchor blocks invalidates formal safety cases, exposing organizations to regulatory sanctions.

### Deterministic Engineering Defenses & Operational Takeaways
To operationalize compiler-grade requirements across engineering pods, teams must enforce four foundational practices:
1. **Mandate the 20 Edge-Case Precondition Sign-off**: Before any feature implementation begins, require business analysts and engineering leads to complete the 20 Edge-Case Matrix, explicitly specifying deterministic behaviors for missing keys, timeouts, and non-finite floats.
2. **Enforce Closed-World Schemas for Telemetry ($I_{05}$)**: Prohibit untyped dictionaries in telemetry ingress. Require typed schemas with explicit closed-world fallback states (`"SHOCK_ADVISED_UNKNOWN"`, `"PROBE_DISCONNECTED"`).
3. **Embed Cryptographically Verified Invariant Blocks**: Require safety-critical modules to embed structured invariant anchor blocks ($I_{01}-I_{22}$) with SHA-1 checksums validated by automated pre-commit and CI tooling.
4. **Enforce Zero-Mock AST Scanning (ZM001–ZM007)**: Integrate automated AST analyzers into continuous integration pipelines, failing any PR where unit tests rely on synthetic constant mocks to satisfy error paths.


