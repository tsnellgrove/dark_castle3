# program: dark castle v3.54
# name: Tom Snellgrove
# date: Dec 20, 2021
# description: class deffinition module for Conditions

### import
from static_gbl import descript_dict, static_dict


class PassThruResult(object):
		def __init__(self, name, cmd_override):
				self._name = name
				self._cmd_override = cmd_override # does the triggered pre-action over-ride the 'standard' response to player command?

		@property
		def name(self):
				return self._name

		@property
		def cmd_override(self):
				return self._cmd_override

		def results_exe(self, active_gs, machine_state):
				return machine_state, self.cmd_override

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

class BufferOnlyResult(PassThruResult):
		def __init__(self, name, result_descript, cmd_override):
				super().__init__(name, cmd_override)
				self._result_descript = result_descript # description of result

		@property
		def result_descript(self):
				return self._result_descript

		def results_exe(self, active_gs, machine_state):
				active_gs.buffer(descript_dict[self.result_descript])
				return machine_state, self.cmd_override

class BufferAndEndResult(BufferOnlyResult):
		def __init__(self, name, result_descript, ending, cmd_override):
				super().__init__(name, result_descript, cmd_override)
				self._ending = ending # game ending - typically 'death' due to a room hazzard

		@property
		def ending(self):
				return self._ending

##		def results_exe(self, active_gs, machine_state):
##				active_gs.set_game_ending(self.ending)
##				super(BufferAndEndResult, self).results_exe(active_gs, machine_state)

		def results_exe(self, active_gs, machine_state):
				active_gs.buffer(descript_dict[self.result_descript])
				active_gs.set_game_ending(self.ending)
				return machine_state, self.cmd_override

class BufferAndGiveResult(BufferOnlyResult):
		def __init__(self, name, result_descript, give_item, cmd_override):
				super().__init__(name, result_descript, cmd_override)
				self._give_item = give_item # item to be given to Burt

		@property
		def give_item(self):
				return self._give_item

		def results_exe(self, active_gs, machine_state):
				active_gs.buffer(descript_dict[self.result_descript])
				active_gs.put_in_hand(self.give_item)
				machine_state = True
				return machine_state, self.cmd_override

class AddObjToRoomResult(BufferOnlyResult):
		def __init__(self, name, result_descript, room_item, cmd_override):
				super().__init__(name, result_descript, cmd_override)
				self._room_item = room_item # item to be added to room_obj_lst

		@property
		def room_item(self):
				return self._room_item

		def results_exe(self, active_gs, machine_state):
				active_gs.buffer(descript_dict[self.result_descript])
				room_obj = active_gs.get_room()
				room_obj.room_obj_lst_append(self.room_item)
				machine_state = True
				return machine_state, self.cmd_override
