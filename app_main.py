# program: dark castle v3.78
# name: Tom Snellgrove
# date: Sept 25, 2023
# description: app-side wrapper module that calls game functions


### import statements
import pickle
from start_up import start_me_up
from interp import interpreter
from validate import validate
from pre_action import pre_action
from cmd_exe import cmd_execute
from post_action import post_action
from score import score
from ending import end
from auto_action import auto_action


### loads game obj, calls other modules, and saves game obj ###
# def wrapper(user_input):
def app_main(user_input):

	# start-up case
	if user_input == "xyzzy42":
		end_of_game, out_buff = start_me_up()
		return end_of_game, out_buff

	# object list loaded from save_obj_pickle2
	with open('save_obj_pickle2', 'rb') as f:
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
	with open('save_obj_pickle2', 'wb') as f:
		pickle.dump(master_obj_lst, f)

	return active_gs.get_end_of_game(), active_gs.get_buff()
