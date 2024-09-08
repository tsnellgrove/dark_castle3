# program: cleesh
# author: Tom Snellgrove
# module description: identifies and executes pre-action commands


### import statements ###

def auto_action(gs):
	mach_obj_lst = gs.map.hero_rm.get_mach_lst(gs)
	for obj in mach_obj_lst:
#		print(f"obj in hero rm: {obj.name}")
#		if obj.is_timer():
#			obj.is_active = False
#			print(f"timer obj is_active state: {str(obj.is_active)}")
		if obj.trigger_type == 'auto_switch_reset':
			obj.switch_state = obj.def_switch_state
#		elif obj.trigger_type == 'auto_act' and obj.is_enabled and (not obj.is_timer() or obj.active):
		elif obj.trigger_type == 'auto_act' and obj.is_enabled and (not obj.is_timer() or obj.is_active):
#			print(f"auto_act obj to be run by run_mach(): {obj.name}")
			_unused1, _unused2 = obj.run_mach(gs)
#		elif obj.trigger_type == 'auto_act' and obj.is_timer() and obj.is_active:
#			_unused1, _unused2 = obj.run_mach(gs)
#		elif obj.trigger_type == 'auto_act' and not obj.is_timer():
#			_unused1, _unused2 = obj.run_mach(gs)
	for obj in mach_obj_lst:
		if obj.trigger_type == 'auto_act_timer' and obj.is_enabled and obj.trig_switch.is_dinging():
			_unused1, _unused2 = obj.run_mach(gs)
	return
