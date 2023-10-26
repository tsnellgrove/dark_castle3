# program: dark castle v3.78
# name: Tom Snellgrove
# date: Sept 25, 2023
# description: executes player commands


### import statements ###
import traceback
from dc3.data.static_gbl import descript_dict, static_dict

### execute commands based on case ###
def cmd_execute(active_gs, case, word_lst):
	try:
		if case == 'help':
			return
		if  case == 'tru_1word':
			word1 = word_lst[0]
			if word1 == 'score':
				active_gs.print_score()
				return
			if word1 == 'version':
				active_gs.buffer(static_dict['version'])
				return
			if word1 == 'credits':
				active_gs.buffer(descript_dict['credits'])
				return
			if word1 == 'debug_poke53281,0':
				active_gs.state_dict['debug'] = not active_gs.state_dict['debug']
				active_gs.buffer(f"Debug Mode is now set to {active_gs.state_dict['debug']}.")
				return
			active_gs.buff_debug_err("[CMD] tru_1word case not found")
			return
		if case == 'go':
			room_obj, word1, word2 = word_lst
			getattr(room_obj, word1)(word2, active_gs)
			return
		if case == '2word':
			word2_obj, word1 = word_lst
			getattr(word2_obj, word1)(active_gs)
			return
		if case == 'prep':
			dirobj_obj, word1, noun_obj = word_lst
			getattr(dirobj_obj, word1)(noun_obj, active_gs)
			return
		active_gs.buff_debug_err("[CMD] command case error")
		return
	except:
		active_gs.buff_debug_err("[CMD] " + traceback.format_exc())
	return
