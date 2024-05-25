# program: cup_of_tea
# author: Tom Snellgrove
# module description: gets obj from game_pkl, buffers starting text, sets starting values, creates active_pkl

### import statements
import pickle
# import random


def start_me_up():
	# object list loaded from def_pkl
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/cup_of_tea/game_file/game_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	gs = master_obj_lst[0]

	# assign str_to_obj_dict
	for obj in master_obj_lst:
		gs.core.set_str_to_obj_dict(obj.name, obj)

	# assign game session values

	# buffer introductory text
	gs.io.buff_e('introduction')

	# buffer <start_rm>.examine()
	for obj in master_obj_lst[1:]:
		if obj.name == 'pub':
			obj.examine(gs)

	# dump updated objects to sav_pkl
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/cup_of_tea/working/active_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.io.get_buff()
