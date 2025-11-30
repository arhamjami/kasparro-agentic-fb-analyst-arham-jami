import pandas as pd
import numpy as np

class DataAgent:
    def __init__(self, path):
        self.path = path
        self.df = None

    def load(self):
        df = pd.read_csv(self.path)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        if 'ctr' not in df.columns and {'clicks','impressions'}.issubset(df.columns):
            df['ctr'] = df['clicks'] / df['impressions']
        for c in ['spend','impressions','clicks','purchases','revenue','roas','ctr']:
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors='coerce')
        self.df = df
        return df

    def summarize(self):
        df = self.load()
        summary = {
            'n_rows': int(len(df)),
            'n_campaigns': int(df['campaign_name'].nunique()) if 'campaign_name' in df.columns else 0,
            'date_range': [str(df['date'].min()) if 'date' in df.columns else None, str(df['date'].max()) if 'date' in df.columns else None],
            'columns_present': df.columns.tolist(),
            'by_campaign': df.groupby('campaign_name').agg({'roas':'mean','ctr':'mean','spend':'sum','impressions':'sum'}).reset_index().to_dict(orient='records')[:50]
        }
        return summary

    def get_low_ctr_campaigns(self, threshold=0.015):
        df = self.df
        if df is None:
            self.load()
        ctr_by_campaign = df.groupby('campaign_name')['ctr'].mean().dropna()
        low = ctr_by_campaign[ctr_by_campaign < threshold].index.tolist()
        return low

    def slice_window(self, recent_days=7, baseline_days=28):
        df = self.df.copy()
        if 'date' not in df.columns:
            raise ValueError('date column required')
        max_date = df['date'].max()
        recent_start = max_date - pd.Timedelta(days=recent_days)
        baseline_start = max_date - pd.Timedelta(days=baseline_days)
        recent = df[df['date'] > recent_start]
        baseline = df[(df['date'] <= recent_start) & (df['date'] > baseline_start)]
        return recent, baseline
