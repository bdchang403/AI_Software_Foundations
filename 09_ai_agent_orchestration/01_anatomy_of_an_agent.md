# Bridge Module 1: Anatomy of an Agent

To bridge the gap between "writing prompts" and "deploying agents," you must understand that an agent is a **Stateful Configuration** of the artifacts you created in Phase 2.

## 🏗️ The Agent Definition Blueprint (GitHub Pattern)

While your **Code Repository** holds the logic, the **.github/agents/** directory holds the orchestration. Below is how an enterprise agent is typically defined within a GitHub-centric workflow.

```text
your-repo/
├── ⚙️ .github/
│   ├── ⚡ copilot-instructions.md    <-- The Router (Tier 1)
│   └── 🤖 agents/                    <-- THE ORCHESTRATION HUB
│       ├── billing-agent.agent.md    <-- THE MANIFEST (Soul + Hands + Memory)
│       └── research-agent.agent.md
├── 📘 docs/
│   ├── 🗺️ context/                   <-- Tier 2 (The Memory)
│   │   └── billing.md                <-- Domain context + ADRs
│   └── 🛠️ registries/                 <-- The Hands (Tool Definitions)
└── 🏗️ src/
    └── [your code]
```

---

## The 3 Pillars of an Agent

An agent is composed of three "buckets" of data. If any bucket is empty or poorly defined, the agent will fail.

### 1. Identity & Instructions (The "Soul")
*   **Source:** The Requirements Lead's **3-Part Directive**.
*   **Mechanism:** This is the `System Prompt`. It defines the agent's personality, its task, and its constraints. 
*   **Example:** "You are a Billing Specialist. Your task is to calculate VAT. You MUST use the existing `TaxRate` registry."

### 2. Knowledge & Context (The "Memory")
*   **Source:** The Builder's **ADRs** and the Requirements Lead's **Semantic Blueprints**.
*   **Mechanism:** Retrieval-Augmented Generation (RAG). The agent is given access to a search tool (like `grep` or a Vector DB) that allows it to "read" the codebase.
*   **Example:** Mapping the agent to the `src/billing/` folder so it can find the code it needs to modify.

### 3. Tools & Skills (The "Hands")
*   **Source:** The Builder's **Function Registry**.
*   **Mechanism:** Function Calling (JSON Schemas). The agent doesn't just write text; it emits a command that your server executes.
*   **Example:** `{"name": "apply_discount", "args": {"amount": 10}}`.

---

[**Next: The Assembly Mechanism →**](./02_the_assembly_mechanism.md)
