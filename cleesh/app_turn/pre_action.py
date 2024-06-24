# program: cleesh
# author: Tom Snellgrove
# module description: identifies and executes pre-action commands


### import statements ###

def pre_action(gs, case, word_lst):
	cmd_override = False
	mach_obj_lst = gs.map.hero_rm.get_mach_lst(gs)
	for obj in mach_obj_lst:
		if obj.trigger_type == 'pre_act_cmd' and obj.trig_check(gs, case, word_lst):
			local_override, _unused = obj.run_mach(gs)
			if local_override:
				cmd_override = True # if any local_override == True then cmd_override == True
	
		elif obj.trigger_type == 'pre_act_timer':
			trig_case = 'timer'
			trig_switch_state_lst = [obj.trig_switch.timer_done]
			if obj.trig_check(gs, trig_case, trig_switch_state_lst):
				local_override, _unused = obj.run_mach(gs)

	return cmd_override


 
