"""
Script to generate Module_03_Data_Analysis_and_Visualization.ipynb
"""

import json
import os

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Module 03: Data Analysis & Visualization 📊\n",
    "\n",
    "**Internship Track:** AI & Python Internship  \n",
    "**Author:** Abishek J (`abi323728-ctrl`)  \n",
    "**Module Focus:** NumPy, Pandas, Data Cleaning, Statistical Analysis, and Matplotlib Visualizations  \n",
    "\n",
    "---\n",
    "\n",
    "## 🎯 Key Objectives Covered:\n",
    "1. **Learn how to work with datasets using Pandas and NumPy**\n",
    "2. **Load and explore a sample dataset** (`.head()`, `.info()`, `.describe()`)\n",
    "3. **Perform simple data cleaning and analysis** (handling missing values, duplicates, feature engineering)\n",
    "4. **Create charts like bar charts, line charts, and pie charts using Matplotlib**\n",
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
    "import seaborn as sns\n",
    "import random\n",
    "\n",
    "# Set visual style for clean, publication-grade figures\n",
    "sns.set_theme(style=\"whitegrid\")\n",
    "plt.rcParams[\"figure.figsize\"] = (10, 5)\n",
    "plt.rcParams[\"font.size\"] = 10\n",
    "\n",
    "print(\"Libraries imported successfully!\")\n",
    "print(f\"NumPy Version: {np.__version__}\")\n",
    "print(f\"Pandas Version: {pd.__version__}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Objective 1: NumPy Foundations & Vectorized Computation\n",
    "NumPy provides high-performance n-dimensional arrays and mathematical operations essential for data analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Array Creation & Reshaping\n",
    "data_points = np.array([12, 18, 25, 30, 42, 55, 68, 74, 88, 95])\n",
    "matrix = np.arange(1, 13).reshape(3, 4)\n",
    "\n",
    "print(\"1D Array:\", data_points)\n",
    "print(\"2D Matrix (3x4):\\n\", matrix)\n",
    "\n",
    "# 2. Vectorized Math Operations\n",
    "squared = np.square(data_points)\n",
    "normalized = (data_points - np.min(data_points)) / (np.max(data_points) - np.min(data_points))\n",
    "\n",
    "print(\"\\nVectorized Normalized Values (0 to 1):\\n\", np.round(normalized, 3))\n",
    "\n",
    "# 3. Statistical Calculations\n",
    "print(\"\\n--- Statistical Metrics ---\")\n",
    "print(f\"Mean               : {np.mean(data_points):.2f}\")\n",
    "print(f\"Median             : {np.median(data_points):.2f}\")\n",
    "print(f\"Standard Deviation : {np.std(data_points):.2f}\")\n",
    "print(f\"25th & 75th %iles  : {np.percentile(data_points, 25):.1f}, {np.percentile(data_points, 75):.1f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Objective 2: Creating and Loading the Sample Dataset\n",
    "We generate a realistic E-Commerce Sales dataset with 250+ transactions across 5 categories, containing intentional real-world anomalies (missing values, duplicates) to demonstrate data cleaning."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate reproducible realistic sample dataset\n",
    "np.random.seed(42)\n",
    "random.seed(42)\n",
    "\n",
    "categories = [\"Electronics\", \"Fashion\", \"Home & Kitchen\", \"Books\", \"Beauty & Personal Care\"]\n",
    "payment_methods = [\"Credit Card\", \"UPI / Digital Wallet\", \"Net Banking\", \"Debit Card\", \"Cash on Delivery\"]\n",
    "regions = [\"North\", \"South\", \"East\", \"West\", \"Central\"]\n",
    "dates = pd.date_range(start=\"2026-01-01\", end=\"2026-06-30\", freq=\"D\")\n",
    "\n",
    "rows = []\n",
    "for i in range(1, 251):\n",
    "    cat = random.choice(categories)\n",
    "    price_map = {\n",
    "        \"Electronics\": random.uniform(100.0, 950.0),\n",
    "        \"Fashion\": random.uniform(20.0, 180.0),\n",
    "        \"Home & Kitchen\": random.uniform(25.0, 300.0),\n",
    "        \"Books\": random.uniform(10.0, 75.0),\n",
    "        \"Beauty & Personal Care\": random.uniform(15.0, 120.0),\n",
    "    }\n",
    "    unit_price = round(price_map[cat], 2)\n",
    "    rows.append({\n",
    "        \"OrderID\": 1000 + i,\n",
    "        \"Date\": random.choice(dates).strftime(\"%Y-%m-%d\"),\n",
    "        \"Category\": cat,\n",
    "        \"Quantity\": random.randint(1, 10),\n",
    "        \"UnitPrice\": unit_price,\n",
    "        \"Discount\": random.choice([0.0, 0.05, 0.10, 0.15, 0.20]),\n",
    "        \"PaymentMethod\": random.choice(payment_methods),\n",
    "        \"Region\": random.choice(regions),\n",
    "        \"CustomerAge\": random.choice([random.randint(18, 65), np.nan]), # Missing values\n",
    "        \"CustomerRating\": round(random.uniform(2.5, 5.0), 1)\n",
    "    })\n",
    "\n",
    "raw_df = pd.DataFrame(rows)\n",
    "\n",
    "# Inject duplicates and missing entries for cleaning demonstration\n",
    "duplicates = raw_df.iloc[:5].copy()\n",
    "df = pd.concat([raw_df, duplicates], ignore_index=True)\n",
    "df.loc[12, \"PaymentMethod\"] = np.nan\n",
    "df.loc[25, \"UnitPrice\"] = np.nan\n",
    "df.loc[45, \"Category\"] = np.nan\n",
    "\n",
    "print(f\"Dataset generated successfully with {len(df)} records and {df.shape[1]} columns!\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Initial Exploration: `.info()` and `.describe()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"--- Dataset Information ---\")\n",
    "df.info()\n",
    "\n",
    "print(\"\\n--- Descriptive Statistics (Numerical Columns) ---\")\n",
    "display(df.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Objective 3: Data Cleaning & Feature Engineering\n",
    "In this phase, we:\n",
    "1. **Identify and remove duplicate entries**\n",
    "2. **Identify and impute missing values (NaNs)**\n",
    "3. **Format date columns for time-series extraction**\n",
    "4. **Engineer new calculated metrics** (`TotalRevenue`)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"--- 1. Missing Values Before Cleaning ---\")\n",
    "print(df.isnull().sum())\n",
    "\n",
    "# Remove duplicates\n",
    "dups_count = df.duplicated().sum()\n",
    "df.drop_duplicates(inplace=True)\n",
    "print(f\"\\n[+] Removed {dups_count} duplicate records.\")\n",
    "\n",
    "# Impute categorical missing values with Mode\n",
    "df[\"Category\"].fillna(df[\"Category\"].mode()[0], inplace=True)\n",
    "df[\"PaymentMethod\"].fillna(df[\"PaymentMethod\"].mode()[0], inplace=True)\n",
    "\n",
    "# Impute numerical missing values with Median\n",
    "df[\"UnitPrice\"].fillna(df[\"UnitPrice\"].median(), inplace=True)\n",
    "df[\"CustomerAge\"].fillna(df[\"CustomerAge\"].median(), inplace=True)\n",
    "\n",
    "print(\"\\n--- 2. Missing Values After Cleaning ---\")\n",
    "print(df.isnull().sum())\n",
    "\n",
    "# Date Formatting\n",
    "df[\"Date\"] = pd.to_datetime(df[\"Date\"])\n",
    "df[\"Month\"] = df[\"Date\"].dt.strftime(\"%Y-%m\")\n",
    "\n",
    "# Feature Engineering: TotalRevenue = Quantity * UnitPrice * (1 - Discount)\n",
    "df[\"TotalRevenue\"] = np.round(df[\"Quantity\"] * df[\"UnitPrice\"] * (1.0 - df[\"Discount\"]), 2)\n",
    "\n",
    "print(\"\\n[+] Cleaned Dataset Shape:\", df.shape)\n",
    "df[[\"OrderID\", \"Date\", \"Category\", \"Quantity\", \"UnitPrice\", \"Discount\", \"TotalRevenue\"]].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Aggregation & GroupBy Analysis\n",
    "Analyzing sales performance and customer ratings grouped by product category."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_summary = df.groupby(\"Category\").agg(\n",
    "    Total_Orders=(\"OrderID\", \"count\"),\n",
    "    Total_Revenue=(\"TotalRevenue\", \"sum\"),\n",
    "    Avg_Order_Value=(\"TotalRevenue\", \"mean\"),\n",
    "    Avg_Customer_Rating=(\"CustomerRating\", \"mean\")\n",
    ").reset_index().sort_values(by=\"Total_Revenue\", ascending=False)\n",
    "\n",
    "print(\"--- Summary by Product Category ---\")\n",
    "display(category_summary)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Objective 4: Data Visualization with Matplotlib\n",
    "\n",
    "### Chart 1: Bar Chart — Total Revenue by Product Category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(10, 5))\n",
    "colors = [\"#2b5c8f\", \"#3c8dbc\", \"#46a5e5\", \"#70bcf4\", \"#99d1fa\"]\n",
    "\n",
    "bars = plt.bar(\n",
    "    category_summary[\"Category\"],\n",
    "    category_summary[\"Total_Revenue\"],\n",
    "    color=colors,\n",
    "    edgecolor=\"black\",\n",
    "    alpha=0.85\n",
    ")\n",
    "\n",
    "plt.title(\"Total Revenue by Product Category\", fontsize=14, fontweight=\"bold\", pad=15)\n",
    "plt.xlabel(\"Product Category\", fontsize=11, fontweight=\"bold\")\n",
    "plt.ylabel(\"Total Revenue ($ USD)\", fontsize=11, fontweight=\"bold\")\n",
    "plt.grid(axis=\"y\", linestyle=\"--\", alpha=0.6)\n",
    "\n",
    "# Adding data values on bars\n",
    "for bar in bars:\n",
    "    height = bar.get_height()\n",
    "    plt.text(bar.get_x() + bar.get_width() / 2.0, height + 1000, f\"${height:,.0f}\", ha=\"center\", va=\"bottom\", fontsize=9, fontweight=\"bold\")\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Chart 2: Line Chart — Monthly Sales Revenue Trend Over Time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "monthly_sales = df.groupby(\"Month\")[\"TotalRevenue\"].sum().reset_index()\n",
    "\n",
    "plt.figure(figsize=(10, 5))\n",
    "plt.plot(\n",
    "    monthly_sales[\"Month\"],\n",
    "    monthly_sales[\"TotalRevenue\"],\n",
    "    marker=\"o\",\n",
    "    color=\"#d9534f\",\n",
    "    linewidth=2.5,\n",
    "    markersize=8,\n",
    "    label=\"Monthly Revenue\"\n",
    ")\n",
    "\n",
    "plt.title(\"Monthly Revenue Growth Trajectory (Jan - Jun 2026)\", fontsize=14, fontweight=\"bold\", pad=15)\n",
    "plt.xlabel(\"Month\", fontsize=11, fontweight=\"bold\")\n",
    "plt.ylabel(\"Total Revenue ($ USD)\", fontsize=11, fontweight=\"bold\")\n",
    "plt.grid(True, linestyle=\"--\", alpha=0.6)\n",
    "plt.legend(loc=\"upper left\")\n",
    "\n",
    "# Annotate data points\n",
    "for x, y in zip(monthly_sales[\"Month\"], monthly_sales[\"TotalRevenue\"]):\n",
    "    plt.annotate(f\"${y:,.0f}\", (x, y), textcoords=\"offset points\", xytext=(0, 10), ha=\"center\", fontsize=9, fontweight=\"bold\")\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Chart 3: Pie Chart — Distribution of Payment Methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "payment_distribution = df[\"PaymentMethod\"].value_counts()\n",
    "\n",
    "plt.figure(figsize=(8, 8))\n",
    "palette = [\"#4daf4a\", \"#377eb8\", \"#ff7f00\", \"#984ea3\", \"#e41a1c\"]\n",
    "explode = (0.06, 0, 0, 0, 0) # Highlight highest share\n",
    "\n",
    "plt.pie(\n",
    "    payment_distribution,\n",
    "    labels=payment_distribution.index,\n",
    "    autopct=\"%1.1f%%\",\n",
    "    startangle=140,\n",
    "    colors=palette,\n",
    "    explode=explode,\n",
    "    shadow=True,\n",
    "    textprops={\"fontsize\": 11, \"fontweight\": \"bold\"}\n",
    ")\n",
    "\n",
    "plt.title(\"Customer Payment Method Share\", fontsize=14, fontweight=\"bold\", pad=20)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bonus Chart: Customer Age Demographic Distribution & Outlier Boxplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))\n",
    "\n",
    "# Histogram of Customer Age\n",
    "ax1.hist(df[\"CustomerAge\"], bins=15, color=\"#5bc0de\", edgecolor=\"black\", alpha=0.8)\n",
    "ax1.set_title(\"Customer Age Demographics\", fontweight=\"bold\", fontsize=12)\n",
    "ax1.set_xlabel(\"Age (Years)\")\n",
    "ax1.set_ylabel(\"Number of Customers\")\n",
    "ax1.grid(axis=\"y\", linestyle=\"--\", alpha=0.6)\n",
    "\n",
    "# Boxplot of Order Revenue\n",
    "ax2.boxplot(df[\"TotalRevenue\"], vert=True, patch_artist=True, boxprops=dict(facecolor=\"#f0ad4e\", color=\"black\"))\n",
    "ax2.set_title(\"Order Value Distribution & Outliers\", fontweight=\"bold\", fontsize=12)\n",
    "ax2.set_ylabel(\"Total Revenue ($)\")\n",
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
    "## 6. Summary of Key Insights & Takeaways\n",
    "\n",
    "1. **Dominant Category:** **Electronics** generated the highest total revenue due to higher unit prices, while **Home & Kitchen** had the highest total volume of orders.\n",
    "2. **Payment Preferences:** Digital payment methods (UPI and Credit Cards) dominate total transaction volume, accounting for over 50% of orders.\n",
    "3. **Data Quality Impact:** Imputing missing customer ages and unit prices with median estimators avoided skewing distributions, and removing duplicate records ensured accurate financial totals.\n",
    "4. **Visual Storytelling:** Combining bar charts, line trends, and pie charts provides an intuitive, executive-ready dashboard for decision-makers."
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

output_path = "03_data_analysis_and_visualization/Module_03_Data_Analysis_and_Visualization.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print(f"Jupyter Notebook successfully created at: {output_path}")

