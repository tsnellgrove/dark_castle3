# program: dark castle v3.75
# name: Tom Snellgrove
# date: Dec 23, 2022
# description: executes player commands


### import statements ###
import random
from static_gbl import descript_dict, static_dict

def rand_error():
		num = random.randint(0, 4)
		interp_error_key = 'interp_error_' + str(num)
		return descript_dict[interp_error_key]

def true_one_word(active_gs, word1, room_obj):
		if word1 == 'score':
				active_gs.print_score()
		elif word1 == 'version':
				active_gs.buffer(static_dict['version'])
		elif word1 == 'help':
				active_gs.buffer(descript_dict['help'])
		elif word1 == 'credits':
				active_gs.buffer(descript_dict['credits'])
		elif word1 == 'inventory':
				active_gs.hero.examine(active_gs)
		elif word1 == 'look':
				room_obj.examine(active_gs)
#		elif word1 == 'exit':
		elif word1 == 'stand':
				active_gs.hero.stand(active_gs)
		return

def cmd_execute(active_gs, case, word_lst):
		room_obj = active_gs.get_room()

		if  case == 'tru_1word':
				word1 = word_lst[0]
				true_one_word(active_gs, word1, room_obj)
		elif case == 'go':
				room_obj, word1, word2 = word_lst
				getattr(room_obj, word1)(word2, active_gs)
		elif case == '2word':
				word2_obj, word1 = word_lst
				getattr(word2_obj, word1)(active_gs) # for troubleshooting
#				try:
#						getattr(word2_obj, word1)(active_gs)
#				except:
#						error_msg = rand_error()
#						active_gs.buffer(error_msg)
###							active_gs.buffer("You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
		elif case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
##				print(f"word1 == {word1}; dirobj_obj == {dirobj_obj}; noun_obj == {noun_obj}")
#				getattr(dirobj_obj, word1)(noun_obj, active_gs) # for troubleshooting
				try:
						getattr(dirobj_obj, word1)(noun_obj, active_gs)
				except:
						error_msg = rand_error()
						active_gs.buffer(error_msg)

