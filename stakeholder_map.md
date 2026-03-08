# Stakeholder Map
## ShopEase Churn Reduction Initiative

---

## Stakeholder Influence-Interest Grid

```
HIGH INFLUENCE
     │
     │   KEEP SATISFIED          MANAGE CLOSELY
     │   ─────────────────────   ─────────────────────
     │   • DPO (Legal/Privacy)   • VP Customer Experience ★
     │   • CTO / IT Lead         • Head of Data Science ★
     │   • CFO (Budget approval) • Marketing Manager ★
     │                           • CSM Team Lead ★
─────┼─────────────────────────────────────────────────── HIGH INTEREST
     │
     │   MONITOR                 KEEP INFORMED
     │   ─────────────────────   ─────────────────────
     │   • Board / Executives    • CSM Frontline Staff
     │   • HR (Change Mgmt)      • Data Analyst Team
     │                           • Customer (end beneficiary)
LOW  │
INFLUENCE

★ = Primary stakeholders; must be actively managed throughout project
```

---

## Stakeholder Register

| Stakeholder | Role | Interest Level | Influence | Engagement Strategy | Communication |
|------------|------|---------------|-----------|--------------------|----|
| VP Customer Experience | Executive Sponsor | High | High | Weekly status updates, sign-off gatekeeper | Weekly 1:1 + steering committee |
| Head of Data Science | Technical Lead | High | High | Collaborative — co-design ML architecture | Daily during build phase |
| Marketing Manager | Campaign Owner | High | High | Workshop involvement, UAT participation | Bi-weekly + milestone reviews |
| CSM Team Lead | End User Rep | High | Medium | Design sessions, UAT lead, change champion | Weekly during design/test |
| IT/Dev Lead | Integration Owner | Medium | High | Technical specs review, API contract sign-off | Weekly during build |
| DPO (Privacy) | Compliance | Medium | High | Privacy Impact Assessment engagement | Milestone checkpoints |
| Frontline CSMs | End Users | High | Low | Training, feedback surveys, pilot group | Training sessions + FAQ |
| CFO | Budget Holder | Low | High | Business case presentation, ROI updates | Monthly executive report |

---

# Swimlane Process Diagram (BPMN-Style Text)
## Future State (TO-BE) Customer Retention Process

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  LANE: CUSTOMER                                                                  │
│  [Browses/Purchases] ──→ [Becomes Inactive] ──→ [Receives Email] ──→ [Returns?] │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  LANE: DATA PIPELINE (AUTOMATED)                                                 │
│  [Purchase/Support/Email Events] ──→ [Kafka Stream] ──→ [Redshift DW] ──→       │
│  [Nightly 90-day Aggregate Job]                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  LANE: ML SCORING ENGINE (NIGHTLY 2AM)                                          │
│  [Read customer_behavior table] ──→ [Run XGBoost model] ──→                     │
│  [Write scores to churn_risk_scores] ──→ [Log performance metrics]              │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  LANE: CAMPAIGN AUTOMATION (EVENT-DRIVEN)                                        │
│  [Score > 60?] ──YES──→ [In suppression window?] ──NO──→                        │
│  [Select template by category] ──→ [Calculate dynamic discount] ──→             │
│  [Send personalized email via HubSpot] ──→ [Log event + track engagement]       │
│              └──YES──→ [Suppress; log]                                           │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  LANE: CUSTOMER SUCCESS MANAGER (GUIDED MANUAL)                                 │
│  [Open CSM Dashboard (8AM)] ──→ [View prioritized at-risk list]                 │
│  ──→ [Select customer] ──→ [Review AI talking points]                           │
│  ──→ [Contact customer] ──→ [Log outcome in CRM]                                │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  LANE: ANALYTICS / REPORTING (AUTOMATED)                                        │
│  [Daily: refresh executive dashboard] ──→                                        │
│  [Monthly: auto-generate churn report] ──→ [Email to leadership]                │
│  [Monthly: retrain ML model] ──→ [Validate AUC] ──→ [Deploy or alert]          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

# Data Flow Diagram (DFD)

## Level 0 — Context Diagram

```
                    ┌────────────────────────────────────┐
    Customer ──────▶│                                    │──────▶ Customer
  (behavior data)   │   ShopEase Churn Prevention        │  (retention email/offer)
                    │         Platform                   │
     CSM ──────────▶│                                    │──────▶ CSM
  (outreach log)    │                                    │  (prioritized list + tips)
                    │                                    │
  Executive ───────▶│                                    │──────▶ Executive
  (KPI review)      │                                    │  (churn dashboard + report)
                    └────────────────────────────────────┘
```

## Level 1 — Sub-Process DFD

```
[External: OMS/Zendesk/HubSpot]
        │
        ▼
   [P1: Collect Behavioral Events] ──▶ {DS1: event_raw}
        │
        ▼
   [P2: Compute Aggregates] ──▶ {DS2: customer_behavior}
        │
        ▼
   [P3: Score Churn Risk] ──▶ {DS3: churn_risk_scores}
       │ │
       │ └──▶ [P4: Trigger Campaigns] ──▶ {DS4: campaign_events} ──▶ [External: Customer]
       │
       └──▶ [P5: Support CSM] ──▶ {DS5: outreach_log} ──▶ [External: CSM]

{DS1–DS5} ──▶ [P6: Generate Analytics] ──▶ [External: Executive Dashboard]
```
