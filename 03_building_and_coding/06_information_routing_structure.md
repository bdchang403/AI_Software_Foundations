# Implementation: The 2-Tier Precision Routing Architecture

To prevent token exhaustion and ensure an AI Agent (like **Gemini 3.1**, **GPT-5.5**, or **Claude 4.7**) can reliably traverse your repository, builders must implement a **2-Tier Precision Routing Architecture**. 

Instead of putting all context into one massive prompt, we use a "Flat + 1" model that ensures the AI only sees what is relevant to the current domain.

## 🏗️ The Context Factory Repository Blueprint (GitHub Copilot Example)

To an AI Agent, your repository is a **Context Map**. We use a 2-tier structure to maximize attention precision.

```text
your-repo/
├── ⚙️ .github/
│   └── ⚡ copilot-instructions.md      <-- Tier 1: The Global Router (~50 lines)
├── 📘 docs/
│   ├── 🗺️ context/                   <-- Tier 2: Surgical Payload (Direct Injection)
│   │   ├── billing.md                <-- Domain Context (boundaries + ADRs)
│   │   └── security.md
│   ├── 🛠️ registries/
│   │   ├── function-registry.md       <-- The Hands (Tool Definitions)
│   │   └── field-definitions.md
│   └── 🧠 stories/                    <-- Active context-enriched stories
│       └── FEAT-101-loyalty.md
└── 🏗️ src/
    └── [your code]
```

> [!NOTE]
> The example above uses the `.github/` folder pattern for GitHub Copilot. If you are using **Antigravity**, **Cursor**, or **Claude Code**, please refer to the [Tool-Specific Entry Points](#-tool-specific-entry-points-tier-1) section below for the correct Tier 1 file path.

---

## ❓ How does the AI find the correct context across the repository?

The AI doesn't "hunt" for them randomly. It finds them because the **Tier 1 Router** (`.github/copilot-instructions.md`) contains **Hardcoded Pointers**. 

### Example: The GPS Logic in `.github/copilot-instructions.md`
```markdown
# Global Instructions
1. ALWAYS read `docs/context-map.md` to understand the domain boundaries.
2. If working on CSV logic, read `docs/skills/csv-processing.md`.
3. If touch any API, check `docs/registries/function-registry.md` for allowed endpoints.
```

By providing the **literal path**, you eliminate the AI's need to "scan" or "search." It traverses the repository like a GPS follows a map.

---

## 🧭 The Token Economy: Why tier the folders?

A common question is: *"Why not just put all instructions in the root?"*

If you put all your architectural rules, story requirements, and tool definitions into the root `.github/copilot-instructions.md`, **every single interaction** with the AI (even a simple comment) will consume your entire token window. This leads to:
1. **High Costs:** You pay for the same 20,000 words over and over.
2. **Hallucinations:** The AI gets "distracted" by irrelevant rules from other domains.

### The Solution: 2-Tier Precision Routing
*   **Tier 1: The Global Router (`.github/`):** Contains ONLY the high-level directions (e.g., "If working in billing, load the billing context"). This is the "Traffic Controller" that keeps the prompt small, fast, and cheap.
*   **Tier 2: The Domain Context (`docs/context/`):** Contains the specific logic, architectural truth (ADRs), and active story requirements for that domain. This is the "Surgical Payload" that the AI reads **on demand**.

---

## 🏛️ The 3 Pillars of a Traceable Repo

| Pillar | Industrial Name | Common Tool Paths | Why it's Required |
| :--- | :--- | :--- | :--- |
| **Tier 1** | The Global Router | `.github/copilot-instructions.md` | The "Entry Point" that directs the AI to the correct domain. |
| **Tier 2** | Domain Knowledge | `docs/context/*.md` | The high-level map of domain boundaries and ADRs. |
| **Tier 2** | Active Story | `docs/stories/*.md` | The specific task requirements and edge cases. |
| **Tier 2** | The "Hands" | `docs/registries/tools.json` | Defines the allowed MCP/Function tools for the agent. |

---

## 🛠️ Tool-Specific Entry Points (Tier 1)

While the **2-Tier Logic** is universal, the physical filename for Tier 1 depends on the AI agent you are using. The "Auto-Loader" is simply the file that your IDE or Agent is configured to read by default as its **System Prompt**.

*   **GitHub Copilot:** Uses `.github/copilot-instructions.md`.
*   **Cursor:** Uses `.cursorrules` in the root.
*   **Claude Code:** Often uses a `.clauderc` or a project-level system prompt configuration.
*   **Antigravity:** Uses `.antigravity/instructions.md` (or your specific agent configuration path).

Regardless of the name, **Tier 1 must always remain a "Thin Router"** that points the AI to the deeper truth in your `docs/` folder.


---

## Tier 1: The Global Router (`.github/copilot-instructions.md`)
**Purpose:** Global repository rules and a directory map.
**Mechanism:** This file automatically loads whenever the AI is invoked. It acts as a **traffic controller**, telling the AI *where* to find the deep context for specific domains.

```markdown
# Global Copilot Instructions

You are an expert Enterprise TypeScript Builder. 
Before answering queries, you MUST load the Tier 2 Domain Context based on your current path.

## Domain Routing
*   `src/billing/**` -> Load `docs/context/billing.md`
*   `src/auth/**` -> Load `docs/context/auth.md`

## Global Constraints
*   Do not use `console.log`. Use `import { logger } from '@core/telemetry'`.
```

---

## Tier 2: The Domain Context (`docs/context/billing.md`)
**Purpose:** The "Surgical Payload" containing architectural truth and active task requirements.
**Mechanism:** This file is a single source of truth for the domain. It consolidates the ADRs and points the AI to the active story.

```markdown
# Billing Domain Context

## 🏛️ Architectural Truth (ADRs)
Before modifying any currency logic, you must strictly adhere to:
👉 **[ADR-042: Multi-Currency Precision Standard](../adr/042-multi-currency-precision.md)**

*Summary:* Always use `Big.js` and integer cents (USD).

## 📋 Active Story Context
*   **Current Task:** [FEAT-88: Currency Localization]
*   **Path:** `docs/stories/FEAT-88-currency.md`
```

---

## How It Comes Together in the IDE

When a builder asks the AI:
> *"Update the refund service to support JPY."*

**The 1-Hop Chain:**
1.  **Tier 1:** The AI reads the Global Router and sees it is in the `billing` domain.
2.  **Tier 2:** It loads `billing.md`, which immediately provides the **ADR-042** rules and points it to the **FEAT-88** edge cases.
3.  **Result:** The AI has 100% of the required context in a single ingestion event, minimizing hallucinations and token waste.

---

### 🎓 Final Step: Practical Application
Congratulations! You have completed the theory modules for the Builder Path. You now understand how to parameterize an AI agent, chain its context, and route it through a complex repository.

Now it's time to put these concepts into practice.

[**Go to Lab Workbook: Registries, Chaining, & Routing →**](./LAB_WORKBOOK.md)
