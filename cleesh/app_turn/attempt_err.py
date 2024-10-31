# program: dark castle
# author: Tom Snellgrove
# module description: module to respond to attemptable errors


### import statements ###
import traceback

def attempt_err(gs, case, word_lst):
    """Responds to attemptable errors.
    """
#	# *** interpreter errors ***
#	if case == 'error':
#		output = word_lst[0]
#		if gs.core.is_debug:
#			gs.io.buffer(f"[INTERP] {output}")
#		else:
#			gs.io.buffer(f"{output}")
#		return False

	# *** attemptable errors ***
    if case in ['2word', 'prep', 'go']:
#        try:
        if case == '2word':
            try:
                word2_obj, word1 = word_lst
                attempt_err = getattr(word2_obj, word1 + '_att')(gs)
            except:
                attempt_err = False
        elif case == 'prep':
            try:
                dirobj_obj, word1, noun_obj = word_lst
                attempt_err = getattr(dirobj_obj, word1 + '_att')(noun_obj, gs)
            except:
                attempt_err = False
        elif case == 'go':
            try:
                room_obj, word1, word2 = word_lst
                attempt_err = getattr(room_obj, word1 + '_att')(word2, gs)
            except:
                attempt_err = False
        if attempt_err and gs.core.is_debug:
            gs.io.buff_no_cr("[INVIS attemptable error postfix]")
#        except:
#            attempt_err = True
#            debug_str = f"[VAL] {traceback.format_exc()}\nDid you possibly forget to add the noun obj to the pickle in game_update() ?"
#            gs.io.buff_dbg(debug_str, gs)
        return attempt_err
    return False

