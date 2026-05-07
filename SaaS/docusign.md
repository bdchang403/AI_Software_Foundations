# SaaS Context Factory: DocuSign Integration

## 🎯 The Industrial Objective
Transforming e-signature workflows into **Contract-First Transaction Pipelines**.

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The Context Factory starts with clear requirements *before* any engineering work begins. POs and BAs provide the crucial **Context-Enriched Stories**.
*   **Semantic Blueprints:** POs contribute by maintaining high-level Contract Lifecycle Maps directly in the `docs/stories/` folder, which GitHub Copilot will read.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues or Jira that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"The event payload must be handled according to the logic defined in `SaaS/docusign/event_routing.md`."*

---

## 🏗️ 2. Context Extraction (Engineer Baseline)
DocuSign templates dictate where users sign and what data is collected. The engineer must pull these down as JSON so Copilot can read the "Tabs" (fields) and "Anchors".

### Step-by-Step Extraction:
### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because DocuSign allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Export the latest **Template JSON** via the DocuSign UI or API and diff it against your `src/docusign/templates/` folder.
2. **Sync Truth:** Always treat the live DocuSign Template ID as the master; ensure your local JSON matches the live state before applying AI edits.

1. **Using the DocuSign Web UI:**
   * Log into DocuSign, go to the **Templates** tab.
   * Select a template, click the action menu, and select **Download**.
   * Move the downloaded JSON file to `src/docusign/templates/`.
2. **Using the API (Advanced):**
   * Ask Copilot to write a script calling: `GET /restapi/v2.1/accounts/{accountId}/templates/{templateId}`
   * Save the response body to `src/docusign/templates/`.

---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build the **2-Tier Precision Routing** structure. This acts as an automated traffic controller so engineers don't have to manually prompt the AI with constraints.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context without guessing.

Add the following path-based routing rules:

```markdown
# Global Routing Rules
* If asked to modify files in `src/docusign/templates/**`, you MUST read `SaaS/docusign/template_standards.md` before generating code.
* If asked to modify files in `src/docusign/webhooks/**`, you MUST read `SaaS/docusign/event_routing.md` and `SaaS/docusign/sdk_registry.md` before generating code.
```

### 3b. Tier 2: Domain Constraints
*   **`template_standards.md`**: Define anchor strings. Example: *"The AI must route signatures to the anchor string `\s1\`. Date fields must route to `\d1\`."*
*   **`event_routing.md`**: State exactly what to do when DocuSign sends a webhook. Example: *"When we receive an `envelope-completed` event, the AI must parse the XML and save the signed PDF to the `/archive` folder."*

### 3c. Tier 2: "The Hands" (SDK Registries & IDE Setup)
1. **IDE Setup (Dependency Indexing):** Run `npm install docusign-esign` (or Maven equivalent) in your repository root. *By installing the SDK, Copilot's language server indexes the `node_modules`, providing perfect autocomplete and syntax accuracy for that specific version.*
2. **The Registry:** Create `SaaS/docusign/sdk_registry.md` to force Auth patterns:
   ```markdown
   # DocuSign SDK Constraints
   * We use the Node.js SDK v6.0+. Do NOT use raw HTTP requests. Do NOT use the SOAP API.
   * For Auth, Copilot MUST use the JWT Grant flow:
     `const jwtLifeSec = 10 * 60; const results = await apiClient.requestJWTUserToken(clientId, userId, scopes, rsaKey, jwtLifeSec);`
   ```

### 🔑 3d. Tier 2: The Token Registry (`SaaS/docusign/token_registry.md`)
To handle environment-specific configurations (Dev vs. Prod), create a Token Registry.
1. Create `SaaS/docusign/token_registry.md`.
2. Map your environment variables:
   ```markdown
   | Key | Dev Value | Prod Value |
   |-----|-----------|------------|
   | `API_URL` | `dev.api.docusign.com` | `prod.api.docusign.com` |
   ```
3. Update your Global Router (`copilot-instructions.md`) to include: `* When generating config, always reference SaaS/docusign/token_registry.md to ensure environment-specific strings are tokenized correctly.`

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the **2-Tier Precision Routing**, the engineer's prompt becomes incredibly simple. The system handles the context deterministically.

1. **Open IDE:** Open VS Code with GitHub Copilot Chat enabled.
2. **Open the Target File:** Open the Webhook listener file you are working on (e.g., `src/docusign/webhooks/listener.js`).
3. **Prompting Copilot Chat:**
   > *"@workspace I need to write a DocuSign Connect webhook listener based on the BA's story [Story Link]. Please generate the code."*
4. **The Deterministic Automation:** 
   * **Tier 1 Triggers:** The AI reads the Global Router and sees you are working in the `src/docusign/webhooks/` directory.
   * **GPS Navigation:** Following the explicit pointers in the Global Router, the AI navigates directly to `event_routing.md` and `sdk_registry.md` to learn the rules.
   * **Result:** Copilot reads the BA's story, applies the event logic, uses the mandatory JWT boilerplate, cross-references the installed `node_modules` for syntax, and generates the webhook code.

---

## ⚖️ 5. Audit, Validation, & Deployment
Before deploying the integration:
1. **The Webhook Tester:** Ask Copilot to generate a "Mock DocuSign Connect Payload" (a sample JSON event matching the BA's scenario).
2. **Validation:** Feed this mock payload into your local webhook listener script to verify it routes correctly based on the `event_routing.md` logic.
3. **Deployment:** Deploy the listener to your staging server and update the DocuSign Connect configuration.



---

## 🏷️ 6. Release & Version Correlation
To prevent version drift between GitHub and the SaaS environment, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** When importing the configuration into the SaaS UI (or deploying via CLI), paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** In GitHub, tag the commit with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

This ensures that if a production issue occurs, you can mathematically trace the live SaaS configuration back to the exact Git commit and AI prompt that generated it.

---

## 🛠️ 7. Local Simulation & Mocking
DocuSign logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals**:
1. **DocuSign Mock Service:** Use the official **DocuSign Mock Service** (Docker-based) or Prism to simulate API responses.
2. **JWT Simulation:** Use a mock JWT provider in your Java tests to bypass the need for a real Integrator Key during local development.

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

To get started immediately, you can copy the physical bootstrap templates we've created for you into your repository.

- [The Global Router](./templates/docusign/copilot-instructions.md)
- [The Domain Constraint](./templates/docusign/event_routing.md)
- [The Function Registry](./templates/docusign/sdk_registry.md)
- [The Token Registry](./templates/docusign/token_registry.md)
- [The Logic Audit Trail](./templates/docusign/logic_audit.csv)
- [The Mock Bootstrap](./templates/docusign/mock_bootstrap.java)
