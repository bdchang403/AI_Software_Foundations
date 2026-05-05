# Module 4: Extreme Context Engineering (The Semantic Contract)

## 🧠 Theory: You are Writing the AI's "Search Algorithm"

As a Requirements Lead in the Context Factory, your most important output is the **Semantic Mapping**. 

In an enterprise repository with 500k LOC, an AI doesn't "know" what a "User Profile" is. It only knows what `src/data/models/user.ts` is. If you use the wrong word, the AI will search for `profile_service` instead of `user_service`, find nothing, and hallucinate a new service.

**You are the bridge between Human Language and Machine Routing.**

---

## 🏗️ 1. The Explicit Semantic Map

In your [Context-Enriched Story Template](../templates_and_resources/stories/context_enriched_story_template.md), the **Semantic Blueprint** table is a literal mapping file for the AI's Retrieval system.

### How it influences the AI:
| Your Input (Business Term) | The AI's Action (Downstream) |
| :--- | :--- |
| **"Calculate Tax"** | The AI performs a vector search *only* in the specified `src/tax/` folder. |
| **"User Account"** | The AI ignores `legacy/accounts` and focuses on `services/auth/`. |
| **"Refund Logic"** | The AI reads the specific ADR you linked to ensure it doesn't break the finance laws. |

**The Result:** You have effectively "Locked" the AI into the correct architectural folder. It is no longer guessing; it is following your map.

---

## 🧱 2. Hardcoding Logic as "Booleans"

AI models struggle with "soft" or "ambiguous" requirements. Your job is to translate human requests into **Boolean Constraints** (True/False).

*   **Soft Requirement (Bad):** *"The report should be generated quickly and look professional."*
*   **Boolean Constraint (Good):** *"The report MUST be generated in PDF format. The file size MUST NOT exceed 5MB. The generation MUST happen in the `BackgroundWorker` to prevent blocking the main UI thread."*

By using words like **MUST**, **MUST NOT**, and **ONLY**, you are creating a "Logic Cage" that the AI cannot escape.

---

## 🧭 3. Best Practices for Writing Semantic Blueprints

To ensure your blueprints act as perfect Context Bounds, follow these rules:

1. **Be Hyper-Specific with Paths:** Never say "Update the UI." Say "Update `src/components/Checkout.tsx`." If you don't know the path, ask a Builder to help you define the boundary.
2. **Outlaw the Dangerous Paths:** Explicitly tell the AI what it is *not* allowed to touch. (e.g., `[BOOLEAN: FALSE] Modifying database schema files`).
3. **Sequence Matters:** If an action must happen before another (e.g., "Reserve inventory BEFORE charging card"), write that sequence into the Boolean Acceptance Criteria.
4. **Define the Fallback:** What happens if an API is down? An AI will often hallucinate a mock API if it gets stuck. Write a strict failure contract (e.g., "If API times out, return HTTP 503. DO NOT mock data").

> **View Full Production Examples here:** [Semantic Blueprint Examples](./examples/semantic_blueprint_example.md)

---

## 🛠️ Exercise: Building the Production Blueprint

**Your Action:**
Open the [Context-Enriched Story Template](../templates_and_resources/stories/context_enriched_story_template.md).

**Scenario:** We are building a "Delete My Account" button.
1.  **Map the Term:** Link "Delete Account" to the `src/services/pii_remover/` folder.
2.  **Define the Logic:** Use "Boolean" language to ensure the user is logged in before the action occurs.
3.  **Link the Knowledge:** Reference the "Internal GDPR Documentation" so the AI understands the legal stakes.

---

### 🎓 Final Step: Practical Application
Congratulations! You have completed the theory modules. Now it's time to put these concepts into practice.

[**Go to Lab Workbook: Semantic Blueprints & Directives →**](./LAB_WORKBOOK.md)
