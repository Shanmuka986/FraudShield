import streamlit as st
from db import get_pipeline_logs
from dashboard.theme import apply_dashboard_theme

apply_dashboard_theme()

st.title("⚙️ ETL Monitor")

logs = get_pipeline_logs()

st.dataframe(
    logs,
    width="stretch"
)