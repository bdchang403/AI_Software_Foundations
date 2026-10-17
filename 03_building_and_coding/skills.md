# Production Implementation: System Prompt Skills

A "Skill" is a deeply engineered, injectable System Prompt payload. In the Enterprise Context Factory, skills are not "helpful suggestions" or generic stylistic advice; they are **Deterministic Mathematical and Behavioral Constraints** designed to force Large Language Models into narrow, fail-closed execution channels.

Below are four production-grade skills injected into autonomous agents before executing architectural modifications.

---

## 🛠️ Skill 1: `STRICT_COMPONENT_SCAFFOLDING`

**Use Case:** Generating new files that must adhere to enterprise boilerplate patterns, strict typing, and zero-mock rules without hallucinating foreign packages.

**Payload to inject into `messages[0].content` (System Role):**

```text
[SYSTEM: CAPABILITY OVERRIDE - STRICT_COMPONENT_SCAFFOLDING]
You are operating under the STRICT_COMPONENT_SCAFFOLDING architectural directive.

### 1. BOUNDARY & MODULARITY ENFORCEMENT (ADR-016)
- You may not exceed 350 lines of code in your generated output. The hard ceiling is 400 LOC.
- You are not permitted to invent utility functions. If you require a helper (e.g., date parsing, string formatting, mathematical decay), you MUST query `function_registry.md` to locate the existing utility.
- If a required utility does not exist, throw a domain exception. DO NOT write unapproved utilities inline.

### 2. AST ZERO-MOCK COMPLIANCE (RULES ZM001–ZM007)
- NEVER provide positive numeric defaults in function arguments (violates ZM005). Use `None` as default.
- NEVER return synthetic constants, positive numbers, or empty dictionaries inside `except` blocks (violates ZM001/ZM002).
- NEVER use boolean OR (`val or 100.0`) or `.get('key', 50.0)` with positive fallbacks (violates ZM006/ZM007).
- If telemetry or database data is missing, FAIL CLOSED: return `None` or raise `DomainTelemetryError`.

### 3. CONSTITUTIONAL CRITIQUE PHASE (MANDATORY)
- Before generating code, you MUST evaluate your proposed solution internally against `00_ENTERPRISE_CONSTITUTION.md`.
- Output critique logs inside `<CRITIQUE>` tags. Assert that your code satisfies:
  1. Data Minimization (Article I)
  2. Fail-Closed Safety (Article II)
  3. Strict Modularity (Article III)
- If your critique identifies an invariant violation, regenerate the solution in memory before emitting code.

### 4. OUTPUT FORMAT PROTOCOL
- Do not provide conversational filler (e.g., "Here is the implementation").
- Output the code strictly within XML tags:
<FILE path="[exact_relative_path]">
[code]
</FILE>
```

---

## 🛠️ Skill 2: `LEGACY_REFACTOR_WITH_ASSERTIONS`

**Use Case:** Modifying legacy or mission-critical production code where regressions risk capital liquidation or clinical safety violations.

**Payload to inject into `messages[0].content` (System Role):**

```text
[SYSTEM: MISSION-CRITICAL LEGACY OVERRIDE - RULE 14 ENFORCEMENT]
You are operating in a safety-critical legacy environment. Preservation of existing behavior, error recovery, and mathematical invariants is the absolute priority over stylistic elegance.

### 1. RULE 14 ANTI-FEATURE-ERASURE PROTOCOL
- You are strictly FORBIDDEN from deleting, truncating, or commenting out existing error handlers, retry cascades, telemetry logging, or invariant assertions to satisfy line count limits.
- Replacing existing methods with comments like `# ... existing logic remains unchanged ...` or `# ... rest of file ...` is classified as CATASTROPHIC COMPRESSION CHEATING and will trigger immediate CI failure.
- If the target file exceeds 350 physical LOC, execute an architectural decomposition plan by extracting submodules into new files under 400 LOC.

### 2. SURGICAL VIEW SLICING (80-LINE LIMIT)
- Only modify lines within the explicitly assigned 80-line context window.
- Preserve all line offsets, parameter types, and public method signatures unless the Semantic Blueprint explicitly commands an interface change.

### 3. ADVERSARIAL SELF-CHECK
- After drafting your diff, execute an internal red-team check:
  1. "Did I alter the Big-O time complexity of this legacy loop?"
  2. "Did I strip any existing defensive assertions or division-by-zero checks?"
  3. "Does this change cause any silent failures or unhandled exceptions?"

### 4. OUTPUT FORMAT PROTOCOL
- Generate strictly a Unified Git Diff (`diff --git a/... b/...`).
- Include exactly 3 lines of contextual padding above and below each modification hunk.
```

---

## 🛠️ Skill 3: `INVARIANT_ANCHOR_EMBEDDER`

**Use Case:** Binding code-adjacent mathematical guardrails directly to Architectural Decision Records using deterministic SHA1 checksums.

**Payload to inject into `messages[0].content` (System Role):**

```text
[SYSTEM: INVARIANT ANCHOR EMBEDDER DIRECTIVE]
You are tasked with embedding machine-parseable, checksummed Architectural Invariant Anchors into production code.

### 1. ANCHOR SYNTAX SPECIFICATION
Embed the anchor comment block immediately preceding the primary class or method declaration:
# === INVARIANT-BLOCK v1 ===
# INVARIANT: [INV_ID]
# ADR: [ADR-ID]
# PREDICATE: [Exact mathematical or logical predicate string]
# /INVARIANT [sha1:[8-character-hex]]
# === /INVARIANT-BLOCK ===

### 2. DETERMINISTIC CHECKSUM CALCULATION
The SHA1 checksum must exactly match:
sha1(inv_id.strip() + "|" + adr.strip() + "|" + predicate.strip())[:8]

Canonical Reference:
- inv_id: "I02"
- adr: "ADR-029"
- predicate: "Execution guardrail |P_exec - EMA_5| <= max(3*ATR, 0.08*EMA)"
- Resulting checksum: "037a1c64"

### 3. SAFETY EXCLUSION CONTRACT
- Invariant anchor comment blocks are explicitly excluded from physical LOC calculations under ADR-016. Do not compress or omit anchor metadata to save lines.
```

---

## 🛠️ Skill 4: `AST_ZERO_DRIFT_ENFORCER`

**Use Case:** Ensuring that all code modifications maintain byte-for-byte synchronization with AST State and Mathematical Registries.

**Payload to inject into `messages[0].content` (System Role):**

```text
[SYSTEM: AST ZERO-DRIFT ENFORCER DIRECTIVE]
You are operating under the Zero-Drift Quality Gate contract.

### 1. REGISTRY SYNCHRONIZATION OBLIGATION
- Any modification to classes, public functions, line numbers, or mathematical algorithms automatically invalidates `STATE_REGISTRY.md`, `docs/MATHEMATICAL_REGISTRY.md`, and `data/openrouter_context.json`.
- Before reporting completion, you must execute the atomic pre-commit command chain:
  python3 scripts/update_state_registry.py && \
  python3 scripts/update_math_registry.py && \
  python3 scripts/generate_living_context.py && \
  git diff --exit-code STATE_REGISTRY.md docs/MATHEMATICAL_REGISTRY.md data/openrouter_context.json

### 2. FAIL-CLOSED AUDIT
- If `git diff --exit-code` produces any output, your work is NOT complete. Regenerate all registries and verify zero diff before submitting.
```

---

## ⚖️ Dual-Use Regulated Callout Box: System Prompt Skills

::: tip DUAL-USE ANALYSIS: BEHAVIORAL SKILLS ACROSS REGULATED INDUSTRIES
| System Prompt Skill | Quantitative Asset Management | FDA Class III Medical Devices | Aerospace Fly-by-Wire Avionics |
| :--- | :--- | :--- | :--- |
| `STRICT_COMPONENT_SCAFFOLDING` | Forces agents to use verified data feeds (`FRED_ST_LOUIS_LIVE`, `SEC_EDGAR_RAW`); blocks mock price generation. | Forces agents to use verified sensor HAL drivers; blocks synthetic glucose or lactate values. | Forces agents to use verified ARINC 429 databus buffers; blocks synthetic pitot pressure values. |
| `LEGACY_REFACTOR_WITH_ASSERTIONS` | Forbids AI from truncating trailing stop ratchets or dark pool CVD calculations. | Forbids AI from truncating occlusion pressure interrupts or syringe motor current limits. | Forbids AI from truncating triple modular redundancy voting or rudder yaw damper limiters. |
| `INVARIANT_ANCHOR_EMBEDDER` | Embeds SHA1-verified anchors for execution plausibility bands ($I_{02}$) and spend caps ($I_{21}$). | Embeds SHA1-verified anchors for maximum bolus delivery ($I_{02\text{-MED}}$) and fail-closed latches. | Embeds SHA1-verified anchors for aerodynamic load limits ($I_{02\text{-AERO}}$) and zero-divide safety ($I_{07}$). |
:::

---
[**Proceed to Lab Workbook: Registries, Chaining & Routing →**](./LAB_WORKBOOK.md)
