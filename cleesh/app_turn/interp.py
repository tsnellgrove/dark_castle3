# program: dark castle
# author: Tom Snellgrove
# module description: converts player input into game commands


### import statements


### input_cleanup - user_input str to lst, lower, convert abbrev & verb_syn, remove articles / buzz
def input_cleanup(gs, user_input):
	# first, convert to lower case and strip leading/trailing whitespace
	user_input = user_input.lower().strip()

	# second, convert user input string into word list
	lst = []
	lst.append(user_input)
	user_input_lst = lst[0].split()

	# third, substitute abbreviationss and verb_syn
	abbrev_dict = gs.io.get_dict('abbreviations_dict','eng')
	verb_syn_dict = gs.io.get_dict('verb_syn_dict','eng')
	for index, word in enumerate(user_input_lst):
		if word in abbrev_dict:
			user_input_lst[index] = abbrev_dict[word]
		elif word in verb_syn_dict:
			user_input_lst[index] = verb_syn_dict[word]

	# finally, strip out articles / buzz words
	for article in gs.io.get_lst('articles_lst','eng'):
		user_input_lst = [word for word in user_input_lst if word != article]
	return user_input_lst


### syntax - convert user_input_lst into a case and action_lst
def syntax(user_input_tpl, input_verb, do_noun, prep_dir_opt, id_noun, gs):

	syntax_dict = {
		('climb', 'hero_dir', 'input_do_noun') : {
			'case' : 'action_dir',
			'base_action_lst' : ['climb', 'hero_dir', 'do_noun_str']
		},
		('climb', 'input_do_noun') : {
			'case' : 'action_dir',
			'base_action_lst' : ['climb', 'up_or_down_dir', 'do_noun_str']
		},
		('meta_cmd',) : {
			'case' : 'tru_1word',
			'base_action_lst' : ['verb_str']
		},
		('help', 'option') : {
			'case' : 'help',
			'base_action_lst' : ['verb_str', 'hero_dir']
		},
		
		('close', 'input_do_noun') : ['close', 'do_noun_str', 'verb_do'],
		('close', 'up', 'input_do_noun') : ['close', 'do_noun_str', 'verb_do'],
		('shut', 'verb_syn') : ['close'],

		('doff', 'input_do_noun') : ['doff', 'do_noun_str', 'verb_do'],

		('drop', 'input_do_noun') : ['drop', 'do_noun_str', 'verb_do'],
		('release', 'verb_syn') : ['drop'],

		('eat', 'input_do_noun') : ['eat', 'do_noun_str', 'verb_do'],
		('bite', 'verb_syn') : ['eat'],
		('consume', 'verb_syn') : ['eat'],
		('devour', 'verb_syn') : ['eat'],
		('gobble', 'verb_syn') : ['eat'],
		('ingest', 'verb_syn') : ['eat'],
		('munch', 'verb_syn') : ['eat'],
		('taste', 'verb_syn') : ['eat'],

		('enter', 'input_do_noun') : ['enter', 'do_noun_str', 'verb_do'],
		('go', 'in', 'prep_phrase_convert') : ['enter'],
		('get', 'in', 'prep_phrase_convert') : ['enter'],

		('examine', 'input_do_noun') : ['examine', 'do_noun_str', 'verb_do'],
		('inventory',) : ['examine', 'hero_obj', 'verb_do'],
		('look', 'input_do_noun') : ['examine', 'do_noun_str', 'verb_do'],
		('look', 'at', 'input_do_noun') : ['examine', 'do_noun_str', 'verb_do'],
		('look', 'in', 'input_do_noun') : ['examine', 'do_noun_str', 'verb_do'],
		('describe', 'verb_syn') : ['examine'],
		('inspect', 'verb_syn') : ['examine'],
		('search', 'verb_syn') : ['examine'],
		('list', 'verb_syn') : ['inventory'],

		('exit', 'input_do_noun') : ['exit', 'do_noun_str', 'verb_do'],
		('get', 'out', 'prep_phrase_convert') : ['exit'],
		('depart', 'verb_syn') : ['exit'],
##		('out', 'verb_syn') : ['enter'],

		('go', 'east') : ['go', 'hero_rm_obj', 'east', 'verb_do_prep'],
		('go', 'west') : ['go', 'hero_rm_obj', 'west', 'verb_do_prep'],
		('go', 'north') : ['go', 'hero_rm_obj', 'north', 'verb_do_prep'],
		('go', 'south') : ['go', 'hero_rm_obj', 'south', 'verb_do_prep'],
		('go', 'northeast') : ['go', 'hero_rm_obj', 'northeast', 'verb_do_prep'],
		('go', 'northwest') : ['go', 'hero_rm_obj', 'northwest', 'verb_do_prep'],
		('go', 'southeast') : ['go', 'hero_rm_obj', 'southeast', 'verb_do_prep'],
		('go', 'southwest') : ['go', 'hero_rm_obj', 'southwest', 'verb_do_prep'],
		('go', 'up') : ['go', 'hero_rm_obj', 'up', 'verb_do_prep'],
		('go', 'down') : ['go', 'hero_rm_obj', 'down', 'verb_do_prep'],
		('proceed', 'verb_syn') : ['go'],
		('run', 'verb_syn') : ['go'],
		('step', 'verb_syn') : ['go'],
		('walk', 'verb_syn') : ['go'],

		('jump',) : ['jump', 'hero_obj', 'verb_do'],
		('jump', 'up') : ['jump', 'hero_obj', 'verb_do'],
		('jump', 'down') : ['jump', 'hero_obj', 'verb_do'],
		('leap', 'verb_syn') : ['jump'],
		('vault', 'verb_syn') : ['jump'],

		('move', 'input_do_noun') : ['move', 'do_noun_str', 'verb_do'],
		('slide', 'verb_syn') : ['move'],
		('roll', 'verb_syn') : ['move'],

		('open', 'input_do_noun') : ['open', 'do_noun_str', 'verb_do'],
		('open', 'up', 'input_do_noun') : ['open', 'do_noun_str', 'verb_do'],

		('pull', 'input_do_noun') : ['pull', 'do_noun_str', 'verb_do'],
		('pull', 'on', 'input_do_noun') : ['pull', 'do_noun_str', 'verb_do'],
		('pull', 'up', 'input_do_noun') : ['pull', 'do_noun_str', 'verb_do'],
		('pull', 'down', 'input_do_noun') : ['pull', 'do_noun_str', 'verb_do'],
		('tug', 'verb_syn') : ['pull'],
		('yank', 'verb_syn') : ['pull'],

		('push', 'input_do_noun') : ['push', 'do_noun_str', 'verb_do'],
		('push', 'on', 'input_do_noun') : ['push', 'do_noun_str', 'verb_do'],
		('press', 'verb_syn') : ['push'],
		('shove', 'verb_syn') : ['push'],

		('read', 'input_do_noun') : ['read', 'do_noun_str', 'verb_do'],
		('read', 'from', 'input_do_noun') : ['read', 'do_noun_str', 'verb_do'],
		('scan', 'verb_syn') : ['read'],
		('skim', 'verb_syn') : ['read'],
		('peruse', 'verb_syn') : ['read'],

		('sit', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'in', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'on', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'into', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'down', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'down', 'in', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'down', 'on', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],
		('sit', 'down', 'into', 'input_do_noun') : ['sit', 'do_noun_str', 'verb_do'],

		('stand',) : ['stand', 'hero_obj', 'verb_do'],
		('stand', 'up') : ['stand', 'hero_obj', 'verb_do'],

		('stow', 'input_do_noun') : ['stow', 'do_noun_str', 'verb_do'],
		('pack', 'verb_syn') : ['stow'],
		('stash', 'verb_syn') : ['stow'],

		('take', 'input_do_noun') : ['take', 'do_noun_str', 'verb_do'],
		('get', 'input_do_noun') : ['take', 'do_noun_str', 'verb_do'],
		('grab', 'verb_syn') : ['take'],
		('remove', 'verb_syn') : ['take'],
		('hold', 'verb_syn') : ['take'],
		('carry', 'verb_syn') : ['take'],

		('wear', 'input_do_noun') : ['wear', 'do_noun_str', 'verb_do'],
		('don', 'verb_syn') : ['wear'],

		# debug cmds
		('get_weight', 'input_do_noun') : ['get_weight', 'do_noun_str', 'verb_do'],
		('capacity', 'input_do_noun') : ['capacity', 'do_noun_str', 'verb_do'],
		('where_is', 'input_do_noun') : ['where_is', 'do_noun_str', 'verb_do'],
	}
	try:
		base_action_lst = syntax_dict[user_input_tpl]
	except:
		return 'error', ["I don't understand that command!"]
	if isinstance(base_action_lst, list):
		case = 'universal'
	else:
		base_action_lst = syntax_dict[user_input_tpl]['base_action_lst']
		case = syntax_dict[user_input_tpl]['case']
	action_lst = base_action_lst.copy()
	for index, word in enumerate(base_action_lst):
		if word == 'hero_obj':
			action_lst[index] = gs.core.hero # convert class noun to object
		if word == 'hero_rm_obj':
			action_lst[index] = gs.map.hero_rm # convert class noun to object
		if word == 'hero_dir':
			action_lst[index] = prep_dir_opt # string
		if word == 'verb_str':
			action_lst[index] = input_verb # string
		if word == 'do_noun_str':
			action_lst[index] = gs.core.get_str_to_obj_dict(do_noun) # convert to obj
		if word == 'up_or_down_dir': # direction not given but can be inferred
			if gs.map.chk_valid_dir(gs.map.hero_rm, 'up') and not gs.map.chk_valid_dir(gs.map.hero_rm, 'down'):
				action_lst[index] = 'up'
				gs.io.buffer(f"(choosing the 'up' direction in which to climb)")
			elif gs.map.chk_valid_dir(gs.map.hero_rm, 'down') and not gs.map.chk_valid_dir(gs.map.hero_rm, 'up'):
				action_lst[index] = 'down'
				gs.io.buffer(f"(choosing the 'down' direction in which to climb)")
			else:
				case = 'error'
				action_lst = ["Which way do you want to climb, up or down?"]
				break
		if word == 'infer_do_noun':
			if input_verb in ['climb']:
				exactly_one_climbable, climbable_obj = infer_climbable(gs)
				if exactly_one_climbable:
					gs.io.buffer(f"(the {climbable_obj.full_name})")
					action_lst = [input_verb, climbable_obj.name]
					case = None
					break
				else:
					case = 'error'
					action_lst = [f"{input_verb.capitalize()} what?"]
				break			
			else:
				case = 'error'
				action_lst = [f"{input_verb.capitalize()} what?"]
				break
	return case, action_lst

def asym_syn(action_lst, gs):
	verb_str= action_lst[0]
	do_noun_obj = action_lst[1]
	case = 'universal'
	if verb_str in ['enter']:
		if do_noun_obj.is_seat():
			action_lst[0] = 'sit'
		elif (
				(do_noun_obj.is_door() or do_noun_obj.is_pathway()) 
				and gs.map.hero_rm.chk_is_vis(do_noun_obj, gs)
			):
			dir_str = gs.map.get_door_dir(gs.map.hero_rm, do_noun_obj, gs)
			action_lst = ['go', gs.map.hero_rm, dir_str, 'verb_do_prep']
#	if verb_str in ['exit'] and gs.core.hero.is_contained(gs) and do_noun_obj == gs.core.hero.get_contained_by(gs):
#		action_lst = ['stand', gs.core.hero, 'verb_do']

	if verb_str in ['exit']:
		if gs.core.hero.is_contained(gs) and do_noun_obj == gs.core.hero.get_contained_by(gs):
			action_lst = ['stand', gs.core.hero, 'verb_do']
#		elif do_noun_obj.is_room() and gs.map.get_neighbor_count(do_noun_obj) ==1:
		elif do_noun_obj == gs.map.hero_rm:
			is_only_1_exit, dir_str = gs.map.only_exit_dir(do_noun_obj, gs)
			if is_only_1_exit:
				action_lst = ['go', do_noun_obj, dir_str, 'verb_do_prep']
			else:
				case = 'error'
				action_lst = [f"Which way do you want to go?"]

#			door = None # temp value; need to repalce with is_only_1_exit, dir_str = gs.map.only_exit_dir(room, gs)
#			dir_str = gs.map.get_door_dir(gs.map.hero_rm, do_noun_obj, gs)
#			action_lst = ['go', gs.map.hero_rm, dir_str, 'verb_do_prep']
	if verb_str in ['take'] and do_noun_obj in gs.core.hero.worn_lst:
		action_lst[0] = 'doff'
	if verb_str in ['examine'] and do_noun_obj.is_writing():
		action_lst[0] = 'read'
	if verb_str in ['move']:
		if do_noun_obj.is_pushable() and not do_noun_obj.is_pullable():
			action_lst[0] = 'push'
		elif do_noun_obj.is_pullable() and not do_noun_obj.is_pushable():
			action_lst[0] = 'pull'
		elif do_noun_obj.is_pushable() and do_noun_obj.is_pullable():
			case = 'error'
			action_lst = [f"Are you trying to push the {do_noun_obj.full_name} or pull it?"]
	return case, action_lst

### unified infer verb function for all verbs ###
def infer_verb(prep_str, gs):
	verb_inferred = False
	verb_str = ''
	if prep_str in ['east', 'west', 'north', 'south', 'northeast', 'northwest', 'southeast', 'southwest', 'up', 'down', 'in']:
		verb_inferred = True
		verb_str = 'go'
	return verb_inferred, verb_str

### unified infer do_noun function for all verbs ###
def infer_do_noun(gs, verb_str):
	scope_lst = gs.map.hero_rm.get_vis_contain_lst(gs)
	do_noun_count = 0
	do_noun_obj = None
	err_txt = f"What do you want to {verb_str}?"
	infer_txt = None

	if verb_str in ['doff'] and len(gs.core.hero.worn_lst) == 1:
		do_noun_count = 1
		do_noun_obj = gs.core.hero.worn_lst[0]
		infer_txt = f"(the {do_noun_obj.full_name})"
	elif verb_str == 'enter':
		seat_count = 0
		door_count = 0
		pathway_count = 0
		for obj in gs.map.hero_rm.get_vis_contain_lst(gs):
			if obj.is_seat():
				seat_count += 1
				seat_obj = obj
			if obj.is_door():
				door_count += 1
				door_obj = obj
			if obj.is_pathway():
				pathway_count += 1
				pathway_obj = obj
		if seat_count == 1:
			do_noun_count = 1
			do_noun_obj = seat_obj
		elif door_count == 1:
			do_noun_count = 1
			do_noun_obj = door_obj
		elif pathway_count == 1:
			do_noun_count = 1
			do_noun_obj = pathway_obj
		if do_noun_count == 1:
			infer_txt = f"(the {do_noun_obj.full_name})"			
	elif verb_str == 'sit':
		err_txt = "Where do you want to sit?"
		for obj in scope_lst:
			if obj.is_seat():
				do_noun_count += 1
				do_noun_obj = obj
				infer_txt = f"(in the {do_noun_obj.full_name})"	
	elif verb_str == 'look':
		do_noun_count = 1
		do_noun_obj = gs.map.hero_rm
	elif verb_str in ['drop', 'stow', 'eat', 'wear'] and not gs.core.hero.hand_is_empty():
		do_noun_count = 1
		do_noun_obj = gs.core.hero.get_hand_item()
		infer_txt = f"(the {gs.core.hero.get_hand_item().full_name})"
	elif verb_str == 'exit' and gs.core.hero.is_contained(gs):
		do_noun_count = 1
		do_noun_obj = gs.core.hero.get_contained_by(gs)
		infer_txt = f"(from the {do_noun_obj.full_name})"

	if do_noun_count == 1 and infer_txt is not None:
		gs.io.buffer(infer_txt)
	return do_noun_count == 1, do_noun_obj, err_txt


### helper function for climb command - infer that if there is only one climbable surface in the room, that's what the player wants to climb
def infer_climbable(gs):
	scope_lst = gs.map.hero_rm.get_vis_contain_lst(gs)
	climbable_count = 0
	climbable_obj = None
	for obj in scope_lst:
		if obj.is_climbable():
			climbable_count += 1
			climbable_obj = obj
	return climbable_count == 1, climbable_obj


### handle nouns and adjectives
def noun_handling(master_obj_lst, user_input_lst):
	gs = master_obj_lst[0]
	word2_txt = user_input_lst[1]

	# convert 3-word verb-adj-noun commands into verb-obj_name commands
	if len(user_input_lst) == 3:
		word3_txt = user_input_lst[2]
		user_input_lst[1] = word2_txt + "_" + word3_txt
		word2_txt = user_input_lst[1]
		del user_input_lst[2]

	# error out commands that are still longer than two words
	if len(user_input_lst) > 2:
		return True, f"Can you state that more simply? {gs.core.hero.full_name} is a person of few words!", None

	try: # check to see if word2 is a known obj_name
		word2_obj = gs.core.get_str_to_obj_dict(word2_txt)
	except: # check to see if the word2 is a root_name; convert to obj_name if valid
		scope_lst = gs.map.hero_rm.get_vis_contain_lst(gs)
		root_count = 0
		for obj in scope_lst:
			if obj.root_name == word2_txt:
				root_count += 1
				word2_obj = obj
			if obj.has_writing():
				if obj.writing.root_name == word2_txt:
					root_count += 1
					word2_obj = obj.writing
		if root_count < 1:
			return True, f"I don't see a {word2_txt.capitalize()} here.", None
		if root_count > 1:
			return True, f"I see more than one {word2_txt.capitalize()}. Please use the full name.", None
	return False, "", word2_obj


### interpreter - determine user intent
def interpreter(user_input, master_obj_lst):

	# *** user_input to cleaned-up user_input_lst conversion ***
	gs = master_obj_lst[0]
	user_input_lst = input_cleanup(gs, user_input)

	# *** initial error checking ***
	# error if no input or the only input is articles 
	if len(user_input_lst) < 1: 
		return 'error', ["I have no idea what you're talking about!"]
	# errro if user input contains reserved syntax words
	for word in user_input_lst:
		if word in ['verb_syn', 'hero_rm_obj', 'hero_dir', 'verb_str', 'do_noun_str', 'up_or_down_dir']: # reserved syntax
			return 'error', [f"What??"]
	# one-word commands where user_input_lst is longer than one word
	if len(user_input_lst) > 1 and user_input_lst[0] in (
			gs.io.get_lst('pre_interp_word_lst','eng') + 
			gs.io.get_lst('one_word_only_lst','eng') + 
			gs.io.get_lst('one_word_secret_lst','eng') +
			gs.io.get_lst('one_word_travel_lst','eng') # added
			):
		return 'error', [f"There are too many words in that sentence. '{user_input_lst[0].capitalize()}' is a one word command!"]
#	if len(user_input_lst) > 2 and user_input_lst[0] in ['help', 'go']:
	if len(user_input_lst) > 2 and user_input_lst[0] in ['help']:
		return 'error', [f"Can you state that more simply? {gs.core.hero.full_name} is a person of few words!"]

	# *** global variable assignment ***
	word1 = user_input_lst[0]
	creature = gs.core.hero
	tst_mode = gs.core.is_debug # test mode is linked to debug mode

	action_verb_lst = [
			'close', 'doff', 'drop', 'eat', 'enter', 'examine', 'exit', 'go', 'jump', 
			'open', 'move', 'push', 'pull', 'read', 'sit', 'stand', 'stow', 'take', 'wear'
			] # action_verbs have a method and / or err routine
	non_action_verb_lst = [
			'get', 'inventory', 'look'
			] # non-action verbs are subsituted in syntax or asym_syn()
	syn_verb_lst = [
			'bite', 'carry', 'consume', 'depart', 'describe', 'devour', 'don', 'gobble', 'grab', 'hold', 
			'ingest', 'inspect', 'leap', 'list', 'munch', 'pack', 'peruse', 'press', 'proceed', 
			'release', 'remove', 'roll', 'run', 'scan', 'shut', 'skim', 'search', 'shove', 'slide', 
			'stash', 'step', 'taste', 'tug', 'vault', 'walk', 'yank'
			] # symetric syn_verbs are substituted pre do_noun infer
	debug_cmd_lst = ['get_weight', 'capacity', 'where_is']
	verb_lst = action_verb_lst + non_action_verb_lst + syn_verb_lst + debug_cmd_lst
	dir_lst = ['east', 'west', 'north', 'south', 'northeast', 'northwest', 'southeast', 'southwest', 'up', 'down']

	meta_cmd_lst = gs.io.get_lst('one_word_only_lst','eng') + gs.io.get_lst('one_word_secret_lst','eng')
	full_verbs_lst = (
			gs.io.get_lst('known_verb_lst','eng') + 
			gs.io.get_lst('debug_verb_lst','eng') +
			gs.io.get_lst('non_action_verb_lst','eng') +
			gs.io.get_lst('one_word_convert_lst','eng') # new
			)
	case = None
	action_lst = None

	# *** one-word and meta commands ***
	if word1 in meta_cmd_lst: # e.g. credits, score, version, verbose, brief, superbrief
		case, action_lst = syntax(('meta_cmd',), word1, None, None, None, gs)
	elif word1 in ['help']:
		if len(user_input_lst) == 1:
			option = 'menu'
		else:
			option = user_input_lst[1]
		case, action_lst = syntax(('help', 'option'), word1, None, option, None, gs)


	# handle sit commands - special case because includes prep
	elif word1 in (verb_lst + dir_lst + ['in']):
		prep = None # LEGACY
		verb_cmd_lst = [] # new
		dir_cmd_lst = [] # new
		do_prep_cmd_lst = [] # new
		do_noun_cmd_lst = [] # new
		id_prep_cmd_lst = [] # new
		id_noun_cmd_lst = [] # new
		verb_index = None # new
		dir_index = None # new
		do_prep_index = None # new
		do_noun_index = None # new
		id_prep_index = None # new
		id_noun_index = None # new
		verb_count = 0 # new
		dir_count = 0 # new
		do_prep_count = 0 # new
		do_noun_count = 0 # new
		id_prep_count = 0 # new
		id_noun_count = 0 # new
		for index, word in enumerate(user_input_lst):
			if word in verb_lst:
				verb_cmd_lst.append(word)
				verb_index = index
				verb_count += 1
			elif word in gs.io.get_lst('one_word_travel_lst','eng') and do_prep_count == 0: # only count as direction if no prep has been identified yet
				dir_cmd_lst.append(word)
				dir_index = index
				dir_count += 1
			elif word in gs.io.get_lst('prep_lst','eng') and do_noun_count == 0: # only count as do_prep if no do_noun has been identified yet
				do_prep_cmd_lst.append(word)
				do_prep_index = index
				do_prep_count += 1
			elif id_prep_count == 0: # only count as do_noun if no id_prep has been identified yet
				do_noun_cmd_lst.append(word)
				do_noun_index = index
				do_noun_count += 1
			elif word in gs.io.get_lst('prep_lst','eng') and do_noun_count > 0: # only count as id_prep if do_noun has already been identified
				id_prep_cmd_lst.append(word)
				id_prep_index = index
				id_prep_count += 1
			elif id_prep_count > 0: # only count as id_noun if id_prep has already been identified
				id_noun_cmd_lst.append(word)
				id_noun_index = index
				id_noun_count += 1
		
		if verb_count == 0:
			verb_inferred, verb_str = infer_verb(word1, gs)
			if verb_inferred:
				verb_count = 1
				verb_cmd_lst.append(verb_str)
			else:
				return 'error', ["Please start your sentence with a known verb!"]
		if verb_cmd_lst[0] in debug_cmd_lst and not gs.core.is_debug:
			return 'error', ["Please start your sentence with a known verb!"]
		if (verb_count > 1): # e.g. 'help attack' already dealt with in one-word command processing
			return 'error', ['I see more than one verb in that sentence!']
		
		user_cmd_lst_pre_syn = verb_cmd_lst + dir_cmd_lst + do_prep_cmd_lst + do_noun_cmd_lst + id_prep_cmd_lst + id_noun_cmd_lst
		if tst_mode:
			print(f"user_cmd_lst_pre_syn: {user_cmd_lst_pre_syn}")

		# apply symetric synonym verb substitution before do_noun inference: 'leap' => 'jump'
		err_chk, tmp_lst = syntax((verb_cmd_lst[0], 'verb_syn'), None, None, None, None, gs)
		if err_chk != 'error':
			verb_cmd_lst = tmp_lst
			word1 = verb_cmd_lst[0]

		if do_prep_count > 0:
			err_chk, tmp_lst = syntax(tuple(verb_cmd_lst + do_prep_cmd_lst + ['prep_phrase_convert']), None, None, None, None, gs)
			if err_chk != 'error':
				verb_cmd_lst = tmp_lst
				do_prep_cmd_lst = []
				word1 = verb_cmd_lst[0]

		user_cmd_lst_syn = verb_cmd_lst + dir_cmd_lst + do_prep_cmd_lst + do_noun_cmd_lst + id_prep_cmd_lst + id_noun_cmd_lst # new
		if tst_mode:
			print(f"user_cmd_lst_syn: {user_cmd_lst_syn}")

		if do_noun_count > 0:
			do_noun_cmd_lst.insert(0, 'blank') # temporary placeholder for verb in noun_handling call
			error_state, error_msg, do_noun_obj = noun_handling(master_obj_lst, do_noun_cmd_lst) # in future, pass without verb and prep
			if error_state:
				return 'error', [error_msg]
			else: # if no error, assign do_noun_obj.name to do_noun_cmd_lst for syntax call
				do_noun_cmd_lst = [do_noun_obj.name]
				do_noun_str = do_noun_obj.name # new - for syntax call
				syntax_do_lst = ['input_do_noun'] # new - for syntax call
		elif user_cmd_lst_syn[0] in ['go', 'inventory', 'stand', 'jump']:
			do_noun_obj = None
			syntax_do_lst = []
			do_noun_str = None
		else:
			exactly_one, do_noun_obj, err_txt = infer_do_noun(gs, word1)
			if exactly_one:
				do_noun_cmd_lst = [do_noun_obj.name]
				syntax_do_lst = ['input_do_noun'] # new - for syntax call
				do_noun_str = do_noun_obj.name # new - for syntax call
			else:
				return 'error', [err_txt]

		if id_noun_count > 0:
			id_noun_cmd_lst.insert(0, 'blank') # temporary placeholder for verb in noun_handling call
			error_state, error_msg, id_noun_obj = noun_handling(master_obj_lst, id_noun_cmd_lst) # in future, pass without verb and prep
			if error_state:
				return 'error', [error_msg]
			else: # if no error, assign do_noun_obj.name to do_noun_cmd_lst for syntax call
				id_noun_cmd_lst = [id_noun_obj.name]
				id_noun_syn_lst = ['input_id_noun']
		else:
			id_noun_obj = None
			id_noun_syn_lst = []

		user_cmd_lst_post_infer = verb_cmd_lst + dir_cmd_lst + do_prep_cmd_lst + do_noun_cmd_lst + id_prep_cmd_lst + id_noun_cmd_lst
		if tst_mode:
			print(f"user_cmd_lst_post_infer: {user_cmd_lst_post_infer}")

		user_syntax_lst = verb_cmd_lst + dir_cmd_lst + do_prep_cmd_lst + syntax_do_lst + id_prep_cmd_lst + id_noun_syn_lst
		if tst_mode:
			print(f"user_syntax_lst: {user_syntax_lst}")

		case, action_lst = syntax(tuple(user_syntax_lst), word1, do_noun_str, prep, None, gs)
		if case == 'error':
			return case, action_lst

		if tst_mode:
			print(f"pre-asym-syn action_lst: {action_lst}")

		case, action_lst = asym_syn(action_lst, gs)

		if tst_mode:
			print(f"post-asym-syn action_lst: {action_lst}")

		return case, action_lst


	elif len(user_input_lst) == 1:
			if word1 in full_verbs_lst:
				pass # let it through to syntax for verb-only command processing
#				case, action_lst = syntax(('infer_verb',), word1, None, None, None, gs)
			else:
				case = 'error'
				action_lst = ["What??"]

	if case is not None:
		return case, action_lst
	elif case is None and action_lst is not None: # infer noun case for non-2word commands - e.g. climb
		user_input_lst = action_lst
	# *** end of one-word command processing ***


	# *** start of multi-word command processing ***

	# initial multi-word error cases
	verb_count = 0
	verb_count = sum(1 for word in user_input_lst if word in full_verbs_lst)
	if verb_count == 0:
		return 'error', ['I don\'t see a verb in that sentence!']
	elif (verb_count > 1): # e.g. 'help attack' already dealt with in one-word command processing
		return 'error', ['I see more than one verb in that sentence!']
	if word1 not in full_verbs_lst:
		return 'error', ["Please start your sentence with a known verb!"]

	# handle climb commands - special case because may include direction
	if word1 in ['climb']:
		direction = None
		if user_input_lst[1] in gs.io.get_lst('one_word_travel_lst','eng'):
			direction = user_input_lst[1]
			user_input_lst.remove(direction)
		if len(user_input_lst) == 1:
			exactly_one, climbable_obj = infer_climbable(gs)
			if exactly_one:
				gs.io.buffer(f"(the {climbable_obj.full_name})")
				case, action_lst = syntax((word1, 'hero_dir', 'input_do_noun'), word1, climbable_obj.name, direction, None, gs)
				return case, action_lst
			else:
				return 'error', [f"What do you want to {word1}?"] # direction provided but no do_noun given
		error_state, error_msg, do_noun_obj = noun_handling(master_obj_lst, user_input_lst) # pass without verb
		if error_state:
			return 'error', [error_msg]
		if direction:
			case, action_lst = syntax((word1, 'hero_dir', 'input_do_noun'), word1, do_noun_obj.name, direction, None, gs)
		else:
			case, action_lst = syntax((word1, 'input_do_noun'), word1, do_noun_obj.name, None, None, gs)
		return case, action_lst


	# handle prep verb commands (special cases first else general case)
	# [SYNTAX start here]

	elif word1 in gs.io.get_lst('prep_verb_lst','eng'):
		if word1 in ['put']:
			if 'in' in user_input_lst:
				prep = 'in'
			elif 'on' in user_input_lst:
				prep = 'on'
			else:
				prep = 'in or on'
		elif word1 in ['show', 'give']:
			prep = 'to'
		elif word1 in ['lock', 'unlock']:
			creature = gs.core.hero
			prep = 'with'
			if len(user_input_lst) < 4 and 'with' not in user_input and not creature.hand_is_empty():
				user_input_lst.extend(['with',creature.get_hand_item().name])
				gs.io.buffer(f"(with the {creature.get_hand_item().full_name})")
		elif word1 in ['attack']:
			creature = gs.core.hero
			prep = 'with'
			if ((len(user_input_lst) < 4) and ('with' not in user_input) 
	   				and (not creature.in_hand_is_weapon()) and (creature.has_weapon(gs))):
				drawn_weapon = creature.get_weapon(gs)
				creature.remove_item(drawn_weapon, gs)
				creature.put_in_hand(drawn_weapon, gs)
				user_input_lst.extend(['with', drawn_weapon.name])
				gs.io.buffer(f"(Sensing imminent combat, you draw the {drawn_weapon.full_name})")			
			elif len(user_input_lst) < 4 and 'with' not in user_input and not creature.hand_is_empty():
				user_input_lst.extend(['with',creature.get_hand_item().name])
				gs.io.buffer(f"(with the {creature.get_hand_item().full_name})")
			elif len(user_input_lst) == 2 and 'with' not in user_input and creature.hand_is_empty():
				user_input_lst.extend(['with',creature.feature_lst[0].name])
				gs.io.buffer(f"(with your {creature.feature_lst[0].full_name})")
		elif word1 in ['drink']:
			creature = gs.core.hero
			if len(user_input_lst) < 4 and 'from' not in user_input and not creature.hand_is_empty():
				user_input_lst.extend(['from',creature.get_hand_item().name])
				gs.io.buffer(f"(from the {creature.get_hand_item().full_name})")
			prep = 'from'
		if prep not in user_input_lst:
			error_msg = f"I don't see the word '{prep}' in that sentence."
			return 'error', [error_msg]
		if len(user_input_lst) < 4:
			error_msg = "That sentence doesn't appear to be complete"
			return 'error', [error_msg]
		# [SYNTAX end here]
		else:
			in_position = user_input_lst.index(prep)
			v_n_lst = user_input_lst[:in_position] # elim verb ?
			p_p_lst = user_input_lst[in_position:] # elim prep ?
			noun_error_state, noun_error_msg, noun_obj = noun_handling(master_obj_lst, v_n_lst) # pass without verb
			dir_obj_error_state, dir_obj_error_msg, dirobj_obj = noun_handling(master_obj_lst, p_p_lst) # pass without prep
			if noun_error_state:
				return 'error', [noun_error_msg]
			elif dir_obj_error_state:
				return 'error', [dir_obj_error_msg]
			if dirobj_obj.is_container() and word1 == 'put' and prep != dirobj_obj.prep:
				error_msg = f"I don't see the word '{dirobj_obj.prep}' in that sentence."
				return 'error', [error_msg]
			elif word1 in ['attack', 'lock', 'unlock', 'drink']:
				if not gs.core.hero.chk_in_hand(dirobj_obj) and gs.core.hero.chk_in_bkpk(dirobj_obj):
					gs.core.hero.put_in_hand(dirobj_obj, gs)
					gs.core.hero.bkpk_lst_remove(dirobj_obj)
				if not gs.core.hero.chk_in_hand(dirobj_obj) and gs.core.hero.chk_is_worn(dirobj_obj):
					gs.core.hero.put_in_hand(dirobj_obj, gs)
					gs.core.hero.worn_lst_remove(dirobj_obj)
					gs.io.buffer(f"(Removing the {dirobj_obj.full_name} first)")
					gs.io.buff_s(f"{gs.core.hero.name}_remove_{dirobj_obj.descript_key}")
				return 'prep', [noun_obj, word1, dirobj_obj]
			else:
				if not gs.core.hero.chk_in_hand(noun_obj) and gs.core.hero.chk_in_bkpk(noun_obj):
					gs.core.hero.put_in_hand(noun_obj, gs)
					gs.core.hero.bkpk_lst_remove(noun_obj)
				if not gs.core.hero.chk_in_hand(noun_obj) and gs.core.hero.chk_is_worn(noun_obj):
					gs.core.hero.put_in_hand(noun_obj, gs)
					gs.core.hero.worn_lst_remove(noun_obj)
					gs.io.buffer(f"(Removing the {noun_obj.full_name} first)")
					gs.io.buff_s(f"{gs.core.hero.name}_remove_{noun_obj.descript_key}")
				return 'prep', [dirobj_obj, word1, noun_obj]
