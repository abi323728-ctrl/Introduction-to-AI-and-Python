"""
Master Capstone Runner: run_capstone.py
Description: End-to-end execution script for Module 06 Final Project:
             1. Generates realistic 1,000-sample customer retention dataset
             2. Executes multi-model training and benchmarking (Logistic Regression vs Random Forest vs Gradient Boosting)
             3. Generates and saves evaluation dashboards & charts
             4. Runs real-time inference on customer risk profiles
Module: Module 06 - Final AI & ML Project
Author: Abishek J (abi323728-ctrl)
Organization: Codomax Digital Solutions
"""

import sys
import os

from dataset.generate_churn_dataset import generate_customer_churn_data
from pipeline.model_trainer import run_capstone_pipeline
from predict_cli import run_sample_evaluations

def main():
    print("=" * 80)
    print("      LAUNCHING CAPSTONE: CUSTOMER CHURN & RETENTION AI PLATFORM       ")
    print("=" * 80)
    
    # Step 1: Generate dataset
    generate_customer_churn_data()
    
    # Step 2: Run ML pipeline & save models/charts
    run_capstone_pipeline()
    
    # Step 3: Run inference engine
    run_sample_evaluations()
    
    print("\n" + "=" * 80)
    print("      ALL CAPSTONE MODULES EXECUTED & VERIFIED SUCCESSFULLY!           ")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
