# Bridge Module 4: Context Mapping Matrix

To ensure an agent is successful, it must have access to the **right context** at the **right time**. This is called **Context Mapping**.

## The Context Mapping Model

Not all files are equal. When building an agent, you must map your repository folders to specific "Context Tiers."

| Tier | Content Type | Agent Access Rule |
| :--- | :--- | :--- |
| **Tier 1 (Global)** | `.github/copilot-instructions.md`, `00_CONSTITUTION.md` | **Traffic Controller.** Always loaded. Directs the agent to the domain. |
| **Tier 2 (Surgical)** | `docs/context/billing.md`, `docs/stories/FEAT-101.md` | **The Payload.** Loaded on-demand. Contains all ADRs and specific task logic. |

## Practical Mapping Exercise

**Scenario:** You are building an agent to "Update the Login Page CSS."

**Your Action:**
1.  **Instructions (Identity):** Which 3-Part Directive do you use?
2.  **Context (Knowledge):** Which folders in the repo should the agent be allowed to "see"? (e.g., `src/ui/`, `public/assets/`).
3.  **Tools (Hands):** Does this agent need the "Database Write" tool? (Answer: No, it only needs the "File Edit" tool).

---

### 🎓 Bridge Complete
You have successfully bridged the gap between role-based theory and autonomous execution. You now understand how the pieces fit together.

[**Final Phase: The Capstone - Building Your Agent →**](../08_final_capstone_project/README.md)
