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
	gs = master_obj_lst[0]
	gs.io.reset_buff() # resets buffer

	# quit case
	user_input_lc = user_input.lower()
	if user_input_lc == "quit" or user_input_lc == "q":
		gs.set_game_ending('quit')
		end(gs)
		return gs.get_end_of_game(), gs.io.get_buff()

	print(f"Last Turn input: {gs.io.last_input_str}")

	# again command
	if user_input_lc == 'again' or user_input_lc == 'g':
		user_input = gs.io.last_input_str

	gs.io.last_input_str = user_input # sets 'again' last_turn input value for next_turn

	# wait command
	if user_input_lc == 'wait' or user_input_lc == 'z':
		gs.move_inc()
		gs.io.buffer("Waiting...")
		auto_action(gs)
		with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
			pickle.dump(master_obj_lst, f)
		return gs.get_end_of_game(), gs.io.get_buff()

	# interpret and validate user_input	
	case, word_lst = interpreter(user_input, master_obj_lst)
	input_valid = validate(gs, case, word_lst)

	# exit if user_input not valid (need to save state due to 'again' command)
	if not input_valid:
		with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
			pickle.dump(master_obj_lst, f)
		return gs.get_end_of_game(), gs.io.get_buff()

	# for valid user_input, increment move count and run pre_action, cmd_exe, post_action, and auto_action
	gs.move_inc()
#	if word_lst[0] != 'wait' and word_lst[0] != 'z':
	cmd_override = pre_action(gs, case, word_lst)
	if not cmd_override:
		cmd_execute(gs, case, word_lst)
	post_action(gs, case, word_lst)
	score(gs)
	if gs.get_game_ending() != "tbd":
		end(gs)
#	else:
#		gs.io.buffer("Waiting...")
	auto_action(gs)

	### dump updated objects to save_obj_pickle2 ###
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.get_end_of_game(), gs.io.get_buff()
