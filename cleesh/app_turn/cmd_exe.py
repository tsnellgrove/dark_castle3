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
			elif option in ['basics', 'adjectives', 'prepositions', 'read', 'attack', 'creatures']:
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
				for key in gs.io.get_dict('abbreviations_dict'):
					pre_out = pre_out + key + " = " + gs.io.get_dict_val('abbreviations_dict',key) + ", "
				output = pre_out[:-2]
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
				gs.io.buffer(f"{gs.io.get_str_nr('game_name')} version = {gs.io.get_str_nr('game_version')}")
				gs.io.buffer(f"{gs.io.get_str_nr('engine_name', 'eng')} version = {gs.io.get_str_nr('engine_version', 'eng')}")
				return
			if word1 == 'credits':
				gs.io.buff_e('credits')
				return
			if word1 == 'debug_poke53281,0':
				gs.core.is_debug = not gs.core.is_debug
				gs.io.buffer(f"Debug Mode is now set to {str(gs.core.is_debug)}.")
				return
			gs.io.buff_dbg("[CMD] tru_1word case not found", gs)
			return
		if case == 'go':
			room_obj, word1, word2 = word_lst
			getattr(room_obj, word1)(word2, gs)
			gs.score.disp_score(word1, gs.map.hero_rm.name, None, gs)
			return
		if case == '2word':
			word2_obj, word1 = word_lst
			getattr(word2_obj, word1)(gs)
			gs.score.disp_score(word1, word2_obj.name, None, gs)
			return
		if case == 'prep':
			dirobj_obj, word1, noun_obj = word_lst
			getattr(dirobj_obj, word1)(noun_obj, gs)
			gs.score.disp_score(word1, dirobj_obj.name, noun_obj.name, gs)
			return
		gs.io.buff_dbg("[CMD] command case error", gs)
		return
	except:
		gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)
	return
