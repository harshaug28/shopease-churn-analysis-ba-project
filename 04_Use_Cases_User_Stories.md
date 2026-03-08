# Use Cases & User Stories
## Project: ShopEase Customer Churn Reduction System

---

## Epic 1: Customer Risk Scoring

### User Story 1.1
**As a** Customer Success Manager,  
**I want to** see a real-time churn risk score for each customer,  
**So that** I can prioritize outreach to high-risk accounts before they leave.

**Acceptance Criteria:**
- [ ] Risk score (0–100) displayed on customer profile page
- [ ] Score updates daily based on latest behavioral data
- [ ] Color-coded indicator: Green (<30), Yellow (30–60), Red (>60)
- [ ] Score history visible for last 90 days

**Priority:** Must Have | **Story Points:** 8 | **Sprint:** 1

---

### User Story 1.2
**As a** Data Analyst,  
**I want to** access the model's feature importance breakdown,  
**So that** I can explain churn risk factors to non-technical stakeholders.

**Acceptance Criteria:**
- [ ] Top 5 contributing factors shown per customer
- [ ] Factors expressed in plain English (not model variable names)
- [ ] Exportable to PDF/Excel for stakeholder reports

**Priority:** Should Have | **Story Points:** 5 | **Sprint:** 2

---

## Epic 2: Automated Retention Campaigns

### User Story 2.1
**As a** Marketing Manager,  
**I want to** automatically trigger a retention email when a customer crosses the high-risk threshold,  
**So that** we can intervene at the right moment without manual monitoring.

**Acceptance Criteria:**
- [ ] Email triggered within 2 hours of risk score crossing 60
- [ ] Email content personalized based on customer's last purchase category
- [ ] Unsubscribe option compliant with CAN-SPAM
- [ ] Campaign results tracked in dashboard (open rate, click rate, conversion)

**Priority:** Must Have | **Story Points:** 13 | **Sprint:** 2

---

### User Story 2.2
**As a** Customer,  
**I want to** receive relevant offers based on my shopping history,  
**So that** I feel valued and am motivated to return to the platform.

**Acceptance Criteria:**
- [ ] Offer is relevant to the customer's top 3 purchase categories
- [ ] Discount is dynamically calculated (higher for higher-risk customers)
- [ ] Customer can opt out of promotional emails at any time

**Priority:** Must Have | **Story Points:** 8 | **Sprint:** 3

---

## Epic 3: Analytics Dashboard

### User Story 3.1
**As a** VP of Customer Experience,  
**I want to** view a monthly churn report with trend analysis,  
**So that** I can track progress against the 15% churn reduction target.

**Acceptance Criteria:**
- [ ] Dashboard shows current churn rate vs. target
- [ ] Month-over-month and year-over-year comparison
- [ ] Segment breakdown: new vs. returning, product category, geography
- [ ] Exportable to PowerPoint for board presentations

**Priority:** Must Have | **Story Points:** 8 | **Sprint:** 3

---

## Use Case Diagram Descriptions

### UC-01: Predict Customer Churn
- **Actor:** System (Automated)
- **Trigger:** Nightly batch job runs at 2:00 AM
- **Main Flow:**
  1. System pulls last 90 days of customer activity from data warehouse
  2. ML model scores each active customer
  3. Scores written to Customer_Risk table
  4. Dashboard refreshed
- **Exception:** If data pull fails, alert sent to Data Engineering team; previous scores retained

### UC-02: Send Retention Campaign
- **Actor:** Marketing Automation System
- **Trigger:** Customer risk score exceeds threshold (>60)
- **Main Flow:**
  1. Event triggered in marketing platform
  2. Customer segment determined (category-based)
  3. Email template selected and personalized
  4. Email sent; event logged
- **Exception:** If customer is already in active campaign, new trigger is suppressed for 14 days

### UC-03: View Customer Profile
- **Actor:** Customer Success Manager
- **Trigger:** CSM opens customer record in CRM
- **Main Flow:**
  1. CRM calls Risk Score API
  2. Risk score, history, and top risk factors displayed
  3. CSM reviews recommended actions
  4. CSM logs notes after outreach
- **Exception:** If API unavailable, show last cached score with timestamp

---

## Backlog Prioritization (MoSCoW)

| Story | Priority | Rationale |
|-------|----------|-----------|
| 1.1 Risk Score Display | Must Have | Foundation for all retention activities |
| 2.1 Auto Email Trigger | Must Have | Direct impact on churn reduction |
| 2.2 Personalized Offers | Must Have | Critical for campaign effectiveness |
| 3.1 Churn Dashboard | Must Have | Required for executive reporting |
| 1.2 Feature Importance | Should Have | Adds transparency, not blocking |
| A/B Testing Framework | Could Have | Optimization, Phase 2 |
| Mobile Push Notifications | Won't Have (v1) | Out of scope for Phase 1 |
