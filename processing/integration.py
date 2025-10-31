import os
import pickle
import pandas as pd
import math
import numpy as np

def is_nan_string(string):
    try:
        float_value = float(string)
        return math.isnan(float_value)
    except ValueError:
        return False

nba_stats_folder_name = "../data/stats"

path_to_headshots = "../data/headshots"

snap_shot_suffixes = ['stats_0125', 'stats_0225', 'stats_0325', 'stats_0425']

nba_stats_paths = [f"{nba_stats_folder_name}/{month}" for month in snap_shot_suffixes]


stat_types = ["advanced", "per_game", "standings", "totals"]   


def get_stats(nba_stats_path=None, stat_types=None):
    """
    Get path for advanced stats and load data
    :param: type of stat we want to get e.g. [advanced, totals, per_game, standings] 
    """
    season = '2024-25'
    if "advanced" in stat_types:
        advanced_df = pd.read_csv(os.path.join(os.path.dirname(__file__), nba_stats_path + "/advanced.csv"))
        advanced_df['Season'] = season
        # _advanced_df = pd.concat([advanced_df, _advanced_df], ignore_index=True)
    if "per_game" in stat_types:
        per_game_df = pd.read_csv(os.path.join(os.path.dirname(__file__), nba_stats_path + "/per_game.csv"))
        per_game_df['Season'] = season
        # _per_game_df = pd.concat([per_game_df, _per_game_df], ignore_index=True)
    if "standings" in stat_types:
        standings_df = pd.read_csv(os.path.join(os.path.dirname(__file__), nba_stats_path + "/standings.csv"))
        standings_df['Season'] = season
        # _standings_df = pd.concat([standings_df, _standings_df], ignore_index=True)
    if "totals" in stat_types:
        totals_df = pd.read_csv(os.path.join(os.path.dirname(__file__),nba_stats_path + "/totals.csv"))
        totals_df['Season'] = season
        # _totals_df = pd.concat([totals_df, _totals_df], ignore_index=True)
    
    return advanced_df, per_game_df, standings_df, totals_df




### CHOOSE THE MONTH HERE!!!!
advanced_df , per_game_df, standings_df, totals_df = get_stats(nba_stats_paths[3], stat_types)

#Team Abbreviations are necessary for connecting players to their teams
team_abbreviations = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BRK",
    "Charlotte Hornets": "CHO",
    "Charlotte Bobcats": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New Orleans Hornets": "NOH",
    "New Jersey Nets": "NJN",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHO",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Seattle SuperSonics": "SEA",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS"
}




def data_cleaning(per_game_df, totals_df, advanced_df):
   
   #takes dataframes and then creates some extra columns to separate stats
   # for example pts per game and total pts are different

  # Rename some columns: add `prefix` to certain column names
    cols_to_keep = ['Rk', 'Rank', 'Team', 'Player', 'Season', 'Pos', 'Age', 'Tm', 'G', 'GS']

    # Rename other columns
    for col in per_game_df.columns:
        if col not in cols_to_keep:
            per_game_df = per_game_df.rename(columns={col: col + '_per_game'})

    for col in totals_df.columns:
        if col not in cols_to_keep:
            totals_df = totals_df.rename(columns={col: col + '_totals'})

    for col in advanced_df.columns:
       if col not in cols_to_keep:
          advanced_df = advanced_df.rename(columns={col: col + '_advanced'}) 
    
    return advanced_df, per_game_df, totals_df 



advanced_df, per_game_df, totals_df = data_cleaning(per_game_df, totals_df, advanced_df)


def standings_cleanup(standings_df):
    #for getting the row count
    count = 0

    for x in standings_df['Rank']:
        if is_nan_string(x) == 0:
            standings_df.loc[count, 'Rank'] = x
        else:
            standings_df.loc[count, 'Rank'] = standings_df.loc[count, 'Team']
        count += 1

    # removing columns that aren't needed
    standings_df = standings_df.drop(columns=['Team', 'GB', 'PS/G', 'PA/G', 'SRS'])

    # Removing the last few characters from the Team Name like (12)
    standings_df['Rank'] = standings_df['Rank'].str[:-4]

    # renaming the Rank column and creating a Record Column as well as a season column
    standings_df = standings_df.rename(columns={'Rank': 'Team'})

    standings_df['Record'] = standings_df['W'].astype(str) + '-' + standings_df['L'].astype(str)

    standings_df['Season'] = '2024-25'

    #Arranging the teams by order of win percentage to get a 'seed'
    standings_df = standings_df.sort_values(by=['W/L%'], ascending=False)

    # Assign seeds based on each team's winning percentages in a dataframe
    standings_df = standings_df.sort_values(by=['W/L%'], ascending=False)
    standings_df['Seed'] = range(1, len(standings_df) + 1)

    # removing columns that aren't needed
    standings_df = standings_df.drop(columns=['W', 'L', 'W/L%'])

    standings_df_team = standings_df[['Team']]

    correct_teams_lst = []
    for index, row in standings_df_team.iterrows():
        team = row['Team']
        if team not in team_abbreviations.keys():
        ### Remove one letter from the end of string to eliminate the space
            team = team[:-1] # Change this code with string strip approach later
        correct_teams_lst.append(team)

    standings_df['Team'] = correct_teams_lst

    nba_teams = pd.DataFrame.from_dict(team_abbreviations, orient='index').reset_index()
    nba_teams = nba_teams.rename(columns={'index': 'Tm', 0: 'Team'})
    _standings_df = standings_df.rename(columns={'Team': 'Tm'})
    standings_w_abbr = pd.merge(_standings_df, nba_teams, on='Tm', how='left')

    wins = (standings_w_abbr['Record'].str.split('-',expand=True)[0]).astype(int)
    games = (standings_w_abbr['Record'].str.split('-',expand=True)[0]).astype(int) + (standings_w_abbr['Record'].str.split('-',expand=True)[1]).astype(int)
    win_pct = wins/games
    standings_w_abbr['win_pct'] = win_pct
    standings_df = standings_w_abbr
    return standings_w_abbr

standings_df = standings_cleanup(standings_df)

def merge_stats(advanced_df , per_game_df, standings_df, totals_df):
    """
    Merge stats
    """
    stats_df = pd.merge(per_game_df, advanced_df, on=['Player', 'Season', 'Team'], how='left')
    stats_df = pd.merge(stats_df, totals_df, on=['Player', 'Season', 'Team'], how='left')
    stats_df = pd.merge(stats_df, standings_df, on=['Team', 'Season'], how='left')

    return stats_df

stats_df = merge_stats(advanced_df , per_game_df, standings_df, totals_df)
# ==========END OF INTEGRATION=====


# =========START OF FEATURE ENG=====


#25 Games for jan
#30 for feb
#40 for march
#50 for april


def mvp_selection_criteria(stats_df):
    features_df = stats_df[
    (
        (stats_df['G'] > 50) &
        (stats_df['MP_per_game'] > 30) &
        (stats_df['PTS_per_game'] > 15) &
        (stats_df['TRB_per_game'] > 1) &
        (stats_df['AST_per_game'] > 2) &
        (stats_df['Team'] != '2TM')
    )
    ]
    return features_df

_features_df = mvp_selection_criteria(stats_df)


### This below line will capture the data frame after filtering out players who don't meet potential mvp criteria
#_features_df.to_csv('apr_mvp_candidates.csv', index=False)



def feature_selection(features_df):
    features_df = features_df.drop(['Player', 'Season', 'Pos', 'Tm', 'Team', 'Record',
                          'Age', 'Seed', 'FGA_per_game', 'G', 'G_x', 'G_y', 'FG_per_game', '3PA_per_game', '3P%_per_game', '2PA_per_game', '2P%_per_game', 'eFG%_per_game', 'FTA_per_game', 'FTA_totals',
                          'FT%_per_game', 'DRB_per_game', 'ORB_per_game', 'ORB%_advanced','DRB%_advanced', 'TRB%_advanced', 'AST%_advanced', 'STL%_advanced', 'BLK%_advanced', 'OWS_advanced',
                          'DWS_advanced', 'WS_advanced', 'WS/48_advanced', 'OBPM_advanced', 'DBPM_advanced', 'BPM_advanced', 'VORP_advanced', '3PAr_advanced', 'FTr_advanced', 'USG%_advanced',
                          'FGA_totals', '3PA_totals', '2PA_totals', 'DRB_totals', 'ORB_totals', 'Awards_advanced', 'Awards_per_game', 'Awards_totals', 'GS', 'Trp-Dbl_totals',
                          
                          'Age_x', 'Age_y', 'GS_x', 'GS_y', 'Pos_x', 'Pos_y', 'Rank', 'Rank_x', 'Rank_y' 
                          ], axis = 1
                        )
    return features_df

features_df = feature_selection(_features_df)
### Display features_df
# print(features_df .columns)


# ======Load model and make predictions====
model_path = os.path.join(os.path.dirname(__file__), '../models/rf_model.pkl')

with open(model_path, 'rb') as file:
    model = pickle.load(file)

### ChatGPT Solution to pkl file average vs advanced problem
# If feature names are stored in feature_names_in_
if hasattr(model, 'feature_names_in_'):
    old_names = model.feature_names_in_
    new_names = np.array([name.replace('_average', '_advanced') for name in old_names])
    model.feature_names_in_ = new_names

### ChatGPT Save New Model
# with open('updated_model.pkl', 'wb') as file:
#     pickle.dump(model, file)

mvp_predictions = model.predict(features_df)
pred = _features_df[['Player', 'Team', 'Season']].copy()
pred['Predicted MVP Votes Share'] = pd.Series(mvp_predictions).values

pred = pred.sort_values(by=['Season', 'Predicted MVP Votes Share'], ascending=[True, False])

# Load player ids
player_id_df = pd.read_csv(os.path.join(os.path.dirname(__file__),path_to_headshots + "/player_id_name.csv"))
print(player_id_df)
pred_final =  pd.merge(player_id_df, pred, left_on='player_name', right_on='Player', how='right')
pred_final = pred_final.drop(columns=['player_name'])
pred_final['headshot_path'] = path_to_headshots + "/headshot/" + pred_final['player_id'] + ".jpg"


def round_list(data, decimal_places=3):
    return [round(value, decimal_places) for value in data]


pred_final['Predicted MVP Votes Share'] = round_list(pred_final['Predicted MVP Votes Share'])
print(pred_final.head(10))

#pred_final.head(5).to_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0125.csv'), index=False)