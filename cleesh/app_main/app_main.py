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
def app_main(user_input, game_name, root_path_str):
	# initiate app_main() - load obj, declare gs, and reset buffer
	pkl_str = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
	with open(pkl_str, 'rb') as f:
		master_obj_lst = pickle.load(f)
	gs = master_obj_lst[0]
	gs.io.reset_buff()

	# local var declarations 
	is_start = False
	is_wait = False
	is_interp_cmd = True
	is_valid = False
	is_att = False

	# mutually exclusive special command cases
	if user_input.lower() in ['quit', 'q']:
		gs.end.game_ending = 'quit.'
		gs.end.is_end = True
		is_interp_cmd = False
	elif user_input.lower() == 'restart':
		gs.end.game_ending = 'restarted.'
		is_start = True
		is_interp_cmd = False
	elif user_input.lower() in ['again', 'g']:
		user_input = gs.io.last_input_str

	# post-'again', special command cases (must be independent 'if' in case of 'again')
	if user_input.lower() in ['wait', 'z']:
		is_wait = True
		gs.io.buffer("Waiting...")
		is_interp_cmd = False

	# for interp commands, interp user_input and validate command
	if is_interp_cmd:
		case, word_lst = interpreter(user_input, master_obj_lst)
		is_valid, is_att, err_txt = validate(gs, case, word_lst)

	# if command is valid or is_wait, increment move
	if is_valid or is_att or is_wait:
		gs.core.move_inc()

	# for valid interp commands, process in-turn game response
	if is_valid or is_att:
		cmd_override = pre_action(gs, case, word_lst, is_valid)
		if not cmd_override and is_att:
			gs.io.buffer(err_txt)
		if (is_valid and not cmd_override):
			cmd_execute(gs, case, word_lst)
		post_action(gs, case, word_lst) # excluding pots_act() from cmd "if" allows creatures to opperate machs

	# post-cmd-response output
	# action order = 1) cmd input, 2) Game response to cmd, 3) Game end / restart OR Game independent actions
	# action order 1), 3), 2) is confusing because the cause and effect link between 1) & 2) is broken
	if gs.end.is_end or is_start: 
		gs.end.disp_end(gs)
	elif is_wait or is_valid or is_att: # elif to avoid case of auto_act() run after ending from cmd
		auto_action(gs)
	if is_start:
		gs.io.buffer("Restarting...") # appears post 'you have restarted' end text and pre 'welcome' text

	# close out turn - save state and last inupt (for 'again' case) and then return
	# note: need to save state even if is_valid == False else 'again' won't work on error cases
	gs.io.last_input_str = user_input
	with open(pkl_str, 'wb') as f:
		pickle.dump(master_obj_lst, f)
	return is_start, gs.end.is_end, gs.end.game_ending, gs.io.get_buff()
