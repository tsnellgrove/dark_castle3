# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for io

### import ###
from importlib import import_module
from cleesh.data.static_gbl import engine_static_dict
from cleesh.class_std.invisible_class_def import Invisible


### local functions ###
def get_game_dict(game_name):
	""" imports game_static_gbl() for game_name and returns game_static_dict"""
	import_str = f"cleesh.games.{game_name}.game_file.game_static_gbl"
	game_static_gbl = import_module(import_str)
	return game_static_gbl.game_static_dict

### classes ###
class IO(Invisible):
	def __init__(self, name, dyn_dict, buff_str, last_input_str, game_name, multi_count, vbosity_mode):
		super().__init__(name)
		self._dyn_dict = dyn_dict # dict of non-static values that persist during game
		self._buff_str = buff_str # holds buffered output
		self._last_input_str = last_input_str # holds previous turn's input
		self._game_name = game_name # name of the current game (also the path to the game)
		self._multi_count = multi_count # tracks the number of times a multiples action will run
		self._vbosity_mode = vbosity_mode # verbosity mode for output
		""" IO class inherits from Invisible. It abstracts all of the string calls to the games 
		various dictionaries (dynamic, engine, and game) and provides a raft of buffer funcions
		for game output. 
		"""

	### setters & getters ###
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

	@property
	def game_name(self):
		return self._game_name

	@game_name.setter
	def game_name(self, new_val):
		self._game_name = new_val

	@property
	def multi_count(self):
		return self._multi_count

	@multi_count.setter
	def multi_count(self, new_val):
		self._multi_count = new_val

	@property
	def vbosity_mode(self):
		return self._vbosity_mode

	@vbosity_mode.setter
	def vbosity_mode(self, new_val):
		self._vbosity_mode = new_val

	
	### check dict methods ###
	def chk_str_exist(self, key):
		if key not in self.dyn_dict and key not in engine_static_dict and key not in get_game_dict(self.game_name):
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
		"""Provides a string (usually a description) from dyn_dict, game_static_dict, and engine_static_dict. Includes failover to ref-based description.
		"""
		try:
			return self.get_dyn_dict(key)
		except:
			try:
				return get_game_dict(self.game_name)[key]
			except:
				try:
					return engine_static_dict[key]
				except:
					return f"The {ref} is simply indescribable."

	def get_str_nr(self, key, mode=None):
		"""Provides a string (usually a description) from dyn_dict, game_static_dict, and engine_static_dict. No ref / fail-over. Useful for cases where the calling method will provide alternate text of its own on dict lookup failure.
		"""
		if mode is None:
			mode = 'std'

		if mode == 'eng':
			try:
				return self.get_dyn_dict(key)
			except:
				return engine_static_dict[key]
		else:
			try:
				return self.get_dyn_dict(key)
			except:
				try:
					return get_game_dict(self.game_name)[key]
				except:
					return engine_static_dict[key]

	def get_dict(self, dict_name, mode=None):
		"""Returns a dict from within engine_static_dict or game_static_dict.
		"""
		if mode is None:
			mode = 'std'

		if mode == 'eng':
			return engine_static_dict[dict_name]
		else:
			try:
				return get_game_dict(self.game_name)[dict_name]
			except:
				return engine_static_dict[dict_name]

	def get_dict_val(self, dict_name, dict_key):
		"""Returns a dictionary value from a dict within engine_static_dict.
		"""
		return get_game_dict(self.game_name)[dict_name][dict_key]

	def get_ddict_val(self, dict_name, dict_key1, dict_key2):
		"""Returns a  value from a double-dictionary within engine_static_dict.
		"""
		return get_game_dict(self.game_name)[dict_name][dict_key1][dict_key2]

	def get_lst(self, lst_name, mode=None):
		"""Returns a list from a dict within engine_static_dict or game_static_dict.
		"""
		if mode is None:
			mode = 'std'

		if mode == 'eng':
			return engine_static_dict[lst_name]
		else:
			try:
				return get_game_dict(self.game_name)[lst_name]
			except:
				return engine_static_dict[lst_name]

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
		"""Buffer Description. Buffers the description (usually of an object) associated with the key attribute. The ref attribute is used to create a default description if none has been defined in engine_static_dict.
		"""
		self.buffer(self.get_str(key, ref))
		return


	def buff_d_no_cr(self, key, ref):
		"""Buffer Description. Buffers the description (usually of an object) associated with the key attribute. The ref attribute is used to create a default description if none has been defined in engine_static_dict. Provides no carriage return.
		"""
		self.buff_no_cr(self.get_str(key, ref))
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
			self.buffer(gs.core.hero.full_name + engine_static_dict['misc_err_' + str(gs.core.cleesh_rand(0, 4))])
