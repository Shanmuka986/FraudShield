import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from db import get_transactions
from dashboard.theme import apply_dashboard_theme

st.set_page_config(
    page_title="Fraud Heatmap",
    page_icon="🔥",
    layout="wide"
)

apply_dashboard_theme()

st.title("🔥 Fraud Heatmap")

df = get_transactions()

st.subheader(
    "City vs Risk Level"
)

heatmap_data = pd.crosstab(
    df["city"],
    df["risk_level"]
)

fig, ax = plt.subplots(
    figsize=(12, 6)
)

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt="d",
    cmap="Reds",
    linewidths=.5,
    ax=ax
)

st.pyplot(fig)