# program: dark castle v3.82
# name: Tom Snellgrove
# date: Feb 28, 2024
# description: app-side wrapper module that calls game functions


### import statements
import pickle
from dc3.app_main.start_up import start_me_up
from dc3.app_turn.interp import interpreter
from dc3.app_turn.validate import validate
from dc3.app_turn.pre_action import pre_action
from dc3.app_turn.cmd_exe import cmd_execute
from dc3.app_turn.post_action import post_action
from dc3.app_turn.auto_action import auto_action

### loads game obj, calls other modules, and saves game obj ###
def app_main(user_input, is_start_of_game):

	# start-up case
	if is_start_of_game == True:
		user_output = start_me_up()
		return False, user_output

	# object list loaded from save_obj_pickle2
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	# Gamestate vatiable instantiated from un-pickled list
	gs = master_obj_lst[0]
	gs.io.reset_buff() # resets buffer


	### pre-interp word cases ('quit', 'again', 'wait') ###
	if user_input.lower() == 'quit' or user_input.lower() == 'q':
		gs.end.game_ending = 'quit.'
##		gs.end.is_end == True
		gs.end.disp_end(gs)
##		return gs.end.is_end, gs.io.get_buff()
		return True, gs.io.get_buff()

	if user_input.lower() == 'restart':
		gs.end.game_ending = 'restarted.'
		gs.end.disp_end(gs)
		gs.io.buffer("Restarting...")
##		return gs.end.is_end, gs.io.get_buff()
		return False, gs.io.get_buff()

	if user_input.lower() == 'again' or user_input.lower() == 'g':
		user_input = gs.io.last_input_str

	gs.io.last_input_str = user_input # sets 'again' last_turn input value for next_turn

	if user_input.lower() == 'wait' or user_input.lower() == 'z':
		gs.core.move_inc()
		gs.io.buffer("Waiting...")
		auto_action(gs)
		with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
			pickle.dump(master_obj_lst, f)
		return gs.end.is_end, gs.io.get_buff()

	### all other word cases ###

	# interpret and validate user_input	
	case, word_lst = interpreter(user_input, master_obj_lst)
	input_valid = validate(gs, case, word_lst)

	# exit if user_input not valid (need to save state due to 'again' command)
	if not input_valid:
		with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
			pickle.dump(master_obj_lst, f)
		return gs.end.is_end, gs.io.get_buff()

	# for valid user_input, increment move count and run pre_action, cmd_exe, post_action, and auto_action
	gs.core.move_inc()
	cmd_override = pre_action(gs, case, word_lst)
	if not cmd_override:
		cmd_execute(gs, case, word_lst)
	post_action(gs, case, word_lst)
	if gs.end.is_end:
		gs.end.disp_end(gs)
	if not gs.end.is_end:
		auto_action(gs)

	### dump updated objects to save_obj_pickle2 ###
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.end.is_end, gs.io.get_buff()
