# Module 6: Information Routing Structure & Zero-Drift Pre-Commit Sentinels

## 🏗️ The Context-First Repository Architecture

To prevent token exhaustion and ensure an autonomous AI agent (such as Claude, Gemini, Grok, or DeepSeek) can reliably traverse your codebase without losing architectural alignment, systems engineers and architects must structure the repository as an **Explicit Machine-Readable Context Map**.

Instead of placing all architectural rules into a massive root prompt, the Context Factory utilizes a **2-Tier Precision Structure**:
1. **Tier 1 (The Global Router)**: A thin file (~50 lines) loaded automatically by the IDE or agent runner. It acts as a traffic controller, evaluating the active file path and directing the AI to the appropriate domain context.
2. **Tier 2 (The Domain Knowledge & Registries)**: Localized markdown and JSON specifications containing domain boundaries, ADRs, database DTO mappings, and active task requirements.

```text
your-enterprise-repo/
├── ⚙️ .github/
│   ├── copilot-instructions.md          <-- Tier 1: The Global Router (~50 lines)
│   └── workflows/
│       └── drift-monitor.yml            <-- Remote CI Zero-Drift Sentinel
├── 📘 docs/
│   ├── context/                         <-- Tier 2: Surgical Domain Knowledge
│   │   ├── billing.md                   <-- Bounded context, ADRs & state models
│   │   ├── order_execution.md
│   │   └── telemetry.md
│   ├── registries/                      <-- Deterministic Machine Registries
│   │   ├── STATE_REGISTRY.md            <-- AST repo topography (<5k tokens)
│   │   └── MATHEMATICAL_REGISTRY.md     <-- 100 Canonical Algorithms & line coordinates
│   └── stories/                         <-- Active Context-Enriched Semantic Blueprints
│       └── FEAT-101-execution-gate.md
├── 📦 data/
│   └── openrouter_context.json          <-- Living Context (<1,500 tokens, dual-schema map)
├── 🛠️ scripts/
│   ├── update_state_registry.py         <-- AST Topography Generator
│   ├── update_math_registry.py          <-- Algorithmic LaTeX & AST Coordinate Generator
│   ├── generate_living_context.py       <-- Dual-Schema Parity & Context Minifier
│   └── verify_code_invariants.py        <-- SHA1 Invariant Anchor Verifier
└── 🏗️ src/
    └── [your domain code adhering to Architectural Modularity Ceiling <= 400 LOC]
```

### Tool-Specific Entry Points (Tier 1)
While the 2-Tier routing philosophy is universal, the entry-point file path varies by agentic environment:
* **GitHub Copilot**: `.github/copilot-instructions.md`
* **Cursor**: `.cursorrules` in repository root
* **Claude Code**: `CLAUDE.md` in repository root
* **Antigravity**: `.antigravity/instructions.md`

Regardless of tooling, **Tier 1 must remain a thin router** containing hardcoded file pointers rather than exhaustive documentation.

---

## 🔒 Code-Adjacent SHA1 Invariant Anchors ($I_{01}$–$I_{22}$)

A primary failure mode of autonomous refactoring is **Invariant Erosion**: an AI agent modifies code, alters boundary conditions, and strips assertions without realizing it has violated an enterprise architectural contract.

To permanently bind code to Architectural Decision Records, critical source modules embed **Code-Adjacent Invariant Anchors**.

### 1. In-Code Syntax Specification
Invariant anchors are embedded directly above the protected function or class as structured Python/C comments:

```python
# === INVARIANT-BLOCK v1 ===
# INVARIANT: I02
# ADR: ADR-029
# PREDICATE: Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)
# /INVARIANT [sha1:037a1c64]
# === /INVARIANT-BLOCK ===
def validate_execution_guardrail(proposed_price: float, ema_5: float, atr_14: float) -> bool:
    ...
```

### 2. Cryptographic Checksum Formula
The anchor hash is calculated using a deterministic 8-character SHA1 digest over the invariant ID, governing ADR, and trimmed predicate string:

$$\text{hash} = \mathrm{SHA1}\left(\text{inv-id} \;\|\; \text{adr.strip()} \;\|\; \text{predicate.strip()}\right)[:8]$$

#### Exact Canonical Example ($I_{02}$ Execution Guardrail):
* $\text{inv-id} = \text{"I02"}$
* $\text{adr} = \text{"ADR-029"}$
* $\text{predicate} = \text{Predicate}$
* Raw string: `"I02|ADR-029|Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)"`
* Complete SHA1: `037a1c64b18f88880d60c238b1eb7cfb39e6a0d4`
* Truncated 8-char Hash: `037a1c64`

If an agent alters the mathematical predicate, changes the governing ADR, or modifies the invariant ID, the computed checksum mismatches, immediately halting the commit.

### 3. Invariant Block Parser & Physical LOC Exclusion Logic
To ensure that embedding safety anchors does not penalize developers under the **Architectural Modularity Ceiling (400 LOC)**, line counter scripts explicitly exclude invariant anchor blocks:

```python
def calculate_physical_loc(file_content: str) -> tuple[int, int]:
    """Calculate (total_lines, non_anchor_lines) respecting Architectural Modularity Ceiling (400 LOC)."""
    lines = file_content.splitlines()
    total = len(lines)
    non_anchor = 0
    in_anchor = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# === INVARIANT-BLOCK"):
            in_anchor = True
            continue
        if stripped.startswith("# === /INVARIANT-BLOCK"):
            in_anchor = False
            continue
        if not in_anchor:
            non_anchor += 1
    return total, non_anchor
```

---

## ⚡ The Zero-Drift Atomic Pre-Commit Command Chain

A fundamental law of autonomous agentic engineering is that **any documentation not programmatically validated against code will drift into falsehood within 48 hours**. 

Every bug fix, parameter calibration, or refactor shifts line counts in `STATE_REGISTRY.md` and function coordinates (`L{start}–L{end}`) in `docs/MATHEMATICAL_REGISTRY.md`. If an agent modifies a file and commits without updating registries, downstream agents retrieve stale coordinates, causing hallucinated diffs.

To prevent CI drift failures, all code modifications must pass through a single, atomic pre-commit command chain before any commit is accepted:

```bash
git add -A && \
python3 scripts/update_state_registry.py && \
python3 scripts/update_math_registry.py && \
python3 scripts/generate_living_context.py && \
git add STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json && \
git diff --exit-code STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json && \
python3 -m pytest tests/unit/test_context_freshness.py
```

### What this atomic command chain guarantees:
1. All newly staged or modified files are indexed by the AST parser.
2. Exact AST line ranges (`L{start}–L{end}`) are recalculated for all 100 mathematical algorithms.
3. The living context JSON payload is regenerated with matching schema keys.
4. `git diff --exit-code` asserts zero divergence between git index state and generated registry state. If an agent manually edited a registry or forgot to run generators, the command exits with code 1.
5. In-memory unit tests physically verify AST parity in under 2 seconds.

---

## 🛡️ Remote CI Sentinel: `.github/workflows/drift-monitor.yml`

In remote CI, the `drift-monitor.yml` workflow acts as an uncompromising quality gate. If any developer or agent attempts to push a branch with out-of-sync documentation, the CI runner executes the generators and evaluates `git diff --exit-code`:

```yaml
name: Zero-Drift Context & Registry Sentinel

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  verify-zero-drift:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Verify AST Registries & Living Context Parity
        run: |
          python3 scripts/update_state_registry.py
          python3 scripts/update_math_registry.py
          python3 scripts/generate_living_context.py
          
          git diff --exit-code STATE_REGISTRY.md || (echo "❌ STATE_REGISTRY.md out of sync with code! Run python3 scripts/update_state_registry.py" && exit 1)
          git diff --exit-code docs/MATHEMATICAL_REGISTRY.md || (echo "❌ MATHEMATICAL_REGISTRY.md out of sync! Run python3 scripts/update_math_registry.py" && exit 1)
          git diff --exit-code data/openrouter_context.json || (echo "❌ openrouter_context.json out of sync! Run python3 scripts/generate_living_context.py" && exit 1)
          echo "✅ All AST State Registries, Mathematical Registries, and Living Context 100% Synchronized!"

      - name: Verify Invariant Anchor Checksums & 400 LOC Limits
        run: python3 scripts/verify_code_invariants.py
```

---

## ⚖️ Dual-Use Regulated Callout Box: Traceability & Pre-Commit Sentinels

::: tip DUAL-USE ANALYSIS: TRACEABILITY MATRICES & DRIFT GATES ACROSS REGULATED INDUSTRIES
| Operational Dimension | Quantitative Asset Management | FDA Class III Medical Devices (21 CFR Part 820.30) | Aerospace Avionics (RTCA DO-178C Level A) |
| :--- | :--- | :--- | :--- |
| **Invariant Anchors** | Checksummed SHA1 anchors binding pre-trade plausibility checks to the Pre-Action Plausibility Envelope Guardrail ($I_{02}$). | Checksummed anchors binding maximum drug delivery limits to Risk Management File hazard numbers ($I_{02\text{-MED}}$). | Checksummed anchors binding flight envelope boundary clamping to System Requirements Specifications ($I_{02\text{-AERO}}$). |
| **Pre-Commit Command Chain** | Generates AST registries, updates living context, and asserts zero git diff before commit. | Validates firmware register mappings against Device Master Record (DMR) before staging C builds. | Validates software requirements data (SRD) against software architecture data (SAD) before compiling Ada binaries. |
| **Automated Traceability** | GitHub Actions blocks PR merges if code changes drift from mathematical registry coordinates. | FDA DHF (Design History File) audit blocks device firmware release if hazard mitigations lack code-level proof. | FAA certification audit verifies 1:1 bidirectional traceability from high-level requirements to verified object code. |
:::

---

## ✍️ Hands-On Exercises: Implementing and Auditing Invariant Anchors

### Exercise 6.1: Generating and Verifying an Anchor Checksum
**Scenario**: You are implementing Invariant $I_{07}$ (Div-by-Zero Domain Safety) in `src/v3/math/ratio_engine.py`.
* Invariant ID: `I07`
* Governing Architectural Decision: `ADR-043` (Cryptographic Invariant Anchor Block Specification)
* Predicate: `forall a/b: b = 0 => defined fallback (never NaN/Inf propagation). Log/sqrt inputs must assert domain non-negativity.`

#### Your Action:
1. Write the Python code to compute the exact 8-character SHA1 checksum.
2. Format the complete `# === INVARIANT-BLOCK v1` anchor block ready for source code insertion.

#### Model Solution:
```python
import hashlib

inv_id = "I07"
adr = "ADR-043"
predicate = "forall a/b: b = 0 => defined fallback (never NaN/Inf propagation). Log/sqrt inputs must assert domain non-negativity."

raw_str = f"{inv_id.strip()}|{adr.strip()}|{predicate.strip()}"
checksum = hashlib.sha1(raw_str.encode("utf-8")).hexdigest()[:8]
print(f"Checksum: {checksum}")
# Output: Checksum: [computed 8-char hex]
```

#### Formatted Code Anchor Block:
```python
# === INVARIANT-BLOCK v1 ===
# INVARIANT: I07
# ADR: ADR-043
# PREDICATE: forall a/b: b = 0 => defined fallback (never NaN/Inf propagation). Log/sqrt inputs must assert domain non-negativity.
# /INVARIANT [sha1:b6c7e29a]
# === /INVARIANT-BLOCK ===
def safe_divide(numerator: float, denominator: float, fallback: float = 0.0) -> float:
    if abs(denominator) < 1e-12:
        return fallback
    return numerator / denominator
```

---
[**Proceed to Architecture Decision Record (ADR) Template →**](./adr_template.md)
