# program: dark castle
# author: Tom Snellgrove
# module description: app-side wrapper module that calls game functions


### import statements
import traceback
import pickle
from cleesh.app_turn.interp import interpreter
from cleesh.app_turn.validate import validate
from cleesh.app_turn.pre_action import pre_action
from cleesh.app_turn.cmd_exe import cmd_execute
from cleesh.app_turn.post_action import post_action
from cleesh.app_turn.auto_action import auto_action
from cleesh.app_turn.hand_manage import hand_mgmt
from cleesh.app_turn.input_cleanup import input_cleanup


### local functions
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

def weapon_disp(gs, start_in_hand):
	"""display weapon draw / sheathe message"""
	if gs.core.hero.hand_is_empty():
		end_in_hand = None
	else:
		end_in_hand = gs.core.hero.get_hand_item()
	if start_in_hand == end_in_hand:
		return
	if (start_in_hand is not None) and (start_in_hand.is_weapon()):
		gs.io.buffer(f"With the {start_in_hand.full_name} no longer in hand, you are a bit more approachable.")
	if (end_in_hand is not None) and (end_in_hand.is_weapon()):
		gs.io.buffer(f"With the {end_in_hand.full_name} in hand you are now armed and dangerous!")
	return

def meta_cmd_exe(word_lst, gs):
	if len(word_lst) == 1:
		word_lst.append('menu')
	meta_cmd, arg, *_ = word_lst
	try:
		if meta_cmd in ['quit', 'q']:
			gs.end.game_ending = 'quit.'
			gs.end.is_end = True
#			is_interp_cmd = False
			gs.io.reset_cmd_queue()
		elif meta_cmd == 'restart':
			gs.end.game_ending = 'restarted.'
#			is_start = True
#			is_interp_cmd = False
			gs.io.reset_cmd_queue()
		elif meta_cmd == 'score':
#		if meta_cmd == 'score':
			gs.score.print_score(gs)
		elif meta_cmd == 'version':
			gs.io.disp_version(gs)
		elif meta_cmd == 'credits':
			gs.io.buff_e('credits')
		elif meta_cmd == 'verbose':
			gs.io.set_verbosity_mode('verbose', gs)
		elif meta_cmd == 'brief':
			gs.io.set_verbosity_mode('brief', gs)
		elif meta_cmd == 'superbrief':
			gs.io.set_verbosity_mode('superbrief', gs)
		elif meta_cmd == 'rand_mode':
			gs.core.disp_rand_mode(gs)
		elif meta_cmd == 'debug':
			gs.core.set_debug_mode(arg, gs)
		elif meta_cmd == 'help':
			gs.io.disp_help(arg, gs)
		gs.core.move_decr()
		return
	except Exception:
		gs.io.buff_dbg("[APP_MAIN-META] " + traceback.format_exc(), gs)


### loads game obj, calls other modules, and saves game obj ###
def app_main(user_input, game_name, root_path_str):
	# initiate app_main() - load obj, declare gs, and reset buffer & cmd_queue
	pkl_str = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
	with open(pkl_str, 'rb') as f:
		master_obj_lst = pickle.load(f)
	gs = master_obj_lst[0]
	gs.io.reset_buff()
	gs.io.reset_cmd_queue()

	# load cmd queue
	if ',' in user_input:
		gs.io.cmd_queue = user_input.split(',')
	else:
		gs.io.append_cmd_queue(user_input)

	# process each command in the queue
	while gs.io.cmd_queue:
		user_input = gs.io.pop_cmd_queue()

		# local var declarations
		is_start = False
		is_wait = False
		is_interp_cmd = True
		is_meta_cmd = False
		is_valid = False
		is_att = False
		has_except = False
		is_multiples_action = False
		word1 = ""

		# mutually exclusive meta command cases
		if user_input.lower().strip() in ['again', 'g']:
			if len(gs.io.last_input_str) == 0:
				user_input = "look"
			else:
				user_input = gs.io.last_input_str

		user_input_lst = input_cleanup(gs, user_input)
		if len(user_input_lst) == 0:
#			word1 = ""
			gs.io.buffer("I beg your pardon?")
			is_interp_cmd = False
		else:
			word1 = user_input_lst[0]

#		if user_input.lower().strip() in ['quit', 'q']:
#		if word1 in ['quit', 'q']:
#			gs.end.game_ending = 'quit.'
#			gs.end.is_end = True
#			is_interp_cmd = False
#			gs.io.reset_cmd_queue()
#		elif user_input.lower().strip() == 'restart':
#		elif word1 == 'restart':
#			gs.end.game_ending = 'restarted.'
#			is_start = True
#			is_interp_cmd = False
#			gs.io.reset_cmd_queue()
#		elif user_input.lower().strip() in ['again', 'g']:
#		elif word1 in ['again', 'g']:
#			if len(gs.io.last_input_str) == 0:
#				user_input = "look"
#			else:
#				user_input = gs.io.last_input_str
#			user_input_lst = input_cleanup(gs, user_input) # new
#			if len(user_input_lst) == 0: # new
#				word1 = "" # new
#			else: # new
#				word1 = user_input_lst[0] # new

		# post-'again', special command cases (must be independent 'if' in case of 'again')
#		if user_input.lower().strip() in ['wait', 'z']:
		if word1 in ['wait', 'z']:
			is_wait = True
			gs.io.buffer("Waiting...")
			is_interp_cmd = False
		elif word1 in [
				'quit', 'q', 'restart','score', 'version', 'credits', 'verbose', 'brief', 'superbrief', 
				'rand_mode', 'debug', 'help'
				]:
			meta_cmd_exe(user_input_lst, gs)
			if word1 == 'restart':
				is_start = True
			is_interp_cmd = False
			is_meta_cmd = True

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
				gs.io.reset_cmd_queue()
				is_interp_cmd = False
				gs.io.buffer(except_err_str)

		# custom handling for multiples action ('take all' or 'drop all')
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
				gs.io.reset_cmd_queue()
			else:
				gs.io.cmd_queue = multiples_lst + gs.io.cmd_queue
				user_input = gs.io.pop_cmd_queue()
				gs.io.multi_count = len(multiples_lst)

		# for interp commands, interp user_input and validate command
		if is_interp_cmd:
			if gs.core.hero.hand_is_empty():
				start_in_hand = None
			else:
				start_in_hand = gs.core.hero.get_hand_item()
			case, word_lst = interpreter(user_input, master_obj_lst)
			is_valid, is_att, err_txt = validate(gs, case, word_lst)
	
		# if command is not valid, clear cmd_queue
		if not is_valid and not is_meta_cmd and not is_wait:
			gs.io.reset_cmd_queue()

		# if command is valid or is_wait, increment move
		if (is_valid or is_att or is_wait):
			gs.core.move_inc()

		# for valid interp commands, process in-turn game response
		if is_valid or is_att:
			cmd_override = pre_action(gs, case, word_lst, is_valid)
			if cmd_override:
				gs.io.reset_cmd_queue()
			if not cmd_override and is_att:
				gs.io.buffer(err_txt)
			if (is_valid and not cmd_override):
				hand_mgmt(case, word_lst, gs)
				cmd_execute(gs, case, word_lst)
			weapon_disp(gs, start_in_hand)
			post_action(gs, case, word_lst, is_valid) # excluding poat_act() from cmd "if" allows creatures to opperate machs

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
