# program: dark castle v3.64
# name: Tom Snellgrove
# date: June 7, 2022
# description: class deffinition module for GameState


### import
from static_gbl import descript_dict, static_dict
from shared_class_func import obj_lst_to_str


### local functions


### classes
class GameState(object):
		def __init__(self, name, dynamic_desc_dict, map_dict, points_earned_dict, static_obj_dict, state_dict, universal_mach_lst, room_lst):
				self._name = name
				self._dynamic_desc_dict = dynamic_desc_dict
				self._map_dict = map_dict
				self._points_earned_dict = points_earned_dict
				self._static_obj_dict = static_obj_dict
				self._state_dict = state_dict
				self._universal_mach_lst = universal_mach_lst
				self._room_lst = room_lst

		### setters & getters ###

		@property
		def universal_mach_lst(self):
				return self._universal_mach_lst

		@property
		def room_lst(self):
				return self._room_lst

		### descriptions ###
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

		### movement ###
		def is_valid_map_direction(self, room_obj, direction):
				return direction in self._map_dict[room_obj.name]

		def get_next_room(self, room_obj, direction):
				next_room = self._map_dict[room_obj.name][direction]
				return next_room

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
		def get_backpack_lst(self):
				return self._state_dict['backpack']

		def backpack_lst_append_item(self, item):
				self._state_dict['backpack'].append(item)

		def backpack_lst_remove_item(self, item):
				self._state_dict['backpack'].remove(item)

		### hand ###

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

		### worn ###
		def get_worn_lst(self):
				return self._state_dict['worn']

		def worn_lst_append_item(self, item):
				self._state_dict['worn'].append(item)

		def worn_lst_remove_item(self, item):
				self._state_dict['worn'].remove(item)

		def clothing_type_worn(self, item):
				type_match = False
				worn_lst = self.get_worn_lst()
				for garment in worn_lst:
						if item.clothing_type == garment.clothing_type:
								type_match = True
				return type_match

		### static obj ###
		def get_static_obj(self, static_key):
				if static_key not in self._static_obj_dict:
						raise KeyError("key does not exist in dict")
				else:
						return self._static_obj_dict[static_key]

		### room ###
		def get_room(self):
				return self._state_dict['room']

		def set_room(self, value):
				self._state_dict['room'] = value

		### buffer ###
		def get_buff(self):
				return self._state_dict['out_buff']

		def buffer(self, output_str):
				out_buff_old = self._state_dict['out_buff']
				out_buff_new = out_buff_old + "\n" + output_str + "\n"
				self._state_dict['out_buff'] = out_buff_new

		def reset_buff(self):
				self._state_dict['out_buff'] = ""

		### inventory ###
		def inventory(self):
				hand_obj_lst = self.get_hand_lst()
				hand_str = obj_lst_to_str(hand_obj_lst)
				self.buffer("In your hand you are holding: " + hand_str)

				backpack_obj_lst = self.get_backpack_lst()
				backpack_str = obj_lst_to_str(backpack_obj_lst)
				self.buffer("In your backpack you have: " + backpack_str)

				worn_obj_lst = self.get_worn_lst()
				worn_str = obj_lst_to_str(worn_obj_lst)
				self.buffer("Special garments you are wearing: " + worn_str)

		### scope lists ###
		def scope_lst(self):
				room_obj = self.get_room()
				hand_lst = self.get_hand_lst()
				backpack_lst = self.get_backpack_lst()
				worn_lst = self.get_worn_lst()
				universal_lst = self.get_static_obj('universal')
				room_obj_lst = room_obj.room_obj_lst
				features_lst = room_obj.features
				scope_lst = (room_obj_lst + hand_lst + backpack_lst 
								+ worn_lst + universal_lst + features_lst)
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

		def room_mach_lst(self):
				room_mach_lst = []
				room_obj = self.get_room()
				scope_lst = self.scope_lst() + room_obj.invis_obj_lst
				for obj in scope_lst:
						if hasattr(obj, 'trigger_type'):
								room_mach_lst.append(obj)
						if hasattr(obj, 'creature_state'):
								if obj.mach_obj_lst != None:
										room_mach_lst.extend(obj.mach_obj_lst)
				return room_mach_lst

		def mach_obj_lst(self):
				mach_obj_lst = self.room_mach_lst()
				mach_obj_lst.extend(self.universal_mach_lst)
				return mach_obj_lst

		def auto_in_alert_scope(self, obj):
				return obj in self.room_mach_lst()

		def obj_exist(self, obj):
				obj_in_world = False
				for room in self.room_lst:
						if obj in room.room_obj_lst:
								obj_in_world = True
				return obj_in_world

		def obj_name_exist(self, name):
				name_in_world = False
				for room in self.room_lst:
						for obj in room.room_obj_lst:
								if obj.name == name:
										name_in_world = True
				return name_in_world

		### obj representation (for printing) ###
		def __repr__(self):
				return f'Object { self._name } is of class { type(self).__name__ } '


