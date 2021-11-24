# program: dark castle v3.50
# name: Tom Snellgrove
# date: Nov 20, 2021
# description: identifies and executes pre-action commands


### import statements ###

def pre_action_cmd(active_gs, case, word_lst):
		print("got to pre_action_cmd")
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
				print(obj.name)
				print(obj.machine_type)
				if obj.machine_type == 'pre_action_trig':
						print("machine_type match")
						if obj.trig_check(active_gs, case, word_lst):
								print("trig_check passed")
								local_override = obj.trigger(active_gs)
								print(str(obj))
								print("local_override: " + str(local_override))
								if local_override:
										cmd_override = True
		print("cmd_override: " + str(cmd_override))
		return cmd_override

