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

### 📷 Screenshots

**Matches Insights**
  - <img width="1000" height="500" alt="man_of_the_match" src="https://github.com/user-attachments/assets/fbe87efa-0ca9-410d-b33a-c0226760c230" />
  - <img width="1000" height="500" alt="total_match_per_seasons" src="https://github.com/user-attachments/assets/aabdf03f-811a-4962-9b24-c7d1483698e7" />
  - <img width="1000" height="600" alt="total_wins_by_teams" src="https://github.com/user-attachments/assets/91512f3c-8e44-4a8a-b9d1-1b1319663526" />
  - <img width="600" height="400" alt="toss_vs_winner" src="https://github.com/user-attachments/assets/ff0a2301-91c9-4dae-9f61-215a4466c069" />
- <img width="600" height="400" alt="toss_decision_distribution" src="https://github.com/user-attachments/assets/bb234837-0160-406d-b9cf-60d6bc379c20" />


**Deliveries Insights**
- <img width="1000" height="600" alt="most_sixes_scores" src="https://github.com/user-attachments/assets/ea465e0a-167e-462c-8f9d-4005ae7e8dd3" />
- <img width="1000" height="500" alt="top_batsmen scores" src="https://github.com/user-attachments/assets/33511db9-a2a5-4196-bd4f-14f06b1b4773" />
- <img width="1000" height="600" alt="top_bowlers" src="https://github.com/user-attachments/assets/225d84f2-63a3-4093-be16-b6bb7f5f6d53" />
- <img width="1000" height="600" alt="top_economy_rate" src="https://github.com/user-attachments/assets/af3e449e-6c68-4313-9c20-5bd7b20e675c" />
- <img width="1000" height="500" alt="top_strike_rate" src="https://github.com/user-attachments/assets/0f600734-7ec5-410e-a0e6-65df4ec2f652" />

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


