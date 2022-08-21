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

	def __repr__(self):
		return f"Object {self.name} is of class {type(self).__name__}"


