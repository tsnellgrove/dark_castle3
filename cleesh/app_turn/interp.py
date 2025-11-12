# program: dark castle
# author: Tom Snellgrove
# module description: converts player input into game commands


### import statements
from itertools import islice


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

### input_cleanup - convert user_input str to lst, lower, convert abbreviations, remove articles
def input_cleanup(gs, user_input):
	# first, convert user input string into word list
	lst = []
	lst.append(user_input)
	user_input_lst = lst[0].split()
	# next, convert all words to lower case and substitute abbreviations
	n = 0 
	for word in user_input_lst:
		word = word.lower()
		abbrev_dict = gs.io.get_dict('abbreviations_dict','eng')
		if word in abbrev_dict:
			word = abbrev_dict[word]
		user_input_lst[n] = word
		n += 1
	# finally, strip out articles
	for article in gs.io.get_lst('articles_lst','eng'):
		user_input_lst = [word for word in user_input_lst if word != article]
	return user_input_lst

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
	gs = master_obj_lst[0]
	creature = gs.core.hero
	user_input_lst = input_cleanup(gs, user_input)
	full_verbs_lst = gs.io.get_lst('known_verb_lst','eng') + gs.io.get_lst('debug_verb_lst','eng')
	tru_1word_lst = gs.io.get_lst('one_word_only_lst','eng') + gs.io.get_lst('one_word_secret_lst','eng')

	# error if no input or the only input is articles 
	if len(user_input_lst) < 1:
		return 'error', ["I have no idea what you're talking about!"]

	# len(user_input_lst) is not < 1 so user_input_lst must have at least one word in it
	word1 = user_input_lst[0]

	# handle true one-word commands
	if len(user_input_lst) == 1 and word1 == 'help':
		return 'help', [word1]
	if len(user_input_lst) == 1 and word1 in tru_1word_lst:
		return 'tru_1word', [word1]
	one_word_max_lst = (gs.io.get_lst('one_word_only_lst','eng') + 
						 gs.io.get_lst('pre_interp_word_lst','eng') + 
						 gs.io.get_lst('one_word_convert_lst','eng') + 
						 gs.io.get_lst('one_word_secret_lst','eng') 
						)
	if word1 in one_word_max_lst and len(user_input_lst) > 1:
		return 'error', [f"There are too many words in that sentence. '{word1}' is a one word command!"]

	# convert one-word commands that are implicit two-word commands 
	full_one_word_lst = gs.io.get_lst('one_word_convert_lst','eng') + gs.io.get_lst('one_word_travel_lst','eng')
	if len(user_input_lst) == 1 and word1 in full_one_word_lst:
#		if word1 in ['north', 'south', 'east', 'west']:
		if word1 in gs.io.get_lst('one_word_travel_lst','eng'):
			user_input_lst.append(word1)
			user_input_lst[0] = 'go'
		if word1 == 'inventory':
			user_input_lst[0] = 'examine'
			user_input_lst.append(gs.core.hero.name)
		if word1 == 'look':
			user_input_lst[0] = 'examine'
			user_input_lst.append(gs.map.hero_rm.name)
		if word1 == 'stand':
			user_input_lst.append(creature.name)
		if word1 == 'jump':
			user_input_lst.append(creature.name)
		word1 = user_input_lst[0]

	# convert one-word commands that are assumed-noun two-word commands
	if len(user_input_lst) == 1 and word1 in gs.io.get_lst('assumed_noun_2word_lst','eng'):
		if word1 in ['exit']:
			if creature.is_contained(gs):
				user_input_lst.append(creature.get_contained_by(gs).name)
		elif not creature.hand_is_empty():
			user_input_lst.append(creature.get_hand_item().name)
			gs.io.buffer(f"(the {creature.get_hand_item().full_name})")

	# if not a known true or convertable one-word command, must be an error
	if len(user_input_lst) == 1:
		if word1 in full_verbs_lst:
			error_msg = word1 + " what?"
		else:
			error_msg = "What??"
		return 'error', [error_msg]

	# all commands longer than one word should start with a verb
	if word1 not in full_verbs_lst:
		return 'error', ["Please start your sentence with a known verb!"]

#	# handle prep_no_do verb commands (special cases first else general case)
#	if word1 in gs.io.get_lst('prep_no_do_verb_lst','eng'):
#		if word1 in ['climb']:
#			word2_txt = user_input_lst[1]
#			if 'up' in user_input_lst:
#				prep = 'up'
#			elif 'down' in user_input_lst:
#				prep = 'down'
#			elif len(user_input_lst) == 2 and gs.core.is_key_in_sto_dict(word2_txt) and gs.core.get_str_to_obj_dict(word2_txt).is_climbable():
#				room = gs.map.hero_rm
#				word2_obj = gs.core.get_str_to_obj_dict(word2_txt)
#				if room == word2_obj.bottom_rm:
#					prep = 'up'
#				elif room == word2_obj.top_rm:
#					prep = 'down'
#				user_input_lst.insert(1, prep)
#				gs.io.buffer(f"(you clamber {prep})")
#			else:
#				prep = 'up or down'
#		if prep not in user_input_lst:
#			error_msg = f"I don't see the word '{prep}' in that sentence."
#			return 'error', [error_msg]
#		if len(user_input_lst) < 3:
#			error_msg = "That sentence doesn't appear to be complete"
#			return 'error', [error_msg]
#		else:
#			in_position = user_input_lst.index(prep)
#			v_n_lst = list(islice(user_input_lst, in_position))
#			noun_error_state, noun_error_msg, noun_obj = noun_handling(master_obj_lst, v_n_lst)
#			if noun_error_state:
#				return 'error', [noun_error_msg]
#			return 'prep', [word1, prep, noun_obj]

	# handle prep verb commands (special cases first else general case)
	if word1 == 'help':
		word2 = user_input_lst[1]
		return 'help', [word2]
	elif word1 == 'go':
		word2 = user_input_lst[1]
		return 'go', [gs.map.hero_rm, word1, word2]
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
#		if (word1 in ['climb'] and len(user_input_lst) < 3) or len(user_input_lst) < 4:
			error_msg = "That sentence doesn't appear to be complete"
			return 'error', [error_msg]
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
			if word1 in ['drop', 'wear', 'eat'] and not creature.chk_in_hand(word2_obj) and gs.core.hero.chk_in_bkpk(word2_obj):
				gs.core.hero.put_in_hand(word2_obj, gs)
				gs.core.hero.bkpk_lst_remove(word2_obj)
			if word1 in ['drop', 'stow', 'eat'] and not creature.chk_in_hand(word2_obj) and gs.core.hero.chk_is_worn(word2_obj):
				gs.core.hero.put_in_hand(word2_obj, gs)
				gs.core.hero.worn_lst_remove(word2_obj)
				gs.io.buffer(f"(Removing the {word2_obj.full_name} first)")
				gs.io.buff_s(f"{gs.core.hero.name}_remove_{word2_obj.descript_key}")
			return '2word', [word2_obj, word1]
