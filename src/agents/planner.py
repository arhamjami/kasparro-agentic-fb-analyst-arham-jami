class Planner:
    def decompose(self, query: str):
        tasks = [
            {'id': 't1', 'name': 'load_data', 'description': 'Load and validate dataset', 'depends_on': [], 'expected_output': 'data_summary'},
            {'id': 't2', 'name': 'summarize', 'description': 'Compute high level summaries', 'depends_on': ['t1'], 'expected_output': 'aggregates'},
            {'id': 't3', 'name': 'generate_hypotheses', 'description': 'Hypothesize reasons for ROAS/CTR changes', 'depends_on': ['t2'], 'expected_output': 'hypotheses'},
            {'id': 't4', 'name': 'validate', 'description': 'Quantitative validation of hypotheses', 'depends_on': ['t3'], 'expected_output': 'validations'},
            {'id': 't5', 'name': 'creative_suggestions', 'description': 'Produce creatives for low-CTR campaigns', 'depends_on': ['t4'], 'expected_output': 'creatives'}
        ]
        return {'tasks': tasks, 'query': query}
