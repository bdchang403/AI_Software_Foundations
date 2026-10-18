# Strategy Lead Lab Workbook: Shaping Strategic Intent & Epistemic Bounding

Welcome to the Strategy Lead & Product Owner Lab. In the enterprise Context Pipeline, your responsibility is **Decomposition, Epistemic Bounding, and Invariant Governance**. If you supply a monolithic, ambiguous, or un-gated Epic into the context factory, downstream autonomous agents will experience attention degradation, hallucinate synthetic data, and introduce catastrophic risk.

This workbook contains three rigorous practical labs designed to train Product Owners and Strategy Leads in high-stakes autonomous engineering.

---

## 🧪 Lab 1: Epic Decomposition & Token Budgeting (Module 3)

### The Scenario
Enterprise leadership issues a high-priority mandate:
> *"Build an automated real-time patient monitoring and hemodynamic stabilization service that detects septic shock, calculates optimal norepinephrine titration, alerts on-call ICU physicians, and files automated billing claims."*

If fed directly to an AI builder agent, the agent will attempt to ingest hospital billing databases, vital sign streaming buses, drug calculation libraries, and alerting protocols simultaneously. This monolithic blast radius exceeds 200,000 tokens, placing the core clinical logic in the "Lost in the Middle" degradation valley ($F(x) \approx 0.35$) and risking lethal drug titration errors.

### Your Task
1. Decompose the monolithic mandate into four strictly bounded Epics that share zero mutable state.
2. Ensure each Epic requires $< 15,000$ tokens of context and each user story has a blast radius $< 4,000$ tokens.
3. Assign governing Invariants ($I_{01}, I_{02}, I_{03}, I_{04}, I_{16}, I_{20}$) to each slice.

### Answer Key (Compare Your Work)

| Epic ID | Bounded Subsystem Scope | Max Token Budget | Governing Invariants | Negative Boundary Constraint |
| :--- | :--- | :--- | :--- | :--- |
| **EPIC-CLIN-01** | **Bedside Arterial Waveform Ingestion** | 12,000 tokens | $I_{01}$ (Zero Mock), $I_{16}$ (Patient Isolation) | Cannot query billing or physician scheduling databases. |
| **EPIC-CLIN-02** | **Hemodynamic Sepsis Risk Evaluator** | 8,000 tokens | $I_{02}$ (Plausibility Band), $I_{07}$ (Div-by-Zero) | Cannot issue automated infusion rate changes directly. |
| **EPIC-CLIN-03** | **Closed-Loop Vasopressor Titration Stepper** | 6,000 tokens | $I_{02}$ (Dose Limiter), $I_{03}$ (Fatal Veto) | Titration changes capped at $|\Delta R| \le 0.05\,\mu\text{g/kg/min}$. |
| **EPIC-CLIN-04** | **Sepsis Audit & Immutable Quarantine Ledger** | 5,000 tokens | $I_{04}$ (Zero Hard-Deletes), $I_{15}$ (UUID Trace) | Raw `DELETE` statements prohibited; all edits append-only. |

---

## 🧪 Lab 2: Epistemic Air-Gap & 80% Commercial Discount (Module 4)

### The Scenario
You are building an intelligence aggregator for executive decision-makers. The system ingests an external financial newsletter and a sponsored medical vendor whitepaper:
- **Source A**: A viral investment blog publishes an article: *"Total Economic Collapse Ahead: Why Gold Will Surge 500%"*. The author includes affiliate links to purchase gold bullion from a retail dealer (`commercial_conflict: true`). Raw extracted polarity is $\text{Polarity}_{\text{raw}} = -8.50$. Author's baseline Brier score is $W_{\text{Brier}} = 0.60$.
- **Source B**: A medical device vendor publishes a whitepaper: *"Revolutionary ICU Sensor Slashes Sepsis Mortality by 80%"*. The whitepaper promotes the vendor's proprietary catheter (`commercial_conflict: true`). Raw reported efficacy score is $+9.20$. Vendor baseline credibility weight is $0.75$.

### Your Task
1. Calculate the stored polarity $\text{Polarity}_{\text{stored}}$ and effective weight $W_{\text{eff}}$ for both sources using the mathematical discount formulas:
   $$W_{\text{eff}} = W_{\text{Brier}} \times W_{\text{commercial}} = W_{\text{Brier}} \times 0.20$$
   $$\text{Polarity}_{\text{stored}} = \text{round}(\text{Polarity}_{\text{raw}} \times 0.20, \; 2)$$
2. Write the negative constraint preventing cognitive priming of the downstream decision solver.

### Answer Key (Compare Your Work)

#### Calculations:
- **Source A (Gold Newsletter)**:
  $$\text{Polarity}_{\text{stored}} = \text{round}(-8.50 \times 0.20, \; 2) = \mathbf{-1.70}$$
  $$W_{\text{eff}} = 0.60 \times 0.20 = \mathbf{0.12}$$
- **Source B (Medical Vendor Whitepaper)**:
  $$\text{Polarity}_{\text{stored}} = \text{round}(+9.20 \times 0.20, \; 2) = \mathbf{+1.84}$$
  $$W_{\text{eff}} = 0.75 \times 0.20 = \mathbf{0.15}$$

#### Negative Boundary Constraint:
```markdown
CONSTRAINT: Unidirectional Epistemic Air-Gap Guardrail Active.
Under no circumstances may the media extractor query internal portfolio risk limits, 
unrealized PnL, or hospital clinical mortality baselines.
All sources flagged with commercial_conflict: true MUST apply the 80% discount factor.
Phrasing asserting that external claims "confirm internal models" triggers a validation error.
```

---

## 🧪 Lab 3: Authoring an Epic Semantic Blueprint (Module 4)

### The Scenario
You are the Strategy Lead for a multi-asset algorithmic execution engine. You are authorizing `EPIC-EXEC-02`: *"Automated Execution Guardrail & Plausibility Verification"*.

### Your Task
Draft a complete, machine-ingestible **Epic Semantic Blueprint** including:
1. Epic metadata, token budget ($\le 3,500$ tokens), and bounded subsystems.
2. Governing Invariants ($I_{01}, I_{02}, I_{04}, I_{15}$).
3. Negative boundary assertions banning mock data fallbacks, synthetic prices, and raw record deletion.

### Answer Key (Compare Your Work)

```markdown
# Epic Semantic Blueprint: Execution Plausibility Guardrails (EPIC-EXEC-02)

## 1. Epic Metadata
- **Epic ID**: `EPIC-EXEC-02`
- **Bounded Subsystem**: `01_strategy_and_vision`, `02_requirements_and_design`
- **Max Token Budget**: `3,500 tokens`
- **Governing Invariants**: `I01, I02, I04, I15`

## 2. Inbound / Outbound Contracts
- **Inbound Trigger**: Proposed execution order payload `ExecutionOrder(ticker, shares, proposed_price, timestamp)`
- **Outbound Verdict**: `AuthorizationVerdict(authorized: bool, execution_limit: float, reason: str, trace_id: UUIDv4)`

## 3. Mathematical Guardrail Specification (Invariant I02)
- The execution price $P_{\text{exec}}$ must be bounded by the 5-day EMA and 14-day ATR:
  $$|P_{\text{exec}} - \text{EMA}_5| \le \max(3.0 \times \text{ATR}_{14}, \; 0.08 \times \text{EMA}_5)$$
- If the trade occurs during a weekend or holiday session, the execution price must match Friday close within 1.0%:
  $$\frac{|P_{\text{exec}} - P_{\text{Friday}}|}{|P_{\text{Friday}}|} \le 0.01$$

## 4. Constitutional Negative Assertions
- Invariant $I_{01}$ (Zero-Simulated-Data): Banish all numeric fallback constants in exception handlers (`except Exception: return 200.0` is strictly prohibited). If live market data fails, return `authorized = False, reason = "UNAVAILABLE"`.
- Invariant $I_{04}$ (Immutable Quarantine): All rejected or failed executions must write full diagnostic payloads to `quarantine_executions` table with an audit reason and timestamp. Raw SQL `DELETE` calls are permanently banned.
- Invariant $I_{15}$ (UUID Traceability): Every verdict must include a valid UUIDv4 trace identifier linked to Cloudflare D1 telemetry logs.
```
