# program: dark castle v3.77
# name: Tom Snellgrove
# date: May 22, 2023
# description: class deffinition module for Creatures


### module vars
room_key_lst = [['room_x', 'dir_x', 'room_y'], ['room_y', 'dir_y', 'room_x']] # list of key_lst for a given room_pair

### classes
class Map(object):
	def __init__(self, map_lst):
		self._map_lst = map_lst # list of room_pair dicts; 
				# format == [{'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall}]
		""" *** Module Documentation ***

		Overview:
			Stores the over-arching map of Dark Castle and provides methods for accessing and updating map info. Contains room_pairs and doors.

		Implementation Detail:
			map_lst is stored in GameState (rather than being a constant declared in the class) to allow for major terrain changes. For example, after a major cave-in the room description might change dramatically and three new passages might open up. One could make all these updates to the original room - but it would be far easier just to redirect to a new room. The most famous example of this behavior is the magic pencil used at the end of The Lurking Horror / Enchanter.
		
		Historic Note:
			Before refactoring, map_dict was an attribute of GameState and was a dictionary-of-dictionaries that was keyed off room and direction and returned next_room ast a value. Room.floor_lst contained doors and Room had an attribute, door_dict, that was keyed off direction and returned a door as its value. 
			
			This worked fine but had a few logistical and philosphical flaws. Logistically, GameState was an ugly monolith. It had *way* too many methods. It was hard to keep track of them all. So it was high time to apply OOP to the operational aspects of the game and organize game state information into classes with methods that would then become attributes of GameState. Map became the first such operational object, in advance of migrating Burt to a Creature. The intention is to do the same for the rest of the operational capabilities in Game State.
			
			The other issue was more about data design philosophy... There was a GameState map_dict entry for room_x that pointed to room_y, and a map_dict entry for room_y that pointed to room_x... but they were independent entries that seemed to imply that the connection was arbitrary. There were also separate door_dict entries for both room_x and room_y that each pointed to the same door that was between them - but again were in theory entirely independent. Lastly, the same door was in floor_lst of both rooms. As my theory of node hierarchy matured, it seemed "right" that there should be one and only one instance of every object... so why was there two of every door?
			
			I considered making doors 'smart' and allowing them know about the rooms on either side of them. This was simple but it broke my rule that 'objects only know what they contain'. Also, it obviated the need for a central map, and I was convinced that a human-readible master map would be a valuable design aid. I even contemplated breaking doors in half... each side of the door would be contained in a given room and link back to a 'master door' that would maintain open and locked state for both. This had the attrictive capability of showing different features on each side of a door... but it seemed over-engineered and, again, eliminated the central map.
			
			The eventual solution was the concept of 'room pairs' - the idea that the whole map is essentially comprised of pairs of rooms that are connected. And that in all but a few exceptional cases, if room_x leads to room_y, then room_y will lead to room_x - and that the door or passage between them will be contained uniquely and consistently within that pair. Based on this thinking I created a custom data structure: a list of room_pair dictionaries (I used a dictionary rather than a list for the sake of making the structure self-documenting). The structure requires a lot of custom methods to access - but this turned out to be a bit of a fun master class in list comprehension. Doors now appear once and only once in map_lst. Of course, now rooms appear multiple times, but for some reason this doesn't bother me. YMMV.
		"""

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

	def chk_obj_exist_recursive(self, obj, lst):
		""" Recursive approach
		"""
		for element in lst:
			if element == obj:
				return True
#			elif isinstance(element, list):
			elif element.is_receptacle:
				return self.chk_obj_exist_recursive(obj, element.get_contain_lst())
#				return self.chk_obj_exist_recursive(obj, element)
#		return False

	def chk_obj_exist(self, obj):
		""" Evaluates whether object obj exists in floor_lst for any room in map_lst
		"""
#		return any(obj in room.floor_lst for room in self.get_room_lst())
		for room in self.get_room_lst():
			if obj in room.floor_lst:
				return True
			self.chk_obj_exist_recursive(obj, room.floor_lst)
#			for floor_obj in room.floor_lst:
#				if floor_obj.chk_contain_item(obj):
#					return True
		return False

	def chk_name_exist(self, name):
		""" Evaluates whether an obj with obj.name == name exists in floor_lst for any room in map_lst
		"""
		return any(obj.name == name for room in self.get_room_lst() for obj in room.floor_lst)

	def get_obj_room(self, obj):
		""" Returns the room that contains obj
		"""
		for room in self.get_room_lst():
			if obj in room.floor_lst:
				return room
			for floor_obj in room.floor_lst:
				if floor_obj.chk_contain_item(obj):
					return room
		raise ValueError(f"{obj.full_name} not found.")

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

	def get_obj_room(self, obj): # rename to get_creature_room ??? 
			""" Returns the room that obj is currently in (so long as it is in room.floor_lst or seat.contain)
			"""
			for room in self.get_room_lst():
				if obj in room.floor_lst:
					return room
				for room_obj in room.floor_lst:
#					if room_obj.is_seat() and room_obj.chk_contain_item(obj):
					if room_obj.chk_contain_item(obj):
						return room
			raise ValueError(f"{obj.full_name} not found.")

	
