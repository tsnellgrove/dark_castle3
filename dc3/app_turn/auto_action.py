# program: dark castle v3.83
# name: Tom Snellgrove
# date: Mar 13, 2024
# description: identifies and executes pre-action commands


### import statements ###

def auto_action(gs):
	mach_obj_lst = gs.map.get_hero_rm(gs).get_mach_lst(gs)
	for obj in mach_obj_lst:
		if obj.trigger_type == 'auto_switch_reset':
			obj.switch_state = obj.def_switch_state
		elif obj.trigger_type == 'auto_act' and obj.is_timer() and obj.active:
			_unused1, _unused2 = obj.run_mach(gs)
		elif obj.trigger_type == 'auto_act' and not obj.is_timer():
			_unused1, _unused2 = obj.run_mach(gs)
