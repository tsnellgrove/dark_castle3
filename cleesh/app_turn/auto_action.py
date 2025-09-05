# program: cleesh
# author: Tom Snellgrove
# module description: identifies and executes pre-action commands


### import statements ###

def auto_action(gs):
	mach_obj_lst = gs.map.hero_rm.get_mach_lst(gs)
	for obj in mach_obj_lst:
		if obj.trigger_type == 'auto_switch_reset':
			obj.switch_state = obj.def_switch_state
		elif obj.trigger_type == 'auto_act' and obj.is_enabled and (not obj.is_timer() or obj.is_active):
			_unused1, _unused2 = obj.run_mach(gs, True) # is_valid independent / assumed True for auto_act
	for obj in mach_obj_lst:
		if (obj.trigger_type == 'auto_act_timer' and obj.is_enabled 
				and obj.trig_check(gs, 'timer', obj.trig_switch.is_dinging(), True)):
			_unused1, _unused2 = obj.run_mach(gs, True) # is_valid independent / assumed True for auto_act
	return
