# codealpha_tasks
📘 CodeAlpha Internship
🕸️ Task: Web Scraping + Exploratory Data Analysis (EDA)
📅 Domain: Data Analytics
🛠️ Tools Used: Python, Pandas, BeautifulSoup, Matplotlib, Seaborn
<br>
⭐ Project Overview

This project completes two tasks from the CodeAlpha Data Analytics Internship:

✔ Task 1 — Web Scraping

Extracted data from a sample website (Books listing) using Python libraries like Requests and BeautifulSoup.
The scraped data was saved into a CSV file for further analysis.

✔ Task 2 — Exploratory Data Analysis (EDA)

Performed data cleaning, conversion of text to numeric values, summary statistics, and created visualizations to understand patterns in the data.

📌 Project Structure
CodeAlpha_WebScraping_EDA/
│
├── scrape.py               # Web scraping script
├── eda.py                  # Data analysis script
├── scraped_data.csv        # Scraped dataset
├── README.md               # Project documentation
└── visuals/
      └── price_distribution.png   # EDA chart

🕸️ Web Scraping Details

Website used: Books to Scrape (or your chosen website)

Extracted fields:

Book Title

Price

Cleaned and stored data in scraped_data.csv.

📊 EDA Highlights

Performed the following:

✔ Data Cleaning

Removed unwanted characters (Â, Ã, £, etc.)

Converted prices into proper numeric format

Handled encoding issues using regex

✔ Data Insights

Calculated price distribution

Summary statistics (mean, median, count)

Visualized price distribution using histogram

📈 Visualization

A histogram showing the distribution of book prices was created using matplotlib.

Example:

Price Distribution Graph


(Place your actual screenshot in the visuals folder.)

🚀 How to Run This Project
Step 1: Install Required Libraries
pip install requests beautifulsoup4 pandas matplotlib seaborn

Step 2: Run Web Scraping
python scrape.py

Step 3: Run EDA
python eda.py

🙌 Acknowledgement

Thanks to CodeAlpha for the opportunity to learn and work on real-world data analytics tasks.

🔥 Complete!

This project satisfies the CodeAlpha requirements:
✔ Scraping code
✔ EDA code
✔ GitHub repo
✔ LinkedIn post
✔ Visuals included
