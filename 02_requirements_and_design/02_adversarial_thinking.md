# Module 2: Adversarial Thinking & Red-Teaming for Requirements Leads

## Theory: Terminology Hallucinations
You receive an Epic that says "Customer Checkout." To you, a human, "Customer" means a verified user. 
To an AI, "Customer" might mean generating a new `Customer` database table when you already have a `UserAccount` infrastructure. 

Red-Teaming for a Requirements Lead means identifying **Implicit Knowledge** and making it **Explicit**. If a term can be misunderstood by a neural network trained on millions of generic GitHub repos, you must patch it.

## Verbose Example
**The Epic Blueprint says:** "Send an email receipt."

**Adversarial Thought:** "If I write 'send an email receipt' into the user story, the Builder's AI agent might install `nodemailer` or configure AWS SES directly in the checkout service. We already have a centralized `NotificationService`. I need to close this loophole."

**The Red-Team Patch:** "Constraint: Do not implement raw email protocols. You must emit an `OrderCompleted` event to the `NotificationService` bus. The Notification system handles the email."

## Exercise: Finding the Terminology Threat

**Scenario:** The Strategy Lead gave you an Epic to "Allow managers to export spreadsheets of employee hours."

**Your Action:** 
Identify two ways an AI Builder agent could catastrophically misinterpret that request, and write the patch constraint for the User Story.

1. **Adversarial Loopholes:** [Think about database queries, formatting engines, etc.]
2. **Your Explicit Patch:** [Write the explicit constraint closing the loophole]

---
[**Next Module: Feature-Level Decomposition →**](./03_decomposition.md)
