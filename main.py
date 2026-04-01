import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

print(df.head())

category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind='bar', title="Sales by Region")
plt.show()