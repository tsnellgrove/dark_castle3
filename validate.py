# program: dark castle v3.75
# name: Tom Snellgrove
# date: Dec 23, 2022
# description: module to validate user_input


### import statements ###
import random
from static_gbl import descript_dict, static_dict

def rand_error():
		num = random.randint(0, 4)
		interp_error_key = 'interp_error_' + str(num)
		return descript_dict[interp_error_key]

### *** make error dict local?? ***

def validate(active_gs, case, word_lst):
		"""Validates user_input.
		
		Brief history of validate():
				Originally, most errors were generated in cmd_exe(). This worked acceptably well right through v3.68 (precedural parity version). However, as coding progressed a couple issues made it clear this was non-ideal:
				
				1) Once timers were introduced, time tracking became important. Previously, errors and time were sort of intended to have a karmic relationship. The turn-counter was incremented for all input and then decremented when it appeared likely that an error was the interpreter's fault. This was inconsistent at best - but, once timers were introduced, it ceased to work at all. We couldn't have the hedgehog eating biscuits on an error turn. The short-term approach was to make Interpreter Errors untimed but Command Errors timed... but a better soluiton was desireable.
				
				2) The bigger problem was the more advanced use of pre_action machines. Machine code is usually triggered by a player command... but what if the command isn't valid? What if user_input == 'get sword' but Burt already has the sword? The upshot was having to put a 2nd set of error checking into Condition methods... which was crazy since error checking was already carefully coded into the verb methods. Clearly a mechanism was needed to validate whether or not a command would be viable *before* it was executed.
				
				For both these reasons, validate() was inserted between interp() and pre_action() during refactoring.
				
		"""

		# *** interpreter errors ***

		if case == 'error':
				input_valid = False
				if word_lst[0] == "random error":
						output = rand_error()
				else:
						output = word_lst[0]
				active_gs.buffer(output)
				return False

		# *** command errors ***
		if case == '2word':
				word2_obj, word1 = word_lst
				room = active_gs.get_room()

				# *** custom method mis-matches ***
#				if (word1 == 'examine') and (room.chk_wrt_is_vis(word2_obj, active_gs)) == True:
#						output = "You can't examine the " + word2_obj.full_name + ". Try using 'read' instead."
#						active_gs.buffer(output)
#						return False

#				if (word1 == 'take') and (room.chk_is_vis(word2_obj, active_gs)) and (word2_obj.is_liquid()):
#						active_gs.buffer("You can't 'take' a liquid. Try 'drink' instead.")
#						return False

				# *** generic command failure ***
##				exclude_lst_2 = ['read', 'examine', 'take', 'drop', 'open', 'close', 'eat', 'wear', 'drink', 'go', 'push', 'pull', 'enter', 'exit']
##				if word1 not in exclude_lst_2 and word2_obj.is_writing():
##						active_gs.buffer(f"That's X laudably creative but, truth be told, the only thing you can generally do with the {word2_obj.full_name} is to read it.")
##						return False

##				exclude_lst = ['read' 'examine', 'take', 'drop', 'eat', 'wear', 'open', 'close', 'drink', 'go', 'push', 'pull', 'enter', 'exit']
##				if word1 not in exclude_lst and not word2_obj.is_writing() and room.chk_is_vis(word2_obj, active_gs) == False:
#				if word1 != 'read' and not word2_obj.is_writing() and room.chk_is_vis(word2_obj, active_gs) == False:
##						active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
##						return False

##				exclude_lst_3 = ['read', 'examine', 'take', 'drop', 'open', 'close', 'eat', 'wear', 'drink', 'go', 'push', 'pull', 'enter', 'exit']
##				if word1 not in exclude_lst_3 and active_gs.hero.is_contained(active_gs) and word2_obj not in active_gs.hero.get_contained_by(active_gs).get_vis_contain_lst(active_gs) + [room]:
##						active_gs.buffer(f"You'll have to exit the {active_gs.hero.get_contained_by(active_gs).full_name} to attempt that.")
##						return False

#				if (word1 in []) and (not active_gs.hero.chk_in_hand(word2_obj)): # 'drop', 'eat', 'wear' removed
#						active_gs.buffer("You're not holding the " + word2_obj.full_name + " in your hand.")
#						return False

				# *** specific command failures ***

				# *** generic method mis-matches ***

		if case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				room = active_gs.get_room()

				# *** generic command failures ***
#				exclude_lst_prep = ['show', 'lock', 'unlock', 'put', 'give', 'attack']
#				if word1 not in exclude_lst_prep and noun_obj.is_writing():
#						active_gs.buffer(f"That's laudably creative but, truth be told, the only thing you can generally do with the {noun_obj.full_name} is to read it.")
#						return False
#				if word1 not in exclude_lst_prep and dirobj_obj.is_writing():
#						active_gs.buffer(f"That's laudably creative but, truth be told, the only thing you can generally do with the {dirobj_obj.full_name} is to read it.")
#						return False
#				if word1 not in exclude_lst_prep and not noun_obj.is_writing() and room.chk_is_vis(noun_obj, active_gs) == False:
#						active_gs.buffer("You can't see a " + noun_obj.full_name + " here.")
#						return False
#				if word1 not in exclude_lst_prep and not dirobj_obj.is_writing() and room.chk_is_vis(dirobj_obj, active_gs) == False:
#						active_gs.buffer("You can't see a " + dirobj_obj.full_name + " here.")
#						return False
#				if word1 not in exclude_lst_prep and active_gs.hero.is_contained(active_gs) and dirobj_obj not in active_gs.hero.get_contained_by(active_gs).get_vis_contain_lst(active_gs) + [room]:
#						active_gs.buffer(f"You'll have to X exit the {active_gs.hero.get_contained_by(active_gs).full_name} to attempt that.")
#						return False
#				if (word1 in []) and (not active_gs.hero.chk_in_hand(noun_obj)): # 'put', 'show', 'give' removed
#						active_gs.buffer("You're not holding the " + noun_obj.full_name + " in your hand.")
#						return False

		return True
