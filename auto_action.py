# program: dark castle v3.68
# name: Tom Snellgrove
# date: July 7, 2022
# description: identifies and executes pre-action commands


### import statements ###

def auto_action(active_gs):
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:

				if obj.trigger_type == 'auto_switch_reset':
						if obj.switch_state != obj.def_switch_state:
								obj.switch_state = obj.def_switch_state

				elif obj.trigger_type == 'auto_act' and obj.is_timer() and obj.active:
						obj.run_mach(active_gs)

