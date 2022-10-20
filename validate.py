# program: dark castle v3.73
# name: Tom Snellgrove
# date: Oct 20, 2022
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
				
				2) The bigger problem was the more advanced use of pre_action machines. Machine code is usually triggered by a player command... but what if the command isn't valid? What if user_input == 'get sword' but Burt already has the sword? The upshot was having to put a 2nd set of error checking into Condition methods... which was crazy since error checking was already carefully coded into the noun class methods. Clearly a mechanism was needed to validate whether or not a command would be viable *before* it was executed.
				
				For both these reasons, validate() was inserted between interp() and pre_action() during refactoring.
				
		Error Types:
				Interpreter Errors: The interpreter is unclear what command the player is trying to issue.
				
				Command Errors: The command is understood but cannot be carried out.
				
				There are 4 flavors of Command Error:
						1) Generic Command Failures: Command failure cases that occur across multiple methods. e.g. very few commands will run if the noun of the command is not in the room's scope. Catching these errors in validate() avoids needing to re-write the same error-checking code repeatedly in multiple methods.
						
						2) Custom Command Failures: Command failure cases specific to a given method. e.g. Burt tries to unlock a container with the wrong key. This is a specific type of error that is best addressed in the unlock() method code itself. The error text is buffered and the fail condition is returned to validate() - which then returns False to app_main() - so that no command is actually run.
						
						3) Generic Method Mis-Match Errors: The player attempts to use a method on an incompatible object. These are usually acts of experimentation or silliness on the player's part. e.g. when Burt tries to 'take castle' no one really expects the command to work. So we throw a random, appropriately snide error.
						
						4) Custom Method Mis-Match Errors: In a few specific cases, player confusion over which methods can be used with which objects is quite justified. e.g. it's not unreasonable for the player to attempt to take the 'water'. In these cases we would like to give an explanitory error - but we can't provide a Custom Method Failure as the method cannot run at all. So, we trap the error in advance in the validate() method so that a helpful response can be given.
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
				if (word1 == 'examine') and (room.chk_wrt_is_vis(word2_obj, active_gs)) == True:
						output = "You can't examine the " + word2_obj.full_name + ". Try using 'read' instead."
						active_gs.buffer(output)
						return False

				if (word1 == 'take') and (room.chk_is_vis(word2_obj, active_gs)) and (word2_obj.is_liquid()):
						active_gs.buffer("You can't 'take' a liquid. Try 'drink' instead.")
						return False

				# *** generic command failure ***
				if word1 != 'read' and room.chk_is_vis(word2_obj, active_gs) == False:
						active_gs.buffer("You can't see a " + word2_obj.full_name + " here.")
						return False

				if (word1 in ['drop', 'eat', 'wear']) and (not active_gs.hero.chk_in_hand(word2_obj)):
						active_gs.buffer("You're not holding the " + word2_obj.full_name + " in your hand.")
						return False

				# *** specific command failures ***

				# *** generic method mis-matches ***

		if case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				room = active_gs.get_room()

				# *** generic command failures ***
				if room.chk_is_vis(noun_obj, active_gs) == False:
						active_gs.buffer("You can't see a " + noun_obj.full_name + " here.")
						return False
				elif room.chk_is_vis(dirobj_obj, active_gs) == False:
						active_gs.buffer("You can't see a " + dirobj_obj.full_name + " here.")
						return False
				elif (word1 in ['put', 'show', 'give']) and (not active_gs.hero.chk_in_hand(noun_obj)):
						active_gs.buffer("You're not holding the " + noun_obj.full_name + " in your hand.")
						return False

		return True
