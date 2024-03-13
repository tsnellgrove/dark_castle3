# program: dark castle v3.83
# name: Tom Snellgrove
# date: Mar 13, 2024
# description: class deffinition module for GameState


### import


### classes
class GameState(object):
	def __init__(self, name, core, map, io, score, end):
		self._name = name
		self._core = core
		self._map = map
		self._io = io
		self._score = score
		self._end = end

	### setters & getters ###
	@property
	def name(self):
		return self._name

	@property
	def core(self):
		return self._core

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

	### obj representation (for printing) ###
	def __repr__(self):
		return f'Object { self._name } is of class { type(self).__name__ } '


