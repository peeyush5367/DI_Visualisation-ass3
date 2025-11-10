import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("LABSHEET 3/country_data.csv")
plt.scatter(df['GDP_per_capita'], df['Happiness_Index'], 
            s=df['Internet_Users']*3, c=df['Literacy_Rate'], cmap='viridis')
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Index")
plt.show()
