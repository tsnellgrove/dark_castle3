# program: dark castle v3.70
# name: Tom Snellgrove
# date: July 24, 2022
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
				if word1 == 'read' and  active_gs.writing_check(word2_obj) == False: # move to 'read' (see reformulation below) - WAIT method issue!
						if active_gs.scope_check(word2_obj) == False:
								active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
								return False
						else:
								output = "You can't read the " + word2_obj.full_name + ". Try using 'examine' instead."
								active_gs.buffer(output)
								return False

				elif (word1 == 'examine') and (active_gs.writing_check(word2_obj)) == True: # move to 'examine' in ViewOnly - WAIT method issue?
						output = "You can't examine the " + word2_obj.full_name + ". Try using 'read' instead."
						active_gs.buffer(output)
						return False

				elif (word1 != 'read') and (active_gs.scope_check(word2_obj) == False): # universal
						active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
						return False

				elif (word1 == 'take') and (active_gs.scope_check(word2_obj)) and (word2_obj.is_beverage()): # move to 'take' - WAIT method issue
						active_gs.buffer("You can't 'take' a beverage.")
						return False

				elif (word1 in ['drop', 'eat', 'wear']) and (not active_gs.hand_check(word2_obj)): # universal
						active_gs.buffer("You're not holding the " + word2_obj.full_name + " in your hand.")
						return False

#				if word1 == 'read':
#						if active_gs.writing_check(word2_obj) == False and active_gs.scope_check(word2_obj) == False:
#								active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
#								return False
#						if active_gs.writing_check(word2_obj) == False:
#								output = "You can't read the " + word2_obj.full_name + ". Try using 'examine' instead."
#								active_gs.buffer(output)
#								return False
#				else:
#						return True

#				if active_gs.scope_check(word2_obj) == False:
#						active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
#						return False

#				if (word1 in ['drop', 'eat', 'wear']) and (not active_gs.hand_check(word2_obj)):
#						active_gs.buffer("You're not holding the " + word2_obj.full_name + " in your hand.")
#						return False

#				if (word1 == 'examine') and (active_gs.writing_check(word2_obj)) == True:
#						output = "You can't examine the " + word2_obj.full_name + ". Try using 'read' instead."
#						active_gs.buffer(output)
#						return False

#				if (word1 == 'take') and (active_gs.scope_check(word2_obj)) and (word2_obj.is_beverage()):
#						active_gs.buffer("You can't 'take' a beverage.")
#						return False

		if case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				if active_gs.scope_check(noun_obj) == False:
						active_gs.buffer("You can't see a " + noun_obj.full_name + " here.")
						return False
				elif active_gs.scope_check(dirobj_obj) == False:
						active_gs.buffer("You can't see a " + dirobj_obj.full_name + " here.")
						return False
				elif (word1 in ['put', 'show', 'give']) and (not active_gs.hand_check(noun_obj)):
						active_gs.buffer("You're not holding the " + noun_obj.full_name + " in your hand.")
						return False

		return True
