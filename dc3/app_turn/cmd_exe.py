# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: executes player commands


### import statements ###
import traceback

### execute commands based on case ###
def cmd_execute(gs, case, word_lst):
	try:
		if case == 'help':
			option = word_lst[0]
			if option == 'help':
				output = gs.io.get_str_nr('help')
			elif option == 'basics':
				output = gs.io.get_str_nr('help_basics')
			elif option == 'adjectives':
				output = gs.io.get_str_nr('help_adjectives')			
			elif option == 'prepositions':
				output = gs.io.get_str_nr('help_prepositions')
			elif option == 'read':
				output = gs.io.get_str_nr('help_read')
			elif option == 'attack':
				output = gs.io.get_str_nr('help_attack')
			elif option == 'creatures':
				output = gs.io.get_str_nr('help_creatures')
			elif option == 'verbs':
				output = "Available verbs include: " + ', '.join(gs.io.get_lst('known_verb_lst'))
			elif option == 'one-word-commands':
				display_one_word_lst = (gs.io.get_lst('one_word_only_lst') + 
						 gs.io.get_lst('pre_interp_word_lst') + 
						 gs.io.get_lst('one_word_convert_lst') + 
						 gs.io.get_lst('one_or_two_word_lst') 
						)
				output = ("Available one word commands include: " + ', '.join(sorted(display_one_word_lst)))
			elif option == 'articles':
				output = ("The following articles are supported but not required: " + ', '.join(gs.io.get_lst('articles_lst')))
			elif  option == 'abbreviations':
				pre_out = "Available abbreviations include: "
				for key in gs.io.get_dict('abbreviations_dict'):
					pre_out = pre_out + key + " = " + gs.io.get_dict_val('abbreviations_dict',key) + ", "
				output = pre_out[:-2]
			elif option == 'debug':
				if not gs.state_dict['debug']:
					output = gs.io.get_str_nr('help_debug_error')
				else:
					output = gs.io.get_str_nr('help_debug') + ', '.join(gs.io.get_lst('debug_verb_lst'))
			else:
				output = gs.io.get_str_nr('help')
			gs.io.buffer(output)
			return
		if  case == 'tru_1word':
			word1 = word_lst[0]
			if word1 == 'score':
				gs.print_score()
				return
			if word1 == 'version':
				gs.io.buff_e('version')
				return
			if word1 == 'credits':
				gs.io.buff_e('credits')
				return
			if word1 == 'debug_poke53281,0':
				gs.state_dict['debug'] = not gs.state_dict['debug']
				gs.io.buffer(f"Debug Mode is now set to {gs.state_dict['debug']}.")
				return
			gs.io.buff_dbg("[CMD] tru_1word case not found", gs)
			return
		if case == 'go':
			room_obj, word1, word2 = word_lst
			getattr(room_obj, word1)(word2, gs)
			return
		if case == '2word':
			word2_obj, word1 = word_lst
			getattr(word2_obj, word1)(gs)
			return
		if case == 'prep':
			dirobj_obj, word1, noun_obj = word_lst
			getattr(dirobj_obj, word1)(noun_obj, gs)
			return
		gs.io.buff_dbg("[CMD] command case error", gs)
		return
	except:
		gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)
	return
