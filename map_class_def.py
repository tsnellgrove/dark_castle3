# program: dark castle v3.71
# name: Tom Snellgrove
# date: Aug 21, 2022
# description: class deffinition module for Creatures

### import


### module vars
room_key_lst = [['room_x', 'dir_x', 'room_y'], ['room_y', 'dir_y', 'room_x']]

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
		""" Returns a de-duped list of all rooms in map_lst
		"""
		room_lst = []
		[room_lst.append(room_pair[room[0]]) for room_pair in self.map_lst for room in room_key_lst
				if room_pair[room[0]] not in room_lst]
		return room_lst
	
	def chk_obj_exist(self, obj):
		""" Evaluates whether object obj exists in floor_lst for any room in map_lst
		"""
		return any(obj in room.floor_lst for room in self.get_room_lst())

	def chk_name_exist(self, name):
		""" Evaluates whether an obj with obj.name == name exists in floor_lst for any room in map_lst
		"""
		return any(obj.name == name for room in self.get_room_lst() for obj in room.floor_lst)

	def	get_door_lst(self, room):
		""" Returns a list of doors adjoining a given room
		"""
		return [room_pair['door'] for room_pair in self.map_lst 
				if (room == room_pair['room_x'] or room == room_pair['room_y']) and not isinstance(room_pair['door'], str)]

	def get_neighbor_count(self, room):
		""" Provide a count of rooms that are connected neighbors of a given room
		"""
		neighbor_count = 0
		for room_pair in self.map_lst:
			for room_lst in room_key_lst:
				if room_pair[room_lst[0]] == room:
					neighbor_count += 1
		return neighbor_count

	def get_door_str(self, room):
		""" Returns a string describing a room's doors and passages. This in turn will be reported by room.examine as the room condition.
		
		Over 30 years ago, my engineering professor for C (before the ++) declared to the class: "No matter what you code, and no moatter what language you code it in, you will always spend 90% of your time and effort on user interface". You would think that in the case of a text adventure he'd be wrong...  but he wasn't.
		"""
		room_door_str = "There is "
		room_count = self.get_neighbor_count(room)
		clause_count = 0
		for room_pair in self.map_lst:
			for room_lst in room_key_lst:
				if room_pair[room_lst[0]] == room:
					if isinstance(room_pair['door'], str):
						room_door_str += f"a {room_pair['door']} to the {room_pair[room_lst[1]]}"
					else:
						room_door_str += f"a {room_pair['door'].full_name} to the {room_pair[room_lst[1]]}"
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
			for room_dir in room_key_lst:
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
			for room_dir in room_key_lst:
				if room_pair[room_dir[0]] == room and room_pair[room_dir[1]] == dir:
					return room_pair[room_dir[2]]

