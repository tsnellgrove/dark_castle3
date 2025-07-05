# program: dark castle
# author: Tom Snellgrove
# module description: Identity class deffinition module

### import
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class Identity(Invisible):
	def __init__(self, name):
		super().__init__(name)
		""" Identity class inherits from Invisible. All tangible classes inherit their 
		class identity methods from Identity. 
		"""

	# *** universal scope methods ***
	def get_contain_lst(self, gs):
		return []

	def get_vis_contain_lst(self, gs):
		return []

	def chk_contain_item(self, item):
		""" Evaluates whether the passed object is contained within the methed-calling object. Only checks a single level deep - does not check in containers.
		"""
		return False

	def get_inv_lst(self, gs):
		""" Returns the list of all objects in the inventory of the methed-calling receptacle.
		"""
		return []

	def chk_item_in_inv(self, item, gs):
		""" Evaluates whether the passed object is contained within the methed-calling object. Performs a deep contain check (i.e. looks in containers). Only called on Room, Creature, and Interactive.
		"""
		return False

	def remove_item(self, item, gs):
		pass
		return 

	# *** class identity methods ***
	def is_invisible(self):
		return True

	def is_writing(self):
		return False

	def is_viewonly(self):
		return False

	def is_item(self):
		return False

	def is_food(self):
		return False

	def is_liquid(self):
		return False

	def is_weapon(self):
		return False

	def	is_openable(self):
		return False
	
	def is_lockable(self):
		return False

	def	is_container(self):
		return False

	def is_room(self):
		return False

	def is_creature(self):
		return False

	def is_switch(self):
		return False

	def is_buttonswitch(self):
		return False

	def is_springsliderswitch(self):
		return False

	def is_leverswitch(self):
		return False

	def has_cond(self):
		return False

	def is_garment(self):
		return False

	def is_seat(self):
		return False
	
	def is_receptacle(self):
		return False
	
	def has_writing(self):
		return False
