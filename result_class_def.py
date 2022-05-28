# program: dark castle v3.60
# name: Tom Snellgrove
# date: Mar 24, 2022
# description: class deffinition module for Conditions


### import
from static_gbl import descript_dict, static_dict
from cmd_exe import cmd_execute


### classes

class BufferOnlyResult(object):
		def __init__(self, name, cmd_override):
				self._name = name
				self._cmd_override = cmd_override # does the triggered pre-action over-ride the 'standard' response to player command?

		@property
		def name(self):
				return self._name

		@property
		def cmd_override(self):
				return self._cmd_override

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				return mach_state, self.cmd_override

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '



class BufferAndEndResult(BufferOnlyResult):
		def __init__(self, name, ending, cmd_override):
				super().__init__(name, cmd_override)
				self._ending = ending # game ending - typically 'death' due to a room hazzard

		@property
		def ending(self):
				return self._ending

##		def results_exe(self, active_gs, mach_state):
##				active_gs.set_game_ending(self.ending)
##				super(BufferAndEndResult, self).results_exe(active_gs, mach_state)

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				active_gs.set_game_ending(self.ending)
				return mach_state, self.cmd_override

class BufferAndGiveResult(BufferOnlyResult):
		def __init__(self, name, give_item, cmd_override):
				super().__init__(name, cmd_override)
				self._give_item = give_item # item to be given to Burt

		@property
		def give_item(self):
				return self._give_item

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				active_gs.put_in_hand(self.give_item)
				mach_state = True
				return mach_state, self.cmd_override

class AddObjToRoomResult(BufferOnlyResult):
		def __init__(self, name, room_item, cmd_override):
				super().__init__(name, cmd_override)
				self._room_item = room_item # item to be added to room_obj_lst

		@property
		def room_item(self):
				return self._room_item

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				room_obj = active_gs.get_room()
				room_obj.room_obj_lst_append(self.room_item)
				mach_state = True
				return mach_state, self.cmd_override

class DoorToggleResult(BufferOnlyResult):
		def __init__(self, name, door_obj, cmd_override):
				super().__init__(name, cmd_override)
				self._door_obj = door_obj # door to be openned or closed

		@property
		def door_obj(self):
				return self._door_obj

		def result_exe(self, active_gs, mach_state):
				if self.door_obj.open_state == True:
						self.door_obj.open_state = False
						descript_ending = "closes."
				else:
						self.door_obj.open_state = True
						descript_ending = "opens."
				try:
						active_gs.buffer(descript_dict[self.name] + descript_ending)
				except:
						pass

				return mach_state, self.cmd_override

class AttackBurtResult(BufferOnlyResult):
		def __init__(self, name, creature_obj, cmd_override):
				super().__init__(name, cmd_override)
				self._creature_obj = creature_obj # creature to attack burt

		@property
		def creature_obj(self):
				return self._creature_obj

		@creature_obj.setter
		def creature_obj(self, new_val):
				self._creature_obj = new_val

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				cmd_execute(active_gs, '2word', [self.creature_obj, 'attack_burt'])
				return mach_state, self.cmd_override

class StartTimerResult(BufferOnlyResult):
		def __init__(self, name, timer_obj, cmd_override):
				super().__init__(name, cmd_override)
				self._timer_obj = timer_obj

		@property
		def timer_obj(self):
				return self._timer_obj

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				self.timer_obj.start()
				return mach_state, self.cmd_override

class TimerAndCreatureItemResult(StartTimerResult):
		def __init__(self, name, timer_obj, cmd_override, creature_obj, ceature_item_obj):
				super().__init__(name, timer_obj, cmd_override)
				self._creature_obj = creature_obj
				self._ceature_item_obj = ceature_item_obj

		@property
		def creature_obj(self):
				return self._creature_obj

		@creature_obj.setter
		def creature_obj(self, new_val):
				self._creature_obj = new_val

		@property
		def ceature_item_obj(self):
				return self._ceature_item_obj

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer(descript_dict[self.name])
				except:
						pass
				self.timer_obj.start()
				self.creature_obj.creature_items_lst.remove(self.ceature_item_obj)
				return mach_state, self.cmd_override

class ChgCreatureDescAndStateResult(BufferOnlyResult):
		def __init__(self, name, cmd_override, creature_obj, new_desc_key):
				super().__init__(name, cmd_override)

		@property
		def creature_obj(self):
				return self._creature_obj

		@creature_obj.setter
		def creature_obj(self, new_val):
				self._creature_obj = new_val

		@property
		def new_desc_key(self):
				return self._new_desc_key

		def result_exe(self, active_gs, mach_state):
				try:
						active_gs.buffer("The " + self.creature_obj.name + " " + descript_dict[self.name])
				except:
						pass
				self.creature_obj.descript_key = self.new_desc_key
				mach_state = True
				return mach_state, self.cmd_override
				



