"""
Script to generate Module_04_Machine_Learning_Fundamentals.ipynb
"""

import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Module 04: Machine Learning Fundamentals 🤖\n",
    "\n",
    "**Internship Track:** AI & Python Internship  \n",
    "**Author:** Abishek J (`abi323728-ctrl`)  \n",
    "**Module Focus:** The Machine Learning Workflow, Scikit-learn, Classification (Iris Flower), Regression (Student Score Prediction), and Model Evaluation  \n",
    "\n",
    "---\n",
    "\n",
    "## 🎯 Key Objectives Covered:\n",
    "1. **Learn the basic Machine Learning workflow** (Data $\\to$ Preprocessing $\\to$ Train/Test Split $\\to$ Model Training $\\to$ Evaluation $\\to$ Inference)\n",
    "2. **Train your first Machine Learning model using Scikit-learn**\n",
    "3. **Use beginner-friendly datasets** (Iris Flower Classification & Student Exam Score Prediction)\n",
    "4. **Test your model and understand prediction results** (Accuracy, Confusion Matrix, Classification Report, R2 Score, and Feature Importances)\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Environment Setup & Library Imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Scikit-Learn tools & models\n",
    "from sklearn.datasets import load_iris\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import (\n",
    "    accuracy_score,\n",
    "    classification_report,\n",
    "    confusion_matrix,\n",
    "    ConfusionMatrixDisplay,\n",
    "    mean_squared_error,\n",
    "    r2_score\n",
    ")\n",
    "\n",
    "plt.rcParams[\"figure.figsize\"] = (9, 5)\n",
    "plt.rcParams[\"font.size\"] = 10\n",
    "\n",
    "print(\"Scikit-learn environment ready!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Theoretical Overview: The Machine Learning Workflow\n",
    "\n",
    "```\n",
    "+------------------+      +--------------------+      +--------------------+\n",
    "| 1. Data Loading  | ---> | 2. Preprocessing   | ---> | 3. Train/Test Split|\n",
    "| (Raw Features X, |      | (StandardScaler,   |      | (e.g. 80% Train,   |\n",
    "|  Labels y)       |      |  Imputation)       |      |  20% Test)         |\n",
    "+------------------+      +--------------------+      +--------------------+\n",
    "                                                                |\n",
    "                                                                v\n",
    "+------------------+      +--------------------+      +--------------------+\n",
    "| 6. Production    | <--- | 5. Model Evaluation| <--- | 4. Model Training  |\n",
    "|    Inference     |      | (Accuracy, Matrix, |      | (model.fit(X_train,|\n",
    "| (model.predict)  |      |  MSE, R2 Score)    |      |            y_train)|\n",
    "+------------------+      +--------------------+      +--------------------+\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Project 1: Iris Flower Classification (Supervised Classification)\n",
    "\n",
    "The Iris dataset is the canonical benchmark dataset in pattern recognition. It consists of 150 flower samples across 3 species (**Setosa**, **Versicolor**, **Virginica**) with 4 morphological features:\n",
    "1. Sepal Length (cm)\n",
    "2. Sepal Width (cm)\n",
    "3. Petal Length (cm)\n",
    "4. Petal Width (cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Load and explore dataset\n",
    "iris = load_iris()\n",
    "X = iris.data\n",
    "y = iris.target\n",
    "feature_names = iris.feature_names\n",
    "target_names = iris.target_names\n",
    "\n",
    "df_iris = pd.DataFrame(X, columns=feature_names)\n",
    "df_iris[\"Species\"] = [target_names[i] for i in y]\n",
    "\n",
    "print(f\"Dataset Shape: {df_iris.shape[0]} samples, {df_iris.shape[1]} columns\")\n",
    "print(f\"Target Classes: {list(target_names)}\")\n",
    "df_iris.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 2: Train/Test Split & Feature Scaling\n",
    "We split the data into 80% for training and 20% for testing. `StandardScaler` normalizes features so they have zero mean and unit variance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.20, random_state=42, stratify=y\n",
    ")\n",
    "\n",
    "# Standardization\n",
    "scaler = StandardScaler()\n",
    "X_train_scaled = scaler.fit_transform(X_train)\n",
    "X_test_scaled = scaler.transform(X_test)\n",
    "\n",
    "print(f\"Training set: {X_train.shape[0]} samples\")\n",
    "print(f\"Testing set : {X_test.shape[0]} samples\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 3: Model Training (KNN & Random Forest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Model 1: K-Nearest Neighbors Classifier\n",
    "knn = KNeighborsClassifier(n_neighbors=5)\n",
    "knn.fit(X_train_scaled, y_train)\n",
    "\n",
    "# Model 2: Random Forest Classifier\n",
    "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "rf.fit(X_train, y_train)\n",
    "\n",
    "print(\"Models successfully trained!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 4: Model Evaluation (Accuracy, Classification Report, Confusion Matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred_knn = knn.predict(X_test_scaled)\n",
    "y_pred_rf = rf.predict(X_test)\n",
    "\n",
    "print(f\"KNN Test Accuracy          : {accuracy_score(y_test, y_pred_knn) * 100:.2f}%\")\n",
    "print(f\"Random Forest Test Accuracy: {accuracy_score(y_test, y_pred_rf) * 100:.2f}%\")\n",
    "\n",
    "print(\"\\n--- Detailed Classification Report (Random Forest) ---\")\n",
    "print(classification_report(y_test, y_pred_rf, target_names=target_names))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Visualizing Confusion Matrix & Feature Importances"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
    "\n",
    "# 1. Confusion Matrix\n",
    "disp = ConfusionMatrixDisplay.from_predictions(\n",
    "    y_test, y_pred_rf, display_labels=target_names, cmap=\"Blues\", ax=ax1\n",
    ")\n",
    "ax1.set_title(\"Confusion Matrix (Random Forest)\", fontweight=\"bold\")\n",
    "ax1.grid(False)\n",
    "\n",
    "# 2. Feature Importances\n",
    "importances = rf.feature_importances_\n",
    "indices = np.argsort(importances)[::-1]\n",
    "ax2.bar([feature_names[i] for i in indices], importances[indices], color=\"#2b5c8f\", edgecolor=\"black\", alpha=0.85)\n",
    "ax2.set_title(\"Feature Importance Weights\", fontweight=\"bold\")\n",
    "ax2.set_ylabel(\"Importance Score\")\n",
    "ax2.grid(axis=\"y\", linestyle=\"--\", alpha=0.6)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 5: Inference on Unseen Custom Flower Measurements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Unseen flower: Sepal Length=5.1, Sepal Width=3.5, Petal Length=1.4, Petal Width=0.2\n",
    "custom_flower = np.array([[5.1, 3.5, 1.4, 0.2]])\n",
    "custom_scaled = scaler.transform(custom_flower)\n",
    "\n",
    "pred_class = knn.predict(custom_scaled)[0]\n",
    "probabilities = knn.predict_proba(custom_scaled)[0]\n",
    "\n",
    "print(\"--- Custom Prediction Output ---\")\n",
    "print(f\"Measurements Input : {custom_flower[0]}\")\n",
    "print(f\"Predicted Species  : {target_names[pred_class].upper()}\")\n",
    "print(f\"Confidence Level   : {probabilities[pred_class] * 100:.1f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Project 2: Student Exam Score Prediction (Supervised Regression)\n",
    "Predicting continuous numerical outcomes using **Linear Regression** based on study hours and attendance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Synthetic realistic dataset\n",
    "np.random.seed(42)\n",
    "study_hours = np.random.uniform(1.0, 10.0, 60)\n",
    "attendance = np.random.uniform(60.0, 100.0, 60)\n",
    "noise = np.random.normal(0, 3.5, 60)\n",
    "exam_scores = np.clip(15 + (6.5 * study_hours) + (0.2 * attendance) + noise, 0, 100)\n",
    "\n",
    "df_scores = pd.DataFrame({\"Hours\": study_hours, \"Attendance\": attendance, \"Score\": exam_scores})\n",
    "\n",
    "X_r = df_scores[[\"Hours\", \"Attendance\"]]\n",
    "y_r = df_scores[\"Score\"]\n",
    "\n",
    "X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(\n",
    "    X_r, y_r, test_size=0.25, random_state=42\n",
    ")\n",
    "\n",
    "model_reg = LinearRegression()\n",
    "model_reg.fit(X_train_r, y_train_r)\n",
    "y_pred_r = model_reg.predict(X_test_r)\n",
    "\n",
    "r2 = r2_score(y_test_r, y_pred_r)\n",
    "mse = mean_squared_error(y_test_r, y_pred_r)\n",
    "\n",
    "print(f\"R-squared (R2) Score : {r2:.4f} (Model explains {r2 * 100:.1f}% of variance)\")\n",
    "print(f\"Mean Squared Error   : {mse:.2f}\")\n",
    "print(f\"Formula: Score = {model_reg.intercept_:.2f} + ({model_reg.coef_[0]:.2f} * Hours) + ({model_reg.coef_[1]:.2f} * Attendance)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Visualizing Regression Performance: Actual vs. Predicted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(8, 5))\n",
    "plt.scatter(y_test_r, y_pred_r, color=\"#337ab7\", edgecolors=\"black\", s=80, label=\"Predictions\")\n",
    "plt.plot([y_test_r.min(), y_test_r.max()], [y_test_r.min(), y_test_r.max()], \"r--\", lw=2, label=\"Perfect Fit Line (y=x)\")\n",
    "plt.title(\"Actual vs. Predicted Exam Scores (Linear Regression)\", fontsize=13, fontweight=\"bold\", pad=12)\n",
    "plt.xlabel(\"Actual Score (%)\", fontweight=\"bold\")\n",
    "plt.ylabel(\"Predicted Score (%)\", fontweight=\"bold\")\n",
    "plt.grid(True, linestyle=\"--\", alpha=0.6)\n",
    "plt.legend()\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Summary & Key Learnings\n",
    "\n",
    "1. **Workflow Structure:** Cleanly separating Data Ingestion, Preprocessing, Model Fitting, and Evaluation guarantees reproducible Machine Learning results.\n",
    "2. **Classification vs Regression:** Classification predicts discrete category labels (`Setosa`, `Versicolor`, `Virginica`), while Regression predicts continuous quantities (`Exam Score`).\n",
    "3. **Importance of Feature Scaling:** Algorithms that rely on Euclidean distance (like KNN) require scaled features to prevent larger-magnitude dimensions from dominating distance metrics.\n",
    "4. **Evaluation Metrics:** Accuracy is complemented by Precision, Recall, Confusion Matrices, and $R^2$ scores to provide a holistic view of model reliability."
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

output_path = "04_machine_learning_fundamentals/Module_04_Machine_Learning_Fundamentals.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print(f"Jupyter Notebook successfully created at: {output_path}")
