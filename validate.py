# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 20, 2023
# description: module to validate user_input


### import statements ###
import traceback

def validate(active_gs, case, word_lst):
	"""Validates user_input.
	"""
	# *** interpreter errors ***
	if case == 'error':
		output = word_lst[0]
		if active_gs.state_dict['debug']:
			active_gs.buffer(f"[INTERP] {output}")
		else:
			active_gs.buffer(f"{output}")
		return False

	# *** command errors ***
	if case in ['2word', 'prep', 'go']:
		try:
			if case == '2word':
				word2_obj, word1 = word_lst
				cmd_error = getattr(word2_obj, word1 + '_err')(active_gs)
			elif case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				cmd_error = getattr(dirobj_obj, word1 + '_err')(noun_obj, active_gs)
			elif case == 'go':
				room_obj, word1, word2 = word_lst
				cmd_error = getattr(room_obj, word1 + '_err')(word2, active_gs)
		except:
			cmd_error = True
			active_gs.buff_debug_err("[VAL] " + traceback.format_exc())
		return not cmd_error
	return True



	"""Brief history of validate():
			Originally, most errors were generated in cmd_exe(). This worked acceptably well right through v3.68 (precedural parity version). However, as coding progressed a couple issues made it clear this was non-ideal:
			
			1) Once timers were introduced, time tracking became important. Previously, errors and time were sort of intended to have a karmic relationship. The turn-counter was incremented for all input and then decremented when it appeared likely that an error was the interpreter's fault. This was inconsistent at best - but, once timers were introduced, it ceased to work at all. We couldn't have the hedgehog eating biscuits on an error turn. The short-term approach was to make Interpreter Errors untimed but Command Errors timed... but a better soluiton was desireable.
			
			2) The bigger problem was the more advanced use of pre_action machines. Machine code is usually triggered by a player command... but what if the command isn't valid? What if user_input == 'get sword' but Burt already has the sword? The upshot was having to put a 2nd set of error checking into Condition methods... which was crazy since error checking was already carefully coded into the verb error methods. Clearly a mechanism was needed to validate whether or not a command would be viable *before* it was executed.
			
			For both these reasons, validate() was inserted between interp() and pre_action() during refactoring. The idea is that every command is inspected in validate() and, if invalid, an error message is presented, validate() returns False, time is not incremented, and we ask the player for new input. We only ever reach cmd_exe() if validate() returns True.
			
	"""
