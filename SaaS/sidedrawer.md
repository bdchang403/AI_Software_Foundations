# SaaS Context Factory: SideDrawer

## 🎯 The Industrial Objective
Managing secure client collaboration through **Schema-Driven Document Vaulting**.

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The Context Factory starts with clear requirements *before* any engineering work begins. POs and BAs provide the crucial **Context-Enriched Stories**.
*   **Semantic Blueprints:** POs contribute by maintaining the high-level Information Architecture (folder structures) directly in the `docs/stories/` folder, which GitHub Copilot will read.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues or Jira that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"This new folder structure must adhere to the permission rules defined in `SaaS/sidedrawer/security_matrix.md`."*

---

## 🏗️ 2. Context Extraction (Engineer Baseline)
SideDrawer is an API-first platform. To give GitHub Copilot context, the engineer must use the API to pull down configurations into JSON files.

### Step-by-Step Extraction:
### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because SideDrawer allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Use the SideDrawer GET APIs to export the current **JSON settings** for your organization and compare against your `src/` baseline.
2. **Drift Management:** Since SideDrawer is API-first, ensure you 'GET' the latest resource state before 'PUTting' any AI-generated configuration.

1. **Get an API Token:** Log into SideDrawer Developer portal and generate an API key.
2. **Fetch Drawer Templates:**
   ```bash
   curl -X GET "https://api.sidedrawer.com/v1/drawer-templates" \
        -H "Authorization: Bearer YOUR_TOKEN" > src/sidedrawer/templates/current_templates.json
   ```
3. **Fetch Webhook Configs:**
   ```bash
   curl -X GET "https://api.sidedrawer.com/v1/webhooks" \
        -H "Authorization: Bearer YOUR_TOKEN" > src/sidedrawer/webhooks/current_webhooks.json
   ```

---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build the **2-Tier Precision Routing** structure. This acts as an automated traffic controller so engineers don't have to manually prompt the AI with constraints.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context without guessing.

Add the following path-based routing rules:

```markdown
# Global Routing Rules
* If asked to modify files in `src/sidedrawer/scripts/**`, you MUST read `SaaS/sidedrawer/provisioning_logic.md` and `SaaS/sidedrawer/api_registry.md` before generating code.
* If asked to modify files in `src/sidedrawer/templates/**`, you MUST read `SaaS/sidedrawer/security_matrix.md` before generating code.
```

### 3b. Tier 2: Domain Constraints
Create **`SaaS/sidedrawer/security_matrix.md`**: Define the roles. Example: *"Sponsors have full access. Viewers can only read. The AI must ALWAYS assign the Viewer role to third-party consultants in the API payload."*

### 3c. Tier 2: "The Hands" (API Registries & IDE Setup)
Because SideDrawer is an API, Copilot needs to know exactly what the API endpoints expect. 

1. **IDE Setup (OpenAPI Indexing):** Create a `/lib/openapi/` folder. Download the official SideDrawer OpenAPI specification (`.yaml` or `.json`) into it. *Copilot natively indexes Swagger files, instantly understanding every valid endpoint.*
2. **The Registry:** Create `SaaS/sidedrawer/api_registry.md` to define your payload *business rules*:
   ```markdown
   # Create Drawer Payload Constraints
   When writing scripts to call POST /v1/drawers, Copilot MUST format the payload this way:
   { 
     "title": "Client Name", 
     "template_id": "YOUR_TEMPLATE_UUID", // Do not hardcode UUIDs, fetch them.
     "owner": { "email": "client@example.com" } 
   }
   ```

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the **2-Tier Precision Routing**, the engineer's prompt becomes incredibly simple. The system handles the context deterministically.

1. **Open IDE:** Open VS Code with GitHub Copilot Chat enabled.
2. **Open the Target File:** Open the Python or Node.js script where you are writing the API integration (e.g., `src/sidedrawer/scripts/provision.py`).
3. **Prompting Copilot Chat:**
   > *"@workspace I need to write an API script to provision new drawers based on the BA's story [Story Link]. Please generate the script."*
4. **The Deterministic Automation:** 
   * **Tier 1 Triggers:** The AI reads the Global Router and sees you are working in the `src/sidedrawer/scripts/` directory.
   * **GPS Navigation:** Following the explicit pointers in the Global Router, the AI navigates directly to `api_registry.md` and `provisioning_logic.md` to learn the rules.
   * **Result:** Copilot reads the BA's story, parses the OpenAPI swagger file in your workspace for the exact HTTP structure, applies the security constraints from Tier 2, and outputs a highly accurate API script.

---

## ⚖️ 5. Audit, Validation, & Deployment
Before running an AI-generated script that creates objects via API:
1. **Schema Validation:** Validate the AI's generated JSON payload against the SideDrawer OpenAPI specification (Swagger) to ensure no required fields are missing.
2. **Dry Run:** Run the script in **Dry-Run Mode** (if you built one) or point the API base URL to a sandbox environment.
3. **Deployment:** Once verified in sandbox, update the API URL to Production and execute the provisioning.



---

## 🏷️ 6. Release & Version Correlation
To prevent version drift between GitHub and the SaaS environment, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** When importing the configuration into the SaaS UI (or deploying via CLI), paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** In GitHub, tag the commit with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

This ensures that if a production issue occurs, you can mathematically trace the live SaaS configuration back to the exact Git commit and AI prompt that generated it.

---

## 🛠️ 7. Local Simulation & Mocking
SideDrawer logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals**:
1. **Prism API Mocking:** Use **Prism** to run a local mock server based on the SideDrawer OpenAPI spec.
2. **Contract Testing:** Point your local Java implementation to the Prism mock (`localhost:4010`) to verify JSON structure before hitting the sandbox.

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

To get started immediately, you can copy the physical bootstrap templates we've created for you into your repository.

- [The Global Router](./templates/sidedrawer/copilot-instructions.md)
- [The Domain Constraint](./templates/sidedrawer/security_matrix.md)
- [The Function Registry](./templates/sidedrawer/api_registry.md)
- [The Token Registry](./templates/sidedrawer/token_registry.md)
- [The Logic Audit Trail](./templates/sidedrawer/logic_audit.csv)
- [The Mock Bootstrap](./templates/sidedrawer/mock_bootstrap.java)
