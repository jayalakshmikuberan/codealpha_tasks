import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

books = []

for item in soup.select(".product_pod"):
    title = item.h3.a["title"]
    price = item.select_one(".price_color").text

    books.append({"title": title, "price": price})

df = pd.DataFrame(books)
df.to_csv("scraped_data.csv", index=False)

print("Data saved to scraped_data.csv")
