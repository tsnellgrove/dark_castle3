# program: dark castle v3.56
# name: Tom Snellgrove
# date: Dec 31, 2021
# description: class deffinition module


### import
import random
from static_gbl import descript_dict, static_dict
from shared_class_func import obj_lst_to_str


### local functions


### classes
class Invisible(object):
		def __init__(self, name):
				self._name = name

		@property
		def name(self):
				return self._name

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

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

