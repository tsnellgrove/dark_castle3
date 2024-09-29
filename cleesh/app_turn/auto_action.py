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
			_unused1, _unused2 = obj.run_mach(gs)
	for obj in mach_obj_lst:
#		if obj.has_switch():
#			print(f"name = {obj.name} and trig_switch = {obj.trig_switch.name}")
#		if obj.trigger_type == 'auto_act_timer' and obj.is_enabled and obj.trig_switch.is_dinging():
##		if obj.trigger_type == 'auto_act_timer':
##			print(f"auto_act_timer mach name = {obj.name} and is_dinging() = {obj.trig_switch.is_dinging()} and is_enabled = {obj.is_enabled}")
		if (obj.trigger_type == 'auto_act_timer' and obj.is_enabled 
				and obj.trig_check(gs, 'timer', [obj.trig_switch.is_dinging()])):
			_unused1, _unused2 = obj.run_mach(gs)
	return

#				- TBD: for trigger_type == 'auto_act_timer' and mach_obj.is_enabled == True:
#					- TBD: from mach_obj.trig_vals_lst, unpack timer_obj (trig_vals_lst[0])
#					- TBD: call timer_obj.trig_check() w/ case = 'timer' ; word_lst = [timer_obj]