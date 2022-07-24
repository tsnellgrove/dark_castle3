# program: dark castle v3.70
# name: Tom Snellgrove
# date: July 24, 2022
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
				active_gs.inventory()
		elif word1 == 'look':
				room_obj.examine(active_gs)
		return

def cmd_execute(active_gs, case, word_lst):
		room_obj = active_gs.get_room()

#		if case == 'help':
#				word2 = word_lst[0] # help() now called from interpreter()
#				help(active_gs, word2) # help() now called from interpreter()
#				pass
		if  case == 'tru_1word':
				word1 = word_lst[0]
				true_one_word(active_gs, word1, room_obj)
		elif case == 'go':
				room_obj, word1, word2 = word_lst
				getattr(room_obj, word1)(word2, active_gs)
		elif case == '2word':
				word2_obj, word1 = word_lst
##						getattr(word2_obj, word1)(active_gs) # for troubleshooting
				try:
						getattr(word2_obj, word1)(active_gs)
				except:
						error_msg = rand_error()
						active_gs.buffer(error_msg)
###							active_gs.buffer("You can't " + word1 + " with the " + word2_obj.full_name + ".") # old error
		elif case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
#				if active_gs.scope_check(noun_obj) == False:
#						active_gs.buffer("You can't see a " + noun_obj.full_name + " here.")
#						return
#				elif active_gs.scope_check(dirobj_obj) == False:
#						active_gs.buffer("You can't see a " + dirobj_obj.full_name + " here.")
#						return
#				elif (word1 in ['put', 'show', 'give']) and (not active_gs.hand_check(noun_obj)):
#						active_gs.buffer("You're not holding the " + noun_obj.full_name + " in your hand.")
#						return
#				else:
				try:
						getattr(dirobj_obj, word1)(noun_obj, active_gs)
				except:
						error_msg = rand_error()
						active_gs.buffer(error_msg)

