# Dataset notes

File: synthetic_fb_ads_undergarments.csv

Columns:
- campaign_name, adset_name, date (YYYY-MM-DD), spend, impressions, clicks, ctr, purchases, revenue, roas, creative_type, creative_message, audience_type, platform, country

Small sample:
- Put a sample CSV at data/sample_fb_ads.csv with 200 rows for quick reproducibility.

To run using sample:
python src/run.py "Analyze ROAS drop" --data data/sample_fb_ads.csv
