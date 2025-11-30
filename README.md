# codealpha_tasks
📘 CodeAlpha Data Analytics Internship
✅ Tasks Completed: Web Scraping + EDA + Data Visualizations
🗂️ Domain: Data Analytics
🛠️ Tools: Python, Pandas, BeautifulSoup, Requests, Matplotlib, Seaborn
🌟 Project Overview

This repository contains the implementation of three tasks from the CodeAlpha Data Analytics Internship program:

1️⃣ Task 1 – Web Scraping
2️⃣ Task 2 – Exploratory Data Analysis (EDA)
3️⃣ Task 3 – Data Visualization

The project involves scraping data from a sample website, cleaning and analyzing the data, and creating visualizations to extract insights.

📁 Project Structure
CodeAlpha_DataAnalytics_Project/
│
├── scrape.py                     # Task 1: Web Scraping
├── eda.py                        # Task 2: Exploratory Data Analysis
├── data_visualization.py         # Task 3: Visualizations
│
├── scraped_data.csv              # Dataset generated from scraping
│
├── visuals/                      # All graphs from Task 3
│     ├── price_distribution.png
│     ├── top10_books.png
│     └── price_boxplot.png
│
└── README.md                     # Project Documentation

🕸️ Task 1 — Web Scraping
✔️ What was done?

Used Requests and BeautifulSoup to scrape data from a sample book website.

Extracted:

Book Title

Book Price

Cleaned the data and stored it in a CSV file:
scraped_data.csv

✔️ Purpose of this task:

To gather real-world data automatically for analysis.

📊 Task 2 — Exploratory Data Analysis (EDA)
✔️ Key Steps:

Loaded the scraped dataset using Pandas

Cleaned price column using regex to fix:

Â

Ã

£

Other encoding issues

Converted price to numeric format

Performed:

Summary statistics

Data structure check

Missing value handling

✔️ Insights observed:

Spread of price values

Average price

Most common price range

Outlier detection

📈 Task 3 — Data Visualization

Three important visualizations were created:

1️⃣ Price Distribution (Histogram)

Shows how book prices are spread across the dataset.

📌 File: visuals/price_distribution.png

2️⃣ Top 10 Most Expensive Books (Bar Chart)

Displays the highest-priced books.

📌 File: visuals/top10_books.png

3️⃣ Price Spread (Box Plot)

Identifies:

Outliers

Price variation

Median and quartiles

📌 File: visuals/price_boxplot.png

🚀 How to Run the Complete Project
🔧 Install Dependencies:
pip install requests beautifulsoup4 pandas matplotlib seaborn

▶️ Run Task 1 (Scraping)
python scrape.py

▶️ Run Task 2 (EDA)
python eda.py

▶️ Run Task 3 (Visualizations)
python data_visualization.py


All charts will be saved inside the visuals/ folder.


🙏 Acknowledgment

Special thanks to CodeAlpha for providing a practical and hands-on learning opportunity in Data Analytics.

🎉 Final Status: All Tasks Completed Successfully

✔ Web Scraping
✔ Data Cleaning
✔ EDA
✔ Visualization
✔ GitHub Upload
✔ LinkedIn Post
