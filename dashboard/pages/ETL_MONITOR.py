import streamlit as st
from db import get_pipeline_logs

st.title("⚙️ ETL Monitor")

logs = get_pipeline_logs()

st.dataframe(
    logs,
    use_container_width=True
)