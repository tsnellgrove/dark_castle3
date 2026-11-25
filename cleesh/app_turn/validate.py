# program: dark castle
# author: Tom Snellgrove
# module description: module to validate user_input


### import statements ###
import traceback

#def validate(gs, case, word_lst):
def validate(gs, word_lst):
	"""Validates user_input.
	"""
	is_att = False
	err_txt= ""


	# *** command errors ***
	try:
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
		elif word_lst[-1] in ['verb_do_prep_id']:
			action_str, do_noun_obj, prep_str, id_noun_obj,  *_  = word_lst
			if action_str in ['put', 'show', 'give']:
				cmd_err, is_att, err_txt = getattr(id_noun_obj, action_str + '_err')(do_noun_obj, gs)
				if (cmd_err and not is_att):
					gs.io.buffer(err_txt)
			if action_str in ['unlock', 'lock', 'drink', 'attack']:
				cmd_err, is_att, err_txt = getattr(do_noun_obj, action_str + '_err')(id_noun_obj, gs)
				if (cmd_err and not is_att):
					gs.io.buffer(err_txt)
	except:
		cmd_err = True
		debug_str = f" [VALIDATE error] {traceback.format_exc()}\nDid you possibly forget to add the noun obj to the pickle in game_update() ?"
		gs.io.buff_dbg(debug_str, gs)
	return not cmd_err, is_att, err_txt
