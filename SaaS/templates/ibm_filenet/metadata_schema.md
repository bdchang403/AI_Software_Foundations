# ADR-001: FileNet Metadata Schema Constraints

## Context
Property constraints are enforced at the database level. AI-generated scripts must validate data before attempting to persist to the Content Engine.

## Decision
1. **Account Number validation:** The `AccountNumber` property must ALWAYS be a 10-digit string. If it is less than 10 digits, pad it with leading zeros.
2. **Date Formatting:** Custom date properties must be passed to the CE API as `java.util.Date` objects, not strings.
