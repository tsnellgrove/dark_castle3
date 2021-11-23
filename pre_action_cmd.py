# program: dark castle v3.50
# name: Tom Snellgrove
# date: Nov 20, 2021
# description: identifies and executes pre-action commands


### import statements ###

def pre_action_cmd(active_gs, case, word_lst):
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
				if obj.machine_type == 'pre-action_trig' and obj.trig_check(active_gs, case, word_lst):
						local_override = triger(active_gs)
						if local_override:
								cmd_override = True
		return cmd_override

