# File: bar_gdp_by_country.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('LABSHEET 3/country_data.csv')

# Sort data by GDP_per_capita
sorted_data = data.sort_values('GDP_per_capita', ascending=False)

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=sorted_data, x='Country', y='GDP_per_capita', palette='coolwarm')
plt.title("GDP per Capita by Country (Sorted)")
plt.xlabel("Country")
plt.ylabel("GDP per Capita (USD)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
