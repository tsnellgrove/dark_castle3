# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: gets obj from default_pkl, welcome text, sets starting values



### import statements
import pickle
import random

### start_me_up - gets obj from default_pkl, welcome text, sets starting values
def start_me_up():

	### object list loaded from default_obj_pickle ###
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/def_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	gs = master_obj_lst[0]

	### Assign Random Secret Code ###
	portcullis_code = random.randint(0, 7)
	port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
	gs.io.set_dyn_dict('messy_handwriting', port_code_txt)
	
	for obj in master_obj_lst[1:]:
		if obj.name == 'control_panel':
			obj.mach_state = portcullis_code

	### introductory text ###
	gs.io.buff_e('introduction')
	gs.io.buffer("*** Entrance ***")
	gs.io.buff_e('entrance')
	gs.io.buffer("There is a Front Gate to the north, a path to the south, a leap down to the moat to the east, and a leap down to the moat to the west.")

	### dump updated objects to save_obj_pickle ###
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

#	end_of_game = gs.get_end_of_game()
#	is_end_of_game = gs.end.is_end_of_game
#	out_buff = gs.io.get_buff()

#	return end_of_game, out_buff
#	return is_end_of_game, out_buff
	return gs.end.is_end_of_game, gs.io.get_buff()
