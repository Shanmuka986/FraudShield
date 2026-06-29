# 🛡️ FraudShield - Enterprise Fraud Analytics Platform

<p align="center">

Enterprise-grade Fraud Analytics Platform with Automated ETL Pipelines, Cloud Database Integration, Interactive Dashboards, Data Quality Monitoring, Automated Reporting, and Daily GitHub Actions Automation.

</p>

---

# 📌 Overview

FraudShield is an enterprise-level fraud analytics platform developed to simulate, process, analyze, and monitor financial transactions using modern Data Engineering and Data Analytics practices.

The platform automatically generates synthetic financial transaction data, executes an end-to-end ETL pipeline, performs data validation and quality checks, stores clean data in a cloud PostgreSQL database, and presents real-time business intelligence through interactive Streamlit dashboards.

The entire ETL pipeline is automated using GitHub Actions, allowing the system to refresh itself daily without any manual intervention.

---

# 🚀 Live Demo

🌐 Live Application

https://github.com/Shanmuka986/FraudShield

💻 GitHub Repository

https://fraudshield-analytics.streamlit.app/

---

# ✨ Features

## 📊 Executive Dashboard

- Executive Business KPIs
- Fraud Rate Monitoring
- Transaction Statistics
- Risk Distribution
- Fraud Score Analysis
- Business Summary

---

## 🚨 Fraud Analytics

- Fraud vs Genuine Transactions
- Risk Level Distribution
- Fraud Score Distribution
- Merchant-wise Fraud Analysis
- Category Analysis
- City-wise Fraud Analytics

---

## 🌍 Fraud Heatmap

- Geographic Fraud Distribution
- City Level Risk Analysis
- Regional Fraud Trends

---

## ⚠ Alert Management

- Critical Risk Alerts
- High Risk Transactions
- Suspicious Activity Monitoring
- Fraud Investigation Support

---

## 📋 Data Quality Monitor

- Missing Value Detection
- Duplicate Detection
- Quality Score Calculation
- Pipeline Health Monitoring
- ETL Execution Logs

---

## 🔍 Transaction Explorer

- Search Transactions
- Filter by Merchant
- Filter by City
- Filter by Risk Level
- Filter by Fraud Status

---

## 📈 Risk Monitor

- Risk Distribution
- Fraud Probability
- High Risk Merchant Tracking
- Critical Transaction Monitoring

---

## 📄 Reports Center

Generate

- CSV Reports
- Excel Reports
- Executive PDF Reports
- Enterprise Analytics Reports

---

## 🤖 AI Insights

Automatically generates business insights including:

- Fraud Trends
- Business Recommendations
- Risk Analysis
- Transaction Summary

---

# ⚙ Automated ETL Pipeline

Every day GitHub Actions automatically executes the complete ETL pipeline.

## Workflow

Generate Transactions

↓

Extract Data

↓

Transform Data

↓

Duplicate Removal

↓

Missing Value Handling

↓

Data Validation

↓

Quality Score Calculation

↓

Load to PostgreSQL

↓

Pipeline Logging

↓

Dashboard Refresh

---

# 🔄 ETL Pipeline Explained

## Extract

Reads newly generated transaction data.

- CSV Extraction
- Pandas DataFrame Loading

---

## Transform

Performs complete data preprocessing.

- Remove Duplicate Records
- Handle Missing Values
- Validate Fraud Scores
- Data Cleaning
- Risk Classification
- Quality Score Calculation

---

## Load

Loads clean data into Supabase PostgreSQL.

- Delete Previous Transactions
- Insert Latest Transactions
- Update Pipeline Logs

---

# 🤖 GitHub Actions Automation

FraudShield uses GitHub Actions for complete pipeline automation.

Every day GitHub

- Creates Ubuntu Runner
- Installs Python
- Installs Dependencies
- Loads GitHub Secrets
- Executes ETL Pipeline
- Updates Cloud Database
- Logs Pipeline Status

No manual execution is required.

---

# 🏗 System Architecture

```
                GitHub Actions
                       │
          Daily ETL Workflow Trigger
                       │
                       ▼
          Ubuntu Virtual Machine
                       │
                       ▼
        Install Dependencies
                       │
                       ▼
             Execute main.py
                       │
                       ▼
          Transaction Generator
                       │
                       ▼
                 Extract
                       │
                       ▼
               Transform
      • Duplicate Removal
      • Missing Value Handling
      • Validation
                       │
                       ▼
                  Load
                       │
                       ▼
        Supabase PostgreSQL
                       │
                       ▼
        Streamlit Dashboard
```

---

# 🗂 Project Structure

```
FraudShield/

│

├── dashboard/
│
├── simulator/
│
├── etl/
│
├── database/
│
├── .github/
│     └── workflows/
│
├── data/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

# 🛠 Technology Stack

## Programming Language

- Python

---

## Frontend

- Streamlit

---

## Visualization

- Plotly

---

## Data Engineering

- Pandas
- NumPy

---

## Database

- PostgreSQL
- Supabase

---

## ORM

- SQLAlchemy

---

## Automation

- GitHub Actions

---

## Reporting

- ReportLab
- OpenPyXL

---

## Version Control

- Git
- GitHub

---

# 📊 Database

Cloud Database

Supabase PostgreSQL

Main Tables

- transactions
- pipeline_logs

---

# 📈 Dashboard Modules

- Executive Dashboard
- Fraud Analytics
- Fraud Heatmap
- Risk Monitor
- Alert Center
- Data Quality Monitor
- Reports Center
- AI Insights
- Transaction Explorer

---

# 📊 Data Quality

FraudShield continuously monitors

- Duplicate Records
- Missing Values
- Data Completeness
- ETL Health
- Pipeline Success
- Pipeline Duration

---

# 📑 Reports

Users can download

- CSV
- Excel
- Executive PDF
- Enterprise Reports

---

# 🔒 Security

Sensitive credentials are never stored in the repository.

Uses

- GitHub Secrets
- Streamlit Secrets
- Environment Variables

Database credentials remain fully protected.

---

# 📌 Skills Demonstrated

## Data Engineering

- ETL Pipeline Development
- Data Validation
- Data Cleaning
- Data Wrangling

---

## Data Analytics

- Exploratory Data Analysis
- KPI Dashboard
- Statistical Analysis
- Fraud Analytics

---

## Database

- PostgreSQL
- SQLAlchemy
- Cloud Database Integration

---

## Automation

- GitHub Actions
- Daily ETL Scheduling
- Cloud Automation

---

## Dashboard Development

- Streamlit
- Interactive Charts
- Business Intelligence
- Data Visualization

---

## Reporting

- PDF Reports
- Excel Reports
- CSV Export

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of

- Data Engineering
- ETL Development
- Business Intelligence
- Dashboard Development
- Cloud Database Integration
- Data Analytics
- Automation using GitHub Actions
- Enterprise Reporting
- Fraud Analytics

---

# 🚀 Future Enhancements

- Machine Learning Fraud Detection
- Real-time Fraud Prediction
- Kafka Streaming
- Docker Deployment
- Kubernetes
- REST API
- Authentication
- Role Based Access
- AI Chat Assistant
- Predictive Fraud Analysis

---

# 👨‍💻 Author

**Thugadam Shanmuka Sai**

B.Tech Computer Science & Engineering (AI & ML)

Madanapalle Institute of Technology & Science

Graduation Year: **2027**

---

# 📜 License

Copyright © 2026 Thugadam Shanmuka Sai

All Rights Reserved.

This project is proprietary and intended for educational, research, and portfolio purposes.

Unauthorized copying, redistribution, modification, or commercial use without prior written permission from the author is prohibited.

---

⭐ If you found this project interesting, consider giving it a star!
