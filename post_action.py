# program: dark castle v3.52
# name: Tom Snellgrove
# date: Dec 15, 2021
# description: identifies and executes pre-action commands


### import statements ###

def post_action(active_gs, case, word_lst):
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		print(mach_obj_lst)
		for obj in mach_obj_lst:
				if obj.trigger_type == 'post_act_switch':
						print(str(obj) + "has trigger type " + obj.trigger_type)
						print(obj.trig_switch.switch_state)
						trig_case = 'switch'

						trig_switch_state_lst = []
#						for switch in obj.trig_switch_lst:
#								trig_switch_state_lst.append(switch.switch_state)

						trig_switch_state_lst.append(obj.trig_switch.switch_state)

#						if obj.trig_check(active_gs, 'switch', obj.trig_vals_lst):
						print(trig_case)
						print(trig_switch_state_lst)
#						if obj.trig_check(active_gs, trig_case, trig_switch_state_lst):
						if obj.trig_check(active_gs, trig_case, trig_switch_state_lst):
								local_override = obj.trigger(active_gs)
#								if local_override:
#										cmd_override = True
#		return cmd_override

