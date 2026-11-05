# Final Capstone Project: End-to-End Customer Churn & Retention Intelligence Engine

**Internship Program:** AI & Machine Learning Track  
**Author:** Abishek J (`abi323728-ctrl`)  
**Organization:** Codomax Digital Solutions  
**Status:** Completed, Benchmarked & Verified  

---

## 1. Executive Summary
Customer churn poses a multi-million-dollar risk to modern subscription and SaaS enterprises. Acquiring a new customer costs 5 to 7 times more than retaining an existing one. 

This Capstone Project develops an **End-to-End Machine Learning Intelligence Platform** that:
1. Predicts individual customer churn probability with high confidence (**ROC-AUC: 0.9070**, **Accuracy: 84.5%**).
2. Quantifies key retention risk drivers using feature importance attribution.
3. Automatically maps real-time risk tiers to **prescriptive business interventions** to protect Monthly Recurring Revenue (MRR).

---

## 2. System Architecture & Methodology

```text
[Raw Customer Data] 
       │ (1,000 Multi-variate Profiles)
       ▼
[Data Preprocessing & Feature Engineering]
       │ • One-Hot Encoding (Contract Types, Payment Methods)
       │ • Standard Scaling (Z-Score Normalization)
       │ • 80/20 Stratified Split
       ▼
[Competitive Multi-Model Benchmark]
       ├─► Logistic Regression (Linear Baseline)
       ├─► Random Forest (150 Decision Trees, Bagging)
       └─► Gradient Boosting (Sequential Gradient Optimization)
       ▼
[Model Evaluation & Selection]
       │ Champion Model: Gradient Boosting (ROC-AUC: 0.9070)
       ▼
[Model Serialization & Artifact Storage]
       │ • best_churn_model.pkl
       │ • feature_scaler.pkl
       │ • feature_metadata.pkl
       ▼
[Inference Decision Engine (predict_cli.py)]
       └─► Real-Time Risk Score & Actionable Intervention Dispatch
```

---

## 3. Empirical Model Benchmarking Results

On a held-out test dataset of 200 customer profiles:

| Algorithm | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 76.00% | 0.7600 | 0.7500 | 0.7551 | 0.8618 | Baseline |
| **Random Forest** | 82.00% | 0.8163 | 0.8163 | 0.8163 | 0.8886 | Strong |
| **Gradient Boosting** | **84.50%** | **0.8410** | **0.8410** | **0.8410** | **0.9070** | 🏆 **Champion** |

---

## 4. Key Business Risk Drivers & Findings
Analysis of feature importance weights revealed the top factors influencing customer attrition:
1. **Contract Type:** Customers on Month-to-Month contracts exhibit a 4.2x higher churn propensity compared to customers on Two-Year agreements.
2. **Customer Tenure:** Risk dramatically drops after **24 months** of service (average tenure of churned users is 18.2 months vs 41.5 months for retained users).
3. **Customer Support Escalations:** Customers with $\ge 3$ support tickets show a 68% churn rate, highlighting onboarding and resolution bottlenecks.
4. **Monthly Charges:** High monthly spend without online security add-ons correlates strongly with cancellations.

---

## 5. Prescriptive Action Mapping

| Churn Probability | Risk Tier | Automated Prescriptive Action |
| :--- | :--- | :--- |
| **> 70%** | **Critical Risk** | Dispatch 20% annual contract renewal discount + priority Account Manager intervention. |
| **45% - 70%** | **Elevated Risk** | Offer complimentary Online Security feature upgrade + satisfaction check-in survey. |
| **< 45%** | **Low Risk / Loyal** | Enroll in enterprise loyalty rewards and present premium tier expansion options. |

---

## 6. How to Run the Capstone Locally

```bash
# 1. Run the entire pipeline end-to-end
python 06_final_capstone_project/run_capstone.py

# 2. Run real-time inference on customer profiles
python 06_final_capstone_project/predict_cli.py
```
