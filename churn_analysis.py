"""
ShopEase Customer Churn Analysis - Exploratory Data Analysis
============================================================
Business Analyst Project | March 2026
Run: python churn_analysis.py
Output: Analysis figures saved to /analysis/charts/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# ── CONFIG ──────────────────────────────────────────────────
COLORS = {
    'primary': '#1E4D8C', 'danger': '#DC2626',
    'warning': '#D97706', 'success': '#166534',
    'light_blue': '#EEF3FB', 'light_red': '#FEF2F2'
}

# ── 1. GENERATE SYNTHETIC DATA ──────────────────────────────
np.random.seed(42)
n = 500

segments = np.random.choice(['Premium', 'Standard', 'Basic'], n, p=[0.2, 0.5, 0.3])
days_inactive = np.where(
    np.random.rand(n) > 0.5,
    np.random.randint(1, 30, n),
    np.random.randint(30, 120, n)
)
tickets = np.random.choice([0, 1, 2, 3, 4], n, p=[0.40, 0.30, 0.15, 0.10, 0.05])
open_rate = np.random.beta(2, 5, n)
login_count = np.random.randint(0, 35, n)
avg_order = np.random.uniform(20, 300, n)
categories = np.random.choice(['Electronics', 'Fashion', 'Home & Garden', 'Sports', 'Beauty'], n)

ltv_mult = np.where(segments == 'Premium', 2.0, np.where(segments == 'Basic', 0.6, 1.0))
ltv = np.random.uniform(50, 2000, n) * ltv_mult

risk_score = np.clip(
    days_inactive * 0.55 + tickets * 9 + (0.35 - open_rate) * 45
    + np.random.normal(0, 8, n), 0, 100
).astype(int)

churned = ((risk_score > 60) & (np.random.rand(n) > 0.3)).astype(int)

df = pd.DataFrame({
    'customer_id': [f'CUST_{i:04d}' for i in range(1, n+1)],
    'segment': segments,
    'days_inactive': days_inactive,
    'support_tickets': tickets,
    'email_open_rate': open_rate,
    'login_count': login_count,
    'avg_order_value': avg_order,
    'top_category': categories,
    'lifetime_value': ltv,
    'risk_score': risk_score,
    'churned': churned
})

df['risk_tier'] = pd.cut(df['risk_score'], bins=[-1, 29, 59, 100],
                          labels=['Low', 'Medium', 'High'])

print("=" * 60)
print("SHOPEASE CUSTOMER CHURN ANALYSIS")
print("=" * 60)
print(f"\nDataset: {len(df):,} customers")
print(f"Churned: {df['churned'].sum():,} ({df['churned'].mean()*100:.1f}%)")
print(f"High-Risk: {(df['risk_tier']=='High').sum():,} ({(df['risk_tier']=='High').mean()*100:.1f}%)")
print(f"Avg Risk Score: {df['risk_score'].mean():.1f}")
print(f"Avg Customer LTV: ${df['lifetime_value'].mean():.0f}")

# ── 2. VISUALIZATIONS ──────────────────────────────────────

import os
os.makedirs('/home/claude/ba-project/analysis/charts', exist_ok=True)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('ShopEase Customer Churn Analysis Dashboard', fontsize=16,
             fontweight='bold', color=COLORS['primary'], y=1.01)
fig.patch.set_facecolor('#F8FAFC')

# -- Plot 1: Churn Rate by Segment
ax1 = axes[0, 0]
seg_churn = df.groupby('segment')['churned'].agg(['mean', 'count']).reset_index()
seg_churn['mean'] *= 100
bar_colors = [COLORS['danger'] if v > 20 else COLORS['warning'] if v > 10 else COLORS['success']
              for v in seg_churn['mean']]
bars = ax1.bar(seg_churn['segment'], seg_churn['mean'], color=bar_colors, edgecolor='white', linewidth=2)
ax1.set_title('Churn Rate by Customer Segment', fontweight='bold', color=COLORS['primary'])
ax1.set_ylabel('Churn Rate (%)')
ax1.set_ylim(0, 50)
ax1.axhline(y=27, color=COLORS['danger'], linestyle='--', linewidth=1.5, label='Baseline 27%')
ax1.legend(fontsize=9)
for bar, val in zip(bars, seg_churn['mean']):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)
ax1.set_facecolor(COLORS['light_blue'])

# -- Plot 2: Risk Score Distribution
ax2 = axes[0, 1]
low = df[df['risk_tier'] == 'Low']['risk_score']
med = df[df['risk_tier'] == 'Medium']['risk_score']
high = df[df['risk_tier'] == 'High']['risk_score']
ax2.hist(low, bins=15, alpha=0.8, color=COLORS['success'], label=f'Low ({len(low)})')
ax2.hist(med, bins=15, alpha=0.8, color=COLORS['warning'], label=f'Medium ({len(med)})')
ax2.hist(high, bins=15, alpha=0.8, color=COLORS['danger'], label=f'High ({len(high)})')
ax2.axvline(x=60, color='black', linestyle='--', linewidth=2, label='Action Threshold (60)')
ax2.set_title('Risk Score Distribution by Tier', fontweight='bold', color=COLORS['primary'])
ax2.set_xlabel('Risk Score')
ax2.set_ylabel('Number of Customers')
ax2.legend(fontsize=9)
ax2.set_facecolor(COLORS['light_blue'])

# -- Plot 3: Days Inactive vs Churn
ax3 = axes[0, 2]
churned_inactive = df[df['churned'] == 1]['days_inactive']
active_inactive = df[df['churned'] == 0]['days_inactive']
ax3.hist(active_inactive, bins=20, alpha=0.7, color=COLORS['primary'], label=f'Not Churned (n={len(active_inactive)})')
ax3.hist(churned_inactive, bins=20, alpha=0.7, color=COLORS['danger'], label=f'Churned (n={len(churned_inactive)})')
ax3.set_title('Days Inactive: Churned vs Retained', fontweight='bold', color=COLORS['primary'])
ax3.set_xlabel('Days Since Last Purchase')
ax3.set_ylabel('Count')
ax3.legend(fontsize=9)
ax3.set_facecolor(COLORS['light_blue'])

# -- Plot 4: Support Tickets vs Churn Rate
ax4 = axes[1, 0]
ticket_churn = df.groupby('support_tickets')['churned'].mean() * 100
ax4.bar(ticket_churn.index, ticket_churn.values,
        color=[COLORS['danger'] if v > 30 else COLORS['warning'] for v in ticket_churn.values],
        edgecolor='white', linewidth=2)
ax4.set_title('Churn Rate by Support Tickets (90d)', fontweight='bold', color=COLORS['primary'])
ax4.set_xlabel('Number of Support Tickets')
ax4.set_ylabel('Churn Rate (%)')
ax4.set_facecolor(COLORS['light_blue'])
for i, (idx, val) in enumerate(ticket_churn.items()):
    ax4.text(idx, val + 0.5, f'{val:.1f}%', ha='center', fontsize=9, fontweight='bold')

# -- Plot 5: LTV by Risk Tier
ax5 = axes[1, 1]
ltv_data = [df[df['risk_tier'] == t]['lifetime_value'].values for t in ['Low', 'Medium', 'High']]
bp = ax5.boxplot(ltv_data, labels=['Low Risk', 'Medium Risk', 'High Risk'],
                 patch_artist=True, notch=False)
colors_bp = [COLORS['success'], COLORS['warning'], COLORS['danger']]
for patch, color in zip(bp['boxes'], colors_bp):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax5.set_title('Customer LTV by Risk Tier', fontweight='bold', color=COLORS['primary'])
ax5.set_ylabel('Lifetime Value ($)')
ax5.set_facecolor(COLORS['light_blue'])

# -- Plot 6: Churn by Top Category
ax6 = axes[1, 2]
cat_churn = df.groupby('top_category')['churned'].mean() * 100
cat_churn = cat_churn.sort_values(ascending=True)
colors_cat = [COLORS['danger'] if v > 25 else COLORS['warning'] if v > 15 else COLORS['success']
              for v in cat_churn.values]
bars6 = ax6.barh(cat_churn.index, cat_churn.values, color=colors_cat, edgecolor='white')
ax6.set_title('Churn Rate by Product Category', fontweight='bold', color=COLORS['primary'])
ax6.set_xlabel('Churn Rate (%)')
for bar, val in zip(bars6, cat_churn.values):
    ax6.text(val + 0.3, bar.get_y() + bar.get_height()/2,
             f'{val:.1f}%', va='center', fontsize=9, fontweight='bold')
ax6.set_facecolor(COLORS['light_blue'])

plt.tight_layout()
plt.savefig('/home/claude/ba-project/analysis/charts/churn_dashboard.png',
            dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("\nChart saved: churn_dashboard.png")

# ── 3. CORRELATION ANALYSIS ──────────────────────────────────
print("\n" + "="*60)
print("KEY FINDINGS — CHURN CORRELATION ANALYSIS")
print("="*60)

numeric_cols = ['days_inactive', 'support_tickets', 'email_open_rate',
                'login_count', 'avg_order_value', 'lifetime_value']
corr = df[numeric_cols + ['churned']].corr()['churned'].drop('churned').sort_values(key=abs, ascending=False)

print("\nCorrelation of features with Churn:")
for feat, val in corr.items():
    direction = "↑ Higher = more churn" if val > 0 else "↓ Lower = more churn"
    print(f"  {feat:<25}: {val:+.3f}  ({direction})")

# ── 4. REVENUE IMPACT ──────────────────────────────────────
print("\n" + "="*60)
print("REVENUE IMPACT ANALYSIS")
print("="*60)

total_customers_real = 250000
churn_rate_current = 0.27
churn_rate_target = 0.15
avg_ltv_real = 850

churned_customers = total_customers_real * churn_rate_current
retained_if_target = total_customers_real * (churn_rate_current - churn_rate_target)
revenue_recoverable = retained_if_target * avg_ltv_real

print(f"\n  Current annual churn:    {churned_customers:,.0f} customers ({churn_rate_current*100:.0f}%)")
print(f"  Target annual churn:     {total_customers_real*churn_rate_target:,.0f} customers ({churn_rate_target*100:.0f}%)")
print(f"  Customers retained:      {retained_if_target:,.0f}")
print(f"  Avg customer LTV:        ${avg_ltv_real:,.0f}")
print(f"  ► Recoverable Revenue:   ${revenue_recoverable:,.0f}")
print(f"  ► Project Cost (Yr 1):   $125,000")
print(f"  ► Net ROI (Yr 1):        ${revenue_recoverable - 125000:,.0f} ({((revenue_recoverable-125000)/125000)*100:.0f}%)")

print("\n" + "="*60)
print("Analysis complete. See analysis/charts/ for visualizations.")
print("="*60)
