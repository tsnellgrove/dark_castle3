# program: dark castle v3.70
# name: Tom Snellgrove
# date: July 24, 2022
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

		def is_item(self):
				return False

		def is_beverage(self):
				return False

		def is_weapon(self):
				return False

		def	is_container(self):
				return False

		def is_creature(self):
				return False

		def is_timer(self):
				return False

		def is_mach(self):
				return False

		def	print_contents_str(self, active_gs):
				if self.is_container() and self.is_open == True:
						container_str = obj_lst_to_str(self.contains)
						active_gs.buffer("The " + self.full_name + " contains: " + container_str)

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

		@descript_key.setter
		def descript_key(self, new_descript):
				self._descript_key = new_descript

		def get_descript_str(self, active_gs):
				try:
						descript_str = active_gs.get_dynamic_desc_dict(self.descript_key)
				except:
						descript_str = descript_dict[self.descript_key]
				return descript_str

		def read(self, active_gs):

				if active_gs.writing_check(self) == False and active_gs.scope_check(self) == False:
						active_gs.buffer("You can't see a " + self.full_name + " here.")
						return

				if active_gs.writing_check(self) == False:
						output = "You can't read the " + self.full_name + ". Try using 'examine' instead."
						active_gs.buffer(output)
						return

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

class Room(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, features, room_obj_lst, door_paths, invis_obj_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._features = features # list of non-items in room (can be examined but not taken)
				self._room_obj_lst = room_obj_lst # list of obj in the room that the player can interact with
				self._door_paths = door_paths # dictionary of {direction1 : door1}
				self._invis_obj_lst = invis_obj_lst # list of invisible obj in room

		# getters & setters
		@property
		def features(self):
				return self._features

		@property
		def room_obj_lst(self):
				return self._room_obj_lst

		def room_obj_lst_append(self, item):
				self._room_obj_lst.append(item)

		def room_obj_lst_extend(self, lst):
				self._room_obj_lst.extend(lst)

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

		# simple methods
		def vis_element_lst(self):
				return self.room_obj_lst + self.features
		
		# complex methods
		def examine(self, active_gs):
				super(Room, self).examine(active_gs)
				room_item_obj_lst = []
				for obj in self.room_obj_lst:
						if not obj.is_item():
								active_gs.buffer("There is a " + obj.full_name + " here.")
								obj.print_contents_str(active_gs)
								if obj.is_creature() and not obj.hand_empty():
										active_gs.buffer("The " + obj.full_name + " is holding a " + obj.hand_item().full_name)
								if obj.is_creature() and not obj.worn_empty():
										active_gs.buffer("The " + obj.full_name + " is wearing: " + obj.worn_str())
						else:
								room_item_obj_lst.append(obj)
				if room_item_obj_lst:
						room_item_str_lst = obj_lst_to_str(room_item_obj_lst)
						active_gs.buffer("The following items are here: " + room_item_str_lst)
				for obj in room_item_obj_lst:
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
				elif (door_in_path) and (door_obj.is_open == False):
						active_gs.buffer("The " +  door_obj.full_name + " is closed.")
				else:
						next_room_obj = active_gs.get_next_room(room_obj, direction)
						active_gs.set_room(next_room_obj)
						next_room_obj.examine(active_gs)

class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key, writing)

		def is_item(self):
				return True

		def take(self, active_gs):

				if active_gs.hand_check(self):
						active_gs.buffer("You're already holding the " + self.full_name)
						return 

				room_obj = active_gs.get_room()
				room_obj_lst = room_obj.room_obj_lst
				backpack_lst = active_gs.get_backpack_lst()
				worn_lst = active_gs.get_worn_lst()

				if self not in room_obj_lst + backpack_lst + worn_lst:
						for obj in room_obj_lst: # handle case of obj in creature hand
								if obj.is_creature() and self in obj.vis_lst():
										active_gs.buffer("Burt, you can't take the " + self.full_name + 
														" it belongs to the " + obj.full_name + "!")
										return

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
								if obj.is_container() and obj.in_container(self):
										obj.contains_remove(self)
				return

		def drop(self, active_gs):
				active_gs.hand_lst_remove_item(self)
				room_obj = active_gs.get_room()
				room_obj.room_obj_lst_append(self)
				active_gs.buffer("Dropped")

class Door(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._is_open = is_open
				self._is_unlocked = is_unlocked
				self._key = key

		@property
		def is_unlocked(self):
				return self._is_unlocked

		@is_unlocked.setter
		def is_unlocked(self, new_state):
				self._is_unlocked = new_state

		@property
		def is_open(self):
				return self._is_open

		@is_open.setter
		def is_open(self, new_state):
				self._is_open = new_state

		@property
		def key(self):
				return self._key

		@key.setter
		def key(self, new_key):
				self._key = new_key

		def examine(self, active_gs):
				super(Door, self).examine(active_gs)
				if self.is_open == False:
						active_gs.buffer("The " + self.full_name + " is closed.")
				else:
						active_gs.buffer("The " + self.full_name + " is open.")

		def unlock(self, active_gs):
				if self.is_unlocked == True:
						active_gs.buffer("The " + self.full_name + " is already unlocked.")
				elif self.key is None:
						active_gs.buffer("You don't see a keyhole for this door.")
				elif not active_gs.hand_check(self.key):
						active_gs.buffer("You aren't holding the correct key.")
				else:
						active_gs.buffer("Unlocked")
						self.is_unlocked = True

		def open(self, active_gs):
				if self.is_open == True:
						active_gs.buffer("The " + self.full_name + " is already open.")
				elif self.is_unlocked == False:
						active_gs.buffer("The " + self.full_name + " is locked.")
				else:
						self.is_open = True
						active_gs.buffer("Openned")

		def close(self, active_gs):
				if self.is_open == False:
						active_gs.buffer("The " + self.full_name + " is already closed.")
				elif self.is_unlocked == False: # for Iron Portcullis
						active_gs.buffer("The " + self.full_name + " is locked.")
				else:
						self.is_open = False
						active_gs.buffer("Closed")

		def lock(self, active_gs):
				if self.is_open == True:
						active_gs.buffer("You can't lock something that's open.")
				elif not active_gs.hand_check(self.key):
						active_gs.buffer("You aren't holding the key.")
				elif self.is_unlocked == False:
						active_gs.buffer("The " + self.full_name + " is already locked.")
				else:
						active_gs.buffer("Locked")
						self.is_unlocked = False

class Container(Door):
		def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key, contains):
				super().__init__(name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key)
				self._contains = contains # list of items in the container

		# getters & setters
		@property
		def contains(self):
				return self._contains

		@contains.setter
		def contains(self, new_obj):
				self._contains = new_obj

		# simple methods
		def in_container(self, obj):
				return obj in self.contains

		def contains_append(self, item):
				self._contains.append(item)

		def contains_remove(self, item):
				self._contains.remove(item)

		def	is_container(self):
				return True

		def vis_lst(self):
				vis_lst = []
				if self.is_open:
						vis_lst = self.contains
				return vis_lst

		# complex methods
		def examine(self, active_gs):
				super(Container, self).examine(active_gs)
				self.print_contents_str(active_gs)

		def open(self, active_gs):
				super(Container, self).open(active_gs)
				self.print_contents_str(active_gs)

		def put(self, obj, active_gs):
				if self.is_open == False:
						active_gs.buffer("The " + self.full_name + " is closed.")
				elif obj.is_container():
						active_gs.buffer("You can't put a container in a container")
				elif obj.is_creature():
						active_gs.buffer("You can't put a creature in a container")
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
					active_gs.hand_lst_remove_item(self)
					output = "Eaten. The " + self.full_name + " " + descript_dict[self.eat_desc_key]
					active_gs.buffer(output)

class Jug(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, is_open, contains):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._is_open = is_open # is the jug uncapped?
				self._contains = contains # obj in the jug

		@property
		def contains(self):
				return self._contains

		@property
		def is_open(self):
				return self._is_open

		def	is_container(self):
				return True

		def vis_lst(self): # DUP FROM CONTAINER CLASS
				vis_lst = []
				if self.is_open:
						vis_lst = self.contains
				return vis_lst

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

		def is_beverage(self):
				return True

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
				if active_gs.clothing_type_worn(self): # was 'elif' before special error
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


class Weapon(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, desc_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._desc_lst = desc_lst # descriptive terms associated with using the weapon to 'attack'

		@property
		def desc_lst(self):
				return self._desc_lst

		def is_weapon(self):
				return True
