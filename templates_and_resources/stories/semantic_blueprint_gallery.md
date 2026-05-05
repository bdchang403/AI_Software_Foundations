# Semantic Blueprint Gallery: Downstream Influence Examples

This gallery shows how a Requirements Lead's "Semantic Blueprint" physically controls the behavior of AI-assisted tools like GitHub Copilot, Cursor, and Claude Code.

---

## Example 1: The "Legacy Lockdown" Blueprint
**Scenario:** You are modifying a 10-year-old service. If the AI sees the legacy code, it will copy the old patterns instead of using the new V2 services.

| Business Term | Technical Route | AI Constraint |
| :--- | :--- | :--- |
| `Calculate Interest` | `src/services/v2/interest/` | `DO NOT read any files in src/legacy/legacy_interest/`. Use the `InterestCalculatorV2` interface exclusively.` |

### 🌊 Downstream Influence:
- **Copilot/Cursor**: When the builder types "calculate interest", the RAG system is explicitly told to *exclude* legacy files. The AI suggests `V2` patterns instead of technical debt.
- **Result**: 0% hallucination of deprecated methods.

---

## Example 2: The "Contract-First" Validation
**Scenario:** You need to ensure the AI uses the centralized `NotificationService` instead of installing its own library.

| Business Term | Technical Route | AI Constraint |
| :--- | :--- | :--- |
| `Notify User` | `src/shared/notifications/` | `MUST use the 'dispatch' method of NotificationService. Do NOT install 'nodemailer' or external packages.` |

### 🌊 Downstream Influence:
- **Claude Code**: During an agentic execution loop, Claude checks the blueprint. It sees the negative constraint (`Do NOT install`). If it attempts to run `npm install`, the internal audit check (Phase 5) will flag a **Constitutional Violation**.
- **Result**: Maintains architectural purity across the 500k LOC codebase.

---

## Example 3: The "PII Privacy" Barrier
**Scenario:** Handling sensitive user data in a regulated environment.

| Business Term | Technical Route | AI Constraint |
| :--- | :--- | :--- |
| `User Profile` | `src/data/models/` | `All logs MUST be anonymized. Mask all emails and phone numbers before console output.` |

### 🌊 Downstream Influence:
- **Validation Lead Testing**: The Validation Lead's agent reads this blueprint and automatically generates **Adversarial Tests** that try to force the code to log an email.
- **Result**: Automated privacy compliance at the story level.
