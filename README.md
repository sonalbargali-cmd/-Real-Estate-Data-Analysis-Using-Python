-Real-Estate-Data-Analysis-Using-Python
Exploratory data analysis of real estate properties using Python, Pandas, Matplotlib, and Seaborn, focusing on pricing trends, property characteristics, and market insights.
 🏠 Real Estate Data Analysis Using Python

📌 Project Overview

This project performs exploratory data analysis on a real estate dataset using Python.

The main goal of this project is to clean and analyze property data and identify patterns related to property prices, localities, BHK configurations, property types, RERA approval, property status, area, and price per square foot.

 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

🧹 Data Cleaning

The dataset was cleaned and prepared for analysis by:

- Removing duplicate records
- Cleaning column names
- Converting price, area, and rate-per-square-foot columns into numeric values
- Cleaning categorical values
- Converting RERA approval information into Boolean values

 📊 Analysis Performed

The project answers the following questions:

1. Which is the costliest flat in the dataset?
2. Which locality has the highest average property price?
3. Which locality has the highest average rate per square foot?
4. Do ready-to-move properties cost more than under-construction properties?
5. Do RERA-approved properties command a price premium?
6. How does area impact property price?
7. Which BHK configuration is the most expensive?
8. Which property type has the highest rate per square foot?
9. Which builders/companies have the highest average rate per square foot?
10. Are larger homes more expensive per square foot?

 📈 Visualizations

The project includes visualizations to understand relationships between:

- Area vs Price
- Area vs Rate per Square Foot

Seaborn and Matplotlib are used to create the visualizations.

 📂 Project Structure

```text
Real-Estate-Data-Analysis/
│
├── data/
│   └── data.csv
│
├── analysis.py
│
├── README.md
│
└── requirements.txt
