# program: cleesh start_up routine
# author: Tom Snellgrove
# module description: gets obj from game_pkl, buffers starting text, sets starting values, creates active_pkl

### import statements
import pickle
from importlib import import_module


### main routine
def start_me_up(game_name):
	# object list loaded from game_pkl
	root_path_str = '/Users/thomassnellgrove/Documents/Python/dark_castle3'
	pkl_str = f"{root_path_str}/cleesh/games/{game_name}/game_file/game_pkl"
#	pkl_str = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/game_file/game_pkl"
	with open(pkl_str, 'rb') as f:
		master_obj_lst = pickle.load(f)
	gs = master_obj_lst[0]

	# assign str_to_obj_dict
	for obj in master_obj_lst:
		gs.core.set_str_to_obj_dict(obj.name, obj)

	# assign game session values
	if gs.core.has_session_vars:
		import_str = f"cleesh.games.{game_name}.game_file.game_start_up"
		import_module(import_str).game_session_vars(gs)

	# buffer introductory text and starting room description
	gs.io.buff_e('introduction')
	gs.core.get_str_to_obj_dict(gs.map.hero_rm.name).examine(gs)

	# dump updated objects to active_pkl
#	pkl_str = f"/Users/tas/Documents/Python/dark_castle3/cleesh/games/{game_name}/working/active_pkl"
	pkl_str = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
	with open(pkl_str, 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.io.get_buff()
