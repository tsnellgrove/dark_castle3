# program: cleesh save_game routine
# author: Tom Snellgrove
# module description: saves and restores games


### import statements
import shutil
from pathlib import Path


### main routine
def save_game(game_name):
    src = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/working/active_pkl"
    dst = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/saves/save_pkl"
    shutil.copyfile(src, dst)
    user_output = "Game saved."
    return user_output

def restore_game(game_name):
    src = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/saves/save_pkl"
    my_file = Path(src)
    if my_file.is_file():
        dst = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/working/active_pkl"
        shutil.copyfile(src, dst)
        user_output = "Game restored."
    else:
        user_output = "There is no saved game to restore."
    return user_output