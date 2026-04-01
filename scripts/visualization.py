import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-- Loading datasets:

card_type_df = pd.read_csv(r"C:\Users\Gabriel\Desktop\eda\outputs\tables\avg_spending_by_card_type.csv")
education_df = pd.read_csv(r"C:\Users\Gabriel\Desktop\eda\outputs\tables\avg_spending_by_education.csv")
gender_df = pd.read_csv(r"C:\Users\Gabriel\Desktop\eda\outputs\tables\avg_spending_by_gender.csv")
inactive_df = pd.read_csv(r"C:\Users\Gabriel\Desktop\eda\outputs\tables\inactive_high_credit_customers.csv")
income_df = pd.read_csv(r"C:\Users\Gabriel\Desktop\eda\outputs\tables\income_distribution.csv")

#-- Granting numeric type:

card_type_df['average_spending'] = pd.to_numeric(card_type_df['average_spending'])
education_df['average_spending'] = pd.to_numeric(education_df['average_spending'])
gender_df['average_spending'] = pd.to_numeric(gender_df['average_spending'])
inactive_df['credit_limit'] = pd.to_numeric(inactive_df['credit_limit'])
income_df['total_customers'] = pd.to_numeric(income_df['total_customers'])

#-- Set sns style:

sns.set_style('whitegrid')

#-- Data Visualization:

#- Card Type:

card_order = card_type_df.sort_values('average_spending', ascending=False)['card_type']

plt.figure(figsize=(10,6))
card_type = sns.barplot(data=card_type_df, x='card_type', y='average_spending', palette='viridis', order=card_order)
plt.xlabel('Card Type', fontsize=12)
plt.ylabel('Avg. Spending ($)', fontsize=12)
plt.title('Average Spending by Card Type', fontsize=16, fontweight='bold')

for p in card_type.patches:
  card_type.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')

sns.despine()
plt.savefig('card_type_spending.png', dpi=300, bbox_inches='tight')
plt.show()

#- Education Level:

education_df = education_df.drop(columns='total_customers')
education_order = education_df.sort_values('average_spending', ascending=False)['education_level']

plt.figure(figsize=(10,6))
education = sns.barplot(data=education_df, x='education_level', y='average_spending', palette='viridis', order=education_order)
plt.title('Average Spending by Education Level', fontsize=16, fontweight='bold')
plt.xlabel('Education Level', fontsize=12)
plt.ylabel('Average Spending ($)', fontsize=12)

for p in education.patches:
    education.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')

sns.despine()
plt.savefig('education_spending.png', dpi=300, bbox_inches='tight')
plt.show()

#- Gender spending:

gender_order = gender_df.sort_values('average_spending', ascending=False)['gender']

plt.figure(figsize=(10,6))
gender = sns.barplot(data=gender_df, x='gender', y='average_spending', palette='viridis', order=gender_order)

for p in gender.patches:
    gender.annotate(f'{p.get_height():.0f}',(p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')
    
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Avg. Spending ($)', fontsize=12)
plt.title('Average Spending by Gender', fontsize=16, fontweight='bold')
sns.despine()
plt.savefig('gender_spending.png', dpi=300, bbox_inches='tight')
plt.show()

#- Inactive customers:

inactive_df = inactive_df.drop(columns='card_type')

plt.figure(figsize=(10,6))
sns.boxplot(data=inactive_df, y='credit_limit', color='lightgray')
sns.stripplot(data=inactive_df, y='credit_limit', color='purple', alpha=0.5, size=5)
plt.title('Credit Limit Distribution of Inactive Customers (6 Months)', fontsize=16, fontweight='bold')
plt.ylabel('Credit Limit ($)')
sns.despine()
plt.savefig('inactive_credit_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

#- Income distribution:

income_order = [
    'Less than \\$40K',
    '\\$40K-\\$60K',
    '\\$60K-\\$80K',
    '\\$80K-\\$120K',
    'More than \\$120K',
    'Not informed'
]

income_df['annual_salary'] = income_df['annual_salary'].replace({
    'Less than $40K': 'Less than \\$40K',
    '$40K - $60K': '\\$40K-\\$60K',
    '$60K - $80K': '\\$60K-\\$80K',
    '$80K - $120K': '\\$80K-\\$120K',
    'More than $120K': 'More than \\$120K'
})

plt.figure(figsize=(10,6))
income = sns.barplot(data=income_df, x='annual_salary', y='total_customers', palette='viridis', order=income_order) 
plt.title('Income Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Annual Salary ($)', fontsize=12)
plt.ylabel('Total Customers', fontsize=12)

for p in income.patches:
    income.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')

sns.despine()
plt.savefig('income_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

