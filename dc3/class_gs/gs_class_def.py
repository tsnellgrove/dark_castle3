# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: class deffinition module for GameState


### import


### classes
class GameState(object):
	def __init__(self, name, state_dict, is_debug, map, io, score, end, hero):
		self._name = name
		self._state_dict = state_dict
		self._is_debug = is_debug
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
	def is_debug(self):
		return self._is_debug

	@is_debug.setter
	def is_debug(self, new_val):
		self._is_debug = new_val

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

	### room ###

##		def get_room(self):
##				return self._state_dict['room']

##		def set_room(self, value):
##				self._state_dict['room'] = value


	### obj representation (for printing) ###
	def __repr__(self):
		return f'Object { self._name } is of class { type(self).__name__ } '


