import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load CSV safely
df = pd.read_csv("scraped_data.csv", encoding="latin-1")

print("FIRST 5 ROWS:")
print(df.head())

print("\nSUMMARY:")
print(df.describe(include='all'))

# Clean price column properly (works for any weird characters)
df['price_num'] = (
    df['price']
    .apply(lambda x: re.sub(r'[^0-9\.]', '', str(x)))   # remove all characters except numbers & .
    .astype(float)
)

# Plot
plt.hist(df['price_num'], bins=10)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()
