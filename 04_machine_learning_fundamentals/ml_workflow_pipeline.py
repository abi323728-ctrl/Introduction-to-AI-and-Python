"""
Module 04: Machine Learning Fundamentals Pipeline
Description: Demonstrates the end-to-end Machine Learning workflow using Scikit-learn:
             1. Problem Formulation & Data Ingestion (Iris Flower Classification + Student Score Regression)
             2. Train/Test Splitting & Feature Standardization
             3. Model Training (KNN, Random Forest, Linear Regression)
             4. Model Evaluation (Accuracy, Precision, Recall, F1, Confusion Matrix, MSE, R2 Score)
             5. Inference on unseen custom test samples
Module: Module 04 - Machine Learning Fundamentals
Author: Abishek J (abi323728-ctrl)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

CHARTS_DIR = "04_machine_learning_fundamentals/charts"

def run_classification_workflow():
    print("\n" + "=" * 75)
    print("      PART 1: IRIS FLOWER CLASSIFICATION (SUPERVISED LEARNING)      ")
    print("=" * 75)

    # 1. Load Dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    df = pd.DataFrame(X, columns=feature_names)
    df["Species"] = [target_names[i] for i in y]

    print("\n--- Step 1: Dataset Exploration ---")
    print(f"Features: {feature_names}")
    print(f"Target Classes: {list(target_names)}")
    print(f"Dataset Dimensions: {df.shape[0]} samples, {df.shape[1]} columns")
    print("\nSample Data:")
    print(df.head())

    # 2. Train / Test Split (80% Training, 20% Testing)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n--- Step 2: Train/Test Split ---")
    print(f"Training Samples: {X_train.shape[0]} | Testing Samples: {X_test.shape[0]}")

    # 3. Feature Scaling (Standardization)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Model Training: K-Nearest Neighbors & Random Forest
    print("\n--- Step 3: Model Training ---")
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train_scaled, y_train)

    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    print("[+] Trained K-Nearest Neighbors Classifier (k=5)")
    print("[+] Trained Random Forest Classifier (100 Trees)")

    # 5. Model Evaluation
    print("\n--- Step 4: Model Evaluation ---")
    y_pred_knn = knn_model.predict(X_test_scaled)
    acc_knn = accuracy_score(y_test, y_pred_knn)
    print(f"KNN Test Accuracy: {acc_knn * 100:.2f}%")

    y_pred_rf = rf_model.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    print(f"Random Forest Test Accuracy: {acc_rf * 100:.2f}%")

    print("\nClassification Report (Random Forest):")
    print(classification_report(y_test, y_pred_rf, target_names=target_names))

    # 6. Confusion Matrix Visualization using sklearn's ConfusionMatrixDisplay
    plt.figure(figsize=(7, 5))
    disp = ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred_rf,
        display_labels=target_names,
        cmap="Blues",
        colorbar=True
    )
    disp.ax_.set_title("Confusion Matrix: Iris Flower Classification", fontsize=13, fontweight="bold", pad=12)
    plt.tight_layout()
    cm_path = os.path.join(CHARTS_DIR, "01_iris_confusion_matrix.png")
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"[+] Saved Confusion Matrix Chart: {cm_path}")

    # 7. Feature Importance Visualization
    importances = rf_model.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(8, 4))
    plt.bar([feature_names[i] for i in indices], importances[indices], color="#2b5c8f", edgecolor="black", alpha=0.85)
    plt.title("Random Forest Feature Importances", fontsize=13, fontweight="bold", pad=12)
    plt.ylabel("Importance Weight", fontweight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    fi_path = os.path.join(CHARTS_DIR, "02_iris_feature_importance.png")
    plt.savefig(fi_path, dpi=300)
    plt.close()
    print(f"[+] Saved Feature Importance Chart: {fi_path}")

    # 8. Inference on Unseen Custom Flower
    new_flower = [[5.1, 3.5, 1.4, 0.2]] # Classic Setosa dimensions
    scaled_new = scaler.transform(new_flower)
    predicted_class = knn_model.predict(scaled_new)[0]
    probabilities = knn_model.predict_proba(scaled_new)[0]

    print("\n--- Step 5: Real-World Inference on Unseen Data ---")
    print(f"Input Measurements: {new_flower[0]}")
    print(f"Predicted Species : {target_names[predicted_class].upper()}")
    print(f"Prediction Confidence: {probabilities[predicted_class] * 100:.1f}%")

def run_regression_workflow():
    print("\n" + "=" * 75)
    print("      PART 2: STUDENT SCORE PREDICTION (REGRESSION WORKFLOW)        ")
    print("=" * 75)

    # Synthetic realistic student study hours vs exam score dataset
    np.random.seed(42)
    study_hours = np.random.uniform(1.0, 10.0, 60)
    attendance_pct = np.random.uniform(60.0, 100.0, 60)
    # Target Exam Score = 15 + (6.5 * Hours) + (0.2 * Attendance) + noise
    noise = np.random.normal(0, 3.5, 60)
    exam_score = np.clip(15 + (6.5 * study_hours) + (0.2 * attendance_pct) + noise, 0, 100)

    reg_df = pd.DataFrame({
        "StudyHours": study_hours,
        "Attendance": attendance_pct,
        "ExamScore": exam_score
    })

    X_reg = reg_df[["StudyHours", "Attendance"]]
    y_reg = reg_df["ExamScore"]

    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
        X_reg, y_reg, test_size=0.25, random_state=42
    )

    lin_reg = LinearRegression()
    lin_reg.fit(X_train_r, y_train_r)

    y_pred_r = lin_reg.predict(X_test_r)
    mse = mean_squared_error(y_test_r, y_pred_r)
    r2 = r2_score(y_test_r, y_pred_r)

    print(f"Linear Regression R2 Score : {r2:.4f} (Model explains {r2 * 100:.1f}% of variance)")
    print(f"Mean Squared Error (MSE)   : {mse:.2f}")
    print(f"Learned Formula: Score = {lin_reg.intercept_:.2f} + ({lin_reg.coef_[0]:.2f} * Hours) + ({lin_reg.coef_[1]:.2f} * Attendance)")

    # Plot Actual vs Predicted Scores
    plt.figure(figsize=(7, 5))
    plt.scatter(y_test_r, y_pred_r, color="#337ab7", edgecolors="black", s=70, label="Test Predictions")
    plt.plot([y_test_r.min(), y_test_r.max()], [y_test_r.min(), y_test_r.max()], "r--", lw=2, label="Perfect Fit (y = x)")
    plt.title("Actual vs. Predicted Student Exam Scores", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Actual Exam Score", fontweight="bold")
    plt.ylabel("Predicted Exam Score", fontweight="bold")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    reg_plot_path = os.path.join(CHARTS_DIR, "03_regression_actual_vs_predicted.png")
    plt.savefig(reg_plot_path, dpi=300)
    plt.close()
    print(f"[+] Saved Regression Fit Chart: {reg_plot_path}")

    # Predict for new student (e.g. 7.5 hours of study, 92% attendance)
    sample_student = [[7.5, 92.0]]
    pred_score = lin_reg.predict(sample_student)[0]
    print(f"\nInference: Student studying {sample_student[0][0]} hrs with {sample_student[0][1]}% attendance -> Predicted Score: {pred_score:.1f}%")

def main():
    os.makedirs(CHARTS_DIR, exist_ok=True)
    run_classification_workflow()
    run_regression_workflow()
    print("\n" + "=" * 75)
    print("      MODULE 04: MACHINE LEARNING WORKFLOW COMPLETED!         ")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    main()
