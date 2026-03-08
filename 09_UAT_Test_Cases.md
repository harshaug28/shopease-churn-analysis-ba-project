# UAT Test Cases
## Project: ShopEase Customer Churn Reduction System

---

**Purpose:** Validate that the delivered system meets business requirements before go-live.  
**UAT Lead:** [Your Name], Business Analyst  
**UAT Window:** 2 weeks prior to go-live  
**Sign-off Required From:** VP Customer Experience, Marketing Manager, CSM Team Lead

**Test Result Legend:**  
✅ Pass | ❌ Fail | ⚠️ Partial Pass | 🔄 Retest Required | ⏳ Not Yet Tested

---

## Module 1: Churn Risk Scoring

| Test ID | Test Scenario | Preconditions | Test Steps | Expected Result | Priority | Result | Notes |
|---------|--------------|---------------|-----------|----------------|----------|--------|-------|
| UAT-01 | Risk score displays on customer profile | Customer record exists in CRM; model deployed | 1. Open any customer in CRM 2. Navigate to "Churn Risk" panel | Score between 0–100 displayed with color indicator (Green/Yellow/Red) | Critical | ⏳ | |
| UAT-02 | Risk score updates daily | Customer had a purchase yesterday | 1. Note current score 2. Check same customer next morning (post 8AM) | Score reflects new purchase activity; should decrease | Critical | ⏳ | |
| UAT-03 | High-risk customer correctly flagged | Customer has 0 purchases in 50 days + 3 support tickets | 1. Identify such customer in test data 2. Check their risk score | Risk score > 60 (Red) | Critical | ⏳ | |
| UAT-04 | Low-risk customer correctly scored | Customer purchased 3 days ago, 0 support tickets | 1. Identify such customer 2. Check their risk score | Risk score < 30 (Green) | High | ⏳ | |
| UAT-05 | Risk score history visible | Customer exists with 90 days of history | 1. Open customer profile 2. Click "View Score History" | Line chart showing daily scores for last 90 days | Medium | ⏳ | |
| UAT-06 | Risk factors explanation displayed | High-risk customer | 1. Open high-risk customer 2. View "Risk Factors" section | Top 5 factors shown in plain English (e.g., "No purchase in 47 days") | High | ⏳ | |

---

## Module 2: Automated Retention Campaigns

| Test ID | Test Scenario | Preconditions | Test Steps | Expected Result | Priority | Result | Notes |
|---------|--------------|---------------|-----------|----------------|----------|--------|-------|
| UAT-07 | Email triggered when score crosses 60 | Test customer below threshold | 1. In test environment, manually set customer risk score from 55 to 65 2. Wait up to 2 hours | Retention email received in test inbox within 2 hours | Critical | ⏳ | |
| UAT-08 | Email content is personalized | Customer's top category is "Electronics" | 1. Trigger email for electronics customer | Email mentions electronics; offer is electronics-related | Critical | ⏳ | |
| UAT-09 | No duplicate emails sent | Customer already in active campaign | 1. Trigger second campaign for same customer within 14 days | Second email NOT sent; suppression confirmed in logs | High | ⏳ | |
| UAT-10 | Unsubscribe link works | Customer receives retention email | 1. Click unsubscribe link in email 2. Check marketing platform | Customer marked as unsubscribed; no further emails sent | Critical | ⏳ | Legal/compliance |
| UAT-11 | Campaign event logged | Email sent successfully | 1. Check campaign log after email send | Event logged with: customer ID, timestamp, template used, score at trigger | Medium | ⏳ | |
| UAT-12 | Email renders correctly on mobile | — | 1. Open email on iOS + Android test devices | Email displays correctly; no layout breaks; CTA button clickable | High | ⏳ | |

---

## Module 3: CSM Dashboard

| Test ID | Test Scenario | Preconditions | Test Steps | Expected Result | Priority | Result | Notes |
|---------|--------------|---------------|-----------|----------------|----------|--------|-------|
| UAT-13 | At-risk customer list loads on login | CSM logs in to CRM | 1. Log in as CSM user | "At-Risk Customers" list loads within 5 seconds | Critical | ⏳ | |
| UAT-14 | Customers sorted by risk × revenue | Mix of high/low risk and high/low revenue customers | 1. View at-risk list | Customers with highest (risk × revenue) product appear at top | High | ⏳ | |
| UAT-15 | AI talking-point recommendation displays | High-risk customer in list | 1. Click on high-risk customer 2. View "Recommended Approach" section | Contextual talking points based on that customer's specific risk factors | High | ⏳ | |
| UAT-16 | CSM can log outreach outcome | CSM has contacted a customer | 1. Open customer 2. Click "Log Outreach" 3. Select: Retained / Churned / No Response | Outcome saved with timestamp; status updates in list | High | ⏳ | |
| UAT-17 | Dashboard performance (load time) | 500+ customers in at-risk list | 1. Load dashboard as CSM | Dashboard fully loads within 5 seconds | Medium | ⏳ | Performance |

---

## Module 4: Leadership Analytics Dashboard

| Test ID | Test Scenario | Preconditions | Test Steps | Expected Result | Priority | Result | Notes |
|---------|--------------|---------------|-----------|----------------|----------|--------|-------|
| UAT-18 | Current churn rate displayed correctly | Real churn data in system | 1. Open executive dashboard | Churn rate matches independently calculated figure (±0.1%) | Critical | ⏳ | |
| UAT-19 | Month-over-month trend chart | 3+ months of data | 1. View trend chart on dashboard | Bar/line chart shows correct MoM % change | High | ⏳ | |
| UAT-20 | Export to PowerPoint works | Dashboard loaded with data | 1. Click "Export to PPT" button | PowerPoint file downloads with all charts and current KPI values | Medium | ⏳ | |
| UAT-21 | Dashboard access control | Non-exec users | 1. Log in as CSM 2. Try to access executive dashboard URL | Access denied; redirect to CSM dashboard | High | ⏳ | Security |

---

## UAT Entry & Exit Criteria

### Entry Criteria (UAT can begin when:)
- [ ] All critical and high-priority functional requirements deployed to UAT environment
- [ ] Test data loaded (min. 1,000 customer records with varied risk profiles)
- [ ] UAT test environment confirmed stable (no deployments during UAT window)
- [ ] All UAT participants identified and available
- [ ] Test accounts created for: CSM role, Marketing role, Executive role

### Exit Criteria (UAT is complete when:)
- [ ] 100% of Critical tests: Pass
- [ ] ≥ 95% of High tests: Pass
- [ ] ≥ 85% of Medium tests: Pass or accepted workaround documented
- [ ] Zero open Severity 1 (showstopper) defects
- [ ] All stakeholder sign-off signatures obtained

---

## Defect Severity Definitions

| Severity | Definition | Example | Response Time |
|----------|-----------|---------|--------------|
| S1 - Critical | System unusable; no workaround | Login fails for all users | Fix within 4 hours |
| S2 - High | Major feature broken; workaround exists | Risk score doesn't display but CSV export works | Fix before go-live |
| S3 - Medium | Feature impaired; workaround easy | Chart renders slowly | Fix within 2 weeks of go-live |
| S4 - Low | Minor cosmetic issue | Button misaligned by 2px | Backlog for next release |

---

## Sign-Off Sheet

| Stakeholder | Role | Signature | Date | Decision |
|------------|------|-----------|------|----------|
| [Name] | VP Customer Experience | | | ☐ Approved ☐ Conditional ☐ Rejected |
| [Name] | Marketing Manager | | | ☐ Approved ☐ Conditional ☐ Rejected |
| [Name] | CSM Team Lead | | | ☐ Approved ☐ Conditional ☐ Rejected |
| [Name] | IT/Dev Lead | | | ☐ Approved ☐ Conditional ☐ Rejected |
