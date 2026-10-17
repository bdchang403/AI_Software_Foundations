# Module 2: Adversarial Thinking & The 20 Pre-condition Boundary Edge-Case Matrix

## 🛡️ The Adversarial Requirements Mindset

When human software engineers read a specification, they subconsciously infer unwritten assumptions. If a specification states *"Calculate the average transaction value"*, a human engineer instinctively adds a check to avoid division-by-zero if the transaction list is empty.

An autonomous AI agent possesses no such intrinsic instinct. The AI optimizes strictly to satisfy the prompt's explicit tokens while minimizing computational loss. If a boundary condition is omitted from the specification, the AI will either:
1. **Crash at runtime** when encountering edge cases (e.g., `ZeroDivisionError`, `KeyError`, `IndexError`).
2. **Implement silent "fail-soft" catch blocks** that return synthetic constants (e.g., `except Exception: return 0.50`), contaminating downstream analytics.
3. **Smuggle corrupt data types** (e.g., treating `True` as numeric `1.0` or propagating `NaN` through mathematical matrices).

In the Context Factory, the Business Analyst must act as an **Adversarial Red-Teamer**. A requirement is incomplete until the BA has systematically defined all **20 Pre-condition Boundary Edge Cases**.

---

## 💥 Forensic Crisis Integration: Case Study 5 — Epistemic Priming & Panic Liquidation

The catastrophic power of unconstrained context and missing requirements boundaries was demonstrated in **Case Study 5: The Epistemic Priming & Liquidation Incident (October 2026)**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        CASE STUDY 5: THE FORENSIC ANATOMY                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Upstream Test Stub Leak: Synthetic 5.25% Fed funds rate injected into pipeline.     │
│ 2. Omniscient Context Hydration: Macro panic leaked to unstructured media extractor.   │
│ 3. Cognitive Priming: Extractor analyzed a YouTube video ("Monetary Reset") through    │
│    its primed panic, concluding creator "independently verifies our crash thesis."     │
│ 4. Commercial Funnel Blindspot: Creator exaggerated a 25 bps rate cut to sell a        │
│    $2,000 retail trading mentorship course.                                            │
│ 5. Circular Corroboration Loop: Multi-agent debate cited the -9.0 polarity as          │
│    "independent market confirmation," maximizing bear conviction.                      │
│ 6. Catastrophic Outcome: $150k in core TSLA shares liquidated into SGOV cash           │
│    equivalents hours before a blowout earnings report sparked a +35% rally.            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Root Cause Analysis for Requirements Engineers

1. **Unbounded Context Leaks**: The system architecture allowed unstructured media extractors to read internal operational context. The extractor was aware of internal macro risk alarms and portfolio drawdowns. This induced **Cognitive Priming**: the LLM interpreted ambiguous narrative claims as confirmation of its internal panic.
2. **Commercial Funnel Ignorance**: The specification lacked rules to detect and discount monetized marketing funnels. The YouTube creator had an overt commercial conflict: exaggerating systemic collapse to sell an expensive day-trading mentorship course.
3. **Circular Corroboration**: The downstream multi-agent debate triad treated the primed media score as an orthogonal, independent data point. This created an echo chamber where internal fear was reflected back as external validation.

### Attempted False Solutions

- ❌ **Prompt Disclaimers**: Adding prompt instructions like *"Ignore marketing hype and evaluate objectively"* failed completely; neural attention still concentrated on high-salience alarmist tokens.
- ❌ **Media Blackout**: Completely cutting off external social media blinded the system to viral product inflections, causing severe underperformance on growth compounders.
- ❌ **Keyword Blacklists**: Attempting to block alarmist words (*"Crash"*, *"Depression"*, *"Reset"*) resulted in endless regex chasing as creators adopted new euphemisms.

### Permanent Architectural Mechanisms (ADR-030 & ADR-044)

The crisis resulted in two binding architectural standards that every BA must incorporate into requirements:

1. **ADR-030 Unidirectional Epistemic Air-Gap**: Unstructured media extractors must be air-gapped from internal operational state. The extractor has zero visibility into portfolio holdings, unrealized PnL, or macro risk levels. It acts strictly as an objective courtroom transcriber, classifying claims into `OBSERVED_CLAIM` versus `GROUND_TRUTH_FACT`.
2. **The 80% Commercial Funnel Discount**: If an unstructured source contains commercial affiliate links, course promotions, or monetized funnels (`commercial_conflict: true`), its polarity and creator Brier weight are automatically slashed by 80%:
   $$W_{\text{eff}} = W_{\text{Brier}} \times W_{\text{commercial}} = W_{\text{Brier}} \times 0.20$$
   $$\text{Polarity}_{\text{stored}} = \text{round}(\text{Polarity}_{\text{raw}} \times 0.20, \; 2)$$
3. **ADR-044 Role-Based Epistemic Slicing**: System context is partitioned into disjoint allowlists, preventing cross-domain contamination.

---

## 📋 The Systematic 20 Pre-condition Boundary Edge-Case Matrix

Every requirement and Semantic Blueprint authored by a Business Analyst must explicitly define the expected system behavior across these 20 canonical edge cases:

| # | Edge Case Category | Input Pre-condition Boundary | Required Deterministic Behavior | Governing Invariant |
|---|---|---|---|---|
| **1** | **Empty Input** | Empty list or null collection passed to analytical function (e.g., `[]`). | Return `None` or typed empty DTO; raise domain exception if required. Never return synthetic defaults like `0.50`. | $I_{01}$ (Zero-Mock) |
| **2** | **Negative Values** | Negative price, volume, dose, or absolute time (e.g., `price = -12.50`). | Fail closed: reject payload; log anomaly to quarantine ledger. Assert domain non-negativity. | $I_{01}, I_{04}$ |
| **3** | **Division-by-Zero** | Zero denominator in ratio or metric calculation (e.g., `margin / 0.0`). | Explicitly guard denominator; return defined fallback or clamp value. Never propagate `ZeroDivisionError` or Inf. | $I_{07}$ (Div-by-Zero) |
| **4** | **NaN Smuggling** | IEEE-754 `float('nan')` injected into numerical calculation payload. | Trap via `math.isfinite()`; reject payload immediately. Never allow NaN to propagate through matrices. | $I_{01}, I_{11}$ |
| **5** | **Inf Smuggling** | IEEE-754 `float('inf')` or `-float('inf')` injected into feature vector. | Trap via `math.isfinite()`; clamp to domain extrema or reject payload with audit log. | $I_{01}, I_{06}$ |
| **6** | **Boolean Smuggling** | Python boolean `True` or `False` injected where a float is expected. | Reject via `isinstance(val, bool)`; do not allow boolean coercion to `1.0` or `0.0`. | $I_{01}$ (Zero-Mock) |
| **7** | **Out-of-Order Timestamps**| Streaming telemetry packet arrives with timestamp earlier than current state ($t < t_{\text{last}}$).| Reject inverted timestamp packet; log to sequence anomaly audit table. Do not corrupt time-series order. | $I_{13}, I_{15}$ |
| **8** | **Stale Telemetry** | Telemetry timestamp exceeds maximum freshness threshold (e.g., $> 24\text{ hours}$ old). | Trigger stale data circuit breaker; mark status as `STALE_TELEMETRY`; do not process live execution. | $I_{13}, I_{17}$ |
| **9** | **Clock Skew** | Telemetry timestamp is $> 5\text{ minutes}$ in the future relative to server UTC clock. | Reject future-dated packet; raise `ClockSkewDetectedError`; quarantine payload. | $I_{13}, I_{15}$ |
| **10**| **Missing Required Keys** | JSON payload lacks mandatory schema attributes (e.g., missing `trace_id`). | Schema validation error; reject payload at boundary; do not infer or default missing keys. | $I_{05}, I_{15}$ |
| **11**| **Unexpected String Injection**| String injected where numerical metric is expected (e.g., `"200.0"` or `"N/A"`). | Strict type parsing; reject un-coerced strings; fail closed if invalid. | $I_{01}$ (Zero-Mock) |
| **12**| **Extreme Outlier / Spike** | Input value deviates by $> 10\sigma$ from rolling historical baseline. | Pre-action plausibility check fails; halt execution; require secondary confirmation. | $I_{02}$ (Plausibility Band) |
| **13**| **Weekend / Holiday Drift** | Execution attempted during market close or maintenance window. | Reject execution (`REJECTED_SESSION_CLOSED`); assert deviation $\le 1.0\%$ from last session close. | $I_{02}, I_{19}$ |
| **14**| **Simulated Data Sentinel** | Payload contains banned sentinel values (e.g., `5.25%`, `0.50`, `200.0`, `MOCK_`). | AST scanner and runtime breaker trap sentinel; halt execution with `HALT_UNVERIFIED_DATA`. | $I_{01}$ (Zero-Mock) |
| **15**| **Commercial Funnel Conflict**| External unstructured source contains affiliate links or course promotions. | Flag `commercial_conflict: true`; slash polarity by 80% ($W_{\text{commercial}} = 0.20$). | $I_{20}$ (Epistemic Air-Gap) |
| **16**| **Database Lock Contention** | Concurrent transaction attempts trigger database lock timeout (e.g., SQLite lock). | Enforce WAL mode; implement exponential backoff with 30s busy timeout; fail closed if unrecovered. | $I_{13}$ (Remote-First) |
| **17**| **Duplicate Trace ID** | Inbound request arrives with a previously processed UUIDv4 trace identifier. | Reject duplicate request (`DUPLICATE_IDEMPOTENCY_VIOLATION`); do not re-execute side effects. | $I_{15}$ (UUID Trace) |
| **18**| **Multi-Entity Contamination**| Batch loop leaks state of entity $A$ into entity $B$ evaluation context. | Assert $\text{State}(A) \cap \text{State}(B) = \emptyset$; instantiate fresh execution sandbox per entity. | $I_{16}$ (Multi-Entity Isolation) |
| **19**| **All-Tiers Network Down** | All upstream API providers fail or rate-limit (Tier 1, Tier 2, Tier 3 down). | Enter terminal fail-closed sink: return `{"status": "UNAVAILABLE", "data": None}`. Never invent mocks. | $I_{01}, I_{05}$ |
| **20**| **Corrupted State / Mutation**| Historical ledger row is flagged as corrupted, tampered, or invalidated by bug. | Archive row to immutable quarantine table with non-null reason; never execute raw SQL `DELETE`. | $I_{04}$ (Immutable Quarantine) |

---

## 🔬 Dual-Use Regulated Callout Boxes

### Callout 1: Real-Time Algorithmic Trading Safeguards
In an automated trade execution gateway, edge cases #3, #4, #8, #12, and #13 are mission-critical:
- **Edge Case #4 (NaN Smuggling)**: An upstream vendor API returns `{"last_price": "NaN"}` following an exchange trading halt. If parsed naively into a portfolio optimizer, `NaN` propagates through the covariance matrix $\Sigma$, causing matrix inversion routines to emit corrupt infinite weights. The BA specifies:
  ```python
  if not math.isfinite(quote.last_price):
      raise InvalidPriceTelemetryError(f"Non-finite price detected: {quote.last_price}")
  ```
- **Edge Case #12 (Extreme Outlier / Flash Crash)**: A glitch order prints at $0.01 on a $200 stock. The pre-trade plausibility band ($I_{02}$) catches the deviation:
  $$|P_{\text{exec}} - \text{EMA}_5| = |0.01 - 200.00| = 199.99 > \max(3\text{ATR}_{14}, 0.08\text{EMA}_5)$$
  The order is instantly rejected with code `REJECTED_EXECUTION_GUARDRAIL`.

### Callout 2: FDA Class III Medical Device Decision Pipeline
In an automated closed-loop intravenous drug delivery system, edge cases #1, #6, #7, #8, and #19 safeguard patient lives:
- **Edge Case #6 (Boolean Smuggling)**: A corrupt telemetry sensor packet sends `{"sensor_ok": True}` in place of `glucose_mg_dl: float`. If language runtime coerces `True` to `1.0`, the system calculates extreme hypoglycemia ($1.0\,\text{mg/dL}$) and administers a fatal intravenous glucagon bolus. The BA blueprint explicitly commands:
  ```python
  if isinstance(payload["glucose_mg_dl"], bool) or not isinstance(payload["glucose_mg_dl"], (int, float)):
      fail_closed_to_basal(reason="TYPE_COERCION_ATTEMPT_DETECTED")
  ```
- **Edge Case #8 (Stale Telemetry)**: If continuous glucose monitor readings stop updating due to wireless RF attenuation in the ICU, the pump must not maintain high titration rates. At $\Delta t > 15\text{ minutes}$, the pump auto-transitions to the fail-closed safe basal rate ($I_{05}$).

### Callout 3: Aerospace Fly-by-Wire Avionics (DO-178C Level A)
In a digital flight control computer, edge cases #7, #9, #18, and #20 govern flight safety:
- **Edge Case #7 (Out-of-Order Timestamps)**: A delayed CAN bus packet arrives out of sequence. If processed, it would cause the actuator to snap to a previous pitch angle, inducing severe structural g-load oscillations. The BA blueprint requires monotonic timestamp sequencing:
  $$t_{\text{packet}} > t_{\text{last\_processed}} \implies \text{Process}, \quad \text{else} \implies \text{Discard with Bus Anomaly Log}$$
