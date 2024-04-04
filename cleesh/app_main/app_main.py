# program: dark castle
# author: Tom Snellgrove
# module description: app-side wrapper module that calls game functions


### import statements
import pickle
from cleesh.app_turn.interp import interpreter
from cleesh.app_turn.validate import validate
from cleesh.app_turn.pre_action import pre_action
from cleesh.app_turn.cmd_exe import cmd_execute
from cleesh.app_turn.post_action import post_action
from cleesh.app_turn.auto_action import auto_action

### loads game obj, calls other modules, and saves game obj ###
def app_main(user_input):
	# initiate app_main() - load obj, declare gs, and reset buffer
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/data/sav_pkl', 'rb') as f:
		master_obj_lst = pickle.load(f)
	gs = master_obj_lst[0]
	gs.io.reset_buff()

	# local var declarations 
	is_start = False
	is_stateful = False
	is_interp_cmd = True
	is_interp_valid = False

	# mutually exclusive non-interp command cases
	if user_input.lower() == 'quit' or user_input.lower() == 'q':
		gs.end.game_ending = 'quit.'
		gs.end.is_end = True
		is_interp_cmd = False
	elif user_input.lower() == 'restart':
		gs.end.game_ending = 'restarted.'
		is_start = True
		is_interp_cmd = False
	elif user_input.lower() == 'again' or user_input.lower() == 'g':
		user_input = gs.io.last_input_str

	# post-'again', non-interp command cases (must be independent 'if' in case of 'again')
	if user_input.lower() == 'wait' or user_input.lower() == 'z':
		is_stateful = True
		gs.io.buffer("Waiting...")
		is_interp_cmd = False

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

	# close out turn - save state and last inupt (for 'again' case) and then return
	# note: need to save state even if is_stateful == False else 'again' won't work on error cases
	gs.io.last_input_str = user_input
	with open('/Users/tas/Documents/Python/dark_castle3/cleesh/data/sav_pkl', 'wb') as f:
		pickle.dump(master_obj_lst, f)
	return is_start, gs.end.is_end, gs.io.get_buff()
	