# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: converts player input into game commands


### import statements
from itertools import islice
from dc3.data.static_gbl import static_dict

### interpreter function language static dictionaries & lists ###
articles_lst = ['a', 'an', 'the']

one_word_only_lst = ['credits', 'score', 'version', 'quit', 'xyzzy42', 'debug_poke53281,0']

one_word_convert_lst = ['north', 'south', 'east', 'west', 'inventory', 'look', 'stand']

known_verbs_lst = ['attack', 'close', 'drink', 'drop', 'eat', 'examine', 'open',
	'give', 'go', 'help', 'lock', 'pull','push', 'put', 'read', 'show', 'take',
	'unlock', 'wear', 'enter', 'exit', 'stand'
] # 'remove' removed

debug_verb_lst = ['get_weight', 'capacity', 'where_is']

full_verbs_lst = known_verbs_lst + debug_verb_lst

abbreviations_dict = {
	'n' : 'north',
	's' : 'south',
	'e' : 'east',
	'w' : 'west',
	'i' : 'inventory',
	'l' : 'look',
	'get' : 'take',
	'x' : 'examine',
	'h' : 'help'
}

### help = print help info
def help(active_gs, option):
	if option == 'basics':
		output = static_dict['help_basics']
	elif option == 'verbs':
		output = "Available verbs include: " + ', '.join(known_verbs_lst)
	elif option == 'one-word-commands':
		display_one_word_lst = one_word_only_lst.copy()
		display_one_word_lst.pop()
		display_one_word_lst.pop()
		display_one_word_lst.extend(['help', 'stand'])
		output = ("Available one word commands include: " + ', '.join(display_one_word_lst))
	elif option == 'articles':
		output = ("The following articles are supported but not required: " + ', '.join(articles_lst))
	elif option == 'adjectives':
		output = static_dict['help_adjectives']
	elif  option == 'abbreviations':
		pre_out = "Available abbreviations include: "
		for key in abbreviations_dict:
			pre_out = pre_out + key + " = " + abbreviations_dict[key] + ", "
		output = pre_out[:-2]
	elif option == 'prepositions':
		output = static_dict['help_prepositions']
	elif option == 'read':
		output = static_dict['help_read']
	elif option == 'attack':
		output = static_dict['help_attack']
	elif option == 'creatures':
		output = static_dict['help_creatures']
	elif option == 'debug':
		if not active_gs.state_dict['debug']:
			output = static_dict['help_debug_error']
		else:
			output = static_dict['help_debug'] + ', '.join(debug_verb_lst)
	else:
		output = static_dict['help']
	active_gs.buffer(output)

### root_word_count - determines if user command contains root words
def root_word_count(active_gs, word2_txt):
	scope_lst = active_gs.get_room().get_vis_contain_lst(active_gs)
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
def input_cleanup(user_input):
	# first, convert user input string into word list
	lst = []
	lst.append(user_input)
	user_input_lst = lst[0].split()
	# next, convert all words to lower case and substitute abbreviations
	n = 0 
	for word in user_input_lst:
		word = word.lower()	
		if word in abbreviations_dict:
			word = abbreviations_dict[word]
		user_input_lst[n] = word
		n += 1
	# finally, strip out articles
	for article in articles_lst:
		user_input_lst = [word for word in user_input_lst if word != article]
	return user_input_lst

### handle nouns and adjectives
def noun_handling(master_obj_lst, user_input_lst):
	active_gs = master_obj_lst[0]
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
		root_count, obj_name = root_word_count(active_gs, word2_txt)
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
	active_gs = master_obj_lst[0]
	room_obj = active_gs.get_room()
	user_input_lst = input_cleanup(user_input)

	# error if no input or the only input is articles 
	if len(user_input_lst) < 1:
		return 'error', ["I have no idea what you're talking about Burt!"]

	# len(user_input_lst) is not < 1 so user_input_lst must have at least one word in it
	word1 = user_input_lst[0]

	# handle true one-word commands
	if len(user_input_lst) == 1 and word1 == 'help':
		active_gs.io.buff_e('help')
		return 'help', [word1]
	if len(user_input_lst) == 1 and word1 in one_word_only_lst:
		return 'tru_1word', [word1]
	if word1 in one_word_only_lst and len(user_input_lst) > 1:
		return 'error', [f"Burt, there are too many words in that sentence. '{word1}' is a one word command!"]

	# convert one-word commands that are implicit two-word commands 
	elif len(user_input_lst) == 1 and word1 in one_word_convert_lst:
		if word1 in ['north', 'south', 'east', 'west']:
			user_input_lst.append(word1)
			user_input_lst[0] = 'go'
		if word1 == 'inventory':
			user_input_lst[0] = 'examine'
			user_input_lst.append(active_gs.hero.name)
		if word1 == 'look':
			user_input_lst[0] = 'examine'
			user_input_lst.append(active_gs.get_room().name)
		if word1 == 'stand':
			user_input_lst.append(active_gs.hero.name)
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
		help(active_gs, word2)
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
			creature = active_gs.hero
			if len(user_input_lst) < 4 and 'with' not in user_input and not creature.hand_is_empty():
				user_input_lst.extend(['with',creature.get_hand_item().name])
				active_gs.buffer(f"(with the {creature.get_hand_item().full_name})")
			prep = 'with'
		elif word1 in ['drink']:
			creature = active_gs.hero
			if len(user_input_lst) < 4 and 'from' not in user_input and not creature.hand_is_empty():
				user_input_lst.extend(['from',creature.get_hand_item().name])
				active_gs.buffer(f"(from the {creature.get_hand_item().full_name})")
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
