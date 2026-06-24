import streamlit as st
from db import get_transactions
from dashboard.theme import apply_dashboard_theme, safe_top_value

apply_dashboard_theme()

st.title("🤖 AI Insights")

df = get_transactions()

top_city = (
    safe_top_value(df["city"])
)

top_merchant = (
    safe_top_value(df["merchant"])
)

top_risk = (
    safe_top_value(df["risk_level"])
)

st.info(
    f"Top Transaction City: {top_city}"
)

st.info(
    f"Top Merchant: {top_merchant}"
)

st.info(
    f"Most Common Risk Level: {top_risk}"
)