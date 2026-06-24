
import streamlit as st
import pandas as pd
from io import BytesIO
from dashboard.chart_export import (
    save_plotly_chart
)

import plotly.express as px
try:
    from dashboard.db import get_transactions
except ModuleNotFoundError:
    from db import get_transactions
from dashboard.theme import apply_dashboard_theme, safe_mode_value, safe_top_value

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image
)
from reportlab.lib.styles import (
    getSampleStyleSheet
)

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Reports Center",
    page_icon="📥",
    layout="wide"
)

apply_dashboard_theme()

st.title("📥 Reports Center")

# ==================================
# LOAD DATA
# ==================================

df = get_transactions()

st.success(
    f"{len(df):,} records available"
)

# ==================================
# FILTERS
# ==================================

st.markdown("---")

st.subheader("🔍 Report Filters")

col1, col2 = st.columns(2)

with col1:

    city = st.selectbox(
        "City",
        ["All"] + sorted(
            df["city"].unique()
        )
    )

with col2:

    risk = st.selectbox(
        "Risk Level",
        ["All"] + sorted(
            df["risk_level"].unique()
        )
    )

filtered_df = df.copy()

if city != "All":

    filtered_df = filtered_df[
        filtered_df["city"] == city
    ]

if risk != "All":

    filtered_df = filtered_df[
        filtered_df["risk_level"] == risk
    ]

if filtered_df.empty:
    st.warning(
        "No records match the current report filters. Try a broader city or risk level."
    )
    st.stop()

# ==================================
# REPORT PREVIEW
# ==================================

st.markdown("---")

st.subheader("📊 Report Preview")

total_transactions = len(
    filtered_df
)

fraud_transactions = (
    filtered_df["fraud_flag"]
    .sum()
)

top_city = (
    safe_mode_value(filtered_df["city"])
)

top_merchant = (
    safe_mode_value(filtered_df["merchant"])
)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Transactions",
        total_transactions
    )

with p2:
    st.metric(
        "Frauds",
        fraud_transactions
    )

with p3:
    st.metric(
        "Top City",
        top_city
    )

with p4:
    st.metric(
        "Top Merchant",
        top_merchant
    )

# ==================================
# CSV EXPORTS
# ==================================

st.markdown("---")

st.header("📄 CSV Exports")

csv_data = df.to_csv(
    index=False
)

st.download_button(
    "📄 Download Full Dataset CSV",
    csv_data,
    "all_transactions.csv",
    "text/csv"
)

fraud_df = df[
    df["fraud_flag"] == True
]

fraud_csv = fraud_df.to_csv(
    index=False
)

st.download_button(
    "🚨 Download Fraud CSV",
    fraud_csv,
    "fraud_transactions.csv",
    "text/csv"
)

filtered_csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    "📊 Download Filtered CSV",
    filtered_csv,
    "filtered_transactions.csv",
    "text/csv"
)

# ==================================
# EXCEL EXPORTS
# ==================================

st.markdown("---")

st.header("📗 Excel Exports")

def to_excel(dataframe):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        dataframe.to_excel(
            writer,
            index=False,
            sheet_name="Transactions"
        )

    return output.getvalue()

excel_data = to_excel(df)

st.download_button(
    "📗 Download Full Excel",
    excel_data,
    "all_transactions.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

fraud_excel = to_excel(
    fraud_df
)

st.download_button(
    "🚨 Download Fraud Excel",
    fraud_excel,
    "fraud_transactions.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

filtered_excel = to_excel(
    filtered_df
)

st.download_button(
    "📊 Download Filtered Excel",
    filtered_excel,
    "filtered_transactions.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

def export_dashboard_charts(df):

    fraud_counts = (
        df["fraud_flag"]
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
        values="Count"
    )

    save_plotly_chart(
        fig,
        "fraud_pie.png"
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
        y="Count"
    )

    save_plotly_chart(
        fig,
        "risk_distribution.png"
    )

    city_df = (
        df["city"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    city_df.columns = [
        "City",
        "Transactions"
    ]

    fig = px.bar(
        city_df,
        x="City",
        y="Transactions"
    )

    save_plotly_chart(
        fig,
        "top_cities.png"
    )

    merchant_df = (
        df["merchant"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    merchant_df.columns = [
        "Merchant",
        "Transactions"
    ]

    fig = px.bar(
        merchant_df,
        x="Merchant",
        y="Transactions"
    )

    save_plotly_chart(
        fig,
        "top_merchants.png"
    )
# ==================================
# PDF GENERATOR
# ==================================

def create_pdf_report(df):

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer
    )

    styles = getSampleStyleSheet()

    content = []

    total_transactions = len(df)

    fraud_transactions = (
        df["fraud_flag"]
        .sum()
    )

    fraud_rate = round(
        (
            fraud_transactions /
            total_transactions
        ) * 100,
        2
    ) if total_transactions > 0 else 0

    total_amount = round(
        df["amount"].sum(),
        2
    )

    avg_amount = round(
        df["amount"].mean(),
        2
    )

    avg_fraud_score = round(
        df["fraud_score"].mean(),
        2
    )

    top_city = safe_top_value(df["city"])

    top_merchant = safe_top_value(df["merchant"])

    top_risk = safe_top_value(df["risk_level"])

    top_category = safe_top_value(df["category"])

    content.append(
        Paragraph(
            "FraudShield Executive Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Total Transactions: {total_transactions}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Fraud Transactions: {fraud_transactions}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Fraud Rate: {fraud_rate}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Total Amount: ₹{total_amount:,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            "Business KPIs",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Average Transaction Amount: ₹{avg_amount:,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Fraud Score: {avg_fraud_score}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top Category: {top_category}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            "Insights",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Top City: {top_city}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top Merchant: {top_merchant}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Most Common Risk Level: {top_risk}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            f"Generated On: {pd.Timestamp.now()}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    pdf_buffer.seek(0)

    return pdf_buffer

# ==================================
# ENTERPRISE PDF FUNCTION
# ==================================

def create_enterprise_pdf(df):

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer
    )

    styles = getSampleStyleSheet()

    content = []

    # COVER PAGE

    content.append(
        Paragraph(
            "FraudShield",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Enterprise Fraud Analytics Report",
            styles["Heading1"]
        )
    )

    content.append(
        Spacer(1, 50)
    )

    content.append(
        Paragraph(
            f"Generated On: {pd.Timestamp.now()}",
            styles["BodyText"]
        )
    )

    content.append(
        PageBreak()
    )

    # EXECUTIVE SUMMARY

    total_transactions = len(df)

    fraud_transactions = (
        df["fraud_flag"]
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

    total_amount = round(
        df["amount"]
        .sum(),
        2
    )

    avg_amount = round(
        df["amount"]
        .mean(),
        2
    )

    avg_fraud_score = round(
        df["fraud_score"]
        .mean(),
        2
    )

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

    top_category = (
        df["category"]
        .value_counts()
        .idxmax()
    )

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Total Transactions: {total_transactions}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Fraud Transactions: {fraud_transactions}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Fraud Rate: {fraud_rate}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Total Amount: ₹{total_amount:,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Transaction Amount: ₹{avg_amount:,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Fraud Score: {avg_fraud_score}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top City: {top_city}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top Merchant: {top_merchant}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Most Common Risk Level: {top_risk}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Top Category: {top_category}",
            styles["BodyText"]
        )
    )

    content.append(
        PageBreak()
    )

    # CHARTS

    chart_files = [
        (
            "Fraud vs Genuine",
            "reports/charts/fraud_pie.png"
        ),
        (
            "Risk Distribution",
            "reports/charts/risk_distribution.png"
        ),
        (
            "Top Cities",
            "reports/charts/top_cities.png"
        ),
        (
            "Top Merchants",
            "reports/charts/top_merchants.png"
        )
    ]

    for title, path in chart_files:

        content.append(
            Paragraph(
                title,
                styles["Heading2"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        try:

            content.append(
                Image(
                    path,
                    width=450,
                    height=250
                )
            )

        except Exception:

            content.append(
                Paragraph(
                    "Chart Not Available",
                    styles["BodyText"]
                )
            )

        content.append(
            PageBreak()
        )

    doc.build(content)

    pdf_buffer.seek(0)

    return pdf_buffer


# ==================================
# PDF REPORTS
# ==================================

st.markdown("---")

st.header("📑 PDF Reports")

if st.button(
    "Generate Chart Exports"
):
    export_dashboard_charts(
        filtered_df
    )

pdf_file = create_pdf_report(
    filtered_df
)

enterprise_pdf = create_enterprise_pdf(
    filtered_df
)

st.download_button(
    "📑 Executive PDF Report",
    pdf_file,
    "FraudShield_Report.pdf",
    "application/pdf"
)

st.download_button(
    "📊 Enterprise Analytics Report",
    enterprise_pdf,
    "FraudShield_Enterprise_Report.pdf",
    "application/pdf"
)
