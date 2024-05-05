# program: Cleesh
# author: Tom Snellgrove
# module description: present a menu of games to the user


### base import
from prettytable import PrettyTable
from importlib import import_module
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
        game_static_gbl = import_module(import_str)
        row_lst = [index, game_static_gbl.game_static_dict['game_full_name'], game_static_gbl.game_static_dict['game_descript']]
        menu.add_row(row_lst)
    print()
    print(menu)
    print()
    return index
