# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for io

### import
import random
from cleesh.data.static_gbl import static_dict

### classes
class IO(object):
	def __init__(self, name, dyn_dict, buff_str, last_input_str):
		self._name = name # name of obj
		self._dyn_dict = dyn_dict # dict of non-static values that persist during game
		self._buff_str = buff_str # holds buffered output
		self._last_input_str = last_input_str # holds previous turn's input

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
	def buff_str(self):
		return self._buff_str

	@buff_str.setter
	def buff_str(self, new_val):
		self._buff_str = new_val

	@property
	def last_input_str(self):
		return self._last_input_str

	@last_input_str.setter
	def last_input_str(self, new_val):
		self._last_input_str = new_val


	### check dict methods ###
	def chk_str_exist(self, key):
		if key not in self.dyn_dict and key not in static_dict:
			return False
		return True

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

	def get_str_nr(self, key):
		"""Provides a string (usually a description) from dyn_dict and static_dict. No ref / fail-over. Useful for cases where the calling method will provide alternate text of its own on dict lookup failure.
		"""
		try:
			return self.get_dyn_dict(key)
		except:
			return static_dict[key]
	
	def get_dict(self, dict_name):
		"""Returns a dict from within static_dict.
		"""
		return static_dict[dict_name]

	def get_dict_val(self, dict_name, dict_key):
		"""Returns a dictionary value from a dict within static_dict.
		"""
		return static_dict[dict_name][dict_key]

	def get_ddict_val(self, dict_name, dict_key1, dict_key2):
		"""Returns a  value from a double-dictionary within static_dict.
		"""
		return static_dict[dict_name][dict_key1][dict_key2]

	def get_lst(self, lst_name):
		"""Returns a list from a dict within static_dict.
		"""
		return static_dict[lst_name]


	### buffer methods ###
	def get_buff(self):
		return self.buff_str

	def reset_buff(self):
		self.buff_str = ""
		return

	def buffer(self, output_str):
		out_buff_old = self.buff_str
		out_buff_new = out_buff_old + "\n" + output_str + "\n"
		self.buff_str = out_buff_new
		return

	def buff_no_cr(self, output_str):
		out_buff_old = self.buff_str
		out_buff_new = out_buff_old + output_str
		self.buff_str = out_buff_new
		return
	
	def buff_cr(self):
		out_buff_old = self.buff_str
		out_buff_new = out_buff_old + "\n"
		self.buff_str = out_buff_new
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
	
	def buff_f(self, key):
		"""Buffer Fail. Buffers the text associated with the provided key attribute. Fails if key does not exist. Useful for cases where the calling method provides local try / except clauses.
		"""
		self.buffer(self.get_str_nr(key))
		return

	def buff_s(self, key):
		"""Buffer Silent. Buffers the text associated with the key attribute. Fails silently (passes) if key does not exist. Useful for cases where there may or may not be a description provided.
		"""
		try:
			self.buffer(self.get_str_nr(key))
		except:
			pass

	def buff_dbg(self, debug_str, gs):
		"""Buffers the debug_str attribute if the game is in debug mode. Otherwise, buffers a random error.
		"""
		if gs.core.is_debug:
			self.buffer(debug_str)
		else:
			self.buffer(static_dict['misc_err_' + str(random.randint(0, 4))])
