# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for GameState


### import
from cleesh.class_std.invisible_class_def import Invisible

### classes
# class GameState(object):
class GameState(Invisible):
	def __init__(self, name, core, map, io, score, end):
		super().__init__(name)
#		self._name = name
		self._core = core
		self._map = map
		self._io = io
		self._score = score
		self._end = end
		""" GameState class inherits from Invisible. It's only purpose is to hold, as attributes, 
		the other component game state class objs. 
		"""

	### setters & getters ###
#	@property
#	def name(self):
#		return self._name

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

#	### obj representation (for printing) ###
#	def __repr__(self):
#		return f'Object { self._name } is of class { type(self).__name__ } '


