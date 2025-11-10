import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("LABSHEET 3/sales_data.csv")
sns.lmplot(data=df, x='Sales', y='Profit', hue='Region', col='Region')
plt.suptitle("Sales vs Profit per Region with Regression Line", y=1.03)
plt.show()
