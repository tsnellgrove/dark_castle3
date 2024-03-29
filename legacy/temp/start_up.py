# program: dark castle v3.78
# name: Tom Snellgrove
# date: Sept 25, 2023
# description: gets obj from default_pkl, welcome text, sets starting values



### import statements
import pickle
import random
from dc3.data.static_gbl import static_dict

### start_me_up - gets obj from default_pkl, welcome text, sets starting values
def start_me_up():

	### object list loaded from default_obj_pickle ###
	with open('default_obj_pickle', 'rb') as f:
		master_obj_lst = pickle.load(f)

	gs = master_obj_lst[0]

	### Assign Random Secret Code ###
	portcullis_code = random.randint(0, 7)
	port_code_txt = "'..ode is " + str(portcullis_code) + ". Don't tell anyo..'"
	gs.set_dyn_static_dict('messy_handwriting', port_code_txt)
	
	for obj in master_obj_lst[1:]:
		if obj.name == 'control_panel':
			obj.mach_state = portcullis_code

	### introductory text ###
	gs.io.buffer(static_dict["introduction"])
	gs.io.buffer("*** Entrance ***")
	gs.io.buffer(static_dict["entrance"])
	gs.io.buffer("There is a Front Gate to the north, a path to the south, a leap down to the moat to the east, and a leap down to the moat to the west.")

	### dump updated objects to save_obj_pickle ###
	with open('save_obj_pickle2', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	end_of_game = gs.get_end_of_game()
	out_buff = gs.get_buff()

	return end_of_game, out_buff
