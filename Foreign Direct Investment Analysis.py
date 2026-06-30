# Generated from: Foreign Direct Investment Analysis.ipynb
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/content/drive/MyDrive/FDI data.csv"  # Replace with your file path
data = pd.read_csv(file_path)

# Display basic info
print(data.info())
print(data.describe())

# Data Cleaning
# Ensure sector names and columns are clean
data.columns = data.columns.str.strip()
data['Sector'] = data['Sector'].str.strip()

# Add a Total column for each sector
data['Total'] = data.iloc[:, 1:].sum(axis=1)


# Summarizing Data
yearly_totals = data.iloc[:, 1:-1].sum()  # Sum across all sectors for each year
sector_totals = data.groupby('Sector')['Total'].sum().sort_values(ascending=False)

# Top Sectors by Total FDI
top_sectors = sector_totals.head(10)
print("Top 10 Sectors by FDI Inflows:")
print(top_sectors)

# Visualization: Sector-wise Total FDI
plt.figure(figsize=(10, 6))
top_sectors.plot(kind='bar', color='skyblue')
plt.title("Top 10 Sectors by Total FDI Inflows (2000-2017)", fontsize=14)
plt.ylabel("Total FDI (in million USD)", fontsize=12)
plt.xticks(rotation=15, ha='right')
plt.show()

# Year-wise Total FDI
plt.figure(figsize=(12, 6))
yearly_totals.plot(kind='line', marker='o', color='purple')
plt.title("Year-wise Total FDI Inflows (2000-2017)", fontsize=14)
plt.ylabel("Total FDI (in million USD)", fontsize=12)
plt.xlabel("Year", fontsize=12)
plt.grid(True)
plt.show()

# Correlation Analysis
corr_matrix = data.iloc[:, 1:-1].corr()
plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix, cmap="YlGnBu", annot=False, cbar=True)
plt.title("Correlation Heatmap of Sector-wise FDI Inflows")
plt.show()

# Emerging Sectors: Identify sectors with consistent growth
emerging_sectors = data[data['Total'] > data['Total'].mean()]
print("Emerging Sectors with above-average FDI inflows:")
print(emerging_sectors[['Sector', 'Total']])

# Export cleaned data and summary
data.to_csv("Cleaned_FDI_Data.csv", index=False)
top_sectors.to_csv("Top_Sectors_by_FDI.csv")
yearly_totals.to_csv("Yearly_FDI_Totals.csv")


print("Analysis Complete. Visualizations generated and data exported.")
