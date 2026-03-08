# AS-IS Process Flow: Customer Churn Management (Current State)
## Project: ShopEase Customer Churn Reduction

---

## Overview
This document maps the **current (AS-IS) state** of how ShopEase identifies and responds to at-risk customers. This process was documented through stakeholder interviews with the Customer Success, Marketing, and Data teams conducted in Week 1 of the project.

**Process Owner:** VP Customer Experience  
**Last Updated:** March 2026  
**Version:** 1.0

---

## Current State Narrative

Currently, ShopEase has **no systematic early-warning system** for customer churn. The process relies heavily on reactive, manual steps that result in late interventions — often after the customer has already churned.

### Step-by-Step Current Process

**Step 1: Customer Becomes Inactive**
- Customer stops purchasing / engaging with the platform
- No automated detection occurs
- Inactivity period can range from 30 to 90+ days before anyone notices

**Step 2: Monthly Reporting (Manual)**
- Data Analyst pulls a manual report from the data warehouse each month
- Report identifies customers with 0 purchases in the past 30 days
- Report is emailed to the Customer Success team as a spreadsheet
- Process takes approximately 4–6 hours of analyst time per month

**Step 3: Manual Review by CSM**
- Customer Success Managers (CSMs) manually review the spreadsheet
- No scoring or prioritization exists — all inactive customers are treated equally
- CSMs have limited time; only the top ~20% of customers (by revenue) receive outreach
- 80% of churned customers receive NO proactive outreach

**Step 4: Ad-Hoc Outreach**
- CSM sends a generic email or makes a phone call
- No standardized messaging or personalization
- No tracking of whether outreach led to re-engagement
- Average response rate: 8%

**Step 5: Marketing Campaigns (Quarterly)**
- Marketing team runs a win-back campaign quarterly
- Targets all lapsed customers with a generic discount coupon
- No segmentation based on churn risk or customer value
- Campaigns are expensive (~$15K per campaign) with low ROI

**Step 6: Customer Churns**
- Most at-risk customers churn before any intervention occurs
- No post-churn analysis conducted
- No feedback loop to improve future retention efforts

---

## Process Pain Points (Identified via Stakeholder Interviews)

| # | Pain Point | Impact | Frequency |
|---|------------|--------|-----------|
| P1 | No real-time churn risk visibility | High-risk customers missed entirely | Daily |
| P2 | Manual reporting is time-consuming | 4–6 hours/month wasted | Monthly |
| P3 | No customer prioritization | Low-value customers treated same as high-value | Monthly |
| P4 | Generic outreach messages | Low response rate (8%) | Monthly |
| P5 | No campaign performance tracking | Cannot measure ROI or improve | Quarterly |
| P6 | Late detection (30–90 day lag) | Interventions come too late | Ongoing |
| P7 | No cross-department coordination | Marketing and CS work in silos | Ongoing |

---

## Swimlane: AS-IS Process

```
LANE: Customer
  [Makes last purchase] → [Becomes inactive] → [May respond to outreach] → [Churns or Returns]

LANE: Data Analyst  
  [Monthly: pulls inactivity report] → [Emails spreadsheet to CS team]

LANE: Customer Success Manager
  [Reviews spreadsheet] → [Manually selects top customers] → [Sends generic email/call]
  
LANE: Marketing Team
  [Quarterly: designs win-back campaign] → [Sends bulk discount email to all lapsed users]

LANE: System / CRM
  [No automated monitoring] → [No risk scoring] → [No triggered communications]
```

---

## Key Metrics: Current State Baseline

| Metric | Current Value |
|--------|--------------|
| Annual Churn Rate | 27% |
| Average Detection Lag | 45–60 days |
| Customers Receiving Proactive Outreach | ~20% |
| Outreach Response Rate | 8% |
| Win-Back Campaign ROI | -12% (net loss) |
| Analyst Hours Spent on Manual Reporting | ~72 hours/year |
| Estimated Annual Revenue Lost to Churn | $4.2M |

---

## Root Cause Analysis (5 Whys)

**Problem:** High customer churn rate (27%)

1. **Why?** → Customers are leaving and not being retained
2. **Why?** → Retention outreach is too late and too generic
3. **Why?** → No early warning system exists to flag at-risk customers
4. **Why?** → Customer behavior data is not being monitored in real-time
5. **Why?** → No investment has been made in churn prediction tooling or processes

**Root Cause:** Lack of a proactive, data-driven customer retention capability
