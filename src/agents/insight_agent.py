class InsightAgent:
    def generate(self, data_summary, plan, config=None):
        hypotheses = []
        by_campaign = data_summary.get('by_campaign', [])
        for row in by_campaign:
            campaign = row.get('campaign_name') if 'campaign_name' in row else row.get('campaign_name')
            roas = row.get('roas')
            ctr = row.get('ctr')
            if roas is None:
                continue
            if ctr is not None and config and ctr < (config.get('ctr_low_threshold', 0.015)):
                hypotheses.append({'id': f'h_{campaign}', 'hypothesis': 'Creative underperformance', 'campaign': campaign, 'rationale': f'Average CTR {ctr:.4f} below threshold', 'evidence_fields': ['ctr','creative_message'], 'prior_confidence': 0.6})
            if roas < 1.0:
                hypotheses.append({'id': f'h_roas_{campaign}', 'hypothesis': 'Low ROAS possibly due to audience mismatch or bids', 'campaign': campaign, 'rationale': f'Avg ROAS {roas:.2f} < 1', 'evidence_fields': ['roas','audience_type','spend'], 'prior_confidence': 0.5})
        hypotheses.append({'id':'h_global_drop','hypothesis':'Recent ROAS drop vs baseline', 'rationale':'Compare recent window to baseline window', 'evidence_fields':['date','roas'], 'prior_confidence':0.6})
        return hypotheses
