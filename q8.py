import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("LABSHEET 3/students_performance.csv")

sns.barplot(data=df, x='Class', y='Math_Score', hue='Gender', palette='Set2')
plt.show()
