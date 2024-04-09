# program: dark castle
# author: Tom Snellgrove
# module description: base class deffinition module


### import
from cleesh.class_std.invisible_class_def import Invisible


class Writing(Invisible):
	def __init__(self, name, full_name, root_name, descript_key):
		super().__init__(name)
		self._full_name = full_name # the object name presented to the player. Typical format = "Adj Noun". First character capitalized
		self._root_name = root_name # the one-word abreviation for the canonical adj_noun formulated name. e.g. rusty_key => key; not unique 
		self._descript_key = descript_key # key used to look up the object description in game_static_dict
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
	def read(self, gs, mode=None):
		""" Reads text found on an object.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		if self.is_writing():
			gs.io.buff_d(self.descript_key, self.full_name)
			return
		elif self.has_writing():
			gs.io.buffer(f"On the {self.full_name}, written in {self.writing.full_name}, you read: {gs.io.get_str(self.writing.name, self.writing.full_name)}.")
			return

	def examine(self, gs, mode=None):
		""" Writing-specific Examine.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		gs.io.buff_d(self.descript_key, self.full_name)
##		gs.io.buffer(f"The {self.full_name} reads as follows: {gs.io.get_str(self.name, self.full_name)}.")

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
	def has_cond(self, gs):
		return False

	def has_writing(self):
		return self.writing is not None

	def has_contain(self, gs):
		return False

	def disp_cond(self, gs):
		pass
		return 

	def disp_writing(self, gs):
		if self.has_writing():
			gs.io.buff_no_cr(f"On the {self.full_name} you see: {self.writing.full_name}. ")
			return 
		pass
		return 

	def disp_contain(self, gs):
		pass
		return

	def get_title_str(self, gs):
		return None


	# *** verb methods ***
	def examine(self, gs, mode=None):
		""" Describes an object.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		if self.get_title_str(gs) is not None:
			gs.io.buffer(self.get_title_str(gs))
		gs.io.buff_d(self.descript_key, self.full_name)
		if self.has_writing() or self.has_cond(gs) or self.has_contain(gs):
			gs.io.buff_cr()
			self.disp_cond(gs)
			self.disp_writing(gs)
			self.disp_contain(gs)
			gs.io.buff_cr()
		if self.get_title_str(gs) is not None and creature.is_contained(gs) and creature.get_contained_by(gs).in_reach_lst:
			creature.disp_in_reach(gs)
		return



