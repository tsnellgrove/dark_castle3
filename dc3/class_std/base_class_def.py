# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: base class deffinition module


### import
from dc3.data.static_gbl import static_dict
from dc3.class_std.invisible_class_def import Invisible


class Writing(Invisible):
	def __init__(self, name, full_name, root_name, descript_key):
		super().__init__(name)
		self._full_name = full_name # the object name presented to the player. Typical format = "Adj Noun". First character capitalized
		self._root_name = root_name # the one-word abreviation for the canonical adj_noun formulated name. e.g. rusty_key => key; not unique 
		self._descript_key = descript_key # the key used to look up the object description in static_dict
		""" Writing objects represent text which can be read().
		"""

	# *** getters & setters ***
	@property
	def full_name(self):
		return self._full_name

	@property
	def root_name(self):
		return self._root_name

	@property
	def descript_key(self):
		return self._descript_key

	@descript_key.setter
	def descript_key(self, new_descript):
		self._descript_key = new_descript

	# *** class identity methods ***
	def is_invisible(self):
		return False

	def is_writing(self):
		return True
	
	# *** verb methods ***
	def read(self, active_gs, mode=None):
		""" Reads text found on an object.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		active_gs.io.buff_d(self.descript_key, self.full_name)
		return


class ViewOnly(Writing):
	def __init__(self, name, full_name, root_name, descript_key, writing):
		super().__init__(name, full_name, root_name, descript_key)
		self._writing = writing # Writing obj associated with the ViewOnly object; writing = None if there is nothing to read on the obj
		""" ViewOnly objects can be examined and text on them can be read, but they can not interacted with in any other way
		"""

	# *** getters & setters ***
	@property
	def writing(self):
		return self._writing

	# *** class identity methods ***
	def is_writing(self):
		return False
	
	def is_viewonly(self):
		return True

	# *** universal display methods ***
	def has_cond(self, active_gs):
		return False

	def has_writing(self):
		return self.writing is not None

	def has_contain(self, active_gs):
		return False

	def disp_cond(self, active_gs):
		pass
		return 

	def disp_writing(self, active_gs):
		if self.has_writing():
			active_gs.io.buff_no_cr(f"On the {self.full_name} you see: {self.writing.full_name}. ")
			return 
		pass
		return 

	def disp_contain(self, active_gs):
		pass
		return

	def get_title_str(self, active_gs):
		return None


	# *** verb methods ***
	def examine(self, active_gs, mode=None):
		""" Describes an object.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		if self.get_title_str(active_gs) is not None:
			active_gs.io.buffer(self.get_title_str(active_gs))
		active_gs.io.buff_d(self.descript_key, self.full_name)
		if self.has_writing() or self.has_cond(active_gs) or self.has_contain(active_gs):
			active_gs.io.buff_cr()
			self.disp_cond(active_gs)
			self.disp_writing(active_gs)
			self.disp_contain(active_gs)
			active_gs.io.buff_cr()
		if self.get_title_str(active_gs) is not None and creature.is_contained(active_gs) and creature.get_contained_by(active_gs).in_reach_lst:
			creature.disp_in_reach(active_gs)
		return



