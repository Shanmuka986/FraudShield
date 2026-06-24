import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_transactions

st.title("🚨 Fraud Analytics")

df = get_transactions()

fraud_df = df[
    df["fraud_flag"] == True
]

st.metric(
    "Total Fraud Cases",
    len(fraud_df)
)

city_df = (
    fraud_df["city"]
    .value_counts()
    .head(10)
    .reset_index()
)

city_df.columns = [
    "City",
    "Fraud Count"
]

fig = px.bar(
    city_df,
    x="City",
    y="Fraud Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)