# program: dark castle v3.79
# name: Tom Snellgrove
# date: Nov 22, 2023
# description: class deffinition module for io

### classes
class IO(object):
	def __init__(self, name, dyn_dict):
		self._name = name # name of obj
		self._dyn_dict = dyn_dict # dict of non-static values that persist during game

	@property
	def name(self):
		return self._name

	@property
	def dyn_dict(self):
		return self._dyn_dict

	@dyn_dict.setter
	def dyn_dict(self, new_val):
		self._dyn_dict = new_val

	def get_dyn_dict(self, key):
		if key not in self.dyn_dict:
			raise KeyError("key does not exist in dict")
		return self.dyn_dict[key]

	def set_dyn_dict(self, key, val):
		self.dyn_dict[key] = val # adds key value pair if it does not exist
		return 