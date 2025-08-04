import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("deliveries.csv")
new_df = df.drop(columns=["extras_type", "player_dismissed", "dismissal_kind", "fielder"])
print(new_df.info())

# ----------------------
# Analysis & Insights
# ----------------------

# Top Batsman Runs
top_batsman_runs = new_df.groupby("batter")["batsman_runs"].size().sort_values(ascending=False).head(10)

# Top Bowlers by Wickets
top_bowlers_by_wickets = new_df.groupby("bowler")["is_wicket"].size().sort_values(ascending=False).head(10)

# Most Sixes Hit by Players
most_sixes_by_player = new_df[new_df["batsman_runs"] == 6]["batter"].value_counts().head(10)

# Strike Rate of Top 10 Batsmen
df_st = new_df.groupby("batter").agg({"batsman_runs": "sum", "ball": "count"})
df_st["strike_rate"] = (df_st["batsman_runs"] / df_st["ball"]) * 100
strike_rate = df_st[df_st["batsman_runs"] > 200]["strike_rate"].sort_values(ascending=False).head(10)
print(strike_rate)

# Economy rate of bowlers
df_er = new_df.groupby("bowler").agg({"batsman_runs": "sum", "ball": "count"})
df_er = df_er[df_er["ball"] > 100]
df_er["Economy_Rate"] = df_er["batsman_runs"] / (df_er["ball"] / 6)
economy_rate = df_er.sort_values(by="Economy_Rate")["Economy_Rate"].head(10)

# ----------------------
# Visualizations
# ----------------------

sns.set_theme(style="whitegrid")

# Top Batsman Runs
plt.figure(figsize=(10,5))
plt.bar(top_batsman_runs.index, top_batsman_runs.values, color="skyblue")
plt.title("Top Batsman Runs Scores")
plt.xlabel("Batsmen")
plt.ylabel("Scores")
plt.tight_layout()
plt.savefig("top_batsmen.scores.png")
plt.show()

# Top Bowlers by Wickets
plt.figure(figsize=(10,6))
plt.barh(top_bowlers_by_wickets.index, top_bowlers_by_wickets.values, color="green")
plt.title("Top Bowlers by Wickets")
plt.xlabel("Bowlers")
plt.ylabel("Wickets")
plt.tight_layout()
plt.savefig("top_bowlers.png")
plt.show()

# Most Sixes Hit by Players
plt.figure(figsize=(10,6))
plt.bar(most_sixes_by_player.index, most_sixes_by_player.values, color="crimson")
plt.title("Most Sixes Hit by Players")
plt.xlabel("Players")
plt.ylabel("Sixes")
plt.tight_layout()
plt.savefig("most_sixes_scores.png")
plt.show()

# Strike Rate of Top 10 Batsmen
plt.figure(figsize=(10,5))
plt.plot(strike_rate.index, strike_rate.values, linestyle="--", linewidth=0.7, marker="o", label="Strike Rate")
plt.title("Strike Rate of Top 10 Batsmen")
plt.xlabel("Batsmen")
plt.ylabel("Strike Rate")
plt.tight_layout()
plt.savefig("top_strike_rate.png")
plt.show()

# Economy rate of bowlers
plt.figure(figsize=(10,6))
plt.bar(economy_rate.index, economy_rate.values, color="purple")
plt.title("Top Economical Bowlers (Min 100 Balls)")
plt.xlabel("Bowlers")
plt.ylabel("Economy Rate")
plt.tight_layout()
plt.savefig("top_economy_rate.png")
plt.show()
