# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 20, 2023
# description: executes player commands


### import statements ###
from static_gbl import descript_dict, static_dict

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
			if word1 == 'help':
				active_gs.buffer(descript_dict['help'])
				return
			if word1 == 'credits':
				active_gs.buffer(descript_dict['credits'])
				return
			active_gs.buffer("[CMD] tru_1word case not found")
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
		active_gs.buffer("[CMD] command case error")
		return
	except:
		active_gs.buffer("[CMD] command execute error")
	return
