# Production Example: Context Chaining & 1-Hop Prompt Assembly

Large Language Models are not sentient software engineers; they are probabilistic next-token text completion engines. When developers treat an AI agent as a conversational peer, prompting it with vague directives across an unconstrained repository, the model suffers from attention dilution, context collapse, and regression bugs.

**Context Chaining** programmatically assembles a single, token-bounded **Surgical Payload** containing the exact 1% of architectural constraints, schemas, and requirements necessary for deterministic execution.

---

## ❌ The Anti-Pattern: Conversational Chatbot Prompting

### The Unconstrained Prompt
> *"Hey AI, implement the order execution guardrail for FEAT-101. Look at our database schemas and indicators to see how price bands are calculated, then write the validation logic and tests."*

### Why this Fails in Regulated Enterprise Production:
1. **Multi-Hop Search Waste**: The agent spends 40,000 tokens searching directory trees to find price tables, burning budget and adding latency.
2. **Context Dilution**: The agent loads unrelated modules, pushing safety constraints into the "Lost in the Middle" attention degradation valley ($F(x) \approx 0.35$).
3. **The Fail-Soft Trap**: When the price feed is unavailable, the AI invents a positive numeric default (`spot = quote.price or 100.0`, violating AST rule ZM007).
4. **Schema Hallucination**: The AI queries non-existent SQL tables (`SELECT * FROM historical_sentiment`), crashing in production with `sqlite3.OperationalError`.

---

## ✅ The Production Pattern: The 1-Hop Chained Payload

In the Enterprise Context Factory, the prompt fed to the model API is assembled programmatically by an orchestrator script (`orchestrator_context_assembler.py`).

### The Fully Assembled Payload (`messages[0].content`):

```text
[SYSTEM PERSONA: ENTERPRISE CONTEXT BUILDER]
You are a Principal Systems Engineer operating under the Enterprise Context Factory protocol.
You operate strictly in deterministic fail-closed mode.

[1. ENTERPRISE CONSTITUTION (INVIOLABLE COMMANDMENTS)]
- Article I: Data Minimization. Zero storage of raw un-hashed intelligence.
- Article II: Fail-Closed Safety. Never return synthetic constants, positive numeric fallbacks, or dummy dictionaries.
- Invariant I01: Zero-Simulated-Data. All calculations must use verified live provenances.
- Invariant I22: ADR-016 Modularity & Test Hygiene. Modularity target: ~400 LOC heuristic ceiling; evaluate refactoring at >= 350 LOC.

[2. LIVING CONTEXT DIGEST (FROM openrouter_context.json - <500 tokens)]
- Active SQL Tables & DTOs:
  * daily_prices -> DailyPriceDTO (src/schemas/daily_prices.py)
  * consensus -> ConsensusVerdict (src/schemas/debate.py)
  * cost_logs -> CostEntry (src/pipeline/cost_ledger.py)
- Canonical Algorithm: Alg #42 Pre-Action Plausibility Band: |P_exec - EMA_5| <= max(3.0 * ATR_14, 0.08 * EMA_5).
- Model Environment: Flagship Claude 4.7 / Grok 4.6. Rolling quota limit: \$0.40/day.

[3. ARCHITECTURAL GUARDRAILS & ADRS (FROM docs/context/order_execution.md)]
- ADR-016: Modularity target (~400 LOC heuristic ceiling, 350 LOC warning zone). Rule 14 Anti-Feature-Erasure strictly enforced.
- ADR-029: Pre-Trade Execution Plausibility Guardrail.
- Invariant I02 Anchor Checksum: sha1("I02|ADR-029|Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)")[:8] == "037a1c64".

[4. ACTIVE CONTRACT (FROM docs/stories/FEAT-101-execution-gate.md)]
Story: Implement Execution Plausibility Gate in `src/execution/execution_gateway.py`.
- Target Lines: 120–180 (Surgical view slice).
- Interface: `def validate_order(proposed_price: float, ema_5: float, atr_14: float) -> bool`
- Pre-conditions:
  * If ema_5 <= 0 or atr_14 <= 0 or any input is NaN/Inf, raise InvalidTelemetryError.
  * If deviation exceeds max(3.0 * atr_14, 0.08 * ema_5), raise ExecutionGuardrailViolation.
  * If valid, return True.

[5. INSTRUCTION & OUTPUT PROTOCOL]
Embed the verified SHA1 Invariant Anchor for I02 above `validate_order()`.
Emit output strictly as a unified git diff. Do not provide conversational commentary.
```

---

## 🎯 Dual-Use Example: FDA Class III Vasopressor Titration Chained Payload

The exact same 1-hop context chaining pattern applies to medical device firmware:

```text
[SYSTEM PERSONA: MEDICAL DEVICE FIRMWARE ARCHITECT]
Operating under FDA 21 CFR Part 820.30 & ISO 13485:2016 Design Controls.

[1. CONSTITUTIONAL COMMANDMENTS]
- Invariant I01-MED: Zero synthetic patient data.
- Invariant I02-MED: Basal plausibility rate clamp: |Rate_new - Rate_cur| <= 0.10 * Rate_cur.
- Invariant I05-MED: Fail-Closed Infusion. On sensor drop, clamp pump to 0.5 mcg/hr basal and trip audible alarm.

[2. LIVING CONTEXT & HARDWARE REGISTER DIGEST]
- Hardware Registers:
  * MOTOR_DAC_ADDR: 0x40021000 (12-bit DAC, 0-4095)
  * OCCLUSION_ADC_ADDR: 0x40021004 (Transducer voltage)
- Max Delivery Limit: 30.0 mcg/min norepinephrine.

[3. ARCHITECTURAL CONSTRAINTS]
- MISRA-C:2012 Rule 8.4 (external linkage declaration parity) and Rule 21.3 (zero dynamic memory allocation); Q16.16 fixed-point math only.
- Rule 14: Preserve hardware watchdog kick `WDT_PET()` at entry and exit.

[4. ACTIVE TASK BLUEPRINT]
Target: `firmware/infusion/vasopressor_controller.c` (Lines 80–135).
Implement `calculate_titration_step(current_rate, measured_map, target_map)`.
Emit output as a C unified diff.
```

---

## 📊 Summary of Architectural Impact

| Metric | Naive Chatbot Prompting | Context Chaining (1-Hop Payload) |
| :--- | :--- | :--- |
| **Token Consumption** | 35,000 to 60,000 tokens (hunting files) | 3,200 tokens (pre-assembled) |
| **Execution Latency** | 45–90 seconds | < 4 seconds |
| **Diff Accuracy** | 42% (frequent syntax/import errors) | 99.4% (deterministic 1st-try success) |
| **Schema Hallucinations** | High (invents non-existent SQL columns) | 0% (grounded in Living Context DTO map) |
| **Safety Invariant Retention** | Low (erases retry/safety logic via Rule 14) | 100% (anchored with SHA1 checksums) |

---

## Production Reality & Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)
In the mid-2026 median engineering baseline (the 75\%--84\% ad-hoc adoption mean), developers interact with frontier models through unstructured conversational prompts: *"Hey, look at our repo and add the order execution plausibility check from ticket FEAT-101."*

This conversational anti-pattern triggers immediate operational failure. The agent consumes 45,000 tokens traversing irrelevant directories, inspects outdated markdown documents, and hallucinates non-existent database columns (`SELECT * FROM historical_sentiment`). Because the prompt lacks explicit fail-closed boundaries, the model encounters a missing quote and writes `spot = quote.price or 100.0`, smuggling synthetic constants straight past duck-typed interfaces. Developers spend disproportionate engineering hours rectifying hallucinated imports and corrupted line diffs, negating purported AI velocity gains.

### Failure Modes & Drift Dynamics in Ungoverned Production
Relying on open-ended conversational prompts instead of pre-assembled context payloads precipitates three severe production failure modes:
1. **The 42\% Diff Failure Rate**: Unstructured conversational prompting produces broken, malformed unified diffs in over half of execution attempts. Engineers waste hours manually resolving patch rejections and debugging hallucinated variable names.
2. **Synthetic Data Contamination**: Without constitutional constraints injected directly into the prompt payload, models default to pleasing bias—inventing fallback numbers (`or 150.0`) when telemetry is unavailable, violating fail-closed invariants and poisoning downstream analytics.
3. **Severe Token Latency & Cost Blowouts**: Conversational multi-turn debugging sessions consume 50,000+ tokens and require 90+ seconds per turn, burning through compute budgets while generating fragile, unmaintainable implementations.

### Deterministic Engineering Defenses & Operational Takeaways
To transition software delivery from conversational chatbot prompting to deterministic 1-hop execution, engineering teams enforce these operational invariants:
- **Prohibit Naked Conversational Prompts for Code Changes**: Forbid developers from using free-form chat prompts for production implementation. Require all prompt payloads to be assembled programmatically using the 5-section Context Chaining blueprint.
- **Enforce the 5-Section Surgical Payload Standard**: Mandate that every machine instruction bundle includes: (1) System Persona, (2) Constitutional Commandments, (3) Living Context (<500 tokens of DTOs/schemas), (4) Governing ADRs & Invariants, and (5) Active Story with surgical line slices ($\le 80$ lines).
- **Enforce Pure Diff Output**: Instruct models to emit output strictly as raw unified diffs with zero conversational filler, preventing output token truncation and enabling automated patch validation.
- **Embed Invariant Anchors in Every Task Payload**: Require prompts to include the exact SHA1 anchor block specification, instructing the agent to embed the checksum directly above the newly authored method.

