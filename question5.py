import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("LABSHEET 3/students_performance.csv")

sns.boxplot(data=df, x='Gender', y='Math_Score')
plt.show()
