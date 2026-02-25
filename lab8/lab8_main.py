"""
Nazaneen Baguaei, 
Lab 8, API's
Feb 24, 2026 
"""
#--------------------------------------
#Example 1: datagrame using pandas
#--------------------------------------

import pandas as pd

# step 1, data collectoin dict_ as the static template of our API 
dict_ = {
    'a': [11, 21, 31],
    'b': [12, 22, 32]
}

# step 2, create a dataframe using pandas 
df = pd.DataFrame(dict_)

# head method of the datafram communicates with the API displaying the first few rows of the dataframe
print("\n Example 1: simple API")
print(df.head())

# step 3 working with the data 
# mean method calculates and returns the mean value of a df 
print(f"The mean value is = {df.mean()}")

#--------------------------------------
#Example 2: Get NBA team from static.py file 
#--------------------------------------
# step 1, data collection 
from static import get_teams

nba_teams = get_teams()

#testing
print(f"The first two teams: {nba_teams[:2]}")

# step 2, create dataframe 
df_teams = pd.DataFrame(nba_teams)
print("\nALL teams")
print(df_teams.head())

# step 3, working with the data in df_teams
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print('\nWarriors')
print(df_warriors)

#--------------------------------------
#Example 3: working with external API's
#--------------------------------------
# step 1, data collection 
# download the pickle file 
import requests 

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save the download file 
file_name = "Golden_state.pkl"

print(f"\nDownloading external file!...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else:
    print("download failed!")

# step 2, create dataframe
# b. load dataframe from a pickle file 
games = pd.read_pickle(file_name)
print(games.head())

# step 3, working with the data in the dataframe
# c. filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
print("\n GSW vs raptors")
print(warriors_vs_raptors)

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('vs')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

print("\n GSW home games")
print(gsw_home_vs_raptors)

# d. calculate the average of the home and away matches
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"GSW home average {home_avg_plus}")
print(f"GSW away average = {away_avg_plus}")

# e. visualization of data analysis
import matplotlib.pyplot as plt 

metrics = ["PLUS_MINUS", "PTS"]
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35 

plt.figure(figsize=(8, 5))

plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title("GSW vs Raptors")
plt.ylabel("Average value")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)

input("Press enter to close...")

#--------------------------------------
#Lab Exercise: working with external API's
#--------------------------------------
# step 1, data collection
# download the csv file
url = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.csv"

# save the download file
file_name = "epl_matches.csv"

print(f"\nDownloading external file!...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else:
    print("download failed!")

# step 2, create dataframe
# b. load dataframe from a csv file
epl_games = pd.read_csv(file_name)
print("\nEPL games data:")
print(epl_games.head())

# step 3, working with the data in the dataframe
# c. filter Man City vs Liverpool
epl_vs = epl_games[
    (epl_games['HomeTeam'].str.contains('Man City') | epl_games['AwayTeam'].str.contains('Man City')) &
    (epl_games['HomeTeam'].str.contains('Liverpool') | epl_games['AwayTeam'].str.contains('Liverpool'))
]
print("\n Man City vs Liverpool")
print(epl_vs)

epl_home = epl_vs[epl_vs['HomeTeam'].str.contains('Man City')]
epl_away = epl_vs[epl_vs['AwayTeam'].str.contains('Man City')]

print("\n Man City home games")
print(epl_home)

# d. calculate the average of the home and away matches
home_avg_goals = epl_home['FTHG'].mean()
away_avg_goals = epl_away['FTAG'].mean()
home_avg_total = (epl_home['FTHG'] + epl_home['FTAG']).mean()
away_avg_total = (epl_away['FTHG'] + epl_away['FTAG']).mean()

print(f"Man City home average goals = {home_avg_goals}")
print(f"Man City away average goals = {away_avg_goals}")

# e. visualization of data analysis
metrics = ["Goals Scored", "Total Goals"]
home_values = [home_avg_goals, home_avg_total]
away_values = [away_avg_goals, away_avg_total]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))

plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title("Man City vs Liverpool - Home vs Away")
plt.ylabel("Average value")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)

input("Press enter to close...")