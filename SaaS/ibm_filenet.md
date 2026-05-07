# SaaS Context Factory: IBM FileNet (P8)

## 🎯 The Industrial Objective
Managing Enterprise Content through **Deterministic Metadata and Workflow Engineering**.

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The Context Factory starts with clear requirements *before* any engineering work begins. POs and BAs provide the crucial **Context-Enriched Stories**.
*   **Semantic Blueprints:** POs contribute by maintaining high-level Taxonomy Maps directly in the `docs/stories/` folder, which GitHub Copilot will read.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues or Jira that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"This new document class must adhere to the retention rules defined in `SaaS/filenet/metadata_schema.md`."*

---

## 🏗️ 2. Context Extraction (Engineer Baseline)
FileNet configurations (like Document Classes and Property Templates) are stored deep inside the Content Engine database. The engineer must use FileNet Deployment Manager (FDM) to extract this for Copilot.

### Step-by-Step Extraction:
### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because FileNet allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Use **FileNet Deployment Manager (FDM)** to export the latest metadata XML for your Document Classes and Properties.
2. **Conflict Detection:** If the Object Store has new properties added via the UI, update your local `src/filenet/schema/` baseline before implementing logic.

1. **Open FileNet Deployment Manager (FDM)** on your Windows client or server.
2. **Create an Export Manifest:**
   * Right-click **Export Manifest** and select **New**.
   * Add the specific Document Classes (e.g., "Invoice") and Property Templates related to your task.
3. **Generate the Dataset:**
   * Right-click your manifest and choose **Export to Deployment Dataset**. FDM generates XML files.
4. **Save to Repo:** Copy these XML files into your Git repository under `src/filenet/classes/`.

---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build the **2-Tier Precision Routing** structure. This acts as an automated traffic controller so engineers don't have to manually prompt the AI with constraints.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context without guessing.

Add the following path-based routing rules:

```markdown
# Global Routing Rules
* If asked to modify files in `src/filenet/ce_scripts/**`, you MUST read `SaaS/filenet/metadata_schema.md` and `SaaS/filenet/ce_api_registry.md` before generating code.
* If asked to modify files in `src/filenet/pe_workflows/**`, you MUST read `SaaS/filenet/process_engine_logic.md` before generating code.
```

### 3b. Tier 2: Domain Constraints
Create **`SaaS/filenet/metadata_schema.md`**: Summarize business rules. Example: *"The `AccountNumber` property must always be a 10-digit string. The AI must enforce this in any validation script it writes."*

### 3c. Tier 2: "The Hands" (CE API Registries & IDE Setup)
1. **IDE Setup:** Create a `/lib/filenet/` folder. Copy `Jace.jar` from your FileNet server into this folder. Add it to your `.classpath` or `pom.xml`. *By adding the JAR to the classpath, Copilot's Java language server reads the compiled classes and prevents hallucinating generic Java libraries.*
2. **The Registry:** Create `SaaS/filenet/ce_api_registry.md` to force connection boilerplate:
   ```java
   # FileNet CE API Constraints
   // Copilot MUST use this exact connection boilerplate for FileNet scripts:
   Connection conn = Factory.Connection.getConnection(uri);
   Subject subject = UserContext.createSubject(conn, username, password, null);
   UserContext.get().pushSubject(subject);
   ObjectStore os = Factory.ObjectStore.fetchInstance(domain, osName, null);
   ```

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the **2-Tier Precision Routing**, the engineer's prompt becomes incredibly simple. The system handles the context deterministically.

1. **Open IDE:** Open Eclipse, IntelliJ, or VS Code.
2. **Open the Target File:** Open the Java file where you are writing the CE API script (e.g., `src/filenet/ce_scripts/AddProperty.java`).
3. **Prompting Copilot Chat:**
   > *"@workspace I need to write a Java script to add the new property defined in the BA's story [Story Link]. Please generate the script."*
4. **The Deterministic Automation:** 
   * **Tier 1 Triggers:** The AI reads the Global Router and sees you are working in the `src/filenet/ce_scripts/` directory.
   * **GPS Navigation:** Following the explicit pointers in the Global Router, the AI navigates directly to `metadata_schema.md` and `ce_api_registry.md` to learn the rules.
   * **Result:** Copilot reads the BA's story, uses the mandatory Java connection boilerplate, parses the `Jace.jar` in your classpath for syntax validation, and generates a perfectly compliant CE API script.

---

## ⚖️ 5. Audit, Validation, & Deployment
1. If Copilot writes a script or modifies an XML dataset, **do not deploy it directly to Production.**
2. **Validation:** Use FDM's **Analyze** feature. Import Copilot's proposed XML dataset into FDM and run an Analysis against your Dev environment. FDM will flag any schema conflicts or missing dependencies.
3. **Deployment:** If the Analysis passes, use FDM to Import and Deploy the changes.



---

## 🏷️ 6. Release & Version Correlation
To prevent version drift between GitHub and the SaaS environment, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** When importing the configuration into the SaaS UI (or deploying via CLI), paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** In GitHub, tag the commit with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

This ensures that if a production issue occurs, you can mathematically trace the live SaaS configuration back to the exact Git commit and AI prompt that generated it.

---

## 🛠️ 7. Local Simulation & Mocking
FileNet logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals**:
1. **Content Engine Mocks:** Use Mockito to mock the `ObjectStore` and `Document` classes from the Jace.jar SDK.
2. **Validation Scripts:** Write a Java test that 'saves' a document to your mock store to verify that the property mappings generated by the AI are valid.

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

To get started immediately, you can copy the physical bootstrap templates we've created for you into your repository.

- [The Global Router](./templates/ibm_filenet/copilot-instructions.md)
- [The Domain Constraint](./templates/ibm_filenet/metadata_schema.md)
- [The Function Registry](./templates/ibm_filenet/ce_api_registry.md)
- [The Token Registry](./templates/ibm_filenet/token_registry.md)
- [The Logic Audit Trail](./templates/ibm_filenet/logic_audit.csv)
- [The Mock Bootstrap](./templates/ibm_filenet/mock_bootstrap.java)
