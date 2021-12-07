# program: dark castle v3.52
# name: Tom Snellgrove
# date: Nov 30, 2021
# description: identifies and executes pre-action commands


### import statements ###

def pre_action(active_gs, case, word_lst):
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
#		print(mach_obj_lst)
		for obj in mach_obj_lst:
				if obj.machine_type == 'pre_action_cmd_trig':
						if obj.trig_check(active_gs, case, word_lst):
								local_override = obj.trigger(active_gs)
								if local_override:
										cmd_override = True
				if obj.machine_type == 'pre_action_auto_reset':
						obj.switch_state = 'neutral'
#						print(obj.name + " has value " + obj.switch_state)
		return cmd_override

