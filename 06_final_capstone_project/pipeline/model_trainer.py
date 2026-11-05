"""
Capstone Pipeline: model_trainer.py
Description: End-to-end Machine Learning pipeline that performs data preprocessing,
             trains multiple benchmark models, evaluates performance, serializes the champion model,
             and generates comprehensive visual analytics.
Module: Module 06 - Final AI & ML Project
Author: Abishek J (abi323728-ctrl)
Organization: Codomax Digital Solutions
"""

import os
import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_FILE = "06_final_capstone_project/dataset/customer_churn_data.csv"
MODELS_DIR = "06_final_capstone_project/models"
CHARTS_DIR = "06_final_capstone_project/charts"

def run_capstone_pipeline():
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(CHARTS_DIR, exist_ok=True)

    print("=" * 80)
    print("      CAPSTONE PROJECT: CUSTOMER CHURN & RETENTION INTELLIGENCE SYSTEM      ")
    print("=" * 80)
    print("Author: Abishek J | Organization: Codomax Digital Solutions\n")

    # 1. Load Dataset
    df = pd.read_csv(DATA_FILE)
    print(f"--- 1. Data Ingestion & Shape ---")
    print(f"Loaded {len(df)} records across {df.shape[1]} features.")
    print(df.head())

    # 2. Data Preprocessing & Feature Engineering
    print("\n--- 2. Feature Engineering & Encoding ---")
    # One-hot encode categorical features
    df_encoded = pd.get_dummies(df, columns=["ContractType", "PaymentMethod"], drop_first=True)
    
    # Feature matrix X and target y
    feature_cols = [c for c in df_encoded.columns if c not in ["CustomerID", "Churn"]]
    X = df_encoded[feature_cols]
    y = df_encoded["Churn"]

    print(f"Features prepared ({len(feature_cols)} total): {feature_cols}")

    # 3. Train/Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training split: {X_train.shape[0]} samples | Testing split: {X_test.shape[0]} samples")

    # 4. Feature Standardization
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Model Training & Multi-Algorithm Benchmark
    print("\n--- 3. Multi-Algorithm Competitive Benchmark ---")
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=8, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)
    }

    results = {}
    fitted_models = {}

    for name, model in models.items():
        if name == "Logistic Regression":
            model.fit(X_train_scaled, y_train)
            preds = model.predict(X_test_scaled)
            probs = model.predict_proba(X_test_scaled)[:, 1]
        else:
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            probs = model.predict_proba(X_test)[:, 1]

        acc = accuracy_score(y_test, preds)
        prec = precision_score(y_test, preds)
        rec = recall_score(y_test, preds)
        f1 = f1_score(y_test, preds)
        auc = roc_auc_score(y_test, probs)

        results[name] = {
            "Accuracy": acc,
            "Precision": prec,
            "Recall": rec,
            "F1-Score": f1,
            "ROC-AUC": auc,
            "Predictions": preds,
            "Probabilities": probs
        }
        fitted_models[name] = model

        print(f"[{name:<20}] Accuracy: {acc*100:.2f}% | F1: {f1:.4f} | ROC-AUC: {auc:.4f}")

    # Identify Champion Model
    best_model_name = max(results, key=lambda k: results[k]["ROC-AUC"])
    champion_model = fitted_models[best_model_name]
    champion_stats = results[best_model_name]

    print(f"\n🏆 Champion Model Selected: {best_model_name} (ROC-AUC: {champion_stats['ROC-AUC']:.4f})")

    # 6. Model Serialization
    model_save_path = os.path.join(MODELS_DIR, "best_churn_model.pkl")
    scaler_save_path = os.path.join(MODELS_DIR, "feature_scaler.pkl")
    feature_meta_path = os.path.join(MODELS_DIR, "feature_metadata.pkl")

    joblib.dump(champion_model, model_save_path)
    joblib.dump(scaler, scaler_save_path)
    joblib.dump(feature_cols, feature_meta_path)
    print(f"[+] Serialized champion model saved to: {model_save_path}")

    # -------------------------------------------------------------
    # 7. Generate Visualizations & Dashboards
    # -------------------------------------------------------------
    print("\n--- 4. Generating Executive Visualizations ---")

    # Figure 1: Churn Demographics Breakdown
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    churn_counts = df["Churn"].value_counts()
    ax1.pie(churn_counts, labels=["Retained (Active)", "Churned"], autopct="%1.1f%%",
            colors=["#5cb85c", "#d9534f"], explode=(0.04, 0), startangle=140, shadow=True)
    ax1.set_title("Customer Churn Distribution", fontweight="bold", fontsize=12)

    # Tenure vs Churn
    tenure_churn = df.groupby("Churn")["TenureMonths"].mean()
    ax2.bar(["Retained", "Churned"], tenure_churn, color=["#5cb85c", "#d9534f"], edgecolor="black", alpha=0.85)
    ax2.set_title("Average Tenure Months by Churn Status", fontweight="bold", fontsize=12)
    ax2.set_ylabel("Average Tenure (Months)")
    for i, v in enumerate(tenure_churn):
        ax2.text(i, v + 1, f"{v:.1f} mo", ha="center", fontweight="bold")
    ax2.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    f1_path = os.path.join(CHARTS_DIR, "01_churn_distribution.png")
    plt.savefig(f1_path, dpi=300)
    plt.close()
    print(f"  [+] Saved: {f1_path}")

    # Figure 2: Model Benchmark Comparison Chart
    plt.figure(figsize=(10, 5))
    metrics_to_plot = ["Accuracy", "Precision", "Recall", "ROC-AUC"]
    x = np.arange(len(metrics_to_plot))
    width = 0.25

    for idx, (m_name, m_data) in enumerate(results.items()):
        vals = [m_data[m] for m in metrics_to_plot]
        plt.bar(x + (idx * width), vals, width, label=m_name, edgecolor="black", alpha=0.85)

    plt.xticks(x + width, metrics_to_plot, fontweight="bold")
    plt.ylabel("Score (0.0 to 1.0)", fontweight="bold")
    plt.ylim(0, 1.1)
    plt.title("Competitive Model Evaluation Benchmark", fontsize=14, fontweight="bold", pad=12)
    plt.legend(loc="lower right")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    f2_path = os.path.join(CHARTS_DIR, "02_model_comparison_benchmark.png")
    plt.savefig(f2_path, dpi=300)
    plt.close()
    print(f"  [+] Saved: {f2_path}")

    # Figure 3: Confusion Matrix & ROC Curve of Champion Model
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    ConfusionMatrixDisplay.from_predictions(
        y_test, champion_stats["Predictions"],
        display_labels=["Retained", "Churned"],
        cmap="Blues", ax=ax1
    )
    ax1.set_title(f"Confusion Matrix: {best_model_name}", fontweight="bold", fontsize=12)
    ax1.grid(False)

    RocCurveDisplay.from_predictions(
        y_test, champion_stats["Probabilities"],
        name=best_model_name, ax=ax2
    )
    ax2.plot([0, 1], [0, 1], "k--", label="Random Chance (AUC = 0.50)")
    ax2.set_title("Receiver Operating Characteristic (ROC) Curve", fontweight="bold", fontsize=12)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend()
    plt.tight_layout()
    f3_path = os.path.join(CHARTS_DIR, "03_confusion_matrix_and_roc_curve.png")
    plt.savefig(f3_path, dpi=300)
    plt.close()
    print(f"  [+] Saved: {f3_path}")

    # Figure 4: Feature Importance (if tree-based)
    if hasattr(champion_model, "feature_importances_"):
        plt.figure(figsize=(10, 5))
        importances = champion_model.feature_importances_
        idx_sorted = np.argsort(importances)[::-1][:8] # Top 8 features
        plt.barh([feature_cols[i] for i in idx_sorted][::-1], importances[idx_sorted][::-1], color="#337ab7", edgecolor="black")
        plt.title(f"Top Churn Risk Drivers ({best_model_name})", fontweight="bold", fontsize=14, pad=12)
        plt.xlabel("Relative Feature Importance Weight", fontweight="bold")
        plt.grid(axis="x", linestyle="--", alpha=0.6)
        plt.tight_layout()
        f4_path = os.path.join(CHARTS_DIR, "04_churn_risk_drivers.png")
        plt.savefig(f4_path, dpi=300)
        plt.close()
        print(f"  [+] Saved: {f4_path}")

    print("\n" + "=" * 80)
    print("      CAPSTONE TRAINING & BENCHMARKING PIPELINE COMPLETE!      ")
    print("=" * 80 + "\n")
    return champion_stats

if __name__ == "__main__":
    run_capstone_pipeline()
