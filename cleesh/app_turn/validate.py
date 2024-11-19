# program: dark castle
# author: Tom Snellgrove
# module description: module to validate user_input


### import statements ###
import traceback

def validate(gs, case, word_lst):
	"""Validates user_input.
	"""
#	cmd_err = False
	is_att = False
	err_txt= ""

	# *** interpreter errors ***
	if case == 'error':
		output = word_lst[0]
		if gs.core.is_debug:
			gs.io.buffer(f"[INTERP] {output}")
		else:
			gs.io.buffer(f"{output}")
#		return False
		return False, False, ""

	# *** command errors ***
	if case in ['2word', 'prep', 'go']:
		try:
			if case == '2word':
				word2_obj, word1 = word_lst
				cmd_err = getattr(word2_obj, word1 + '_err')(gs)
			elif case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				cmd_err = getattr(dirobj_obj, word1 + '_err')(noun_obj, gs)
			elif case == 'go':
				room_obj, word1, word2 = word_lst
				cmd_err = getattr(room_obj, word1 + '_err')(word2, gs)
			if cmd_err and gs.core.is_debug:
				gs.io.buff_no_cr("[INVIS error postfix]")
		except:
			cmd_err = True
			debug_str = f"[VAL] {traceback.format_exc()}\nDid you possibly forget to add the noun obj to the pickle in game_update() ?"
			gs.io.buff_dbg(debug_str, gs)
		return not cmd_err, is_att, err_txt
#	return True
	return True, None, ""

#	cmd_err, is_att, and err_txt