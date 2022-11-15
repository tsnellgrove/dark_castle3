# program: dark castle v3.74
# name: Tom Snellgrove
# date: Nov 5, 2022
# description: class deffinition module for Machines


### import
from base_class_def import ViewOnly


### classes
class SwitchMixIn(object):
	def __init__(self, switch_state, def_switch_state, trigger_type):
		""" The SwitchMixIn can be combined with other classes (most typically ViewOnly) to produce a switch the player can manipulate.
		"""
		self._switch_state = switch_state # sample switch_state values = 'pushed' or 'neutral'
		self._def_switch_state = def_switch_state # default switch state, typically 'neutral'
		self._trigger_type = trigger_type # typically 'auto_switch_reset' for auto-springback switches or None for stateful switches

	# *** getters & setters ***
	@property
	def switch_state(self):
		return self._switch_state

	@switch_state.setter
	def switch_state(self, new_state):
		self._switch_state = new_state

	@property
	def def_switch_state(self):
		return self._def_switch_state

	@property
	def trigger_type(self):
		return self._trigger_type

	# *** simple methods ***
	def is_mach(self):
		return True

class ButtonSwitch(SwitchMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
		""" The ButtonSwitch class combines ViewOnly and SwitchMixIn to create a simple 2-state ('neutral' or 'pushed') switch that automatically springs back to neutral.
		"""
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		SwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

	# *** verb methods ***
	def push(self, active_gs):
		""" Sets the switch state to 'pushed' until it is auto-reset in the auto_action.py module
		"""
		self.switch_state = 'pushed'
		active_gs.buffer("Pushed.")
		return 

class SpringSliderSwitch(ButtonSwitch):
	def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
		""" SpringSliderSwitch class inherits from ButtonSwitch. It is a 3-state switch ('neutral', 'pushed', and 'pulled') that automatically springs back to 'neutral'.
		"""
		super().__init__(name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type)

	# *** verb methods ***
	def pull(self, active_gs):
		""" Sets the switch state to 'pulled' until it is auto-reset in the auto_action.py module
		"""
		self.switch_state = 'pulled'
		active_gs.buffer("Pulled.")
		return 

class LeverSwitch(SwitchMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
		""" LeverSwitch class combines ViewOnly and SwitchMixIn to create a 2-state ('up' or 'down') stateful switch.
		"""
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		SwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

	# *** display methods ***
	def has_cond(self):
		return True

	def disp_cond(self, active_gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		active_gs.buff_no_cr(f"The {self.full_name} is {self.switch_state}.")
		return 

	# *** verb methods ***
	def pull(self, active_gs):
		""" Toggles the switch state between 'up' and 'down'.
		"""
		if self.switch_state == 'down':
			self.switch_state = 'up'
		else:
			self.switch_state = 'down'
		active_gs.buffer("Pulled.")
		return 


