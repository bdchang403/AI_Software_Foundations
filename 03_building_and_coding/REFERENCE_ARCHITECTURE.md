# Builder Reference Architecture: The Context-First Repository

To succeed in the Context Factory, your repository must be organized for **Machine Readability**. This structure ensures that an AI Agent can find the "Strategic Guardrails" without you needing to paste them into the prompt.

## 📂 Standardized Folder Structure

```text
root/
├── .github/
│   ├── copilot-instructions.md    <-- Tier 1: The Global Router (Direct Pointers)
│   └── agents/                    <-- Agent configurations (YAML/JSON)
├── docs/
│   ├── context/                   <-- Tier 2: Surgical Payload (boundaries + ADRs)
│   │   ├── billing.md             <-- Domain Rules + Architectural Truth
│   │   └── security.md
│   └── stories/                   <-- Context-Enriched Stories (The Input)
│       └── LOYALTY-101.md
├── src/
│   ├── domain_a/                  <-- Bounded Contexts
│   │   ├── services/
│   │   └── registry.json          <-- Local Function Registry
│   └── shared/
└── tests/
    ├── adversarial/               <-- Validation Lead toxic prompts
    └── contracts/                 <-- AI-enforced interface tests
```

---

## 🛠️ The "Machine Entry Point" Pattern

Every repository MUST have a `.github/copilot-instructions.md` (or equivalent for your IDE). This file acts as the **Bootstrap Code** for the AI.

### Recommended Content for `.github/copilot-instructions.md`:
```markdown
# AI Bootstrapping Rules (Tier 1)
1. ALWAYS identify the domain of the files you are modifying.
2. If working in `src/billing/`, you MUST load `docs/context/billing.md` (Tier 2).
3. If working on security logic, you MUST load `docs/context/security.md` (Tier 2).
4. Adhere to all ADRs contained within the domain context.
5. Use the local `registry.json` for all external tool calls.
```

---

## 🧩 Local Function Registries

Instead of one giant registry, keep them close to the code.

**Example: `src/billing/registry.json`**
```json
{
  "domain": "Billing",
  "tools": [
    {
      "name": "calculate_tax",
      "description": "Calculates regional tax. Use this instead of hardcoding percentage logic.",
      "parameters": { ... }
    }
  ]
}
```

**Downstream Influence:** When the AI enters the `src/billing/` folder, it reads this local registry and realizes it is restricted to using the `calculate_tax` tool for all financial math.
