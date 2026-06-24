import streamlit as st
from db import get_transactions
from simulator.config import (
    HIGH_RISK_MERCHANTS,
    FESTIVAL_MONTHS
)
from dashboard.theme import apply_dashboard_theme

apply_dashboard_theme()

st.title("🔍 Transaction Explorer")

df = get_transactions()

search = st.text_input(
    "Transaction ID"
)

city = st.selectbox(
    "City",
    ["All"] + sorted(
        df["city"].unique()
    )
)

risk = st.selectbox(
    "Risk",
    ["All"] + sorted(
        df["risk_level"].unique()
    )
)

filtered = df.copy()

if city != "All":
    filtered = filtered[
        filtered["city"] == city
    ]

if risk != "All":
    filtered = filtered[
        filtered["risk_level"] == risk
    ]

if search:
    filtered = filtered[
        filtered["transaction_id"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.dataframe(
    filtered,
    width="stretch"
)