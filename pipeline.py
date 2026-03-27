"""
Decompose 209 Chen-Zimmermann anomalies into overnight vs intraday components.
Reads CRSP daily data + locally saved signal CSVs.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import warnings

warnings.filterwarnings('ignore')
os.makedirs("output", exist_ok=True)

CRSP_PATH = r"D:\Liquidity Scoring Engine\Data 2\crsp_daily.csv"
SIGNALS_DIR = r"D:\Liquidity Scoring Engine\Data 2\signals"


# load and prep CRSP
print("Loading CRSP data...")
t0 = time.time()

crsp = pd.read_csv(
    CRSP_PATH,
    usecols=['PERMNO', 'date', 'PRC', 'OPENPRC', 'RET', 'SHROUT'],
    dtype={'PERMNO': int, 'PRC': float, 'OPENPRC': float, 'SHROUT': float},
    low_memory=False,
)

crsp['date'] = pd.to_datetime(crsp['date'], format='mixed')
crsp = crsp.sort_values(['PERMNO', 'date']).reset_index(drop=True)
crsp['RET'] = pd.to_numeric(crsp['RET'], errors='coerce')

print(f"  {len(crsp):,} rows, {crsp['PERMNO'].nunique():,} stocks ({time.time()-t0:.0f}s)")

# session returns
crsp['prc_abs'] = crsp['PRC'].abs()
crsp['prev_close'] = crsp.groupby('PERMNO')['prc_abs'].shift(1)
crsp['overnight'] = np.log(crsp['OPENPRC'] / crsp['prev_close'])
crsp['intraday'] = np.log(crsp['prc_abs'] / crsp['OPENPRC'])

for col in ['overnight', 'intraday']:
    crsp.loc[crsp[col].abs() > 0.5, col] = np.nan

crsp = crsp.dropna(subset=['overnight', 'intraday'])
crsp['yyyymm'] = crsp['date'].dt.year * 100 + crsp['date'].dt.month

print(f"  {len(crsp):,} valid session-return observations")


# load all signal files and merge with CRSP one at a time
# this avoids building a massive merged dataframe in memory
signal_files = [f for f in os.listdir(SIGNALS_DIR) if f.endswith('.csv')]
print(f"\n{len(signal_files)} signal files found. Running decompositions...\n")

results = []
failed = []

for i, fname in enumerate(sorted(signal_files)):
    char = fname.replace('.csv', '')
    if (i + 1) % 25 == 0:
        print(f"  {i+1}/{len(signal_files)}: {char}")

    try:
        sig = pd.read_csv(os.path.join(SIGNALS_DIR, fname))

        # standardize column names
        sig.columns = [c.lower() if c.lower() in ['permno', 'yyyymm'] else c for c in sig.columns]
        if 'permno' in sig.columns:
            sig = sig.rename(columns={'permno': 'PERMNO'})

        # the signal value column is whatever isn't permno or yyyymm
        val_cols = [c for c in sig.columns if c not in ['PERMNO', 'yyyymm']]
        if len(val_cols) != 1:
            failed.append((char, f"unexpected columns: {sig.columns.tolist()}"))
            continue
        val_col = val_cols[0]

        sig = sig.dropna(subset=[val_col])
        sig['PERMNO'] = sig['PERMNO'].astype(int)
        sig['yyyymm'] = sig['yyyymm'].astype(int)

        # merge with CRSP on PERMNO + yyyymm
        merged = crsp.merge(sig[['PERMNO', 'yyyymm', val_col]], on=['PERMNO', 'yyyymm'], how='inner')

        if len(merged) < 10000:
            failed.append((char, f"only {len(merged)} obs after merge"))
            continue

        # quintile sort each month
        merged['q'] = merged.groupby('yyyymm')[val_col].transform(
            lambda x: pd.qcut(x, 5, labels=False, duplicates='drop') if len(x) >= 20 else np.nan
        )
        merged = merged.dropna(subset=['q'])

        if len(merged) < 5000:
            failed.append((char, "not enough after sorting"))
            continue

        # long-short spread: Q5 minus Q1, daily
        q5 = merged[merged['q'] == 4].groupby('date')[['overnight', 'intraday']].mean()
        q1 = merged[merged['q'] == 0].groupby('date')[['overnight', 'intraday']].mean()

        common = q5.index.intersection(q1.index)
        if len(common) < 500:
            failed.append((char, "not enough overlap"))
            continue

        spread = q5.loc[common] - q1.loc[common]
        monthly = spread.resample('ME').sum().dropna()

        if len(monthly) < 24:
            failed.append((char, "not enough months"))
            continue

        o_mean = monthly['overnight'].mean()
        i_mean = monthly['intraday'].mean()
        o_t = o_mean / (monthly['overnight'].std() / np.sqrt(len(monthly)))
        i_t = i_mean / (monthly['intraday'].std() / np.sqrt(len(monthly)))

        total_abs = abs(o_mean) + abs(i_mean)
        ratio = abs(o_mean) / total_abs if total_abs > 0 else 0.5

        if abs(o_mean) > abs(i_mean) * 1.5 and abs(o_t) > 1.65:
            cls = "OVERNIGHT"
        elif abs(i_mean) > abs(o_mean) * 1.5 and abs(i_t) > 1.65:
            cls = "INTRADAY"
        else:
            cls = "MIXED"

        results.append({
            'characteristic': char,
            'overnight_ann': o_mean * 12,
            'overnight_t': o_t,
            'intraday_ann': i_mean * 12,
            'intraday_t': i_t,
            'session_ratio': ratio,
            'classification': cls,
            'n_months': len(monthly),
        })

    except Exception as e:
        failed.append((char, str(e)))

print(f"\n{len(results)} succeeded, {len(failed)} failed")
if failed:
    print(f"  failed examples: {failed[:5]}")


# results table
res_df = pd.DataFrame(results).sort_values('overnight_ann', ascending=False)

print(f"\n{'Char':<25} {'Over%':>8} {'Ot':>6} {'Intra%':>8} {'It':>6} {'Class':>10}")
print("-" * 70)
for _, r in res_df.iterrows():
    print(f"{r['characteristic']:<25} {r['overnight_ann']:>7.2%} {r['overnight_t']:>5.1f} "
          f"{r['intraday_ann']:>7.2%} {r['intraday_t']:>5.1f} {r['classification']:>10}")

counts = res_df['classification'].value_counts()
total = len(res_df)
print(f"\nBreakdown:")
for c, n in counts.items():
    print(f"  {c}: {n} ({n/total:.0%})")

res_df.to_csv("output/anomaly_decomposition.csv", index=False)


# scatter plot
fig, ax = plt.subplots(figsize=(12, 12))

colors = {'OVERNIGHT': '#1a5276', 'INTRADAY': '#c0392b', 'MIXED': '#7f8c8d'}

for cls in ['OVERNIGHT', 'INTRADAY', 'MIXED']:
    sub = res_df[res_df['classification'] == cls]
    ax.scatter(
        sub['overnight_ann'] * 100, sub['intraday_ann'] * 100,
        c=colors[cls], s=50, alpha=0.7, edgecolors='white', linewidth=0.5,
        label=f"{cls} ({len(sub)})",
    )

top = pd.concat([
    res_df.nlargest(5, 'overnight_ann'),
    res_df.nsmallest(5, 'overnight_ann'),
    res_df.nlargest(5, 'intraday_ann'),
    res_df.nsmallest(5, 'intraday_ann'),
]).drop_duplicates(subset='characteristic')

for _, r in top.iterrows():
    ax.annotate(r['characteristic'],
                (r['overnight_ann'] * 100, r['intraday_ann'] * 100),
                textcoords="offset points", xytext=(8, 4), fontsize=7)

ax.axhline(0, color='black', lw=0.5, alpha=0.3)
ax.axvline(0, color='black', lw=0.5, alpha=0.3)
ax.plot([-100, 100], [-100, 100], 'k--', alpha=0.15)

ax.set_xlabel('Overnight annual alpha (%)', fontsize=12)
ax.set_ylabel('Intraday annual alpha (%)', fontsize=12)
ax.set_title(f'Session decomposition: {len(results)} anomalies', fontsize=14, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.2)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('output/anomaly_scatter.png', dpi=200, bbox_inches='tight')

print(f"\nTop 10 overnight:")
for _, r in res_df.nlargest(10, 'overnight_ann').iterrows():
    print(f"  {r['characteristic']:<25} over={r['overnight_ann']:>7.2%} (t={r['overnight_t']:.1f})  "
          f"intra={r['intraday_ann']:>7.2%} (t={r['intraday_t']:.1f})")

print(f"\nTop 10 intraday:")
for _, r in res_df.nlargest(10, 'intraday_ann').iterrows():
    print(f"  {r['characteristic']:<25} over={r['overnight_ann']:>7.2%} (t={r['overnight_t']:.1f})  "
          f"intra={r['intraday_ann']:>7.2%} (t={r['intraday_t']:.1f})")

print("\nDone. Check output/anomaly_scatter.png")