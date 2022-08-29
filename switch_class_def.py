# program: dark castle v3.71
# name: Tom Snellgrove
# date: Aug 10, 2022
# description: class deffinition module for Machines

### import
from noun_class_def import ViewOnly

### class definitions
class SwitchMixIn(object):
		def __init__(self, switch_state, def_switch_state, trigger_type):
				self._switch_state = switch_state # values = 'pushed' or 'neutral'
				self._def_switch_state = switch_state # default switch state, typically 'neutral'
				self._trigger_type = trigger_type # typically 'pre_act_auto_switch_reset' or None

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

class ButtonSwitch(ViewOnly, SwitchMixIn):
		def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
				ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
				SwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

		def push(self, active_gs):
				self.switch_state = 'pushed'
				active_gs.buffer("Pushed.")

class SpringSliderSwitch(ButtonSwitch):
		def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
				super().__init__(name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type)

		def pull(self, active_gs):
				self.switch_state = 'pulled'
				active_gs.buffer("Pulled.")

class LeverSwitch(ViewOnly, SwitchMixIn):
		def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, def_switch_state, trigger_type):
				ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
				SwitchMixIn.__init__(self, switch_state, def_switch_state, trigger_type)

		def pull(self, active_gs):
				if self.switch_state == 'down':
						self.switch_state = 'up'
				else:
						self.switch_state = 'down'
				active_gs.buffer("Pulled.")

		def obj_cond_disp(self, active_gs):
				active_gs.buffer(f"The {self.full_name} is {self.switch_state}.")

#		def examine(self, active_gs):
#				super(LeverSwitch, self).examine(active_gs)
#				lever_string = "The " + self.full_name + " is " + self.switch_state + "."
#				active_gs.buffer(lever_string)
