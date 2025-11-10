import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("students_performance.csv")

sns.lmplot(data=df, x='Study_Hours', y='Math_Score', hue='Gender')
plt.show()
