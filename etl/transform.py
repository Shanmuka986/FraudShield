import pandas as pd
import os


def transform_data(df):

    # Remove duplicates
    initial_rows = len(df)

    df = df.drop_duplicates()

    final_rows = len(df)

    print(
        f"Removed {initial_rows - final_rows} duplicates"
    )

    # Handle missing values
    df["amount"] = df["amount"].fillna(0)

    # Convert fraud flag
    df["fraud_flag"] = df["fraud_flag"].astype(bool)

    # Create folder automatically
    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    # Save processed data
    df.to_csv(
        "data/processed/clean_transactions.csv",
        index=False
    )

    print(
        "Processed file saved successfully."
    )

    return df