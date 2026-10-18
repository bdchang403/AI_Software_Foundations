# Executive Reference: The 3-Tier Context Pipeline Architecture

---

## 🎯 Executive Overview & Scope

In autonomous enterprise software engineering, large language models must never be prompted with unconstrained raw repositories. Feeding an entire codebase into an LLM causes attention entropy dispersion, triggers "Lost in the Middle" amnesia, and leads to code bloat and hallucinations.

The Context Factory solves this by enforcing the **3-Tier Context Pipeline**: a deterministic compilation chain that extracts only verified AST signatures, schema contracts, and active invariants into an audited, token-dense payload (<1,500 tokens).

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      THE 3-TIER CONTEXT COMPILATION HIERARCHY                                    │
├────────────────────┬───────────────────────────────────┬─────────────────────────────────────────┤
│ Context Tier       │ Scope & Content                   │ Token Budget Allocation                 │
├────────────────────┼───────────────────────────────────┼─────────────────────────────────────────┤
│ Tier 1: Global     │ Enterprise Constitution & Rules   │ 200 – 400 tokens (Immutable / Pinned)   │
│ Tier 2: Structural │ AST Living Context JSON           │ 800 – 1,200 tokens (Dynamic AST Cache)  │
│ Tier 3: Surgical   │ Domain Blueprint & AST Node Scope │ 400 – 600 tokens (Target Scope Focus)   │
├────────────────────┴───────────────────────────────────┴─────────────────────────────────────────┤
│ TOTAL COMBINED PROMPT PAYLOAD CEILING:                 │ <= 2,500 TOKENS (95%+ Attention Zone)   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 End-to-End Context Pipeline & Zero-Drift Verification

```mermaid
flowchart TD
    subgraph Repo_Sources ["1. Git-Tracked Codebase Sources"]
        A["Tracked Python Modules (git ls-files)"]
        B["Canonical Algorithm Registry"]
        C["D1 SQL Database DTO Schemas"]
    end

    subgraph Compilation_Engine ["2. AST Compilation Engine (<2 seconds)"]
        A --> D["AST State Parser (update_state_registry.py)"]
        B --> E["Math Line Coordinate Indexer (update_math_registry.py)"]
        C --> F["Living Context Compiler (generate_living_context.py)"]
        
        D --> G["STATE_REGISTRY.md (<5k tokens)"]
        E --> H["MATHEMATICAL_REGISTRY.md (Exact Line Bounds)"]
        F --> I["living_context.json (<1.5k tokens)"]
    end

    subgraph Agent_Ingress ["3. Zero-Drift Agent Ingress"]
        G & H & I --> J{"CI Drift Gate: git diff --exit-code"}
        J -- "Parity Verified (Zero Drift)" --> K["Inject into Agent Prompt (<2,500 tokens)"]
        J -- "Drift Detected" --> L["FAIL CLOSED: Block Commit / Pull Request"]
    end

    style Repo_Sources fill:#f8f9fa,stroke:#343a40,stroke-width:2px;
    style Compilation_Engine fill:#e8f4f8,stroke:#17a2b8,stroke-width:2px;
    style Agent_Ingress fill:#eafaf1,stroke:#28a745,stroke-width:2px;
    style L fill:#ffcdd2,stroke:#c62828,stroke-width:2px;
```

---

## 🏛️ Context Pipeline Core Artifacts & Implementation Guide

### 1. The AST State Registry (`STATE_REGISTRY.md`)
*   **Purpose**: Lightweight topographic index (<5,000 tokens) compiled directly from Python native `ast.parse` over git-tracked files.
*   **Contents**: Module paths, physical line counts, classes, public function signatures, and modularity health status (`✅ Healthy (<350 LOC)` vs `⚠️ Near 400 LOC Cap`).
*   **Deep Implementation**: [Context Engineering (03_04)](./03_building_and_coding/04_context_engineering.md).

### 2. The Canonical Mathematical Registry (`MATHEMATICAL_REGISTRY.md`)
*   **Purpose**: Catalogs all safety and quantitative algorithms with exact AST start/end line coordinates (`L_start` to `L_end`), LaTeX formulas, and linked unit tests.
*   **Contents**: 100+ formal algorithms with zero line-drift.
*   **Deep Implementation**: [Context Engineering (03_04)](./03_building_and_coding/04_context_engineering.md).

### 3. The Living Context Compiler (`living_context.json`)
*   **Purpose**: Token-dense JSON context payload (<1,500 tokens) injected into model prompts before execution.
*   **Contents**: Active model routing matrix, database schema parity map (SQL DTOs to Pydantic models), and governing invariants.
*   **Deep Implementation**: [Context Engineering (03_04)](./03_building_and_coding/04_context_engineering.md) and [Context Mapping Matrix (09_04)](./09_ai_agent_orchestration/04_context_mapping_matrix.md).

### 4. Zero-Drift Pre-Commit Hook & Remote CI Monitor
*   **Purpose**: Guaranteed byte-parity between physical code and documentation.
*   **Execution Command**:
    ```bash
    python3 scripts/update_state_registry.py &&     python3 scripts/update_math_registry.py &&     python3 scripts/generate_living_context.py &&     git diff --exit-code
    ```
*   **Deep Implementation**: [Automated Traceability (05_05)](./05_deployment_and_operations/05_automated_traceability.md).

---

[**Proceed to The Mathematics of AI Risk →**](./00_THE_MATHEMATICS_OF_AI_RISK.md) | [**Return to Main Curriculum Hub →**](./README.md)
