import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
df = pd.read_csv("matches.csv")
print(df.info())

# ----------------------
# Analysis & Insights
# ----------------------

# Top Winning Teams
top_win = df["winner"].value_counts()

# Matches Played Per Season
total_match = df["season"].value_counts().sort_index()

# Toss Decision Analysis
df["toss_decision"].value_counts()

# Most Played Venues
df["venue"].value_counts().head(10)

# Most Man of the Match Awards
man_of_match = df["player_of_match"].value_counts().head(10)

# Toss Winner vs Match Winner Correlation
toss_match_win_count = (df["toss_winner"] == df["winner"]).value_counts()

# Toss decision by city
toss_decision_by_city = df.groupby("toss_decision")["city"].value_counts()

# Team performance per venue
team_wins_by_venue = df.groupby(["winner", "venue"]).size().sort_values(ascending=False)

# Winner % per season
total_match_per_season = df.groupby("season").size()
team_win_per_season = df.groupby(["season", "winner"]).size().reset_index(name="wins")
team_win_per_season["total_matches"] = team_win_per_season["season"].map(total_match_per_season)
season_data = team_win_per_season["win_percentage"] = (team_win_per_season["wins"] / team_win_per_season["total_matches"]) * 100

# ----------------------
# Visualizations
# ----------------------

sns.set_theme(style="whitegrid")

# Total matches per season
plt.figure(figsize=(10,5), dpi=100)
plt.bar(total_match.index, total_match.values, color="skyblue")
plt.title("Matches Played Per Season")
plt.xlabel("Seasons")
plt.ylabel("Match Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_match_per_seasons.png")
# plt.show()

# Most successful teams
plt.figure(figsize=(10,6), dpi=100)
plt.barh(top_win.index, top_win.values, color="limegreen")
plt.title("Total Wins by Teams")
plt.xlabel("Win Count")
plt.ylabel("Teams")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("total_wins_by_teams.png")
# plt.show()

# Toss Decision Distribution
plt.figure(figsize=(6,4), dpi=100)
sns.countplot(x="toss_decision", data=df, palette="pastel", hue="toss_decision", legend=False)
plt.title("Toss Decision Distribution")
plt.xlabel("Decision")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("toss_decision_distribution.png")
# plt.show()

# Toss Winner vs Match Winner
plt.figure(figsize=(6,4), dpi=100)
plt.bar(toss_match_win_count.index,toss_match_win_count.values, color=["red", "green"])
plt.title("Toss Winner vs Match Winner")
plt.ylabel("Match Count")
plt.xticks([0,1], ["No", "Yes"], rotation=0)
plt.tight_layout()
plt.savefig("toss_vs_winner.png")
# plt.show()

# Most Player of the Match Awards
plt.figure(figsize=(10,6), dpi=100)
plt.bar(man_of_match.index, man_of_match.values, color="orange")
plt.title("Most Player of the Match Awards")
plt.xlabel("Players")
plt.ylabel("Awards Count")
plt.tight_layout()
plt.savefig("man_of_the_match.png")
plt.show()
