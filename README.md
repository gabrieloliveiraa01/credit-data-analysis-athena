# 📊 Credit Data Analysis using SQL (Amazon Athena)

## 🎯 Objective

This project aims to analyze credit card customer data to identify patterns in customer behavior, spending habits, and financial characteristics.

The analysis focuses on understanding how different variables—such as income, education level, gender, and credit limits—relate to customer activity and spending behavior.

---

## 📁 Project Structure

```
credit-analysis/
│
├── data/
│   └── credit.csv
│
├── notebooks/
│   └── eda-using-sql-in-amazon-athena.ipynb
│
├── outputs/
│   ├── charts/
│   │   ├── card_type_spending.png
│   │   ├── education_spending.png
│   │   ├── gender_spending.png
│   │   ├── inactive_credit_distribution.png
│   │   └── income_distribution.png
│   │
│   └── tables/
│       ├── avg_spending_by_card_type.csv
│       ├── avg_spending_by_education.csv
│       ├── avg_spending_by_gender.csv
│       ├── inactive_high_credit_customers.csv
│       └── income_distribution.csv
│
└── scripts/
    └── visualization.py
```

---

## 📊 Dataset

The dataset contains **2,564 credit card customers**, including:

* Demographics (age, gender, marital status, education level)
* Financial information (income range, credit limit)
* Credit usage behavior (transactions, inactivity, product usage)

Source:
https://github.com/andre-marcos-perez/ebac-course-utils

Note:  
The original dataset was provided in Brazilian Portuguese (pt-BR) and was translated into English as part of the data preparation process to ensure consistency, improve readability, and align the project with international standards.

---

## 🛠️ Tools & Technologies

* SQL (Amazon Athena)
* Python (Pandas, Matplotlib, Seaborn)
* AWS S3
* Jupyter Notebook

---

## 🔍 Analysis Process

### 1. Data Exploration

* Verified dataset structure and data types
* Checked for missing values (e.g., "unknown")
* Identified categorical and numerical variables

---

### 2. Data Analysis (SQL - Athena)

Key analyses performed:

* Customer distribution by gender and age
* Income distribution
* Credit limit analysis
* Spending behavior by card type
* Spending differences by education level
* Identification of inactive customers with high credit limits

---

### 3. Data Visualization (Python)

Visualizations were created using Pandas, Matplotlib, and Seaborn, including:

* Average spending by card type
* Average spending by education level
* Spending comparison by gender
* Credit limit distribution for inactive customers
* Income distribution

---

## 📈 Key Insights

* Most customers earn **less than $40K annually**, indicating a concentration in lower income ranges
* Customers with **Gold cards show higher average spending**
* **Female customers have slightly higher average spending** than male customers
* Some customers with **high credit limits remain inactive for long periods**, indicating possible disengagement
* Spending behavior is influenced by multiple factors, not just income

---

## 📊 Highlight: Inactive High-Value Customers

The analysis reveals that customers inactive for 6 months can still maintain **high credit limits (up to ~$30K)**.

This suggests:

* Potential customer disengagement
* Missed revenue opportunities
* Opportunities for targeted re-engagement strategies

---

## 📂 Outputs

### Charts

* Card Type Spending Analysis
* Education Level Spending
* Gender Spending Comparison
* Credit Limit Distribution (Inactive Customers)
* Income Distribution

### Tables

* Aggregated results generated from SQL queries
* Used as input for visualization

---

## 🚀 Conclusion

This project demonstrates how SQL and Python can be combined to transform raw data into meaningful insights.

The analysis highlights how customer behavior is influenced by multiple variables and shows the importance of identifying inactive high-value customers for business strategy.

---

## 👤 Author

Gabriel Oliveira
📊 Junior Data Analyst

🔗 LinkedIn: https://www.linkedin.com/in/gabrieloliveiraa01
🔗 GitHub: https://github.com/gabrieloliveiraa01
🔗 Kaggle: https://www.kaggle.com/gabrieloliveira01

---
