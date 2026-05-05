# Module 2: Adversarial Thinking & Red-Teaming for Strategy Leads

## Theory: Breaking the Bot
The AI wants to please you. If you leave ambiguity in your Epic scope, the AI will confidently hallucinate a solution that sounds plausible but destroys your architecture. 

**Red-Teaming** in ownership means actively trying to find how an AI could purposefully misunderstand your directive, and then writing a "constraint patch" before handing it to the Requirements Lead.

## Verbose Example
**Initial Epic Prompt:** "Integrate Stripe to allow users to pay for premium subscriptions."

**Adversarial Thought (How the AI might break this):** 
*"Wait, if I pass this to an AI Agent via a Builder, the AI might realize we already have a legacy payment DB. It might write a script to migrate all old users to Stripe without asking, taking down our live revenue stream."*

**The Red-Team Patch (Added to the Epic):**
*"Constraint: This integration is strictly for NEW users. Under NO circumstances should any legacy payment records be modified, migrated, or read by the Stripe integration during this phase."*

## Exercise: Patching the Loophole

**Scenario:** You wrote an Epic defining a new "Bulk User Delete" feature to comply with GDPR. 

**Your current Epic rule says:** *"Admins can delete any user from the interface to comply with data privacy policies."*

**Action Required:**
Think adversarially. What catastrophic action could an AI builder agent take when writing code for "delete any user"? 
* **Write your Red-Team Patch here:** [e.g., "Constraint: Admins cannot delete other Admins, and system-level accounts must be excluded from this deletion cascade..."]

*(Once complete, proceed to the next module)*

---
[**Next Module: Decomposition Mathematics →**](./03_decomposition.md)
