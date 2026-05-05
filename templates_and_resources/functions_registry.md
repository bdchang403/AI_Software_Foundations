# Function Registry Template

This registry defines the "Skills" (Tools) available to the AI Agent via Function Calling or MCP.

## 1. File Operations
- `read_file(path)`: Use to ingest ADRs or context-enriched stories.
- `write_to_file(path, content)`: Use to implement feature code.

## 2. Domain-Specific Tools (Example)
```json
{
  "name": "validate_tax_id",
  "description": "Validates a VAT ID against the regional service.",
  "parameters": {
    "type": "object",
    "properties": {
      "tax_id": { "type": "string" },
      "region": { "type": "string", "enum": ["US", "EU"] }
    },
    "required": ["tax_id", "region"]
  }
}
```

## 3. Constraint-Check Tools
- `check_constitution(content)`: Scans generated code for PII or Article VI violations.
