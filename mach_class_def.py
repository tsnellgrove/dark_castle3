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

class Warning(Invisible):
		def __init__(self, name, trigger_type, trig_vals_lst, warn_max, warn_count):
				super().__init__(name)

## DUP CODE TO MachineMixIn ###
				self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
				self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
## DUP CODE TO MachineMixIn ###

				self._warn_max = warn_max # max number of warnings - usually 0 or 2
				self._warn_count = warn_count # number of warnings given so far

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
				cmd_override = False
				self.warn_count += 1
				warn_key = self.name + "_" + str(self.warn_count)
				warn_key_recur = self.name + "_1"
				warn_default = "I'm not sure that's a good idea Burt..."
				warn_close = "Don't say I didn't warn you Burt..."
				if self.warn_max == 0:
						cmd_override = True
						try:
								active_gs.buffer(descript_dict[warn_key_recur])
						except:
								active_gs.buffer(warn_default)
				elif self.warn_count < self.warn_max:
						cmd_override = True
						try:
								active_gs.buffer(descript_dict[warn_key])
						except:
								active_gs.buffer(warn_default)
				elif self.warn_count == self.warn_max:
						active_gs.buffer(warn_close)
				return cmd_override


class Timer(Invisible):
		def __init__(self, name, trigger_type, active, timer_count, timer_max, message_type, timer_done, alert_anchor):
				super().__init__(name)

## DUP CODE TO MachineMixIn ###
				self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
## DUP CODE TO MachineMixIn ###

				self._active = active
				self._timer_count = timer_count
				self._timer_max = timer_max
				self._message_type = message_type
				self._timer_done = timer_done
				self._alert_anchor = alert_anchor

## DUP CODE TO MachineMixIn ###
		@property
		def trigger_type(self):
				return self._trigger_type
## DUP CODE TO MachineMixIn ###

		@property
		def active(self):
				return self._active

		@active.setter
		def active(self, new_val):
				self._active = new_val

		@property
		def timer_count(self):
				return self._timer_count

		@timer_count.setter
		def timer_count(self, new_count):
				self._timer_count = new_count

		@property
		def timer_max(self):
				return self._timer_max

		@property
		def message_type(self):
				return self._message_type

		@property
		def timer_done(self):
				return self._timer_done

		@timer_done.setter
		def timer_done(self, new_val):
				self._timer_done = new_val

		@property
		def alert_anchor(self):
				return self._alert_anchor

		def run_mach(self, active_gs):
				cmd_override = False
				self.timer_count += 1				
#				print(str(self.timer_count))
#				print(str(self.timer_done))
				timer_key = self.name + "_" + str(self.timer_count)
				timer_key_constant = self.name + "_1"
				timer_default = "Beep!"

#				if active_gs.auto_in_alert_scope(self): #checks to see if Burt is still in the same room as the timer
				if active_gs.scope_check(self.alert_anchor):

						if self.message_type == 'variable':
								try:
										active_gs.buffer(descript_dict[timer_key])
								except:
										active_gs.buffer(timer_default)
						elif self.message_type == 'constant':
								try:
										active_gs.buffer(descript_dict[timer_key_constant])
								except:
										active_gs.buffer(timer_default)

				if self.timer_count == self.timer_max:
						self.active = False
						self.timer_count = 0
						self.timer_done = True
				return cmd_override

		def start(self):
				self.active = True

		def reset(self):
				self.timer_count = 0


