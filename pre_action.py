# program: dark castle v3.54
# name: Tom Snellgrove
# date: Dec 19, 2021
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
										
##				if obj.trigger_type == 'pre_act_auto':
##								local_override = obj.run_mach(active_gs)
##								if local_override:
##										cmd_override = True
										
				if obj.trigger_type == 'pre_act_auto_switch_reset':
						if obj.switch_state != obj.def_switch_state:
								obj.switch_state = obj.def_switch_state
#						obj.switch_state = 'neutral'
		return cmd_override


 
