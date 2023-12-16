# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: executes player commands


### import statements ###
import traceback

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
				active_gs.io.buff_e('version')
				return
			if word1 == 'credits':
				active_gs.io.buff_e('credits')
				return
			if word1 == 'debug_poke53281,0':
				active_gs.state_dict['debug'] = not active_gs.state_dict['debug']
				active_gs.io.buffer(f"Debug Mode is now set to {active_gs.state_dict['debug']}.")
				return
#			active_gs.buff_debug_err("[CMD] tru_1word case not found")
			active_gs.io.buff_dbg("[CMD] tru_1word case not found", active_gs.is_dbg())
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
#		active_gs.buff_debug_err("[CMD] command case error")
		active_gs.io.buff_dbg("[CMD] command case error", active_gs.is_dbg())
		return
	except:
#		active_gs.buff_debug_err("[CMD] " + traceback.format_exc())
		active_gs.io.buff_dbg("[CMD] " + traceback.format_exc(), active_gs.is_dbg())
	return
