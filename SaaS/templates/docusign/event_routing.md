# ADR-001: DocuSign Connect Webhook Logic

## Context
We must maintain an immutable audit trail of all signed contracts.

## Decision
1. **Completed Envelopes:** When we receive an `envelope-completed` event from DocuSign Connect, the AI must write logic to parse the payload, extract the PDF bytes, and save the signed PDF to the secure `/archive` network drive.
2. **Voided Envelopes:** If the event is `envelope-voided`, log the void reason to the database and trigger a Slack alert to the Sales team.
