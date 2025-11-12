# File: correlation_heatmap.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
mpg = sns.load_dataset('mpg')

# Compute correlation
corr = mpg.corr(numeric_only=True)

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap for mpg Dataset")
plt.show()
