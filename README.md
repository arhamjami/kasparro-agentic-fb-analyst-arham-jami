# kasparro-agentic-fb-analyst-arham-jami

This repository contains my submission for the **Kasparro Applied AI Engineer – Agentic Facebook Performance Analyst Assignment**.  
It implements a **multi-agent system** that analyzes Facebook Ads performance, generates hypotheses, validates them statistically, and produces creative recommendations.

The system is modular, production-ready, and structured according to the official evaluator checklist.

---

# 🚀 Quick Start

```bash
python -V  # should be >= 3.10
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days" --data data/synthetic_fb_ads_undergarments.csv
```

This generates:

- reports/report.md – human-readable summary  
- reports/insights.json – structured insight hypotheses  
- reports/creatives.json – creative recommendations  

---

# 📁 Data

- The full CSV is located at `data/synthetic_fb_ads_undergarments.csv`
- You can override with:  
  `DATA_CSV=/path/to/file.csv`
- For sampling or debugging, create a smaller file at:  
  `data/sample_fb_ads.csv`

---

# ⚙️ Config

Edit `config/config.yaml`:

```yaml
python: "3.10"
random_seed: 42
confidence_min: 0.6
sample_data_path: data/synthetic_fb_ads_undergarments.csv
output_dir: reports
ctr_threshold: 0.015
roas_threshold: 1.0
```

---

# 🧠 System Architecture

This project follows an **agentic pipeline architecture** consisting of 5 specialized agents orchestrated by a central controller.

User Query → Planner → Data Agent → Insight Agent → Evaluator → Creative Generator

---

# 📂 Repository Map

```
src/agents/        # planner.py, data_agent.py, insight_agent.py, evaluator.py, creative_generator.py
prompts/           # *.md prompt files
reports/           # report.md, insights.json, creatives.json
logs/              # execution logs / traces
tests/             # test_evaluator.py
config/            # config.yaml
data/              # dataset
```

---

# 📈 Output Examples

### insights.json
```json
[
  {
    "campaign": "men signature soft",
    "type": "low_ctr",
    "confidence": 0.60
  }
]
```

### creatives.json
- Includes headlines, primary text, CTAs  
- 3–6 creative suggestions per flagged campaign

---

# 🧪 Testing

```bash
python -m pytest tests
```

---

# 🔍 Observability

Place Langfuse logs or exported traces here:

```
reports/observability/
```

---

# 🏷️ Release

To tag a release:

```bash
git tag -a v1.0 -m "Kasparro submission v1.0"
git push origin v1.0
```

---

# 👤 Author

**Arham Jami**  
Applied AI Engineer Candidate
