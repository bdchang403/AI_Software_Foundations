# Module 3: Code Decomposition, Architectural Modularity Ceiling (400 LOC) & Rule 14 Anti-Feature-Erasure

## 🧠 Theory: Token Economics, Working Memory & The U-Curve Collapse

In a large enterprise repository (500,000+ lines of code), autonomous AI agents face physical working memory limits imposed by transformer attention architecture. Even with expanded nominal context windows (128k to 1M tokens), model attention is neither uniform nor infinite.

### The Physics of Attention Collapse in Monolithic Code
As detailed in [The Mathematics of AI Risk](../00_THE_MATHEMATICS_OF_AI_RISK.md), the information-theoretic attention entropy across sequence length $N$ scales logarithmically:
$$\mathcal{H}(A_i) = -\sum_{j=1}^N A_{ij} \ln A_{ij}$$

When a 1,200-line monolithic file (~9,000 tokens) is loaded into an agent's context alongside project documentation, system instructions, and tool schemas, attention entropy disperses across thousands of non-relevant lines. The model's positional retrieval fidelity follows the empirical **U-shaped attention curve ("Lost in the Middle")**:

$$F(x) = \begin{cases} 
1.0 - k_1 x & x \in [0.0, 0.15] \quad \text{(Primacy Bias)} \\
0.35 + \epsilon(x) & x \in (0.15, 0.85) \quad \text{(Degradation Valley: 40 to 75 percent information loss)} \\
1.0 - k_2 (1.0 - x) & x \in [0.85, 1.0] \quad \text{(Recency Bias)}
\end{cases}$$

In a 1,200-line monolith, functions positioned between lines 200 and 1,000 reside directly in the **Degradation Valley**, where retrieval fidelity drops to approximately 35%. When instructed to make modifications to a method inside this valley, the autonomous agent exhibits three pathological failure modes:
1. **Context Amputation**: The agent loses track of variables instantiated at the top of the file, redeclaring them locally and shadowing state.
2. **Diff Corruption**: The agent produces hallucinated line numbers in its diff hunks, failing patch application.
3. **The Compression Cheating Trap (Silent Feature Erasure)**: Constrained by output token budgets, the model truncates peripheral code, replacing 200 lines of error handlers, retry logic, and invariant checks with comments like `# ... existing logic remains unchanged ...`.

---

## 🏛️ The Architectural Modularity Heuristic Standard (400 LOC)

To eliminate monolithic degradation, prevent cognitive drift, and guarantee deterministic code modifications, enterprise software architecture codifies **Architectural Modularity Heuristics (The 400-LOC Guideline)**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           THE ARCHITECTURAL MODULARITY HEURISTIC (400 LOC)                       │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   1. THE 400-LOC ARCHITECTURAL MODULARITY HEURISTIC                                              │
│      • Source modules in `src/`, `workers/`, and `tests/` maintain a target heuristic ceiling    │
│        of <= 400 physical lines to safeguard the Single Responsibility Principle (SRP).         │
│      • Excludes code-adjacent `# === INVARIANT-BLOCK` lines (safety annotations are free).      │
│      • Orchestration runners and complex coordinators have an explicit ceiling of 600 LOC.        │
│                                                                                                  │
│   2. THE 350-LOC REFACTORING HEURISTIC TRIGGER                                                   │
│      • Any module reaching 350 physical lines enters the "Refactor Warning Zone".               │
│      • Serves as an architectural modularity heuristic: before adding extensive feature sets,    │
│        engineers evaluate decomposition. Localized bug fixes and atomic patches remain          │
│        permitted without forcing premature, brittle micro-module fragmentation.                  │
│                                                                                                  │
│   3. SEMANTIC AST STRUCTURAL SCOPING                                                             │
│      • Autonomous agents inspect code via cohesive AST node units (functions, classes, and      │
│        interface declarations) rather than arbitrary physical line-slicing windows.             │
│      • In modern frontier models with context windows >= 128k tokens, inspecting an entire       │
│        cohesive module (<= 400 LOC, ≈ 2,500 tokens) operates well within high-fidelity          │
│        attention (<2% context capacity), preventing truncation of parameter lists or try-blocks.│
│                                                                                                  │
│   4. RULE 14: THE ANTI-FEATURE-ERASURE PROTOCOL                                                 │
│      • Refactoring to meet modularity targets MUST decompose logic into domain submodules.       │
│      • Agents are strictly forbidden from deleting fallback cascades, retry loops, or telemetry. │
│      • Banned: replacing existing methods with `# ... existing code ...` or pass-through stubs.   │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Canonical Decomposition Patterns: Real-World Case Studies

### Case Study A: Decomposing a Monolithic Portfolio Tracker
When `paper_portfolio_tracker.py` grew to **480 lines of code**, adding tax-lot accounting threatened to push the file past 600 LOC, inducing attention dilution.

#### The Anti-Pattern (Compression Cheating):
An unconstrained AI agent was asked to "reduce `paper_portfolio_tracker.py` under 400 lines." The model deleted the 3-tier trailing stop ratchet and stripped drawdown calculation assertions, returning a 380-line file that silently broke portfolio risk stops in production.

#### The Architectural Modularity & Rule 14 Compliant Decomposition:
The system architect decomposed the module into three cohesive, single-responsibility units:
1. `portfolio_risk_stops.py` (192 LOC): Extracted trailing stop ratchets, volatility bands, and high-water mark tracking.
2. `paper_portfolio_metrics.py` (166 LOC): Extracted Sharpe ratio, Sortino ratio, max drawdown, and beta calculations.
3. `paper_portfolio_tracker.py` (332 LOC): Retained core state machine, order execution hooks, and position persistence.

*Result*: 100% of safety handlers and mathematical algorithms were preserved. All files satisfied the Architectural Modularity Ceiling ($< 350$ LOC).

---

### Case Study B: Decomposing the Multi-Agent Debate Matrix
The dialectical debate engine originally combined macro beta estimation, covariance whitening, and agent orchestration in a single 520-line file.

#### The Modular Decomposition (400-LOC Ceiling):
1. `macro_beta.py` (87 LOC): Mathematical estimation of market beta and idiosyncratic residual variance.
2. `zca_whitening.py` (118 LOC): Alg #89 Anchor-Preserving Symmetrical ZCA Whitening and Ledoit-Wolf shrinkage.
3. `epistemic_triad_orchestrator.py` (111 LOC): 3-stage Path C multi-agent debate coordination.
4. `debate_matrix.py` (284 LOC): Core consensus aggregation and convex log-odds solver bindings.

---

## 🔄 Visual Workflow: The Architectural Modularity Refactoring Lifecycle (400-LOC Ceiling)

The following Mermaid diagram details the deterministic decision tree executed before any code modification is merged:

```mermaid
flowchart TD
    A[New Feature or Bugfix Request] --> B[Inspect Module via Semantic AST Scoping]
    B --> C["Check Target Physical LOC: calculate_physical_loc(file)"]
    C --> D{"Non-Anchor LOC >= 350 & Expansion?"}
    
    D -- Yes --> E[EVALUATE MODULAR DECOMPOSITION HEURISTIC]
    E --> F[Identify Cohesive Domain Boundaries]
    F --> G[Extract Submodules < 400 LOC]
    G --> H[Apply Rule 14 Anti-Feature-Erasure Audit]
    H --> I{"Any Fallback, Retry, or Assertion Deleted?"}
    I -- Yes --> J[REJECT REFACTOR: Restore All Handlers into New Submodule]
    J --> G
    I -- No --> K[Update AST State & Math Registries]
    
    D -- No --> L[Implement Target Modification / Atomic Patch]
    L --> M{"Did Edit Push LOC >= 400?"}
    M -- Yes --> E
    M -- No --> K
    
    K --> N["Execute Atomic Pre-Commit Chain (git diff --exit-code)"]
    N --> O[Commit & Merge Clean]

    style E fill:#ffdddd,stroke:#d90429,stroke-width:2px;
    style H fill:#fff3cd,stroke:#ffb703,stroke-width:2px;
    style K fill:#e8f4f8,stroke:#028090,stroke-width:2px;
    style N fill:#eafaf1,stroke:#2a9d8f,stroke-width:2px;
```

---

## ⚖️ Dual-Use Regulated Callout Box: Modular Deconstruction in Safety-Critical Domains

::: tip DUAL-USE ANALYSIS: MODULARITY HEURISTICS & ANTI-FEATURE-ERASURE ACROSS REGULATED INDUSTRIES
| Engineering Requirement | Quantitative Asset Management Pipeline | FDA Class III Medical Device Firmware (21 CFR Part 820.30) | Aerospace Fly-by-Wire Avionics (RTCA DO-178C Level A) |
| :--- | :--- | :--- | :--- |
| **Physical Modularity Heuristics** | 400 LOC target per file. Preserves single responsibility and maintains active code well within high-fidelity attention ($<2\%$ context capacity). | MISRA C:2012 Design Guidelines: Recommends small, cohesive functions to prevent path explosion (Rule 8.4 mandates compatible external linkage declarations to prevent type mismatches). | DO-178C Unit Testing: Units strictly scoped to single-condition decision paths to guarantee 100% MC/DC testability. |
| **Rule 14 Anti-Feature-Erasure** | Forbids AI from removing 4-tier live price discovery waterfall (FMP $\to$ Yahoo $\to$ Finnhub $\to$ D1) to meet file limits. | Forbids AI from deleting redundant hardware watchdog pet routines (`WDT_PET()`) or sensor out-of-range clamps. | Forbids AI from stripping triple-modular redundancy (TMR) sensor voting or dual-channel bus synchronization logic. |
| **Semantic AST Structural Scoping** | Inspects cohesive AST units (functions, classes, schemas); operates in peak fidelity attention zone without severing syntax scopes. | Auditing and modifying single state-machine transitions without loading unrelated driver interrupt tables. | Verifying single aerodynamic table lookup functions without exposing actuator servo PID control loops. |
:::

---

## 🛠️ Practical Decomposition Protocol: The 4-Step Slicing Pipeline

When an architectural epic requires substantial new functionality, do not attempt to prompt an AI to implement the entire feature in a single pass. Decompose the implementation into **Sequential, Context-Bounded Pull Requests**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 4-STEP CONTEXT-BOUNDED PR PIPELINE                              │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   PR 1: SCHEMAS & INTERFACE CONTRACTS                                                            │
│   • Context: Database migration files, Pydantic DTO models, TypeScript interfaces.               │
│   • Target LOC: <= 120 lines.                                                                    │
│   • Output: Staged schema migrations and verified table-to-DTO mappings.                         │
│                                                                                                  │
│   PR 2: CORE MATHEMATICAL & DOMAIN ALGORITHMS                                                    │
│   • Context: PR 1 schemas + specific algorithmic formulation from `MATHEMATICAL_REGISTRY.md`.    │
│   • Target LOC: <= 250 lines.                                                                    │
│   • Output: Pure domain functions with zero external I/O and co-located unit test suite.        │
│                                                                                                  │
│   PR 3: APPLICATION SERVICES & ORCHESTRATION                                                     │
│   • Context: PR 2 domain models + function registry tools + domain ADRs.                         │
│   • Target LOC: <= 300 lines.                                                                    │
│   • Output: Service orchestrator managing state transitions and fail-closed error handling.      │
│                                                                                                  │
│   PR 4: PRESENTATION, APIS & INVARIANT ANCHORS                                                   │
│   • Context: Service interface + router definitions + `# === INVARIANT-BLOCK` checksum anchors.  │
│   • Target LOC: <= 180 lines.                                                                    │
│   • Output: REST/GraphQL endpoints and verified SHA1 invariant anchors.                          │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## ✍️ Hands-On Exercises: Slicing a Complex Enterprise Epic

### Exercise 3.1: Decomposing a Closed-Loop Infusion Controller
**Scenario**: You are tasked with adding a "Pediatric Auto-Titration Mode" to an FDA Class III infusion pump. The existing `infusion_controller.c` file is at **365 physical lines** (in the 350-400 LOC Refactor Zone). The new feature requires:
1. A pediatric patient profile schema (weight, age, metabolic clearance rate).
2. A pharmacokinetic drug concentration decay model: $C(t) = C_0 \cdot e^{-k_e \cdot t}$.
3. Dynamic rate clamping based on measured blood pressure.

#### Your Action:
1. Write the architectural modularity refactoring plan to bring `infusion_controller.c` under 300 lines before adding the feature.
2. Define the submodules to extract and verify that Rule 14 Anti-Feature-Erasure is enforced.

#### Model Solution:
```markdown
### 1. REFACTORING PLAN (PRE-FEATURE DECOMPOSITION)
- TARGET: `firmware/infusion/infusion_controller.c` (currently 365 LOC).
- EXTRACTIONS:
  1. `firmware/infusion/pressure_occlusion_guard.c` (110 LOC): Extract hardware pressure transducer sampling, occlusion detection, and emergency line-clamp actuation.
  2. `firmware/infusion/infusion_telemetry.c` (85 LOC): Extract audit logging, delivery rate serialization, and UI annunciator events.
- POST-REFACTOR BASELINE: `infusion_controller.c` reduced to 170 LOC (< 350 LOC, Healthy).

### 2. RULE 14 ANTI-FEATURE-ERASURE VERIFICATION
- AUDIT: All pressure threshold assertions (`ASSERT_OCCLUSION_LIMIT`), watchdog kicks (`WDT_FEED()`), and fail-safe latching routines must be preserved verbatim in `pressure_occlusion_guard.c`.
- ZERO-MOCK COMPLIANCE: If pediatric sensor telemetry is disconnected, controller fails closed to basal hold (0.5 mcg/hr) and triggers nurse-call alarm. Zero default weight or synthetic rate imputation permitted.

### 3. PEDIATRIC FEATURE PR SLICING
- PR 1: `firmware/schemas/pediatric_profile.h` (45 LOC): Define typed struct with metabolic constants.
- PR 2: `firmware/math/pk_clearance_model.c` (90 LOC): Implement discrete exponential clearance calculation with fixed-point arithmetic.
- PR 3: `firmware/infusion/infusion_controller.c` (+75 LOC -> 245 LOC total): Bind pediatric profile to titration state machine.
```

---
[**Proceed to Module 4: Context Engineering (The Builder's Guardrails) →**](./04_context_engineering.md)
