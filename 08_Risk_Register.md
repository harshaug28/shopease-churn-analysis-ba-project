# Risk Register
## Project: ShopEase Customer Churn Reduction System

---

**Project:** ShopEase Churn Reduction Initiative  
**Owner:** [Your Name], Business Analyst  
**Last Updated:** March 2026  
**Review Frequency:** Weekly during project; Monthly post-launch

**Risk Scoring:**  
- Likelihood: 1 (Rare) → 5 (Almost Certain)  
- Impact: 1 (Negligible) → 5 (Critical)  
- Risk Score = Likelihood × Impact  
- Rating: Low (1–6) | Medium (7–14) | High (15–19) | Critical (20–25)

---

## Risk Register Table

| ID | Risk Description | Category | Likelihood | Impact | Score | Rating | Owner | Mitigation Strategy | Contingency Plan | Status |
|----|-----------------|----------|-----------|--------|-------|--------|-------|---------------------|-----------------|--------|
| R01 | ML model accuracy below 80% AUC — too many false positives erode CSM trust | Technical | 3 | 4 | 12 | Medium | Data Science Lead | Use ensemble methods; validate on holdout set; tune threshold | Fall back to rule-based scoring (RFM model) | Open |
| R02 | Data pipeline delays exceed 15-min SLA, causing stale risk scores | Technical | 2 | 4 | 8 | Medium | Data Engineering | Implement pipeline monitoring with PagerDuty alerts; set SLA in vendor contract | Revert to nightly batch if real-time fails | Open |
| R03 | GDPR/privacy compliance issues with customer behavioral profiling | Compliance | 2 | 5 | 10 | Medium | Legal / DPO | Conduct privacy impact assessment; implement consent management; anonymize PII in ML training data | Pause campaign automation until legal review complete | Open |
| R04 | Low CSM adoption of new dashboard and process | Change Mgmt | 4 | 3 | 12 | Medium | HR / BA Lead | Early involvement of CSMs in design; gamification of adoption; dedicated training sessions | Maintain parallel old process for 4 weeks | Open |
| R05 | Integration between CRM (Salesforce) and ML system fails or is delayed | Technical | 3 | 3 | 9 | Medium | IT / Dev Team | Engage Salesforce certified developer early; use standard REST API patterns | Manual CSV import as interim workaround | Open |
| R06 | Stakeholder misalignment on churn definition (different teams use different metrics) | Business | 3 | 4 | 12 | Medium | BA / Project Sponsor | Define and document single agreed churn definition in BRD; obtain sign-off in Week 1 | Escalate to VP for arbitration | Closed ✅ |
| R07 | Email campaigns trigger spam filters, reducing delivery rate | Operational | 2 | 3 | 6 | Low | Marketing | Work with email deliverability specialist; warm up sending domain; monitor bounce rates | Switch to push notification channel | Open |
| R08 | Key subject matter expert (SME) unavailability during requirements phase | Resource | 3 | 3 | 9 | Medium | Project Manager | Identify backup SMEs; schedule interviews 2 weeks in advance; document all decisions | Use secondary interviews; review historical docs | Closed ✅ |
| R09 | Data quality issues — missing or corrupted customer behavioral data | Data | 3 | 4 | 12 | Medium | Data Engineering | Profile data before model training; establish data quality thresholds; build imputation logic | Exclude low-quality records; document data limitations | Open |
| R10 | Budget overrun due to cloud infrastructure costs | Financial | 2 | 3 | 6 | Low | Finance / PM | Get cloud cost estimates upfront; use reserved instances; set budget alerts at 80% threshold | Scale down to smaller instance types; defer non-critical features | Open |
| R11 | Competitor launches similar retention program, reducing our differentiation | Strategic | 1 | 3 | 3 | Low | Product / Strategy | Monitor competitive landscape; focus on proprietary data advantage | Accelerate Phase 2 features | Open |
| R12 | Customers perceive churn emails as intrusive, damaging brand perception | Reputational | 2 | 4 | 8 | Medium | Marketing | Test tone and frequency with focus group; include easy unsubscribe; A/B test messaging style | Pull back campaign frequency; issue customer apology | Open |

---

## Risk Heat Map

```
         IMPACT
         1    2    3    4    5
    5  |    |    |    |    |    |
L   4  |    |    | R04|    |    |
I   3  |    |    | R08| R01| R03|
K   2  |    |    | R07| R02| R09|
E   1  |    |    | R11|    |    |
L
I
H
O
O
D

  KEY: R01=Model accuracy, R02=Pipeline SLA, R03=Privacy, R04=Adoption
       R07=Spam, R08=SME availability, R09=Data quality, R11=Competition
```

---

## Top 3 Risks Deep Dive

### R03 — GDPR/Privacy Compliance (Score: 10)
**Detailed Description:** Using detailed behavioral data (browsing, purchase patterns, engagement) for ML profiling may require explicit customer consent under GDPR and PIPEDA. Failure to comply could result in regulatory fines up to 4% of annual revenue (~$2M) and reputational damage.

**Mitigation Steps:**
1. Conduct Privacy Impact Assessment (PIA) with DPO by Week 2
2. Review current privacy policy and consent language
3. Implement consent flag in customer profile
4. Use pseudonymized customer IDs in ML training data
5. Document lawful basis for processing (Legitimate Interest or Consent)

**Residual Risk after Mitigation:** Low (2 × 3 = 6)

---

### R04 — CSM Adoption (Score: 12)
**Detailed Description:** CSMs are accustomed to manual processes. New dashboard and AI-guided recommendations may face resistance, especially from senior CSMs who distrust "black box" recommendations.

**Mitigation Steps:**
1. Include 2 CSMs in the design review workshops
2. Conduct UX testing with CSMs before launch
3. Create "why this customer is at risk" explanations (explainable AI)
4. Offer certification badge for completing training
5. Track adoption rates weekly; report to VP

**Residual Risk after Mitigation:** Low (2 × 2 = 4)

---

### R01 — Model Accuracy (Score: 12)
**Detailed Description:** A poorly calibrated model that flags too many customers as high-risk will waste CSM time and erode trust in the system. Conversely, missing high-risk customers defeats the project purpose.

**Mitigation Steps:**
1. Use cross-validation and holdout test sets during model development
2. Target AUC ≥ 0.80, Precision ≥ 0.70 before production deployment
3. Build a champion-challenger testing framework
4. Conduct monthly model performance reviews
5. Define clear model retirement criteria

**Residual Risk after Mitigation:** Low (2 × 3 = 6)

---

## Risk Escalation Matrix

| Risk Score | Action Required | Escalate To |
|------------|----------------|-------------|
| 1–6 (Low) | Monitor monthly; note in status updates | BA / Project Lead |
| 7–14 (Medium) | Active mitigation plan required; review weekly | Project Sponsor |
| 15–19 (High) | Immediate mitigation; bi-weekly stakeholder update | VP Sponsor + Steering Committee |
| 20–25 (Critical) | Project pause consideration; daily updates | Executive Team |
