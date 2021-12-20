# program: dark castle v3.54
# name: Tom Snellgrove
# date: Dec 20, 2021
# description: class deffinition module for Conditions

### import


### classes

# class Invisible(object):
#		def __init__(self, name):
#				self._name = name

#		@property
#		def name(self):
#				return self._name

#		def __repr__(self):
#				return f'Object { self.name } is of class { type(self).__name__ } '

# class PassThruCond(Invisible):
class PassThruCond(object):
		def __init__(self, name):
#				super().__init__(name)
				self._name = name

		@property
		def name(self):
				return self._name

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				cond_state = True
				return cond_state

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

# class NotInHandCond(Invisible):
class NotInHandCond(PassThruCond):
		def __init__(self, name, not_in_hand_lst):
				super().__init__(name)
				self._not_in_hand_lst = not_in_hand_lst # list of items that will not meet condition

		@property
		def not_in_hand_lst(self):
				return self._not_in_hand_lst

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				cond_state = True
				hand_lst = active_gs.get_hand_lst()
				for item in self.not_in_hand_lst:
						if item in hand_lst:
								cond_state = False
				return cond_state

# class StateCond(Invisible):
class StateCond(PassThruCond):
		def __init__(self, name, mach_state_cond):
				super().__init__(name)
				self._mach_state_cond = mach_state_cond # boolean test for passed in boolean value

		@property
		def mach_state_cond(self):
				return self._mach_state_cond

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				return machine_state == self.mach_state_cond

# class InHandAndStateCond(Invisible):
class InHandAndStateCond(StateCond):
		def __init__(self, name, in_hand_lst, mach_state_cond):
#				super().__init__(name)
				super().__init__(name, mach_state_cond)
				self._in_hand_lst = in_hand_lst # list of items that will meet condition
#				self._mach_state_cond = mach_state_cond # boolean test for passed in boolean value

		@property
		def in_hand_lst(self):
				return self._in_hand_lst

#		@property
#		def mach_state_cond(self):
#				return self._mach_state_cond

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				cond_state = False
				if machine_state == self.mach_state_cond:
						hand_lst = active_gs.get_hand_lst()
						for item in self.in_hand_lst:
								if item in hand_lst:
										cond_state = True
				return cond_state

# class SwitchStateCond(Invisible):
class SwitchStateCond(PassThruCond):
		def __init__(self, name, switch_state_val_lst):
				super().__init__(name)
				self._switch_state_val_lst = switch_state_val_lst # list of switch state values to meet condition

		@property
		def switch_state_val_lst(self):
				return self._switch_state_val_lst

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				switch_state_lst = []
				for switch in cond_swicth_lst:
						switch_state_lst.append(switch.switch_state)
				return switch_state_lst == self.switch_state_val_lst



