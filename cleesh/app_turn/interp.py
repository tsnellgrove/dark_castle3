# program: dark castle
# author: Tom Snellgrove
# module description: converts player input into game commands


### import statements
from itertools import islice


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
def syntax(user_input_tpl, input_dir, verb_action, do_noun, gs):

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
		}
	}
	base_action_lst = syntax_dict[user_input_tpl]['base_action_lst']
	action_lst = base_action_lst.copy()
##	print(f"base_action_lst: {base_action_lst}")
	for index, word in enumerate(base_action_lst):
		if word == 'hero_obj':
			action_lst[index] = gs.core.hero # convert class noun to object
		if word == 'hero_rm_obj':
			action_lst[index] = gs.map.hero_rm # convert class noun to object
		if word == 'hero_dir':
			action_lst[index] = input_dir # string
		if word == 'verb_str':
			action_lst[index] = verb_action # string
		if word == 'do_noun_str':
			action_lst[index] = gs.core.get_str_to_obj_dict(do_noun) # convert to obj
##	print(f"action_lst: {action_lst}")
	return syntax_dict[user_input_tpl]['case'], action_lst


### root_word_count - determines if user command contains root words
def root_word_count(gs, word2_txt):
	scope_lst = gs.map.hero_rm.get_vis_contain_lst(gs)
	root_count = 0
	obj_name = ""
	for obj in scope_lst:
		if obj.root_name == word2_txt:
			root_count += 1
			obj_name = obj.name
		if obj.has_writing():
			if obj.writing.root_name == word2_txt:
				root_count += 1
				obj_name = obj.writing.name
	return root_count, obj_name


### handle nouns and adjectives
def noun_handling(master_obj_lst, user_input_lst):
	gs = master_obj_lst[0]
	error_state = False
	error_msg = ""
	word2_obj = ""
	word2_txt = user_input_lst[1]

	# convert 3-word verb-adj-noun commands into verb-obj_name commands
	if len(user_input_lst) == 3:
		word3_txt = user_input_lst[2]
		user_input_lst[1] = word2_txt + "_" + word3_txt
		word2_txt = user_input_lst[1]
		del user_input_lst[2]

	# error out commands that are still longer than two words
	if len(user_input_lst) > 2:
		error_msg = f"Can you state that more simply? {gs.core.hero.full_name} is a person of few words!"
		error_state = True
		return error_state, error_msg, word2_obj

	# check to see if word2 is a known obj_name
	word2_txt_known = False
	if gs.core.is_key_in_sto_dict(word2_txt):
		word2_txt_known = True
		word2_obj = gs.core.get_str_to_obj_dict(word2_txt)

	# check to see if the word2 is a root_name; convert to obj_name if valid
	if not word2_txt_known:
		root_count, obj_name = root_word_count(gs, word2_txt)
		if root_count < 1:
			error_msg = "I don't see a " + word2_txt.capitalize() + " here."
			error_state = True
			return error_state, error_msg, word2_obj
		elif root_count > 1:
			error_msg = "I see more than one " + word2_txt + ". Please use the full name."
			error_state = True
			return error_state, error_msg, word2_obj
		else:
			if gs.core.is_key_in_sto_dict(obj_name):
				word2_obj = gs.core.get_str_to_obj_dict(obj_name)
	return error_state, error_msg, word2_obj


### interpreter - determine user intent
def interpreter(user_input, master_obj_lst):

	# *** user_input to cleaned-up user_input_lst conversion ***
	gs = master_obj_lst[0]
	user_input_lst = input_cleanup(gs, user_input)
#	if len(user_input_lst) > 0:
#		word1 = user_input_lst[0]

	# *** initial error checking ***
	if len(user_input_lst) < 1: # error if no input or the only input is articles 
		return 'error', ["I have no idea what you're talking about!"]
	for word in user_input_lst:
		if word in ['hero_obj', 'hero_rm_obj', 'hero_dir', 'verb_str', 'do_noun_str']: # reserved syntax
			return 'error', [f"What??"]

	# *** global variable assignment ***
	word1 = user_input_lst[0]
	creature = gs.core.hero
	full_verbs_lst = gs.io.get_lst('known_verb_lst','eng') + gs.io.get_lst('debug_verb_lst','eng')

	# *** special case of help commands ***
	if word1 == 'help':
		if len(user_input_lst) == 1:
			option = 'menu'
		else:
			option = user_input_lst[1]
		return 'help', [option]
	
	# *** process actual one-word commands ***
	if len(user_input_lst) == 1 and word1 in (
			gs.io.get_lst('one_word_only_lst','eng') + 
			gs.io.get_lst('one_word_secret_lst','eng')
			):
		return 'tru_1word', [word1]	
	if len(user_input_lst) == 1 and word1 in gs.io.get_lst('one_word_convert_lst','eng'):
		case, action_lst = syntax(tuple(user_input_lst), None, None, None, gs)
		return case, action_lst
	if len(user_input_lst) == 1 and word1 in gs.io.get_lst('one_word_travel_lst','eng'):
		case, action_lst = syntax(('hero_dir',), word1, None, None, gs) 
		return case, action_lst

	# for two-word commands where only the verb is given, if the noun is assumable, assign it
#	if len(user_input_lst) == 1 and word1 in gs.io.get_lst('assumed_noun_2word_lst','eng'):
#		creature = gs.core.hero
#		if word1 in ['exit'] and creature.is_contained(gs):
#			case, action_lst = syntax(('input_verb', 'input_do_noun'), None, word1, creature.get_contained_by(gs).name, gs)
#			gs.io.buffer(f"(from the {creature.get_contained_by(gs).full_name})")
#		elif word1 not in ['exit'] and not creature.hand_is_empty():
#			case, action_lst = syntax(('input_verb', 'input_do_noun'), None, word1, creature.get_hand_item().name, gs)
#			gs.io.buffer(f"(the {creature.get_hand_item().full_name})")
#		else:
#			case = 'error' # review
#			action_lst = [f"{word1.capitalize()} what?"]
#		return case, action_lst

	# for two-word commands where only the verb is given, if the noun is assumable, assign it
#	creature = gs.core.hero
	if len(user_input_lst) == 1 and word1 in ['exit'] and creature.is_contained(gs):
		case, action_lst = syntax(('input_verb', 'input_do_noun'), None, word1, creature.get_contained_by(gs).name, gs)
		gs.io.buffer(f"(from the {creature.get_contained_by(gs).full_name})")
		return case, action_lst
	if len(user_input_lst) == 1 and word1 in ['drop', 'stow', 'eat', 'wear'] and not creature.hand_is_empty():
		case, action_lst = syntax(('input_verb', 'input_do_noun'), None, word1, creature.get_hand_item().name, gs)
		gs.io.buffer(f"(the {creature.get_hand_item().full_name})")
		return case, action_lst
	
	# exit error case 1: one-word commands where user_input_lst is longer than one word
	if len(user_input_lst) > 1 and word1 in (
			gs.io.get_lst('one_word_only_lst','eng') + 
			gs.io.get_lst('pre_interp_word_lst','eng') + 
			gs.io.get_lst('one_word_secret_lst','eng') +
			gs.io.get_lst('one_word_convert_lst','eng') # added
			):
		return 'error', [f"There are too many words in that sentence. '{word1}' is a one word command!"]

	# variable assignment
#	full_verbs_lst = gs.io.get_lst('known_verb_lst','eng') + gs.io.get_lst('debug_verb_lst','eng')

	# exit error case 2: len(user_input_lst) == 1 but word1 is not known or is a known non-one-word verb
	if len(user_input_lst) == 1:
		if word1 in full_verbs_lst:
			error_msg = word1.capitalize() + " what?"
		else:
			error_msg = "What??"
		return 'error', [error_msg]

	# *** end of one-word command processing ***


	# *** start of multi-word command processing ***

	# initial error case 1: no verbs or more than one verb
	verb_count = 0
	for word in user_input_lst:
		if word in full_verbs_lst:
			verb_count += 1
	if verb_count == 0:
		return 'error', ['I don\'t see a verb in that sentence!']
	elif (verb_count > 1) and (word1 != 'help'): # e.g. 'help attack' is valid
		return 'error', ['I see more than one verb in that sentence!']
		
	# initial error case 2: all commands longer than one word should start with a verb
	if word1 not in full_verbs_lst:
		return 'error', ["Please start your sentence with a known verb!"]

	# handle go commands
	if word1 == 'go':
		if len(user_input_lst) > 2:
			return 'error', [f"Can you state that more simply? {gs.core.hero.full_name} is a person of few words!"]
		else:
			case, action_lst = syntax(('go', 'hero_dir'), user_input_lst[1], None, None, gs)
			return case, action_lst



	# handle prep_no_do verb commands (special cases first else general case) [SYNTAX]
	if word1 in gs.io.get_lst('prep_no_do_verb_lst','eng'):
		if word1 in ['climb']:
			room = gs.map.hero_rm
			if user_input_lst[1] in ['up', 'down']:
				prep = user_input_lst[1]
				user_input_lst.remove(prep)
			elif user_input_lst[1] in ['north', 'south', 'east', 'west', 'northwest', 'northeast', 'southwest', 'southeast']:
				error_msg = f"You can only climb 'up' or 'down'."
				return 'error', [error_msg]
			elif gs.map.chk_valid_dir(room, 'up') and not gs.map.chk_valid_dir(room, 'down'):
				prep = 'up'
				gs.io.buffer(f"(choosing the 'up' direction in which to climb)")
			elif gs.map.chk_valid_dir(room, 'down') and not gs.map.chk_valid_dir(room, 'up'):
				prep = 'down'
				gs.io.buffer(f"(choosing the 'down' direction in which to climb)")
			else:
				return 'error', ["Which way do you want to climb, up or down?"]
			error_state, error_msg, word2_obj = noun_handling(master_obj_lst, user_input_lst)
			if error_state:
				return 'error', [error_msg]
			return 'prep_no_do', [word1, prep, word2_obj]


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
			v_n_lst = list(islice(user_input_lst, in_position))
			p_p_lst = list(islice(user_input_lst, in_position, None))
			noun_error_state, noun_error_msg, noun_obj = noun_handling(master_obj_lst, v_n_lst)
			dir_obj_error_state, dir_obj_error_msg, dirobj_obj = noun_handling(master_obj_lst, p_p_lst)
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
		error_state, error_msg, word2_obj = noun_handling(master_obj_lst, user_input_lst)
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
			return '2word', [word2_obj, word1]
