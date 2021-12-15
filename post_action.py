# program: dark castle v3.52
# name: Tom Snellgrove
# date: Dec 15, 2021
# description: identifies and executes pre-action commands


### import statements ###

def post_action(active_gs, case, word_lst):
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
				if obj.trigger_type == 'post_act_switch':
						if obj.trig_check(active_gs, 'switch', obj.trig_vals_lst):
								local_override = obj.trigger(active_gs)
#								if local_override:
#										cmd_override = True
#		return cmd_override

