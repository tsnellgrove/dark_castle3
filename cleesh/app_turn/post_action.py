# program: clessh
# author: Tom Snellgrove
# module description: identifies and executes pre-action commands


def post_action(gs, case, word_lst):
	mach_obj_lst = gs.map.hero_rm.get_mach_lst(gs)
	for obj in mach_obj_lst:
		if obj.trigger_type == 'post_act_switch':
			trig_case = 'switch'
			trig_switch_state_lst = [obj.trig_switch.switch_state]
			if obj.trig_check(gs, trig_case, trig_switch_state_lst):
				_unused, result_name = obj.run_mach(gs)
				gs.score.disp_score(result_name, obj.name, None, gs)
		if obj.trigger_type == 'post_act_cmd':
			if obj.trig_check(gs, case, word_lst):
				_unused, result_name = obj.run_mach(gs)
				gs.score.disp_score(result_name, obj.name, None, gs)
	return

