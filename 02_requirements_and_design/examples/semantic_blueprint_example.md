# Concrete Production Examples: Context-Enriched Semantic Blueprints

Business Analysts must translate abstract business requirements into boolean, structural contracts that autonomous AI agents and validation test harnesses can execute deterministically.

Below are two exhaustive production-grade Semantic Blueprint examples from high-stakes regulated domains:
1. **Regulated Domain A: Quantitative Algorithmic Trading Safeguards (`STORY-FIN-109`)**
2. **Regulated Domain B: FDA Class III Medical Device Hemodynamic Safety Gate (`STORY-MED-402`)**

---

## 🏛️ Example 1: Quantitative Algorithmic Trading Safeguards (`STORY-FIN-109`)

### 1. Execution Metadata
- **Story ID**: `STORY-FIN-109`
- **Epic ID**: `EPIC-RISK-02`
- **Bounded Subsystem**: `02_requirements_and_specifications`, `src/execution/guardrails.py`
- **Max Token Budget**: `3,200 tokens`
- **Target File LOC**: `280 lines of code (Architectural Modularity Ceiling <= 400)`
- **Governing Invariants**: `I01, I02, I04, I07, I15`
- **Required Skill Level**: `EXPERT_PYTHON_QUANT_SYSTEM_PROMPT`

### 2. Bounded Subsystem Execution Map
| Business Domain Concept | Required Code Pattern (Must Exist) | Restricted Search Path (Sandbox) | Forbidden Traversal Paths |
| :--- | :--- | :--- | :--- |
| **"Execution Plausibility Gate"** | `ExecutionGuardrail.verify_order` | `src/execution/*` | `legacy/*`, `src/synthetic/*` |
| **"Daily Volatility Envelope"** | `VolatilityCalculator.compute_bands`| `src/math/volatility.py` | `tests/fixtures/*` |
| **"Quarantine Manager"** | `QuarantineLedger.archive_rejection` | `src/storage/quarantine.py` | Raw SQL `DELETE` calls |

> **AGENT ROUTING DIRECTIVE**: Do NOT invoke `grep_search` or `view_file` on paths outside `src/execution/*`, `src/math/volatility.py`, and `src/storage/quarantine.py`.

### 3. Mathematical Contracts
The proposed order execution price $P_{\text{exec}}$ must lie within the dynamic volatility band:
$$|P_{\text{exec}} - \text{EMA}_5| \le \max(3.0 \times \text{ATR}_{14}, \; 0.08 \times \text{EMA}_5)$$
Weekend and off-session orders must match Friday close within 1.0%:
$$\frac{|P_{\text{exec}} - P_{\text{Friday}}|}{|P_{\text{Friday}}|} \le 0.01$$

### 4. Boolean Acceptance Criteria
- `[BOOLEAN: TRUE]` Execution price $|P_{\text{exec}} - \text{EMA}_5| \le \max(3\text{ATR}_{14}, 0.08\text{EMA}_5)$.
- `[BOOLEAN: TRUE]` Spot price telemetry originates from `VERIFIED_PROVENANCE_ALLOWLIST` ($I_{01}$).
- `[BOOLEAN: FALSE]` Synthetic price imputation in exception handlers (e.g., `price or 200.0` is banned per ZM007).
- `[BOOLEAN: FALSE]` Raw SQL `DELETE` calls on failed executions (Invariant $I_{04}$).
- **Expected Return Contract**: `OrderAuthorizationVerdict(authorized=True, fill_limit=float, trace_id=UUIDv4)`.
- **Expected Failure Contract**: Reject order with `OrderAuthorizationVerdict(authorized=False, reason="REJECTED_EXECUTION_GUARDRAIL")`; archive to `quarantine_executions`.

---

## 🏥 Example 2: FDA Class III Medical Device Hemodynamic Safety Gate (`STORY-MED-402`)

### 1. Execution Metadata
- **Story ID**: `STORY-MED-402`
- **Epic ID**: `EPIC-CLIN-03`
- **Bounded Subsystem**: `src/clinical/titration_guardrail.py`
- **Max Token Budget**: `3,500 tokens`
- **Target File LOC**: `310 lines of code (Architectural Modularity Ceiling <= 400)`
- **Governing Invariants**: `I01, I02, I03, I04, I05, I07, I15`
- **Required Skill Level**: `EXPERT_EMBEDDED_SAFETY_SYSTEM_PROMPT`

### 2. Bounded Subsystem Execution Map
| Business Domain Concept | Required Code Pattern (Must Exist) | Restricted Search Path (Sandbox) | Forbidden Traversal Paths |
| :--- | :--- | :--- | :--- |
| **"Titration Guardrail"** | `TitrationSafetyGate.validate_titration`| `src/clinical/titration_guardrail.py` | `src/billing/*`, `src/export/*` |
| **"Arterial Catheter SQI"** | `ArterialSensor.get_signal_quality` | `src/sensors/arterial_line.py` | `tests/mocks/*` |
| **"Clinical Black Box"** | `ClinicalAuditLedger.archive_event` | `src/storage/clinical_quarantine.py` | Raw SQL `DELETE` calls |

### 3. Mathematical Contracts
The vasopressor dose adjustment $|\Delta R|$ is strictly bounded relative to patient baseline:
$$|\text{Rate}_{\text{exec}} - \text{Rate}_{\text{baseline}}| \le \max(3.0 \times \sigma_{\text{patient}}, \; 0.10 \times \text{Rate}_{\text{baseline}})$$
Absolute rate is hard-clamped to safe physiological limits:
$$\text{Rate}_{\text{exec}} \in [0.01, \; 0.50]\,\mu\text{g/kg/min}$$

### 4. Boolean Acceptance Criteria
- `[BOOLEAN: TRUE]` Arterial line Signal Quality Index (SQI) $\ge 0.85$ ($I_{01}$).
- `[BOOLEAN: TRUE]` Titration rate delta $|\Delta R| \le 0.05\,\mu\text{g/kg/min}$ per 5-minute interval ($I_{02}$).
- `[BOOLEAN: FALSE]` Maintaining high titration rates when telemetry drops for $> 15\text{ minutes}$ ($I_{05}$).
- `[BOOLEAN: FALSE]` Overwriting or deleting historical telemetry records ($I_{04}$).
- **Expected Return Contract**: `TitrationVerdict(authorized=True, approved_rate=float, trace_id=UUIDv4)`.
- **Expected Failure Contract**: Latch pump to baseline basal infusion rate, activate dual audible/visual alarms, and write sensor fault frame to `clinical_quarantine_ledger`.
