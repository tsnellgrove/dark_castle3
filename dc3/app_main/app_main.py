# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: app-side wrapper module that calls game functions


### import statements
import pickle
from dc3.app_main.start_up import start_me_up
from dc3.app_turn.interp import interpreter
from dc3.app_turn.validate import validate
from dc3.app_turn.pre_action import pre_action
from dc3.app_turn.cmd_exe import cmd_execute
from dc3.app_turn.post_action import post_action
from dc3.app_turn.score import score
from dc3.app_turn.ending import end
from dc3.app_turn.auto_action import auto_action

### loads game obj, calls other modules, and saves game obj ###
def app_main(user_input):

	# start-up case
	if user_input == "xyzzy42":
		end_of_game, user_output = start_me_up()
		return end_of_game, user_output

	# object list loaded from save_obj_pickle2
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	# Gamestate vatiable instantiated from un-pickled list
	active_gs = master_obj_lst[0]
	active_gs.reset_buff() # resets buffer

	# quit case
	if user_input == "quit" or user_input == "q":
		active_gs.set_game_ending('quit')
		end(active_gs)
		return active_gs.get_end_of_game(), active_gs.get_buff()

	# interpret and validate user_input
	case, word_lst = interpreter(user_input, master_obj_lst)
	input_valid = validate(active_gs, case, word_lst)

	# exit if user_input not valid
	if not input_valid:
		return active_gs.get_end_of_game(), active_gs.get_buff()

	# for valid user_input, increment move count and run pre_action, cmd_exe, post_action, and auto_action
	active_gs.move_inc()
	cmd_override = pre_action(active_gs, case, word_lst)
	if not cmd_override:
		cmd_execute(active_gs, case, word_lst)
	post_action(active_gs, case, word_lst)
	score(active_gs)
	if active_gs.get_game_ending() != "tbd":
		end(active_gs)
	auto_action(active_gs)

	### dump updated objects to save_obj_pickle2 ###
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return active_gs.get_end_of_game(), active_gs.get_buff()
