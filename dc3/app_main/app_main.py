# program: dark castle v3.80
# name: Tom Snellgrove
# date: Jan 7, 2024
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
def app_main(user_input, start_of_game):

	# start-up case
	if start_of_game == True:
		end_of_game, user_output = start_me_up()
		return end_of_game, user_output

	# object list loaded from save_obj_pickle2
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)

	# Gamestate vatiable instantiated from un-pickled list
	gs = master_obj_lst[0]
	gs.io.reset_buff() # resets buffer


	### pre-interp word cases ('quit', 'again', 'wait') ###
	if user_input.lower() == 'quit' or user_input.lower() == 'q':
		gs.set_game_ending('quit')
		end(gs)
		return gs.get_end_of_game(), gs.io.get_buff()

	if user_input.lower() == 'restart':
		gs.io.buffer("Restarting...")
		return gs.get_end_of_game(), gs.io.get_buff()

	if user_input.lower() == 'again' or user_input.lower() == 'g':
		user_input = gs.io.last_input_str

	gs.io.last_input_str = user_input # sets 'again' last_turn input value for next_turn

	if user_input.lower() == 'wait' or user_input.lower() == 'z':
		gs.move_inc()
		gs.io.buffer("Waiting...")
		auto_action(gs)
		with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
			pickle.dump(master_obj_lst, f)
		return gs.get_end_of_game(), gs.io.get_buff()


	### all other word cases ###

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
	cmd_override = pre_action(gs, case, word_lst)
	if not cmd_override:
		cmd_execute(gs, case, word_lst)
	post_action(gs, case, word_lst)
	score(gs)
#	gs.score.get_score(gs)
	if gs.get_game_ending() != "tbd":
		end(gs)
	auto_action(gs)

	### dump updated objects to save_obj_pickle2 ###
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return gs.get_end_of_game(), gs.io.get_buff()
