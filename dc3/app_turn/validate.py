# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: module to validate user_input


### import statements ###
import traceback

def validate(gs, case, word_lst):
	"""Validates user_input.
	"""
	# *** interpreter errors ***
	if case == 'error':
		output = word_lst[0]
		if gs.is_debug:
			gs.io.buffer(f"[INTERP] {output}")
		else:
			gs.io.buffer(f"{output}")
		return False

	# *** command errors ***
	if case in ['2word', 'prep', 'go']:
		try:
			if case == '2word':
				word2_obj, word1 = word_lst
				cmd_error = getattr(word2_obj, word1 + '_err')(gs)
			elif case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				cmd_error = getattr(dirobj_obj, word1 + '_err')(noun_obj, gs)
			elif case == 'go':
				room_obj, word1, word2 = word_lst
				cmd_error = getattr(room_obj, word1 + '_err')(word2, gs)
			if cmd_error and gs.is_debug:
				gs.io.buff_no_cr("[INVIS error postfix]")
		except:
			cmd_error = True
			gs.io.buff_dbg("[VAL] " + traceback.format_exc(), gs)
		return not cmd_error
	return True

