# File: facetgrid_time_smoker.py
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# FacetGrid for time and smoker
g = sns.FacetGrid(tips, col='time', row='smoker', height=4, aspect=1)
g.map_dataframe(sns.scatterplot, x='total_bill', y='tip', color='teal', alpha=0.7)
g.set_axis_labels("Total Bill ($)", "Tip ($)")
g.add_legend()
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Scatter Plots Faceted by Time and Smoker")
plt.show()
