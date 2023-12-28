# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: converts player input into game commands


### import statements
from itertools import islice

### interpreter function language static dictionaries & lists ###
# one_word_convert_lst = ['north', 'south', 'east', 'west', 'inventory', 'look', 'stand']

### help = print help info
def help(gs, option):
	if option == 'basics':
		output = gs.io.get_str_nr('help_basics')
	elif option == 'verbs':
		output = "Available verbs include: " + ', '.join(gs.io.get_lst('known_verb_lst'))
	elif option == 'one-word-commands':
		display_one_word_lst = gs.io.get_lst('one_word_only_lst').copy()
		display_one_word_lst.pop()
		display_one_word_lst.pop()
		display_one_word_lst.extend(['again', 'help', 'quit', 'stand'])
		output = ("Available one word commands include: " + ', '.join(sorted(display_one_word_lst)))
	elif option == 'articles':
		output = ("The following articles are supported but not required: " + ', '.join(gs.io.get_lst('articles_lst')))
	elif option == 'adjectives':
		output = gs.io.get_str_nr('help_adjectives')
	elif  option == 'abbreviations':
		pre_out = "Available abbreviations include: "
		for key in gs.io.get_dict('abbreviations_dict'):
			pre_out = pre_out + key + " = " + gs.io.get_dict_val('abbreviations_dict',key) + ", "
		output = pre_out[:-2]
	elif option == 'prepositions':
		output = gs.io.get_str_nr('help_prepositions')
	elif option == 'read':
		output = gs.io.get_str_nr('help_read')
	elif option == 'attack':
		output = gs.io.get_str_nr('help_attack')
	elif option == 'creatures':
		output = gs.io.get_str_nr('help_creatures')
	elif option == 'debug':
		if not gs.state_dict['debug']:
			output = gs.io.get_str_nr('help_debug_error')
		else:
			output = gs.io.get_str_nr('help_debug') + ', '.join(gs.io.get_lst('debug_verb_lst'))
	else:
		output = gs.io.get_str_nr('help')
	gs.io.buffer(output)

### root_word_count - determines if user command contains root words
def root_word_count(gs, word2_txt):
	scope_lst = gs.map.get_hero_rm(gs).get_vis_contain_lst(gs)
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
		if word in gs.io.get_dict('abbreviations_dict'):
			word = gs.io.get_dict_val('abbreviations_dict',word)
		user_input_lst[n] = word
		n += 1
	# finally, strip out articles
	for article in gs.io.get_lst('articles_lst'):
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
		error_msg = "Can you state that more simply? Burt's a man of few words!"
		error_state = True
		return error_state, error_msg, word2_obj

	# check to see if word2 is a known obj_name
	word2_txt_known = False
	for obj in master_obj_lst[1:]:
		if obj.name == word2_txt:
			word2_txt_known = True
			word2_obj = obj

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
			for obj in master_obj_lst[1:]:
				if obj.name == obj_name:
						word2_obj = obj
	return error_state, error_msg, word2_obj

### interpreter - determine user intent
def interpreter(user_input, master_obj_lst):
	gs = master_obj_lst[0]
	room_obj = gs.map.get_hero_rm(gs)
	user_input_lst = input_cleanup(gs, user_input)
	full_verbs_lst = gs.io.get_lst('known_verb_lst') + gs.io.get_lst('debug_verb_lst')

	# error if no input or the only input is articles 
	if len(user_input_lst) < 1:
		return 'error', ["I have no idea what you're talking about Burt!"]

	# len(user_input_lst) is not < 1 so user_input_lst must have at least one word in it
	word1 = user_input_lst[0]

	# handle true one-word commands
	if len(user_input_lst) == 1 and word1 == 'help':
		gs.io.buff_e('help')
		return 'help', [word1]
	if len(user_input_lst) == 1 and word1 in gs.io.get_lst('one_word_only_lst'):
		return 'tru_1word', [word1]
	if word1 in gs.io.get_lst('one_word_only_lst') and len(user_input_lst) > 1:
		return 'error', [f"Burt, there are too many words in that sentence. '{word1}' is a one word command!"]

	# convert one-word commands that are implicit two-word commands 
#	elif len(user_input_lst) == 1 and word1 in one_word_convert_lst:
	elif len(user_input_lst) == 1 and word1 in gs.io.get_lst('one_word_convert_lst'):
		if word1 in ['north', 'south', 'east', 'west']:
			user_input_lst.append(word1)
			user_input_lst[0] = 'go'
		if word1 == 'inventory':
			user_input_lst[0] = 'examine'
			user_input_lst.append(gs.hero.name)
		if word1 == 'look':
			user_input_lst[0] = 'examine'
			user_input_lst.append(gs.map.get_hero_rm(gs).name)
		if word1 == 'stand':
			user_input_lst.append(gs.hero.name)
		word1 = user_input_lst[0]

	# if not a known true or convertable one-word command, must be an error
	elif len(user_input_lst) == 1:
		if word1 in full_verbs_lst:
			error_msg = word1 + " what?"
		else:
			error_msg = "What??"
		return 'error', [error_msg]

	# all commands longer than one word should start with a verb
	if word1 not in full_verbs_lst:
		return 'error', ["Please start your sentence with a known verb!"]

	# handle prep verb commands (special cases first else general case)
	if word1 == 'help':
		word2 = user_input_lst[1]
		help(gs, word2)
		return 'help', [word2]
	elif word1 == 'go':
		word2 = user_input_lst[1]
		return 'go', [room_obj, word1, word2]
	elif word1 in ['put', 'show', 'give', 'attack', 'lock', 'unlock', 'drink']:
		if word1 in ['put']:
			if 'in' in user_input_lst:
				prep = 'in'
			elif 'on' in user_input_lst:
				prep = 'on'
			else:
				prep = 'in or on'
		elif word1 in ['show', 'give']:
			prep = 'to'
		elif word1 in ['attack', 'lock', 'unlock']:
			creature = gs.hero
			if len(user_input_lst) < 4 and 'with' not in user_input and not creature.hand_is_empty():
				user_input_lst.extend(['with',creature.get_hand_item().name])
				gs.io.buffer(f"(with the {creature.get_hand_item().full_name})")
			prep = 'with'
		elif word1 in ['drink']:
			creature = gs.hero
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
				return 'prep', [noun_obj, word1, dirobj_obj]
			else:
				return 'prep', [dirobj_obj, word1, noun_obj]
	else: # '2word' case
		error_state, error_msg, word2_obj = noun_handling(master_obj_lst, user_input_lst)
		if error_state:
			return 'error', [error_msg]
		else:
			return '2word', [word2_obj, word1]
