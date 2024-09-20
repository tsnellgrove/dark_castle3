# program: cleesh
# author: Tom Snellgrove
# module description: identifies and executes pre-action commands


### import statements ###

def pre_action(gs, case, word_lst):
	cmd_override = False
	mach_obj_lst = gs.map.hero_rm.get_mach_lst(gs)
	for obj in mach_obj_lst:
		local_override = False
		if obj.trigger_type == 'pre_act_cmd' and obj.has_trigger() and obj.has_cond():
			print(f"machine name = {obj.name}")
			print(f"trig_vals_lst = {obj.trig_vals_lst}")
			print(f"cond_lst = {obj.cond_lst}")
			print(f"result_lst = {obj.result_lst}")
		if obj.trigger_type == 'pre_act_cmd' and obj.is_enabled and obj.trig_check(gs, case, word_lst):
			local_override, _unused = obj.run_mach(gs)
# elim pre_act_timer as a trigger_type ???
		elif obj.trigger_type == 'pre_act_timer' and obj.trig_switch.is_dinging():
			local_override, _unused = obj.run_mach(gs)
		if local_override:
			cmd_override = True # if any local_override == True then cmd_override == True
	return cmd_override


 
