# The End-to-End Context Pipeline

The central innovation of the Context Factory is the **Context Handshake**: a standardized methodology for business and technical roles to communicate through AI-ready documentation. 

AI literacy is not just an individual skill—it is a collective team capability. If a Requirements Lead writes a vague requirement, the Builder's AI agent will hallucinate an architecture, causing the Validation Lead's automated tests to fail, and the BuilderOps pipeline to block the release.

To prevent token exhaustion and logic drift, context must flow sequentially, getting more bounded and deterministic at every step.

## The Context Handshake Flowchart

```mermaid
flowchart TD
    %% Roles
    Strategy Lead[Strategy Lead]
    BSA[Business Systems Analyst]
    DEV[Builder / Architect]
    Validation Lead[Validation Lead]
    OPS[Deployment Lead / BuilderOps]
    
    %% Artifacts
    EPIC[Epic / Strategic Intent]
    CES[Context-Enriched Story <br> & Semantic Blueprint]
    CODE[copilot-instructions.md <br> Code & Unit Tests]
    TESTS[Automated Verification <br> Contract-First Tests]
    TRACE[GitHub Actions / SBOM <br> Auditable AI Traces]

    %% Flow
    Strategy Lead -- "Decomposition & Value Definition" --> EPIC
    EPIC -- "Context Handshake" --> BSA
    BSA -- "3-Part Directives & Edge Cases" --> CES
    CES -- "Repository Injection (/stories/)" --> DEV
    DEV -- "AI-Assisted Generation & ADRs" --> CODE
    CODE -- "Context Handshake" --> Validation Lead
    Validation Lead -- "Adversarial Prompting & Validation" --> TESTS
    TESTS -- "Context Handshake" --> OPS
    OPS -- "Security & Compliance Check" --> TRACE
    
    %% Feedback Loop
    TRACE -. "Metrics & DORA" .-> Strategy Lead
    TESTS -. "Failed Logic / Missing Context" .-> BSA

    classDef role fill:#1f77b4,color:#fff,stroke:#000,stroke-width:2px;
    classDef artifact fill:#2ca02c,color:#fff,stroke:#000,stroke-width:2px;
    
    class Strategy Lead,BSA,DEV,Validation Lead,OPS role;
    class EPIC,CES,CODE,TESTS,TRACE artifact;
```

## The Role-to-Role Handoffs

### 1. Strategy Lead → Requirements Lead
*   **The Goal:** Break monolithic ideas into deterministic boundaries.
*   **Key Concept:** **Decomposition**. An AI agent cannot process "rebuild the login portal." The Strategy Lead must slice the feature into vertical slices that fit within a single AI agent's memory constraints.
*   **The Output:** Bounded Epics and clear Acceptance Criteria boundaries.

### 2. Requirements Lead → Builder
*   **The Goal:** Produce **context-enriched stories** that builders can feed directly into their IDE.
*   **Key Concept:** **Semantic Blueprints & The 3-Part Directive**. The BSA removes all ambiguity. They define the *Role*, the *Task*, and the *Format*. They brainstorm 20 edge cases before a line of code is written.
*   **The Output:** A Markdown-formatted **context-enriched story** stored in the repository (e.g., `docs/stories/`) that `@workspace` can ingest.

### 3. Builder → Validation Lead
*   **The Goal:** Translate human requirements into machine-executable logic without hallucination.
*   **Key Concept:** **Function Registries & 2-Tier Precision Routing**. The builder uses the context-enriched story to constrain the AI. They implement a 1-hop routing model (Global Router → Domain Context) that points the AI to the exact truth needed for the task.
*   **The Output:** Application code and unit tests generated via AI, mapped exactly to the context-enriched story.

### 4. Validation Lead → BuilderOps
*   **The Goal:** Mathematically prove the AI didn't hallucinate.
*   **Key Concept:** **Adversarial Red-Teaming**. The Validation Lead uses AI to try to break the AI-generated code. They build automated Contract-First testing suites. Since AI increases coding speed, the test-to-code ratio must increase.
*   **The Output:** Green automated test pipelines and security scans.

### 5. BuilderOps → Leadership (The Feedback Loop)
*   **The Goal:** Ensure the pipeline remains secure, auditable, and performant.
*   **Key Concept:** **AI Tracing & SBOMs**. Release engineers ensure every AI-generated commit is tagged. They monitor DORA and SPACE metrics to ensure the "Context Handshake" is actually speeding up the factory, not just creating technical debt faster.
*   **The Output:** Executive dashboarding and continuous improvement of the context-enriched story templates.

## The Technical Mechanics: How Context Actually Moves (The "Pipes")

It is not enough to talk about "handoffs" conceptually. In a monolithic enterprise codebase, context must move through physical, automated systems to constrain the AI. Here is exactly how the data flows:

1. **The Origin (Jira/Confluence):** The Strategy Lead and Requirements Lead collaborate in an agile management tool. The Requirements Lead writes the **context-enriched story**, ensuring the 3-Part Directive and Edge Cases are explicitly defined.
2. **Repository Injection (`/stories/`):** When the sprint begins, the **context-enriched story** is physically exported (manually or via webhook) and saved as a Markdown file inside the codebase, adjacent to the feature code (e.g., `src/billing/stories/BILL-102.md`). *This is the most critical step—if the context is not in the repository, the AI cannot accurately see it.*
3. **MCP / Tool Calling Execution (IDE):** The Builder opens their IDE. Instead of writing a "blank canvas" chat prompt, their AI Agent relies on a **Function Registry** and the **2-Tier Router**. The Agent programmatically ingests the active story from `docs/stories/` and the domain context from `docs/context/`, mathematically constraining the generated code.
4. **Contract-First Validation (CI/CD):** The Validation Lead does not write tests based on what the Builder *says* they built. The Validation Lead uses an AI agent to read the exact same `BILL-102.md` file and generate adversarial tests. The CI pipeline executes these tests against the Builder's code.
5. **Telemetry & Tracing (Release Pipeline):** When the code merges, the Deployment Lead's automated pipeline (e.g., a GitHub Action) scans the commit. It links the PR back to the original context-enriched story and attaches an AI Software Bill of Materials (SBOM) to track which agent generated which lines of code.


## The Virtuous Cycle
**Better Context** → **Better AI Answers** → **Fewer Meetings** → **More time to create better context.**

---

[**Return to Root README →**](./README.md)
