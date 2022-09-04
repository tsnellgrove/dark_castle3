# program: dark castle v3.71
# name: Tom Snellgrove
# date: Aug 10, 2022
# description: identifies and executes pre-action commands


### import statements ###

def pre_action(active_gs, case, word_lst):
		cmd_override = False
#		mach_obj_lst = active_gs.mach_obj_lst()
		mach_obj_lst = active_gs.get_room().get_mach_lst(active_gs)
		for obj in mach_obj_lst:
##				print(obj) # for mach troubleshooting

				if obj.trigger_type == 'pre_act_cmd':
						if obj.trig_check(active_gs, case, word_lst):
								local_override = obj.run_mach(active_gs)
								if local_override:
										cmd_override = True

				#	moved to auto_action()
##				elif obj.trigger_type == 'pre_act_auto':
##						if obj.active:
##								local_override = obj.run_mach(active_gs)
##								if local_override:
##										cmd_override = True

				# move to auto_action()
##				elif obj.trigger_type == 'pre_act_auto_switch_reset':
##						if obj.switch_state != obj.def_switch_state:
##								obj.switch_state = obj.def_switch_state

				elif obj.trigger_type == 'pre_act_timer':
						trig_case = 'timer'
						trig_switch_state_lst = [obj.trig_switch.timer_done]
##						trig_switch_state_lst = []    # retain in case switch_state becomes multi-value in the future
##						trig_switch_state_lst.append(obj.trig_switch.switch_state)
						if obj.trig_check(active_gs, trig_case, trig_switch_state_lst):
								local_override = obj.run_mach(active_gs)

		return cmd_override


 
