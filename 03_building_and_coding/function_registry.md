# Production Implementation: Function Registry Schemas

This file is a literal representation of how you map your 500k LOC enterprise codebase into a Model Context Protocol (MCP) or OpenAI Tool Calling schema array. 

**DO NOT give AI Agents raw read/write access to your entire repository.** Provide them with strict, abstract tools defined by these schemas. 

> [!TIP]
> **More Than Just Allowed Tools:** A Function Registry is not just a restrictive contract that defines what an AI *can* execute. It is also a critical architectural knowledge graph. It helps the AI understand what existing functions do, and explicitly maps out their **upstream and downstream dependencies**. By querying the registry, the AI can safely orient itself within complex integrations without needing to randomly read thousands of lines of code.
## 1. Codebase Routing Tool (The "Eyes" of the Agent)

When an AI needs to understand context, it must explicitly call this tool. Handing the AI this tool prevents it from silently guessing logic.

```json
{
  "name": "read_domain_context",
  "description": "Reads the localized files for a specific domain mapped in the Semantic Blueprint. Use this before writing any code to understand the existing contracts.",
  "parameters": {
    "type": "object",
    "properties": {
      "semantic_component": {
        "type": "string",
        "description": "The exact component name provided by the Requirements Lead (e.g., 'src/services/billing')"
      },
      "max_lines": {
        "type": "integer",
        "description": "Limit the readout to prevent token exhaustion. Max 500.",
        "default": 300
      }
    },
    "required": ["semantic_component"]
  }
}
```

## 2. Contract Action Tool (The Exposer)

When a builder creates a shared service (like Auditing or Telemetry), they must register its execution schema here. When the AI agent needs to log something or call an API, it calls this schema to understand the TypeScript interface, **as well as any upstream or downstream dependencies** (e.g., "Calling StripePayment requires upstream Auth validation"). This saves thousands of tokens that would otherwise be wasted `grep`ing the file system.

```json
{
  "name": "get_contract_schema_and_dependencies",
  "description": "Retrieves the TypeScript interface, JSON schema, and dependency map for internal microservice communications.",
  "parameters": {
    "type": "object",
    "properties": {
      "domain_intent": {
        "type": "string",
        "enum": ["AuditLogging", "StripePayment", "UserAuthentication", "EmailDispatch"],
        "description": "The semantic action the code intends to perform."
      },
      "include_dependencies": {
        "type": "boolean",
        "description": "If true, returns the upstream services required to call this function, and the downstream services this function impacts.",
        "default": true
      }
    },
    "required": ["domain_intent"]
  }
}
```

## How to use this Registry in Code
In your orchestration layer (e.g., LangChain, AutoGen, or custom Node.js execution wrapper):

```javascript
// Example Node.js Orchestrator extracting the Registry
const fs = require('fs');
const registryTools = JSON.parse(fs.readFileSync('./function_registry.json'));

const response = await openai.chat.completions.create({
  model: "gpt-4-turbo",
  messages: [
    {"role": "system", "content": "You are scoped by the active Semantic Blueprint."},
    {"role": "user", "content": "Implement the Story-112 Requirements."}
  ],
  tools: registryTools, 
  tool_choice: "auto" // The AI will automatically route itself based on the schemas above!
});
```
