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
def app_main(user_input, is_start):

	# for new game - call start_me_up and return start_me_up() output
	if is_start == True:
		user_output = start_me_up()
		return False, False, user_output

	# initiate app_main() - load obj, declare gs, and reset buffer
	with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)
	gs = master_obj_lst[0]
	gs.io.reset_buff()

	# local var declarations 
	is_stateful = False
	is_interp_cmd = False
	is_interp_valid = False

	# non-interp command cases
	if user_input.lower() == 'quit' or user_input.lower() == 'q':
		gs.end.game_ending = 'quit.'
		gs.end.is_end = True
	elif user_input.lower() == 'restart':
		gs.end.game_ending = 'restarted.'
		is_start = True
	elif user_input.lower() == 'again' or user_input.lower() == 'g':
		is_interp_cmd = True
		user_input = gs.io.last_input_str
	elif user_input.lower() == 'wait' or user_input.lower() == 'z':
		is_stateful = True
		gs.io.buffer("Waiting...")
	else:
		is_interp_cmd = True

	# for interp commands, interp user_input and validate command
	if is_interp_cmd:
		case, word_lst = interpreter(user_input, master_obj_lst)
		is_interp_valid = validate(gs, case, word_lst)

	# if command is valid or is_stateful (captures 'wait' case), increment move
	if is_interp_valid or is_stateful:
		gs.core.move_inc()

	# for valid interp commands, process in-turn game response
	if is_interp_valid:
		is_stateful = True
		cmd_override = pre_action(gs, case, word_lst)
		if not cmd_override:
			cmd_execute(gs, case, word_lst)
		post_action(gs, case, word_lst)

	# post-turn output (nominally, the turn ends on post_act()); auto_action() essentially occurs at the *start* of the *next* turn)
	if gs.end.is_end or is_start: 
		gs.end.disp_end(gs)
	elif is_stateful: # need to avoid case where auto_act() runs after player dies from is_valid_interp command (in which case is_stateful = True)
		auto_action(gs)
	if is_start:
		gs.io.buffer("Restarting...") # should appear after the 'you have restarted' end text and before the 'welcome' text

	# close out turn - if stateful, save state and last inupt (for 'again' case) and then return
	if is_stateful and not gs.end.is_end: # no need to save state if player has won or died
		gs.io.last_input_str = user_input
		with open('/Users/tas/Documents/Python/dark_castle3/dc3/data/sav_pkl', 'wb') as f:
			pickle.dump(master_obj_lst, f)
	return is_start, gs.end.is_end, gs.io.get_buff()
	