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
	
	def chk_obj_in_any_floor_lst(self, obj): # checks for obj in floor_lst for each room in map
		return any(obj in room.floor_lst for room in self.get_room_lst())

	def chk_name_in_any_floor_lst(self, name): # checks for obj.name in floor_lst for each room in map
		for room in self.get_room_lst():
			for obj in room.floor_lst:
				if obj.name == name:
					return True
		return False

