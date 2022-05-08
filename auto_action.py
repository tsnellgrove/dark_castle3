# program: dark castle v3.62
# name: Tom Snellgrove
# date: May 8, 2022
# description: identifies and executes pre-action commands


### import statements ###

def auto_action(active_gs):
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
				if obj.trigger_type == 'auto_act' and obj.active:
						obj.run_mach(active_gs)

