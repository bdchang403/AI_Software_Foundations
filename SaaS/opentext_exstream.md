# SaaS Context Factory: OpenText Exstream

## 🎯 The Industrial Objective
Transforming OpenText Exstream template design and data mapping from manual "UI clicking" into **Deterministic Configuration Engineering**.

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The Context Factory starts with clear requirements *before* any engineering work begins. POs and BAs provide the crucial **Context-Enriched Stories**.
*   **Semantic Blueprints:** POs maintain high-level Business Requirements directly in the `docs/stories/` folder, which GitHub Copilot will read to understand the 'why'.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues or Jira that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"Constraint: This new template must strictly adhere to the Q3 Corporate Branding Guidelines."* (The Global Router will automatically map this to the correct branding markdown based on the file path).*

---

## 🏗️ 2. Context Extraction (Engineer Baseline)
Before GitHub Copilot can assist with the BA's story, the engineer must get the current configuration *out* of the Exstream UI and into text files (XML) that Copilot can read.

### Step-by-Step Extraction:
### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because Exstream allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Before every implementation, you MUST export the latest **Transport Package (XML)** from Exstream Design Manager and perform a `git diff` against your local `src/` folder.
2. **Conflict Resolution:** If the UI has drifted, you must commit the UI's 'truth' to GitHub *before* asking the AI to implement new logic.

**Method A: Using Design Manager (UI)**
1. Open **Exstream Design Manager**.
2. In the tree view, locate the **Application** or **Library** you need to modify.
3. Right-click the object and select **Export**.
4. **CRITICAL:** Select the **XML format** option (do not select the proprietary package format).
5. Save the generated XML to your repository: `src/exstream/templates/application_name.xml`.

**Method B: Extracting Data Maps**
1. In Design Manager, navigate to the **Data Dictionary**.
2. Select your variables and choose **Export**.
3. Save as CSV to `src/exstream/mapping/data_dictionary.csv`.

### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because OpenText Exstream allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Before every implementation, you MUST export the latest XML from Exstream and perform a `git diff` against your local `src/` folder.
2. **Conflict Resolution:** If the UI has drifted, you must commit the UI's "truth" to GitHub *before* asking the AI to implement new logic. This prevents the AI from accidentally deleting manual production hotfixes.


---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build the **2-Tier Precision Routing** structure. This acts as an automated traffic controller so engineers don't have to manually prompt the AI with constraints.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context without guessing.

Add the following path-based routing rules:

```markdown
# Global Routing Rules
* If asked to modify files in `src/exstream/templates/**`, you MUST read `SaaS/exstream/branding_standards.md` before generating code.
* If asked to modify files in `src/exstream/mapping/**`, you MUST read `SaaS/exstream/data_schemas.md` before generating code.
* If asked to write or modify formulas, you MUST read `SaaS/exstream/formula_registry.md` before generating code.
```

### 3b. Tier 2: Domain Constraints
Create **`SaaS/exstream/branding_standards.md`**. Literally write out the hex codes and font names. Example: *"All headers must be Arial 14pt, Color: #003366. Do not let the AI use any other color."*

### 3c. Tier 2: "The Hands" (Formula Registries & IDE Setup)
Because Exstream uses a proprietary formula language, Copilot will hallucinate JavaScript unless stopped.
1. **IDE Setup:** Save Exstream formula scripts with a `.js` or `.txt` extension in your repository so Copilot's indexing engine can scan them.
2. **The Registry:** Create `SaaS/exstream/formula_registry.md` as your strict syntax constraint:
   ```markdown
   # Allowed Exstream Formulas
   You MUST use these specific functions:
   * Dates: USE `GetDate()` - DO NOT USE `Date.now()`
   * Strings: USE `StrCat(a, b)` - DO NOT USE `a + b`
   ```

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the **2-Tier Precision Routing**, the engineer's prompt becomes incredibly simple. The system handles the context deterministically.

1. **Open IDE:** Open VS Code with GitHub Copilot Chat enabled.
2. **Open the Target File:** Open the XML file or Formula script you want to edit (e.g., `src/exstream/mapping/invoice.csv`).
3. **Prompting Copilot Chat:**
   > *"@workspace I need to implement the data mapping logic for the BA's story linked here: [Story Link]. Please generate the changes."*
4. **The Deterministic Automation:** 
   * **Tier 1 Triggers:** The AI reads the Global Router and sees you are working in the `src/exstream/mapping/` directory.
   * **GPS Navigation:** Following the explicit pointers in the Global Router, the AI navigates directly to `data_schemas.md` and `formula_registry.md` to learn the rules.
   * **Result:** Copilot generates the proprietary Exstream logic deterministically without you having to manually tag `#file` or explain Exstream syntax.
5. **Update Logic Audit:** Open `SaaS/exstream/logic_audit.csv` and ask Copilot: *"Summarize the reasoning for these changes and append a new line to the logic_audit.csv following the format: Date, StoryID, Component, Rationale, AI_Model."*

---

## ⚖️ 5. Audit, Validation, & Deployment
Before you import the AI's modified XML back into Exstream, you must validate it.
1. **Linting:** Ask Copilot to write a Python script that validates your new XML against the official **Exstream Design XSD** (XML Schema Definition).
2. **Deployment:** If the XML passes validation, use the Exstream UI **Import** function to bring the changes back into the Dev environment.
3. **Visual Regression:** Run a test output and compare the "Before" and "After" PDF to ensure no branding regression occurred.



---

## 🏷️ 6. Release & Version Correlation
To prevent version drift between GitHub and the SaaS environment, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** When importing the configuration into the SaaS UI (or deploying via CLI), paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** In GitHub, tag the commit with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

This ensures that if a production issue occurs, you can mathematically trace the live SaaS configuration back to the exact Git commit and AI prompt that generated it.

---

## 🛠️ 7. Local Simulation & Mocking
Exstream logic is notoriously difficult to test without the full engine. To speed up development, you must build **Mock Data Injections**.
1. **The Mock Baseline:** Create `test/exstream/mock_data.xml`. This should contain the most complex data scenarios (e.g., missing fields, multi-page overflows).
2. **AI Simulation:** Ask Copilot: *"Using the formula rules in SaaS/exstream/formula_registry.md, simulate how the GetDate() function will transform the data in mock_data.xml. Output the result to a console log."*
3. **Validation:** This allows you to verify logic *before* the expensive and slow "Import-to-SaaS" cycle.


---

## 🛠️ 7. Local Simulation & Mocking
Exstream logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals**:
1. **The Mock Baseline:** Create `test/exstream/mock_data.xml` containing complex data scenarios.
2. **AI Simulation:** Ask Copilot: *'Using the formula rules in SaaS/exstream/formula_registry.md, simulate how the GetDate() function will transform the data in mock_data.xml.'*

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

To get started immediately, you can copy the physical bootstrap templates we've created for you into your repository.

- [The Global Router](./templates/opentext_exstream/copilot-instructions.md)
- [The Domain Constraint](./templates/opentext_exstream/branding_standards.md)
- [The Function Registry](./templates/opentext_exstream/formula_registry.md)
- [The Token Registry](./templates/opentext_exstream/token_registry.md)
- [The Logic Audit Trail](./templates/opentext_exstream/logic_audit.csv)
- [The Mock Bootstrap](./templates/opentext_exstream/mock_bootstrap.java)
