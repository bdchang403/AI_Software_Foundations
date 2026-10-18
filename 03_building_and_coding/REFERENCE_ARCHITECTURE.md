# Builder Reference Architecture: The Context-First Repository

In the Enterprise Context Factory, a repository is not merely an arbitrary collection of folders for human developers. To an autonomous AI agent, **your repository is an active, machine-readable Knowledge Graph and Context Map**. 

If the repository layout is unconstrained, agents spend thousands of tokens traversing directory trees, guess foreign imports, and suffer context collapse. The **Context-First Reference Architecture** organizes the filesystem so an agent can locate authoritative domain truth, active schemas, and architectural invariants in a single 1-hop execution.

---

## 📂 Standardized Context-First Folder Structure

```text
enterprise-repo/
├── ⚙️ .github/
│   ├── copilot-instructions.md          <-- Tier 1: The Global Router (~50 lines)
│   └── workflows/
│       └── drift-monitor.yml            <-- CI Sentinel: Verifies zero AST/schema drift
├── 📘 docs/
│   ├── context/                         <-- Tier 2: Surgical Domain Knowledge
│   │   ├── billing.md                   <-- Domain boundaries, business rules, local ADRs
│   │   ├── order_execution.md
│   │   ├── patient_monitoring.md
│   │   └── flight_controls.md
│   ├── registries/                      <-- Deterministic Machine-Generated Registries
│   │   ├── STATE_REGISTRY.md            <-- AST Repo Topography (<5,000 tokens)
│   │   └── MATHEMATICAL_REGISTRY.md     <-- 100 Canonical Algorithms & AST coordinates
│   └── stories/                         <-- Active Context-Enriched Semantic Blueprints
│       ├── FEAT-101-execution-gate.md   <-- Active task with 20 edge-case pre-conditions
│       └── BUG-204-concurrency-lock.md
├── 📦 data/
│   └── openrouter_context.json          <-- Living Context (<1,500 tokens, D1 table-to-DTO map)
├── 🛠️ scripts/
│   ├── update_state_registry.py         <-- Native ast.parse over git ls-files
│   ├── update_math_registry.py          <-- Line resolution & fail-closed test assertion
│   ├── generate_living_context.py       <-- Dual-schema parity compiler
│   └── verify_code_invariants.py        <-- SHA1 Invariant Anchor verification
├── 🏗️ src/                              <-- Bounded Domain Modules (Modularity Heuristics <= 400 LOC)
│   ├── domain_billing/
│   │   ├── models.py                    <-- Pydantic / Dataclass DTOs
│   │   ├── service.py                   <-- Domain state machine with SHA1 Invariant Anchors
│   │   └── registry.json                <-- Local Function Registry (Tool definitions)
│   └── shared/
│       ├── exceptions.py                <-- Fail-closed domain exception hierarchy
│       └── event_bus.py
└── 🧪 tests/
    ├── conftest.py                      <-- Hermetic socket isolation (SocketBlockedError)
    ├── unit/
    │   ├── test_context_freshness.py    <-- In-memory zero-drift verification
    │   └── test_math_invariants.py
    └── contracts/                       <-- Schema & Invariant verification suites
```

---

## 🧭 The Machine Entry Point Pattern across Toolchains

Every repository must establish an authoritative **Tier 1 Bootstrap Entry Point**. This file acts as the agent's initial operating instructions and contains hardcoded pointers to domain contexts.

| AI Toolchain | Canonical Entry Point Path | Purpose & Content |
| :--- | :--- | :--- |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Auto-loaded system prompt; points agent to `docs/context/*.md` based on active file path. |
| **Cursor** | `.cursorrules` (Repository Root) | Binds IDE agent to Semantic AST Scoping and Architectural Modularity Heuristics (<= 400 LOC). |
| **Claude Code** | `CLAUDE.md` (Repository Root) | Configures CLI agent environment, pre-commit command chains, and testing mandates. |
| **Antigravity** | `.antigravity/instructions.md` | Configures autonomous agent subagents, memory boundaries, and skill attachments. |

### Canonical Tier 1 Bootstrap Instruction Example
```markdown
# Enterprise Repository Architecture Rules (Tier 1)

1. DOMAIN BOUNDARIES: You operate in a strictly bounded architecture. Before modifying any code, identify the domain from the file path and load the Tier 2 Domain Context from `docs/context/{domain}.md`.
2. ARCHITECTURAL MODULARITY HEURISTICS: Source modules in `src/`, `workers/`, or `tests/` maintain a target heuristic ceiling of <= 400 lines. Files reaching 350 lines enter the refactor warning zone for proactive decomposition.
3. RULE 14 ANTI-FEATURE-ERASURE: You are strictly forbidden from truncating, commenting out, or deleting existing retry cascades, fallback pricing, or assertions to meet line limits.
4. ZERO-MOCK MANDATE: NEVER emit synthetic constants, positive numeric defaults in arguments (ZM005), or fallback constants in `except` blocks (ZM001). Fail closed (return None or raise).
5. INVARIANT ANCHORS: Critical methods must maintain their `# === INVARIANT-BLOCK` with verified SHA1 checksums.
6. PRE-COMMIT CHAIN: All changes must pass `git diff --exit-code` against generated AST registries.
```

---

## 🧩 Local Function Registries

Instead of maintaining a single monolithic tool registry that consumes thousands of tokens, high-performance repositories place **Localized Function Registries** directly within domain folders:

**Example: `src/domain_billing/registry.json`**
```json
{
  "domain": "Billing",
  "version": "2.4.0",
  "tools": [
    {
      "name": "calculate_regional_tax",
      "description": "Calculates regional tax. Use this tool exclusively instead of hardcoding percentage logic.",
      "parameters": {
        "type": "object",
        "properties": {
          "amount_cents": {"type": "integer"},
          "jurisdiction_code": {"type": "string"}
        },
        "required": ["amount_cents", "jurisdiction_code"]
      }
    }
  ]
}
```

When an agent enters `src/domain_billing/`, it reads this localized registry and recognizes that tax calculation logic is restricted to the `calculate_regional_tax` tool, preventing speculative arithmetic implementations.

---

## ⚖️ Dual-Use Regulated Callout Box: Reference Architecture Across Industries

::: tip DUAL-USE ANALYSIS: CONTEXT-FIRST TOPOLOGY IN REGULATED ENTERPRISES
| Architectural Layer | Quantitative Asset Management Pipeline | FDA Class III Medical Device Firmware | Aerospace Avionics (RTCA DO-178C Level A) |
| :--- | :--- | :--- | :--- |
| **Tier 1 Global Router** | `.github/copilot-instructions.md` routing to quant strategies, execution gateways, risk stops. | `.cursorrules` routing to pump motor control, glucose sensing, hazard mitigations. | `CLAUDE.md` routing to flight control laws, sensor voting, air data computers. |
| **Tier 2 Domain Context** | `docs/context/quant_engine.md` detailing Compensatory Confluence (Invariant I09) and Plausibility Bands. | `docs/context/titration.md` detailing 21 CFR Part 820.30 design controls and basal limits. | `docs/context/autopilot.md` detailing DO-178C Level A flight envelope limiters and fault recovery. |
| **Living Context Schema** | `data/openrouter_context.json` mapping 29 D1 SQL tables to Pydantic models. | Hardware register maps binding memory-mapped I/O addresses to C struct types. | ARINC 424 navigation database schemas binding binary records to flight plan structs. |
| **Quality Gate** | Pre-commit zero-drift gate asserting AST registry and math symbol synchronization. | Device Master Record (DMR) compilation gate asserting firmware binaries match hazard traces. | Software Configuration Index (SCI) gate asserting source code matches low-level requirements. |
:::

---
[**Proceed to System Prompt Skills Catalog →**](./skills.md)
