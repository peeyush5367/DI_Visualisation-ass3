# File: scatter_gdp_happiness.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('LABSHEET 3/country_data.csv')

# Scatter plot
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=data,
    x='GDP_per_capita',
    y='Happiness_Index',
    size='Internet_Users',
    hue='Literacy_Rate',
    sizes=(50, 400),
    palette='viridis',
    alpha=0.8,
    edgecolor='black'
)

plt.title("GDP per Capita vs Happiness Index\n(Size = Internet Users, Color = Literacy Rate)")
plt.xlabel("GDP per Capita (USD)")
plt.ylabel("Happiness Index")
plt.legend(title="Literacy Rate / Internet Users", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
