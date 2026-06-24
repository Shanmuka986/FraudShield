import pandas as pd
import random
from datetime import datetime, timedelta
from uuid import uuid4
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from simulator.merchants import MERCHANTS
from simulator.locations import CITIES
from simulator.categories import CATEGORIES
from simulator.devices import DEVICES
from simulator.fraud_rules import calculate_risk


HIGH_RISK_MERCHANTS = [
    "Amazon",
    "Flipkart",
    "Paytm Mall",
    "Snapdeal"
]

FESTIVAL_MONTHS = [10, 11, 12]


def generate_transactions(num_records=1000):

    data = []

    for i in range(num_records):

        amount = round(
            random.uniform(100, 100000),
            2
        )

        risk_level = calculate_risk(amount)

        transaction_time = datetime.now() - timedelta(
            days=random.randint(0, 364),
            seconds=random.randint(0, 86399)
        )

        merchant = random.choice(MERCHANTS)

        fraud_probability = 0.02

        # Amount Risk
        if risk_level == "Critical":
            fraud_probability += 0.25

        elif risk_level == "High":
            fraud_probability += 0.12

        elif risk_level == "Medium":
            fraud_probability += 0.05

        # Merchant Risk
        if merchant in HIGH_RISK_MERCHANTS:
            fraud_probability += 0.10

        # Night Time Risk
        if (
            transaction_time.hour >= 22
            or transaction_time.hour <= 5
        ):
            fraud_probability += 0.15

        # Festival Risk
        if transaction_time.month in FESTIVAL_MONTHS:
            fraud_probability += 0.05

        fraud_score = round(
            fraud_probability * 100,
            2
        )

        fraud_flag = (
            random.random() < fraud_probability
        )

        data.append({
            "transaction_id": f"TXN-{uuid4().hex[:12]}",
            "merchant": merchant,
            "city": random.choice(CITIES),
            "category": random.choice(CATEGORIES),
            "device": random.choice(DEVICES),
            "amount": amount,
            "fraud_flag": fraud_flag,
            "fraud_score": fraud_score,
            "risk_level": risk_level,
            "transaction_time": transaction_time
        })

    return pd.DataFrame(data)


if __name__ == "__main__":

    df = generate_transactions(1000)

    output_path = Path(
        "data/raw/transactions.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        "1000 transactions generated successfully."
    )