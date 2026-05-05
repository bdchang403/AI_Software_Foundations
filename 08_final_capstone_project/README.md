# Capstone: Building Your First Autonomous Agent

This module is the final synthesis of the **Context Factory**. Here, we move from theoretical "role-based handoffs" to the physical assembly of an autonomous AI agent. 

An agent is more than just a chatbot; it is a software component that uses **Instructions**, **Context**, and **Tools** to achieve a goal. In the Context Factory, every role contributes a layer to the agent's configuration.

---

## 1. The Assembly Line: How Roles Build an Agent

Building an agent is an assembly process where each role "programs" a different part of the agent's brain:

| Agent Component | Role Responsible | Context Factory Artifact |
| :--- | :--- | :--- |
| **Identity & Goal** | Strategy Lead | **Epic Strategic Intent** |
| **Logic & Constraints** | Requirements Lead | **3-Part Directive & context-enriched story** |
| **The "Hands" (Tools)** | Builder | **Function Registry (OpenAPI/MCP)** |
| **Boundary Protection** | Validation Lead | **Adversarial Edge Cases** |
| **Regulatory Guardrails** | Security Lead | **Article VI/VII Sign-Off** |
| **Activation & Audit** | BuilderOps / Release Eng | **GitHub Agent YAML / AI-SBOM** |

---

## 2. Bridging the Prior Learning

### From Requirements Lead Directives to Agent Instructions
The **3-Part Directive** (Role, Task, Format) you learned in the Requirements Lead module becomes the `system_instructions` for the agent. When you create an agent in **Gemini Studio** or a `.github/agents/` file, you are literally pasting the Requirements Lead's work into the configuration.

### From ADRs to Agent Memory (RAG)
Agents suffer from "knowledge gaps" about your specific codebase. By establishing **Architecture Decision Records (ADRs)** and **Context Routers**, you are building the "Knowledge Base" that the agent queries via RAG (Retrieval-Augmented Generation). 

### From Function Registries to Agent Tools
An agent cannot "do" anything without tools. The **Function Registry** schemas built by Builders are converted into **OpenAPI Specifications**. These specs are then "mounted" to the agent, allowing Gemini to physically call your backend services to execute the code.

---

## 3. Practical Example: The Adversarial QA Agent

To see this in action, review the [Adversarial QA Agent Example](./examples/.github/agents/adversarial-qa.yaml).

This agent is designed to:
1.  **Trigger** when a new Pull Request is opened.
2.  **Read** the corresponding User Story from the repository.
3.  **Analyze** the builder's code for hallucinations or logic drift.
4.  **Execute** adversarial test cases to try and "break" the PR.

## 4. Next Steps: Deploying Your Agent
Now that you understand how to assemble the pieces, proceed to the final Hands-On Lab.

---
[**Final Lab: Assembling the Autonomous Agent →**](./LAB_WORKBOOK.md)
