# program: dark castle v3.50
# name: Tom Snellgrove
# date: Nov 20, 2021
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
class GameState(object):
		def __init__(self, name, dynamic_desc_dict, map_dict, points_earned_dict, static_obj_dict, state_dict):
				self._name = name
				self._dynamic_desc_dict = dynamic_desc_dict
				self._map_dict = map_dict
				self._points_earned_dict = points_earned_dict
				self._static_obj_dict = static_obj_dict
				self._state_dict = state_dict

		def get_dynamic_desc_dict(self, dynamic_desc_key):
				if dynamic_desc_key not in self._dynamic_desc_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._dynamic_desc_dict[dynamic_desc_key]

		def set_dynamic_desc_dict(self, dynamic_desc_key, dynamic_desc_str):
				if dynamic_desc_key not in self._dynamic_desc_dict:
						raise KeyError("key does not exist in dict")
				else:
						self._dynamic_desc_dict[dynamic_desc_key] = dynamic_desc_str

		def is_valid_map_direction(self, room_obj, direction):
				return direction in self._map_dict[room_obj.name]

		def get_next_room(self, room_obj, direction):
				next_room = self._map_dict[room_obj.name][direction]
				return next_room

		def get_points_earned_state(self, score_key):
				if score_key not in self._points_earned_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._points_earned_dict[score_key]

		def set_points_earned_state(self, score_key, value):
				if score_key not in self._points_earned_dict:
						raise KeyError("key does not exist in dict")
				else:
						self._points_earned_dict[score_key] = value

		def update_score(self, points):
				self._state_dict['score'] += points 

		def get_score(self):
				return self._state_dict['score']

		def print_score(self):
				output1 = ("Your score is now " + str(self.get_score()))
				output2 = (" out of " + str(static_dict['max_score']))
				self.buffer(output1 + output2)

		def move_inc(self):
				self._state_dict['move_counter'] += 1

		def move_dec(self):
				self._state_dict['move_counter'] -= 1

		def get_moves(self):
				return self._state_dict['move_counter']

		def get_end_of_game(self):
				return self._state_dict['end_of_game']

		def set_end_of_game(self, value):
				self._state_dict['end_of_game'] = value

		def get_game_ending(self):
				return self._state_dict['game_ending']

		def set_game_ending(self, value):
				self._state_dict['game_ending'] = value

		def get_backpack_lst(self):
				return self._state_dict['backpack']

		def backpack_lst_append_item(self, item):
				self._state_dict['backpack'].append(item)

		def backpack_lst_remove_item(self, item):
				self._state_dict['backpack'].remove(item)

		def get_hand_lst(self):
				return self._state_dict['hand']

		def hand_lst_append_item(self, item):
				self._state_dict['hand'].append(item)

		def hand_lst_remove_item(self, item):
				self._state_dict['hand'].remove(item)

		def hand_check(self, obj):
				return obj in self.get_hand_lst()

		def hand_empty(self):
				return len(self.get_hand_lst()) == 0

		def put_in_hand(self, new_item):
				if not self.hand_empty():
						hand_lst = self.get_hand_lst()
						hand_item = hand_lst[0]
						self.backpack_lst_append_item(hand_item)
						self.hand_lst_remove_item(hand_item)
				self.hand_lst_append_item(new_item)

		def get_static_obj(self, static_key):
				if static_key not in self._static_obj_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._static_obj_dict[static_key]

		def get_room(self):
				return self._state_dict['room']

		def set_room(self, value):
				self._state_dict['room'] = value

		def get_buff(self):
				return self._state_dict['out_buff']

		def buffer(self, output_str):
				out_buff_old = self._state_dict['out_buff']
				out_buff_new = out_buff_old + "\n" + output_str + "\n"
				self._state_dict['out_buff'] = out_buff_new

		def reset_buff(self):
				self._state_dict['out_buff'] = ""

		def inventory(self):
				hand_obj_lst = self.get_hand_lst()
				hand_str = obj_lst_to_str(hand_obj_lst)
				self.buffer("In your hand you are holding: " + hand_str)

				backpack_obj_lst = self.get_backpack_lst()
				backpack_str = obj_lst_to_str(backpack_obj_lst)
				self.buffer("In your backpack you have: " + backpack_str)

		def scope_lst(self):
				room_obj = self.get_room()
				hand_lst = self.get_hand_lst()
				backpack_lst = self.get_backpack_lst()
				universal_lst = self.get_static_obj('universal')
				room_obj_lst = room_obj.room_obj_lst
				features_lst = room_obj.features
				scope_lst = (room_obj_lst + hand_lst + backpack_lst 
								+ universal_lst + features_lst)
				scope_lst.append(room_obj)
				room_containers = []
				for obj in scope_lst:
						if hasattr(obj, 'contains'):
								room_containers.append(obj)
				open_cont_obj_lst = []
				for obj in room_containers:
						if len(obj.contains) > 0 and obj.open_state == True:
								open_cont_obj_lst = open_cont_obj_lst + obj.contains
				scope_lst = scope_lst + open_cont_obj_lst
				return scope_lst

		def writing_check(self, writing):
				scope_lst = self.scope_lst()
				writing_found = False
				for obj in scope_lst:
						if obj.writing == writing:
								writing_found = True
				return writing_found

		def scope_check(self, obj):
				scope_lst = self.scope_lst()
				return obj in scope_lst

		def inter_obj_lst(self):
				inter_obj_lst = []
				room_obj = self.get_room()
				scope_lst = self.scope_lst() + room_obj.invis_obj_lst
				for obj in scope_lst:
						if hasattr(obj, 'inter_obj_type'):
								inter_obj_lst.append(obj)
				return inter_obj_lst

		def __repr__(self):
				return f'Object { self._name } is of class { type(self).__name__ } '

class Invisible(object):
		def __init__(self, name):
				self._name = name

		@property
		def name(self):
				return self._name

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

class TravelEffect(Invisible):
		def __init__(self, name, cmd_trigger_lst, effect_desc, cmd_override,
						inter_obj_type, game_ending, in_hand_cond, in_hand_lst, give_or_take,
						give_item, put_place):
				super().__init__(name)
				self._cmd_trigger_lst = cmd_trigger_lst # format = ["case", "word1", "word2"]
				self._effect_desc = effect_desc # what does is the player told when the pre-action trigger takes effect?
				self._cmd_override = cmd_override # does the pre-action trigger override the player's command?
				self._inter_obj_type = inter_obj_type # pre-action_trig, post-action_trig, pre-action_auto, or post-action_auto
				self._game_ending = game_ending # usually None but could be 'death' from walking into a dangerous room
				self._in_hand_cond = in_hand_cond # None for no condition; True for check items in hand; False for check items NOT in hand
				self._in_hand_lst = in_hand_lst # list of items either in or NOT in hand_lst (depending on the value of in_hand_cond)
				self._give_or_take = give_or_take # switch to choose whether an item is given or taken from hand_lst; None = no give or take
				self._give_item = give_item # item to be given to player if conditions met
				self._put_place = put_place # where players item will be placed if conditions are met

		@property
		def cmd_trigger_lst(self):
				return self._cmd_trigger_lst

		@property
		def effect_desc(self):
				return self._effect_desc

		@property
		def cmd_override(self):
				return self._cmd_override

		@property
		def inter_obj_type(self):
				return self._inter_obj_type

		@property
		def game_ending(self):
				return self._game_ending

		@property
		def in_hand_cond(self):
				return self._in_hand_cond

		@property
		def in_hand_lst(self):
				return self._in_hand_lst

		@property
		def give_or_take(self):
				return self._give_or_take

		@property
		def give_item(self):
				return self._give_item

		@property
		def put_place(self):
				return self._put_place

		def trig_check(self, active_gs, case, word_lst):
				hand_lst = active_gs.get_hand_lst()
				trig_case = self.cmd_trigger_lst[0]
				if trig_case != case:
						return False
				else:
						word1 = word_lst[1]
						word2 = word_lst[2]
						cmd_check = [case, word1, word2]
						if cmd_check == self.cmd_trigger_lst:
								if self.in_hand_cond is None:
										return True
								elif (active_gs.hand_empty()) and (self.in_hand_cond == False):
										return True
								else:
										cond_match = False
										for obj in self.in_hand_lst:
												if active_gs.hand_check(obj):
														cond_match = True
										return cond_match == self.in_hand_cond

		def trigger(self, active_gs):
				active_gs.buffer(descript_dict[self.effect_desc])
				if self.game_ending is not None:
						active_gs.set_game_ending(self.game_ending)
				if self.give_or_take is not None:
						if self.give_or_take == 'give':
								active_gs.put_in_hand(self.give_item)
						else: # take option
								hand_lst = active_gs.get_hand_lst()
								hand_item = hand_lst[0]
								if not active_gs.hand_empty():
										self.put_place.append(hand_item)
										active_gs.hand_lst_remove_item(hand_item)

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
				room_obj_lst = room_obj.room_obj_lst
				if active_gs.hand_check(self):
						active_gs.buffer("You're already holding the " + self.full_name)
				else:
						if not active_gs.hand_empty(): # if hand not empty move item to backpack
								active_gs.backpack_lst_append_item(hand_lst[0])
								active_gs.hand_lst_remove_item(hand_lst[0])
						active_gs.hand_lst_append_item(self) # put taken item in hand
						active_gs.buffer("Taken")
						if self in backpack_lst: # if taken from backpack, remove from backpack
								active_gs.backpack_lst_remove_item(self)					
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
				self.open_state = open_state # is the jug uncapped?
				self._contains = contains # obj in the jug

		@property
		def contains(self):
				return self._contains

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
