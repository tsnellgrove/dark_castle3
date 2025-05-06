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


### loacl functions
def except_mini_interpreter(gs, user_input, inventory_lst):
	""" mini-interpreter for 'except' command in multiples actions """
	gs.io.last_input_str = user_input # assign 'again' value
	statement_lst = user_input.split('except')

	if len(statement_lst) > 2:
		return "", "", True, "You can only use 'except' once in a command."
	user_input = statement_lst[0]
	except_str = statement_lst[1]
	if len(except_str.strip()) == 0:
		return "", "", True, "Except what?"
	ee_lst = except_str.split()
	if len(ee_lst) > 2:
		return "", "", True, "You can only 'except' one item in a multiples action."
	if len(ee_lst) == 2:
		except_element = f"{ee_lst[0]}_{ee_lst[1]}"
	if len(ee_lst) == 1:
		except_element = ee_lst[0]
	name_lst = []
	root_lst = []
	temp_root = "" # elim var initialization?
	for obj in inventory_lst:
		name_lst.append(obj.name)
		root_lst.append(obj.root_name)
		if except_element == obj.root_name:
			temp_root = except_element
			except_element = obj.name
	if except_element.lower().strip() not in (name_lst):
		return "", "", True, f"The {except_element} is not present or cannot be excluded."
	if root_lst.count(temp_root) > 1:
		return "", "", True, f"There is more than one {temp_root} here. Please use the full name."
	return user_input, except_element, False, ""

def multiples_mini_interpreter(gs, user_input, inventory_lst, multiples_action_type, except_element, has_except):
	""" mini-interpreter for multiples actions ('take all', 'drop all') """
	if len(inventory_lst) == 0:
		return [], True, f"There's nothing here you can {multiples_action_type}!"
	if not has_except:
		gs.io.last_input_str = user_input
	multiples_lst = []
	for item in inventory_lst:
		if (has_except) and (item.name == except_element):
			has_except = False
		else:
			multiples_lst.append(f"{multiples_action_type} {item.name}")
	if len(multiples_lst) == 0:
		return [], True, f"With that exception, there's nothing you can {multiples_action_type}."
	return multiples_lst, False, ""

### loads game obj, calls other modules, and saves game obj ###
def app_main(user_input, game_name, root_path_str):
	# initiate app_main() - load obj, declare gs, and reset buffer & cmd_queue
	pkl_str = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
	with open(pkl_str, 'rb') as f:
		master_obj_lst = pickle.load(f)
	gs = master_obj_lst[0]
	gs.io.reset_buff()
	cmd_queue = []

	# load cmd queue
	if ',' in user_input:
		cmd_queue = user_input.split(',')
	else:
		cmd_queue = [user_input]

	# process each command in the queue
	while cmd_queue:
		user_input = cmd_queue.pop(0)

		# local var declarations
		is_start = False
		is_wait = False
		is_interp_cmd = True
		is_valid = False
		is_att = False
		has_except = False
		is_multiples_action = False

		# mutually exclusive special command cases
		if user_input.lower().strip() in ['quit', 'q']:
			gs.end.game_ending = 'quit.'
			gs.end.is_end = True
			is_interp_cmd = False
			cmd_queue = []
		elif user_input.lower().strip() == 'restart':
			gs.end.game_ending = 'restarted.'
			is_start = True
			is_interp_cmd = False
			cmd_queue = []
		elif user_input.lower().strip() in ['again', 'g']:
			user_input = gs.io.last_input_str

		# post-'again', special command cases (must be independent 'if' in case of 'again')
		if user_input.lower().strip() in ['wait', 'z']:
			is_wait = True
			gs.io.buffer("Waiting...")
			is_interp_cmd = False

		# custom handling for 'x all except'
		if user_input.lower().strip().startswith('drop all except'):
			inventory_lst = gs.core.hero.hand_lst + gs.core.hero.bkpk_lst
			has_except = True
		if (user_input.lower().strip().startswith('take all except') 
				or user_input.lower().strip().startswith('get all except')):
			inventory_lst = gs.map.hero_rm.get_take_all_lst(gs)
			has_except = True		
		if has_except:
			user_input, except_element, is_except_err, except_err_str = except_mini_interpreter(gs, user_input, inventory_lst)
			if is_except_err:
				cmd_queue = []
				is_interp_cmd = False
				gs.io.buffer(except_err_str)

		# custom handling for multiples action ('tak all' or 'drop all')
		if user_input.lower().strip() in ['drop all']:
			is_multiples_action = True
			multiples_action_type = 'drop'
			inventory_lst = gs.core.hero.hand_lst + gs.core.hero.bkpk_lst
		if user_input.lower().strip() in ['take all', 'get all']:
			is_multiples_action = True
			multiples_action_type = 'take'
			inventory_lst = gs.map.hero_rm.get_take_all_lst(gs)
		if is_multiples_action:
			except_element = "" if not has_except else except_element
			multiples_lst, is_multiples_err, multiples_err_str = multiples_mini_interpreter(gs, user_input, inventory_lst, multiples_action_type, except_element, has_except)
			if is_multiples_err:
				gs.io.buffer(multiples_err_str)
				is_interp_cmd = False
				cmd_queue = []
			else:
				cmd_queue = multiples_lst + cmd_queue
				user_input = cmd_queue.pop(0)
				gs.io.multi_count = len(multiples_lst)

		# for interp commands, interp user_input and validate command
		if is_interp_cmd:
			case, word_lst = interpreter(user_input, master_obj_lst)
			is_valid, is_att, err_txt = validate(gs, case, word_lst)

		# if command is not valid, clear cmd_queue
		if not is_valid:
			cmd_queue = []

		# if command is valid or is_wait, increment move
		if is_valid or is_att or is_wait:
			gs.core.move_inc()

		# for valid interp commands, process in-turn game response
		if is_valid or is_att:
			cmd_override = pre_action(gs, case, word_lst, is_valid)
			if cmd_override:
				cmd_queue = []
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

		# save state and last inupt (for 'again' case)
		# note: need to save state even if is_valid == False else 'again' won't work on error cases
		if gs.io.multi_count == 0:
			gs.io.last_input_str = user_input
		if gs.io.multi_count > 0:
			gs.io.multi_count -= 1

	# close out turn with return
	with open(pkl_str, 'wb') as f:
		pickle.dump(master_obj_lst, f)
	return is_start, gs.end.is_end, gs.end.game_ending, gs.end.is_bkstry, gs.io.get_buff()
