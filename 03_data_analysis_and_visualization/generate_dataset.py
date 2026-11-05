"""
Dataset Generator: generate_dataset.py
Description: Generates a realistic E-Commerce Sales & Customer Demographics dataset
             with intentional missing values, mixed types, and duplicates to demonstrate
             data exploration, cleaning, analysis, and visualization.
Module: Module 03 - Data Analysis & Visualization
"""

import os
import random
import numpy as np
import pandas as pd

def create_sample_dataset(filepath: str = "03_data_analysis_and_visualization/sample_sales_data.csv", n_rows: int = 250):
    np.random.seed(42)
    random.seed(42)

    categories = ["Electronics", "Fashion", "Home & Kitchen", "Books", "Beauty & Personal Care"]
    payment_methods = ["Credit Card", "UPI / Digital Wallet", "Net Banking", "Debit Card", "Cash on Delivery"]
    regions = ["North", "South", "East", "West", "Central"]
    dates = pd.date_range(start="2026-01-01", end="2026-06-30", freq="D")

    records = []
    for i in range(1, n_rows + 1):
        order_id = 1000 + i
        date = random.choice(dates).strftime("%Y-%m-%d")
        category = random.choice(categories)
        units = random.randint(1, 10)
        
        # Base prices by category
        price_map = {
            "Electronics": random.uniform(80.0, 950.0),
            "Fashion": random.uniform(20.0, 180.0),
            "Home & Kitchen": random.uniform(25.0, 300.0),
            "Books": random.uniform(10.0, 75.0),
            "Beauty & Personal Care": random.uniform(15.0, 120.0),
        }
        unit_price = round(price_map[category], 2)
        discount = round(random.choice([0.0, 0.05, 0.10, 0.15, 0.20]), 2)
        payment = random.choice(payment_methods)
        region = random.choice(regions)
        customer_age = random.choice([random.randint(18, 65), np.nan]) # Intentional missing values
        rating = round(random.uniform(2.5, 5.0), 1)

        records.append({
            "OrderID": order_id,
            "Date": date,
            "Category": category,
            "Quantity": units,
            "UnitPrice": unit_price,
            "Discount": discount,
            "PaymentMethod": payment,
            "Region": region,
            "CustomerAge": customer_age,
            "CustomerRating": rating
        })

    df = pd.DataFrame(records)

    # Insert a few intentional duplicate rows to demonstrate cleaning
    duplicates = df.iloc[:5].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    # Insert a few NaN values in PaymentMethod and UnitPrice to demonstrate imputation
    df.loc[12, "PaymentMethod"] = np.nan
    df.loc[25, "UnitPrice"] = np.nan
    df.loc[45, "Category"] = np.nan

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"[+] Dataset created successfully at: {filepath} ({len(df)} records)")
    return filepath

if __name__ == "__main__":
    create_sample_dataset()

