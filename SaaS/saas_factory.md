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

## 🏗️ 2. Context Extraction & Synchronization (Engineer Baseline)
Your first job when working with *any* new SaaS tool is to figure out how to export its state so Copilot can read it.

### 2a. The Initial Baseline
*   **Action:** Find the "Export", "Backup", or "CLI" tool for the platform. 
*   **Outcome:** Generate XML, JSON, YAML, or XAML files. 
*   **Git Commit:** Commit these files to your GitHub repository (e.g., `src/[saas_name]/`). Now Copilot has a baseline!

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
1. **Bring the SDK to the IDE:** Download the proprietary SaaS `.dll`, `.jar`, SDK, or OpenAPI Swagger spec. Put them in your repository and add them to your build path.
2. **Create the Registry Markdown:** Create a markdown file (e.g., `api_registry.md`) showing exact examples of the allowed syntax and boilerplate.

### 🔑 3d. Tier 2: The Token Registry (`docs/context/[saas_name]/token_registry.md`)
To handle environment-specific configurations (Dev vs. Prod), create a Token Registry. Reference this in your Global Router to ensure AI-generated config is environment-agnostic.

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the 2-Tier Precision Routing, the engineer does not have to manually explain business rules in every prompt.

1.  **Open Target File:** The engineer opens the config file they need to modify (e.g., `src/[saas_name]/config.xml`).
2.  **Prompt Copilot Chat:** 
    > *"@workspace I need to implement the BA's story linked here: [Story Link]. Please generate the configuration changes."*
3.  **The Deterministic Automation:** The AI follows the Global Router pointers to the Domain Constraints and SDK Registry to generate logic.
4. **Update Logic Audit:** Open `docs/context/[saas_name]/logic_audit.csv` and ask Copilot: *"Summarize the reasoning for these changes and append a new line to the logic_audit.csv following the format: Date, StoryID, Component, Rationale, AI_Model."*

---

## ⚖️ 5. Audit, Validation, & Deployment
Before you import the AI's modified configuration back into the SaaS platform:
1. **Schema Validation:** Ask Copilot to write a Python script that validates your new config against the official **XSD/JSON Schema**.
2. **Visual/Functional Regression:** If applicable, run a test output (e.g., PDF, Log, or Response) and compare the "Before" and "After" states to ensure no regression.
3. **Deployment:** Commit the validated config to GitHub, then use the SaaS tool's **Import** function to bring the changes into the Dev environment.

---

## 🏷️ 6. Release & Version Correlation
To prevent version drift, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** Paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** Tag the commit in GitHub with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

---

## 🛠️ 7. Local Simulation & Mocking
SaaS logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals** using SDK mocks or API interceptors (e.g. Prism/WireMock) to verify logic *before* hitting the cloud.

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

- [The Global Router](./templates/saas_factory/copilot-instructions.md)
- [The Domain Constraint](./templates/saas_factory/[saas_name]_business_rules.md)
- [The Function Registry](./templates/saas_factory/[saas_name]_api_registry.md)
- [The Token Registry](./templates/saas_factory/token_registry.md)
- [The Logic Audit Trail](./templates/saas_factory/logic_audit.csv)
- [The Mock Bootstrap](./templates/saas_factory/mock_bootstrap.java)
