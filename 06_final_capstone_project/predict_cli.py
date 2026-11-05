"""
Capstone Inference Engine: predict_cli.py
Description: Production CLI decision support system that loads the trained champion model,
             evaluates real-time customer risk, and outputs prescriptive retention recommendations.
Module: Module 06 - Final AI & ML Project
Author: Abishek J (abi323728-ctrl)
Organization: Codomax Digital Solutions
"""

import os
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = "06_final_capstone_project/models/best_churn_model.pkl"
META_PATH = "06_final_capstone_project/models/feature_metadata.pkl"

def load_inference_artifacts():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(META_PATH):
        raise FileNotFoundError("Model artifacts not found. Please run model_trainer.py first.")
    model = joblib.load(MODEL_PATH)
    features = joblib.load(META_PATH)
    return model, features

def assess_customer_risk(customer_data: dict, model, feature_names: list[str]) -> dict:
    """Takes customer attributes, shapes into feature vector, and outputs prediction with confidence."""
    # Build complete dictionary with default zeros for one-hot columns
    vector_dict = {col: 0 for col in feature_names}

    vector_dict["TenureMonths"] = customer_data.get("TenureMonths", 12)
    vector_dict["MonthlyCharges"] = customer_data.get("MonthlyCharges", 50.0)
    vector_dict["TotalCharges"] = customer_data.get("TotalCharges", vector_dict["TenureMonths"] * vector_dict["MonthlyCharges"])
    vector_dict["TechSupportTickets"] = customer_data.get("TechSupportTickets", 0)
    vector_dict["PaperlessBilling"] = int(customer_data.get("PaperlessBilling", 1))
    vector_dict["OnlineSecurity"] = int(customer_data.get("OnlineSecurity", 0))

    contract = customer_data.get("ContractType", "Month-to-Month")
    if contract == "One-Year":
        vector_dict["ContractType_One-Year"] = 1
    elif contract == "Two-Year":
        vector_dict["ContractType_Two-Year"] = 1

    payment = customer_data.get("PaymentMethod", "Electronic Check")
    if payment == "Credit Card":
        vector_dict["PaymentMethod_Credit Card"] = 1
    elif payment == "Electronic Check":
        vector_dict["PaymentMethod_Electronic Check"] = 1
    elif payment == "Mailed Check":
        vector_dict["PaymentMethod_Mailed Check"] = 1

    input_df = pd.DataFrame([vector_dict])[feature_names]
    churn_prob = model.predict_proba(input_df)[0][1]
    is_churn = int(churn_prob > 0.45)

    if churn_prob > 0.70:
        tier = "CRITICAL RISK (Immediate Intervention Required)"
        action = "Dispatch 20% annual contract discount + dedicated account manager call."
    elif churn_prob > 0.45:
        tier = "ELEVATED RISK (Monitor & Engage)"
        action = "Recommend complimentary Online Security feature upgrade."
    else:
        tier = "LOW RISK / LOYAL CUSTOMER"
        action = "Enroll in loyalty rewards program and cross-sell premium tiers."

    return {
        "churn_probability": round(float(churn_prob * 100), 1),
        "prediction": "CHURN" if is_churn else "RETAINED",
        "risk_tier": tier,
        "recommended_action": action
    }

def run_sample_evaluations():
    print("=" * 75)
    print("       AI CUSTOMER RETENTION & CHURN INFERENCE ENGINE         ")
    print("=" * 75)
    print("Author: Abishek J | Organization: Codomax Digital Solutions\n")

    model, feature_names = load_inference_artifacts()

    profiles = [
        {
            "name": "Sarah Miller (High Churn Risk Candidate)",
            "TenureMonths": 3,
            "MonthlyCharges": 98.50,
            "TotalCharges": 295.50,
            "ContractType": "Month-to-Month",
            "PaymentMethod": "Electronic Check",
            "TechSupportTickets": 4,
            "PaperlessBilling": 1,
            "OnlineSecurity": 0
        },
        {
            "name": "David Chen (Long-Term Loyal Enterprise Client)",
            "TenureMonths": 48,
            "MonthlyCharges": 65.00,
            "TotalCharges": 3120.00,
            "ContractType": "Two-Year",
            "PaymentMethod": "Credit Card",
            "TechSupportTickets": 0,
            "PaperlessBilling": 1,
            "OnlineSecurity": 1
        }
    ]

    for p in profiles:
        print(f"Customer Profile: {p['name']}")
        print(f"  • Tenure: {p['TenureMonths']} months | Spend: ${p['MonthlyCharges']}/mo | Contract: {p['ContractType']} | Support Tickets: {p['TechSupportTickets']}")
        res = assess_customer_risk(p, model, feature_names)
        print(f"  -> Prediction          : [{res['prediction']}]")
        print(f"  -> Churn Probability   : {res['churn_probability']}%")
        print(f"  -> Risk Classification : {res['risk_tier']}")
        print(f"  -> Prescriptive Action : {res['recommended_action']}\n")

    print("=" * 75 + "\n")

if __name__ == "__main__":
    run_sample_evaluations()

