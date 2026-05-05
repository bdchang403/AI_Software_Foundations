# Example: Decomposition & Token Math

Strategy Leads often fail AI initiatives by providing scope that exceeds token window logic.

## ❌ The BAD Example: The Monolithic Epic
**Epic:** Rebuild the Legacy Billing Dashboard  
*"We need to migrate the entire Angular dashboard to React. The AI should read the existing `src/billing` directory and recreate the 15 UI views, the 5 data service layers, and the Redux state store."*

### Why this fails mathematically:
- `src/billing` $\approx$ 15,000 LOC.
- 15,000 LOC $\approx$ 120,000 Input Tokens.
- Outputting 15,000 LOC in one go $\approx$ 120,000 Output Tokens.
- Most LLMs have a hard output limit of exactly 4,096 tokens per request. 
- **Result:** The AI will crash at 4% completion, leaving corrupted half-finished files.

---

## ✅ The GOOD Example: Token-Bounded Delivery
**Epic:** Migrate Billing Dashboard (Segmented)

**Story 1: Scaffold Initial Redux Store (Data Layer)**
- *Scope:* Migrate only `billing.service.ts` and `billing.store.ts` to Redux Toolkit.
- *Input Token Weight:* ~1,500 Tokens.
- *Output Token Weight:* ~800 Tokens.
- *Probability of AI Success:* 99%

**Story 2: Scaffold View - Invoice List (UI Layer)**
- *Scope:* Migrate only `invoice-list.component.html/.ts` to React.
- *Dependency Limit:* AI is only allowed to import the Store from Story 1. It is forbidden from writing new service logic.
- *Input Token Weight:* ~2,000 Tokens.
- *Output Token Weight:* ~1,200 Tokens.
- *Probability of AI Success:* 95%

### Why this succeeds:
By enforcing strict architectural boundaries, the AI never hits the 4,096 output ceiling, and it never suffers from "Lost in the Middle" attention degradation.
