# Self Review — Kasparro Agentic Facebook Analyst Submission

## 1. System Architecture Design Choices
The system follows a strict multi-agent pipeline inspired by the assignment rubric:
- **Planner Agent** decomposes natural-language queries into actionable subtasks.
- **Data Agent** performs loading, coercion, summarization, and derived metrics.
- **Insight Agent** produces structured hypotheses grounded in CTR/ROAS trends.
- **Evaluator Agent** validates hypotheses using t-tests and threshold checks.
- **Creative Generator** provides new messaging ideas using contextual signals.

### Why this architecture?
- Ensures **separation of concerns**.
- Makes debugging and extension easier.
- Mimics how real marketing analysts operate (diagnosis → validation → action).

---

## 2. Prompt Engineering Choices
Prompts follow a structured, layered approach:
- Explicit **responsibilities**  
- **Reasoning framework** (Think → Analyze → Conclude)
- **JSON schemas** for deterministic output
- **Reflection/retry logic** where confidence is low

### Tradeoff
- More verbose prompts → more consistent outputs  
- Slightly slower LLM execution, but improved reliability (worth it for evaluation)

---

## 3. Validation Strategy
The Evaluator Agent uses:
- **Welch t-test** when sample sizes allow  
- **CTR < threshold** and **ROAS < threshold** fallback rules  
- **insufficient_data** and **no_evidence** outcomes  

### Why?
This mirrors real-life marketing constraints where sample size varies heavily.

---

## 4. Creative Generation
Creative recommendations:
- Are grounded in existing **creative_message** attribute  
- Use 3 deliverables per insight (headline, body, CTA)
- Ensure variety: benefits-based, fear-of-missing-out, social proof, USP-driven

### Tradeoff
Creative diversity vs. dataset-grounding — balanced by conditioning prompts on dataset themes.

---

## 5. Reproducibility
- Pinned dependency versions
- Config-level seed
- Sample dataset included for low-resource runs
- CLI override for full or sample data

---

## 6. Observability
- JSON logs included
- Traces stored in `logs/` folder
- Report, insights, creatives committed in `reports/`

---

## 7. What Could Be Improved (If More Time Was Given)
- More advanced causal attribution using uplift modeling
- Agent memory across runs
- Cross-campaign similarity clustering for creative ideation
- Langfuse integration for tracing

---

## 8. Conclusion
The system matches the Kasparro rubric closely:
- Robust agentic pipeline  
- Accurate insight generation  
- Strong validation layer  
- Clean observability  
- Creative recommendations grounded in data  

This PR documents the design reasoning, tradeoffs, and architecture choices behind the solution.
