# [STORY-ID]: [Story Title]

> [!NOTE]
> **Requirements Lead Customization Guide:** 
> - **[REQUIRED]**: The 3-Part Directive & Semantic Blueprint must remain for AI success.
> - **[MODULAR]**: You may add your company-specific Acceptance Criteria (AC) or Internal Doc links below.
> - **[OPTIONAL]**: The Edge Case Matrix can be removed for trivial, single-file changes.

## 1. Traditional Acceptance Criteria [MODULAR]
*Use this section for your existing human-to-human project management requirements.*
- **AC1:** [e.g., User must see a confirmation modal]
- **AC2:** [e.g., Error message must be localized in Spanish]

## 2. The 3-Part Directive [REQUIRED - AI Instructions]
- **Role:** You are a [Persona Name].
- **Task:** [Specific, bounded technical goal].
- **Format:** [The exact output format, e.g., TypeScript Service with 100% test coverage].

## 3. Knowledge & Research Links [MODULAR]
*Link to internal documentation here. The AI will use these as "starting points" for research.*
- **Technical Wiki:** [URL to Confluence/Wiki]
- **Design Specs:** [URL to Figma/AdobeXD]
- **API Swagger:** [URL to internal API docs]

## 4. Strategic Context (Why) [REQUIRED]
[1-2 sentences on business value to prevent the AI from optimizing for the wrong outcome].

## 5. 🧩 Semantic Blueprint [REQUIRED]
| Business Term | Technical Route / ADR | AI Constraint |
| :--- | :--- | :--- |
| `[User Term]` | `src/[path]/` | `MUST use the [Repository] pattern.` |
| `[Business Logic]` | `docs/adr/[XXX].md` | `Strictly adhere to the [Decision] logic.` |

## 6. Adversarial Guardrails [REQUIRED]
- **DO NOT** [Hallucinated behavior, e.g., Create a new database table].
- **DO NOT** [Anti-pattern, e.g., Use any library outside of the core package.json].

## 7. 🔍 Edge Case Matrix [OPTIONAL]
- [Edge Case 1]: [Expected behavior]
- [Edge Case 2]: [Expected behavior]
