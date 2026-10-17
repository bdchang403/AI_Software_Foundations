# Module 4: Semantic Context Engineering & Closed-World Schemas

## 🧠 Writing the AI's "Search and Routing Algorithm"

In a 500,000-line enterprise repository, an autonomous AI agent does not understand abstract business terminology. If a requirement states:
> *"Retrieve the customer's account balance and verify transaction risk before approving the order,"*

the AI has no inherent knowledge of where "account balance" resides. If the codebase contains both legacy systems (`legacy/billing/user_acc.py`) and modern event-driven microservices (`src/ledger/account_balance.py`), the AI will guess. In doing so, it frequently links against obsolete endpoints, breaks database normalization, or invents its own mock tables.

In the Context Factory, the Business Analyst authors the **Semantic Context Map**. You do not merely state *what* business rule to execute; you explicitly define the **AST Search Boundaries, Domain Paths, and Sandbox Fences**.

---

## 🗺️ The Explicit Semantic Mapping Table

The core of every Context-Enriched Semantic Blueprint is the **Bounded Subsystem Execution Map**. This table maps human business concepts directly to technical codebase coordinates:

| Business Domain Term | Canonical Implementation Path (Must Exist) | Restricted Search Sandbox | Forbidden Traversal Paths |
| :--- | :--- | :--- | :--- |
| **"Order Execution Guardrail"** | `src/execution/guardrails.py` | `src/execution/*` | `legacy/*`, `tests/fixtures/*` |
| **"Execution Price Discovery"** | `src/pricing/waterfall.py` | `src/pricing/*` | `src/synthetic/*`, `scripts/mocks/*` |
| **"Quarantine Persistence"** | `src/storage/quarantine_manager.py` | `src/storage/*` | Raw SQL `DELETE` calls |
| **"Patient Hemodynamic State"** | `src/clinical/arterial_monitor.py` | `src/clinical/*` | `src/billing/*`, `src/ehr_export/*` |

> **AGENT ROUTING DIRECTIVE**: Autonomous agents reading this blueprint are contractually forbidden from executing tools (`grep_search`, `view_file`, `find_by_name`) outside the Restricted Search Sandbox. If a required dependency is missing from the sandbox, the agent must halt and request clarification from the Requirements Lead.

---

## 🔒 The Closed-World Fallback Doctrine (Invariant $I_{05}$)

One of the most dangerous failure modes in autonomous engineering is the "fail-soft" fallback. When an external API times out or a database query fails, traditional web developers often write code that returns synthetic default values (e.g., returning `0.50` for missing dark pool ratio, or `5.25%` for missing interest rates). As proved in Crisis 3, this practice poisoned 900,000 database rows and triggered a $150k panic liquidation.

Under **Invariant $I_{05}$ (Closed-World Fallback)**, the Business Analyst mandates a **Strict Closed-World Schema**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        INVARIANT I05: CLOSED-WORLD FALLBACK SCHEMA                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ When external data feeds or remote databases fail:                                     │
│ 1. Zero Synthetic Imputation: Do NOT generate artificial numeric values or defaults.   │
│ 2. Explicit UNAVAILABLE Sentinel: Flag all missing data fields as "UNAVAILABLE".       │
│ 3. Structural BUY Block: Recommendation is forced to WATCH (Confidence = 40%).        │
│ 4. Hard Veto Active: BUY recommendations are structurally blocked under Invariant I03. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### JSON Schema Contract for Closed-World Telemetry:

```json
{
  "ticker": "AAPL",
  "spot_price": 224.50,
  "spot_provenance": "FMP_REALTIME_VERIFIED",
  "telemetry_status": "DEGRADED_CLOSED_WORLD",
  "pillars": {
    "quality_metrics": "UNAVAILABLE",
    "residual_momentum": "UNAVAILABLE",
    "network_diffusion": "UNAVAILABLE",
    "smart_flow": "UNAVAILABLE"
  },
  "guardrail_verdict": {
    "status": "WATCH",
    "confidence": 40,
    "buy_blocked": true,
    "reason": "UPSTREAM_BUNDLE_TIMEOUT_CLOSED_WORLD_ACTIVE"
  }
}
```

---

## 🔬 Dual-Use Regulated Callout Boxes

### Callout 1: Real-Time Algorithmic Trading Safeguards
In financial market trading, if market data bundles from the primary vendor experience packet loss:
- **Flawed Implementation**: The system falls back to yesterday's closing price or an interpolated average from social media sentiment, executing an erroneous market buy.
- **Closed-World Blueprint ($I_{05}$)**: The BA specification requires that if the data bundle times out but a verified spot price exists from direct exchange quotes, the prompt emitted to the multi-agent debate receives a closed-world schema. All 4 quantitative pillars are marked `UNAVAILABLE`. The execution engine is structurally blocked from emitting `BUY` per Invariant $I_{03}$. The default verdict is clamped to `WATCH (40% confidence)`.

### Callout 2: FDA Class III Medical Device Decision Pipeline
In an ICU multi-parameter patient monitor:
- **Flawed Implementation**: When a pulse oximeter probe detaches from a patient's finger, the firmware defaults to a "normal" baseline reading of 98% oxygen saturation ($\text{SpO}_2$) to prevent alarming clinical staff. The patient quietly suffers anoxic hypoxia.
- **Closed-World Blueprint ($I_{05}$)**: The BA mandates a closed-world fallback contract:
  ```json
  {
    "patient_id": "ICU-BED-04",
    "spo2_status": "PROBE_DISCONNECTED",
    "spo2_value": null,
    "pulse_rate": "UNAVAILABLE",
    "clinical_state": "ALARM_TELEMETRY_UNAVAILABLE",
    "closed_loop_infusion_locked": true
  }
  ```
  The infusion pump mechanically latches its current titration, sounds a high-priority audible alarm, and refuses to administer any automated boluses until physical sensor contact is re-verified.

### Callout 3: Aerospace Fly-by-Wire Avionics (DO-178C Level A)
In a commercial flight control system, if an inertial reference unit (IRU) fails:
- **Closed-World Blueprint ($I_{05}$)**: The flight management computer flags all inertial attitude telemetry as `UNAVAILABLE`. It forbids synthetic pitch rate extrapolation and immediately notifies the flight crew, switching from Normal Flight Law to Alternate/Direct Law, ensuring that aircraft control surfaces are not actuated based on hallucinated gyroscopic coordinates.
