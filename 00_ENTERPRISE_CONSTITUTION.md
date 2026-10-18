# The Enterprise AI Constitution: Architectural Invariants, Inviolable Commandments, and Governance Doctrines

## Preamble & Sovereign Authority

This Constitution establishes the immutable engineering laws, architectural constraints, and operational boundaries governing all autonomous AI agents, human practitioners, and automated CI/CD pipelines within the enterprise.

In mission-critical, regulated environments—spanning FDA Class III closed-loop medical devices (21 CFR Part 820), aerospace avionics (DO-178C Level A), banking mainframes, and autonomous quantitative execution engines—**probabilistic Large Language Models (LLMs) cannot possess sovereign architectural authority.** Stochastic models hallucinate plausible-sounding interfaces, drop error handlers under token pressure, and fabricate synthetic data when external telemetry drops.

Therefore, this Constitution serves as a **deterministic, non-negotiable compile-time and runtime governor**. All agent prompts, code generators, and architectural decisions must execute under the active constraint of this Constitution during both the design phase and the programmatic self-critique phase. Any agent output or human pull request that violates any Constitutional Article, Invariant, or Commandment is structurally invalidated, rejected by automated AST sentinels, and quarantined.

---

## 1. The Ten Inviolable Commandments of Autonomous Software Engineering

These Ten Inviolable Commandments represent the bedrock principles of enterprise software engineering with AI. They override all transient feature requests, speed-to-market pressures, and conversational prompt instructions:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           THE TEN INVIOLABLE COMMANDMENTS                                        │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  I.    Zero Simulated Data in Production: Missing live data must fail closed (return None).       │
│  II.   400 LOC Module Hard Ceiling (ADR-016): Modularize at 350 lines; enforce Rule 14.          │
│  III.  Hermetic Socket Isolation in Tests: Outbound egress raises SocketBlockedError.            │
│  IV.   Zero AST Registry Drift: Byte-for-byte synchronization between code and metadata.         │
│  V.    Epistemic Air-Gap for External Media (ADR-030): Ingest as psychology; discount 80%.      │
│  VI.   Dialectical Adversarial Triads (ADR-039): Multi-agent debate arbitrated by convex solver.  │
│  VII.  No Single-Metric Vetoes Over Confluence (ADR-024): Compensatory M-of-N orthogonal logic.  │
│  VIII. Protect Quality Compounders with Horizon-Matched Decay: Secular assets need long memory.  │
│  IX.   Pre-Action Execution Plausibility Bands (ADR-029): Clamp actions to volatility envelopes. │
│  X.    Deflate Sharpe Ratios for Selection Bias: Validate calibrations using DSR >= 0.95.        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Detailed Commandment Specifications:

1. **Commandment I — Zero Simulated Data in Production (Invariant $I_{01}$):**  
   Synthetic data, mock dictionaries, fallback ratios, and optimistic sentinels are strictly prohibited in production code paths. When an upstream sensor, database, or API fails, the system must **fail closed** (`None` or explicit exception). Never fabricate plausible numbers to maintain the illusion of operational continuity.
2. **Commandment II — 400 LOC Module Hard Ceiling (ADR-016 / Invariant $I_{22}$):**  
   No single production, test, or configuration file may exceed 400 Physical Lines of Code (LOC). When a file reaches 350 LOC, all feature additions are frozen until the file is refactored into cohesive domain submodules. Under Rule 14 (Anti-Feature-Erasure), refactoring must partition logic cleanly—deleting defensive assertions, error handlers, or fallbacks is a constitutional violation.
3. **Commandment III — Hermetic Socket Isolation in Tests:**  
   Unit and component test suites must execute under OS-level network socket blocking (`tests/conftest.py` with `--disable-socket`). Any test that attempts outbound network communication raises `SocketBlockedError`. Tests must be 100% hermetic, deterministic, and repeatable offline.
4. **Commandment IV — Zero AST Registry Drift:**  
   Source code changes shift Abstract Syntax Tree (AST) coordinates and signature contracts. Developers and agents must execute the atomic pre-commit command chain to synchronize `STATE_REGISTRY.md`, `docs/MATHEMATICAL_REGISTRY.md`, and `data/openrouter_context.json`. CI gates halt merges if `git diff --exit-code` reports any registry drift.
5. **Commandment V — Epistemic Air-Gap for External Telemetry (ADR-030 / Invariant $I_{20}$):**  
   External unstructured narrative feeds (news, social media, transcripts, vendor brochures) must be ingested across a unidirectional epistemic air-gap. Internal portfolio positions, patient medical records, and macro bias labels must never leak into ingestion prompts. Promotional commercial funnels must have their sentiment polarity discounted by 80% ($W_{\text{commercial}} = 0.20$).
6. **Commandment VI — Dialectical Adversarial Triads for Critical Allocation (ADR-039):**  
   Autonomous action authorization cannot rely on a single agent prone to pleasing bias. High-stakes capital allocation or clinical dosage changes require a 3-stage dialectical debate between a Proponent (Bull), an Adversary (Bear), and a Forensic Auditor, arbitrated by a deterministic convex log-odds solver with Jensen-Shannon Divergence entropy discounting.
7. **Commandment VII — No Single-Metric Vetoes Over Confluence (ADR-024 / Invariant $I_{09}$):**  
   Sequential conjunctive boolean `AND` gates induce 99% false-negative gate paralysis. Decision-making must project evidence onto $N = 4$ orthogonal pillars, authorizing action when $M \ge 2$ pillars exhibit high conviction ($\ge 0.35$). Hard vetoes are strictly restricted to fatal existential collapse ($I_{03}$).
8. **Commandment VIII — Protect Quality Compounders with Horizon-Matched Decay (ADR-033 & ADR-031):**  
   Signal confidence must decay continuously using category-matched half-lives ($5\text{d}$ kinematic to $90\text{d}$ secular compounder). Secular high-reinvestment compounders must be protected by a 20-trading-day Time-in-State Hold Lock and session-close momentum barriers, preventing premature shakeouts on transient noise.
9. **Commandment IX — Pre-Action Execution Plausibility Bands (ADR-029 / Invariant $I_{02}$):**  
   Every proposed state-mutating execution must satisfy a dynamic kinematic envelope: $|P_{\text{exec}} - \text{EMA}_5| \le \max(3\cdot \text{ATR}_{14}, 0.08\cdot \text{EMA}_5)$. Actions breaching this band are rejected as flash crashes, fat-finger errors, or sensor dropouts.
10. **Commandment X — Deflate Sharpe Ratios for Multiple Testing Bias:**  
    Any parameter optimization or algorithmic model tuned over $N$ historical trials must be evaluated using the Deflated Sharpe Ratio (DSR). Calibrations with $\text{DSR} < 0.95$ are rejected as overfit statistical artifacts (P-hacking).

---

## 2. The 22 Canonical System Invariants ($I_{01}$ through $I_{22}$)

The 22 Canonical Invariants constitute the formal mathematical and structural contracts of the architecture. Every invariant belongs to an explicit classification, is governed by formal Architectural Decision Records (ADRs), maps to target production modules, and is verified by dedicated automated tests.

| ID | Invariant Name | Governing ADRs | Class | Mathematical Predicate & Semantic Contract | Target Modules | Primary Enforcement Test |
|:---|:---|:---|:---|:---|:---|:---|
| **$I_{01}$** | **Zero-Simulated-Data** | ADR-029<br>ADR-045 | HARD-SAFETY | $\forall p \in \text{Pipeline}: p.\text{src} \in \text{ALLOWLIST} \land \neg p.\text{synthetic}$. Missing live telemetry forces fail-closed return (`None` / Exception). ATR calculation requires $\ge 15$ verified live bars. | `api_client.py`<br>`quant_engine.py` | `test_zero_taint_fail_closed.py`<br>`test_spot_price_enforcement.py` |
| **$I_{02}$** | **Execution-Price Guardrail** | ADR-029 | HARD-SAFETY | $\|P_{\text{exec}} - \text{EMA}_5\| \le \max(3.0 \cdot \text{ATR}_{14}, \; 0.08 \cdot \text{EMA}_5)$. Weekend/off-session execution rejected unless matching Friday close within $\le 1.0\%$. | `execution_guardrails.py`<br>`portfolio_tracker.py` | `test_execution_guardrails.py`<br>`test_math_stress_invariants.py` |
| **$I_{03}$** | **Fatal-Contagion Veto** | ADR-024<br>ADR-026 | HARD-SAFETY | $\text{SCSI} \le -0.35 \lor D_{\text{toxic}} > 1.50 \lor (\text{Altman Z} < 1.10 \land \text{NetDebt} > 0) \implies \text{Action} \neq \text{BUY}$. Fatal contagion overrides all positive confluence. | `consensus_service.py`<br>`debate/matrix.py` | `test_compensatory_confluence.py`<br>`test_hype_divergence_veto.py` |
| **$I_{04}$** | **Immutable-Ledger Quarantine** | ADR-027 | HARD-SAFETY | $\forall r \in \text{Ledger}: \text{DELETE}(r) = \emptyset$. Raw hard-deletes are structurally banned. Corrupted, stale, or invalidated records migrate atomically to `quarantine` with non-null audit reason. | `consensus_service.py`<br>`api_client.py` | `test_quarantine_governance.py` |
| **$I_{05}$** | **Closed-World Fallback** | ADR-029<br>ADR-045 | HARD-SAFETY | On bundle or upstream DB failure with verified spot price: prompt receives closed-world fallback schema with 4 Pillars `UNAVAILABLE`, stops `UNAVAILABLE`, and action forced to `WATCH`. | `query_orchestrator.py`<br>`data_ingest.py` | `test_cross_channel_conformal_fuzz.py` |
| **$I_{06}$** | **MOS Bounded Multipliers** | ADR-043<br>ADR-034 | MATH-BOUND | Risk sizing multiplier $M \in [0.20, 1.25]$. Margin of Safety $\text{MOS} \in [-1.0, 1.0]$. Computed values outside bounds are clamped deterministically with telemetry alarms. | `quant_engine.py`<br>`composite_mos.py` | `test_math_stress_invariants.py` |
| **$I_{07}$** | **Div-by-Zero Domain Safety** | ADR-043 | MATH-BOUND | $\forall a/b: b = 0 \implies \text{defined finite fallback}$ (zero NaN/Inf propagation). Logarithmic and square-root operations must assert non-negativity of arguments before evaluation. | `quant_engine.py`<br>`breakout_scout.py` | `test_math_stress_invariants.py` |
| **$I_{08}$** | **Growth-Adjusted Hurdle** | ADR-031 | MATH-BOUND | $\text{EGR} = \text{FCF-Yield} + \min(g, 0.25)$. For high-growth units ($g \ge 10\%$), action authorization requires $\text{EGR} \ge r_{\text{baseline}}$. Growth factor $g$ is hard-capped at $0.25$. | `quant_engine.py` | `test_growth_adjusted_hurdle.py` |
| **$I_{09}$** | **Compensatory Confluence** | ADR-024 | MATH-BOUND | $\text{Action Approved} \iff \sum_{k=1}^4 \mathbb{I}(P_k \ge 0.35) \ge 2 \;\land\; \neg \text{FatalContagion}$. No single orthogonal pillar possesses unilateral veto authority over confluence. | `consensus_service.py`<br>`debate/matrix.py` | `test_compensatory_confluence.py` |
| **$I_{10}$** | **Bandit Prior Integrity** | ADR-034 | MATH-BOUND | Contextual Thompson Sampling policy over exactly 6 discrete action arms. Beta conjugate priors clamped $\alpha, \beta \ge 0.5$. Rewards update on beta-stripped residual delta $r_{\text{resid}}$. | `contextual_bandit_rl.py` | `test_contextual_bandit_rl.py` |
| **$I_{11}$** | **Whitening Stability** | ADR-039 | MATH-BOUND | Ledoit-Wolf shrinkage matrix condition number $\mathrm{cond}(\Sigma_{\text{LW}}) \le 10^{12}$. Symmetrical ZCA whitening clamps eigenvalues $\lambda \ge \epsilon_{\text{floor}} \lambda_{\max}$ to prevent alpha destruction. | `quant_engine.py`<br>`debate/matrix.py` | `test_zca_whitening.py` |
| **$I_{12}$** | **Conformal Coverage** | ADR-040 | MATH-BOUND | Split-conformal prediction intervals calibrated over rolling 120-day window. Plausibility band width is monotonically non-decreasing in market stress / volatility regime buckets. | `quant_engine.py` | `test_conformal_calibration.py` |
| **$I_{13}$** | **Remote-First Freshness** | ADR-000<br>ADR-038 | SCHEMA-PARITY | Canonical truth resides in distributed remote ledger. Mandatory pull-before-push (`sync_data.py --pull`). Local worker cache reads $> 3 \text{ days}$ stale fail closed (`StaleDataCircuitBreaker`). | `api_client.py`<br>`live_price_engine.py` | `test_spot_price_enforcement.py` |
| **$I_{14}$** | **Cross-Channel Sync** | ADR-038 | SCHEMA-PARITY | Immutable server-composed directional header lock in prompts. Table `channel_verdict_audit` logs all presentation events; automated daily sentinel detects any inter-channel divergence. | `consensus_service.py`<br>`query_orchestrator.py` | `test_cross_channel_verdict_parity.py` |
| **$I_{15}$** | **UUID Traceability** | ADR-018 | SCHEMA-PARITY | Every LLM call, consensus verdict, and state mutation carries a cryptographically unique UUIDv4 trace ID persisted into immutable remote audit ledgers. | `decision_trace.py`<br>`debate/matrix.py` | `test_traceability.py` |
| **$I_{16}$** | **Multi-Entity Isolation** | ADR-045 | SCHEMA-PARITY | $\forall e_1 \neq e_2: \text{State}(e_1) \cap \text{State}(e_2) = \emptyset$. Loop-carried scalar contamination across batch loops is structurally banned; all entities evaluated in hermetic scopes. | `query_orchestrator.py`<br>`debate/matrix.py` | `test_cross_channel_conformal_fuzz.py` |
| **$I_{17}$** | **Horizon-Matched Decay** | ADR-027<br>ADR-033 | DECAY-TIMING | $w(\Delta t) = w_0 \cdot 2^{-\Delta t / t_{1/2}(h)}$ with $t_{1/2}(h) \in [5\text{d}, 90\text{d}]$. Signals with $\Delta t > 2 \cdot t_{1/2}$ automatically demote to `NEUTRAL (EXPIRED)` with zero decision weight. | `consensus_service.py`<br>`quant_engine.py` | `test_consensus_decay.py` |
| **$I_{18}$** | **Compounder Hold Lock** | ADR-033<br>ADR-044 | DECAY-TIMING | 20-trading-day Time-in-State Compounder Guard: no liquidation while asset return exceeds benchmark $r_{\text{asset}} \ge r_{\text{bench}}$ absent fatal veto. 14-day post-exit cooldown strictly enforced. | `portfolio_tracker.py`<br>`consensus_service.py` | `test_portfolio_tracker.py` |
| **$I_{19}$** | **Session Momentum Lock** | ADR-031 | DECAY-TIMING | Never liquidate or downgrade an entity closing in the upper quartile $(close - low)/(high - low) \ge 0.75$ on expanding volume ($\ge 1.25\times 20\text{d}$ average) into cash equivalents. | `execution_guardrails.py`<br>`portfolio_tracker.py` | `test_momentum_lock.py` |
| **$I_{20}$** | **Epistemic News Isolation** | ADR-030<br>ADR-044 | CONTEXT-ISOLATION | External media ingested as unverified crowd psychology; air-gapped from internal holdings. Commercial marketing funnels automatically detected and discounted by 80% ($W_{\text{commercial}} = 0.20$). | `debate/context_slicer.py`<br>`data_ingest.py` | `test_epistemic_firewall.py` |
| **$I_{21}$** | **Macro Transmission Gate** | ADR-044<br>ADR-042 | CONTEXT-ISOLATION | Fast acute (10d) vs Slow structural (3y) macro partition. When Transmission Gate $\mathcal{G}_{\text{trans}} = 0$, slow macro drag is decoupled ($0.0$). Whisper Shield active against broad market panic. | `macro_aggregator.py`<br>`debate/context_slicer.py` | `test_macro_transmission_gate.py` |
| **$I_{22}$** | **400 LOC & Test Hygiene** | ADR-016<br>ADR-045 | CODE-HYGIENE | Physical file LOC $\le 400$ across all repositories. Verifiable SHA1-checksummed invariant anchors. Automated adversarial QA auditor rating score must achieve $\ge 90\%$. | All Source & Test Files | `verify_code_invariants.py`<br>`audit_test_quality.py` |

---

## 3. Cryptographic Invariant Anchor Block Mechanics

To bridge high-level constitutional doctrine with concrete source code, every production module implementing an invariant must embed a standardized, machine-readable **SHA1 Invariant Anchor Block**.

### 3.1 Anchor Block Syntax & Schema

Invariant blocks must be placed immediately above the canonical function or class implementation:

```python
# === INVARIANT-BLOCK v1 (DO NOT EDIT MANUALLY) ===
# INVARIANT: I02
# NAME: Execution-Price Guardrail
# ADR: ADR-029
# CLASS: HARD-SAFETY
# ROLE: CANONICAL_IMPL
# PREDICATE: Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)
# ASSERT: tests/unit/test_execution_guardrails.py
# /INVARIANT [sha1:037a1c64]
# === /INVARIANT-BLOCK ===
def validate_execution_price(p_exec: float, ema_5: float, atr_14: float) -> bool:
    """Canonical implementation of Invariant I02."""
    if p_exec <= 0 or ema_5 <= 0 or atr_14 <= 0:
        return False
    threshold = max(3.0 * atr_14, 0.08 * ema_5)
    return abs(p_exec - ema_5) <= threshold
```

### 3.2 The Cryptographic Verification Hashing Formula

The 8-character hex checksum appended to `# /INVARIANT [sha1:xxxxxxxx]` is deterministically generated from the concatenation of the Invariant ID, Governing ADR, and Predicate string:

$$\text{raw-payload} = \text{inv-id} \parallel \text{adr.strip()} \parallel \text{predicate.strip()}$$

$$\text{anchor-hash} = \mathrm{SHA1}\left(\text{RawPayload}\right)\left[:8\right]$$

### 3.3 AST Verification Scanner & Physical LOC Calculation

The pre-commit script `scripts/verify_code_invariants.py` parses the AST of every tracked file, extracts all Invariant Blocks, recomputes the SHA1 hash, and verifies parity against the test specified in the `ASSERT` field.

To ensure that detailed invariant documentation does not penalize engineers under the ADR-016 400-LOC ceiling, the AST scanner computes physical non-anchor LOC as:

$$\text{non-anchor-loc} = \text{total-file-lines} - \text{anchor-block-lines} \le 400$$

If any developer or AI agent edits an invariant predicate without updating the corresponding test and recalculating the SHA1 hash, CI immediately rejects the commit with a cryptographic tampering error.

---

## 4. The Fail-Closed Telemetry Doctrine & Zero Hard-Deletes Mandate

### 4.1 The Fail-Closed Telemetry Doctrine

In non-critical web development, engineers routinely adopt "fail-soft" patterns: if an API call fails or a database field is null, the system catches the exception and returns a default value (`0.50`, `0.0`, or `true`) to keep the user interface responsive.

In high-stakes autonomous systems, **the fail-soft pattern is an existential vulnerability**. As demonstrated in the 900,000-Row Synthetic Poison Catastrophe, defaulting a missing metric to a plausible constant corrupts downstream mathematical solvers, inflating risk calculations and triggering catastrophic real-world liquidations.

**The Fail-Closed Doctrine Mandates:**
1. **Explicit Nullability:** All quantitative functions must return `Optional[T]`.
2. **Zero In-Catch Defaulting:** Catching an exception and returning a positive constant (flagged by AST rule `ZM001`) is a constitutional violation. The handler must return `None` or re-raise a domain exception.
3. **Execution Halting:** If a critical metric (e.g., spot price, vital sign, airspeed) returns `None`, downstream execution must immediately transition to a safe, latched state (`HALT_EXECUTION_DUE_TO_UNVERIFIED_DATA`).

### 4.2 The Zero Hard-Deletes Mandate (ADR-027)

In regulated enterprise environments (FDA 21 CFR Part 11, SEC Rule 17a-4, Sarbanes-Oxley §802), destroying historical data is illegal. Errant, buggy, or invalidated consensus records must never be purged via raw `DELETE FROM table`.

**Quarantine Governance Mechanics:**
1. **Structural Ban on Hard Deletes:** Raw `DELETE` SQL statements against operational ledgers (`consensus`, `executions`, `patient_vitals`) are blocked by database triggers and code linting.
2. **Atomic Quarantine Migration:** When a consensus record is invalidated (due to an upstream bug or data corruption), it must be atomically migrated into an immutable quarantine ledger:
   ```sql
   INSERT INTO consensus_quarantine (id, original_payload, invalidation_reason, bug_reference, quarantined_at)
   VALUES (:id, :payload, 'Stale SOFR imputation bug', 'ISSUE-402', CURRENT_TIMESTAMP);
   ```
3. **Audit Trail Completeness:** Forensic auditors must be capable of reconstructing the exact state of the system at any historical microsecond, proving what data the AI saw and why it made each decision.

---

## 5. The Seven Constitutional Articles

### Article I: Data Minimization & PII Sanitization
The Agent shall actively minimize the exposure and persistence of Personally Identifiable Information (PII) and Protected Health Information (PHI).
- If a query, log trace, or prompt payload can be fulfilled using an anonymized UUID rather than plain-text identifiers (names, emails, medical record numbers), the Agent **MUST** default strictly to the anonymized field.
- The Agent shall never log PII/PHI into console streams, telemetry payloads, or unencrypted error dumps.

### Article II: Principle of Least Privilege
The Agent shall grant the minimum viable permissions required for an infrastructure script, API service, or worker process to execute.
- When generating Infrastructure as Code (Terraform, Kubernetes manifests, IAM roles), the Agent **MUST** default to deny-all and explicitly allow bounded, resource-constrained actions.
- Wildcard permissions (`"Action": "*"`, `"Resource": "*"`) are constitutional violations.

### Article III: Preservation of Core Architecture & Registry Precedence
The Agent shall not introduce foreign architectural frameworks, rogue state stores, or duplicate utility libraries when an approved enterprise primitive exists.
- The Agent **MUST** consult the AST State Registry and Function Registry prior to implementation.
- If an internal mathematical algorithm, logging utility, or database client exists, the Agent **MUST** bind to that verified primitive rather than writing an un-audited implementation from scratch.

### Article IV: Fail-Closed Execution & Zero-Taint State Mutation
The Agent shall assume that all external infrastructure, network sockets, and third-party APIs will experience transient or permanent failure in production.
- All state-mutating operations **MUST** be idempotent and encapsulated within atomic transactional boundaries that rollback cleanly upon failure.
- Silenced exception handlers, empty catch blocks, and optimistic fallback defaults are strictly prohibited. Missing telemetry must fail closed.

### Article V: Traced Causality & Cryptographic Provenance
The Agent shall never generate code, modify schemas, or dispatch autonomous actions without an explicit, auditable chain of causality linking back to verified human intent.
- Every automated commit and PR **MUST** embed an AI-SBOM header declaring the Agent ID, Foundation Model version, Temperature, and governing Context Nodes.
- Every runtime decision payload **MUST** persist a UUIDv4 trace ID into Cloudflare D1 / SQL audit tables.

### Article VI: Algorithmic Fairness & Elimination of Proxy Bias
The Agent shall not construct decision algorithms, scoring models, or filtering logic that utilize protected demographic characteristics (Race, Gender, Religion, Sexual Orientation, Disability) as variables.
- The Agent **MUST** actively detect and reject "Proxy Variables" (e.g., using ZIP codes, credit scores, or social graph density as proxies for protected characteristics in high-stakes clinical or financial allocation).

### Article VII: Model Reproducibility & 7-Year Immutable Audit Trail
The Agent's output is not mere text; it is the deterministic result of an epistemic state machine operating on a specific context vector.
- For all state-mutating and capital-allocating actions, the Agent **MUST** record the exact hydrated prompt digest, model version, and parameter seeds into an immutable audit ledger.
- This immutable record must be retained for the statutory retention period (minimum 7 years) to satisfy regulatory subpoenas, FDA inspections, and forensic audits.

---

## 6. Constitutional Enforcement Architecture

```mermaid
flowchart TD
    subgraph AgentGeneration ["1. Autonomous Agent Generation Lifecycle"]
        PROMPT["Hydrated Context & Task Prompt"] --> AGENT["LLM Agent Generation"]
        AGENT --> CRITIQUE{"Self-Critique Phase: Cross-Reference Constitution"}
        CRITIQUE -- "Violates Invariant / Commandment" --> REJECT_LOCAL["Discard Output & Generate Compliant Alternative"]
        CRITIQUE -- "Compliant" --> OUTPUT_CODE["Emit Generated Code / Artifact"]
    end

    subgraph StaticCI ["2. Deterministic AST CI Gates (Compile Time)"]
        OUTPUT_CODE --> AST_SCAN["scripts/scan_mock_data.py (ZM001-ZM007)"]
        AST_SCAN -- "Mock Violation" --> BLOCK_PR["HALT CI: Block Pull Request"]
        AST_SCAN -- "Pass" --> INVAR_SCAN["scripts/verify_code_invariants.py (I01-I22)"]
        INVAR_SCAN -- "SHA1 Mismatch / Missing Test" --> BLOCK_PR
        INVAR_SCAN -- "Pass" --> LOC_SCAN["verify_loc_ceiling.py (ADR-016 <= 400 LOC)"]
        LOC_SCAN -- "LOC > 400" --> BLOCK_PR
        LOC_SCAN -- "Pass" --> MERGE["Authorized for Staging"]
    end

    subgraph RuntimeGov ["3. Runtime Circuit Breakers & Quarantine (Execution Time)"]
        MERGE --> RUNTIME["Runtime Execution Pipeline"]
        RUNTIME --> CB{"Zero-Mock Circuit Breaker (ADR-029)"}
        CB -- "Unverified / Synthetic" --> DEMOTE["Demote to HALT_EXECUTION (Confidence = 0)"]
        CB -- "Live Provenance" --> SOLV{"Merton Solvency / Plausibility Envelope"}
        SOLV -- "Envelope Breached" --> QUARANTINE["Isolate Record to consensus_quarantine (ADR-027)"]
        SOLV -- "Passed All Invariants" --> SAFE_DISPATCH["SAFE DISPATCH TO SYSTEM ACTUATORS"]
    end

    style AgentGeneration fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px;
    style StaticCI fill:#ffebee,stroke:#c62828,stroke-width:2px;
    style RuntimeGov fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
```

---

[**Next: The Context Pipeline →**](./00_THE_CONTEXT_PIPELINE.md) | [**Return to Root README →**](./README.md)
