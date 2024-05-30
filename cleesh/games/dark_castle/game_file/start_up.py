# program: dark castle
# author: Tom Snellgrove
# module description: gets obj from def_pkl, buffers starting text, sets starting values, creates sav_pkl

### import statements
import pickle
import random

def game_session_vars(self, gs):
	# assign game session values
	portcullis_code = random.randint(0, 7)
	port_code_txt = f"'..ode is {str(portcullis_code)}. Don't tell anyo..'"
	gs.io.set_dyn_dict('messy_handwriting', port_code_txt)
	gs.core.get_str_to_obj_dict('control_panel').mach_state = portcullis_code
	return

def start_me_up():
	# object list loaded from def_pkl
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/dark_castle/game_file/game_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	gs = master_obj_lst[0]

	# assign str_to_obj_dict
	for obj in master_obj_lst:
		gs.core.set_str_to_obj_dict(obj.name, obj)

	# assign game session values
	portcullis_code = random.randint(0, 7)
	port_code_txt = f"'..ode is {str(portcullis_code)}. Don't tell anyo..'"
	gs.io.set_dyn_dict('messy_handwriting', port_code_txt)
	gs.core.get_str_to_obj_dict('control_panel').mach_state = portcullis_code

	# buffer introductory text
	gs.io.buff_e('introduction')

	# buffer <start_rm>.examine()
	gs.core.get_str_to_obj_dict('entrance').examine(gs)

	# dump updated objects to sav_pkl
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/dark_castle/working/active_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.io.get_buff()
