import numpy as np
try:
    from scipy import stats
    _HAS_SCIPY = True
except Exception:
    _HAS_SCIPY = False

def welch_ttest(a, b):
    # returns t statistic and p-value (two-sided) using Welch's t-test approx
    a = np.array(a); b = np.array(b)
    ma = np.nanmean(a); mb = np.nanmean(b)
    sa = np.nanvar(a, ddof=1); sb = np.nanvar(b, ddof=1)
    na = np.sum(~np.isnan(a)); nb = np.sum(~np.isnan(b))
    denom = np.sqrt(sa/na + sb/nb)
    if denom == 0:
        return 0.0, 1.0
    t = (ma - mb) / denom
    # degrees of freedom
    df = (sa/na + sb/nb)**2 / ((sa**2)/((na**2)*(na-1)) + (sb**2)/((nb**2)*(nb-1))) if (na>1 and nb>1) else 1
    # approximate two-sided p-value using normal approx if df small
    try:
        if _HAS_SCIPY:
            p = stats.t.sf(abs(t), df)*2
        else:
            # use normal approximation
            from math import erf, sqrt
            z = abs(t)
            p = 2*(1 - 0.5*(1 + erf(z / sqrt(2))))
    except Exception:
        p = 1.0
    return float(t), float(p)

class Evaluator:
    def __init__(self, config=None):
        self.config = config or {}

    def validate(self, hypotheses, data_agent):
        results = []
        recent_days = self.config.get('recent_window_days', 7)
        baseline_days = self.config.get('baseline_window_days', 28)
        recent, baseline = data_agent.slice_window(recent_days, baseline_days)

        if not recent.empty and not baseline.empty and 'roas' in recent.columns and 'roas' in baseline.columns:
            try:
                a = recent['roas'].dropna().values
                b = baseline['roas'].dropna().values
                if _HAS_SCIPY:
                    stat, p = stats.ttest_ind(a, b, equal_var=False)
                else:
                    stat, p = welch_ttest(a, b)
                mean_diff = float(np.nanmean(a) - np.nanmean(b))
                conclusion = 'significant_drop' if (mean_diff < 0 and p < 0.05) else 'no_significant_drop'
                results.append({'hypothesis_id':'h_global_drop','test_name':'ttest_ind','statistic':float(stat),'p_value':float(p),'effect_size':mean_diff,'conclusion':conclusion,'confidence':0.7 if p<0.05 else 0.4})
            except Exception as e:
                results.append({'hypothesis_id':'h_global_drop','conclusion':'test_error','error':str(e),'confidence':0.1})

        df = data_agent.df
        for h in hypotheses:
            if h['id'].startswith('h_') and 'Creative underperformance' in h['hypothesis']:
                campaign = h['campaign']
                seg = df[df['campaign_name']==campaign]
                res = {'hypothesis_id':h['id'],'campaign':campaign}
                if len(seg) < 5:
                    res.update({'conclusion':'insufficient_data','confidence':0.2})
                else:
                    others = df[df['campaign_name']!=campaign]
                    if len(others) < 5:
                        res.update({'conclusion':'no_bench_data','confidence':0.3})
                    else:
                        try:
                            a = seg['ctr'].dropna().values
                            b = others['ctr'].dropna().values
                            if _HAS_SCIPY:
                                stat, p = stats.ttest_ind(a, b, equal_var=False)
                            else:
                                stat, p = welch_ttest(a, b)
                            mean_cmp = float(np.nanmean(a) - np.nanmean(b))
                            res.update({'test_name':'ttest_ind','statistic':float(stat),'p_value':float(p),'conclusion':'creative_underperforming' if p<0.05 and mean_cmp<0 else 'no_evidence','confidence':0.8 if p<0.05 else 0.4})
                        except Exception as e:
                            res.update({'conclusion':'error','error':str(e),'confidence':0.1})
                results.append(res)
            elif h['id'].startswith('h_roas_'):
                campaign = h['campaign']
                seg = df[df['campaign_name']==campaign]
                if len(seg) < 5:
                    results.append({'hypothesis_id':h['id'],'campaign':campaign,'conclusion':'insufficient_data','confidence':0.2})
                else:
                    others = df[df['campaign_name']!=campaign]
                    try:
                        a = seg['roas'].dropna().values
                        b = others['roas'].dropna().values
                        if _HAS_SCIPY:
                            stat, p = stats.ttest_ind(a, b, equal_var=False)
                        else:
                            stat, p = welch_ttest(a, b)
                        mean_cmp = float(np.nanmean(a) - np.nanmean(b))
                        results.append({'hypothesis_id':h['id'],'campaign':campaign,'test_name':'ttest_ind','statistic':float(stat),'p_value':float(p),'conclusion':'low_roas_vs_peers' if p<0.05 and mean_cmp<0 else 'no_evidence','confidence':0.75 if p<0.05 else 0.35})
                    except Exception as e:
                        results.append({'hypothesis_id':h['id'],'campaign':campaign,'conclusion':'error','error':str(e),'confidence':0.1})
        return results
