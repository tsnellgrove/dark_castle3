# program: dark castle v3.75
# name: Tom Snellgrove
# date: Dec 23, 2022
# description: identifies and executes pre-action commands


### import statements ###

def auto_action(active_gs):
		mach_obj_lst = active_gs.get_room().get_mach_lst(active_gs)
		for obj in mach_obj_lst:

				if obj.trigger_type == 'auto_switch_reset':
						obj.switch_state = obj.def_switch_state

				elif obj.trigger_type == 'auto_act' and obj.is_timer() and obj.active:
						obj.run_mach(active_gs)

				elif obj.trigger_type == 'auto_act' and not obj.is_timer():
						obj.run_mach(active_gs)
