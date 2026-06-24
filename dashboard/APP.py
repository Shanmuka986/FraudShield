import streamlit as st
import pandas as pd
import plotly.express as px

from db import (
    get_transactions,
    get_pipeline_logs
)
from dashboard.theme import apply_dashboard_theme, safe_top_value

# ==================================
# PAGE CONFIG (MUST BE FIRST)
# ==================================

st.set_page_config(
    page_title="FraudShield",
    page_icon="🛡️",
    layout="wide"
)
apply_dashboard_theme()

st.markdown("""
<div class="hero">

<h1>🛡 FraudShield</h1>

<p>
Enterprise Fraud Analytics Platform
</p>

</div>
""", unsafe_allow_html=True)

# ==================================
# TITLE
# ==================================

#st.title("🛡️ FraudShield")

# ==================================
# LOAD DATA
# ==================================

df = get_transactions()
logs_df = get_pipeline_logs()

# ==================================
# SIDEBAR FILTERS
# ==================================

st.sidebar.header("Filters")

selected_city = st.sidebar.selectbox(
    "City",
    ["All"] + sorted(df["city"].unique().tolist())
)

selected_risk = st.sidebar.selectbox(
    "Risk Level",
    ["All"] + sorted(df["risk_level"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["category"].unique().tolist())
)

# ==================================
# APPLY FILTERS
# ==================================

filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["city"] == selected_city
    ]

if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["risk_level"] == selected_risk
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

if filtered_df.empty:
    st.warning(
        "No transactions match the current filters. Clear one or more filters to see results."
    )
    st.stop()
# ===============================
# ALERT BANNER
# ===============================

high_fraud = len(
    filtered_df[
        filtered_df["fraud_score"] > 50
    ]
)

if high_fraud > 0:
    st.error(
        f"🚨 {high_fraud} High Risk Transactions Detected"
    )

# ===============================
# EXECUTIVE SUMMARY
# ===============================

top_city = (
    safe_top_value(filtered_df["city"])
)

top_merchant = (
    safe_top_value(filtered_df["merchant"])
)

top_risk = (
    safe_top_value(filtered_df["risk_level"])
)

st.subheader("📋 Executive Summary")

s1, s2, s3 = st.columns(3)

with s1:
    st.success(
        f"🏙 Top City\n\n{top_city}"
    )

with s2:
    st.success(
        f"🏪 Top Merchant\n\n{top_merchant}"
    )

with s3:
    st.success(
        f"⚠ Most Common Risk\n\n{top_risk}"
    )

# ===============================
# CORE KPI CARDS
# ===============================

total_transactions = len(
    filtered_df
)

fraud_transactions = (
    filtered_df["fraud_flag"]
    .sum()
)

fraud_rate = round(
    (
        fraud_transactions
        /
        total_transactions
    ) * 100,
    2
)

total_amount = (
    filtered_df["amount"]
    .sum()
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💳 Transactions",
        f"{total_transactions:,}"
    )

with col2:
    st.metric(
        "🚨 Frauds",
        fraud_transactions
    )

with col3:
    st.metric(
        "⚠ Fraud %",
        f"{fraud_rate}%"
    )

with col4:
    st.metric(
        "💰 Amount",
        f"₹{total_amount:,.0f}"
    )

# ===============================
# BUSINESS KPIs
# ===============================

avg_amount = round(
    filtered_df["amount"]
    .mean(),
    2
)

avg_fraud_score = round(
    filtered_df["fraud_score"]
    .mean(),
    2
)

high_risk_pct = round(
    (
        len(
            filtered_df[
                filtered_df["risk_level"]
                .isin(
                    ["High", "Critical"]
                )
            ]
        )
        /
        len(filtered_df)
    ) * 100,
    2
)

top_category = (
    safe_top_value(filtered_df["category"])
)

st.divider()

st.subheader(
    "📊 Business KPIs"
)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Avg Amount",
        f"₹{avg_amount:,.0f}"
    )

with k2:
    st.metric(
        "Avg Fraud Score",
        avg_fraud_score
    )

with k3:
    st.metric(
        "High Risk %",
        f"{high_risk_pct}%"
    )

with k4:
    st.metric(
        "Top Category",
        top_category
    )
# ==================================
# FRAUD PIE CHART
# ==================================

st.divider()

st.subheader("Fraud vs Genuine")

fraud_counts = (
    filtered_df["fraud_flag"]
    .value_counts()
    .reset_index()
)

fraud_counts.columns = [
    "Fraud Status",
    "Count"
]

fig = px.pie(
    fraud_counts,
    names="Fraud Status",
    values="Count",
    title="Fraud vs Genuine Transactions"
)

st.plotly_chart(
    fig,
    width="stretch",
    key="fraud_pie_chart"
)

# ==================================
# RISK DISTRIBUTION
# ==================================

st.divider()

st.subheader("Risk Distribution")

risk_df = (
    filtered_df["risk_level"]
    .value_counts()
    .reset_index()
)

risk_df.columns = [
    "Risk Level",
    "Count"
]

risk_fig = px.bar(
    risk_df,
    x="Risk Level",
    y="Count",
    title="Transactions by Risk Level"
)

st.plotly_chart(
    risk_fig,
    width="stretch",
    key="risk_distribution_chart"
)
# ==================================
# TOP CITIES
# ==================================

st.divider()

st.subheader("Top Cities")

city_df = (
    filtered_df["city"]
    .value_counts()
    .head(10)
    .reset_index()
)

city_df.columns = [
    "City",
    "Transactions"
]

city_fig = px.bar(
    city_df,
    x="City",
    y="Transactions",
    title="Top 10 Cities by Transactions"
)

st.plotly_chart(
    city_fig,
    width="stretch",
    key="top_cities_chart"
)

# ==================================
# TOP MERCHANTS
# ==================================

st.divider()

st.subheader("Top Merchants")

merchant_df = (
    filtered_df["merchant"]
    .value_counts()
    .head(10)
    .reset_index()
)

merchant_df.columns = [
    "Merchant",
    "Transactions"
]

merchant_fig = px.bar(
    merchant_df,
    x="Merchant",
    y="Transactions",
    title="Top 10 Merchants"
)

st.plotly_chart(
    merchant_fig,
    width="stretch",
    key="top_merchants_chart"
)

#==========================
#Fraud Score Distribution
#==========================


st.divider()

st.subheader("Fraud Score Distribution")

fig = px.histogram(
    filtered_df,
    x="fraud_score",
    nbins=20,
    title="Fraud Score Distribution"
)

st.plotly_chart(
    fig,
    width="stretch",
    key="fraud_score_chart"
)
#==================
#Top Fraud Cities
#==================

st.divider()

st.subheader(
    "Top Fraud Cities"
)

fraud_city_df = (
    filtered_df[
        filtered_df["fraud_flag"] == True
    ]["city"]
    .value_counts()
    .head(10)
    .reset_index()
)

fraud_city_df.columns = [
    "City",
    "Fraud Count"
]

fig = px.bar(
    fraud_city_df,
    x="City",
    y="Fraud Count",
    title="Top Fraud Cities"
)

st.plotly_chart(
    fig,
    width="stretch"
)
#====================
#top fraud merchants
#====================


st.divider()

st.subheader(
    "Top Fraud Merchants"
)

fraud_merchant_df = (
    filtered_df[
        filtered_df["fraud_flag"] == True
    ]["merchant"]
    .value_counts()
    .head(10)
    .reset_index()
)

fraud_merchant_df.columns = [
    "Merchant",
    "Fraud Count"
]

fig = px.bar(
    fraud_merchant_df,
    x="Merchant",
    y="Fraud Count",
    title="Top Fraud Merchants"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ==================================
# FRAUD TREND
# ==================================

st.divider()

st.subheader("Fraud Trend")

trend_df = filtered_df.copy()

trend_df["transaction_time"] = pd.to_datetime(
    trend_df["transaction_time"]
)

trend_df["date"] = (
    trend_df["transaction_time"]
    .dt.date
)

trend_df = (
    trend_df
    .groupby("date")
    .size()
    .reset_index(name="Transactions")
)

trend_fig = px.line(
    trend_df,
    x="date",
    y="Transactions",
    title="Transaction Trend Over Time"
)

st.plotly_chart(
    trend_fig,
    width="stretch"
)
# ==================================
# PIPELINE LOGS
# ==================================

st.divider()

st.subheader("Latest Pipeline Run")

st.dataframe(
    logs_df.head(1),
    width="stretch"
)