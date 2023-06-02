# program: dark castle v3.77
# name: Tom Snellgrove
# date: May 22, 2023
# description: provides mix in classes for interactive objects

### import statements
from base_class_def import ViewOnly
from item_class_def import Item

### mixin classes
class OpenableMixIn(object):
	def __init__(self, is_open):
		""" The OpenablehMixIn can be combined with other classes (most typically ViewOnly) to produce doors and lidded containers.
		"""
		self._is_open = is_open # state of the door; True for door open

	# *** getters & setters ***
	@property
	def is_open(self):
		return self._is_open

	@is_open.setter
	def is_open(self, new_state):
		self._is_open = new_state

	# *** class identity methods ***
	def	is_openable(self):
		return True

	# *** attribute methods ***
	def is_not_closed(self):
		return self.is_open is not False

	# *** display methods ***
	def has_cond(self, active_gs):
		return True

	def disp_cond(self, active_gs):
		""" Displays object-specific conditions. Used in examine().
		"""
##		if self.is_open is None:
##			active_gs.buff_no_cr(f"The {self.full_name} has no closure; it always remains open. ")
##			return
		if self.is_open == False:
			active_gs.buff_no_cr(f"The {self.full_name} is closed. ")
			return
		active_gs.buff_no_cr(f"The {self.full_name} is open. ") # is_open == True
		return 

    # *** verb methods ***
	def open(self, active_gs, mode=None):
		""" Opens a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		self.is_open = True

		active_gs.buff_cr()
		active_gs.buff_no_cr("Openned. ")
		if self.is_container() or self.can_contain():
			self.disp_open(active_gs)
#			if self.is_empty():
#				active_gs.buff_no_cr(f"The {self.full_name} is empty.")
#			self.disp_contain(active_gs)
		active_gs.buff_cr()
		return

	def close(self, active_gs, mode=None):
		""" Closes a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		active_gs.buffer("Closed")

		self.is_open = False
		return


### noun classes
# class DoorSimple(ViewOnly, OpenableMixIn):
class DoorSimple(OpenableMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, is_open):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		OpenableMixIn.__init__(self, is_open)
		""" A simple door with no lock.
		"""

	# *** class identity methods ***
#	def	is_door(self):
#		return True
	
#	def is_simple_door(self):
#		return True



