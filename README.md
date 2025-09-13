# Customer Churn Analysis using Power BI

## 📌 Project Overview
This project focuses on analyzing customer churn in the telecom industry using **Power BI dashboards**.  
The dataset contains customer demographics, subscription details, payment methods, and churn status.  
The goal is to identify **key factors influencing churn** and provide actionable insights.

---
## 📊 Dashboards
- **Customer Churn Dashboard** → Shows overall churn rates, customer demographics, and service usage.
- **Customer Risk Analysis Dashboard** → Highlights high-risk customer groups and churn probability patterns.

---
## 🗂 Dataset
- Source: `data/Customer Churn-Dataset.xlsx`
- Rows: ~7000 customers
- Key Columns:
  - `gender`, `SeniorCitizen`, `Partner`, `Dependents`
  - `tenure`, `Contract`, `MonthlyCharges`, `TotalCharges`
  - `PaymentMethod`, `InternetService`, `TechSupport`
  - `Churn` (Target Variable)

---
## 🔍 Exploratory Data Analysis (EDA)
Run the Python script `eda_script.py` to explore the dataset.  
It covers:
- Missing value checks
- Churn distribution
- Categorical breakdowns (Contract type, Payment Method, Internet Service)
- Numerical analysis (Tenure, Charges)
---
## 🚀 How to Use
1. Open the Power BI dashboards from the `dashboards/` folder.
2. Run the EDA script (`eda_script.py`) for data exploration.
3. Refer to `README.md` for project details.

---
## 📷 Screenshots
- Churn Dashboard  
  ![Churn Dashboard](images/Customer%20Churn%20Dashboard.png)

- Risk Analysis Dashboard  
  ![Risk Analysis](images/Customer%20Risk%20Analysis.png)

## ▶️ Running EDA Script
```bash
# Install dependencies
pip install -r requirements.txt

# Run EDA
python eda_script.py
---
## ✅ Key Insights
- Month-to-month contracts and electronic check payments have **higher churn**.
- Customers with **shorter tenure (<12 months)** are at greater risk.
- Lack of tech support and online security is linked to higher churn.
- Fiber optic internet customers churn more than DSL users.

---
## 📁 Project Structure
```
Customer-Churn-Analysis/
│── dashboards/                 # Power BI Dashboards
│   ├── Customer Churn Dashboard.pbix
│   ├── Customer Risk Analysis Dashboard.pbix
│
│── data/                       # Dataset
│   ├── Customer Churn-Dataset.xlsx
│
│── images/                     # Dashboard Screenshots
│   ├── Customer Churn Dashboard.png
│   ├── Customer Risk Analysis.png
│── requirements.txt            #required python dependencies
│── eda_script.py               # EDA in Python
│── README.md                   # Documentation
```
