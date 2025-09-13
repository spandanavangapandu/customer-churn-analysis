# Exploratory Data Analysis for Customer Churn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("data/Customer Churn-Dataset.xlsx")

# Basic Info
print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print("Missing values:\n", df.isnull().sum())

# Churn distribution
sns.countplot(x="Churn", data=df)
plt.title("Churn Distribution")
plt.show()

# Contract type breakdown
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Contract Type vs Churn")
plt.show()

# Payment Method breakdown
sns.countplot(y="PaymentMethod", hue="Churn", data=df)
plt.title("Payment Method vs Churn")
plt.show()

# Tenure distribution
sns.histplot(df["tenure"], kde=True, bins=30)
plt.title("Tenure Distribution")
plt.show()

# Monthly Charges
sns.histplot(df["MonthlyCharges"], kde=True, bins=30, hue=df["Churn"])
plt.title("Monthly Charges Distribution by Churn")
plt.show()

# Correlation heatmap (numerical features)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
