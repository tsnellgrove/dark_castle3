# program: dark castle v3.77
# name: Tom Snellgrove
# date: May 22, 2023
# description: miscelaneous class deffinition module


### import
from dc3.class_std.base_class_def import ViewOnly


### classes
class Liquid(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing):
		super().__init__(name, full_name, root_name, descript_key, writing)
		""" Liquids are ViewOnly objects. You cannot take a Liquid but you can drink() it from a Container.
		"""

	# *** class identity methods ***
	def is_liquid(self):
		return True

	# *** verb methods ***
	def drink(self, active_gs, mode=None):
		""" Consumes a liquid if it is in a Container that Burt is holding in his hand.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		creature.get_hand_item().contain_lst.remove(self)

		active_gs.io.buffer("Drunk.")
		active_gs.io.buff_s(f"{creature.name}_drink_{self.name}")
		return 


""" *** Module Documentation ***

	* Item class:
		Overview: Liquids and drinking them currently have no purpose in the game but in future versions I intend to implement food and drink requirements similar to those in Enchanter. I also plan to eventually implement a pour() verb method that allows Burt to do more with water than just drink() it.

"""
