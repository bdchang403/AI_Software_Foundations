# Team Analysis & Baseline Metrics: The Day Zero Prerequisite

Before any team members begin their Role-Based AI Training or start utilizing the Context Factory workflows, the organization **must** perform a dual-track assessment:
1.  **Behavioral Analysis:** How are teams *actually* using AI today? (Usage Discovery)
2.  **Engineering Metrics:** What is the current performance baseline? (DORA/SPACE)

Without this assessment, you cannot mathematically prove that AI-assisted Context Engineering is actually reducing friction. It becomes purely anecdotal.

## I. Team AI Usage Discovery (The Behavioral Audit)

You must understand the "As-Is" state of your team's AI interaction before applying the Context Factory's "To-Be" engineering discipline.

### 1. The Tooling Audit (Identifying Shadow AI)
*   **Approved vs. Unapproved:** Survey teams to find the delta between company-provided tools (e.g., GitHub Copilot Enterprise) and "Shadow AI" (personal Claude, ChatGPT, or local LLM instances).
*   **Tooling Fragmentation:** Identify if different squads are using different IDEs (Cursor vs. VS Code), as this dictates which **Context Routing** templates (e.g., `.cursorrules` vs. `clauderules.md`) they will need.

### 2. Interaction Maturity Assessment
Analyze a random sample of 50 recent AI interactions (from chat logs or PR descriptions) to categorize team maturity:
*   **The "Magic Wand" Pattern (Low Maturity):** One-liner prompts like *"Fix this bug"* or *"Implement the billing logic."* (High hallucination risk).
*   **The "Monolithic Dump" (Medium Maturity):** Pasting thousands of lines of code into a chat window to "give context." (High token waste/Attention Dilution).
*   **The "Context Factory" (High Maturity):** Referencing specific ADRs, using 3-Part Directives, and utilizing surgical pathing.

### 3. Friction Point Identification
Interview Senior Builders to identify the "AI-Cliff":
*   At what file count or LOC (Lines of Code) threshold does the team stop using AI because it "gets lost" or "breaks the build"?
*   Identifying this threshold allows you to target the **Decomposition** and **Routing** modules where they are needed most.

---

## II. DORA & SPACE Metrics Extraction (The Performance Baseline)

We rely on extracting standard Agile metrics natively from the GitHub API. Your BuilderOps team should run these queries to capture the baseline.

### 1. DORA: Lead Time for Changes
**Why measure it?** We hypothesize that strictly bounding context using Semantic Blueprints will allow builders to write code exponentially faster. We need to prove this.
**How to measure (GitHub API):**
* **First Commit to Merge:** Calculate the time delta between the earliest commit timestamp on a PR branch and the PR's merged timestamp.
* **Merge to Deploy:** Calculate the time delta between a PR merge timestamp and the timestamp of the successful deployment workflow run on the `main` branch.

### 2. DORA: Change Failure Rate (CFR)
**Why measure it?** AI is notoriously confident when hallucinating. We hypothesize that our Red-Teaming modules (Adversarial Thinking) will prevent AI hallucination from making it to production, keeping CFR stable.
**How to measure:**
* Track the ratio of incident/bug tickets (e.g., Jira issues tagged `Bug` linked to GitHub PRs) against the total number of successful deployments.

### 3. SPACE: Review Cognitive Load
**Why measure it?** If the Builder prompts are constrained perfectly by ADRs and Registries, human reviewers won't need to leave as many comments correcting architectural mistakes.
**How to measure:**
* **Avg Review Comments per PR:** Track the sheer volume of review comments. A steep drop post-AI implementation signifies that the Context Factory is aligning AI outputs with human expectations perfectly.
* **PR Size Ratio:** Track if PRs are staying consistently small (< 200 lines). The "Decomposition" training module should enforce this.

### 4. SPACE: AI Adoption Proxies
**Why measure it?** To understand where the AI is physically assisting.
**How to measure:**
* **Test Code Ratio:** Calculate the percentage of PR line additions occurring within `test` or `spec` files. If Validation Leads are using the training effectively, this ratio should skew heavily upward as AI generates massive test suites.

---

> [!IMPORTANT]  
> **Action Required:** Export these metrics for the previous 90 days into a dashboard. Once completed, teams may begin the training modules.

---

[**Return to Root README →**](./README.md)
