# program: dark castle v3.71
# name: Tom Snellgrove
# date: Aug 21, 2022
# description: class deffinition module for Creatures

### import
from static_gbl import descript_dict

### classes
class Map(object):
	def __init__(self, map_lst):
		self._map_lst = map_lst # list of room-pair dictionaries

## {'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall}

	# *** getters & setters ***
	@property
	def map_lst(self):
		return self._map_lst

	# *** simple obj methods ***
	def __repr__(self):
		return f"Object {self.name} is of class {type(self).__name__}"

	# *** complex obj methods ***
	def get_room_lst(self):
		room_lst = []
		for room_pair in self.map_lst:
			if room_pair['room_x'] not in room_lst:
				room_lst.append(room_pair['room_x'])
			if room_pair['room_y'] not in room_lst:
				room_lst.append(room_pair['room_y'])
		return room_lst
	
	def chk_obj_exist(self, obj): # checks for obj in floor_lst for each room in map
		return any(obj in room.floor_lst for room in self.get_room_lst())

	def chk_name_exist(self, name): # checks for obj.name in floor_lst for each room in map
		for room in self.get_room_lst():
			for obj in room.floor_lst:
				if obj.name == name:
					return True
		return False

	def	door_lst(self, room): # returns list of doors adjoining a given room
		return [room_pair['door'] for room_pair in self.map_lst 
				if (room == room_pair['room_x'] or room == room_pair['room_y']) and room_pair['door'] is not None]

	def room_doors_str(self, room): # returns string describing a room's doors and passages
		room_door_str = ""
		for room_pair in self.map_lst:
			if room_pair['room_x'] == room:
				if room_pair['door'] is None:
					room_door_str += f"There is a passage to the {room_pair['dir_x']}.\n"
				else:
					room_door_str += f"There is a {room_pair['door'].full_name} to the {room_pair['dir_x']}.\n"
			if room_pair['room_y'] == room:
				if room_pair['door'] is None:
					room_door_str += f"There is a passage to the {room_pair['dir_y']}.\n"
				else:
					room_door_str += f"There is a {room_pair['door'].full_name} to the {room_pair['dir_y']}.\n"
		return room_door_str


