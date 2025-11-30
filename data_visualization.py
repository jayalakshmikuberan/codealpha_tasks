import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load data
df = pd.read_csv("scraped_data.csv", encoding="latin-1")

# Clean price column to remove symbols
df['price_num'] = (
    df['price']
    .apply(lambda x: re.sub(r'[^0-9\.]', '', str(x)))
    .astype(float)
)

# ============================
# 1. PRICE DISTRIBUTION (HISTOGRAM)
# ============================
plt.figure(figsize=(10,5))
plt.hist(df['price_num'], bins=10)
plt.title("Price Distribution of Books")
plt.xlabel("Price")
plt.ylabel("Count")
plt.savefig("visuals/price_distribution.png")
plt.close()

# ============================
# 2. TOP 10 MOST EXPENSIVE BOOKS (BAR CHART)
# ============================
top10 = df.sort_values(by='price_num', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='price_num', y='title', data=top10)
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price")
plt.ylabel("Book Title")
plt.savefig("visuals/top10_books.png")
plt.close()

# ============================
# 3. PRICE SPREAD (BOX PLOT)
# ============================
plt.figure(figsize=(6,7))
sns.boxplot(y=df['price_num'])
plt.title("Price Spread & Outliers")
plt.ylabel("Price")
plt.savefig("visuals/price_boxplot.png")
plt.close()

print("All charts created and saved in the 'visuals' folder!")
