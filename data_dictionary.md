# Data Dictionary
## Project: ShopEase Customer Churn Reduction System

---

**Source Systems:** Order Management System (OMS), CRM (Salesforce), Support Ticketing (Zendesk), Email Platform (HubSpot)  
**Last Updated:** March 2026  
**Owner:** Data Engineering Team

---

## Table: customer_profile

| Field Name | Data Type | Description | Example | Source | Notes |
|------------|-----------|-------------|---------|--------|-------|
| customer_id | VARCHAR(36) | Unique customer identifier (UUID) | cust_a1b2c3d4 | OMS | Primary key; never null |
| signup_date | DATE | Date customer created account | 2023-04-15 | OMS | |
| customer_segment | VARCHAR(20) | Customer tier: Premium, Standard, Basic | Premium | CRM | Recalculated quarterly |
| country | VARCHAR(2) | ISO 2-letter country code | CA | OMS | |
| email_opt_in | BOOLEAN | Has consented to marketing emails | true | HubSpot | GDPR consent flag |
| lifetime_value | DECIMAL(10,2) | Total revenue from customer (USD) | 1254.50 | OMS | Running total |

---

## Table: customer_behavior (90-day rolling window)

| Field Name | Data Type | Description | Example | Source | Notes |
|------------|-----------|-------------|---------|--------|-------|
| customer_id | VARCHAR(36) | Foreign key to customer_profile | cust_a1b2c3d4 | OMS | |
| days_since_last_purchase | INT | Days since most recent order | 23 | OMS | Key churn feature |
| purchase_count_90d | INT | Number of orders in last 90 days | 4 | OMS | |
| avg_order_value_90d | DECIMAL(8,2) | Average order value last 90 days | 87.50 | OMS | |
| top_category | VARCHAR(50) | Most purchased product category | Electronics | OMS | Used for personalization |
| support_tickets_90d | INT | Number of support tickets opened | 2 | Zendesk | High correlation with churn |
| email_open_rate_90d | DECIMAL(5,4) | % of emails opened in last 90 days | 0.2300 | HubSpot | 0.0000 to 1.0000 |
| email_click_rate_90d | DECIMAL(5,4) | % of email links clicked | 0.0750 | HubSpot | |
| login_count_90d | INT | Number of platform logins | 12 | OMS | |
| browse_to_purchase_rate | DECIMAL(5,4) | Sessions resulting in purchase | 0.1500 | OMS | |

---

## Table: churn_risk_scores

| Field Name | Data Type | Description | Example | Source | Notes |
|------------|-----------|-------------|---------|--------|-------|
| customer_id | VARCHAR(36) | Foreign key to customer_profile | cust_a1b2c3d4 | ML System | |
| score_date | DATE | Date score was generated | 2026-03-08 | ML System | One record per customer per day |
| risk_score | INT | Churn probability score (0–100) | 73 | ML System | Higher = more at risk |
| risk_tier | VARCHAR(10) | Derived label: Low/Medium/High | High | ML System | High if score > 60 |
| top_factor_1 | VARCHAR(100) | #1 contributing risk factor | No purchase in 47 days | ML System | Plain English explanation |
| top_factor_2 | VARCHAR(100) | #2 contributing risk factor | 3 unresolved support tickets | ML System | |
| top_factor_3 | VARCHAR(100) | #3 contributing risk factor | Email open rate dropped 80% | ML System | |
| model_version | VARCHAR(10) | ML model version that generated score | v2.1 | ML System | For audit/debugging |

---

## Table: churn_events (ground truth)

| Field Name | Data Type | Description | Example | Source | Notes |
|------------|-----------|-------------|---------|--------|-------|
| customer_id | VARCHAR(36) | Foreign key | cust_a1b2c3d4 | OMS | |
| churn_date | DATE | Date customer officially churned | 2025-11-15 | OMS | |
| churn_definition | VARCHAR(50) | How churn was defined | 90-day no purchase | Business Rules | |
| retention_attempted | BOOLEAN | Was outreach attempted before churn | true | CRM | |
| win_back_date | DATE | If re-acquired, date of return | 2026-01-03 | OMS | NULL if not returned |

---

## Churn Definition (Official)

> A customer is considered **churned** if they have made **zero purchases in the past 90 consecutive days** AND have not responded to any retention outreach in that period.

*This definition was agreed upon by the VP Customer Experience, Head of Analytics, and Marketing Director on 2026-02-14. All metrics in this project use this definition.*

---

## Feature Engineering Notes

The following derived features are calculated from raw data before being fed into the ML model:

| Feature | Formula | Rationale |
|---------|---------|-----------|
| purchase_velocity_trend | (purchases_last_30d / purchases_30-60d_ago) | Captures acceleration/deceleration of purchase behavior |
| support_ticket_severity_score | Avg severity of tickets (1=low, 3=high) × count | High-severity tickets are stronger churn predictors |
| engagement_score | (email_open_rate × 0.4) + (login_frequency × 0.3) + (browse_to_purchase × 0.3) | Composite engagement metric |
| rfm_score | Recency (35%) + Frequency (35%) + Monetary (30%) | Classic RFM model for baseline comparison |
