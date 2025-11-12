# File: boxplot_tip_by_day.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(data=tips, x='day', y='tip', hue='time', palette='Set2')
plt.title("Boxplot of Tips by Day with Time as Hue")
plt.xlabel("Day of Week")
plt.ylabel("Tip ($)")
plt.legend(title="Time")
plt.show()
