# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
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
			active_gs.io.buffer(f"[INTERP] {output}")
		else:
			active_gs.io.buffer(f"{output}")
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
			if cmd_error and active_gs.state_dict['debug']:
				active_gs.buff_no_cr("[INVIS error postfix]")
		except:
			cmd_error = True
			active_gs.buff_debug_err("[VAL] " + traceback.format_exc())
		return not cmd_error
	return True

