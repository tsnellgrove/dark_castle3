# program: dark castle
# author: Tom Snellgrove
# module description: gets obj from def_pkl, buffers starting text, sets starting values, creates sav_pkl

### import statements
import pickle
import random


def start_me_up():
	# object list loaded from def_pkl ###
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/dark_castle/game_file/game_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	gs = master_obj_lst[0]

	# Determine Random Secret Code ###
	portcullis_code = random.randint(0, 7)
	port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
	gs.io.set_dyn_dict('messy_handwriting', port_code_txt)
	
	# introductory text ###
	gs.io.buff_e('introduction')

	# set control_panel.mach_state and buffer entrance.examine()
	for obj in master_obj_lst[1:]:
		if obj.name == 'control_panel':
			obj.mach_state = portcullis_code
		if obj.name == 'entrance':
			obj.examine(gs)

	# dump updated objects to sav_pkl ###
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/dark_castle/working/active_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.io.get_buff()
