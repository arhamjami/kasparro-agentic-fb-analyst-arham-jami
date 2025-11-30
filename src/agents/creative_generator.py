import itertools, uuid

TEMPLATES = [
    ('Urgency', '{headline} — limited time only!'),
    ('SocialProof', 'Join {n} customers who switched to {product}.'),
    ('Benefit', 'Get {benefit} with {product}.'),
    ('Curiosity', 'What happens when you {action}? Find out.'),
    ('Testimonial', '“{quote}” — Real customer')
]

class CreativeGenerator:
    def generate(self, data_agent, validations, config=None):
        config = config or {}
        low_campaigns = data_agent.get_low_ctr_campaigns(threshold=config.get('ctr_low_threshold',0.015))
        df = data_agent.df
        suggestions = []
        for c in low_campaigns:
            seed_msgs = df[df['campaign_name']==c]['creative_message'].dropna().astype(str).tolist()[:10] if 'creative_message' in df.columns else []
            seeds = set()
            for s in seed_msgs:
                parts = s.split('.')
                for p in parts:
                    if len(p.strip())>10:
                        seeds.add(p.strip())
            seeds = list(seeds)[:5]
            items = []
            for i,(tag,tmpl) in zip(range(12), itertools.cycle(TEMPLATES)):
                id_ = str(uuid.uuid4())[:8]
                seed = seeds[i % max(1,len(seeds))] if seeds else 'this product'
                headline = tmpl.format(headline='Hurry', n=120, product=seed, benefit='savings', action='try this', quote='Best purchase ever')
                primary_text = f"Try {seed} now — limited stock. Works great for {c}."
                cta = 'Shop Now' if i%2==0 else 'Learn More'
                items.append({'id':id_,'headline':headline,'primary_text':primary_text,'cta':cta,'rationale':tag,'diversity_tag':tag})
                if len(items)>=12:
                    break
            suggestions.append({'campaign':c,'suggestions':items})
        return suggestions
