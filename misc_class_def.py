# program: dark castle v3.75
# name: Tom Snellgrove
# date: Dec 23, 2022
# description: miscelaneous class deffinition module


### import
from static_gbl import descript_dict, static_dict
from base_class_def import ViewOnly


### classes
class Liquid(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing):
		super().__init__(name, full_name, root_name, descript_key, writing)
		""" Liquids are ViewOnly objects. You cannot take a Liquid but you can drink() it from a Container.
		"""

	# *** simple methods ***
	def is_liquid(self):
		return True

	# *** verb methods ***
	def take(self, active_gs):
		""" Provides context-specific error message when player attempts to take() a liquid
		"""
		active_gs.buffer("You can't 'take' a liquid. Try 'drink' instead.")
		return

	def drink(self, active_gs):
		base_error = super(Liquid, self).drink(active_gs)
		""" Consumes a liquid if it is in a Container that Burt is holding in his hand.
		"""
		if base_error:
			return
		creature = active_gs.hero
		if not creature.hand_is_empty():
			hand_item = creature.get_hand_item()
		if (creature.hand_is_empty()) or (hand_item.is_container() == False):
			active_gs.buffer(f"You don't seem to be holding a container of {self.full_name} in your hand.")
			return 
		if self not in hand_item.contain_lst:
			active_gs.buffer(f"The container in your hand doesn't contain {self.full_name}.")
			return 

		hand_item.contain_lst.remove(self)

		active_gs.buffer("Drunk.")
		active_gs.buff_try_key(f"{creature.name}_drink_{self.name}")
		return 


""" *** Module Documentation ***

	* Item class:
		Overview: Liquids and drinking them currently have no purpose in the game but in future versions I intend to implement food and drink requirements similar to those in Enchanter. I also plan to eventually implement a pour() verb method that allows Burt to do more with water than just drink() it.

"""
