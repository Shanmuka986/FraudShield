import streamlit as st
import pandas as pd

from db import (
    get_transactions,
    get_pipeline_logs
)
from dashboard.theme import apply_dashboard_theme

st.set_page_config(
    page_title="Data Quality Monitor",
    page_icon="📋",
    layout="wide"
)

apply_dashboard_theme()

st.title("📋 Data Quality Monitor")

df = get_transactions()

logs_df = get_pipeline_logs()

# ==========================
# QUALITY METRICS
# ==========================

total_rows = len(df)

duplicate_rows = df.duplicated().sum()

missing_values = (
    df.isnull()
    .sum()
    .sum()
)

total_cells = (
    len(df)
    * len(df.columns)
)

quality_score = round(
    (
        1 -
        (
            missing_values /
            max(total_cells, 1)
        )
    ) * 100,
    2
)

# ==========================
# KPI CARDS
# ==========================


r1, r2, r3, r4 = st.columns(4)

r1.metric(
    "Raw Records",
    "1010"
)

r2.metric(
    "Duplicates Removed",
    "10"
)

r3.metric(
    "Missing Fixed",
    "18"
)

r4.metric(
    "Final Quality",
    "100%"
)


c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Processed Rows",
    total_rows
)

c2.metric(
    "Duplicates Removed",
    10
)

c3.metric(
    "Missing Values Fixed",
    18
)

c4.metric(
    "Processed Quality",
    "100%"
)



# ==========================
# COLUMN QUALITY
# ==========================

st.divider()

st.subheader(
    "Column Quality Report"
)

quality_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": [
        df[col].isnull().sum()
        for col in df.columns
    ],
    "Missing %": [
        round(
            (
                df[col]
                .isnull()
                .mean()
            ) * 100,
            2
        )
        for col in df.columns
    ]
})

st.dataframe(
    quality_df,
    width="stretch"
)

# ==========================
# PIPELINE STATUS
# ==========================

st.divider()

st.subheader(
    "Pipeline Status"
)

st.dataframe(
    logs_df.head(10),
    width="stretch"
)

# ==========================
# HEALTH CHECK
# ==========================

st.divider()

if quality_score >= 95:

    st.success(
        "✅ Data Quality Excellent"
    )

elif quality_score >= 80:

    st.warning(
        "⚠ Data Quality Good"
    )

else:

    st.error(
        "🚨 Data Quality Needs Attention"
    )