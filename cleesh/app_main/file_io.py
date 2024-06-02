# program: cleesh save_game routine
# author: Tom Snellgrove
# module description: saves and restores games


### import statements
import shutil


### main routine
def save_game(game_name):
    src = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/working/active_pkl"
    dst = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/saves/save_pkl"
    shutil.copyfile(src, dst)
    return

def restore_game(game_name):
    src = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/saves/save_pkl"
    dst = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/working/active_pkl"
    shutil.copyfile(src, dst)
    return