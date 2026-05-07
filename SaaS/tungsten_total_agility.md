# SaaS Context Factory: Tungsten Total Agility (TTA)

## 🎯 The Industrial Objective
Automating Business Process Management (BPM) by treating TTA Workflows and Forms as **Managed State Machines**.

---

## 📝 1. Requirements Gathering (Product Owner & Business Analyst)
The Context Factory starts with clear requirements *before* any engineering work begins. POs and BAs provide the crucial **Context-Enriched Stories**.
*   **Semantic Blueprints:** POs contribute by maintaining the high-level Business Process Maps (the desired workflow steps) directly in the `docs/stories/` folder, which GitHub Copilot will read.
*   **The 3-Part Directive:** BAs write user stories in GitHub Issues or Jira that explicitly define the **Goal**, **Context**, and **Constraint**.
*   **Semantic Constraints:** The BA's story must define the business constraint using semantic language, not technical file paths. Example: *"This new routing step must be added to the process defined in `SaaS/tta/process_map.md`."*

---

## 🏗️ 2. Context Extraction (Engineer Baseline)
Before GitHub Copilot can assist with the BA's story, the engineer must export the workflow definition so the AI can analyze the process steps.

### Step-by-Step Extraction:
### 🛡️ 2c. Managing "Split-Brain" Conflict (Anti-Drift)
Because TTA allows manual UI changes, your repository can become "stale."
1. **The Pull-Before-AI Rule:** Use the `PackageService` SDK or TTA Designer to export the latest **.zip package** of your process and compare the metadata XML against your `src/` directory.
2. **Conflict Resolution:** If a process map was changed in the UI, sync the repository baseline first to avoid overwriting production logic.

1. Open the **Tungsten Total Agility Designer** in your web browser.
2. Navigate to **System > Import/Export**.
3. Select **Export** and check the boxes for the **Processes** and **Forms** relevant to the user story.
4. Click Export. This downloads a ZIP package.
5. **Unzip** the package. Inside, you will find XML files that define the workflow and forms.
6. Copy these XML files into your repository at `src/tta/workflows/` and `src/tta/forms/`.
7. *For C# Scripts:* If your workflow uses .NET script nodes, copy the raw C# code into `src/tta/scripts/`.

---

## 🧭 3. Routing & Guardrails (Engineer Setup)
To make AI changes deterministic, you must build the **2-Tier Precision Routing** structure. This acts as an automated traffic controller so engineers don't have to manually prompt the AI with constraints.

### 3a. Tier 1: The Global Router (`.github/copilot-instructions.md`)
Create a file named `.github/copilot-instructions.md`. This acts as the "Traffic Controller" for the AI. You use this file to provide path-based pointers, so the AI knows exactly where to find its domain context without guessing.

Add the following path-based routing rules:

```markdown
# Global Routing Rules
* If asked to modify files in `src/tta/workflows/**`, you MUST read `SaaS/tta/process_map.md` before generating code.
* If asked to modify files in `src/tta/scripts/**`, you MUST read `SaaS/tta/sdk_rules.md` before generating code.
```

### 3b. Tier 2: Domain Constraints
Create **`SaaS/tta/process_map.md`**: Write down the literal steps of the workflow so the AI understands the sequence. Example: *"Node 1: Scan, Node 2: Document Classification, Node 3: Data Extraction, Node 4: Export to ERP."*

### 3c. Tier 2: "The Hands" (SDK Registries & IDE Setup)
When writing C# for TTA, you must use the proprietary TTA SDK (`Agility.Sdk.Model`). 

1. **IDE Setup:** Create a `/lib/kofax/` folder in your repo. Copy the SDK `.dll` files (e.g., `Agility.Sdk.Model.dll`) from your server into this folder. Add assembly references to your `.csproj`. *This allows Copilot to index the compiled SDK classes directly.*
2. **The Registry:** Create `SaaS/tta/sdk_rules.md` to force specific patterns:
   ```csharp
   # Tungsten SDK Constraints
   // To update a job variable in TTA, Copilot MUST use this exact pattern:
   var session = new SessionContext { SessionId = sessionId };
   var jobService = new JobService();
   jobService.UpdateJobVariable(session, jobId, new Variable { Id = "VarName", Value = "NewValue" });
   ```

---

## 💻 4. AI-Assisted Implementation (Copilot Workflow)
Because you set up the **2-Tier Precision Routing**, the engineer's prompt becomes incredibly simple. The system handles the context deterministically.

1. **Open IDE:** Open Visual Studio or VS Code.
2. **Open the Target File:** Open the TTA C# script you want to edit (e.g., `src/tta/scripts/ExtractionNode.cs`).
3. **Prompting Copilot Chat:**
   > *"@workspace I need to implement the BA's story linked here: [Story Link]. Please generate the code."*
4. **The Deterministic Automation:** 
   * **Tier 1 Triggers:** The AI reads the Global Router and sees you are working in the `src/tta/scripts/` directory.
   * **GPS Navigation:** Following the explicit pointers in the Global Router, the AI navigates directly to `sdk_rules.md` and `process_map.md` to learn the rules.
   * **Result:** Copilot reads the BA's story, cross-references the process map to avoid circular dependencies, uses the allowed SDK patterns, and parses the referenced `.dll` files to generate a syntactically perfect C# script.

---

## ⚖️ 5. Audit, Validation, & Deployment
Before deploying AI-generated workflow changes:
1. **State Conflict Check:** Ask Copilot to verify that the new node doesn't break any downstream data extraction rules defined in your SLA documentation.
2. **Deployment:** Import the AI-modified XML or C# scripts back into TTA using the **Import/Export** utility.
3. **Validation:** In TTA Designer, create a **Test Job** for your modified process and step through the "Job Viewer" to verify the token routes correctly.



---

## 🏷️ 6. Release & Version Correlation
To prevent version drift between GitHub and the SaaS environment, you MUST establish bi-directional correlation upon deployment:
1. **The Hash Injection:** When importing the configuration into the SaaS UI (or deploying via CLI), paste the GitHub Commit Hash into the SaaS tool's "Description" or "Release Notes" field. 
2. **The Git Tag:** In GitHub, tag the commit with the official SaaS release version (e.g., `git tag v2.4.1-[saas-name]`).

This ensures that if a production issue occurs, you can mathematically trace the live SaaS configuration back to the exact Git commit and AI prompt that generated it.

---

## 🛠️ 7. Local Simulation & Mocking
TTA logic is difficult to test without the live server. To speed up development, you must build **Mock/Simulation deals**:
1. **SDK Mocking:** Use Moq or NSubstitute in C# to mock the `JobService` and `VariableService`.
2. **Local Test Harness:** Create a `test/tta/ProcessSimulation.cs` that uses your mocks to verify business logic without connecting to the TTA server.

---

## 🚀 Appendix: Quick-Start Bootstrap Templates

To get started immediately, you can copy the physical bootstrap templates we've created for you into your repository.

- [The Global Router](./templates/tungsten_total_agility/copilot-instructions.md)
- [The Domain Constraint](./templates/tungsten_total_agility/process_map.md)
- [The Function Registry](./templates/tungsten_total_agility/sdk_rules.md)
- [The Token Registry](./templates/tungsten_total_agility/token_registry.md)
- [The Logic Audit Trail](./templates/tungsten_total_agility/logic_audit.csv)
- [The Mock Bootstrap](./templates/tungsten_total_agility/mock_bootstrap.cs)
