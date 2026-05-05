# Master Skills Template Hub

This directory contains the "Cognitive Scaffolding" for your AI Agents. These templates ensure that regardless of the IDE or LLM used (Copilot, Cursor, Claude Code), the agent adheres to the **Context Factory** standards.

## 📂 Included Templates

### 1. 2-Tier Precision Routing (The Brain)
- [**Master Router**](./master_router.md): The primary entry point.
- [**Domain Contexts**](./context/): Sub-files for domain-specific rules (e.g., Billing, Auth).
- [**Story Templates**](./stories/): Context-enriched story templates and the **Semantic Blueprint Gallery**.
- [**Functions Registry**](./functions_registry.md): Defines available agentic tools.

### 2. Platform Scaffolding
- [**Platforms Hub**](./platforms/): Includes tailored rules for Copilot, Cursor, and Claude Code.
- [**Agent Examples**](./agents/): Real-world configurations for GitHub Agents, Antigravity, Codex (OpenAI), and Claude Code.
- [**Skills Hub**](./skills/): Defines specific personas (Coder, Reviewer, Auditor).

### 3. Auditability (The AI Trailer)
Every template now includes mandatory **AI Trailers** for commit messages and PR reviews. This ensures that AI-assisted changes are distinguishable from human-only changes in the audit log.

---

## 🛠️ Usage
1. Copy the relevant template to your repository's configuration directory.
2. Replace the `[BRACKETED]` placeholders with your specific project details.
3. Update the **Master Router** whenever new microservices or architectural domains are added.
