# kasparro-agentic-fb-analyst-arham-jami

This repository contains my submission for the **Kasparro Applied AI Engineer – Agentic FB Analyst Assignment**.  
It implements a **multi-agent system** that analyzes Facebook Ads performance, generates hypotheses, validates them statistically, and produces creative recommendations.

The system is fully modular, production-ready, and structured according to Kasparro’s evaluator checklist.

---

# 🚀 Quickstart

### **1. Install dependencies**
```
python -m pip install -r requirements.txt
```

*(Ensure `pandas` and `numpy` are installed if running in a restricted/offline environment.)*

### **2. Run the pipeline**
```
python src/run.py "Analyze ROAS drop in last 7 days" --data data/synthetic_fb_ads_undergarments.csv
```

This generates:

- reports/report.md – human-readable summary  
- reports/insights.json – structured insight hypotheses  
- reports/creatives.json – creative recommendations  

---

# 🧠 System Architecture

This project follows an **agentic pipeline architecture** consisting of 5 specialized agents orchestrated by a central controller.

(Architecture diagram omitted in downloadable file)

---

# 📂 Project Structure

```
kasparro-agentic-fb-analyst-arham-jami/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│   └── config.yaml
│
├── data/
│   └── synthetic_fb_ads_undergarments.csv
│
├── prompts/
│   ├── planner.md
│   ├── data_agent.md
│   ├── insight_agent.md
│   ├── evaluator.md
│   └── creative_generator.md
│
├── src/
│   ├── run.py
│   ├── orchestrator.py
│   └── agents/
│       ├── planner.py
│       ├── data_agent.py
│       ├── insight_agent.py
│       ├── evaluator.py
│       └── creative_generator.py
│
├── reports/
│   ├── report.md
│   ├── insights.json
│   └── creatives.json
│
├── logs/
│   └── run_log.json
│
└── tests/
    └── test_evaluator.py
```

---

# 📈 Output Examples

### **Insights (`insights.json`):**
```
[
  {
    "campaign": "men signature soft",
    "type": "low_ctr",
    "confidence": 0.60
  }
]
```

---

# 🔧 Configuration

Example:
```
python: "3.10"
sample_data_path: data/synthetic_fb_ads_undergarments.csv
output_dir: reports
ctr_threshold: 0.015
roas_threshold: 1.0
```

---

# 🧪 Testing
```
python -m pytest tests
```

---

# 👤 Author

**Arham Jami**  
Applied AI Engineer Candidate
