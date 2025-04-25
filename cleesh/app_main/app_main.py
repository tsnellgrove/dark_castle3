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
		except_element = ""
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

		# custom handling for 'drop all except'
		if user_input.lower().strip().startswith('drop all except'):
			except_err = False
			has_except = True
			except_element = ""
			statement_lst = user_input.split('except')
			if len(statement_lst) > 2:
				gs.io.buffer("You can only use 'except' once in a command.")
				except_err = True
			else:
				user_input = statement_lst[0]
				except_element = statement_lst[1]
				if len(except_element.strip()) == 0 and not except_err: 
					gs.io.buffer("Except what?")
					except_err = True
				else:
					ee_lst = except_element.split()
					if len(ee_lst) > 2:
						gs.io.buffer("You can only 'except' one item in a multiples action.")
						except_err = True
					else:
						if len(ee_lst) == 2:
							except_element = f"{ee_lst[0]}_{ee_lst[1]}"
						if len(ee_lst) == 1:
							except_element = ee_lst[0]
						name_lst = []
						root_lst = []
						temp_root = ""
						for obj in gs.core.hero.hand_lst + gs.core.hero.bkpk_lst:
							name_lst.append(obj.name)
							root_lst.append(obj.root_name)
							if except_element == obj.root_name:
								temp_root = except_element
								except_element = obj.name
						if except_element.lower().strip() not in (name_lst) and not except_err:
							print(f"The {except_element} is not in your inventory.")
							gs.io.buffer(f"The {except_element} is not in your inventory.")
							except_err = True
						if root_lst.count(temp_root) > 1:
							gs.io.buffer(f"You have more than one {temp_root} in your inventory. Please use the full name.")
							except_err = True
			if except_err:
				cmd_queue = []
				multiples_lst = []
				user_input = ""
				is_interp_cmd = False
				except_element = ""

		# custom handling for multiples action
		if user_input.lower().strip() in ['drop all']:
			is_multiples_action = True
			multiples_action_type = 'drop'
			inventory_lst = gs.core.hero.hand_lst + gs.core.hero.bkpk_lst
		if user_input.lower().strip() in ['take all', 'get all']:
			is_multiples_action = True
			multiples_action_type = 'take'
			inventory_lst = gs.core.hero.hand_lst + gs.core.hero.bkpk_lst # fix
		if is_multiples_action:
			multiples_lst = []
			for item in inventory_lst:
				if (has_except) and (item.name == except_element):
					has_except = False
				else:
					multiples_lst.append(f'drop {item.name}')
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
		gs.io.last_input_str = user_input
		if gs.io.multi_count > 0:
			gs.io.multi_count -= 1

	# close out turn with return
	with open(pkl_str, 'wb') as f:
		pickle.dump(master_obj_lst, f)
	return is_start, gs.end.is_end, gs.end.game_ending, gs.end.is_bkstry, gs.io.get_buff()
