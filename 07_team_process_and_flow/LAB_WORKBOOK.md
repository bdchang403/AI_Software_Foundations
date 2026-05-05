# Agile Leader Lab Workbook: The Metrics Audit

As an Agile Leader (Scrum Master, Coach, or Engineering Manager), your "Code" is the **Process**. In this lab, you will learn how to audit the factory's output to identify where context is breaking.

---

## Lab 1: Identifying the "Hallucination Loop" (Module 1)

**The Scenario:**
Team Beta's DORA dashboard shows a 48-hour **Lead Time for Changes** for a simple "Update Logo" task. The builder reports they are "fighting the AI."

### Your Task
Investigate the **Context Hand-off**. 
1. Open the [Semantic Blueprint Template](../templates_and_resources/stories/context_enriched_story_template.md).
2. Look at the "Forbidden Domains" section. If it's empty, why is the AI struggling?

**Answer Key:**
If the "Forbidden Domains" or "Semantic Mapping" is empty, the AI is scanning the entire 500k LOC repo to find where the logo is stored. It is likely finding 50 different logo files and guessing which one to update. 
**The Intervention:** Coach the Requirements Lead to explicitly map the `logo_asset` to the specific path `src/assets/branding/`.

---

## Lab 2: Detecting "Ghost Productivity" (Module 2)

**The Scenario:**
A builder submits a PR that was 100% AI-generated. It contains 1,200 lines of code. The task was "Add a login button."

### Your Task
Perform a **Context Audit** on the PR.
1. Does the PR include an **AI Trailer** (`AI-Generated-By`)?
2. Does the code include a new `OAuth` library that wasn't approved in the **ADRs**?

**Answer Key:**
If the AI introduced a new library, the **Master Router** or **ADR** context was missing from the prompt.
**The Intervention:** Ensure the builder is using the `copilot-instructions.md` which links to the global `ADR` folder.

---

## Lab 3: Comparative ROI Analysis (Module 3)

**The Scenario:**
Management wants to know if the "Context Factory" is actually saving money.

### Your Task
Calculate the **Token Savings**.
- **Scenario A (No Factory):** AI reads 500,000 lines of code. Cost: ~$15.00 per prompt.
- **Scenario B (Factory):** AI reads 1 Router + 1 ADR + 1 Story + 1 Target File. Cost: ~$0.05 per prompt.

**Coaching Action:**
Present this 300x cost reduction to the stakeholders to justify the time spent writing Semantic Blueprints.

---

## 🏁 The Finish Line

Congratulations! You have successfully audited the factory and identified a context-related bottleneck.

[**Proceed to Phase 4: Agent Orchestration & Assembly →**](../09_ai_agent_orchestration/01_anatomy_of_an_agent.md)
