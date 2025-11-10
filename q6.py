import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("students_performance.csv")

sns.violinplot(data=df, x='Class', y='Reading_Score', hue='Gender', split=True)
plt.show()
