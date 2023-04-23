# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 20, 2023
# description: module to validate user_input


### import statements ###
import random
from static_gbl import descript_dict, static_dict

def rand_error():
	num = random.randint(0, 4)
	interp_error_key = 'interp_error_' + str(num)
	return descript_dict[interp_error_key]

def validate(active_gs, case, word_lst):
	"""Validates user_input.
	"""

	# *** interpreter errors ***

	if case == 'error':
		output = word_lst[0]
		active_gs.buffer(f"[INTERP] {output}")
		return False

	# *** command errors ***
#	two_word_lst = ['open', 'close', 'drink', 'push', 'enter', 'exit', 'pull']
	prep_word_lst = []
	two_word_lst_2 = ['take', 'drop', 'eat', 'wear', 'read', 'examine']

	if case == '2word':
		word2_obj, word1 = word_lst

#		room = active_gs.get_room() # maybe only need this for case = 'go' ?
#		cmd_error = False # temp; don't think I need this even temporary ?
#		if word1 in two_word_lst: # temp until all 2word cases covered

		if word1 in two_word_lst_2:
#			err_word = word1 + '_err'
			cmd_error = getattr(word2_obj, word1 + '_err')(active_gs)
			return not cmd_error

##		cmd_error = getattr(word2_obj, word1)(active_gs, 'validate') # for troubleshooting
		try:
			cmd_error = getattr(word2_obj, word1)(active_gs, 'validate')
		except:
			cmd_error = True
			active_gs.buffer(rand_error())
		return not cmd_error

	if case == 'prep':
		dirobj_obj, word1, noun_obj = word_lst
		room = active_gs.get_room()

	return True

	"""Brief history of validate():
			Originally, most errors were generated in cmd_exe(). This worked acceptably well right through v3.68 (precedural parity version). However, as coding progressed a couple issues made it clear this was non-ideal:
			
			1) Once timers were introduced, time tracking became important. Previously, errors and time were sort of intended to have a karmic relationship. The turn-counter was incremented for all input and then decremented when it appeared likely that an error was the interpreter's fault. This was inconsistent at best - but, once timers were introduced, it ceased to work at all. We couldn't have the hedgehog eating biscuits on an error turn. The short-term approach was to make Interpreter Errors untimed but Command Errors timed... but a better soluiton was desireable.
			
			2) The bigger problem was the more advanced use of pre_action machines. Machine code is usually triggered by a player command... but what if the command isn't valid? What if user_input == 'get sword' but Burt already has the sword? The upshot was having to put a 2nd set of error checking into Condition methods... which was crazy since error checking was already carefully coded into the verb methods. Clearly a mechanism was needed to validate whether or not a command would be viable *before* it was executed.
			
			For both these reasons, validate() was inserted between interp() and pre_action() during refactoring.
			
	"""
