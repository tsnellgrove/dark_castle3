# program: dark castle
# author: Tom Snellgrove
# module description: module to validate user_input


### import statements ###
import traceback

def validate(gs, case, word_lst):
	"""Validates user_input.
	"""
	is_att = False
	err_txt= ""

	# *** interpreter errors ***
	if case == 'error':
		output = word_lst[0]
		if gs.core.is_debug:
			gs.io.buffer(f"[INTERP error] {output}")
		else:
			gs.io.buffer(f"{output}")
		return False, False, ""

	# *** command errors ***
	if case in ['prep', 'action_dir', 'universal']:
		try:
			if case == 'universal':
				if word_lst[-1] in ['verb_do']:
					action_str, do_noun_obj, *_ = word_lst
					cmd_err, is_att, err_txt = getattr(do_noun_obj, action_str + '_err')(gs)
					if (cmd_err and not is_att and err_txt != ""):
						gs.io.buffer(err_txt)
				elif word_lst[-1] in ['verb_prep_do']:
					action_str, prep_str, do_noun_obj,  *_  = word_lst
					cmd_err, is_att, err_txt = getattr(do_noun_obj, action_str + '_err')(prep_str, gs)
					if (cmd_err and not is_att):
						gs.io.buffer(err_txt)
			elif case == 'action_dir':
				action_str, dir_str, do_noun_obj = word_lst
				cmd_err, is_att, err_txt = getattr(do_noun_obj, action_str + '_err')(dir_str, gs)
				if (cmd_err and not is_att):
					gs.io.buffer(err_txt)
			elif case == 'prep':
				dirobj_obj, word1, noun_obj = word_lst
				cmd_err, is_att, err_txt = getattr(dirobj_obj, word1 + '_err')(noun_obj, gs)
				if (cmd_err and not is_att and err_txt != ""):
					gs.io.buffer(err_txt)
			if cmd_err and gs.core.is_debug:
				gs.io.buff_no_cr(" [ERROR error postfix]")
		except:
			cmd_err = True
			debug_str = f" [VALIDATE error] {traceback.format_exc()}\nDid you possibly forget to add the noun obj to the pickle in game_update() ?"
			gs.io.buff_dbg(debug_str, gs)
		return not cmd_err, is_att, err_txt
	return True, None, ""
