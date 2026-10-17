# Production Implementation: Function & Tool Registry Schemas

This document defines the production standard for mapping a 500,000-LOC enterprise codebase into machine-executable **Model Context Protocol (MCP)** and OpenAI Tool Calling schemas.

## ⚠️ Core Architectural Doctrine

**DO NOT grant autonomous AI agents unconstrained read/write filesystem access to your repository.** 

Granting an unconstrained agent bash access or raw filesystem tools results in multi-hop directory scans, token exhaustion, and accidental modification of out-of-scope files. Instead, agents must interact with the codebase through **Strict Abstract Tools** defined by these schemas.

> **The Registry as a Knowledge Graph**: A Function Registry is not merely a tool execution permission list; it acts as an architectural knowledge graph. It defines explicit upstream prerequisites and downstream side-effects, allowing agents to orient themselves within complex microservice boundaries in <2 seconds.

---

## 🛠️ Canonical Architecture Tools for Autonomous Builders

### 1. Codebase Routing Tool: `read_domain_context`
When an AI agent needs to understand domain rules, it must call this tool to retrieve the Tier 2 Domain Context. Handing the agent this bounded tool prevents it from scanning the directory tree.

```json
{
  "name": "read_domain_context",
  "description": "Reads the localized architectural context and ADRs for a specific domain mapped in the Semantic Blueprint. Use before writing code to understand existing interface contracts and invariants.",
  "parameters": {
    "type": "object",
    "properties": {
      "domain_name": {
        "type": "string",
        "enum": ["billing", "order_execution", "market_data", "infusion_control", "navigation"],
        "description": "The authoritative domain name specified in the Semantic Blueprint."
      },
      "max_lines": {
        "type": "integer",
        "description": "Hard limit on lines returned to prevent token attention dilution (ADR-016 compliant). Maximum 80 lines.",
        "default": 80
      }
    },
    "required": ["domain_name"]
  }
}
```

---

### 2. Living Context Query Tool: `query_living_context`
Allows an agent to inspect the active table-to-DTO mappings and canonical mathematical algorithms without loading large markdown files.

```json
{
  "name": "query_living_context",
  "description": "Queries the minified Living Context (openrouter_context.json) to retrieve active D1 SQL table schemas, Pydantic DTO models, or canonical algorithm signatures.",
  "parameters": {
    "type": "object",
    "properties": {
      "query_type": {
        "type": "string",
        "enum": ["table_dto_map", "canonical_math_algorithms", "inviolable_rules", "active_models"],
        "description": "The category of living context information requested."
      },
      "filter_key": {
        "type": "string",
        "description": "Optional specific table name (e.g., 'daily_prices') or algorithm name (e.g., 'CUSUM')."
      }
    },
    "required": ["query_type"]
  }
}
```

---

### 3. Invariant Anchor Verifier Tool: `verify_ast_invariant_anchor`
Allows an agent to compute and verify the cryptographic SHA1 checksum of an `# === INVARIANT-BLOCK` before generating code diffs.

```json
{
  "name": "verify_ast_invariant_anchor",
  "description": "Computes and verifies the deterministic 8-character SHA1 checksum for a code-adjacent invariant anchor block: sha1(inv_id|adr|predicate)[:8].",
  "parameters": {
    "type": "object",
    "properties": {
      "invariant_id": {
        "type": "string",
        "description": "Canonical invariant identifier, e.g., 'I02'."
      },
      "governing_adr": {
        "type": "string",
        "description": "Governing Architectural Decision Record, e.g., 'ADR-029'."
      },
      "predicate_text": {
        "type": "string",
        "description": "The exact single-line mathematical or logical predicate string."
      }
    },
    "required": ["invariant_id", "governing_adr", "predicate_text"]
  }
}
```

---

### 4. Contract & Dependency Query Tool: `get_contract_schema_and_dependencies`
Retrieves the TypeScript interface, Python DTO dataclass, and dependency map for internal service calls. It explicitly lists the required upstream checks and downstream side-effects.

```json
{
  "name": "get_contract_schema_and_dependencies",
  "description": "Retrieves the typed interface, schema validation rules, and upstream/downstream dependency graph for a domain service.",
  "parameters": {
    "type": "object",
    "properties": {
      "service_intent": {
        "type": "string",
        "enum": ["OrderExecution", "VasopressorTitration", "AuditLogging", "ConsensusAggregation"],
        "description": "The high-level service boundary."
      },
      "include_dependencies": {
        "type": "boolean",
        "description": "If true, returns upstream prerequisites and downstream impacted services.",
        "default": true
      }
    },
    "required": ["service_intent"]
  }
}
```

---

## 💻 Python Orchestrator Integration Example

The following self-contained Python script illustrates how an enterprise orchestration layer exposes these tools to an autonomous coding agent via standard OpenAI / OpenRouter function calling:

```python
"""
function_registry_orchestrator.py
Exposes strictly bounded architecture tools to autonomous AI agents.
"""
import hashlib
import json
from pathlib import Path
from typing import Dict, Any, List

REPO_ROOT = Path(__file__).resolve().parent.parent


def execute_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Executes a registered function call and returns a deterministic string result."""
    
    if tool_name == "verify_ast_invariant_anchor":
        inv_id = arguments["invariant_id"].strip()
        adr = arguments["governing_adr"].strip()
        predicate = arguments["predicate_text"].strip()
        raw = f"{inv_id}|{adr}|{predicate}"
        checksum = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8]
        return json.dumps({
            "invariant_id": inv_id,
            "adr": adr,
            "predicate": predicate,
            "computed_sha1": checksum,
            "anchor_block": (
                f"# === INVARIANT-BLOCK v1 ===\n"
                f"# INVARIANT: {inv_id}\n"
                f"# ADR: {adr}\n"
                f"# PREDICATE: {predicate}\n"
                f"# /INVARIANT [sha1:{checksum}]\n"
                f"# === /INVARIANT-BLOCK ==="
            )
        })

    elif tool_name == "read_domain_context":
        domain = arguments["domain_name"]
        max_lines = min(80, arguments.get("max_lines", 80))
        target = REPO_ROOT / "docs" / "context" / f"{domain}.md"
        if not target.exists():
            return json.dumps({"error": f"Domain context '{domain}' not found."})
        lines = target.read_text(encoding="utf-8").splitlines()[:max_lines]
        return json.dumps({"domain": domain, "content": "\n".join(lines)})

    elif tool_name == "query_living_context":
        ctx_file = REPO_ROOT / "data" / "openrouter_context.json"
        if not ctx_file.exists():
            return json.dumps({"error": "openrouter_context.json not found."})
        data = json.loads(ctx_file.read_text(encoding="utf-8"))
        category = arguments["query_type"]
        filter_key = arguments.get("filter_key")
        
        result = data.get(category, {})
        if filter_key and isinstance(result, dict):
            result = {filter_key: result.get(filter_key, "Not found")}
        return json.dumps({"query_type": category, "result": result})

    return json.dumps({"error": f"Unknown tool: {tool_name}"})
```

---

## ⚖️ Dual-Use Regulated Callout Box: Tool Registries in Safety-Critical Systems

::: tip DUAL-USE ANALYSIS: RESTRICTED TOOL SURFACES ACROSS REGULATED INDUSTRIES
| Tool Registry Dimension | Quantitative Trading Systems | FDA Class III Medical Devices | Aerospace Avionics (DO-178C) |
| :--- | :--- | :--- | :--- |
| **Banned Actions** | Agents cannot directly emit FIX orders or execute raw SQLite drop commands. | Agents cannot directly write to motor driver DAC registers or override alarm thresholds. | Agents cannot write directly to servo command registers or alter ARINC 429 databus tables. |
| **Allowed Tools** | `validate_order_bounds`, `query_market_depth`, `verify_invariant_anchor`. | `validate_titration_step`, `query_patient_limits`, `verify_device_hazard_mitigation`. | `compute_surface_deflection`, `query_aerodynamic_polar`, `verify_do178c_traceability`. |
| **Dependency Graph** | `OrderExecution` requires upstream `AuthService` and `RiskPlausibilityGate`. | `BolusDelivery` requires upstream `SensorValidityCheck` and `AirInLineSensorGate`. | `ActuatorCommand` requires upstream `TripleModularVoter` and `HydraulicPressureCheck`. |
:::

---
[**Proceed to Builder Reference Architecture →**](./REFERENCE_ARCHITECTURE.md)
