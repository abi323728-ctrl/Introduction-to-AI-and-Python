"""
Data Analysis Pipeline: data_analysis_pipeline.py
Description: End-to-end data analysis and visualization pipeline implementing:
             1. Pandas and NumPy dataset manipulation
             2. Data cleaning & handling missing values/duplicates
             3. Summary statistics and group aggregations
             4. Matplotlib charts: Bar chart, Line chart, and Pie chart
Module: Module 03 - Data Analysis & Visualization
Author: Abishek J (abi323728-ctrl)
"""

import os
import matplotlib
matplotlib.use("Agg") # Non-interactive headless backend for clean script execution
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CHARTS_DIR = "03_data_analysis_and_visualization/charts"
DATA_FILE = "03_data_analysis_and_visualization/sample_sales_data.csv"

def run_analysis_pipeline():
    os.makedirs(CHARTS_DIR, exist_ok=True)
    print("=" * 75)
    print("      MODULE 03: DATA ANALYSIS & VISUALIZATION PIPELINE       ")
    print("=" * 75)

    # -------------------------------------------------------------
    # STEP 1: Load and Explore Dataset (Pandas & NumPy)
    # -------------------------------------------------------------
    print("\n--- STEP 1: Loading Dataset & Initial Exploration ---")
    df = pd.read_csv(DATA_FILE)
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values Count (Before Cleaning):")
    print(df.isnull().sum())

    # -------------------------------------------------------------
    # STEP 2: Data Cleaning & Preprocessing
    # -------------------------------------------------------------
    print("\n--- STEP 2: Data Cleaning & Preprocessing ---")
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - len(df)} duplicate records. Current rows: {len(df)}")

    # Handle missing values
    # Fill categorical nulls with Mode
    df["Category"] = df["Category"].fillna(df["Category"].mode()[0])
    df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])

    # Fill numerical nulls with Median
    df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median())
    df["CustomerAge"] = df["CustomerAge"].fillna(df["CustomerAge"].median())

    print("Missing Values Count (After Cleaning):")
    print(df.isnull().sum().to_dict())

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    # Feature Engineering using vectorized NumPy operations
    # TotalAmount = (Quantity * UnitPrice) * (1 - Discount)
    raw_subtotal = np.multiply(df["Quantity"].values, df["UnitPrice"].values)
    discount_factor = 1.0 - df["Discount"].values
    df["TotalRevenue"] = np.round(raw_subtotal * discount_factor, 2)

    print("\nEngineered Feature 'TotalRevenue' sample:")
    print(df[["OrderID", "Category", "Quantity", "UnitPrice", "Discount", "TotalRevenue"]].head())

    # -------------------------------------------------------------
    # STEP 3: Summary Statistics & Aggregations
    # -------------------------------------------------------------
    print("\n--- STEP 3: Statistical Metrics & Aggregations ---")
    revenue_array = df["TotalRevenue"].to_numpy()
    print(f"Total Gross Revenue    : ${np.sum(revenue_array):,.2f}")
    print(f"Average Order Value    : ${np.mean(revenue_array):.2f}")
    print(f"Median Order Value     : ${np.median(revenue_array):.2f}")
    print(f"Standard Deviation     : ${np.std(revenue_array):.2f}")
    print(f"25th & 75th Percentiles: ${np.percentile(revenue_array, 25):.2f}, ${np.percentile(revenue_array, 75):.2f}")

    category_summary = df.groupby("Category").agg(
        Total_Orders=("OrderID", "count"),
        Total_Revenue=("TotalRevenue", "sum"),
        Avg_Rating=("CustomerRating", "mean")
    ).reset_index().sort_values(by="Total_Revenue", ascending=False)

    print("\nRevenue Breakdown by Product Category:")
    print(category_summary.to_string(index=False))

    # -------------------------------------------------------------
    # STEP 4: Data Visualizations with Matplotlib
    # -------------------------------------------------------------
    print("\n--- STEP 4: Generating Matplotlib Visualizations ---")

    # 1. BAR CHART: Total Revenue by Category
    plt.figure(figsize=(9, 5))
    colors = ["#2b5c8f", "#3c8dbc", "#46a5e5", "#70bcf4", "#99d1fa"]
    bars = plt.bar(category_summary["Category"], category_summary["Total_Revenue"], color=colors, edgecolor="black", alpha=0.85)
    plt.title("Total Revenue by Product Category", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Product Category", fontsize=11, fontweight="bold")
    plt.ylabel("Total Revenue ($ USD)", fontsize=11, fontweight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Add numeric labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height + 500, f"${height:,.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

    plt.tight_layout()
    bar_chart_path = os.path.join(CHARTS_DIR, "01_revenue_by_category_barchart.png")
    plt.savefig(bar_chart_path, dpi=300)
    plt.close()
    print(f"  [+] Saved Bar Chart: {bar_chart_path}")

    # 2. LINE CHART: Monthly Revenue Trends Over Time
    monthly_trend = df.groupby("Month")["TotalRevenue"].sum().reset_index()
    plt.figure(figsize=(9, 5))
    plt.plot(monthly_trend["Month"], monthly_trend["TotalRevenue"], marker="o", color="#d9534f", linewidth=2.5, markersize=8, label="Monthly Revenue")
    plt.title("Monthly Revenue Trajectory (Jan - Jun 2026)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Month", fontsize=11, fontweight="bold")
    plt.ylabel("Revenue ($ USD)", fontsize=11, fontweight="bold")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper left")

    for x, y in zip(monthly_trend["Month"], monthly_trend["TotalRevenue"]):
        plt.annotate(f"${y:,.0f}", (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9, fontweight="bold")

    plt.tight_layout()
    line_chart_path = os.path.join(CHARTS_DIR, "02_monthly_trend_linechart.png")
    plt.savefig(line_chart_path, dpi=300)
    plt.close()
    print(f"  [+] Saved Line Chart: {line_chart_path}")

    # 3. PIE CHART: Payment Method Proportions
    payment_counts = df["PaymentMethod"].value_counts()
    plt.figure(figsize=(7, 7))
    pie_colors = ["#4daf4a", "#377eb8", "#ff7f00", "#984ea3", "#e41a1c"]
    explode = (0.05, 0, 0, 0, 0) # Highlight the top payment method
    plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", startangle=140, colors=pie_colors, explode=explode, shadow=True, textprops={"fontsize": 10})
    plt.title("Distribution of Customer Payment Methods", fontsize=14, fontweight="bold", pad=15)
    plt.tight_layout()
    pie_chart_path = os.path.join(CHARTS_DIR, "03_payment_distribution_piechart.png")
    plt.savefig(pie_chart_path, dpi=300)
    plt.close()
    print(f"  [+] Saved Pie Chart: {pie_chart_path}")

    # 4. BONUS COMBO VISUALIZATION: Customer Age Distribution Histogram & Boxplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.hist(df["CustomerAge"], bins=15, color="#5bc0de", edgecolor="black", alpha=0.75)
    ax1.set_title("Customer Age Demographics", fontweight="bold")
    ax1.set_xlabel("Age (Years)")
    ax1.set_ylabel("Frequency")
    ax1.grid(axis="y", linestyle="--", alpha=0.6)

    ax2.boxplot(df["TotalRevenue"], vert=True, patch_artist=True, boxprops=dict(facecolor="#f0ad4e", color="black"))
    ax2.set_title("Order Revenue Boxplot (Outlier Detection)", fontweight="bold")
    ax2.set_ylabel("Order Value ($)")
    ax2.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    dist_chart_path = os.path.join(CHARTS_DIR, "04_demographics_and_distribution.png")
    plt.savefig(dist_chart_path, dpi=300)
    plt.close()
    print(f"  [+] Saved Distribution & Boxplot Chart: {dist_chart_path}")

    print("\n" + "=" * 75)
    print("      DATA ANALYSIS & VISUALIZATION PIPELINE COMPLETED!       ")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    run_analysis_pipeline()

