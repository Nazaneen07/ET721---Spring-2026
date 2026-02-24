"""
Nazaneen Baguaei, 
Lab 8, API's
Feb 24, 2026 
"""
#--------------------------------------
#Example 1: datagrame using pandas
#--------------------------------------

import pandas as pd

# step 1, data collectoindict_ as the static template of our API 
dict_ = {
    'a': [11, 21, 31],
    'b': [12, 22, 32]
}

# step 2, create a dataframe using pandas 
df = pd.DataFrame(dict_)

# head method of the datafram communicates with the API displaying the first few rows of the dataframe
print("\n Example 1: simple API")
print(df.head())

# step 3 working witg the data 
# mean method calculates adn returns the mean value of a df 
print(f"The mean value is = {df.mean()}")

#--------------------------------------
#Example 2: Get NBA team from static.py file 
#--------------------------------------
# step 1, data collection 
from static import get_teams

nba_teams = get_teams()

#testing
print(f"The first two teams: {nba_teams[:2]}")

# step 2, creare dataframe 
df_teams = pd.DataFrame(nba_teams)
print("\nALL teams")
print(df_teams.head())

# step 3, working with the data in df_teams
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print('\nWarriors')
print(df_warriors)

#--------------------------------------
#Example 2: working with external API's
#--------------------------------------
# step 1, data collection 
# download tje pickle file 
import requests 

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save teh download file 
file_name = "Golden_state.pkl"

print(f"\nDownloading external file!...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else:
    print("download failed!")

#step 2, create dataframe
#b. load dataframe from a pickle file 
games = pd.read_pickle(file_name)
print(games.head())

# step 3, working with the data in the dataframe
# c. filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
#testing
print("\n GSW vs raptors")
print(warriors_vs_raptors)

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('vs')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

# testing
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

plt.figure(figsize=(8,5))

plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label = 'Home', color='skyblue')
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label = 'Away', color='orange')

plt.xticts(x, metrics)
plt.title("GSW vs Raptors")

plt.ylabel("Average value")
plt.legends()
plt.show(block=True)

input("Press enter to close...")