# Capstone Lab Workbook: Assembling & Certifying an Enterprise Autonomous Agent

---

## 🎯 Executive Overview & Lab Objectives

In this capstone lab, you act as the **Principal AI Systems Orchestrator**. You will synthesize the deliverables authored across all functional roles (Strategy Lead, Requirements Lead, Software Builder, Validation Lead, and BuilderOps Engineer) into an assembled, tested, and certified autonomous software engineering agent.

By completing this lab, you will:
1. Construct the complete 7-layer agent configuration schema (`.github/agents/enterprise-agent.yaml`).
2. Implement and mount the deterministic AST Living Context compiler (<1,500 tokens).
3. Connect strictly-typed function actuators with runtime schema validation.
4. Implement the **3-Stage Dialectical Adversarial Triad** (Proponent, Adversary, Auditor) with zero-compute Jensen-Shannon Divergence bypass ($\text{JSD} \le 0.12$).
5. Enforce non-negotiable physical invariant clamps ($I_{01}$ Zero-Simulated-Data and $I_{02}$ Pre-Action Plausibility Bands).
6. Embed automated AI-SBOM cryptographic audit traceability (SPDX 3.0).
7. Validate your assembled agent against offline hermetic test suites (`pytest tests/ --disable-socket`).

```mermaid
flowchart TD
    subgraph Step1 ["Step 1: Cognitive Soul"]
        S1["3-Part Directive & Identity<br>(Layer 1: Context, Instruction, Guardrails)"]
    end

    subgraph Step2 ["Step 2: Invariant Binding"]
        S2["Closed-World Schema & Invariants<br>(Layer 2: I01-I22 & 20-Row Edge-Case Matrix)"]
    end

    subgraph Step3 ["Step 3: Living Context"]
        S3["AST Context Compiler<br>(Layer 3: &lt;1,500 tokens, Zero Vector Drift)"]
    end

    subgraph Step4 ["Step 4: Actuation Tools"]
        S4["Function Registry & Tool Payloads<br>(Layer 4: OpenAPI 3.1 & MCP Validation)"]
    end

    subgraph Step5 ["Step 5: Dialectical Triad"]
        S5["Multi-Agent Consensus Engine<br>(Layer 5: Proponent, Adversary, JSD &le; 0.12 Bypass)"]
    end

    subgraph Step6 ["Step 6: Plausibility Clamps"]
        S6["Physical Execution Envelopes<br>(Layer 6: &verbar;V_exec - Baseline&verbar; &le; Band)"]
    end

    subgraph Step7 ["Step 7: Hermetic Certification"]
        S7["Cryptographic Trace & Offline CI<br>(Layer 7: SPDX 3.0 AI-SBOM & pytest --disable-socket)"]
    end

    S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7

    style Step1 fill:#f8f9fa,stroke:#495057,stroke-width:2px;
    style Step2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px;
    style Step3 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    style Step4 fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    style Step5 fill:#fce4ec,stroke:#c2185b,stroke-width:2px;
    style Step6 fill:#ede7f6,stroke:#512da8,stroke-width:2px;
    style Step7 fill:#e0f2f1,stroke:#00796b,stroke-width:2px;
```

---

## 🛠️ Lab Prerequisites & Hermetic Environment Setup

Enterprise AI systems in high-stakes regulated domains must execute under strict network boundaries. Verify that your environment is configured for offline hermetic testing:

```bash
# 1. Verify Python virtual environment (Python 3.11+)
python3 --version

# 2. Confirm hermetic testing dependencies
pytest --version

# 3. Verify zero external network egress during test execution
pytest tests/ --disable-socket -v
```

---

## 🏗️ Step 1: Cognitive Soul & Directive Definition (Layer 1: Identity & Constitution)

The agent cognitive soul defines its deterministic purpose, operational domain, and bounded output structure. You will formulate this using the **3-Part Directive Framework**:
1. **Context**: Operational environment, current domain boundaries, and governing invariants.
2. **Instruction**: Unambiguous imperative task logic written in ASD-STE100 (Simplified Technical English).
3. **Execution Guardrails**: Deterministic failure conditions, token quotas, and forbidden operations.

### Configuration Template: `instructions.md`
```markdown
# Autonomous System Instruction: Payment Settlement Routing Engine

## 1. Context & Operational Scope
You are the Autonomous Liquidity Routing Agent for the Core Banking Settlement Network.
You operate under Federal Reserve SR 11-7 model governance and Article I data minimization standards.
You do not possess authority to modify ledger accounts directly; you output signed transaction recommendations.

## 2. Deterministic Imperative Task
Process incoming interbank settlement tickets and calculate optimal routing pathways:
- Ingest ticket amount $T$, source BIC, destination BIC, and timestamp $\tau$.
- Verify counterparty solvency and currency liquidity depth via registered tools.
- Evaluate routing risk using the 4 orthogonal validation pillars: Velocity, Biometrics, Solvency, Liquidity.
- Emit a strongly-typed settlement recommendation matching the JSON schema `schemas/settlement_decision.json`.

## 3. Mandatory Execution Guardrails
- Invariant I01: If any counterparty balance or exchange rate returns null, NaN, or simulated data, reject the ticket immediately.
- Invariant I02: Clamped settlement limits: $|T - \mu_{\text{historical}}| \le 3.5\sigma$.
- Architectural Modularity Heuristic: Target <= 400 lines of code to maintain SRP and cognitive bounds.
- Epistemic Air-Gap: Never evaluate unverified external payloads without telemetry normalization.
```

---

## 🧠 Step 2: Deterministic AST Context Memory Assembly (Layer 3: AST Memory)

Enterprise agents must never ingest unbounded source code. Instead, compile a living context payload strictly bounded below 1,500 tokens.

```python
"""
compile_living_context.py: Deterministic Context Compiler
Extracts exact signatures and invariants from AST state registries without vector drift.
"""
import json
import re
from pathlib import Path

def compile_context(registry_path: Path, max_tokens: int = 1500) -> dict:
    if not registry_path.exists():
        raise FileNotFoundError(f"State registry missing: {registry_path}")
        
    with open(registry_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract function signatures and invariant identifiers using regex
    signatures = re.findall(r"def\s+([a-zA-Z0-9_]+\([^)]*\))", content)
    invariants = re.findall(r"(I[0-9]{2}:[^\n]+)", content)

    context_payload = {
        "version": "1.0.0",
        "ast_signatures": signatures[:25],
        "active_invariants": invariants[:10],
        "token_estimate": len(signatures) * 12 + len(invariants) * 15
    }

    if context_payload["token_estimate"] > max_tokens:
        raise ValueError(f"Context payload ({context_payload['token_estimate']} tokens) exceeds ceiling of {max_tokens}!")

    return context_payload

if __name__ == "__main__":
    context = compile_context(Path("03_building_and_coding/STATE_REGISTRY.md"))
    print(f"Context compiled successfully: {json.dumps(context, indent=2)}")
```

---

## 🔧 Step 3: Tool Mounting & Function Registry (Layer 4: Actuation Tools)

Agents must only interact with physical environments through strongly-typed schemas. Mount tools using the OpenAPI 3.1 / Model Context Protocol format:

```yaml
# tools_manifest.yaml
tools:
  - name: "query_liquidity_depth"
    description: "Queries real-time verified central bank liquidity depth for a currency pair."
    parameters:
      type: "object"
      properties:
        currency_pair:
          type: "string"
          pattern: "^[A-Z]{3}/[A-Z]{3}$"
        timestamp_utc:
          type: "string"
          format: "date-time"
      required: ["currency_pair", "timestamp_utc"]
      additionalProperties: false

  - name: "evaluate_counterparty_solvency"
    description: "Evaluates real-time solvency ratio for a correspondent banking counterparty."
    parameters:
      type: "object"
      properties:
        bic_code:
          type: "string"
          pattern: "^[A-Z0-9]{8,11}$"
      required: ["bic_code"]
      additionalProperties: false
```

---

## ⚖️ Step 4: Dialectical Adversarial Triad & Consensus Gate (Layer 5: Adversarial Bounds)

Configure the 3-stage multi-agent consensus engine to prevent single-model sycophancy.

```mermaid
flowchart TD
    A["Raw Ingress Task"] --> B["Proponent Agent (Draft Recommendation)"]
    A --> C["Adversary Agent (Failure Mode Stress-Test)"]
    A --> D["Forensic Auditor Agent (Invariant Compliance)"]
    
    B & C & D --> E["Consensus Evaluator (Compute JSD)"]
    E --> F{"JSD <= 0.12?"}
    
    F -- "Yes (Consensus)" --> G["Fast-Path Execution (Zero Arbitration Cost)"]
    F -- "No (Divergence)" --> H["Convex Log-Odds Evidence Arbiter"]
    H --> I["Synthesized Balanced Action"]
    
    G & I --> J["Pre-Action Plausibility Band Clamp (I02)"]
```

### Implementing the Fast-Path JSD Evaluator in Python:

```python
import numpy as np

def compute_jsd(p: np.ndarray, q: np.ndarray) -> float:
    """Computes Jensen-Shannon Divergence between two probability distributions (Lin, 1991)."""
    m = 0.5 * (p + q)
    kl_pm = np.sum(np.where(p > 0, p * np.log2(p / m), 0.0))
    kl_qm = np.sum(np.where(q > 0, q * np.log2(q / m), 0.0))
    return float(0.5 * (kl_pm + kl_qm))

def evaluate_consensus(proponent_scores: list[float], adversary_scores: list[float]) -> tuple[bool, float]:
    p = np.array(proponent_scores, dtype=float)
    q = np.array(adversary_scores, dtype=float)
    p = p / np.sum(p)
    q = q / np.sum(q)
    
    jsd_val = compute_jsd(p, q)
    # Threshold for fast-path consensus bypass: JSD <= 0.12
    is_consensus = jsd_val <= 0.12
    return is_consensus, jsd_val
```

---

## 🛡️ Step 5: Runtime Physical Invariant Guardrails & Plausibility Clamps (Layer 6: Execution Clamps)

Enforce physical invariant clamps on all proposed actions before physical state commitment:

```python
class InvariantViolationError(Exception):
    """Raised when an agent action violates a non-negotiable physical invariant."""
    pass

def enforce_settlement_guardrails(proposed_transfer: float, historical_mean: float, std_dev: float, is_simulated: bool) -> float:
    # Invariant I01: Zero-Simulated-Data Guardrail
    if is_simulated:
        raise InvariantViolationError("Invariant I01 Violation: Simulated test data detected in production pathway!")

    # Invariant I02: Pre-Action Plausibility Band (|T - mu| <= 3.5 * sigma)
    max_band = historical_mean + (3.5 * std_dev)
    min_band = max(0.0, historical_mean - (3.5 * std_dev))

    if proposed_transfer > max_band:
        raise InvariantViolationError(
            f"Invariant I02 Violation: Proposed transfer ${proposed_transfer:,.2f} exceeds dynamic upper band ${max_band:,.2f}!"
        )
    if proposed_transfer < min_band:
        raise InvariantViolationError(
            f"Invariant I02 Violation: Proposed transfer ${proposed_transfer:,.2f} below dynamic lower band ${min_band:,.2f}!"
        )

    return proposed_transfer
```

---

## 📜 Step 6: Immutable AI-SBOM & Audit Custody (Layer 7: Audit Custody)

Every output emitted by the agent must carry a cryptographically verifiable SPDX 3.0 provenance header:

```json
{
  "spdx_version": "SPDX-3.0",
  "data_license": "CC0-1.0",
  "spdx_id": "SPDXRef-AgentExecution-c8f9b42e",
  "name": "SettlementRoutingDecision",
  "creation_info": {
    "created": "2026-10-17T23:30:00Z",
    "creators": ["Tool: AutonomousSettlementEngine-v2.4.1"],
    "model_digest": "sha256:4b9a8f12d8e037c28e914df5a02e8d35688a44b1",
    "execution_temperature": 0.0,
    "uuidv4_trace": "c8f9b42e-9d21-4a56-b183-f54210e7b891"
  },
  "invariants_certified": ["I01", "I02", "I09", "I15"],
  "decision_payload": {
    "action": "ROUTE_TRANSFER",
    "target_gateway": "FEDWIRE_GATEWAY_01",
    "amount_usd": 2500000.00
  }
}
```

---

## 🔬 Hands-on Implementation: Track A vs. Track B

Select your designated capstone implementation track:

### Track A: FDA SaMD Closed-Loop Clinical Titration Agent
* **Domain**: Healthcare Medical Device (FDA 21 CFR Part 820.30, ISO 13485).
* **Sensor Input**: Continuous Glucose Monitor (CGM) sensor telemetry stream.
* **Governing Invariants**:
  - $I_{01}$: Corrupted CGM packet (`NaN`, negative glucose, or stale timestamp > 15 min) triggers immediate system halt and clinical alarm.
  - $I_{02}$: Insulin bolus adjustment clamped to physiological limits: $|\Delta \text{Dose}| \le 2.0\text{ Units}$.
  - $I_{04}$: Quarantined telemetry routed to `clinical_telemetry_quarantine` table with zero hard deletion.

### Track B: High-Value Financial Wire & Liquidity Router
* **Domain**: Core Banking / Interbank Settlement (Federal Reserve SR 11-7, SOX 404).
* **Input**: Ingress settlement transfer ticket from SWIFT/ISO 20022 messaging gateway.
* **Governing Invariants**:
  - $I_{01}$: Synthetic or mock market data in routing pathway raises fatal error.
  - $I_{02}$: Transfer value clamped to statistical volatility window: $|T - \mu| \le 3.5\sigma$.
  - $I_{09}$: Compensatory confluence requires positive sign across $\ge 2$ orthogonal risk pillars.

---

## 🧪 Step 7: Automated Verification & Certification Run

Execute the hermetic test suite to prove full compliance with zero external dependencies:

```bash
# Run hermetic test suite with offline network isolation
pytest tests/ --disable-socket -v

# Run AST Zero-Mock static scanner across the repository
python3 scripts/scan_mock_data.py --path .

# Confirm 100% zero-drift between registries and living context
python3 scripts/verify_context_drift.py
```

### Passing Verification Checklist:
- [ ] 0 unit test failures under `pytest --disable-socket`.
- [ ] 0 AST Zero-Mock violations (rules ZM001 through ZM009 satisfied).
- [ ] 0 bare ADR acronyms (all guardrails fully spelled out).
- [ ] Living context compilation size strictly $< 1,500$ tokens.
- [ ] Context Debt Ratio compliant ($\text{CDR}_{\text{token}} \le 0.18$, $\text{CDR}_{\text{structural}} \le 0.05$).
- [ ] Prompt Regression Interval compliant ($\text{PRI}_{\text{turns}} \le 3$, $\text{PRI}_{\text{hours}} \le 0.08$).
- [ ] All Mermaid diagrams validated with 0 syntax errors.

---

## Production Reality & Operational Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)
The mid-2026 median engineer treats agent development like prompt prototyping. At the 75\%–84\% industry baseline, developers paste messy Python into a chat sidebar, ask for an "agentic loop," and commit whatever inline ghost-text appears.

> [!WARNING]
> **The Mock Contamination Trap**: When testing, median teams write unit tests stuffed with `unittest.mock.MagicMock` patches that mock network calls, sensor inputs, and state validation. These tests pass with 100\% green bars but verify nothing about runtime behavior.

The team falls into the DORA Verification Trap. Engineers spend days debugging deceptive hallucinations masked by tautological mocks, spiking PR review bloat by +91\% as reviewers untangle why an agent passed local mocks but corrupted production state.

### Ungoverned Production Failure Modes
When engineering teams treat agent testing as optional prompt engineering and deploy unanchored workflows into production:
- **Mock Contamination & Silent Failures**: Synthetic fallbacks (such as numeric returns in `except` blocks or default empty dictionaries, violating rules ZM001–ZM007) will cause the agent to swallow upstream network drops or schema mismatches. Instead of failing closed, the agent silently feeds garbage data into downstream actuators.
- **Context Bloat & Token Runaway**: Without compiling a Living Context under 1,500 tokens and monitoring Context Debt Ratio ($\text{CDR} \le 0.18$), prompt context balloons into hundreds of thousands of tokens, triggering attention dilution, position-dependent lost-in-the-middle degradation, and multiplying API token costs.
- **Review Gridlock**: Reviewers will reject 3,000-line monolithic agent PRs because no human can reason about multi-turn agent state transitions without deterministic AST scans and hermetic boundary guarantees.

### Deterministic Engineering Defenses & Operational Takeaways
1. **Install AST Zero-Mock Verification as a CI Gate**: Add `python3 scripts/scan_mock_data.py --path .` to the CI pipeline. Any PR containing banned mock prefixes (`mock_`, `fake_`), default dictionary fallbacks (`ZM006`), or boolean error fallbacks (`ZM007`) is rejected before review.
2. **Compile Context from AST Registries**: Stop manually editing prompt strings. Automatically compile agent context from `STATE_REGISTRY.md` and `MATHEMATICAL_REGISTRY.md` via `scripts/compile_living_context.py`, enforcing a strict $< 1,500$ token ceiling.
3. **Execute Cartesian Fault-Injection Testing**: Before writing happy-path unit tests, write three adversarial tests: one injecting `NaN`/`Inf` floats, one injecting boolean smuggling (`isinstance(True, int)`), and one simulating total socket loss (`--disable-socket`). The agent must fail closed in all three.
4. **Enforce the Prompt Regression Interval Limit**: Measure Prompt Regression Interval ($\text{PRI}_{\text{turns}} \le 3$). If an agent cannot stabilize its execution within three automated turns, cut execution and fall back to a deterministic closed-world baseline.

---

[**Return to Capstone Architecture Overview →**](./README.md) | [**Return to Root Curriculum Overview →**](../README.md)
