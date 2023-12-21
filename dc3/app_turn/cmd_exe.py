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
