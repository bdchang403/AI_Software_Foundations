# Claude Code Agent Config (.clauderules)

## 🕵️ Research Protocol
- Before any file modification, you MUST list the contents of `templates_and_resources/routing/` to identify the correct architectural context.
- You MUST read the `context-enriched story` for the current ticket before suggesting changes.

## 🏗️ Implementation Guidelines
- Prioritize using terminal tools (`grep`, `ls`, `cat`) to verify the existing implementation before editing.
- Ensure every PR review you conduct includes a "Constitutional Compliance" section referencing `00_ENTERPRISE_CONSTITUTION.md`.

## 📜 Auditability
- Append this trailer to all git commits: `AI-Generated-By: Claude-Code-3.5-Sonnet`
- Append this trailer to all code review summaries: `AI-Reviewed-By: Claude-Code-3.5-Sonnet`

## 🚫 Critical Constraints
- Never delete more than 100 lines of code in a single command without human confirmation.
- Do not modify files in the `06_security_and_compliance/` directory.
