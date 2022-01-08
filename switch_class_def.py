# program: dark castle v3.56
# name: Tom Snellgrove
# date: Jan 8, 2022
# description: class deffinition module for Machines

### import
from noun_class_def import ViewOnly

### class definitions
class ButtonSwitch(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, trigger_type):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._switch_state = switch_state # values = 'pushed' or 'neutral'
				self._trigger_type = trigger_type # machine state variable; for switches typically 'pre_action_auto_reset'

		@property
		def switch_state(self):
				return self._switch_state

		@switch_state.setter
		def switch_state(self, new_state):
				self._switch_state = new_state

		@property
		def trigger_type(self):
				return self._trigger_type

		def push(self, active_gs):
				self.switch_state = 'pushed'
				active_gs.buffer("Pushed.")

class SpringSliderSwitch(ButtonSwitch):
		def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, trigger_type):
				super().__init__(name, full_name, root_name, descript_key, writing, switch_state, trigger_type)

		def pull(self, active_gs):
				self.switch_state = 'pulled'
				active_gs.buffer("Pulled.")

class LeverSwitch(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, switch_state, trigger_type):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._switch_state = switch_state # values = 'pushed' or 'neutral'
				self._trigger_type = trigger_type # machine state variable; for switches typically 'pre_action_auto_reset'

		@property
		def switch_state(self):
				return self._switch_state

		@switch_state.setter
		def switch_state(self, new_state):
				self._switch_state = new_state

		@property
		def trigger_type(self):
				return self._trigger_type

		def pull(self, active_gs):
				if self.switch_state == 'down':
						self.switch_state = 'up'
				else:
						self.switch_state = 'down'
				active_gs.buffer("Pulled.")

		def examine(self, active_gs):
				super(LeverSwitch, self).examine(active_gs)
				lever_string = "The " + self.full_name + " is " + self.switch_state + "."
				active_gs.buffer(lever_string)	
