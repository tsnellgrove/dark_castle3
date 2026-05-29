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
		('inventory',) : {
			'case' : 'action_2word',
			'base_action_lst' : ['examine', 'hero_obj']
		},
		('look',) : {
			'case' : 'action_2word',
			'base_action_lst' : ['examine', 'hero_rm_obj']
		},
		('stand',) : {
			'case' : 'action_2word',
			'base_action_lst' : ['stand', 'hero_obj']
		},
		('jump',) : {
			'case' : 'action_2word',
			'base_action_lst' : ['jump', 'hero_obj']
		},
		('hero_dir',) : {
			'case' : 'action_dir',
			"base_action_lst" : ['go', 'hero_dir', 'hero_rm_obj']
		},
		('go', 'hero_dir') : {
			'case' : 'action_dir',
			'base_action_lst' : ['go', 'hero_dir', 'hero_rm_obj']
		},
		('input_verb', 'input_do_noun') : {
			'case' : 'action_2word',
			'base_action_lst' : ['verb_str', 'do_noun_str']
		},
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
		('infer_verb',) : {
			'case' : 'action_2word',
			'base_action_lst' : ['infer_do_noun']
		},

		('sit', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'in', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'on', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'into', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'down', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'down', 'in', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'down', 'on', 'input_do_noun') : ['sit', 'do_noun_str'],
		('sit', 'down', 'into', 'input_do_noun') : ['sit', 'do_noun_str'],

	}
	try:
		base_action_lst = syntax_dict[user_input_tpl]
	except:
		return 'error', ["What??"]
	if isinstance(base_action_lst, list):
		case = 'universal'
	else:
		base_action_lst = syntax_dict[user_input_tpl]['base_action_lst']
		case = syntax_dict[user_input_tpl]['case']
	action_lst = base_action_lst.copy()
##	print(f"base_action_lst: {base_action_lst}")
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
			if input_verb in ['exit'] and gs.core.hero.is_contained(gs):
				gs.io.buffer(f"(from the {gs.core.hero.get_contained_by(gs).full_name})")
				action_lst = [input_verb, gs.core.hero.get_contained_by(gs)]
				break
			elif input_verb in ['drop', 'stow', 'eat', 'wear'] and not gs.core.hero.hand_is_empty():
				gs.io.buffer(f"(the {gs.core.hero.get_hand_item().full_name})")
				action_lst = [input_verb, gs.core.hero.get_hand_item()]
				break
			elif input_verb in ['climb']:
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
##	print(f"action_lst: {action_lst}")
	return case, action_lst


### unified infer do_noun function for all verbs ###
def infer_do_noun(gs, verb_str):
	scope_lst = gs.map.hero_rm.get_vis_contain_lst(gs)
	do_noun_count = 0
	do_noun_obj = None
	if verb_str == 'sit':
		err_txt = "Where do you want to sit?"
		for obj in scope_lst:
			if obj.is_seat():
				do_noun_count += 1
				do_noun_obj = obj
				infer_txt = f"(in the {do_noun_obj.full_name})"
	if do_noun_count == 1:
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
		if word in ['hero_obj', 'hero_rm_obj', 'hero_dir', 'verb_str', 'do_noun_str', 'up_or_down_dir']: # reserved syntax
			return 'error', [f"What??"]
	# one-word commands where user_input_lst is longer than one word
	if len(user_input_lst) > 1 and user_input_lst[0] in (
			gs.io.get_lst('pre_interp_word_lst','eng') + 
			gs.io.get_lst('one_word_only_lst','eng') + 
			gs.io.get_lst('one_word_secret_lst','eng') +
			gs.io.get_lst('one_word_convert_lst','eng') + # added
			gs.io.get_lst('one_word_travel_lst','eng') # added
			):
		return 'error', [f"There are too many words in that sentence. '{user_input_lst[0].capitalize()}' is a one word command!"]
	if len(user_input_lst) > 2 and user_input_lst[0] in ['help', 'go']:
		return 'error', [f"Can you state that more simply? {gs.core.hero.full_name} is a person of few words!"]

	# *** global variable assignment ***
	word1 = user_input_lst[0]
	creature = gs.core.hero
	meta_cmd_lst = gs.io.get_lst('one_word_only_lst','eng') + gs.io.get_lst('one_word_secret_lst','eng')
	full_verbs_lst = (
			gs.io.get_lst('known_verb_lst','eng') + 
			gs.io.get_lst('debug_verb_lst','eng') +
			gs.io.get_lst('non-action_verb_list','eng')
			)
	case = None
	action_lst = None

	# *** one-word and meta commands ***
	if len(user_input_lst) == 1 and word1 in gs.io.get_lst('one_word_travel_lst','eng'):
		case, action_lst = syntax(('hero_dir',), None, None, word1, None, gs)
	elif word1 in gs.io.get_lst('one_word_convert_lst','eng'): # e.g. inventory, look, stand, jump
		case, action_lst = syntax(tuple(user_input_lst), word1, None, None, None, gs)
	elif word1 in meta_cmd_lst: # e.g. credits, score, version, verbose, brief, superbrief
		case, action_lst = syntax(('meta_cmd',), word1, None, None, None, gs)
	elif word1 in ['help']:
		if len(user_input_lst) == 1:
			option = 'menu'
		else:
			option = user_input_lst[1]
		case, action_lst = syntax(('help', 'option'), word1, None, option, None, gs)


	# handle sit commands - special case because includes prep
	elif word1 in ['sit']:
		if word1 not in full_verbs_lst:
			return 'error', ["Please start your sentence with a known verb!"]
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
		for index, word in enumerate(user_input_lst): # new
			if word in full_verbs_lst:
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
			return 'error', ['I don\'t see a verb in that sentence!']
		elif (verb_count > 1): # e.g. 'help attack' already dealt with in one-word command processing
			return 'error', ['I see more than one verb in that sentence!']
		if do_noun_count > 0:
			do_noun_cmd_lst.insert(0, 'blank') # temporary placeholder for verb in noun_handling call
			error_state, error_msg, do_noun_obj = noun_handling(master_obj_lst, do_noun_cmd_lst) # in future, pass without verb and prep
			if error_state:
				return 'error', [error_msg]
			else: # if no error, assign do_noun_obj.name to do_noun_cmd_lst for syntax call
				do_noun_cmd_lst = [do_noun_obj.name]
		else:
			exactly_one, do_noun_obj, err_txt = infer_do_noun(gs, word1)
			if exactly_one:
				do_noun_cmd_lst = [do_noun_obj.name]
				do_noun_obj = do_noun_obj
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
		user_cmd_lst_raw = verb_cmd_lst + dir_cmd_lst + do_prep_cmd_lst + do_noun_cmd_lst + id_prep_cmd_lst + id_noun_cmd_lst # new
##		print(f"user_cmd_lst_raw: {user_cmd_lst_raw}")
		user_syn_lst = verb_cmd_lst + dir_cmd_lst + do_prep_cmd_lst + ['input_do_noun'] + id_prep_cmd_lst + id_noun_syn_lst # new
##		print(f"user_syn_lst: {user_syn_lst}")
		case, action_lst = syntax(tuple(user_syn_lst), word1, do_noun_obj.name, prep, None, gs)
		return case, action_lst


	elif len(user_input_lst) == 1:
			if word1 in full_verbs_lst:
				case, action_lst = syntax(('infer_verb',), word1, None, None, None, gs)
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

	# handle go commands - special case beacause no do_noun
	if word1 in ['go']:
		case, action_lst = syntax(('go', 'hero_dir'), word1, None, user_input_lst[1], None, gs)
		return case, action_lst

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
	else: # '2word' case
		error_state, error_msg, word2_obj = noun_handling(master_obj_lst, user_input_lst) # pass without verb
		if error_state:
			return 'error', [error_msg]
		else:
			creature = gs.core.hero
			if word1 in ['drop', 'wear', 'eat'] and not creature.chk_in_hand(word2_obj) and gs.core.hero.chk_in_bkpk(word2_obj):
				gs.core.hero.put_in_hand(word2_obj, gs)
				gs.core.hero.bkpk_lst_remove(word2_obj)
			if word1 in ['drop', 'stow', 'eat'] and not creature.chk_in_hand(word2_obj) and gs.core.hero.chk_is_worn(word2_obj):
				gs.core.hero.put_in_hand(word2_obj, gs)
				gs.core.hero.worn_lst_remove(word2_obj)
				gs.io.buffer(f"(Removing the {word2_obj.full_name} first)")
				gs.io.buff_s(f"{gs.core.hero.name}_remove_{word2_obj.descript_key}")
			case, action_lst = syntax(('input_verb', 'input_do_noun'), word1, word2_obj.name, None, None, gs)
			return case, action_lst
