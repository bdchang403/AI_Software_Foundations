# GitHub Copilot (platforms/copilot-instructions.md)

## Context Loading (1-Hop Pattern)
- Identify the domain being modified.
- Load the corresponding file from `docs/context/` (e.g., `billing.md`).
- Use `@workspace` to find the relevant `docs/stories/` file.

## AI-Only Trailers
- When you suggest a commit message for code YOU generated, append:
  `AI-Generated-By: GitHub-Copilot`
- When you provide feedback in a PR comment, append:
  `AI-Reviewed-By: GitHub-Copilot`
- **Exception:** Do not add trailers to human-written text suggestions where you are only correcting spelling/grammar.

## Enforcement
- Strictly follow Article VI (Bias) and Article VII (Reproducibility).
