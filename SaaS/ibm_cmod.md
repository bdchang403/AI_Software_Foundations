# SaaS Context Factory: IBM CMOD (Content Manager OnDemand)

## 🎯 The Industrial Objective
Automating high-volume report archiving through **Precision Indexing and Storage Management**.

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The Context Factory starts with clear requirements *before* any engineering work begins. POs and BAs provide the crucial **Context-Enriched Stories**.
*   **Semantic Blueprints:** POs contribute by maintaining high-level Data Retention Policies directly in the `docs/stories/` folder, which GitHub Copilot will read.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues or Jira that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"This new archival source must be indexed according to the standard in `SaaS/cmod/indexing_standards.md`."*

---

## 🏗️ 2. Context Extraction (Engineer Baseline)
CMOD configurations (Application Groups, Applications, Folders) must be extracted using the `arsxml` tool. This turns the database config into readable XML for Copilot.

### Step-by-Step Extraction:
### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because CMOD allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Run the `arsxml export` command to pull the latest **Application Group** and **Folder** definitions into XML.
2. **Diff Baseline:** Compare the `arsxml` output with your `src/cmod/config/` files to identify any manual 'Trigger' or 'Field' changes made in the CMOD Admin client.

1. Log into your CMOD server.
2. Use the `arsxml` export command to pull down the configuration:
   ```bash
   arsxml export -h YOUR_CMOD_INSTANCE -u admin -p password -i Invoices -t appGrp -o /tmp/Invoices_AppGrp.xml
   arsxml export -h YOUR_CMOD_INSTANCE -u admin -p password -i InvoiceSearch -t folder -o /tmp/InvoiceSearch_Folder.xml
   ```
3. Move these generated `.xml` files into your repository under `src/cmod/config/`.
4. *For Indexing:* Locate your ACIF parameter files (`.parm` or `.txt`) and copy them to `src/cmod/indexers/`.

---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build the **2-Tier Precision Routing** structure. This acts as an automated traffic controller so engineers don't have to manually prompt the AI with constraints.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context without guessing.

Add the following path-based routing rules:

```markdown
# Global Routing Rules
* If asked to modify files in `src/cmod/indexers/**`, you MUST read `SaaS/cmod/indexing_standards.md` and `SaaS/cmod/cli_registry.md` before generating code.
* If asked to modify files in `src/cmod/config/**`, you MUST read `SaaS/cmod/folder_mapping.md` before generating code.
```

### 3b. Tier 2: Domain Constraints
Create **`SaaS/cmod/indexing_standards.md`**: Define how to locate data on a page. Example: *"For Invoices, the Account Number is always located on Line 5, Column 10. Copilot must use this trigger logic."*

### 3c. Tier 2: "The Hands" (CLI & ODWEK Registries & IDE Setup)
1. **IDE Setup (If using Java ODWEK):** Create a `/lib/cmod/` folder. Copy `ODApi.jar` from your server into this folder and add it to your IDE's build path. *This allows Copilot to index the proprietary IBM classes.*
2. **The Registry (For CLI tools):** Create `SaaS/cmod/cli_registry.md` to force safe bash logic:
   ```markdown
   # CMOD CLI Constraints
   * When generating load scripts, Copilot MUST ALWAYS use the `-n` (no load) flag for initial testing.
     Example: `arsload -h instance -u user -p pass -n -g AppGrp -a App file.out`
   ```

### 🔑 3d. Tier 2: The Token Registry (`SaaS/cmod/token_registry.md`)
To handle environment-specific configurations (Dev vs. Prod), create a Token Registry.
1. Create `SaaS/cmod/token_registry.md`.
2. Map your environment variables:
   ```markdown
   | Key | Dev Value | Prod Value |
   |-----|-----------|------------|
   | `API_URL` | `dev.api.cmod.com` | `prod.api.cmod.com` |
   ```
3. Update your Global Router (`copilot-instructions.md`) to include: `* When generating config, always reference SaaS/cmod/token_registry.md to ensure environment-specific strings are tokenized correctly.`

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the **2-Tier Precision Routing**, the engineer's prompt becomes incredibly simple. The system handles the context deterministically.

1. **Open IDE:** Open VS Code with GitHub Copilot Chat enabled.
2. **Open the Target File:** Open the ACIF `.parm` file or the Bash script you want to update (e.g., `src/cmod/indexers/invoice_load.sh`).
3. **Prompting Copilot Chat:**
   > *"@workspace I need to update the ACIF indexing parameters for the BA's story [Story Link]. Please generate the updates."*
4. **The Deterministic Automation:** 
   * **Tier 1 Triggers:** The AI reads the Global Router and sees you are working in the `src/cmod/indexers/` directory.
   * **GPS Navigation:** Following the explicit pointers in the Global Router, the AI navigates directly to `indexing_standards.md` and `cli_registry.md` to learn the rules.
   * **Result:** Copilot reads the BA's story, analyzes the existing `.parm` file, applies the coordinate constraints from Tier 2, applies the safe `-n` flag from the CLI registry, and outputs the updated logic.

---

## ⚖️ 5. Audit, Validation, & Deployment
1. **Index Testing:** When Copilot modifies an ACIF indexer file, run the indexer locally *without* loading into CMOD (`arsload -n`). 
2. **Validation:** Check the generated `.ind` file to ensure the AI correctly captured the target Account Numbers and Dates from the raw print stream.
3. **XML Linting & Deploy:** Use `arsxml validate` to check any AI-modified XML before attempting to import (`arsxml add/update`) it back into the CMOD instance.



---

## 🏷️ 6. Release & Version Correlation
To prevent version drift between GitHub and the SaaS environment, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** When importing the configuration into the SaaS UI (or deploying via CLI), paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** In GitHub, tag the commit with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

This ensures that if a production issue occurs, you can mathematically trace the live SaaS configuration back to the exact Git commit and AI prompt that generated it.

---

## 🛠️ 7. Local Simulation & Mocking
CMOD logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals**:
1. **ODWEK Mocking:** Mock the `ODServer` and `ODHit` classes from the ODWEK Java API.
2. **Sample Data Injection:** Create a `test/cmod/sample_load.txt` file and write a mock parser that simulates how your indexing logic will split the file based on the AI-generated coordinates.

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

To get started immediately, you can copy the physical bootstrap templates we've created for you into your repository.

- [The Global Router](./templates/ibm_cmod/copilot-instructions.md)
- [The Domain Constraint](./templates/ibm_cmod/indexing_standards.md)
- [The Function Registry](./templates/ibm_cmod/cli_registry.md)
- [The Token Registry](./templates/ibm_cmod/token_registry.md)
- [The Logic Audit Trail](./templates/ibm_cmod/logic_audit.csv)
- [The Mock Bootstrap](./templates/ibm_cmod/mock_bootstrap.java)
