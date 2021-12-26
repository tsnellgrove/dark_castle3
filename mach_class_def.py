# program: dark castle v3.54
# name: Tom Snellgrove
# date: Dec 22, 2021
# description: class deffinition module for Machines

### import
from class_def import Invisible

### classes
# class InvisMach(object):
class MachineMixIn(object):
#		def __init__(self, name, trigger_type, machine_state, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
		def __init__(self, trigger_type, machine_state, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
#				self._name = name
				self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
				self._machine_state = machine_state # machine state variable; boolean for simple machines; Int for complex
				self._trig_switch = trig_switch # the switch whose state change can trigger the machine (only one switch per machine)
				self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
				self._cond_swicth_lst = cond_swicth_lst # list of switches associated with the machine with states that contribute to conditions
				self._cond_lst = cond_lst # list of condition obj to test for; should cover all trigger cases
				self._result_lst = result_lst # list of possible result obj ordered by assciated condition

#		@property
#		def name(self):
#				return self._name

		@property
		def trigger_type(self):
				return self._trigger_type

		@property
		def machine_state(self):
				return self._machine_state

		@machine_state.setter
		def machine_state(self, new_state):
				self._machine_state = new_state

		@property
		def trig_switch(self):
				return self._trig_switch

		@property
		def trig_vals_lst(self):
				return self._trig_vals_lst

		@property
		def cond_swicth_lst(self):
				return self._cond_swicth_lst

		@property
		def cond_lst(self):
				return self._cond_lst

		@property
		def result_lst(self):
				return self._result_lst

#		def __repr__(self):
#				return f'Object { self.name } is of class { type(self).__name__ } '

		# formats trigger state into trig_key_lst based on case and returns true if trig_key_lst is in trig_vals_lst
		def trig_check(self, active_gs, case, word_lst):
				trig_key_lst = 'not_valid'
				if case == 'go':
						trig_key_lst = [word_lst[1], word_lst[2]]
				elif case == '2word':
						trig_key_lst = [word_lst[1], word_lst[0].name]
				elif  case == 'tru_1word':
						trig_key_lst = word_lst
				elif  case == 'put':
						trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
				elif case == 'switch':
						trig_key_lst = word_lst[0]
				return trig_key_lst in self.trig_vals_lst

		def trigger(self, active_gs):
				cond_return_lst = []
				for cond in self.cond_lst:
						cond_return = cond.cond_check(active_gs, self.machine_state, self.cond_swicth_lst)
						cond_return_lst.append(cond_return)
				result_num = cond_return_lst.index(True)
				result = self.result_lst[result_num]
				temp_machine_state, cmd_override = result.results_exe(active_gs, self.machine_state)
				self.machine_state = temp_machine_state
				return cmd_override

class InvisMach(Invisible, MachineMixIn):
		def __init__(self, name, trigger_type, machine_state, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
				Invisible.__init__(self, name)
				MachineMixIn.__init__(self, trigger_type, machine_state, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst)


