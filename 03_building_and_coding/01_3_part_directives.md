# Module 1: The 3-Part Directive for Architecture & Systems Engineering

## 🧠 Theory: The Physics of LLM Task Execution & Working Memory Limits

When software engineers and system architects begin utilizing autonomous AI coding agents, the default instinct is conversational prompting:
> *"Implement the checkout authorization flow."*  
> *"Refactor the order matching engine to make it faster."*  
> *"Update the clinical telemetry parser for pediatric patients."*

These unstructured requests treat the Large Language Model as an omniscient human colleague. In production, this approach fails catastrophically. An LLM is not a conscious engineer possessing ambient repository memory; it is a probabilistic autoregressive sequence predictor governed by the mathematical physics of transformer self-attention.

### The Attention Entropy Dilution Law

Given an input context of sequence length $N$ tokens mapped to Query ($Q$), Key ($K$), and Value ($V$) representations in $\mathbb{R}^{N \times d_k}$:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

The softmax normalization over sequence length $N$ imposes a strict conservation constraint:
$$\sum_{j=1}^N A_{ij} = 1.0 \implies \mathbb{E}[A_{ij}] = \frac{1}{N}$$

The information-theoretic attention entropy across sequence length $N$ is defined as:
$$\mathcal{H}(A_i) = -\sum_{j=1}^N A_{ij} \ln A_{ij}$$

As context length $N$ expands, maximum possible entropy scales logarithmically ($\mathcal{H}_{\max} = \ln N$). When an unconstrained request is provided without strict context boundaries, the model disperses its attention entropy broadly across irrelevant repository files, ambient library imports, and speculative designs. Consequently, the attention probability allocated to negative boundary constraints, error handlers, and invariant assertions drops below the activation threshold required for reliable generation.

Furthermore, empirical benchmarks demonstrate the **U-Shaped Positional Attention Curve ("Lost in the Middle")**:
$$F(x) = \begin{cases} 
1.0 - k_1 x & x \in [0.0, 0.15] \quad \text{(Primacy Bias)} \\
0.35 + \epsilon(x) & x \in (0.15, 0.85) \quad \text{(Degradation Valley: 40 to 75 percent information loss)} \\
1.0 - k_2 (1.0 - x) & x \in [0.85, 1.0] \quad \text{(Recency Bias)}
\end{cases}$$

When instructions are casually worded, critical architectural constraints placed in the middle of prompts suffer up to 75% retrieval degradation. The AI compensates by hallucinating non-existent database columns, inventing new foreign dependencies, or truncating existing safety checks.

---

## 📐 Formal Anatomy of the Architectural 3-Part Directive

To guarantee deterministic, production-grade output, every machine instruction emitted by a Software Engineer or System Architect must adhere to the **3-Part Directive for Architecture**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         ANATOMY OF THE ARCHITECTURAL 3-PART DIRECTIVE                             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   PART 1: CONTEXT BOUNDARY (The Explicit Epistemic Sandbox)                                      │
│   • Exact file paths and AST function symbols targeted.                                          │
│   • Bounded context slice: maximum 80 physical lines of active code.                             │
│   • Explicit exclusions: files, tables, and directories the agent is FORBIDDEN to touch.         │
│   • Architectural Invariant Bindings: citations of active invariants (e.g., $I_{01}$, $I_{22}$).   │
│                                                                                                  │
│   PART 2: TASK INSTRUCTION (The Surgical Algorithmic Delta)                                      │
│   • Specific functional requirement decomposed from the Semantic Blueprint.                      │
│   • Exact mathematical algorithm citation from `MATHEMATICAL_REGISTRY.md`.                       │
│   • Explicit parameter inputs, return types, and state transitions.                              │
│   • Pre-condition and post-condition invariants.                                                 │
│                                                                                                  │
│   PART 3: FORMAT & ARCHITECTURAL CONSTRAINTS (The Non-Negotiable Rules)                          │
│   • Architectural Modularity Ceiling: target file non-anchor LOC must remain $\le 400$ lines.             │
│   • Rule 14 Anti-Feature-Erasure: zero deletion of fallback retries or telemetry handlers.       │
│   • Fail-Closed Error Policy: raise domain exception or return `None`; zero synthetic fallbacks. │
│   • AST Zero-Mock compliance: zero ZM001–ZM007 violations.                                       │
│   • Output representation: strictly unified diff format or standardized `<DIFF>` XML tags.       │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Role-Based Operational Playbook: Before vs. After Comparisons

### Domain A: Quantitative Finance (Order Execution Guardrail)

#### ❌ The Naive Conversational Prompt (Failure Mode)
> *"Update `execution_gateway.py` to make sure orders don't execute at crazy prices compared to market averages."*
* **What Happens**: The AI inspects the 800-line monolithic file, invents a synthetic fallback price when the market feed is delayed (`spot = quote.price or 150.0`, violating ZM007), replaces 60 lines of FIX protocol error recovery with `# ... existing retry logic ...` (violating Rule 14), and leaves the file at 840 LOC (violating the 400-LOC Architectural Modularity Ceiling).

#### ✅ The Architectural 3-Part Directive (Production Standard)
```markdown
### 1. CONTEXT BOUNDARY
- TARGET FILE: `src/v3/execution/execution_gateway.py` (Non-anchor lines 140–215 only).
- BOUNDING REGISTRY: `docs/MATHEMATICAL_REGISTRY.md` (Algorithm #42: Pre-Trade Execution Plausibility Band).
- BOUNDING INVARIANTS: Invariant $I_{02}$ (Execution-Price Guardrail), Invariant $I_{22}$ (400 LOC Ceiling).
- FORBIDDEN PATHS: Do not modify `src/v3/schemas/` or `src/v3/pipeline/`.

### 2. TASK INSTRUCTION
Implement the mathematical pre-action plausibility check inside `ExecutionGateway.validate_order()`:
$$|P_{\text{exec}} - \text{EMA}_5| \le \max(3.0 \cdot \text{ATR}_{14}, \; 0.08 \cdot \text{EMA}_5)$$
- Inputs: `proposed_price: float`, `ema_5: float`, `atr_14: float`.
- Behavior: If deviation exceeds the maximum band, reject the order with `ExecutionGuardrailViolation`.
- If `ema_5 <= 0` or `atr_14 <= 0` or any input is non-finite (`NaN`/`Inf`), fail closed immediately by raising `InvalidTelemetryError`.

### 3. FORMAT & ARCHITECTURAL CONSTRAINTS
- ARCHITECTURAL MODULARITY CEILING: `execution_gateway.py` currently stands at 320 LOC; your modification must not push total non-anchor lines above 350 LOC.
- RULE 14 ANTI-FEATURE-ERASURE: Preserve all existing FIX tag assertions and latency timestamps verbatim.
- ZERO-MOCK COMPLIANCE: Do not provide default values for `ema_5` or `atr_14` (violates ZM005). Do not return `True` in `except` blocks (violates ZM001).
- INVARIANT ANCHOR: Embed the verified SHA1 Invariant Anchor for $I_{02}$ directly above `validate_order()`:
  `# === INVARIANT-BLOCK v1`
  `# INVARIANT: I02`
  `# GUARDRAIL: Pre-Action Execution Plausibility Envelope ($I_{02}$)`
  `# PREDICATE: Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)`
  `# /INVARIANT [sha1:037a1c64]`
  `# === /INVARIANT-BLOCK ===`
- OUTPUT FORMAT: Emit strictly a git unified diff patch. No markdown commentary before or after.
```

---

### Domain B: FDA Class III Medical Device Firmware (Closed-Loop Vasopressor Titration)

#### ❌ The Naive Conversational Prompt (Failure Mode)
> *"Write a function that calculates the next infusion rate for the vasopressor pump based on mean arterial pressure."*
* **What Happens**: The AI outputs a function with hardcoded fallback rates (`if map is None: return 5.0`), smuggling dangerous synthetic constants into a life-critical closed-loop titration controller (violating fail-closed medical principles).

#### ✅ The Architectural 3-Part Directive (Production Standard)
```markdown
### 1. CONTEXT BOUNDARY
- TARGET FILE: `firmware/infusion/vasopressor_controller.c` (Lines 80–145).
- BOUNDING SPECIFICATION: 21 CFR Part 820.30 Design Controls & ISO 13485:2016 §7.3.
- BOUNDING INVARIANTS: Hard-Safety Invariant $I_{02\text{-MED}}$ (Basal Plausibility Band: $|\text{Rate}_{\text{new}} - \text{Rate}_{\text{cur}}| \le 0.10 \cdot \text{Rate}_{\text{cur}}$).
- EXCLUSIONS: Do not alter hardware timer interrupt ISRs in `firmware/drivers/timer_pwm.c`.

### 2. TASK INSTRUCTION
Implement `vasopressor_calculate_step()` enforcing closed-loop norepinephrine titration bounds:
- Inputs: `current_rate_mcg_min: uint32_t`, `measured_map_mmhg: uint16_t`, `target_map_mmhg: uint16_t`.
- Formula: $\Delta \text{Rate} = k_p \cdot (\text{Target} - \text{Measured})$. Clamp $\Delta \text{Rate}$ to $[-0.5, +0.5]\,\mu\text{g/min}$.
- Safety Clamp: Enforce absolute maximum delivery ceiling $\le 30.0\,\mu\text{g/min}$.
- Sensor Drop Intercept: If `measured_map_mmhg == 0` or sensor invalidity flag is asserted, mechanically latch the pump to the fail-safe basal rate ($2.0\,\mu\text{g/min}$) and trip the audible alarm interrupt. Zero synthetic imputation allowed.

### 3. FORMAT & ARCHITECTURAL CONSTRAINTS
- MISRA-C:2012 COMPLIANCE: Zero dynamic memory allocation (`malloc`/`free`); zero floating-point arithmetic (use Q16.16 fixed-point math); all integer conversions must be explicit.
- LOC BOUNDS: Function length must not exceed 65 physical lines.
- RULE 14 PRESERVATION: Preserve hardware watchdog kick `WDT_PET()` at the entry and exit of the control block.
- OUTPUT FORMAT: Emit C code enclosed in `<FIRMWARE_DIFF>` tags.
```

---

### Domain C: Aerospace Fly-by-Wire Avionics (Control Surface Actuation)

#### ❌ The Naive Conversational Prompt (Failure Mode)
> *"Add a yaw damper function to smooth out rudder oscillations during turbulence."*
* **What Happens**: The AI generates a recursive filter without bounding the condition number or checking for floating-point NaN/Inf, potentially triggering aeroelastic flutter during severe atmospheric shears.

#### ✅ The Architectural 3-Part Directive (Production Standard)
```markdown
### 1. CONTEXT BOUNDARY
- TARGET FILE: `avionics/fcs/rudder_yaw_damper.adb` (Ada 2012 package body).
- REGULATORY BASELINE: RTCA DO-178C / EUROCAE ED-12C Level A (Catastrophic Failure Condition).
- BOUNDING INVARIANTS: Aerospace Invariant $I_{07\text{-AERO}}$ (Div-by-Zero and NaN Domain Safety).
- FORBIDDEN PATHS: Do not modify Primary Flight Control Computer (PFCC) bus arbitration.

### 2. TASK INSTRUCTION
Implement `Compute_Damping_Command` implementing washed-out yaw rate filtering:
$$H(s) = \frac{K_{\text{damper}} \cdot \tau s}{\tau s + 1}$$
- Discretize via Tustin bilinear transform at sample frequency $f_s = 100\,\text{Hz}$ ($\Delta t = 10\,\text{ms}$).
- Hard Actuator Limiter: Deflection command $\delta_r$ must be mechanically clamped to $[-5.0^{\circ}, +5.0^{\circ}]$ and rate-clamped to $\le 20.0^{\circ}/\text{sec}$.
- Defective Gyro Gate: If yaw rate gyro bit `FAULT_STATUS = TRUE` or input is non-finite, set $\delta_r = 0.0^{\circ}$ (neutral trim) and assert `DISENGAGE_YAW_DAMPER_ANNUNCIATOR`.

### 3. FORMAT & ARCHITECTURAL CONSTRAINTS
- DO-178C LEVEL A: Code must contain zero recursive subprograms, bounded loops only, and explicit range contracts (`with Dynamic_Predicate`).
- RULE 14 PRESERVATION: Preserve actuator sensor LVDT feedback calibration routine verbatim.
- OUTPUT FORMAT: Emit pure Ada unified diff.
```

---

## ⚖️ Dual-Use Callout Box: High-Stakes Directive Enforcement

::: tip DUAL-USE ANALYSIS: DIRECTIVE ENFORCEMENT ACROSS REGULATED INDUSTRIES
| Operational Dimension | Quantitative Trading Systems | FDA Class III Medical Devices | Aerospace Flight Management (DO-178C) |
| :--- | :--- | :--- | :--- |
| **Context Sandbox** | Restricts AI to specific trading strategy modules (`src/v3/strategy/`). Banning access to raw database drop privileges. | Restricts AI to algorithmic drug calculation modules. Banning access to hardware interrupt vector tables. | Restricts AI to navigation calculation modules. Banning modification of flight-critical servo actuation loops. |
| **Fail-Closed Mandate** | Order rejected on unverified market price; cash balance untouched ($I_{05}$). | Infusion clamped to safe basal rate on transducer failure; audible alarm sounded ($I_{05\text{-MED}}$). | Autopilot disengaged to Direct Law on pitot icing; flight director handoff to manual ($I_{05\text{-AERO}}$). |
| **Anti-Feature-Erasure** | Forbids AI from truncating 150 lines of multi-broker fallback cascades into `# ... rest of broker logic ...`. | Forbids AI from deleting occlusion pressure sensing or bubble detector interrupt routines. | Forbids AI from stripping dual-redundant bus cross-comparisons or cyclic redundancy checks (CRCs). |
:::

---

## ✍️ Hands-On Exercises: Authoring Architectural Directives

### Exercise 1.1: Re-writing the Vague Invoicing Directive
**Scenario**: The Business Analyst's Semantic Blueprint states: *"Emit an `InvoiceGeneratedEvent` to the shared event bus whenever an order is marked settled. The event must carry the immutable UUID and the total integer cents."*

#### Your Action:
Author the 3-Part Directive for the autonomous builder agent. Include the Context Boundary, Task Instruction, and Architectural Constraints (enforcing the Architectural Modularity Ceiling ($\le 400$ LOC), Rule 14 Anti-Feature-Erasure, and zero synthetic fallbacks).

#### Model Solution:
```markdown
### 1. CONTEXT BOUNDARY
- TARGET FILE: `src/services/billing/invoice_settlement.py` (Lines 110–180).
- BOUNDING REGISTRIES: `function_registry.md` (`EventBus.publish_event`).
- BOUNDING INVARIANTS: Invariant $I_{15}$ (UUID Traceability), Invariant $I_{22}$ (400 LOC Ceiling).
- FORBIDDEN ACTIONS: Do not install external messaging packages; use existing `src/infrastructure/event_bus.py`.

### 2. TASK INSTRUCTION
Inside `InvoiceSettlementService.mark_settled()`, construct and publish `InvoiceGeneratedEvent`:
- Required fields: `invoice_uuid: str` (RFC 4122 v4), `order_uuid: str`, `amount_cents: int`, `settled_at_epoch_ms: int`.
- Enforce integer invariant: `amount_cents` must be strictly positive integer ($> 0$). Reject floating-point currency representation.
- Dispatch via `EventBus.publish("invoices.generated", event.to_payload())`.

### 3. FORMAT & ARCHITECTURAL CONSTRAINTS
- ARCHITECTURAL MODULARITY CEILING: Ensure total file LOC remains $< 350$ lines (enforcing the 400-LOC Ceiling).
- RULE 14 PRESERVATION: Retain all database transaction rollback blocks and dead-letter queue routing verbatim.
- ZERO-MOCK COMPLIANCE: Do not supply a fallback amount or default UUID. If fields are missing, raise `UnprocessableSettlementError`.
- OUTPUT: Emit unified diff only.
```

---
[**Proceed to Module 2: Adversarial Thinking & Red-Teaming for Builders →**](./02_adversarial_thinking.md)
