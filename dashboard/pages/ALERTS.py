import streamlit as st
import pandas as pd

from db import get_transactions

st.set_page_config(
    page_title="Alert Center",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Fraud Alert Center")

df = get_transactions()

# ==========================
# HIGH FRAUD SCORE ALERTS
# ==========================

high_fraud_df = df[
    df["fraud_score"] >= 40
]

critical_df = df[
    df["risk_level"] == "Critical"
]

# KPI CARDS

c1, c2, c3 = st.columns(3)

c1.metric(
    "High Fraud Alerts",
    len(high_fraud_df)
)

c2.metric(
    "Critical Risk Alerts",
    len(critical_df)
)

c3.metric(
    "Total Alerts",
    len(high_fraud_df) + len(critical_df)
)

st.divider()

# ==========================
# HIGH FRAUD SCORE
# ==========================

st.subheader(
    "🚨 High Fraud Score Transactions"
)

st.dataframe(
    high_fraud_df.sort_values(
        by="fraud_score",
        ascending=False
    ),
    width="stretch"
)

st.divider()

# ==========================
# CRITICAL RISK
# ==========================

st.subheader(
    "⚠️ Critical Risk Transactions"
)

st.dataframe(
    critical_df,
    width="stretch"
)

st.divider()

# ==========================
# SUSPICIOUS MERCHANTS
# ==========================

st.subheader(
    "🏪 Suspicious Merchants"
)

merchant_alerts = (
    high_fraud_df["merchant"]
    .value_counts()
    .reset_index()
)

merchant_alerts.columns = [
    "Merchant",
    "Alert Count"
]

st.dataframe(
    merchant_alerts,
    width="stretch"
)

st.divider()

# ==========================
# ALERT SUMMARY
# ==========================

st.subheader(
    "📋 Alert Summary"
)

if len(high_fraud_df) > 0:

    top_merchant = (
        high_fraud_df["merchant"]
        .value_counts()
        .idxmax()
    )

    top_city = (
        high_fraud_df["city"]
        .value_counts()
        .idxmax()
    )

    st.error(
        f"""
        🚨 High Risk Activity Detected

        Top Suspicious Merchant:
        {top_merchant}

        Top Suspicious City:
        {top_city}

        Total Alerts:
        {len(high_fraud_df)}
        """
    )

else:

    st.success(
        "✅ No Major Fraud Alerts Detected"
    )