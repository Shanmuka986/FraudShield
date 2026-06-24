import streamlit as st
import pandas as pd

from db import (
    get_transactions,
    get_pipeline_logs
)

st.set_page_config(
    page_title="Data Quality Monitor",
    page_icon="📋",
    layout="wide"
)

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

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Rows",
    total_rows
)

c2.metric(
    "Duplicate Rows",
    duplicate_rows
)

c3.metric(
    "Missing Values",
    missing_values
)

c4.metric(
    "Quality Score",
    f"{quality_score}%"
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