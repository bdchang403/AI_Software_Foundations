# Module 1: Auditing the 3-Part Directive (Governance at the Root)

## 🧠 Theory: You are the Constitutional Guardrail

In a traditional organization, auditors are "Downstream"—they check for mistakes after the code is in production. In the **Context Factory**, you are "Upstream." You audit the **Semantic Contract** *before* a single line of code is written.

By auditing the **3-Part Directive**, you prevent **Algorithmic Poisoning**. If a requirement is biased at the root, the AI will generate biased code with 100% efficiency.

---

## 🏗️ 1. Identifying "Proxy Variable" Risks

AI is an expert at finding patterns. If you tell an AI to optimize for "Profitability" without constraints, it may discover that certain zip codes or demographics are less profitable and start discriminating against them automatically.

### Your Audit Protocol:
When reviewing a Requirements Lead's directive, look for:
- **Proxy Variables:** Are they using data points (like Zip Code, Age, or Gender) that could act as a proxy for protected classes?
- **Opaque Logic:** Is the requirement "Give the AI freedom to decide"? (This is a violation of Article VII: Reproducibility).
- **Implicit Bias:** Does the "Strategic Why" of the story conflict with the **Enterprise Constitution**?

---

## 🏗️ 2. The Audited Directive (Case Study)

### ❌ The Poisoned Directive (Constitutional Violation):
*   **Task:** "Create a credit scoring algorithm."
*   **Constraint:** "Analyze the user's social media followers and recent purchases to determine creditworthiness."
*   **Risk:** Violates Article VI (Fairness) and GDPR (Data Minimization).

### ✅ The Audited Directive:
*   **Task:** "Create a credit scoring algorithm."
*   **Constraint:** "Use only verified financial data (Income, Debt-to-Equity, Credit History). All calculations MUST be logged with the specific mathematical weight used for each variable."
*   **Auditor's Note:** This ensures the final code is **Transparent** and **Deterministic**.

---

## 🛠️ Exercise: Spot the Strategic Risk

**Scenario:** A Requirements Lead submits a directive: *"Optimize the delivery routes. Prioritize deliveries in high-income neighborhoods to reduce the risk of package theft."*

**Your Action:** 
1.  Explain which Article of the **Enterprise Constitution** this violates.
2.  Rewrite the constraint to optimize for "Security" without using "Income" as a proxy.

---

[**Next Module: Regulatory Red-Teaming →**](./02_regulatory_red_teaming.md)
