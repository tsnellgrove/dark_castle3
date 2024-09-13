# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for Machines

### import
from cleesh.class_std.item_class_def import Item
from cleesh.class_std.invisible_class_def import Invisible
from cleesh.class_std.base_class_def import ViewOnly
from cleesh.class_std.interactive_class_def import ContainerFixedSimple

### classes
class ProtoMachMixIn(object):
	def __init__(self, mach_state, trigger_type, alert_anchor, is_enabled):
		self._mach_state = mach_state # machine state variable; can be bool or int 
		self._trigger_type = trigger_type # pre_act_cmd, pre_act_timer, post_act_cmd, post_act_switch, auto_act, auto_switch_reset
		self._alert_anchor = alert_anchor # hero must be in same room as alert_anchor to get mach updates
		self._is_enabled = is_enabled # bool indicating whether mach is enabled to run

	# getters & setters
	@property
	def mach_state(self):
		return self._mach_state

	@mach_state.setter
	def mach_state(self, new_state):
		self._mach_state = new_state

	@property
	def trigger_type(self):
		return self._trigger_type

	@property
	def alert_anchor(self):
		return self._alert_anchor

	@alert_anchor.setter
	def alert_anchor(self, new_val):
		self._alert_anchor = new_val

	@property
	def is_enabled(self):
		return self._is_enabled

	@is_enabled.setter
	def is_enabled(self, new_val):
		self._is_enabled = new_val

	# *** class identity methods ***
	def is_mach(self):
		return True

	# complex methods
	def run_mach(self, gs):
		pass
		return False, False

class TrigMixIn(object):
	def __init__(self, trig_vals_lst):
		self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (cmd / switches)

	# getters & setters
	@property
	def trig_vals_lst(self):
		return self._trig_vals_lst

	# complex methods
	def trig_check(self, gs, case, word_lst):
		trig_key_lst = ['not_valid']
		trig_wc_lst = ['not_valid'] # wildcards are only supported for nouns
		if case == 'go':
			trig_key_lst = [word_lst[1], word_lst[2]]
		elif case == '2word':
			trig_key_lst = [word_lst[1], word_lst[0].name]
			trig_wc_lst = [word_lst[1], '*']
		elif  case == 'tru_1word':
			trig_key_lst = word_lst
		elif  case == 'prep':
			trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
			trig_wc_lst = [word_lst[1], '*', word_lst[0].name]
		elif case == 'switch':
			trig_key_lst = word_lst[0]
		return (trig_key_lst in self.trig_vals_lst) or (trig_wc_lst in self.trig_vals_lst)


class Timer(ProtoMachMixIn, Invisible):
	def __init__(self, name, trigger_type, mach_state, alert_anchor, is_enabled, is_active, timer_max):
		Invisible.__init__(self, name)
		ProtoMachMixIn.__init__(self, mach_state, trigger_type, alert_anchor, is_enabled) # mach_state = timer_count		
		self._is_active = is_active # bool that indicates whether Timer obj is active [replace w/ mehthod]
		self._timer_max = timer_max # int; number that timer counts up to

	# getters & setters
	@property
	def is_active(self):
		return self._is_active

	@is_active.setter
	def is_active(self, new_val):
		self._is_active = new_val

	@property
	def timer_max(self):
		return self._timer_max

	@timer_max.setter
	def timer_max(self, new_val):
		self._timer_max = new_val

	# class identity methods
	def is_timer(self):
		return True

	# simple methods
	def start(self):
		self.is_active = True
		return

	def stop(self):
		self.is_active = False
		return

	def reset(self):
		self.mach_state = 0
		self.is_active = False
		return

	def set_timer(self, new_max):
		self.timer_max = new_max
		return

	def is_dinging(self):
		return self.is_active and (self.mach_state == self.timer_max)

	# complex methods
	def run_mach(self, gs):
		if self.is_dinging():
			self.reset()
			return False, False
		self.mach_state += 1
		if gs.map.hero_rm.chk_is_vis(self.alert_anchor, gs):
			try:
				gs.io.buff_f(f"{self.name}_0") # constant message type
			except:
				gs.io.buff_f(f"{self.name}_{str(self.mach_state)}") # variable message type
		return False, False


class Warning(ProtoMachMixIn, TrigMixIn, Invisible):
	def __init__(self, name, trigger_type, mach_state, alert_anchor, is_enabled, trig_vals_lst, warn_max):
		Invisible.__init__(self, name)
		TrigMixIn.__init__(self, trig_vals_lst)
		ProtoMachMixIn.__init__(self, mach_state, trigger_type, alert_anchor, is_enabled) # mach_state = warn_count		
		self._warn_max = warn_max # int; number that warning counts up to

	# getters & setters
	@property
	def warn_max(self):
		return self._warn_max

	# complex methods
	def run_mach(self, gs):
		cmd_override = True
		self.mach_state += 1
		if self.warn_max == 0:
			try:
				gs.io.buff_f(f"{self.name}_0")
			except:
				gs.io.buffer(f"I'm not sure that's a good idea {gs.core.hero.name}...")
		elif self.mach_state < self.warn_max:
			try:
				gs.io.buff_f(f"{self.name}_{str(self.mach_state)}")
			except:
				gs.io.buffer(f"I'm not sure that's a good idea {gs.core.hero.name}...")
		elif self.mach_state == self.warn_max:
			cmd_override = False
			self.is_enabled = False
			try:
				gs.io.buff_f(f"{self.name}_{str(self.mach_state)}")
			except:
				gs.io.buffer(f"Don't say I didn't warn you {gs.core.hero.name}...")
		return cmd_override, cmd_override


class AutoMachMixIn(ProtoMachMixIn):
	def __init__(self, mach_state, trigger_type, alert_anchor, is_enabled, cond_lst, result_lst):
		self._cond_lst = cond_lst # list of condition obj to test for; should cover all cases
		self._result_lst = result_lst # list of possible result obj ordered by assciated condition

	# getters & setters
	@property
	def cond_lst(self):
		return self._cond_lst

	@property
	def result_lst(self):
		return self._result_lst

	# complex methods
	def run_mach(self, gs):
##		print(f"mach running; mach_name = {self.name}") # for troubleshooting
		for idx, cond in enumerate(self.cond_lst):
			if cond.cond_check(gs, self.mach_state, self.cond_swicth_lst):
				result = self.result_lst[idx]
				if isinstance(result, list):
					cmd_override = False
					for result_element in result:
						element_mach_state, element_cmd_override = result_element.result_exe(gs, self.mach_state, result_element.name, self.alert_anchor)
						if element_cmd_override == True:
							cmd_override = True # if element_cmd_override == True for *any* result, cmd_override = True
						if element_mach_state != None:
							self.mach_state = element_mach_state # if element_mach_state set for *any* result, mach_state is set
					return cmd_override, result_element.name
				else:
					self.mach_state, cmd_override = result.result_exe(gs, self.mach_state, result.name, self.alert_anchor)
				return cmd_override, result.name
		return False, 'pass_result'


class MachineMixIn(object):
	def __init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled):
		self._mach_state = mach_state # machine state variable; boolean for simple machines; Int for complex
		self._trigger_type = trigger_type # pre_act_cmd, pre_act_timer, post_act_cmd, post_act_switch, auto_act, auto_switch_reset
		self._trig_switch = trig_switch # the switch whose state change can trigger the machine (only one switch per machine)
		self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
		self._cond_swicth_lst = cond_swicth_lst # list of switches associated with the machine with states that contribute to conditions
		self._cond_lst = cond_lst # list of condition obj to test for; should cover all trigger cases
		self._result_lst = result_lst # list of possible result obj ordered by assciated condition
		self._alert_anchor = alert_anchor # hero must be in same room as alert_anchor to get mach updates
		self._is_enabled = is_enabled # bool indicating whether mach is enabled to run

	# getters & setters
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

	@property
	def alert_anchor(self):
		return self._alert_anchor

	@alert_anchor.setter
	def alert_anchor(self, new_val):
		self._alert_anchor = new_val

	@property
	def is_enabled(self):
		return self._is_enabled

	# *** class identity methods ***
	def is_mach(self):
		return True

	# complex methods

	# formats trigger state into trig_key_lst based on case and returns true if trig_key_lst is in trig_vals_lst
	def trig_check(self, gs, case, word_lst):
		trig_key_lst = ['not_valid']
		trig_wc_lst = ['not_valid'] # wildcards are only supported for nouns
		if case == 'go':
			trig_key_lst = [word_lst[1], word_lst[2]]
		elif case == '2word':
			trig_key_lst = [word_lst[1], word_lst[0].name]
			trig_wc_lst = [word_lst[1], '*']
		elif  case == 'tru_1word':
			trig_key_lst = word_lst
		elif  case == 'prep':
			trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
			trig_wc_lst = [word_lst[1], '*', word_lst[0].name]
		elif case == 'switch':
			trig_key_lst = word_lst[0]
		elif  case == 'timer':
			trig_key_lst = word_lst[0]
##		print(f"mach = {self.name}, trig_key_lst = {trig_key_lst}") # troubleshooting
		return (trig_key_lst in self.trig_vals_lst) or (trig_wc_lst in self.trig_vals_lst)

	def run_mach(self, gs):
##		print(f"mach running; mach_name = {self.name}") # for troubleshooting
		for idx, cond in enumerate(self.cond_lst):
			if cond.cond_check(gs, self.mach_state, self.cond_swicth_lst):
				result = self.result_lst[idx]
				if isinstance(result, list):
					cmd_override = False
					for result_element in result:
						element_mach_state, element_cmd_override = result_element.result_exe(gs, self.mach_state, result_element.name, self.alert_anchor)
						if element_cmd_override == True:
							cmd_override = True # if element_cmd_override == True for *any* result, cmd_override = True
						if element_mach_state != None:
							self.mach_state = element_mach_state # if element_mach_state set for *any* result, mach_state is set
					return cmd_override, result_element.name
				else:
					self.mach_state, cmd_override = result.result_exe(gs, self.mach_state, result.name, self.alert_anchor)
				return cmd_override, result.name
		return False, 'pass_result'


class InvisMach(MachineMixIn, Invisible):
	def __init__(self, name, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled):
		Invisible.__init__(self, name)
		MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled)

class ViewOnlyMach(MachineMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled)

class ItemMach(MachineMixIn, Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled):
		Item.__init__(self, name, full_name, root_name, descript_key, writing, weight)
		MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled)

class ContainerFixedSimpleMach(MachineMixIn, ContainerFixedSimple):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled):
		ContainerFixedSimple.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep)
		MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst, alert_anchor, is_enabled)

#class SeatMach(MachineMixIn, ContainerFixedSimple):
#		def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, in_reach_lst, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
#				Seat.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, in_reach_lst)
#				MachineMixIn.__init__(self, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst)

"""
class Warning(Invisible):
	def __init__(self, name, trigger_type, trig_vals_lst, warn_max, warn_count, is_enabled):
		super().__init__(name)

## DUP CODE TO MachineMixIn ###
		self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
		self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
## DUP CODE TO MachineMixIn ###

		self._warn_max = warn_max # max number of warnings - usually 0 or 2
		self._warn_count = warn_count # number of warnings given so far
		self._is_enabled = is_enabled # bool indicating whether warning is enabled to run

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
	def is_enabled(self):
		return self._is_enabled

## DUP CODE TO MachineMixIn ###

	# simple methods
	def is_mach(self):
		return True

	# complex methods

	# formats trigger state into trig_key_lst based on case and returns true if trig_key_lst is in trig_vals_lst
	def trig_check(self, gs, case, word_lst):
		trig_key_lst = 'not_valid'
		if case == 'go':
			trig_key_lst = [word_lst[1], word_lst[2]]
		elif case == '2word':
			trig_key_lst = [word_lst[1], word_lst[0].name]
		elif  case == 'tru_1word':
			trig_key_lst = word_lst
		elif  case == 'prep':
			trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
		elif case == 'switch':
			trig_key_lst = word_lst[0]
		elif  case == 'timer':
			trig_key_lst = word_lst[0]
##				print(trig_key_lst) # used for trigger key troubleshooting
		return trig_key_lst in self.trig_vals_lst
## DUP CODE TO MachineMixIn ###


	def run_mach(self, gs):
		cmd_override = False
		self.warn_count += 1
		warn_key = self.name + "_" + str(self.warn_count)
		warn_key_recur = self.name + "_1"
		if self.warn_max == 0:
			cmd_override = True
			try:
				gs.io.buff_f(warn_key_recur)
			except:
				gs.io.buffer("I'm not sure that's a good idea Burt...")
		elif self.warn_count < self.warn_max:
			cmd_override = True
			try:
				gs.io.buff_f(warn_key)
			except:
				gs.io.buffer("I'm not sure that's a good idea Burt...")
		elif self.warn_count == self.warn_max:
			gs.io.buffer("Don't say I didn't warn you Burt...")
		return cmd_override, cmd_override
"""


""""
 class Timer(Invisible):
	def __init__(self, name, trigger_type, active, timer_count, timer_max, message_type, timer_done, alert_anchor, is_enabled):
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
		self._is_enabled = is_enabled # bool indicating whether timer is enabled to run

	# setters & getters

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

	@alert_anchor.setter
	def alert_anchor(self, new_val):
		self._alert_anchor = new_val

	@property
	def is_enabled(self):
		return self._is_enabled

	# simple methods
	def is_mach(self):
		return True

	def is_timer(self):
		return True

	# complex methods
	def run_mach(self, gs):
		cmd_override = False
		self.timer_count += 1				
		timer_key = self.name + "_" + str(self.timer_count)
		timer_key_constant = self.name + "_1"

		if gs.map.hero_rm.chk_is_vis(self.alert_anchor, gs):
			if self.message_type == 'variable':
				try:
					gs.io.buff_f(timer_key)
				except:
					gs.io.buffer("Beep!")
			elif self.message_type == 'constant':
				try:
					gs.io.buff_f(timer_key_constant)
				except:
					gs.io.buffer("Beep!")

		if self.timer_count == self.timer_max:
			self.active = False
			self.timer_count = 0
			self.timer_done = True

##				print(self.name, self.timer_count, self.timer_max, self.active, self.timer_done) # for timer troubleshooting

		return cmd_override, cmd_override

	def start(self):
		self.active = True

	def reset(self):
		self.timer_count = 0

"""