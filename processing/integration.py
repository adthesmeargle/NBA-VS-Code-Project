import pandas as pd

nba_stats_folder_name = "C:\Users\zephy\Coding Projects\NBA-VS-Code-Project\data\stats"

path_to_headshots = "C:\Users\zephy\Coding Projects\NBA-VS-Code-Project\data\headshots"

snap_shot_suffixes = ['stats_0125', 'stats_0225', 'stats_0325', 'stats_0425']

nba_stats_paths = [f"{nba_stats_folder_name}\{month}" for month in snap_shot_suffixes]

stat_types = ["advanced", "per_game", "standings", "totals"]   


def get_stats(nba_stats_paths=None, stat_types=None):
    """
    Get path for advanced stats and load data
    :param: type of sta we want to get e.g. [advanced, totals, per_game, standings] 
    """

    for path in nba_stats_paths:
        if "advanced" in stat_types:
            advanced_df = pd.read_csv(path + "\advanced.csv")
            _advanced_df = pd.concat([advanced_df, _advanced_df], ignore_index=True)
        if "per_game" in stat_types:
            per_game_df = pd.read_csv(path + "\per_game.csv")
            _per_game_df = pd.concat([per_game_df, _per_game_df], ignore_index=True)
        if "standings" in stat_types:
            standings_df = pd.read_csv(path + "\standings.csv")
            _standings_df = pd.concat([standings_df, _standings_df], ignore_index=True)
        if "totals" in stat_types:
            totals_df = pd.read_csv(path + "\totals.csv")
            _totals_df = pd.concat([totals_df, _totals_df], ignore_index=True)
    
    return _advanced_df, _per_game_df, _standings_df, _totals_df


advanced_df , per_game_df, standings_df, totals_df = get_stats(nba_stats_paths, stat_types)


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




def data_cleaning(list_of_dataframes):
   
   #takes dataframes and then creates some extra columns to separate stats
   # for example pts per game and total pts are different

 


   return something







  # Rename some columns: add `prefix` to certain column names
    cols_to_keep = ['Rk', 'Player', 'Season', 'Pos', 'Age', 'Tm', 'G', 'GS']

    # Rename other columns
    for col in per_game_df.columns:
        if col not in cols_to_keep:
            per_game_df = per_game_df.rename(columns={col: col + '_per_game'})

    for col in totals_df.columns:
        if col not in cols_to_keep:
            totals_df = totals_df.rename(columns={col: col + '_totals'})

    for col in advanced_df.columns:
       if col not in cols_to_keep:
          advanced_df = advanced_df.rename(columns={col: col + '_average'})



df = pd.merge(per_game_df, advanced_df, on=['Player', 'Season', 'Tm'], how='left')
df = pd.merge(df, totals_df, on=['Player', 'Season', 'Tm'], how='left')

grouped_df = df.groupby(['Player', 'Season', 'Tm']).size().reset_index(name='counts')
sorted_df = grouped_df.sort_values('counts', ascending=False)

nba_teams = pd.DataFrame.from_dict(team_abbreviations, orient='index').reset_index()
nba_teams = nba_teams.rename(columns={'index': 'Team', 0: 'Tm'})
standings_w_abbr = pd.merge(standings_df, nba_teams, on='Team', how='left')

wins = (standings_w_abbr['Record'].str.split('-',expand=True)[0]).astype(int)
games = (standings_w_abbr['Record'].str.split('-',expand=True)[0]).astype(int) + (standings_w_abbr['Record'].str.split('-',expand=True)[1]).astype(int)
win_pct = wins/games
standings_w_abbr['win_pct'] = win_pct

nba_stats_merged = df.merge(standings_w_abbr, on=['Tm', 'Season'], how='left')


def merge_all_the_data(list_of_data_frames):

    return merged_data

merged_df = merge_all_the_data([advanced_df, totals_df])