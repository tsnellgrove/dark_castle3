# program: dark castle v3.60
# name: Tom Snellgrove
# date: Mar 24, 2022
# description: class deffinition module for Machines

### import
from noun_class_def import Invisible, ViewOnly
from static_gbl import descript_dict

### classes
class MachineMixIn(object):
		def __init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
				self._mach_state = mach_state # machine state variable; boolean for simple machines; Int for complex
				self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
				self._trig_switch = trig_switch # the switch whose state change can trigger the machine (only one switch per machine)
				self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
				self._cond_swicth_lst = cond_swicth_lst # list of switches associated with the machine with states that contribute to conditions
				self._cond_lst = cond_lst # list of condition obj to test for; should cover all trigger cases
				self._result_lst = result_lst # list of possible result obj ordered by assciated condition

		@property
		def mach_state(self):
				return self._mach_state

		@property
		def trigger_type(self):
				return self._trigger_type

		@mach_state.setter
		def mach_state(self, new_state):
				self._mach_state = new_state

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

		def run_mach(self, active_gs):
				cond_return_lst = []
				for cond in self.cond_lst:
						cond_return = cond.cond_check(active_gs, self.mach_state, self.cond_swicth_lst)
						cond_return_lst.append(cond_return)
				result_index = cond_return_lst.index(True)
				result = self.result_lst[result_index]
				temp_mach_state, cmd_override = result.result_exe(active_gs, self.mach_state)
				self.mach_state = temp_mach_state
				return cmd_override

class InvisMach(Invisible, MachineMixIn):
		def __init__(self, name, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
				Invisible.__init__(self, name)
				MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst)

class ViewOnlyMach(ViewOnly, MachineMixIn):
		def __init__(self, name, full_name, root_name, descript_key, writing, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
				ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
				MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst)

# class WarnClass(InvisMach):
class Warning(Invisible):
		def __init__(self, name, trigger_type, trig_vals_lst, warn_max, warn_count, warn_key_1, warn_key_2):
#				super().__init__(name, trigger_type, trig_vals_lst)
				super().__init__(name)

## DUP CODE TO MachineMixIn ###
				self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
				self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
## DUP CODE TO MachineMixIn ###

				self._warn_max = warn_count # max number of warnings - usually 0 or 2
				self._warn_count = warn_count # number of warnings given so far
				self._warn_key_1 = warn_key_1 # first warning key
				self._warn_key_2 = warn_key_2 # second warning key


## DUP CODE TO MachineMixIn ###
		@property
		def trigger_type(self):
				return self._trigger_type

		@property
		def trig_vals_lst(self):
				return self._trig_vals_lst
## DUP CODE TO MachineMixIn ###

		@property
		def warn_max(self):
				return self._warn_max

		@property
		def warn_count(self):
				return self._warn_count

		@warn_count.setter
		def warn_count(self, new_count):
				self._warn_count = new_count

		@property
		def warn_key_1(self):
				return self._warn_key_1

		@property
		def warn_key_2(self):
				return self._warn_key_2


## DUP CODE TO MachineMixIn ###
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
## DUP CODE TO MachineMixIn ###


		def run_mach(self, active_gs):
				cmd_override = True
				if self.warn_max == 0:
						active_gs.buffer(descript_dict[self.warn_key_1])
				elif self.warn_count < self.warn_max + 1:
						local_key = 'warn_key_' + warn_count
						active_gs.buffer(descript_dict[local_key])
				elif self.warn_count == self.warn_max + 1:
						active_gs.buffer("Don't say I didn't warn you Burt...")
						cmd_override = False
				return cmd_override

