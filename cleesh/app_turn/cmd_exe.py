# program: dark castle
# author: Tom Snellgrove
# module description: executes player commands


### import statements ###
import traceback
from cleesh.app_turn.meta_cmd import meta_cmd_exe

### execute commands based on case ###
def cmd_execute(gs, case, word_lst):
	try:
		if case == 'universal':
			if word_lst[-1] in ['meta']:
				meta_cmd_exe(word_lst, gs)
			elif word_lst[-1] in ['verb_do']:
				action_str, do_noun_obj, *_ = word_lst
				getattr(do_noun_obj, action_str)(gs)
				if not gs.end.is_end: # check to avoid double score display on end
					gs.score.disp_score(action_str, do_noun_obj.name, None, gs)
			elif word_lst[-1] in ['verb_prep_do']:
				action_str, prep_str, do_noun_obj, *_ = word_lst
				getattr(do_noun_obj, action_str)(prep_str, gs)
				if not gs.end.is_end: # check to avoid double score display on end
					gs.score.disp_score(action_str, do_noun_obj.name, prep_str, gs)
			return
		if case == 'prep':
			dirobj_obj, word1, noun_obj = word_lst
			getattr(dirobj_obj, word1)(noun_obj, gs)
			if not gs.end.is_end: # check to avoid double score display on end
				gs.score.disp_score(word1, dirobj_obj.name, noun_obj.name, gs)
			return
		gs.io.buff_dbg("[CMD] command case error", gs)
		return
	except:
		gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)
	return
