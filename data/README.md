# Data Folder Documentation

This folder contains the datasets used by the Agentic Facebook Performance Analyst system.

## 📌 Files Included

### 1. `synthetic_fb_ads_undergarments.csv`
This is the **main synthetic Facebook Ads dataset** provided for the assignment.

**Columns:**
- campaign_name
- adset_name
- date
- spend
- impressions
- clicks
- ctr
- purchases
- revenue
- roas
- creative_type
- creative_message
- audience_type
- platform
- country

This file is used for **full-run execution** of the system.

---

### 2. `sample_fb_ads.csv` (optional)
A small 200-row subset of the main dataset.

Use this when:
- running quick tests
- debugging agent behavior
- low-resource or offline environments

This file is optional but recommended for easier evaluation.

---

## 📥 How the System Loads Data

The default data path is defined in:

```
config/config.yaml
```

Example snippet:
```yaml
sample_data_path: data/synthetic_fb_ads_undergarments.csv
```

### Override the dataset at runtime:

#### ▶ Full Dataset
```bash
python src/run.py "Analyze ROAS drop" --data data/synthetic_fb_ads_undergarments.csv
```

#### ▶ Sample Dataset
```bash
python src/run.py "Analyze ROAS drop" --data data/sample_fb_ads.csv
```

---

## 🧹 Data Handling Notes (Evaluator Friendly)

- All numeric fields (`impressions`, `clicks`, `spend`, `revenue`, etc.) are coerced safely.
- Missing or inconsistent **CTR** and **ROAS** values are recomputed by the **Data Agent**.
- Dates are parsed into `YYYY-MM-DD`.
- The system supports both **full** and **sample** datasets via config or CLI.

---

## 📁 Folder Structure

```
kasparro-agentic-fb-analyst-arham-jami/
└── data/
    ├── synthetic_fb_ads_undergarments.csv
    ├── sample_fb_ads.csv   (optional)
    └── README.md           ← THIS FILE
```
