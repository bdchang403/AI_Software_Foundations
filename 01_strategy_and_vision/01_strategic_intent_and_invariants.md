# Module 1: Strategic Intent Directives & Invariant Governance

## 🎯 The Failure of Traditional User Stories in the AI Era

In classical agile development, the standard template:
> *"As a [user role], I want [feature], so that [business benefit]."*

relies heavily on human commonsense, unwritten institutional conventions, and implicit context. When an autonomous AI builder receives this open-ended instruction, it interprets the task probabilistically based on internet-scale training weights. Without explicit negative constraints, the AI will:
1. **Invent unvetted dependencies** (e.g., importing external packages that breach security policies or licensing terms).
2. **Implement silent "fail-soft" catch blocks** that return synthetic constants (e.g., `0.50` or `200.0`), directly violating Invariant $I_{01}$.
3. **Trigger uncontrolled scope expansions**, modifying unrelated database schemas or deleting legacy handlers to force compilation.

To achieve deterministic execution in high-stakes regulated enterprises, Strategy Leads and Product Owners must replace conversational prompts with **3-Part Directives with Invariant Bindings**.

---

## 📐 Anatomy of the 3-Part Directive

Every strategic directive delivered to downstream autonomous agents consists of three mathematically grounded components:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               THE 3-PART DIRECTIVE                                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. ROLE: Persona, Epistemic Scope, and Domain Tool Boundary                            │
│    "You are the [Domain Service / Agent]. Your toolset is strictly isolated to [...]"   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. TASK: Deterministic Functional Transformation                                       │
│    "Ingest [Verified Input Type X]. Transform via [Algorithm Y]. Emit [Output Type Z]."│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. CONSTRAINT: Invariant Bindings & Negative Boundary Conditions                       │
│    "Must satisfy Canonical Invariants [I_xx, I_yy]. Banned behaviors: [...]"            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

### 1. Role (Epistemic Allowlist & Bounded Identity)
Defines the agent's exact operational persona and enforces Role-Based Epistemic Slicing Guardrail. The agent is explicitly informed of what data it may observe and what tools it is permitted to invoke. It is strictly denied access to out-of-scope domain state to prevent cognitive priming.

### 2. Task (Deterministic Functional Transformation)
Specifies the input data contract, the mathematical or algorithmic operation to perform, and the exact output schema. Vague adjectives (*"user-friendly"*, *"fast"*, *"robust"*) are prohibited; only typed specifications and deterministic criteria are accepted.

### 3. Constraint & Invariant Binding (Constitutional Locks)
The non-negotiable architectural boundaries. Every directive binds to specific Canonical Invariants ($I_{01}-I_{22}$) and explicitly enumerates negative boundary conditions (what the AI must *never* do).

---

## 🔗 The Canonical Invariant Strategic Binding Matrix

When authoring strategic directives, the Strategy Lead binds business requirements directly to the system's 22 Invariants:

| Invariant | Name | Strategic Intent & Governance Rule | Target Regulated Domain |
| :--- | :--- | :--- | :--- |
| **$I_{01}$** | **Zero-Simulated-Data** | Banish all synthetic mock fallbacks in runtime code. If live data is unavailable, fail closed immediately. | Fintech (Live Prices) / MedTech (Vital Signs) |
| **$I_{02}$** | **Execution Guardrails** | Enforce pre-action plausibility bands: $\lVert V_{\text{exec}} - \text{Baseline} \rVert \le \text{Band}$. Halt out-of-bound executions. | Trading (Slippage) / Infusion Pumps (Dose Limit) |
| **$I_{03}$** | **Fatal-Contagion Veto** | Critical risk metrics (e.g., bankruptcy risk, toxic sensor readings) trigger an immediate, unilateral halt. | Credit Solvency / Toxic Biomarker Overdose |
| **$I_{04}$** | **Immutable Quarantine** | Raw `DELETE` operations are strictly banned. Invalid or corrupted data must be archived to an audit ledger. | Audit Compliance (SR 11-7, 21 CFR Part 11) |
| **$I_{05}$** | **Closed-World Fallback** | When telemetry is degraded, emit a closed-world schema with missing attributes explicitly flagged as `UNAVAILABLE`. | Degraded Sensor Telemetry / Network Partitions |
| **$I_{07}$** | **Div-by-Zero Safety** | All denominator terms must be clamped or checked. Log/sqrt operations must assert domain non-negativity. | Risk Analytics / Medical Dosing Calculations |
| **$I_{18}$** | **Compounder Hold Lock** | Enforce minimum time-in-state windows (e.g., 20 trading days or therapeutic course completion) to stop churn. | Asset Management / Pharmacokinetic Regimens |
| **$I_{20}$** | **Epistemic News Isolation** | Unstructured external media must be ingested behind a unidirectional air-gap with an 80% commercial discount. | Market Sentiment / Clinical Trial Literature |
| **$I_{22}$** | **Modularity & Test Hygiene** | All implementation modules must adhere to Architectural Modularity Heuristics (target $\le 400$ LOC per Single Responsibility Principle) and embed verifiable SHA1 invariant anchors. | Software Engineering Architecture |

---

## 🔬 Comparative Domain Examples

### Example 1: Quantitative Finance (Order Execution Routing)

#### Traditional Flawed Story:
> *"As a trader, I want an automated order routing service that executes orders at the best available market price across connected exchanges."*
>
> **Failure Mode**: The AI agent writes an execution script that falls back to a hardcoded synthetic price when exchange APIs timeout (`except: price = 200.0`), orders during wide bid-ask spreads during market opens, and deletes audit logs on order failure.

#### Strategic 3-Part Directive:
```markdown
### 3-Part Directive: Smart Order Router (SOR-101)
- **Role**: You are the Low-Latency Smart Order Execution Service. Your access is restricted to verified Level 1 exchange feeds and the live execution order gateway.
- **Task**: Ingest live market quotes for target ticker $T$. Check liquidity across venues $V_1, V_2, V_3$. Compute VWAP-optimal slice size. Route child orders if and only if execution conditions are met.
- **Constraint**: 
  1. Enforce Invariant $I_{01}$ (Zero-Simulated-Data): If any venue feed emits stale timestamps (>250ms) or null prices, drop the venue; do not impute prices.
  2. Enforce Invariant $I_{02}$ (Execution-Price Guardrail): Assert that $|P_{\text{exec}} - \text{EMA}_5| \le \max(3\text{ATR}_{14}, 0.08\text{EMA}_5)$. Reject orders violating the band.
  3. Enforce Invariant $I_{04}$ (Immutable Quarantine): All rejected or failed executions must write full payload states to `execution_quarantine_ledger`. Hard deletes are forbidden.
```

---

### Example 2: FDA Class III Medical Device (Closed-Loop Vasopressor Infusion)

#### Traditional Flawed Story:
> *"As an ICU intensivist, I want an automated infusion controller that adjusts norepinephrine titration to maintain patient Mean Arterial Pressure (MAP) at 65 mmHg."*
>
> **Failure Mode**: The AI agent implements a simple PID controller with positive default feedback. When an arterial line probe slips (reading MAP = 0), the controller infuses maximum vasopressor, inducing catastrophic ischemic stroke.

#### Strategic 3-Part Directive:
```markdown
### 3-Part Directive: Hemodynamic Titration Controller (HTC-301)
- **Role**: You are the Closed-Loop Hemodynamic Infusion Controller. Your input is restricted to dual-channel arterial catheter telemetry; your output connects strictly to the mechanical stepper motor interface.
- **Task**: Read arterial line blood pressure waveforms at 100 Hz. Extract MAP across a 10-second sliding window. Calculate titration delta $\Delta R$ to converge on target MAP $65\,\text{mmHg}$.
- **Constraint**:
  1. Enforce Invariant $I_{01}$ (Zero-Simulated-Data): Arterial catheter signal-quality index (SQI) must exceed 0.85. If SQI drops, fail closed: lock titration rate at baseline basal infusion and emit audible alert. Zero metric extrapolation permitted.
  2. Enforce Invariant $I_{02}$ (Execution Guardrail): Max dose change $|\Delta R| \le 0.05\,\mu\text{g/kg/min}$ per 5-minute interval. Absolute rate capped at $0.50\,\mu\text{g/kg/min}$.
  3. Enforce Invariant $I_{07}$ (Div-by-Zero Safety): All resistance index equations ($R = \Delta P / Q$) must assert cardiac output $Q > 0.5\,\text{L/min}$.
  4. Enforce Invariant $I_{04}$ (Immutable Quarantine): Invalidate erratic catheter telemetry into the `sensor_quarantine_log`; do not overwrite historical telemetry records.
```

---

## 🛠️ Practical Exercises

### Exercise 1: Refactoring an Ambiguous Strategic Directive
You are the Product Owner for an Aerospace Flight Management System. The executive committee submits the following requirement:
> *"Implement an autonomous angle-of-attack (AoA) stabilizer to prevent aerodynamic stalls during high-altitude climb."*

**Your Task**: Refactor this requirement into a rigorous 3-Part Directive:
1. Define the isolated **Role** and allowable sensors.
2. Formulate the deterministic **Task** transformation.
3. Bind the directive to Canonical Invariants ($I_{01}, I_{02}, I_{03}, I_{05}$) and specify negative boundaries.

#### Reference Solution:
*   **Role**: Autonomous Flight Envelope AoA Trim Controller. Bounded to dual calibrated left/right AoA vanes and digital flight data recorder.
*   **Task**: Ingest dual AoA vane angles $(\theta_{\text{left}}, \theta_{\text{right}})$ and indicated airspeed $V_{\text{IAS}}$ at 50 Hz. Compute aerodynamic stall margin. Adjust horizontal stabilizer trim actuator $\Delta \alpha_{\text{trim}}$ when stall margin $< 15\%$.
*   **Constraint**:
    *   Bind to $I_{01}$ / $I_{05}$: If sensor delta $|\theta_{\text{left}} - \theta_{\text{right}}| > 5.0^\circ$, declare telemetry degraded; do not average contradictory sensors; fail closed to pilot manual trim.
    *   Bind to $I_{02}$: Maximum actuator deflection rate limited to $|\dot{\alpha}_{\text{trim}}| \le 0.25^\circ/\text{sec}$; absolute deflection capped at $\pm 2.5^\circ$.
    *   Bind to $I_{03}$: Autotrim immediately disengages if pilot applies contrary yoke stick force $> 15\,\text{lbf}$.
