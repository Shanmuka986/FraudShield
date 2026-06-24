import pandas as pd
import os


def transform_data(df):

    initial_rows = len(df)

    # ==========================
    # Missing Values
    # ==========================

    missing_before = (
        df.isnull()
        .sum()
        .sum()
    )

    df["city"] = (
        df["city"]
        .fillna("Unknown")
    )

    df["category"] = (
        df["category"]
        .fillna("Unknown")
    )

    # ==========================
    # Duplicate Detection
    # ==========================

    duplicate_count = (
        df.duplicated(
            subset=[
                "merchant",
                "city",
                "category",
                "device",
                "amount",
                "fraud_flag",
                "fraud_score",
                "risk_level"
            ]
        )
        .sum()
    )

    df = df.drop_duplicates(
        subset=[
            "merchant",
            "city",
            "category",
            "device",
            "amount",
            "fraud_flag",
            "fraud_score",
            "risk_level"
        ]
    )

    # ==========================
    # Data Types
    # ==========================

    df["fraud_flag"] = (
        df["fraud_flag"]
        .astype(bool)
    )

    # ==========================
    # Quality Score
    # ==========================

    quality_score = round(
        (
            1 -
            (
                duplicate_count
                +
                missing_before
            )
            /
            initial_rows
        ) * 100,
        2
    )

    # ==========================
    # Save Processed File
    # ==========================

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    df.to_csv(
        "data/processed/clean_transactions.csv",
        index=False
    )

    print(
        f"Missing Values Found: {missing_before}"
    )

    print(
        f"Duplicates Removed: {duplicate_count}"
    )

    print(
        f"Quality Score: {quality_score}%"
    )

    print(
        "Processed file saved successfully."
    )

    return df
