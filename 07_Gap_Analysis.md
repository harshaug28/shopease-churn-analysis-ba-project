# Gap Analysis
## Project: ShopEase Customer Churn Reduction System

---

**Purpose:** Identify gaps between the current (AS-IS) state and the desired (TO-BE) state, and define the actions required to close those gaps.

**Analyst:** [Your Name]  
**Date:** March 2026

---

## Gap Analysis Summary Table

| # | Capability Area | AS-IS State | TO-BE State | Gap | Priority | Action Required |
|---|----------------|-------------|-------------|-----|----------|----------------|
| G1 | Churn Detection | Manual, monthly, 45-day lag | Automated, daily, <24hr | No real-time monitoring | Critical | Implement ML scoring pipeline |
| G2 | Data Pipeline | Batch SQL pulls by analyst | Real-time streaming | No event streaming infrastructure | Critical | Build Kafka/Kinesis data pipeline |
| G3 | Customer Risk Scoring | None | ML model scoring 0–100 | No scoring model exists | Critical | Develop & deploy churn ML model |
| G4 | Campaign Personalization | Generic bulk emails | Behavior-based personalization | No personalization engine | High | Integrate customer segments into marketing platform |
| G5 | CRM Integration | Manual spreadsheet updates | Real-time API-driven updates | No CRM-to-model integration | High | Build Salesforce API integration |
| G6 | CSM Tooling | Unfiltered spreadsheet list | Prioritized dashboard with AI guidance | No prioritization or guidance tool | High | Build CSM at-risk dashboard |
| G7 | Campaign Tracking | None | Real-time performance dashboard | No campaign analytics | Medium | Implement marketing analytics layer |
| G8 | Model Governance | N/A | Monthly retraining + drift monitoring | No ML ops process | Medium | Define MLOps workflow |
| G9 | Cross-Team Coordination | Siloed teams | Unified churn KPI dashboard | No shared visibility | Medium | Create unified leadership dashboard |
| G10 | Change Management | N/A | CSM training on new tools | No training program exists | Low | Develop training materials |

---

## Detailed Gap Analysis

### G1: Churn Detection Speed

**Current State:**  
Customer inactivity is detected only when a Data Analyst manually runs a monthly report. By the time the report is reviewed and outreach occurs, customers have been inactive for 45–60 days. At this stage, over 60% of these customers have already made their next purchase elsewhere.

**Desired State:**  
Customers show risk signals within 7–14 days of behavioral changes. The system detects these signals within 24 hours and initiates intervention.

**Gap:**  
45-day detection lag vs. target <24 hours. This is a 98% gap in detection speed.

**Actions to Close:**
- Implement real-time behavioral event streaming (G2)
- Deploy nightly ML scoring batch job
- Set alert threshold at risk score > 60

---

### G2: Data Pipeline Infrastructure

**Current State:**  
All data analysis requires a data analyst to manually query the production database. There is no data warehouse, no streaming pipeline, and no automated refresh.

**Desired State:**  
Customer events (purchases, logins, support tickets, etc.) are streamed to a data warehouse in near real-time (<15 minutes). The warehouse serves as the single source of truth for all analytics and ML workloads.

**Gap:**  
No data infrastructure exists beyond the operational database.

**Actions to Close:**
- Design and implement data warehouse schema (AWS Redshift or Snowflake recommended)
- Set up event streaming from application layer (Kafka or AWS Kinesis)
- Establish data quality checks and SLAs

---

### G3: Machine Learning Churn Model

**Current State:**  
No predictive model exists. The company has no way to assess the probability of a specific customer churning.

**Desired State:**  
A trained ML classification model (Random Forest or XGBoost recommended) predicts churn probability for each customer daily. Model AUC ≥ 0.80.

**Gap:**  
No model, no training data pipeline, no deployment infrastructure.

**Actions to Close:**
- Source 24+ months of historical churn data for model training
- Define feature set (days since purchase, frequency, support tickets, email engagement)
- Train, validate, and test model
- Deploy model to production scoring environment
- Establish retraining schedule (monthly)

---

### G4 & G5: Personalization & CRM Integration

**Current State:**  
Marketing sends quarterly bulk emails. CRM (Salesforce) contains customer data but is not connected to any behavioral analytics.

**Desired State:**  
CRM displays real-time churn score. Marketing campaigns are automatically personalized using customer's purchase history and risk profile.

**Gap:**  
No API integration between ML system, CRM, and marketing platform.

**Actions to Close:**
- Build REST API to expose churn scores
- Develop Salesforce custom fields for risk score display
- Integrate HubSpot with customer segmentation data
- Build personalization logic (segment → template mapping)

---

## Capability Maturity Assessment

| Capability | Current Maturity | Target Maturity | Gap (Levels) |
|------------|-----------------|-----------------|-------------|
| Data Management | Level 1 (Ad-hoc) | Level 3 (Defined) | +2 |
| Analytics | Level 1 (Ad-hoc) | Level 4 (Managed) | +3 |
| Customer Segmentation | Level 2 (Repeatable) | Level 4 (Managed) | +2 |
| Campaign Management | Level 2 (Repeatable) | Level 3 (Defined) | +1 |
| ML/AI Capability | Level 0 (None) | Level 3 (Defined) | +3 |

*Maturity Scale: 0=None, 1=Ad-hoc, 2=Repeatable, 3=Defined, 4=Managed, 5=Optimized*

---

## Recommended Closure Roadmap

**Phase 1 (Weeks 1–4): Foundation**
- Set up data warehouse and streaming pipeline (G2)
- Define ML feature set and collect training data (G3)

**Phase 2 (Weeks 5–8): Core Build**
- Train and deploy churn prediction model (G3)
- Build CRM integration and CSM dashboard (G5, G6)

**Phase 3 (Weeks 9–12): Activation**
- Activate automated campaigns with personalization (G4)
- Launch leadership dashboard (G9)
- Begin CSM training (G10)

**Phase 4 (Weeks 13–16): Optimize**
- Set up model monitoring and drift detection (G8)
- Run first A/B test on campaign variants
- Review vs. baseline KPIs
