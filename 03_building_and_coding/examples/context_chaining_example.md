# Example: Context Chaining

Builders often think an AI agent is a "smart chatbot." It is not. It is a text-completion engine. You must chain rigid context together programmatically before asking it to write code.

## ❌ The BAD Example: Chatbot Prompting
**Builder Prompt:** 
> "Hey AI, build the login flow for Jira-123. Look at the database folder and figure out where the user table is, then write the endpoint and the tests."

### Why this fails:
1. The AI has to blindly guess what Jira-123 means.
2. It has to `grep` entire directories to find the database schema, wasting 50,000 tokens.
3. It has no architectural guardrails, so it uses Express.js even though your company uses Fastify.

---

## ✅ The GOOD Example: The Chained Payload
This is what your orchestration script (or your manual prompt) should *actually* look like when querying the LLM API.

**Final Assembled Payload (`messages[0].content`):**
```text
[SYSTEM PERSONA]
You are a Senior TypeScript Engineer. You operate exclusively in strict enforcement mode.

[SYSTEM: CAPABILITY OVERRIDE (Injected from skills.md)]
You are under the STRICT_COMStrategy LeadNENT_SCAFFOLDING directive.
1. You may not invent utilities.
2. You must output code via XML tags.
3. [CONSTITUTIONAL_CRITIQUE_PHASE] You must critique your code against the Enterprise Constitution before outputting.

[ARCHITECTURAL GUARDRAILS (Injected from adr_template.md)]
[ADR-012]: All backend routing MUST use Fastify. Express.js is strictly prohibited.

[THE CONTRACT (Injected from Requirements Lead's semantic_blueprint.md)]
Story: Create Login Flow.
Required Route: /src/auth/auth0_service.ts
Acceptance: Must route to Auth0ProviderTool. Do not process passwords locally.

[USER COMMAND]
Execute the contract above. Provide the file diff.
```

### Why this succeeds:
The AI has no room to hallucinate. It is bound by the rules of the framework (Fastify), the rules of the business (Auth0), and the rules of the payload wrapper (XML).
