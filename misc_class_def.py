# program: dark castle v3.74
# name: Tom Snellgrove
# date: Nov 5, 2022
# description: miscelaneous class deffinition module


### import
from static_gbl import descript_dict, static_dict
from base_class_def import ViewOnly

### local functions


### classes
class Liquid(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing):
		super().__init__(name, full_name, root_name, descript_key, writing)
		""" Liquids are ViewOnly objects. You cannot take a Liquid but you can drink() it from a Container.
		"""

	# *** simple obj methods ***
	def is_liquid(self):
		return True

	# *** complex obj methods ***
	def drink(self, active_gs):
		""" Consumes a liquid if it is in a Container that Burt is holding in his hand.
		"""
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
		try:
			active_gs.buffer(descript_dict["drink_"+self.name])
		except:
			pass
		return 

