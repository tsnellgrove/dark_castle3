# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: identifies and executes pre-action commands


def post_action(gs, case, word_lst):
	cmd_override = False
	mach_obj_lst = gs.get_room().get_mach_lst(gs)
	for obj in mach_obj_lst:
		if obj.trigger_type == 'post_act_switch':
			trig_case = 'switch'
			trig_switch_state_lst = [obj.trig_switch.switch_state]
##			trig_switch_state_lst = []    # retain in case switch_state becomes multi-value in the future
##			trig_switch_state_lst.append(obj.trig_switch.switch_state)
			if obj.trig_check(gs, trig_case, trig_switch_state_lst):
				local_override = obj.run_mach(gs)

		if obj.trigger_type == 'post_act_cmd':
			if obj.trig_check(gs, case, word_lst):
				local_override = obj.run_mach(gs)
	return

