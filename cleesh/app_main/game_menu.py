# program: Cleesh
# author: Tom Snellgrove
# module description: present a menu of games to the user


### base import
from prettytable import PrettyTable
from cleesh.data.static_gbl import engine_static_dict


### main routine
def print_game_menu():
    menu = PrettyTable()
    menu.field_names = ["#", "Game", "Description"]
    game_lst = engine_static_dict['game_lst']
    index = 0
    for game in game_lst:
        index += 1
        import_str = f"cleesh.games.{game}.game_file.game_static_gbl"
        from import_str import game_static_dict
        row_lst = [index, game_static_dict['game_full_name'], game_static_dict['game_descript']]
        menu.ad_row(row_lst)
    print(menu)

# from cleesh.games.dark_castle.game_file.game_static_gbl import game_static_dict