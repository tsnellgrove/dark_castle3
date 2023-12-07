# program: dark castle v3.79
# name: Tom Snellgrove
# date: Nov 22, 2023
# description: class deffinition module for io

### import
import random
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
		"""Provides a string (usually a description) from dyn_dict and static_dict. Includes failover to ref-based description.
		"""
		try:
			return self.get_dyn_dict(key)
		except:
			try:
				return static_dict[key]
			except:
				return f"The {ref} is simply indescribable."

	def get_str_no_ref(self, key):
			"""Provides a string (usually a description) from dyn_dict and static_dict. No ref / fail-over. Useful for cases where the calling method will provide alternate text of its own on dict lookup failure.
			"""
			try:
				return self.get_dyn_dict(key)
			except:
				return static_dict[key]
				

	### buffer methods ###
	def get_buff(self):
		return self.buff_dict['current_turn']

	def reset_buff(self):
		self.buff_dict['current_turn'] = ""
		return

	def buffer(self, output_str):
		out_buff_old = self.buff_dict['current_turn']
		out_buff_new = out_buff_old + "\n" + output_str + "\n"
		self.buff_dict['current_turn'] = out_buff_new
		return

	def buff_no_cr(self, output_str):
		out_buff_old = self.buff_dict['current_turn']
		out_buff_new = out_buff_old + output_str
		self.buff_dict['current_turn'] = out_buff_new
		return
	
	def buff_cr(self):
		out_buff_old = self.buff_dict['current_turn']
		out_buff_new = out_buff_old + "\n"
		self.buff_dict['current_turn'] = out_buff_new
		return

	def buff_d(self, key, ref):
		"""Buffer Description. Buffers the description (usually of an object) associated with the key attribute. The ref attribute is used to create a default description if none has been defined in static_dict.
		"""
		self.buffer(self.get_str(key, ref))
		return

	def buff_e(self, key):
		"""Buffer Event. Buffers the event description associated with the key attribute. Unlike buff_d(), there is no ref attribute for the default description.
		"""
		self.buffer(self.get_str(key, 'experience'))
		return
	
	def buff_a(self, key):
		"""Buffer Auto-Gen. Buffers the description associated with the provided auto-gen key attribute. Fails if key does not exist - which allows local try / except defaults built into the calling method to be expressed.
		"""
		self.buffer(self.get_str_no_ref(key))
		return

	def buff_s(self, key):
		"""Buffer Silent. Buffers the description associated with the key attribute. Fails silently (passes) if key does not exist. Useful for cases where there may or may not be a description provided.
		"""
		try:
			self.buffer(self.get_str_no_ref(key))
		except:
			pass

	def buff_dbg(self, debug_str, debug):
		"""Buffers the debug_str attribute if the game is in debug mode. Otherwise, buffers a random error.
		"""
		if debug:
			self.buffer(debug_str)
		else:
			self.buffer(static_dict['misc_err_' + str(random.randint(0, 4))])
