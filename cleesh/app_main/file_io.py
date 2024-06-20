# program: cleesh save_game routine
# author: Tom Snellgrove
# module description: saves and restores games


### import statements
import shutil
from pathlib import Path


### main routine
def save_game(game_name, root_path_str):
#    root_path_str = '/Users/thomassnellgrove/Documents/Python/dark_castle3'
    src = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
    dst = f"{root_path_str}/cleesh/games/{game_name}/saves/save_pkl"
    shutil.copyfile(src, dst)
    user_output = "\nGame saved.\n"
    return user_output

def restore_game(game_name, root_path_str):
#    root_path_str = '/Users/thomassnellgrove/Documents/Python/dark_castle3'
    src = f"{root_path_str}/cleesh/games/{game_name}/saves/save_pkl"
    my_file = Path(src)
    if my_file.is_file():
        dst = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
        shutil.copyfile(src, dst)
        user_output = "\nGame restored.\n"
    else:
        user_output = "\nThere is no saved game to restore.\n"
    return user_output