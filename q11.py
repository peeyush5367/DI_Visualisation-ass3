# File: scatter_totalbill_tip.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='day',
    size='size',
    sizes=(20, 200),
    palette='viridis',
    alpha=0.8
)
plt.title("Scatter Plot of Total Bill vs Tip (Color=Day, Size=Party Size)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(title="Day / Size", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
