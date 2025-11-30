import os, json, yaml
from pathlib import Path
from agents.data_agent import DataAgent
from agents.planner import Planner
from agents.insight_agent import InsightAgent
from agents.evaluator import Evaluator
from agents.creative_generator import CreativeGenerator

class Orchestrator:
    def __init__(self, data_path=None, config_path='config/config.yaml'):
        self.config = yaml.safe_load(open(config_path))
        self.data_path = data_path or self.config.get('sample_data_path')
        self.output_dir = Path(self.config.get('output_dir', 'reports'))
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self, query):
        planner = Planner()
        plan = planner.decompose(query)
        data_agent = DataAgent(self.data_path)
        data_summary = data_agent.summarize()

        insight_agent = InsightAgent()
        hypotheses = insight_agent.generate(data_summary, plan, config=self.config)

        evaluator = Evaluator(config=self.config)
        validations = evaluator.validate(hypotheses, data_agent)

        creative_gen = CreativeGenerator()
        creatives = creative_gen.generate(data_agent, validations, config=self.config)

        insights_path = self.output_dir / 'insights.json'
        creatives_path = self.output_dir / 'creatives.json'
        report_path = self.output_dir / 'report.md'

        with open(insights_path, 'w') as f:
            json.dump(hypotheses, f, indent=2)
        with open(creatives_path, 'w') as f:
            json.dump(creatives, f, indent=2)

        with open(report_path, 'w') as f:
            f.write('# Executive Summary\n\n')
            f.write('## Query\n')
            f.write(str(plan['query']) + '\n\n')
            f.write('## Top insights\n')
            for h in hypotheses:
                f.write(f"- {h.get('id')}: {h.get('hypothesis')} (conf {h.get('prior_confidence')})\n")
            f.write('\n## Validations\n')
            for v in validations:
                f.write(f"- {v.get('hypothesis_id')}: {v.get('conclusion')} (p={v.get('p_value')})\n")
        return {'report_path': str(report_path), 'insights_path': str(insights_path), 'creatives_path': str(creatives_path)}
