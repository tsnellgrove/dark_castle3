# program: dark castle
# author: Tom Snellgrove
# module description: executes player commands


### import statements ###
import traceback

### execute commands based on case ###
def cmd_execute(gs, case, word_lst):
	try:
		if case == 'help':
			option = word_lst[0]
			if option == 'help':
				output = gs.io.get_str_nr('help')
			elif option in ['basics', 'adjectives', 'prepositions', 'read', 'attack', 'creatures', 'save', 'multiples', 'command-queue', 'inventory']:
				key_str = "help_" + option
				output = gs.io.get_str_nr(key_str)
			elif option == 'verbs':
				output = "Available verbs include: " + ', '.join(sorted(gs.io.get_lst('known_verb_lst','eng')))
			elif option == 'one-word-commands':
				display_one_word_lst = (gs.io.get_lst('one_word_only_lst','eng') + 
						 gs.io.get_lst('pre_interp_word_lst','eng') + 
						 gs.io.get_lst('one_word_convert_lst','eng') + 
						 gs.io.get_lst('one_or_two_word_lst','eng') 
						)
				output = ("Available one word commands include: " + ', '.join(sorted(display_one_word_lst)))
			elif option == 'articles':
				output = ("The following articles are supported but not required: " + ', '.join(gs.io.get_lst('articles_lst','eng')))
			elif  option == 'abbreviations':
				pre_out = "Available abbreviations include: "
				abbrev_dict = gs.io.get_dict('abbreviations_dict','eng')
				for key in abbrev_dict:
					pre_out = pre_out + key + " = " + abbrev_dict[key] + ", "
				output = pre_out[:-2]
			elif option == 'travel':
				output = (gs.io.get_str_nr(f"help_{option}") + ', '.join(gs.io.get_lst('one_word_travel_lst','eng')) + " (e.g. 'go north'). You can also 'climb' up or down a climbable object (e.g. 'climb up tree').")
			elif option == 'debug':
				if not gs.core.is_debug:
					output = gs.io.get_str_nr('help_debug_error')
				else:
					output = gs.io.get_str_nr('help_debug') + ', '.join(gs.io.get_lst('debug_verb_lst','eng'))
			else:
				output = gs.io.get_str_nr('help')
			gs.io.buffer(output)
			return
		if  case == 'tru_1word':
			word1 = word_lst[0]
			if word1 == 'score':
				gs.score.print_score(gs)
				return
			if word1 == 'version':
				gs.io.buffer(f"{gs.io.get_str_nr('game_full_name')} version = {gs.io.get_str_nr('game_version')}")
				gs.io.buffer(f"{gs.io.get_str_nr('engine_name', 'eng')} version = {gs.io.get_str_nr('engine_version', 'eng')}")
				return
			if word1 == 'credits':
				gs.io.buff_e('credits')
				return
			if word1 == 'debug_xyzzy':
				gs.core.is_debug = not gs.core.is_debug
				gs.io.buffer(f"Debug Mode is now set to {str(gs.core.is_debug)}.")
				return
			if word1 == 'rand_mode':
				if not gs.core.is_debug:
					gs.io.buffer("Please start your sentence with a known verb!")
				else:
					gs.io.buffer("The current random mode is: " + str(gs.core.rand_mode))
					gs.io.buffer("The default random mode is 'random'. In 'locked' mode, all random events / responses are fixed. This is useful for testing and debugging. To enter 'locked' mode, start the game with an 'L' or 'l' after the game number at the game menu.")
				return
			gs.io.buff_dbg("[CMD] tru_1word case not found", gs)
			return
		if case == 'go':
			room_obj, word1, word2 = word_lst
			getattr(room_obj, word1)(word2, gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(word1, gs.map.hero_rm.name, None, gs)
			return
		if case == '2word':
			word2_obj, word1 = word_lst
			getattr(word2_obj, word1)(gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(word1, word2_obj.name, None, gs)
			return
		if case == 'prep_no_do':
			word1, prep, noun_obj = word_lst
			getattr(noun_obj, word1)(prep, gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(word1, noun_obj.name, prep, gs)
			return
		if case == 'prep':
			dirobj_obj, word1, noun_obj = word_lst
			getattr(dirobj_obj, word1)(noun_obj, gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(word1, dirobj_obj.name, noun_obj.name, gs)
			return
		gs.io.buff_dbg("[CMD] command case error", gs)
		return
	except:
		gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)
	return
