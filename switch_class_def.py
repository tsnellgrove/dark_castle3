# program: dark castle v3.75
# name: Tom Snellgrove
# date: Dec 23, 2022
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
	def is_switch(self):
		return True

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
	def has_cond(self, active_gs):
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


""" *** Module Documentation ***

	* Item class:

		Overview: 
			Switches are the first and simplest component of Complex Machines. Switches can trigger Machines (e.g. red_button, throne). Switches can also act as Conditions that control the behavior of Machines (e.g. left_lever, middle_lever, right_lever). Some switches also exhibit  simple Machine behaviors themselves (e.g. ButtonSwitch and SpringSliderSwitch classes are typically reset to 'neutral' state in the auto_action module). For this reason, is_mach() is set to True for the SwitchMixIn class.
			
		Program Architecture:
			Switches are the first class we see being implemented via the MixIn pattern. The SwitchMixIn class is not intended to be used directly for object instantiation. Instead, it can be combined (via dual inheritance) with other classes - most often ViewOnly - to give objects of those classes switch-like capabilities. Objects that dual-inherit from SwitchMixIn can appear as traditional levers and buttons that are clearly meant to invoke or contrl an action - or they can have the appearance of regular objects (e.g. the throne) - leaving it to the player to intuit that they can be manipulated.
			
			Switches, by design, are 'dumb' - meaning that they know nothing about the actions they can trigger or the Complex Machine that they are connected to. Switches only know their current switch_state. Complex Machines use switch_state as either a trigger or a condition. This approach is intuitive (at least to older minds like mine that grew up before you could fit a computer inside a button) and helps to centralize the 'smarts' of  the Complex Machine into the MachineMixIn object itself.
			
			A final topic worth covering is: where do switches reside? In the current version of Dark Castle (v3.75 as of this writing) the implementation is a bit kludgy. The throne is simply sitting in the middle of the throne_room. But the control_panel switches (red_button, left_lever, middle_levrer, and right_lever) are mentioned in the control_panel description but actually reside in antechamber.feature_lst. This keeps them out of sight and mind when Burt first enters the room but makes them available once he can examine() the control_panel and is aware of them. From a player perspective this works pretty well but it's definitely a hack. My future intention is to create a Surface class (similar to Container but objects are 'on' Surfaces rather than 'in' them and Surfaces can never be closed), make the control_panel a Surface, and then put the control_panel switches 'on' the control_panel (they are ViewOnly so Burt won't be able to take them). More on this solution once it is actually implemented.

"""
