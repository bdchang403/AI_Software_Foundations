# The SaaS Factory: Managing COTS Configurations in GitHub

## 🎯 The Industrial Objective
GitHub Copilot cannot see inside a proprietary SaaS database or a UI. To effectively use AI assistance, we must turn SaaS platforms into a "Codebase" that Copilot can index and understand.

This document outlines the **Left-to-Right SDLC Flow** for applying Context Factory principles to *any* Commercial Off-The-Shelf (COTS) or SaaS product (e.g., UiPath, Salesforce, ServiceNow).

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The workflow starts with the business defining the "Why" and "What" before engineers touch the configuration.
*   **Semantic Blueprints:** POs maintain high-level Business Process Maps directly in the `docs/stories/` folder.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"Constraint: This new integration must strictly adhere to the Q3 Security Boundaries policy."* (The Global Router will automatically map this semantic rule to the correct technical markdown based on the file path).

---

---

## 🏗️ 2. Context Extraction & Synchronization (The Brownfield Baseline)
As Peter Bell identifies in *Scaling AI Adoption in Engineering* (O'Reilly, 2026, Ch. 1–2), applying AI to brownfield enterprise stacks without automated test harnesses and baselines accelerates technical debt. COTS and SaaS platforms (e.g., IBM FileNet, IBM CMOD, OpenText Exstream, Tungsten TotalAgility, DocuSign, SideDrawer) represent mission-critical brownfield systems where drift can cause severe operational and regulatory non-compliance.

### 2a. The Initial Baseline
*   **Action:** Find the "Export", "Backup", or "CLI" tool for the platform (e.g., FileNet FDM, CMOD `arsdoc`, TTA `PackageService`, Exstream Design Manager export). 
*   **Outcome:** Generate XML, JSON, YAML, or XAML files. 
*   **Git Commit:** Commit these files to your GitHub repository (e.g., `src/[saas_name]/`). Now Copilot and coding agents have an immutable baseline!

### 🛡️ 2b. Managing "Split-Brain" Conflict (Anti-Drift)
Because SaaS tools allow manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Before every implementation, you MUST export the latest state from the SaaS UI/CLI and perform a `git diff` against your local `src/` folder.
2. **Conflict Resolution:** If the UI has drifted, commit the UI's "truth" to GitHub *before* asking the AI to implement new logic. This prevents overwriting manual production hotfixes.

---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build a **2-Tier Precision Routing** structure. This acts as an automated traffic controller.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context.

*   *Rule Example:* `If asked to modify files in src/[saas_name]/**, you MUST read docs/context/[saas_name]/branding.md before generating code.`

### 3b. Tier 2: Domain Constraints
These are the markdown files that contain your organizational ADRs, branding rules, and business logic boundaries.

### 3c. Tier 2: "The Hands" (Registries & IDE Setup)
1. **Bring the SDK to the IDE:** Download the proprietary SaaS `.dll`, `.jar`, SDK, or OpenAPI Swagger spec (e.g., FileNet `Jace.jar`, TTA `Agility.Sdk.Model.dll`). Put them in your repository and add them to your build path.
2. **Create the Registry Markdown:** Create a markdown file (e.g., `api_registry.md`) showing exact examples of the allowed syntax and boilerplate.

### 🔑 3d. Tier 2: The Token Registry (`docs/context/[saas_name]/token_registry.md`)
To handle environment-specific configurations (Dev vs. Prod), create a Token Registry. Reference this in your Global Router to ensure AI-generated config is environment-agnostic.

---

## 💻 4. AI-Assisted Implementation: The "Ralph Wiggum" Convergence Loop
Rather than unconstrained chat loops, agentic configuration changes follow the **Ralph Wiggum Loop** (Bell, 2026, Ch. 5):

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    SAAS CONFIG RALPH CONVERGENCE LOOP                        │
│                                                                              │
│  [BA Story + SaaS Schema / API Registry + Prior Failure Ledger]              │
│                       │                                                      │
│                       ▼                                                      │
│           [Spawn Ephemeral Agent]                                            │
│                       │                                                      │
│                       ▼                                                      │
│       [Execute Verifiable Reward Gate (Rv)]                                  │
│        • XML/JSON Schema Validates against XSD                               │
│        • Java/C# Compiles against Local Mock SDK Bootstrap                  │
│        • Modularity & Token Invariants Satisfied                             │
│                       │                                                      │
│        ┌──────────────┴──────────────┐                                       │
│        ▼ (PASS)                      ▼ (FAIL & Budget Remaining)             │
│  [Emit .audit/PR-<id>.jsonl]     [Log Delta to Failure Ledger]               │
│                                  [Worktree Reset & Respawn Clean Agent]      │
└──────────────────────────────────────────────────────────────────────────────┘
```

1. **The Verifiable SaaS Reward ($R_v$):**
   $$R_v(s) = \mathbb{I}(\text{SchemaPass}) \times \mathbb{I}(\text{MockCompiles}) \times \mathbb{I}(\text{AuditValid})$$
2. **Deterministic Context Injection:** The AI reads the Global Router pointers to the Domain Constraints and SDK Registry to generate logic.
3. **Structured Audit Emission:** Every PR appends a structured record to `docs/context/[saas_name]/.audit/PR-<id>.jsonl` governed by `audit_schema.json`, capturing `review_risk_tier`, `loop_iterations_burned`, `verifiable_reward_score`, and `failed_hypotheses_logged`.

---

## ⚖️ 5. Audit, Validation, & Risk-Tiered PR Routing
To prevent SaaS configuration PRs from congesting the engineering review queue (Bell, 2026, Ch. 5), review workflows are partitioned into **3 Risk Tiers**:

1. **Tier 0: Dark Auto-Merge (0 Human Reviewers):**
   * Scope: Environment Token Registry syncs, schema docstring updates, or isolated test fixture backfills.
   * Gate: Automated XSD/JSON schema validation passes, zero blast radius.
2. **Tier 1: Streamlined Single Approval (SLA < 2 hrs):**
   * Scope: Bounded workflow routing changes, property mapping scripts, or single-form field additions.
   * Gate: Passing local mock bootstrap (`mock_bootstrap.java` / `.cs`), passing schema checks, and $R_v \ge 0.80$.
3. **Tier 2: Full Architectural Review (2 Human Approvers):**
   * Scope: Cross-system schema modifications, authentication/permission models, legal retention rules (e.g. SEC 17a-4 / FINRA in CMOD/FileNet), or cryptographic key management (SideDrawer).
   * Gate: Full human inspection of the Semantic Blueprint and CISO compliance verification.

### 5b. Deployment
Commit the validated config to GitHub, then use the SaaS tool's **Import** function or CI/CD deployment runner to bring the changes into the target environment.

---

## 🏷️ 6. Release & Version Correlation
To prevent version drift, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** Paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** Tag the commit in GitHub with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

---

## 🛠️ 7. Local Simulation & Mocking
SaaS logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals** using SDK mocks or API interceptors (e.g., Prism, WireMock, `mock_bootstrap.java`) to verify logic *before* hitting the cloud.

---

## 🚀 Appendix: Platform Guides & Templates

### Dedicated Platform Implementations
- [IBM FileNet (P8) Guide](./ibm_filenet.md)
- [IBM CMOD Guide](./ibm_cmod.md)
- [OpenText Exstream Guide](./opentext_exstream.md)
- [DocuSign eSignature Guide](./docusign.md)
- [SideDrawer Vault Guide](./sidedrawer.md)
- [Tungsten TotalAgility Guide](./tungsten_total_agility.md)

### Quick-Start Bootstrap Templates
- [The Global Router](./templates/saas_factory/copilot-instructions.md)
- [The Domain Constraint](./templates/saas_factory/[saas_name]_business_rules.md)
- [The Function Registry](./templates/saas_factory/[saas_name]_api_registry.md)
- [The Token Registry](./templates/saas_factory/token_registry.md)
- [The Logic Audit Schema](./templates/saas_factory/.audit/audit_schema.json)
- [The Logic Audit Trail](./templates/saas_factory/.audit/PR-<id>.jsonl)
- [The Mock Bootstrap](./templates/saas_factory/mock_bootstrap.java)
