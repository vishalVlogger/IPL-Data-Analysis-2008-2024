# 📋 IPL EDA Insights Summary 2008-2024
  - This project performs a comprehensive Exploratory Data Analysis (EDA) on an IPL (Indian Premier League) match dataset using Pandas, Matplotlib, and Seaborn.

## 🏆 Match-Level Insights

### ✅ What's Performing Well

- **CSK** and **MI** are among the top winners.
- **The seasons from 2018 to 2020** had high match volumes.
- **Toss decision:** Teams preferred to **field first**.
- In \~**50% of matches**, toss winners also won the game.
- Players like **Kohli**, **Rohit**, and **Russell** frequently received **Player of the Match** awards.

### ⚠️ What Needs Attention

- Some seasons (like 2021, 2023) saw fewer matches in dummy data.
- Some venues are **underrepresented**, which may distort the venue analysis.

---

## 🧠 Deliveries-Level Insights

### ✅ What's Performing Well

- **Kohli** and **Buttler** scored the most runs.
- **Russell** is the top six-hitter.
- **Shami** and **Chahal** are top wicket-takers.
- **Dhoni** and **Buttler** show strong **strike rates**.
- **Boult** and **Narine** have **great economy rates**.

### ⚠️ What Needs Attention

- Some players had a low ball count but maintained a high economy and strike rate. Be sure to check for minimum filters.
- Ball count imbalance may affect the accuracy of bowling stats.

---

## 📈 Trends or Surprises

- **Fielding first** (after toss) seems more common — may indicate chasing preference.
- Many matches are **evenly split** between the toss-winner and the final-winner.
- A strike rate of >180 is common among top batters, reflecting **T20 aggression**.
- Bowlers with economy <6.5 are still possible despite the T20 format — shows impact.

---

## 🛠 Tools Used

- Python 3.x
- Pandas
- Seaborn
- Matplotlib

## 📂 Output Files

- 📄 `matches.csv`
- 📄 `deliveries.csv`
- 📜 Python scripts: `IPL_Matches_EDA.py`, `IPL_Deliveries_EDA.py`
- 📊 Charts: saved as PNG files for insights

## ✍️ Author

**Vishal Patil**\
Salesforce Developer | Aspiring Data Analyst


