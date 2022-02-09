# program: dark castle v3.59
# name: Tom Snellgrove
# date: Feb 9, 2022
# description: app-side wrapper module that calls game functions


### import statements
import pickle
from start_up import start_me_up
from interp import interpreter
from pre_action import pre_action
from cmd_exe import cmd_execute
from post_action import post_action
from  score import score
from ending import end


### wrapper code - loads game obj, calls other modules, and saves game obj
def wrapper(user_input):
		if user_input == "xyzzy42":
				end_of_game, out_buff = start_me_up()
		else:

				# object list loaded from save_obj_pickle2
				with open('save_obj_pickle2', 'rb') as f:
						master_obj_lst = pickle.load(f)

				# Gamestate vatiable instantiated from un-pickled list
				active_gs = master_obj_lst[0]

				active_gs.move_inc()
				active_gs.reset_buff() # resets buffer

				case, word_lst = interpreter(user_input, master_obj_lst)
				cmd_override = pre_action(active_gs, case, word_lst)
				if not cmd_override:
						cmd_execute(active_gs, case, word_lst)
				post_action(active_gs, case, word_lst)
				score(active_gs)
				if active_gs.get_game_ending() != "tbd":
						end(active_gs)

				### dump updated objects to save_obj_pickle2 ###
				with open('save_obj_pickle2', 'wb') as f:
						pickle.dump(master_obj_lst, f)

				end_of_game = active_gs.get_end_of_game()
				out_buff = active_gs.get_buff()

		return end_of_game, out_buff
