# program: dark castle
# author: Tom Snellgrove
# module description: executes player commands


### import statements ###
import traceback

### execute commands based on case ###
def cmd_execute(gs, word_lst):
	try:
		if word_lst[-1] in ['verb_do']:
			action_str, do_noun_obj, *_ = word_lst
			getattr(do_noun_obj, action_str)(gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(action_str, do_noun_obj.name, None, gs)
		elif word_lst[-1] in ['verb_prep_do']:
			action_str, prep_str, do_noun_obj, *_ = word_lst
			getattr(do_noun_obj, action_str)(prep_str, gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(action_str, do_noun_obj.name, prep_str, gs)
		elif word_lst[-1] in ['verb_do_prep_id']:
			action_str, do_noun_obj, prep_str, id_noun_obj,  *_  = word_lst
			if action_str in ['put', 'show', 'give']:
				getattr(id_noun_obj, action_str)(do_noun_obj, gs)
				if not gs.end.is_end: # check to avoid double score display on end
					gs.score.disp_score(action_str, do_noun_obj.name, id_noun_obj.name, gs)
			if action_str in ['unlock', 'lock', 'drink', 'attack']:
				getattr(do_noun_obj, action_str)(id_noun_obj, gs)
				if not gs.end.is_end: # check to avoid double score display on end
					gs.score.disp_score(action_str, do_noun_obj.name, id_noun_obj.name, gs)
		return
	except:
		gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)
	return
