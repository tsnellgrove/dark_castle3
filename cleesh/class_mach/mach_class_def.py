# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for Machines

### import
from cleesh.class_std.item_class_def import Item, Weapon
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
		""" ProtoMachMixIn provides the core machine attributes. All other machine classes inherit from it. 
		"""

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
	def run_mach(self, gs, is_valid):
		pass
		return False, False

class TrigMixIn(object):
	def __init__(self, trig_vals_lst):
		self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (cmd / switches)
		""" TrigMixIn provides the trig_vals_lst attribute and the trig_check method.
		All non-auto machine classes inherit from TrigMixIn. 
		"""

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
		elif  case == 'prep':
			trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
			trig_wc_lst = [word_lst[1], '*', word_lst[0].name]
		elif case in['tru_1word', 'timer', 'switch']:
			trig_key_lst = word_lst
		return (trig_key_lst in self.trig_vals_lst) or (trig_wc_lst in self.trig_vals_lst)


class Timer(ProtoMachMixIn, Invisible):
	def __init__(self, name, trigger_type, mach_state, alert_anchor, is_enabled, is_active, timer_max):
		Invisible.__init__(self, name)
		ProtoMachMixIn.__init__(self, mach_state, trigger_type, alert_anchor, is_enabled) # mach_state = timer_count		
		self._is_active = is_active # bool that indicates whether Timer obj is active [replace w/ mehthod]
		self._timer_max = timer_max # int; number that timer counts up to
		""" Timer is the most primitive non-MixIn machine class - inheriting from ProtoMachMixIn and Invisible.
		It has a number of simple methods and overrides the ProtoMachMixIn run_mach method. 
		"""

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
	def run_mach(self, gs, is_valid):
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
		""" Warning is a primitive non-MixIn machine class - inheriting from ProtoMachMixIn, TrigMixIn, 
		and Invisible. It has one attribute (warn_max) and overrides run_mach(). 
		"""

	# getters & setters
	@property
	def warn_max(self):
		return self._warn_max

	# complex methods
	def run_mach(self, gs, is_valid):
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
		ProtoMachMixIn.__init__(self, mach_state, trigger_type, alert_anchor, is_enabled)
		self._cond_lst = cond_lst # list of condition obj to test for; should cover all cases
		self._result_lst = result_lst # list of possible result obj ordered by assciated condition
		""" AutoMachMixIn inherits from ProtoMachMixIn and adds attributes for conditions and results. 
		It provides the version of run_mach() that will be used by all inheriting machines. 
		All machines that auto-run each turn inherit directly from AutoMachMixIn.
		"""

	# getters & setters
	@property
	def cond_lst(self):
		return self._cond_lst

	@property
	def result_lst(self):
		return self._result_lst

	# complex methods
	def run_mach(self, gs, is_valid):
		for idx, cond in enumerate(self.cond_lst):
			if cond.cond_check(gs, self.mach_state, is_valid):
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

class InvisAutoMach(AutoMachMixIn, Invisible):
	def __init__(self, name, mach_state, trigger_type, alert_anchor, is_enabled, cond_lst, result_lst):
		Invisible.__init__(self, name)
		AutoMachMixIn.__init__(self, mach_state, trigger_type, alert_anchor, is_enabled, cond_lst, result_lst)

class WeaponAutoMach(AutoMachMixIn, Weapon):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, desc_lst, mach_state, trigger_type, alert_anchor, is_enabled, cond_lst, result_lst):
		Weapon.__init__(self, name, full_name, root_name, descript_key, writing, weight, desc_lst)
		AutoMachMixIn.__init__(self, mach_state, trigger_type, alert_anchor, is_enabled, cond_lst, result_lst)

	def disp_cond(self, gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		if self.mach_state is None:
			return
		else:
			gs.io.buff_d(f"{self.name}_{self.mach_state}", self.full_name)
			return

class TrigMachMixIn(AutoMachMixIn, TrigMixIn):
	def __init__(self, mach_state, trigger_type, alert_anchor, is_enabled, trig_vals_lst, cond_lst, result_lst):
		AutoMachMixIn.__init__(self,  mach_state, trigger_type, alert_anchor, is_enabled, cond_lst, result_lst)
		TrigMixIn.__init__(self, trig_vals_lst)
		""" TrigMachMixIn inherits from AutoMachMixIn and TrigMixIn. All command-triggered machines inherit 
		from it.
		"""

class InvisTrigMach(TrigMachMixIn, Invisible):
	def __init__(self, name, mach_state, trigger_type, alert_anchor, is_enabled, trig_vals_lst, cond_lst, result_lst):
		Invisible.__init__(self, name)
		TrigMachMixIn.__init__(self,  mach_state, trigger_type, alert_anchor, is_enabled, trig_vals_lst, cond_lst, result_lst)

class ItemTrigMach(TrigMachMixIn, Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, mach_state, trigger_type, alert_anchor, is_enabled, trig_vals_lst, cond_lst, result_lst):
		Item.__init__(self, name, full_name, root_name, descript_key, writing, weight)
		TrigMachMixIn.__init__(self,  mach_state, trigger_type, alert_anchor, is_enabled, trig_vals_lst, cond_lst, result_lst)

class SwitchMachMixIn(TrigMachMixIn):
	def __init__(self, mach_state, trigger_type, alert_anchor, is_enabled, trig_switch, trig_vals_lst, cond_lst, result_lst):
		TrigMachMixIn.__init__(self,  mach_state, trigger_type, alert_anchor, is_enabled, trig_vals_lst, cond_lst, result_lst)
		self._trig_switch = trig_switch # switch obj that triggers the machine
		""" SwitchMachMixIn inherits from TrigMachMixIn and adds an attribute for the switch obj that
		acts as a trigger. All switch-triggered machines inherit from it.
		"""

	# getters & setters
	@property
	def trig_switch(self):
		return self._trig_switch

class InvisSwitchMach(SwitchMachMixIn, Invisible):
	def __init__(self, name, mach_state, trigger_type, alert_anchor, is_enabled, trig_switch, trig_vals_lst, cond_lst, result_lst):
		Invisible.__init__(self, name)
		SwitchMachMixIn.__init__(self,  mach_state, trigger_type, alert_anchor, is_enabled, trig_switch, trig_vals_lst, cond_lst, result_lst)

class ContainerFixedSimpleSwitchMach(SwitchMachMixIn, ContainerFixedSimple):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, mach_state, trigger_type, alert_anchor, is_enabled, trig_switch, trig_vals_lst, cond_lst, result_lst):
		ContainerFixedSimple.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep)
		SwitchMachMixIn.__init__(self,  mach_state, trigger_type, alert_anchor, is_enabled, trig_switch, trig_vals_lst, cond_lst, result_lst)

