# File: filtered_regression_lmplot.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
mpg = sns.load_dataset('mpg')

# Filter data
filtered = mpg[(mpg['mpg'] < 50) & (mpg['weight'] < 5000)]

# Regression plot
sns.lmplot(data=filtered, x='weight', y='mpg', height=6, aspect=1.2, scatter_kws={'alpha':0.6})
plt.title("Regression Plot (Filtered: mpg < 50, weight < 5000)")
plt.show()
