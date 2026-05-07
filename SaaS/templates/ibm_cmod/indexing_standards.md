# ADR-001: ACIF Indexing Coordinates

## Context
Standardizing the ACIF parameters prevents mis-indexed reports from failing silently.

## Decision
1. **Invoice Triggers:** For Invoice load files, the Account Number is always located on Line 5, Column 10. The AI must use this trigger logic for the `TRIGGER1` parameter.
2. **Date Extraction:** The Statement Date is always located on Line 2, Column 60.
