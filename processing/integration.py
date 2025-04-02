# import pandas as pd

data_root_path = ""
nba_stats_folder_name = ""
path_to_headshots = ""

season_snap_shot_months = ['01', '02', '03']

nba_stats_paths = [f"{nba_stats_folder_name}_{month}" for month in season_snap_shot_months]

def get_advanced_stats_path(nba_stats_paths=None):
    """
    Get path for advanced stats 
    """
    for path in nba_stats_paths:
        return path + "_advanced.csv"

def get_total_stats_path(nba_stats_paths=None):
    """
    Get path for advanced stats 
    """
    for path in nba_stats_paths:
        return path + "_advanced.csv"     

def get_stats_path_csv(nba_stats_paths=None, stat_types=None):
    """
    Get path for advanced stats
    :param: type of sta we want to get e.g. [advanced, totals, per_game, standings] 
    """
    if "advanced" in stat_types:
        for path in nba_stats_paths:
            return path + "_advanced.csv"
    if "advanced" in stat_types:
        for path in nba_stats_paths:
            return path + "_advanced.csv"

def load_all_the_data(list_of_stat_paths):
    """
    """
    return all_the_advanced_data, all_the_totals_data


list_of_stat_paths = get_stats_path_csv(nba_stats_paths, ["advanced", "totals"])
advanced_df, totals_df = load_all_the_data(list_of_stat_paths)

def merge_all_the_data(advanced_df, totals_df):
    return merged_data

merged_df = merge_all_the_data(advanced_df, totals_df)