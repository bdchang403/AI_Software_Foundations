# Module 1: Interpreting AI System Metrics (Signal vs. Noise)

## 🧠 Theory: Metrics are the "Smoke Detectors" of Context

In a Context Factory, metrics are no longer about "Velocity"—they are about **Accuracy**. 

If your team's velocity triples, but your technical debt also triples, you aren't more productive; you are just automatedly making things worse. As an Agile Leader, you must look for the **Context-to-Code Ratio**.

### 🚥 Key Signals to Watch:

#### 1. The "Hallucination Loop" (Lead Time Spiking)
If the **Lead Time for Changes** is increasing while **PR Size** is decreasing, your builders are likely suffering from **Context Fatigue**. They are stuck in a loop of:
- *Prompt AI* -> *AI breaks code* -> *Revert* -> *Try different prompt*.
- **The Fix:** Coach the Requirements Lead to improve the **Semantic Blueprint**. Don't blame the Builder; blame the context.

#### 2. The "Reviewer Choke-Point" (Comment Spikes)
If the number of comments per PR increases while using AI, it means the human reviewer is working *harder* to catch the AI's mistakes. 
- **The Signal:** The AI is ignoring your **Enterprise Constitution**.
- **The Fix:** Audit the **Master Router**. Is the AI being fed the correct ADRs? If not, the AI is "guessing" the style guide, and humans are paying the price in review time.

#### 3. The "Ghost Productivity" (Lines of Code Spiking)
AI can generate 1,000 lines in 5 seconds. If your `LOC` metric is skyrocketing but your `Business Value Delivered` (Tickets closed) is flat, you have **Code Bloat**.
- **The Signal:** The AI is implementing "extra" features or redundant logic because the **3-Part Directive** wasn't bounded.
- **The Fix:** Coach the Strategy Lead on **Decomposition**. The AI should only solve the *exact* task, nothing more.

---

## 🛠️ Exercise: The "Perfect Failure" Scenario

**Scenario:** 
Team Alpha's dashboard shows:
- **Deployment Frequency:** 5x faster than last month.
- **Change Failure Rate:** 20% higher (bugs in production).
- **PR Size:** Small (under 200 lines).

**Your Hypothesis:**
Traditional metrics say the team is "High Performing" but "Losing Quality."
**In the Context Factory view:** The team has mastered **PR Slicing** (Module 3) but failed **Adversarial Thinking** (Module 2). 

**Your Coaching Action:**
*   **Don't** tell them to slow down.
*   **Do** require a **Validation Lead Sign-off** on the Semantic Blueprint *before* the Builder starts the AI generation. This forces the "unhappy path" to be defined before the code is written.

---

[**Next Module: Intervening in the Factory →**](./02_intervening_in_the_factory.md)
