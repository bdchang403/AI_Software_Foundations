# ADR-001: Invoice Processing Map

## Context
TTA jobs often fail if tokens are routed to nodes out of order.

## Decision
1. **Node Sequences:** The AI must always assume the following sequence for Invoices: Node 1 (Scan) -> Node 2 (Extraction) -> Node 3 (Export).
2. **Variable Immutability:** Do not write C# scripts that modify the `InvoiceTotal` variable after Node 2. It must be locked before export.
