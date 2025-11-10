import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
plt.scatter(df['Sales'], df['Profit'], s=df['Customers']*5)
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()
