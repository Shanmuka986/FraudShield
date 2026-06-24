import streamlit as st
import pandas as pd
import plotly.express as px

from db import get_transactions
from dashboard.theme import apply_dashboard_theme

st.set_page_config(
    page_title="Risk Monitor",
    page_icon="⚠️",
    layout="wide"
)

apply_dashboard_theme()

st.title("⚠️ Risk Monitor")

df = get_transactions()

# ==========================
# KPI CARDS
# ==========================

total_high_risk = len(
    df[
        df["risk_level"] == "High"
    ]
)

total_critical = len(
    df[
        df["risk_level"] == "Critical"
    ]
)

avg_fraud_score = round(
    df["fraud_score"].mean(),
    2
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "High Risk Transactions",
    total_high_risk
)

c2.metric(
    "Critical Transactions",
    total_critical
)

c3.metric(
    "Average Fraud Score",
    avg_fraud_score
)

# ==========================
# RISK DISTRIBUTION
# ==========================

st.divider()

st.subheader(
    "Risk Distribution"
)

risk_df = (
    df["risk_level"]
    .value_counts()
    .reset_index()
)

risk_df.columns = [
    "Risk Level",
    "Count"
]

fig = px.bar(
    risk_df,
    x="Risk Level",
    y="Count",
    title="Risk Level Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ==========================
# FRAUD SCORE DISTRIBUTION
# ==========================

st.divider()

st.subheader(
    "Fraud Score Distribution"
)

fig = px.histogram(
    df,
    x="fraud_score",
    nbins=20,
    title="Fraud Score Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ==========================
# HIGH RISK TRANSACTIONS
# ==========================

st.divider()

st.subheader(
    "High Risk Transactions"
)

high_risk_df = df[
    df["fraud_score"] >= 40
]

st.dataframe(
    high_risk_df,
    width="stretch"
)