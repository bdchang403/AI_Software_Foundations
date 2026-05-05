# Module 2: Adversarial Thinking & Permissions

## Theory: The Agent Escaping the Sandbox
BuilderOps and Deployment Leading is about security and permissions. If you build an autonomous CI/CD pipeline that allows an AI Agent to provision infrastructure or fix bugs, you have created a severe security vector.

Red-teaming in BuilderOps means explicitly assuming the AI Agent is malicious or compromised.

## Verbose Example
**Adversarial Thought:** "If I give the AI an AWS IAM role that has `AdministratorAccess` because it's 'easy', the AI could hallucinate a script that deletes our production RDS database."

**The Red-Team Patch:**
* Do not rely solely on prompt-based constraints (e.g., telling the AI "Do not delete the DB").
* The patch must be **Structural**. Your CI/CD pipelines must run the agent with an IAM Role that explicitly `Denies` destructive actions.

## Exercise: Constrain the Automation

**Scenario:** You have a Github Action where an AI Agent automatically reviews Pull Requests and suggests code fixes.

**Your Action:**
Write down two structural (pipeline or IAM-level) constraints to prevent the AI from approving its own malicious code.
1. **Structural Constraint 1:** [e.g., Mandatory human review before merge for code authored by `-bot`]
2. **Structural Constraint 2:** [e.g., Disabling the `git push` capability on the runner token]

---
[**Next Module: Pipeline Decomposition →**](./03_decomposition.md)
