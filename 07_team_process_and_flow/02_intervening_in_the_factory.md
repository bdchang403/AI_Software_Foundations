# Module 2: Intervening in the Factory (Targeted Role Coaching)

---

## 🎯 Executive Overview & Coaching Philosophy

When an AI-assisted engineering team struggles with degraded quality, ballooning cycle times, or security alerts, inexperienced management often responds with blunt, ineffective mandates: *"Ban AI usage,"* *"Slow down,"* or *"Send everyone to prompt engineering training."*

In the **Context Factory**, process failures are structural, not individual. An autonomous agent is a deterministic mirror of the context it receives. When an agent produces broken code, the failure occurred at an upstream hand-off. The Agile Leader acts as an **Industrial Quality Inspector**, intervening precisely at the point of context breakdown using structured, role-specific coaching protocols.

| Factory Role | Observable Failure Symptom | Structural Root Cause & Immediate Action |
| :--- | :--- | :--- |
| **Strategy Lead** | Scope creep; dead code bloat | Epic lacks value thesis & bounded scope; enforce business invariants. |
| **Requirements Lead** | Agent prompt loops (High CDR) | Semantic Blueprint missing edge cases; mandate 20-edge-case matrix. |
| **Software Builder** | PRs $> 400$ LOC; CI timeouts | Modularity Ceiling violated; decompose into Bounded Task Units (BTUs). |
| **Validation Lead** | Production bugs (High QDF) | AST Zero-Mock bypassed; enforce real recorded telemetry (ZM001–ZM009). |
| **BuilderOps Lead** | Unverified provenance in prod | AI-SBOM omitted; enforce zero-drift pre-commit check (`git diff --exit-code`). |

---

## 🛠️ Role-by-Role Intervention Playbooks & Coaching Scripts

### Playbook 1: Intervening with the Strategy Lead
*   **Trigger Symptom**: Large batches of agent-generated features are abandoned post-implementation; product backlog churns rapidly.
*   **Structural Root Cause**: The Strategy Lead is issuing open-ended feature requests without defining the business invariant or value metrics.
*   **Coaching Script (Simplified Technical English)**:
    > **Agile Leader**: "The engineering team delivered 12 agent-generated microservices this sprint, but 7 were rejected by compliance. We cannot feed open-ended initiatives to builders. Before this epic enters sprint planning, you must define: (1) The explicit business invariant, (2) The non-negotiable compliance constraint, and (3) The bounded value thesis. An agent without strategic boundaries builds unmaintainable software at light speed."

---

### Playbook 2: Intervening with the Requirements Lead (Business Analyst / Product Owner)
*   **Trigger Symptom**: Context Debt Ratio ($\text{CDR}$) exceeds $0.20$. Builders report running 8 to 15 prompt iterations per ticket.
*   **Structural Root Cause**: The user story lacks a structured **Semantic Blueprint** or fails to specify the **20-Edge-Case Matrix**. The agent is guessing data types and error responses.
*   **Coaching Script**:
    > **Agile Leader**: "Your user stories contain narrative paragraphs instead of mathematical schemas. Look at ticket SEC-402: the builder spent 180,000 tokens because the agent kept hallucinating different null-handling logic. We must halt generation on this story. Convert the narrative into our 3-Part Directive format with explicit input/output schemas and the 20-edge-case matrix before handing off to development."

---

### Playbook 3: Intervening with the Software Builder (Software Engineer)
*   **Trigger Symptom**: Pull requests exceed 1,000 lines of code; code review comments spike; reviewers express exhaustion.
*   **Structural Root Cause**: The builder bypassed the **Architectural Modularity Ceiling (maximum 400 lines of code)** and dumped an entire epic into a single prompt session.
*   **Coaching Script**:
    > **Agile Leader**: "This pull request contains 1,450 lines of code across 18 files. Human reviewers cannot verify this safely, and our automated invariant scanners cannot isolate fault domains. The Architectural Modularity Ceiling is 400 lines of code. Split this task into three Bounded Task Units (BTUs). Compile your AST Living Context to keep context below 1,500 tokens before prompting the model."

---

### Playbook 4: Intervening with the Validation Lead (Quality Engineer)
*   **Trigger Symptom**: Change Failure Rate ($\text{CFR}$) rises despite 100% green unit test reports in CI.
*   **Structural Root Cause**: Test tautology and mock data smuggling. The agent wrote unit tests that mocked out the actual database and business logic, satisfying code coverage while hiding critical defects.
*   **Coaching Script**:
    > **Agile Leader**: "Our production incident yesterday passed every automated unit test. When we inspected the test suite, the agent mocked the database layer using `MagicMock` with hardcoded return values (violating AST Zero-Mock Rule ZM001). The tests validated the agent own hallucinations. You must replace all synthetic mocks with the SQLite in-memory test harness and enforce `scan_mock_data.py` on every PR."

---

### Playbook 5: Intervening with the BuilderOps Engineer (Release / Platform)
*   **Trigger Symptom**: Git commits lack cryptographic audit signatures; context registry drift goes undetected between releases.
*   **Structural Root Cause**: The zero-drift pre-commit hooks and SPDX 3.0 AI-SBOM generator workflows were disabled or bypassed using `--no-verify`.
*   **Coaching Script**:
    > **Agile Leader**: "We detected unverified commits deployed to our staging environment that lacked AI-SBOM traceability headers. Under model risk governance, unverified deployments violate regulatory compliance. We are enabling branch protection rules that enforce automated drift verification and reject any merge lacking a validated UUIDv4 execution trace."

---

## 🔄 The Multi-Role Escalation & Remediation Workflow

```mermaid
flowchart TD
    A["Telemetry Anomaly Detected (CDR > 0.20 or QDF > 0.05)"] --> B["Agile Leader Triages Forensic Trace"]
    
    B --> C{"Identify Breach Domain"}
    C -- "Story Ambiguity" --> D["Quarantine Story Back to Requirements Lead"]
    C -- "Code Bloat (>400 LOC)" --> E["Reject PR Back to Builder for Decomposition"]
    C -- "Synthetic Mocking" --> F["Demote Test Suite Back to Validation Lead"]
    C -- "Drift / Audit Gap" --> G["Block Pipeline via BuilderOps Pre-Commit Gate"]
    
    D --> H["Execute Semantic Blueprint Remediation"]
    E --> I["Enforce Architectural Modularity Refactoring"]
    F --> J["Apply AST Zero-Mock Rules (ZM001-ZM009)"]
    G --> K["Regenerate SPDX 3.0 AI-SBOM Headers"]
    
    H & I & J & K --> L["Verify Clean Trace & Resume Autonomous Pipeline"]
    
    style A fill:#ffcdd2,stroke:#c62828,stroke-width:2px;
    style L fill:#d4edda,stroke:#28a745,stroke-width:2px;
```

---

## 🏥 Dual-Use Industry Case Studies

| Regulated Sector | Operational Problem | Agile Leader Intervention | Verified Business Outcome |
| :--- | :--- | :--- | :--- |
| **Healthcare Infusion Controller (FDA 21 CFR 820.30)** | Agent generated unit tests passing on mocked synthetic sensor data | Intervened with Validation Lead; enforced rule ZM001 (Zero Synthetic Data) against recorded clinical streams | Detected insulin overdose edge-case prior to pre-market clinical validation |
| **Financial Core Wire Router (Fed SR 11-7)** | Builder submitted oversized 2,200 LOC pull request for FX settlement | Rejected PR citing Modularity Ceiling; sliced into (1) Schema, (2) Solvency gate, (3) Wire execution | Review cycle dropped from 4 days to 45 minutes; zero production regressions |

---

## 📋 Module Summary & Practical Next Step

---

## Production Reality & Operational Failure Modes in the AI Era

### The Mid-2026 Production Baseline (The Verification Trap & Context Debt)

> [!WARNING]
> **Individual Blame vs. Assembly Line Failure**: Treating failed model generations as individual developer errors obscures structural upstream context defects.

In the median mid-2026 pod, failed AI implementations are blamed on individual developers. Leadership assumes engineers lack prompting skills or that models hallucinate unpredictably.

This misunderstanding leads to solitary prompt hacking:
* **Prompt Death Loops**: Developers iterate 8 to 12 times with IDE chat assistants, copy-pasting errors and consuming thousands of tokens without forward progress.
* **Ignored Assembly Lines**: Teams rarely analyze the context pipeline or recognize upstream failures.
* **Missing Root-Cause Audits**: Nobody inspects whether the Product Owner provided an unconstrained directive, the Analyst omitted the edge-case matrix, or the Architect forgot schema contracts.

### Ungoverned Production Failure Modes
Treating AI generation errors as random stochastic accidents rather than systemic upstream pipeline failures causes severe operational damage:
- **Engineering Capacity Hemorrhage**: Developers spend 30% to 40% of their sprint capacity trapped in unproductive prompt-retry death loops. Token expenditures spike while working software output stagnates.
- **Sprint Delivery Collapse**: Stories that appear "almost done" on Day 2 of a two-week sprint linger in review paralysis or prompt debugging through Day 10, completely destroying sprint predictability and team morale.
- **Viral Technical Debt Ingestion**: Engineers under deadline pressure eventually accept whatever functioning workaround the model provides, committing anti-patterns, duplicate helper functions (the GitClear cloning inversion), and bypassed security checks into production branches.

### Deterministic Engineering Defenses & Operational Takeaways
To transform the software factory into a deterministic delivery engine, engineering organizations must enforce four operational protocols:
1. **Enforce the "3-Iteration Prompt Circuit Breaker"**: If an engineer cannot generate a compiling, passing implementation within 3 prompt iterations, they must halt re-prompting. They must inspect and identify which upstream context asset (AST registry, schema, or invariant boundary) is missing or corrupted.
2. **Execute Standardized Factory Coaching Scripts**: When a PR is rejected for architectural drift or review bloat, leads must intervene using role-specific coaching scripts (BA for missing edge cases, Architect for missing schemas, Builder for oversized task slices).
3. **Institute Daily Context-Blocker Standup Triage**: In daily standups, replace passive status recitations with targeted blockers: *"Did any AI workflow fail to produce clean code on the first pass, and what upstream contract was missing?"*
4. **Mandate Bounded Task Slicing Before Prompting**: Never permit a developer to prompt a model for an entire feature. Tasks must be pre-sliced into Bounded Task Units (BTUs) targeting under 80 lines of diff before any prompt is executed.

---

[**Proceed to Module 3: Tooling and Analysis (The Determinism Proof) →**](./03_tooling_and_analysis.md)

