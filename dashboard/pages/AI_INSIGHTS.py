import streamlit as st
from db import get_transactions

st.title("🤖 AI Insights")

df = get_transactions()

top_city = (
    df["city"]
    .value_counts()
    .idxmax()
)

top_merchant = (
    df["merchant"]
    .value_counts()
    .idxmax()
)

top_risk = (
    df["risk_level"]
    .value_counts()
    .idxmax()
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