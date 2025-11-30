# Agent graph and data flow

Diagram:
Planner -> Data Agent -> Insight Agent -> Evaluator -> Creative Generator

Explanation:
- Planner decomposes the query into tasks (see prompts/planner.md).
- Data Agent provides summary statistics and aggregated windows (recent vs baseline).
- Insight Agent proposes hypotheses grounded in summary stats and creative_message text mining.
- Evaluator validates hypotheses quantitatively (Welch t-test / bootstrap) and marks confidence.
- Creative Generator uses validated insights to produce contextual creative variants.

Design rationale:
- Separation of concerns enables testability and extensibility. Reflection loops handle low-confidence outputs by requesting re-aggregation or grouping.
