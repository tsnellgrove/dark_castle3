# program: dark castle v3.71
# name: Tom Snellgrove
# date: Aug 21, 2022
# description: class deffinition module for Creatures

### import


### module vars
room_dir_key_lst = [['room_x', 'dir_x', 'room_y'], ['room_y', 'dir_y', 'room_x']]

### classes
class Map(object):
	def __init__(self, map_lst):
		self._map_lst = map_lst # list of room_pair dicts
				# format == {'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall}

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
			for room in room_dir_key_lst:
				if room_pair[room[0]] not in room_lst:
					room_lst.append(room_pair[room[0]])
#			if room_pair['room_x'] not in room_lst:
#				room_lst.append(room_pair['room_x'])
#			if room_pair['room_y'] not in room_lst:
#				room_lst.append(room_pair['room_y'])
		print(room_lst)
		return room_lst
	
	def chk_obj_exist(self, obj): # checks for obj in floor_lst for each room in map
		return any(obj in room.floor_lst for room in self.get_room_lst())

	def chk_name_exist(self, name): # checks for obj.name in floor_lst for each room in map
		for room in self.get_room_lst():
			for obj in room.floor_lst:
				if obj.name == name:
					return True
		return False

	def	get_door_lst(self, room): # returns list of doors adjoining a given room
		return [room_pair['door'] for room_pair in self.map_lst 
				if (room == room_pair['room_x'] or room == room_pair['room_y']) and not isinstance(room_pair['door'], str)]

	def get_room_count(self, room):
		room_count = 0
		for room_pair in self.map_lst:
			if room_pair['room_x'] == room:
				room_count += 1
			if room_pair['room_y'] == room:
				room_count += 1
		return room_count

	def get_door_str(self, room): # returns string describing a room's doors and passages
		room_door_str = "There is "
		room_count = self.get_room_count(room)
		clause_count = 0
		for room_pair in self.map_lst:
			if room_pair['room_x'] == room:
				if isinstance(room_pair['door'], str):
					room_door_str += f"a {room_pair['door']} to the {room_pair['dir_x']}"
				else:
					room_door_str += f"a {room_pair['door'].full_name} to the {room_pair['dir_x']}"
				clause_count +=1
				if clause_count == room_count:
					break
				if clause_count == room_count - 1 and clause_count ==1:
					room_door_str += " and "
				elif clause_count == room_count - 1:
					room_door_str += ", and "
				else:
					room_door_str += ", "
			if room_pair['room_y'] == room:
				if isinstance(room_pair['door'], str):
					room_door_str += f"a {room_pair['door']} to the {room_pair['dir_y']}"
				else:
					room_door_str += f"a {room_pair['door'].full_name} to the {room_pair['dir_y']}"
				clause_count +=1
				if clause_count == room_count:
					break
				if clause_count == room_count - 1 and clause_count ==1:
					room_door_str += " and "
				elif clause_count == room_count - 1:
					room_door_str += ", and "
				else:
					room_door_str += ", "
		room_door_str += "."
		return room_door_str

	def is_valid_dir(self, room, dir):
		for room_pair in self.map_lst:
			for room_dir in room_dir_key_lst:
				if room_pair[room_dir[0]] == room and room_pair[room_dir[1]] == dir:
					return True
		return False

	def get_door(self, room, dir):
		for room_pair in self.map_lst:
			if room_pair['room_x'] == room and room_pair['dir_x'] == dir:
				return room_pair['door']
			if room_pair['room_y'] == room and room_pair['dir_y'] == dir:
				return room_pair['door']

	def get_next_room(self, room, dir):
		for room_pair in self.map_lst:
			for room_dir in room_dir_key_lst:
				if room_pair[room_dir[0]] == room and room_pair[room_dir[1]] == dir:
					return room_pair[room_dir[2]]

