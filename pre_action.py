# program: dark castle v3.60
# name: Tom Snellgrove
# date: Mar 24, 2022
# description: identifies and executes pre-action commands


### import statements ###

def pre_action(active_gs, case, word_lst):
		cmd_override = False
		mach_obj_lst = active_gs.mach_obj_lst()
		for obj in mach_obj_lst:
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

				elif obj.trigger_type == 'pre_act_auto_switch_reset':
						if obj.switch_state != obj.def_switch_state:
								obj.switch_state = obj.def_switch_state
		return cmd_override


 
