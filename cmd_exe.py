# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 20, 2023
# description: executes player commands


### import statements ###
import random
from static_gbl import descript_dict, static_dict


def rand_error():
	num = random.randint(0, 4)
	interp_error_key = 'interp_error_' + str(num)
	return descript_dict[interp_error_key]

def true_one_word(active_gs, word1):
	if word1 == 'score':
		active_gs.print_score()
	elif word1 == 'version':
		active_gs.buffer(static_dict['version'])
	elif word1 == 'help':
		active_gs.buffer(descript_dict['help'])
	elif word1 == 'credits':
		active_gs.buffer(descript_dict['credits'])
	return

#def cmd_execute(active_gs, case, word_lst):
def cmd_execute_old(active_gs, case, word_lst):
	room_obj = active_gs.get_room()

	if  case == 'tru_1word':
		word1 = word_lst[0]
		true_one_word(active_gs, word1)
	elif case == 'go':
		room_obj, word1, word2 = word_lst
##		getattr(room_obj, word1)(word2, active_gs) # for troubleshooting
		try:
			getattr(room_obj, word1)(word2, active_gs)
		except:
			active_gs.buffer(rand_error())
	elif case == '2word':
		word2_obj, word1 = word_lst
##		getattr(word2_obj, word1)(active_gs) # for troubleshooting
		try:
			getattr(word2_obj, word1)(active_gs)
		except:
			active_gs.buffer(rand_error())
###			active_gs.buffer("You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
	elif case == 'prep':
		dirobj_obj, word1, noun_obj = word_lst
##				print(f"word1 == {word1}; dirobj_obj == {dirobj_obj}; noun_obj == {noun_obj}") # troubleshooting
##				getattr(dirobj_obj, word1)(noun_obj, active_gs) # for troubleshooting
		try:
			getattr(dirobj_obj, word1)(noun_obj, active_gs)
		except:
			active_gs.buffer(rand_error())

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
