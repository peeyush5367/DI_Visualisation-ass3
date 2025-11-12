# File: regression_weight_mpg.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
mpg = sns.load_dataset('mpg')

# Regression plot
sns.lmplot(data=mpg, x='weight', y='mpg', hue='origin', height=6, aspect=1.2)
plt.title("Regression Line between Weight and MPG (by Origin)")
plt.show()
