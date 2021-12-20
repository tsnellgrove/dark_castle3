# program: dark castle v3.54
# name: Tom Snellgrove
# date: Dec 19, 2021
# description: class deffinition module


### import
import random
from static_gbl import descript_dict, static_dict


### class functions
def obj_lst_to_str(obj_lst):
		if not isinstance(obj_lst, list):
				raise ValueError("is not a list")
		elif len(obj_lst) == 0:
				lst_str = "nothing"
		else:
				lst_str = ""
				for obj in obj_lst:
						lst_str = lst_str + obj.full_name + ", "
				lst_str = lst_str[:-2]
		return lst_str

### classes
class Invisible(object):
		def __init__(self, name):
				self._name = name

		@property
		def name(self):
				return self._name

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

class NotInHandCond(Invisible):
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

class StateCond(Invisible):
		def __init__(self, name, mach_state_cond):
				super().__init__(name)
				self._mach_state_cond = mach_state_cond # boolean test for passed in boolean value

		@property
		def mach_state_cond(self):
				return self._mach_state_cond

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				return machine_state == self.mach_state_cond

class InHandAndStateCond(Invisible):
		def __init__(self, name, in_hand_lst, mach_state_cond):
				super().__init__(name)
				self._in_hand_lst = in_hand_lst # list of items that will meet condition
				self._mach_state_cond = mach_state_cond # boolean test for passed in boolean value

		@property
		def in_hand_lst(self):
				return self._in_hand_lst

		@property
		def mach_state_cond(self):
				return self._mach_state_cond

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				cond_state = False
				if machine_state == self.mach_state_cond:
						hand_lst = active_gs.get_hand_lst()
						for item in self.in_hand_lst:
								if item in hand_lst:
										cond_state = True
				return cond_state

class PassThruCond(Invisible):
		def __init__(self, name):
				super().__init__(name)

		def cond_check(self, active_gs, machine_state, cond_swicth_lst):
				cond_state = True
				return cond_state

class SwitchStateCond(Invisible):
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


class BufferOnlyResult(Invisible):
		def __init__(self, name, result_descript, cmd_override):
				super().__init__(name)
				self._result_descript = result_descript # description of result
				self._cmd_override = cmd_override # does the triggered pre-action over-ride the 'standard' response to player command?

		@property
		def result_descript(self):
				return self._result_descript

		@property
		def cmd_override(self):
				return self._cmd_override

		def results_exe(self, active_gs, machine_state):
				active_gs.buffer(descript_dict[self.result_descript])
				return machine_state, self.cmd_override

class BufferAndEndResult(BufferOnlyResult):
		def __init__(self, name, result_descript, ending, cmd_override):
				super().__init__(name, result_descript, cmd_override)
				self._ending = ending # game ending - typicall 'death' due to hazzard or None (meaning no ending)

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
				self._room_item = room_item # item to be given to Burt

		@property
		def room_item(self):
				return self._room_item

		def results_exe(self, active_gs, machine_state):
				active_gs.buffer(descript_dict[self.result_descript])
				room_obj = active_gs.get_room()
				room_obj.room_obj_lst_append(self.room_item)
				machine_state = True
				return machine_state, self.cmd_override

class InvisMach(Invisible):
		def __init__(self, name, trigger_type, machine_state, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst):
				super().__init__(name)
				self._trigger_type = trigger_type # pre_act_cmd, pre_act_switch, pre_act_auto, post_act_cmd, post_act_switch, or post_act_auto
				self._machine_state = machine_state # machine state variable; boolean for simple machines; Int for complex
				self._trig_switch = trig_switch # the switch whose state change can trigger the machine (only one switch per machine)
				self._trig_vals_lst = trig_vals_lst # tirgger values that will start the machine (commands or switch states; None for auto?)
				self._cond_swicth_lst = cond_swicth_lst # list of switches associated with the machine with states that contribute to conditions
				self._cond_lst = cond_lst # list of condition obj to test for; should cover all trigger cases
				self._result_lst = result_lst # list of possible result obj ordered by assciated condition

		@property
		def trigger_type(self):
				return self._trigger_type

		@property
		def machine_state(self):
				return self._machine_state

		@machine_state.setter
		def machine_state(self, new_state):
				self._machine_state = new_state

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

		# formats trigger state into trig_key_lst based on case and returns true if trig_key_lst is in trig_vals_lst
		def trig_check(self, active_gs, case, word_lst):
				trig_key_lst = 'not_valid'
				if case == 'go':
						trig_key_lst = [word_lst[1], word_lst[2]]
				elif case == '2word':
						trig_key_lst = [word_lst[1], word_lst[0].name]
				elif  case == 'tru_1word':
						trig_key_lst = word_lst
				elif  case == 'put':
						trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
				elif case == 'switch':
						trig_key_lst = word_lst[0]
				return trig_key_lst in self.trig_vals_lst

		def trigger(self, active_gs):
				cond_return_lst = []
				for cond in self.cond_lst:
						cond_return = cond.cond_check(active_gs, self.machine_state, self.cond_swicth_lst)
						cond_return_lst.append(cond_return)
				result_num = cond_return_lst.index(True)
				result = self.result_lst[result_num]
				temp_machine_state, cmd_override = result.results_exe(active_gs, self.machine_state)
				self.machine_state = temp_machine_state
				return cmd_override

class Writing(Invisible):
		def __init__(self, name, full_name, root_name, descript_key):
				super().__init__(name)
				self._full_name = full_name
				self._root_name = root_name
				self._descript_key = descript_key

		@property
		def full_name(self):
				return self._full_name

		@property
		def root_name(self):
				return self._root_name

		@property
		def descript_key(self):
				return self._descript_key

		def get_descript_str(self, active_gs):
				try:
						descript_str = active_gs.get_dynamic_desc_dict(self.descript_key)
				except:
						descript_str = descript_dict[self.descript_key]
				return descript_str

		def is_container(self):
					return hasattr(self, 'contains')

		def is_beverage(self):
				return hasattr(self, 'drink_desc_key')

		def	print_contents_str(self, active_gs):
				if self.is_container() and self.open_state == True:
						container_str = obj_lst_to_str(self.contains)
						active_gs.buffer("The " + self.full_name + " contains: " + container_str)

		def read(self, active_gs):
				descript_str = self.get_descript_str(active_gs)
				active_gs.buffer(descript_str)

class ViewOnly(Writing):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key)
				self._writing = writing

		@property
		def writing(self):
				return self._writing

		def has_writing(self):
				return (self.writing is not None)

		def examine(self, active_gs):
				descript_str = self.get_descript_str(active_gs)
				active_gs.buffer(descript_str)
				if self.has_writing():
						output = "On the " + self.full_name + " you see: " + self.writing.full_name
						active_gs.buffer(output)

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


class Room(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, features, room_obj_lst, door_paths, invis_obj_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._features = features # list of non-items in room (can be examined but not taken)
				self._room_obj_lst = room_obj_lst # list of obj in the room that the player can interact with
				self._door_paths = door_paths # dictionary of {direction1 : door1}
				self._invis_obj_lst = invis_obj_lst # list of invisible obj in room

		@property
		def features(self):
				return self._features

		@property
		def room_obj_lst(self):
				return self._room_obj_lst

		def room_obj_lst_append(self, item):
				self._room_obj_lst.append(item)

		def room_obj_lst_remove(self, item):
				self._room_obj_lst.remove(item)

		@property
		def door_paths(self):
				return self._door_paths
		
		def	door_in_path(self, direction):
				return direction in self.door_paths

		def get_door(self, direction):
				return self.door_paths[direction]

		@property
		def invis_obj_lst(self):
				return self._invis_obj_lst

		def examine(self, active_gs):
				super(Room, self).examine(active_gs)
				room_str = obj_lst_to_str(self.room_obj_lst)
				active_gs.buffer("The room contains: " + room_str)
				for obj in self.room_obj_lst:
						obj.print_contents_str(active_gs)

		def go(self, direction, active_gs):
				room_obj = active_gs.get_room()
				door_in_path = self.door_in_path(direction)
				if door_in_path:
						door_obj = self.get_door(direction)
				if not active_gs.is_valid_map_direction(room_obj, direction):
						num = random.randint(0, 4)
						wrong_way_key = 'wrong_way_' + str(num)
						active_gs.buffer(descript_dict[wrong_way_key])
				elif (door_in_path) and (door_obj.open_state == False):
						active_gs.buffer("The " +  door_obj.full_name + " is closed.")
				else:
						next_room_obj = active_gs.get_next_room(room_obj, direction)
						active_gs.set_room(next_room_obj)
						next_room_obj.examine(active_gs)

class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key, writing)

		def take(self, active_gs):
				room_obj = active_gs.get_room()
				hand_lst = active_gs.get_hand_lst()
				backpack_lst = active_gs.get_backpack_lst()
				worn_lst = active_gs.get_worn_lst()
				room_obj_lst = room_obj.room_obj_lst
				if active_gs.hand_check(self):
						active_gs.buffer("You're already holding the " + self.full_name)
				else:
						active_gs.put_in_hand(self)
						active_gs.buffer("Taken")
						if self in backpack_lst: # if taken from backpack, remove from backpack
								active_gs.backpack_lst_remove_item(self)
						elif self in worn_lst: # if taken from worn_lst, remove from worn_lst
								if self.remove_descript is not None:
										active_gs.buffer(descript_dict[self.remove_descript])
								active_gs.worn_lst_remove_item(self)
						elif self in room_obj_lst: # if taken from room, remove from room
								room_obj.room_obj_lst_remove(self)
						else:
								for obj in room_obj_lst: # else remove item from container it's in
										if obj.is_container():
												if self in obj.contains:
														obj.contains_remove(self)

		def drop(self, active_gs):
				if not active_gs.hand_check(self):
						output = "You're not holding the " + self.full_name + " in your hand."
						active_gs.buffer(output)
				else:
						active_gs.hand_lst_remove_item(self)
						room_obj = active_gs.get_room()
						room_obj.room_obj_lst_append(self)
						active_gs.buffer("Dropped")

class Door(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, open_state, unlock_state, key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._open_state = open_state
				self._unlock_state = unlock_state
				self._key = key

		@property
		def unlock_state(self):
				return self._unlock_state

		@unlock_state.setter
		def unlock_state(self, new_state):
				self._unlock_state = new_state

		@property
		def open_state(self):
				return self._open_state

		@open_state.setter
		def open_state(self, new_state):
				self._open_state = new_state

		@property
		def key(self):
				return self._key

		@key.setter
		def key(self, new_key):
				self._key = key

		def examine(self, active_gs):
				super(Door, self).examine(active_gs)
				if self.open_state == False:
						active_gs.buffer("The " + self.full_name + " is closed.")
				else:
						active_gs.buffer("The " + self.full_name + " is open.")

		def unlock(self, active_gs):
				if self.unlock_state == True:
						active_gs.buffer("The " + self.full_name + " is already unlocked.")
				elif self.key is None:
						active_gs.buffer("You don't see a keyhole for this door.")
				elif not active_gs.hand_check(self.key):
						active_gs.buffer("You aren't holding the key.")
				else:
						active_gs.buffer("Unlocked")
						self.unlock_state = True

		def open(self, active_gs):
				if self.open_state == True:
						active_gs.buffer("The " + self.full_name + " is already open.")
				elif self.unlock_state == False:
						active_gs.buffer("The " + self.full_name + " is locked.")
				else:
						self.open_state = True
						active_gs.buffer("Openned")

		def close(self, active_gs):
				if self.open_state == False:
						active_gs.buffer("The " + self.full_name + " is already closed.")
				elif self.unlock_state == False: # for Iron Portcullis
						active_gs.buffer("The " + self.full_name + " is locked.")
				else:
						self.open_state = False
						active_gs.buffer("Closed")

		def lock(self, active_gs):
				if self.open_state == True:
						active_gs.buffer("You can't lock something that's open.")
				if not active_gs.hand_check(self.key):
						active_gs.buffer("You aren't holding the key.")
				elif self.unlock_state == False:
						active_gs.buffer("The " + self.full_name + " is already locked.")
				else:
						active_gs.buffer("Locked")
						self.unlock_state = False

class Container(Door):
		def __init__(self, name, full_name, root_name, descript_key, writing, open_state, unlock_state, key, contains):
				super().__init__(name, full_name, root_name, descript_key, writing, open_state, unlock_state, key)
				self._contains = contains # list of items in the container

		@property
		def contains(self):
				return self._contains

		def contains_append(self, item):
				self._contains.append(item)

		def contains_remove(self, item):
				self._contains.remove(item)

		def examine(self, active_gs):
				super(Container, self).examine(active_gs)
				self.print_contents_str(active_gs)

		def open(self, active_gs):
				super(Container, self).open(active_gs)
				self.print_contents_str(active_gs)

		def put(self, obj, active_gs):
				if not active_gs.hand_check(obj):
						active_gs.buffer("You aren't holding the " + obj.full_name)
				elif self.open_state == False:
						active_gs.buffer("The " + self.full_name + " is closed.")
				elif obj.is_container():
						active_gs.buffer("You can't put a container in a container")
				else:
						active_gs.hand_lst_remove_item(obj)
						self.contains_append(obj)
						active_gs.buffer("Done")
						
class Food(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, eat_desc_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._eat_desc_key = eat_desc_key # keys to description of eating food (stored in descript_dict)

		@property
		def eat_desc_key(self):
				return self._eat_desc_key

		def eat(self, active_gs):
				if not active_gs.hand_check(self):
						output = "You're not holding the " + self.full_name + " in your hand."
						active_gs.buffer(output)
				else:
						active_gs.hand_lst_remove_item(self)
						output = "Eaten. The " + self.full_name + " " + descript_dict[self.eat_desc_key]
						active_gs.buffer(output)

class Jug(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, open_state, contains):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._open_state = open_state # is the jug uncapped?
				self._contains = contains # obj in the jug

		@property
		def contains(self):
				return self._contains

		@property
		def open_state(self):
				return self._open_state

		def examine(self, active_gs):
				super(Jug, self).examine(active_gs)
				self.print_contents_str(active_gs)

class Beverage(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, drink_descript_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._drink_desc_key = drink_descript_key # key to description of drinking the beverage (stored in descript_dict)

		@property
		def drink_desc_key(self):
				return self._drink_desc_key

		def drink(self, active_gs):
				hand_lst = active_gs.get_hand_lst()
				if (active_gs.hand_empty()) or (hand_lst[0].is_container() == False):
						output = "You don't seem to be holding a container of " + self.full_name + " in your hand."
						active_gs.buffer(output)
				elif self not in hand_lst[0].contains:
						output = "The container in your hand doesn't contain " + self.full_name + "."
						active_gs.buffer(output)
				else:
						hand_lst[0].contains.remove(self)
						output = "Drunk. The " + self.full_name + " " + descript_dict[self.drink_desc_key]
						active_gs.buffer(output)

class Clothes(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, wear_descript, remove_descript, clothing_type):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._wear_descript = wear_descript # description when wearing garment (can be None)
				self._remove_descript = remove_descript # description when removing garment (can be None)
				self._clothing_type = clothing_type # e.g. 'hat'; Burt can only wear one garment of a given type at a time

		@property
		def wear_descript(self):
				return self._wear_descript

		@property
		def remove_descript(self):
				return self._remove_descript

		@property
		def clothing_type(self):
				return self._clothing_type

		def wear(self, active_gs):
				if not active_gs.hand_check(self):
						output = "You're not holding the " + self.full_name + " in your hand."
						active_gs.buffer(output)
				elif active_gs.clothing_type_worn(self):
						output = "You are already wearing a " + self.clothing_type + ". You can't wear two garments of the same type at the same time."
						active_gs.buffer(output)
				else:
						active_gs.worn_lst_append_item(self)
						active_gs.hand_lst_remove_item(self)
						active_gs.buffer("Worn.")
						if self.wear_descript is not None:
								active_gs.buffer(descript_dict[self.wear_descript])

##		def remove(self, active_gs):
##				if self not in active_gs.get_worn_lst():
##						output = "You're not wearing the " + self.full_name + "."
##						active_gs.buffer(output)
##				else:
##						active_gs.put_in_hand(self)
##						active_gs.worn_lst_remove_item(self)
##						active_gs.buffer("Removed.")
##						if self.remove_descript is not None:
##								active_gs.buffer(descript_dict[self.remove_descript])

