# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: class deffinition module for GameState


### import


### classes
class GameState(object):
	def __init__(self, name, state_dict, map, io, score, end, hero):
		self._name = name
		self._state_dict = state_dict
		self._map = map
		self._io = io
		self._score = score
		self._end = end
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
	def end(self):
		return self._end

	@property
	def hero(self):
		return self._hero

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


