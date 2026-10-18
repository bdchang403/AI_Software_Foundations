# Lab Workbook: Registries, Chaining, & Zero-Drift Routing

## 🎯 Lab Objectives
By completing this workbook, Software Engineers and System Architects will master:
1. **Embedding & Verifying SHA1 Invariant Anchors**: Programmatically generating and validating `# === INVARIANT-BLOCK` checksums ($I_{01}$–$I_{22}$).
2. **Constructing an AST State Registry Parser**: Extracting physical line counts, classes, public function signatures, and Architectural Modularity Target (~400 LOC) health flags.
3. **Compiling Living Context Payloads**: Generating minified JSON (<1,500 tokens) with strict dual-schema table-to-DTO mappings.
4. **Executing the Zero-Drift Pre-Commit Chain**: Enforcing `git diff --exit-code` and resolving AST drift in local development.
5. **Enforcing Rule 14 Anti-Feature-Erasure**: Decomposing files exceeding modularity thresholds ($\ge 350$ LOC) without truncating error handlers or assertions.

---

## 🧪 Lab 1: Embedding & Verifying an Invariant Anchor (Module 6)

### Scenario
You are modifying the execution gateway in `src/execution/execution_gateway.py`. The governing architectural decision is **ADR-029 (Pre-Action Execution Plausibility Envelope Guardrail)**, and the governing constraint is **Invariant $I_{02}$ (Execution-Price Guardrail)**.

The invariant predicate states:
`Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)`

### Your Task
1. Write a Python script to compute the deterministic 8-character SHA1 checksum using the formula:
   $$\text{Checksum} = \mathrm{SHA1}\left(\text{AnchorPayload}\right)[:8]$$
2. Confirm that the computed checksum equals `037a1c64`.
3. Construct the complete code comment anchor block.

### Step-by-Step Implementation & Answer Key
```python
import hashlib

def generate_anchor_block(inv_id: str, adr: str, predicate: str) -> str:
    raw_str = f"{inv_id.strip()}|{adr.strip()}|{predicate.strip()}"
    checksum = hashlib.sha1(raw_str.encode("utf-8")).hexdigest()[:8]
    
    return (
        f"# === INVARIANT-BLOCK v1 ===\n"
        f"# INVARIANT: {inv_id.strip()}\n"
        f"# ADR: {adr.strip()}\n"
        f"# PREDICATE: {predicate.strip()}\n"
        f"# /INVARIANT [sha1:{checksum}]\n"
        f"# === /INVARIANT-BLOCK ==="
    )

anchor = generate_anchor_block(
    "I02",
    "ADR-029",
    "Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)"
)
print(anchor)
assert "sha1:037a1c64" in anchor
print("✅ Checksum verified: 037a1c64")
```

---

## 🧪 Lab 2: Building an AST State Registry Parser (Module 4)

### Scenario
You must implement a standalone AST indexer that scans Python files in a directory, extracts non-private functions and classes, counts physical lines, and asserts whether the file satisfies the Architectural Modularity warning threshold ($< 350$ lines).

### Your Task
Create `parse_module_topography(file_path: Path) -> dict` utilizing Python's native `ast` library.

### Step-by-Step Implementation & Answer Key
```python
import ast
from pathlib import Path
from typing import Dict, Any, List

def parse_module_topography(file_path: Path) -> Dict[str, Any]:
    source = file_path.read_text(encoding="utf-8")
    lines = source.splitlines()
    total_loc = len(lines)
    
    tree = ast.parse(source, filename=str(file_path))
    classes: List[str] = []
    public_functions: List[str] = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            public_functions.append(node.name)
            
    is_healthy = total_loc < 350
    status_flag = "✅ Healthy (<350 LOC)" if is_healthy else "⚠️ Modularity Warning Zone (>=350 LOC)"
    
    return {
        "file": str(file_path.name),
        "total_loc": total_loc,
        "classes": sorted(classes),
        "public_functions": sorted(public_functions),
        "status_flag": status_flag,
        "is_healthy": is_healthy
    }
```

---

## 🧪 Lab 3: Compiling Living Context with Dual-Schema Parity (Module 4)

### Scenario
To prevent LLM database column hallucinations (such as `SELECT * FROM historical_sentiment`), you must compile a minified JSON dictionary mapping active SQL tables to their backing Pydantic DTO models and files.

### Your Task
Construct `generate_living_context_payload()` that compiles:
1. `table_dto_map`: All production tables mapped to model classes and source files.
2. `canonical_math_algorithms`: Key algorithms with exact file and symbol coordinates.
3. Assert that the total compiled JSON payload is under 1,500 tokens.

### Step-by-Step Implementation & Answer Key
```python
import json
from typing import Dict, Any

def generate_living_context_payload() -> Dict[str, Any]:
    payload = {
        "active_models": {
            "flagship": "claude-3-7-sonnet-20250219",
            "fast": "google/gemini-2.0-flash-001"
        },
        "table_dto_map": {
            "daily_prices": {"model": "DailyPriceDTO", "file": "src/schemas/daily_prices.py"},
            "consensus": {"model": "ConsensusVerdict", "file": "src/schemas/debate.py"},
            "consensus_quarantine": {"model": "QuarantineRecord", "file": "src/utils/quarantine.py"},
            "cost_logs": {"model": "CostEntry", "file": "src/pipeline/cost_ledger.py"}
        },
        "canonical_math_algorithms": {
            "Alg_42_PlausibilityBand": {"file": "src/execution/gateway.py", "symbol": "validate_order"},
            "Alg_89_ZCAWhitening": {"file": "src/math/whitening.py", "symbol": "anchor_preserving_zca_whitening"}
        },
        "inviolable_rules": [
            "Architectural Modularity Target: ~400 LOC heuristic target per file.",
            "Zero-Mock: Return None or raise on missing data; zero synthetic constants.",
            "Compensatory Confluence: >=2 of 4 pillars unblock BUY."
        ]
    }
    
    # Estimate token count (approx 4 chars per token)
    json_str = json.dumps(payload, indent=2)
    estimated_tokens = len(json_str) // 4
    assert estimated_tokens < 1500, f"Payload exceeded 1,500 tokens: {estimated_tokens}"
    return payload
```

---

## 🧪 Lab 4: Executing the Zero-Drift Command Chain (Module 6)

### Scenario
An autonomous agent modified `src/math/whitening.py` by adding an assertion, shifting the line numbers of `anchor_preserving_zca_whitening()` by 4 lines.

### Your Task
Execute the pre-commit chain to detect and eliminate AST drift:
1. Stage your code modification.
2. Run generator scripts to re-align registries.
3. Assert zero uncommitted drift exists via `git diff --exit-code` before staging.
4. Stage the verified synchronized registries and commit cleanly.

### Step-by-Step Shell Commands
```bash
# 1. Stage modified code
git add src/math/whitening.py

# 2. Run AST Topography and Mathematical Indexers to regenerate registries
python3 scripts/update_state_registry.py
python3 scripts/update_math_registry.py
python3 scripts/generate_living_context.py

# 3. Assert zero uncommitted drift exists before staging (matching 03_06 atomic chain):
git diff --exit-code STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json

# 4. Stage the verified synchronized registries:
git add STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json

# 5. Execute in-memory verification suite
python3 -m pytest tests/unit/test_context_freshness.py
```

---

## 🧪 Lab 5: Applying Rule 14 Anti-Feature-Erasure (Module 3)

### Scenario
A file `risk_manager.py` is at **380 physical lines**. An unconstrained AI agent was tasked with adding a new volatility filter, and submitted a PR that reduced the file to 320 lines by replacing 80 lines of multi-tier broker fallbacks with `# ... remaining broker logic ...`.

### Your Task
Identify the Rule 14 violation and apply genuine architectural decomposition.

### Evaluation & Remediation Rubric
* **Violation Detected**: Compression Cheating / Silent Feature Erasure. The agent deleted critical runtime error recovery to satisfy the ~400-LOC modularity target.
* **Remediation Action**: Reject the PR. Decompose `risk_manager.py` by extracting `broker_fallbacks.py` (110 LOC) and `volatility_filter.py` (90 LOC), reducing the primary risk manager to 200 LOC while preserving 100% of safety handlers.

---

## ✅ Mastery Verification Checklist
- [ ] Computed and verified the exact SHA1 checksum for Invariant $I_{02}$ (`037a1c64`).
- [ ] Built an AST parser identifying classes, public functions, and the 350-LOC modularity review trigger.
- [ ] Confirmed that `openrouter_context.json` maps SQL tables to DTOs in under 1,500 tokens.
- [ ] Executed the atomic pre-commit command chain with clean zero-diff exit status.
- [ ] Enforced Rule 14 Anti-Feature-Erasure against compression cheating.
