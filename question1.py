import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("LABSHEET 3/sales_data.csv")
# df=pd.removeduplicate() 
# print(df)
# 1. Line chart: monthly sales for both regions
plt.figure(figsize=(10,5))
for region, group in df.groupby('Region'):
    # aggregate monthly sales
    monthly = group.groupby('Month')['Sales'].sum()
    plt.plot(monthly.index, monthly.values, marker='o', label=region)
plt.title("Monthly Sales by Region")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(title="Region")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()