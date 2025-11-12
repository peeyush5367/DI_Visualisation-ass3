# File: pairplot_mpg_weight_horsepower.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
mpg = sns.load_dataset('mpg')

# Select relevant columns
selected = mpg[['mpg', 'weight', 'horsepower']]

# Pairplot
sns.pairplot(selected, diag_kind='kde')
plt.suptitle("Pairplot for MPG, Weight, and Horsepower", y=1.02)
plt.show()
