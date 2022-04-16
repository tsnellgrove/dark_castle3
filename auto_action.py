# program: dark castle v3.60
# name: Tom Snellgrove
# date: Apr 15, 2022
# description: identifies and executes pre-action commands


### import statements ###

#def pre_auto(active_gs, case, word_lst):
def auto_action(active_gs):
#		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
				if obj.trigger_type == 'pre_act_auto':
						if obj.active:
								obj.run_mach(active_gs)
#								local_override = obj.run_mach(active_gs)
#								if local_override:
#										cmd_override = True
