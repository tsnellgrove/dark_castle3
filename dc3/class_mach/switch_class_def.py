# program: dark castle v3.82
# name: Tom Snellgrove
# date: Feb 28, 2024
# description: class deffinition module for Machines


### import
from dc3.class_std.base_class_def import ViewOnly
from dc3.class_std.interactive_class_def import Seat


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

	# *** class identity methods ***
	def is_switch(self):
		return True

	def is_mach(self):
		return True

class ButtonSwitchMixIn(SwitchMixIn):
	def __init__(self, switch_state, def_switch_state, trigger_type):
		""" The ButtonSwitchMixIn can be combined with other classes (most typically ViewOnly) to produce a push-button switch the player can manipulate.
		"""
		SwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

	# *** class identity methods ***
	def is_buttonswitch(self):
		return True

	# *** verb methods ***
	def push(self, gs, mode=None):
		""" Sets the switch state to 'pushed' until it is auto-reset in the auto_action.py module
		"""
		if mode is None:
			mode = 'std'
		creature = gs.hero

		self.switch_state = 'pushed'

		gs.io.buffer("Pushed.")
		return 

class ViewOnlyButtonSwitch(ButtonSwitchMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
		""" The ViewOnlyButtonSwitch class combines ViewOnly and ButtonSwitchMixIn to create a simple 2-state ('neutral' or 'pushed') switch that automatically springs back to neutral.
		"""
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		ButtonSwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

class SpringSliderSwitchMixIn(ButtonSwitchMixIn):
	def __init__(self, switch_state, def_switch_state, trigger_type):
		""" SpringSliderSwitchMixIn class inherits from ButtonSwitchMixIn. It is a 3-state switch ('neutral', 'pushed', and 'pulled') that automatically springs back to 'neutral'.
		"""
		ButtonSwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

	# *** class identity methods ***
	def is_springsliderswitch(self):
		return True

	# *** verb methods ***
	def pull(self, gs, mode=None):
		""" Sets the switch state to 'pulled' until it is auto-reset in the auto_action.py module
		"""
		if mode is None:
			mode = 'std'
		creature = gs.hero

		self.switch_state = 'pulled'

		gs.io.buffer("Pulled.")
		return 


class SeatSpringSliderSwitch(SpringSliderSwitchMixIn, Seat):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, in_reach_lst, switch_state, def_switch_state, trigger_type):
		""" The SeatSpringSliderSwitch class combines Seat and SpringSliderSwitchMixIn to create a Seat class that can also be pushed or pulled.
		"""
		Seat.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, in_reach_lst)
		SpringSliderSwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)



class LeverSwitch(SwitchMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
		""" LeverSwitch class combines ViewOnly and SwitchMixIn to create a 2-state ('up' or 'down') stateful switch.
		"""
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		SwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

	# *** class identity methods ***
	def is_leverswitch(self):
		return True

	# *** display methods ***
	def has_cond(self, gs):
		return True

	def disp_cond(self, gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		gs.io.buff_no_cr(f"The {self.full_name} is {self.switch_state}.")
		return 

	# *** verb methods ***
	def pull(self, gs, mode=None):
		""" Toggles the switch state between 'up' and 'down'.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.hero

		if self.switch_state == 'down':
			self.switch_state = 'up'
		else:
			self.switch_state = 'down'
			
		gs.io.buffer(f"Pulled. The {self.full_name} is now {self.switch_state}.")
		return 



