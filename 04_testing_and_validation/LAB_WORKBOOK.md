# Validation Lead Lab Workbook: Contract Validation & Adversarial Testing

Welcome to the Validation Lead Lab. In the Context Factory, the Builder's AI wrote code based on the Requirements Lead's blueprint. Your job is to mathematically prove the AI did not hallucinate.

Because AI generates code incredibly fast, you cannot rely on manual testing. You must use **Adversarial Red-Teaming** and **Contract-First Tests**.

---

## Lab 1: The AI Red-Team Exercise (Module 2)

**The Scenario:**
The Builder merged the `Point Accrual Service`. You have access to the original `LOYALTY-101.md` story.

### Your Task
Use an AI Agent to generate adversarial unit tests aimed specifically at breaking the edge cases defined by the Requirements Lead.

### Answer Key (Compare Your Work)
Run this prompt in your IDE or AI Tool:
> *"@workspace Read `docs/stories/LOYALTY-101.md`. You are an adversarial security tester. The builder implemented this in `src/services/LoyaltyService.ts`. Write 5 Jest unit tests that attempt to break the fractional dollar rounding rule and the refund clawback rule."*

---

## Lab 2: Creating the Validation Contract (Module 4)

**The Scenario:**
The CI/CD pipeline needs an automated way to verify that the AI-generated API matches the exact JSON schema defined in the original requirements.

### Your Task
Write a JSON Schema validation test. You are not testing the *logic* of the code yet; you are testing the *contract shape*. 

### Answer Key (Compare Your Work)
Your test suite should include a strict validator using a library like `ajv` or `zod`:

```typescript
import { z } from 'zod';

const LoyaltyResponseSchema = z.object({
  user_id: z.string(),
  points_awarded: z.number().int(), // Proves the AI didn't use floats
});

test('AI generated endpoint returns strict contract shape', async () => {
  const response = await api.post('/loyalty/earn', { amount: 100 });
  expect(() => LoyaltyResponseSchema.parse(response.body)).not.toThrow();
});
```

---

## Lab 3: Elevating the Test-to-Code Ratio

Because AI writes code at 10x speed, your test suite must expand proportionally. 
Review your test coverage. If your AI agent wrote 100 lines of functional code, you should have generated at least 200-300 lines of adversarial test code to surround it. If you don't, the AI velocity will outpace your safety net.
