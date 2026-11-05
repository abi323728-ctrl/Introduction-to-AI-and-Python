"""
Capstone Dataset Generator: generate_churn_dataset.py
Description: Generates a realistic, 1,000-sample Customer Retention & Churn dataset
             with multi-variate features including tenure, monthly spend, contract type,
             support tickets, and churn labels.
Module: Module 06 - Final AI & ML Project
Author: Abishek J (abi323728-ctrl)
Organization: Codomax Digital Solutions
"""

import os
import random
import numpy as np
import pandas as pd

def generate_customer_churn_data(filepath: str = "06_final_capstone_project/dataset/customer_churn_data.csv", n_samples: int = 1000):
    np.random.seed(42)
    random.seed(42)

    customer_ids = [f"CUST-{20000 + i}" for i in range(1, n_samples + 1)]
    tenure_months = np.random.randint(1, 72, n_samples)
    monthly_charges = np.round(np.random.uniform(20.0, 120.0, n_samples), 2)
    total_charges = np.round(tenure_months * monthly_charges * np.random.uniform(0.95, 1.05, n_samples), 2)
    
    contract_types = np.random.choice(["Month-to-Month", "One-Year", "Two-Year"], size=n_samples, p=[0.55, 0.25, 0.20])
    payment_methods = np.random.choice(["Electronic Check", "Mailed Check", "Bank Transfer", "Credit Card"], size=n_samples)
    tech_support_tickets = np.random.poisson(lam=1.5, size=n_samples)
    paperless_billing = np.random.choice([1, 0], size=n_samples, p=[0.6, 0.4])
    online_security = np.random.choice([1, 0], size=n_samples, p=[0.5, 0.5])

    # Calculate probabilistic churn risk based on realistic business factors
    # Month-to-Month contracts, high monthly charges, high support tickets, and low tenure increase churn
    risk_score = (
        (1.2 * (contract_types == "Month-to-Month")) +
        (0.6 * (monthly_charges > 75.0)) +
        (0.8 * (tech_support_tickets >= 3)) -
        (1.5 * (tenure_months > 24)) -
        (0.5 * (online_security == 1)) +
        np.random.normal(0, 0.5, n_samples)
    )

    # Sigmoid function for probability
    churn_prob = 1.0 / (1.0 + np.exp(-risk_score))
    churn = (churn_prob > 0.45).astype(int)

    df = pd.DataFrame({
        "CustomerID": customer_ids,
        "TenureMonths": tenure_months,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "ContractType": contract_types,
        "PaymentMethod": payment_methods,
        "TechSupportTickets": tech_support_tickets,
        "PaperlessBilling": paperless_billing,
        "OnlineSecurity": online_security,
        "Churn": churn
    })

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"[+] Capstone dataset generated: {filepath} ({len(df)} samples, Churn rate: {df['Churn'].mean() * 100:.1f}%)")
    return filepath

if __name__ == "__main__":
    generate_customer_churn_data()

