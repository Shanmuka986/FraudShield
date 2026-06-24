import pandas as pd

def extract_data():

    df = pd.read_csv(
        "data/raw/transactions.csv"
    )

    print(
        f"Extracted {len(df)} records"
    )

    return df