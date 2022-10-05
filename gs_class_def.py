# program: dark castle v3.72
# name: Tom Snellgrove
# date: Sept 10, 2022
# description: class deffinition module for GameState


### import
from static_gbl import descript_dict, static_dict

### local functions
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
		def __init__(self, name, dyn_descript_dict, points_earned_dict, static_obj_dict, state_dict, universal_mach_lst, map, hero):
				self._name = name
				self._dyn_descript_dict = dyn_descript_dict
				self._points_earned_dict = points_earned_dict
				self._static_obj_dict = static_obj_dict
				self._state_dict = state_dict
				self._universal_mach_lst = universal_mach_lst
				self._map = map
				self._hero = hero

		### setters & getters ###

		@property
		def universal_mach_lst(self):
				return self._universal_mach_lst

		@property
		def room_lst(self):
				return self._room_lst

		@property
		def map(self):
				return self._map

		@property
		def hero(self):
				return self._hero

		### descriptions ###
		def get_dyn_descript_dict(self, descript_key):
				if descript_key not in self._dyn_descript_dict:
						raise KeyError("key does not exist in dict")
						return 
				return self._dyn_descript_dict[descript_key]

		def set_dyn_descript_dict(self, descript_key, descript_val):
				self._dyn_descript_dict[descript_key] = descript_val # adds key value pair if it does not exist
				return 

		### score ###
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

		### game moves counter ###
		def move_inc(self):
				self._state_dict['move_counter'] += 1

		def move_dec(self):
				self._state_dict['move_counter'] -= 1

		def get_moves(self):
				return self._state_dict['move_counter']

		### game ending ###
		def get_end_of_game(self):
				return self._state_dict['end_of_game']

		def set_end_of_game(self, value):
				self._state_dict['end_of_game'] = value

		def get_game_ending(self):
				return self._state_dict['game_ending']

		def set_game_ending(self, value):
				self._state_dict['game_ending'] = value

		### backpack ###
#		def get_backpack_lst(self):
#				return self._state_dict['backpack']

#		def backpack_lst_append_item(self, item):
#				self._state_dict['backpack'].append(item)

#		def backpack_lst_remove_item(self, item):
#				self._state_dict['backpack'].remove(item)

		### hand ###

#		def get_hand_lst(self):
#				return self._state_dict['hand']

#		def hand_empty(self):
#				return len(self.get_hand_lst()) == 0

#		def hand_check(self, obj):
#				return obj in self.get_hand_lst()

#		def hand_lst_append_item(self, item):
#				self._state_dict['hand'].append(item)

#		def hand_lst_remove_item(self, item):
#				self._state_dict['hand'].remove(item)

#		def weapon_in_hand(self):
#				hand_lst = self.get_hand_lst()
#				return bool(hand_lst) and hand_lst[0].is_weapon()

#		def put_in_hand(self, new_item):
#				if not self.hand_empty():
#						hand_lst = self.get_hand_lst()
#						hand_item = hand_lst[0]
#						self.backpack_lst_append_item(hand_item)
#						self.hand_lst_remove_item(hand_item)
#				self.hand_lst_append_item(new_item)

		### worn ###
#		def get_worn_lst(self):
#				return self._state_dict['worn']

		def worn_lst_append_item(self, item):
				self._state_dict['worn'].append(item)

		def worn_lst_remove_item(self, item):
				if item.remove_descript is not None:
						self.buffer(descript_dict[item.remove_descript])
				self._state_dict['worn'].remove(item)

#		def clothing_type_worn(self, item):
#				type_match = False
#				worn_lst = self.get_worn_lst()
#				for garment in worn_lst:
#						if item.clothing_type == garment.clothing_type:
#								type_match = True
#				return type_match

		### static obj ###
		def get_static_obj(self, static_key):
				if static_key not in self._static_obj_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._static_obj_dict[static_key]

		### room ###
#		def get_hero_room(self):
		def get_room(self):
				""" Returns the room that active_gs.hero is currently in
				"""
				for room in self.map.get_room_lst():
						if self.hero in room.floor_lst:
								return room
				raise ValueError(f"{self.hero.name} not found.")
		
##		def get_room(self):
##				return self._state_dict['room']

##		def set_room(self, value):
##				self._state_dict['room'] = value

		### buffer ###
		def get_buff(self):
				return self._state_dict['out_buff']

		def buffer(self, output_str):
				out_buff_old = self._state_dict['out_buff']
				out_buff_new = out_buff_old + "\n" + output_str + "\n"
				self._state_dict['out_buff'] = out_buff_new

		def reset_buff(self):
				self._state_dict['out_buff'] = ""

		### inventory ### (to be moved to Creature method)
#		def inventory(self):
#				self.buffer(descript_dict['burt'])
#				hand_lst = self.get_hand_lst()
#				hand_str = obj_lst_to_str(hand_lst)
#				self.buffer("In your hand you are holding: " + hand_str)

#				backpack_obj_lst = self.get_backpack_lst()
#				backpack_str = obj_lst_to_str(backpack_obj_lst)
#				self.buffer("In your backpack you have: " + backpack_str)

#				worn_obj_lst = self.get_worn_lst()
#				worn_str = obj_lst_to_str(worn_obj_lst)
#				self.buffer("Special garments you are wearing: " + worn_str)

		### obj representation (for printing) ###
		def __repr__(self):
				return f'Object { self._name } is of class { type(self).__name__ } '


