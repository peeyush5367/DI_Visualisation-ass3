import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("LABSHEET 3/sales_data.csv")
p = df.pivot_table(index='Month', columns='Region', values='Profit', aggfunc='sum')
p.plot(kind='bar')
plt.title("Profit by Region")
plt.show()
