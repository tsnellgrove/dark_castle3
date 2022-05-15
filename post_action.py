# program: dark castle v3.59
# name: Tom Snellgrove
# date: Feb 9, 2021
# description: identifies and executes pre-action commands


### import statements ###

def post_action(active_gs, case, word_lst):
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
				if obj.trigger_type == 'post_act_switch':
						trig_case = 'switch'
						trig_switch_state_lst = [obj.trig_switch.switch_state]
##						trig_switch_state_lst = []    # retain in case switch_state becomes multi-value in the future
##						trig_switch_state_lst.append(obj.trig_switch.switch_state)
						if obj.trig_check(active_gs, trig_case, trig_switch_state_lst):
								local_override = obj.run_mach(active_gs)

				if obj.trigger_type == 'post_act_cmd':
						if obj.trig_check(active_gs, case, word_lst):
								local_override = obj.run_mach(active_gs)
								if local_override:
										cmd_override = True
