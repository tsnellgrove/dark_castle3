# program: dark castle v3.79
# name: Tom Snellgrove
# date: Nov 22, 2023
# description: class deffinition module for io

### import
from dc3.data.static_gbl import static_dict

### classes
class IO(object):
	def __init__(self, name, dyn_dict, buff_dict):
		self._name = name # name of obj
		self._dyn_dict = dyn_dict # dict of non-static values that persist during game
		self._buff_dict = buff_dict # holds buffered output

	### setters & getters ###
	@property
	def name(self):
		return self._name

	@property
	def dyn_dict(self):
		return self._dyn_dict

	@dyn_dict.setter
	def dyn_dict(self, new_val):
		self._dyn_dict = new_val

	@property
	def buff_dict(self):
		return self._buff_dict

	@buff_dict.setter
	def buff_dict(self, new_val):
		self._buff_dict = new_val

	### description methods ###
	def get_dyn_dict(self, key):
		if key not in self.dyn_dict:
			raise KeyError("key does not exist in dict")
		return self.dyn_dict[key]

	def set_dyn_dict(self, key, val):
		self.dyn_dict[key] = val # adds key value pair if it does not exist
		return 

	def get_str(self, key, ref):
		"""Provides a string (usually a description) from dyn_dict and static_dict.
		"""
		try:
			return self.get_dyn_dict(key)
		except:
			try:
				return static_dict[key]
			except:
				return f"The {ref} is simply indescribable."

	### buffer methods ###
	def get_buff(self):
		return self.buff_dict['current_turn']

