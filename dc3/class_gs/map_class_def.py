# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for Map


### module vars
room_key_lst = [['room_x', 'dir_x', 'room_y'], ['room_y', 'dir_y', 'room_x']] # list of key_lst for a given room_pair

### classes
class Map(object):
	def __init__(self, name, hero_loc, map_lst):
		self._name = name
		self._hero_loc = hero_loc # the current location of the player's character (previously searched for)
		self._map_lst = map_lst # list of room_pair dicts; 
				# format == [{'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall}]

	# *** getters & setters ***
	@property
	def name(self):
		return self._name
	
	@property
	def hero_loc(self):
		return self._hero_loc

	@hero_loc.setter
	def hero_loc(self, new_val):
		self._hero_loc = new_val

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

	def chk_obj_exist(self, obj, gs, lst=None):
		""" Evaluates whether object obj exists in any room in map_lst
		"""
		if lst == None:
			lst = self.get_room_lst()

		for element in lst:
			if element == obj:
				return True
			if element.is_receptacle():
				if self.chk_obj_exist(obj, gs, element.get_contain_lst(gs)):
					return True
		return False


##	def chk_obj_exist(self, obj): # how this method previously worked
##		""" Evaluates whether object obj exists in floor_lst for any room in map_lst
##		"""
##		return any(obj in room.floor_lst for room in self.get_room_lst())


	def chk_name_exist(self, name):
		""" Evaluates whether an obj with obj.name == name exists in floor_lst for any room in map_lst
		"""
		return any(obj.name == name for room in self.get_room_lst() for obj in room.floor_lst)

	def get_obj_from_name(self, name_str, gs): # room = hero_room ; search limited to room floor
		room = self.get_hero_rm(gs)
		for obj in room.floor_lst:
			if obj.name == name_str:
				return obj
		raise ValueError('An obj with name name_str was not found in hero_rm.')

	def get_obj_room(self, obj, gs, lst=None):
		""" Returns the room that contains obj
		"""
		room_lst = self.get_room_lst()
		if lst == None:
			lst = room_lst

		for element in lst:
			if element == obj:
				if lst == room_lst: # is this possible for default case??
					return element # is this possible for default case??
				return True
			if element.is_receptacle():
				if self.get_obj_room(obj, gs, element.get_contain_lst(gs)):
					if element.is_room():
						return element
					return True
		if lst == room_lst:
			raise ValueError(f"{obj.full_name} not found.")

	def get_hero_rm(self, gs):
		""" Returns the room that gs.core.hero is currently in
		"""
		for room in self.get_room_lst():
			if gs.core.hero in room.floor_lst:
				return room
			for room_obj in room.floor_lst:
				if room_obj.is_seat() and room_obj.chk_contain_item(gs.core.hero):
					return room
		raise ValueError(f"{gs.core.hero.name} not found.")

	def chk_obj_in_creature_inv(self, obj, gs, lst=None):
		""" Evaluates whether obj is in a creature's inventory; returns evaluation & creature
		"""
		if lst == None:
			lst = self.get_room_lst()

		if obj.is_creature():
			return False, None

		for element in lst:
			if element == obj:
				return True, None
			if element.is_receptacle():
				exist, creature_obj = self.chk_obj_in_creature_inv(obj, gs, element.get_contain_lst(gs))
				if exist:
					if element is not None and element.is_creature():
						return True, element
					if element.is_room() and creature_obj is None:
						return False, None
					elif element.is_room():
						return creature_obj.is_creature(), creature_obj
		return False, None	


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

	def chk_valid_dir(self, room, dir):
		""" Evaluates whether going direction dir from room is viable.
		"""
		return any(room_pair[room_lst[0]] == room and room_pair[room_lst[1]] == dir
				for room_pair in self.map_lst for room_lst in room_key_lst)

	def get_door(self, room, dir):
		""" Returns room_pair['door'] given a starting room and a direction where room_pair['door'] can be either a door object or a string describing the open passage. Is intended to be run after chk_valid_dir() and will produce an error if run on an invalid route.
		
		I initially refactored this method to a list comprehension and returned the 0th member of the list... but this seemed out of keeping with the zen of list comprehension. Also, the nested-for-loop version was more efficient as it returned as soon as it found a match.
		"""
		for room_pair in self.map_lst:
			for room_lst in room_key_lst:
				if room_pair[room_lst[0]] == room and room_pair[room_lst[1]] == dir:
					return room_pair['door']
		raise ValueError(f"There is no 'door' value associated with going {dir} from room {room}. This must not be a valid route.")

	def get_next_room(self, room, dir):
		""" Returns the destination room (room_pair['room_y']) given a starting room and a direction. Is intended to be run after chk_valid_dir() and will produce an error if run on an invalid route.
		"""
		for room_pair in self.map_lst:
			for room_dir in room_key_lst:
				if room_pair[room_dir[0]] == room and room_pair[room_dir[1]] == dir:
					return room_pair[room_dir[2]]
		raise ValueError(f"There is no 'room_y' value associated with going {dir} from room {room}. This must not be a valid route.")

	
