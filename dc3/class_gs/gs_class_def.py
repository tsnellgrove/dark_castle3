# program: dark castle v3.80
# name: Tom Snellgrove
# date: Jan 7, 2024
# description: class deffinition module for GameState


### import


### classes
class GameState(object):
#	def __init__(self, name, points_earned_dict, state_dict, map, io, score, hero):
	def __init__(self, name, state_dict, map, io, score, hero):
		self._name = name
#		self._points_earned_dict = points_earned_dict
		self._state_dict = state_dict
		self._map = map
		self._io = io
		self._score = score
		self._hero = hero

	### setters & getters ###

	@property
	def state_dict(self):
		return self._state_dict

	@state_dict.setter
	def state_dict(self, new_state):
		self._state_dict = new_state

	@property
	def map(self):
		return self._map

	@property
	def io(self):
		return self._io

	@property
	def score(self):
		return self._score

	@property
	def hero(self):
		return self._hero

	### score ###
#	def get_points_earned_state(self, score_key):
#		if score_key not in self._points_earned_dict:
#			raise KeyError("key does not exist in dict")
#		else:
#			return self._points_earned_dict[score_key]

#	def set_points_earned_state(self, score_key, value):
#		if score_key not in self._points_earned_dict:
#			raise KeyError("key does not exist in dict")
#		else:
#			self._points_earned_dict[score_key] = value

	def update_score(self, points):
		self._state_dict['score'] += points 

	def get_score(self):
		return self._state_dict['score']

	def print_score(self):
		output1 = ("Your score is now " + str(self.get_score()))
		output2 = (" out of " + str(self.io.get_str_nr('max_score')))	
		self.io.buffer(output1 + output2)

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

	### debug mode ###

	def is_dbg(self):
		return self.state_dict['debug']

	### room ###

##		def get_room(self):
##				return self._state_dict['room']

##		def set_room(self, value):
##				self._state_dict['room'] = value


	### obj representation (for printing) ###
	def __repr__(self):
		return f'Object { self._name } is of class { type(self).__name__ } '


