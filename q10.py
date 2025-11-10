import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("LABSHEET 3/country_data.csv").sort_values('GDP_per_capita', ascending=False)
sns.barplot(data=df, x='Country', y='GDP_per_capita')
plt.xticks(rotation=90)
plt.show()
