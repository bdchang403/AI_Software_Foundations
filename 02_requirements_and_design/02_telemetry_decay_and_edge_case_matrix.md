# Module 2: Temporal Telemetry Decay & The 20 Edge-Case Precondition Matrix

---

## 🎯 Executive Overview & The Adversarial Requirements Mindset

When human software engineers read a specification, they subconsciously infer unwritten assumptions. If a specification states *"Calculate the average transaction value"*, a human engineer instinctively adds a guard check to avoid division-by-zero if the transaction list is empty.

An autonomous AI agent possesses no such intrinsic instinct. An LLM optimizes strictly to satisfy the prompt explicit tokens while minimizing loss. If a boundary condition is omitted from a specification, the agent will either:
1. **Crash at runtime** when encountering unexpected edge cases (`ZeroDivisionError`, `KeyError`, `TypeError`).
2. **Implement silent "fail-soft" catch blocks** that return synthetic constants (e.g., `except Exception: return 0.50`), directly violating Invariant $I_{01}$ (Zero-Simulated-Data).
3. **Smuggle non-finite numerical types** (e.g., treating `NaN` as a valid float or evaluating `True` as numeric `1.0`), corrupting downstream databases.

In the **Context Factory**, the Requirements Lead (Business Analyst / Systems Engineer) must act as an **Adversarial Red-Teamer**. A requirement is not ready for implementation until all boundary conditions, temporal telemetry decay rules, and the **20 Pre-condition Boundary Edge Cases** are formally codified.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   THE REQUIREMENTS DEFENSE HIERARCHY                                             │
├────────────────────┬───────────────────────────────────┬─────────────────────────────────────────┤
│ Defense Layer      │ Mathematical Mechanism            │ Operational Objective                   │
├────────────────────┼───────────────────────────────────┼─────────────────────────────────────────┤
│ 1. Epistemic Gap   │ Unidirectional Normalizer         │ Strip promotional hype & script tags.   │
│ 2. Funnel Discount │ $W_{\text{comm}} = 0.20$ Discount │ Deflate commercial claims by 80%.       │
│ 3. Telemetry Decay │ $w(\Delta t) = w_0 (1/2)^{\Delta t/t_{1/2}}$ │ Attenuate stale evidence continuously.  │
│ 4. Edge-Case Matrix│ 20 Explicit Pre-conditions        │ Prevent runtime exception fallbacks.    │
└────────────────────┴───────────────────────────────────┴─────────────────────────────────────────┘
```

---

## ⏳ Temporal Telemetry Decay & The Four-Horizon Taxonomy

In mission-critical autonomous environments, requirements must account for temporal decay. Data does not remain fresh indefinitely. As elapsed time $\Delta t = t - t_0$ increases, the continuous decayed weight $w(\Delta t)$ is governed by the half-life decay formulation:

$$w(\Delta t) = w_0 \cdot \left(\frac{1}{2}\right)^{\frac{\Delta t}{t_{1/2}}} = w_0 \cdot \exp\left(-\frac{\ln 2}{t_{1/2}} \Delta t\right)$$

The effective integer confidence score utilized in downstream invariant gating is:

$$\text{effective-confidence}(\Delta t) = \mathrm{int}\left(\mathrm{round}\left(w_0 \cdot 2^{-\frac{\Delta t}{t_{1/2}}}\right)\right)$$

### The Four Operational Horizons
Requirements Leads must explicitly categorize all ingress telemetry into one of four operational horizons to prevent decisions based on stale inputs:

| Horizon Classification | Half-Life ($t_{1/2}$) | Hard Expiry ($2 \cdot t_{1/2}$) | Domain Telemetry: Healthcare (FDA SaMD) | Domain Telemetry: Core Banking |
| :--- | :--- | :--- | :--- | :--- |
| **1. Kinematic / Momentum** | $5.0\text{ days}$ (120 hrs) | $10.0\text{ days}$ | Acute hemodynamic pulse, continuous glucose rate | Foreign exchange intraday spot volatility |
| **2. Tactical Operational** | $7.0\text{ days}$ (168 hrs) | $14.0\text{ days}$ | 24-hour clinical fluid balance, body temperature | Interbank settlement queue depth, short-term repo |
| **3. Structural Solvency** | $21.0\text{ days}$ (504 hrs) | $42.0\text{ days}$ | Serum creatinine clearance ($Kt/V$), liver panels | Correspondent bank debt maturity, counterparty CDS |
| **4. Secular Quality** | $90.0\text{ days}$ (2,160 hrs) | $180.0\text{ days}$ | 90-day HbA1c trajectory, chronic dialysis status | 10-K audited cash flow, Tier-1 capital ratio |

When $\Delta t > 2 \cdot t_{1/2}$, the telemetry is **strictly expired**: the agent must discard the data point, fail closed, and request fresh observations.

---

## 💥 Forensic Case Study: Epistemic Priming & Panic Liquidation

The necessity of strict requirements air-gapping was demonstrated during **The Epistemic Priming Crisis**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        FORENSIC CRISIS AUTOPSY: EPISTEMIC PRIMING                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Upstream Test Stub Leak: Synthetic 5.25% interest rate stub was accidentally left active.     │
│ 2. Context Bleed: Internal risk panic leaked to an unstructured media ingestion agent.           │
│ 3. Cognitive Priming: The media agent ingested a sensationalist YouTube video titled             │
│    "Systemic Monetary Reset," evaluating it through its primed panic state.                      │
│ 4. Commercial Funnel Blindspot: Creator exaggerated macroeconomic panic to sell a $2,000 course. │
│ 5. Echo Chamber Feedback: Multi-agent debate cited the -9.0 media score as independent proof.    │
│ 6. Catastrophic Outcome: $150,000 of high-quality assets were liquidated hours before a blowout  │
│    earnings release triggered a +35% market rally.                                               │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### The Architectural Guardrails for Requirements:
1. **Unidirectional Epistemic Air-Gap Guardrail**: Ingress telemetry agents must never have access to internal account balances, portfolio holdings, or current system fear/greed states.
2. **The 80% Commercial Funnel Discount**: If an external telemetry payload includes commercial marketing funnels, affiliate links, or paid promotions (`commercial_conflict: true`), its reported sentiment and confidence are automatically discounted by 80%:

$$W_{\text{effective}} = W_{\text{raw}} \cdot W_{\text{commercial}} = W_{\text{raw}} \cdot 0.20$$
$$\text{Polarity}_{\text{stored}} = \mathrm{round}(\text{Polarity}_{\text{raw}} \cdot 0.20, \; 2)$$

---

## 🛡️ The 20 Pre-condition Boundary Edge-Case Matrix

Every Semantic Blueprint authored by a Requirements Lead must explicitly define the expected system behavior across all 20 canonical edge cases:

| # | Edge-Case Category | Specific Boundary Failure Condition | Mandatory Agent Behavior |
|---|---|---|---|
| 1 | **Empty Collection** | Ingress list/array has length 0 | Return empty collection; zero division avoided. |
| 2 | **Non-Finite Float** | Float evaluates to `NaN`, `+Inf`, or `-Inf` | Invariant $I_{01}$ trip; immediate execution halt. |
| 3 | **Negative Quantity** | Transfer amount, dosage, or price $\le 0$ | Reject transaction; log validation error. |
| 4 | **Temporal Expiry** | Telemetry timestamp $\Delta t > 2 \cdot t_{1/2}$ | Demote status to `EXPIRED`; request fresh telemetry. |
| 5 | **Future Timestamp** | Telemetry timestamp $> \text{now}() + 5\text{ min}$ | Clock drift detected; route to quarantine. |
| 6 | **Division by Zero** | Denominator evaluates to $0.0$ | Clamp to specified epsilon $\epsilon = 10^{-12}$. |
| 7 | **Missing Null Key** | Required dictionary key is `null` or missing | Strict JSON schema rejection; no fallback stubs. |
| 8 | **Type Coercion** | Ingress boolean `True` passed to numeric field | Reject payload; refuse silent numeric coercion. |
| 9 | **String Encoding** | Payload contains invalid UTF-8 or null bytes | Sanitize via standard codec; reject if malformed. |
| 10| **Rate Limit / 429**| Upstream API returns HTTP 429 / Throttled | Exponential backoff with jitter; zero synthetic data. |
| 11| **Database Timeout**| SQL execution exceeds timeout envelope | Abort transaction; rollback atomic state change. |
| 12| **Upper Plausibility**| Proposed action exceeds $\mu + 3.5\sigma$ band | Invariant $I_{02}$ clamp; reroute to dual custody. |
| 13| **Lower Plausibility**| Proposed action falls below physiological floor | Reject action; sound physical safety alarm. |
| 14| **Concurrent Mutation**| Optimistic locking version mismatch detected | Abort mutation; re-fetch latest state and retry. |
| 15| **Duplicate Ingress**| Webhook delivered twice with same UUIDv4 | Idempotent response; return cached execution receipt.|
| 16| **Extreme Matrix Cond**| Covariance matrix $\mathrm{cond}(\Sigma) > 10^{12}$ | Apply Ledoit-Wolf analytical shrinkage target. |
| 17| **Pillar Divergence**| Orthogonal pillars disagree ($\text{JSD} > 0.12$) | Activate Convex Log-Odds Evidence Solver. |
| 18| **Single Fatal Veto**| Fatal contagion sensor tripped ($I_{03}$) | Immediate veto; overrides all positive pillars. |
| 19| **Commercial Funnel**| Marketing links detected in unstructured text | Apply 80% Commercial Funnel Discount (\$0.20). |
| 20| **Schema Version Drift**| Ingress schema version mismatches registry | Reject payload; trigger automated drift alert. |

---

## 🏥 Dual-Use Regulated Industry Case Studies

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   ADVERSARIAL REQUIREMENTS CASE STUDIES                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   HEALTHCARE: FDA Class III Closed-Loop Titration System                                         │
│   • Edge Case Tested: Edge-Case 2 (Non-finite float) & Edge-Case 4 (Telemetry Expiry).           │
│   • Adversarial Probe: CGM sensor transmitter emitted NaN glucose after 30 minutes offline.      │
│   • Specification Requirement: System must fail closed, emit 0.0 Units basal, and sound nurse   │
│     pager alarm. Hard prohibition against interpolating missing readings with historical mean.   │
│   • Result: Zero clinical hypoglycemic events; objective design validation evidence satisfying 21 CFR 820.30(g) acceptance criteria. │
│                                                                                                  │
│   FINANCE: High-Value Core Banking Settlement Network                                            │
│   • Edge Case Tested: Edge-Case 12 (Upper Plausibility) & Edge-Case 15 (Duplicate Ingress).       │
│   • Adversarial Probe: Ingress wire message replayed twice with transfer value of \$250,000,000. │
│   • Specification Requirement: Idempotency deduplication via UUIDv4 cache; transaction value     │
│     diverted to human dual-custody hold due to exceeding account 3.5σ kinematic limit.           │
│   • Result: Bank protected against duplicate \$250M wire release; objective audit evidence supporting SOX Section 404 internal controls. │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Module Summary & Practical Next Step

Adversarial requirements engineering prevents autonomous agents from inventing dangerous fallbacks. By specifying temporal decay horizons and the 20 boundary edge cases, Requirements Leads establish deterministic guardrails for downstream builders.

[**Proceed to Module 3: Feature-Level Decomposition & Bounded Subsystems →**](./03_feature_slicing_and_confluence.md)
