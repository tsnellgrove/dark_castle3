# program: dark castle v3.49
# name: Tom Snellgrove
# date: Nov 16, 2021
# description: identifies and executes pre-action commands


### import statements ###

def pre_action_cmd(active_gs, case, word_lst):
		cmd_override = False
		inter_obj_lst = active_gs.inter_obj_lst()
		for obj in inter_obj_lst:
				if obj.inter_obj_type == 'pre-action_trig':
						if obj.trig_check(active_gs, case, word_lst):
								obj.trigger(active_gs)
								if obj.cmd_override:
										cmd_override = True
		return cmd_override
	
