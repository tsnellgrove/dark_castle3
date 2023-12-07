# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: item class deffinition module


### import
from dc3.class_std.base_class_def import ViewOnly


### classes
class Item(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._weight = weight # represents the weight of the object
		""" Items can be 'taken' and 'dropped'. Item inherits from ViewOnly and has no new attributes - just new methods: take() and drop(). 
		"""

	# *** getters & setters ***
	@property
	def weight(self):
		return self._weight

	@weight.setter
	def weight(self, new_weight):
		self._weight = new_weight

	# *** attrib methods ***
	def increment_weight(self, increment_by):
		""" Increments the weight of an Item by a given amount
		"""
		self.weight += increment_by
		return

	def decrement_weight(self, decrement_by):
		""" Decrements the weight of an Item by a given amount
		"""
		self.weight -= decrement_by
		return

	# *** class identity methods ***
	def is_item(self):
		return True

	# *** verb methods ***
	def take(self, active_gs, mode=None):
		""" Takes an object from either the room or from Burt's inventory and places it into Burt's hand
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero
		
		active_gs.io.buffer("Taken")
		if creature.chk_is_worn(self):
			active_gs.io.buffer(f"You are no longer wearing the {self.full_name}.")
			active_gs.io.buff_s(f"{creature.name}_remove_{self.descript_key}")
		
		active_gs.get_room().remove_item(self, active_gs)
		creature.put_in_hand(self, active_gs)
		return

	def drop(self, active_gs, mode=None):
		""" Drops an object from Burt's hand to the floor of the room.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		creature.hand_lst_remove(self)
		if creature.is_contained(active_gs):
			creature.get_contained_by(active_gs).contain_lst_append(self, active_gs)
		else:
			active_gs.get_room().floor_lst_append(self)
		
		active_gs.io.buffer("Dropped")
		return 

	# *** debug methods ***
	def get_weight(self, active_gs, mode=None):
		""" Reports the weight of an Item. Only usable in debug mode.
		"""
		if mode is None:
			mode = 'std'
		
		active_gs.io.buffer(f"The weight of the {self.full_name} is {self.weight}.")
		return


class Food(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight):
		super().__init__(name, full_name, root_name, descript_key, writing, weight)
		""" Burt can eat() food. Food may be of interest to other creatures in Dark Castle as well. Food inherits from Item and can be taken.
		"""

	# *** class identity methods ***
	def is_food(self):
		return True
	
	# *** verb methods ***
	def eat(self, active_gs, mode=None):
		""" Removes the Food object from the game and provides a description of how the food tasted.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		creature.hand_lst_remove(self)
		
		active_gs.io.buffer(f"Eaten.")
		active_gs.io.buff_s(f"{creature.name}_eat_{self.descript_key}")
		return 


class Liquid(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight):
		super().__init__(name, full_name, root_name, descript_key, writing, weight)
		""" Liquids are ViewOnly objects. You cannot take a Liquid but you can drink() it from a Container.
		"""

	# *** class identity methods ***
	def is_liquid(self):
		return True
	
	# *** verb methods ***
	def drink(self, obj, active_gs, mode=None):
		""" Consumes a liquid if it is in a Container that Burt is holding in his hand.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

#		obj.contain_lst.remove(self)
		obj.remove_item(self, active_gs)

		active_gs.io.buffer("Drunk.")
		active_gs.io.buff_s(f"{creature.name}_drink_{self.descript_key}")
		return 


class Garment(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, garment_type):
		super().__init__(name, full_name, root_name, descript_key, writing, weight)
		self._garment_type = garment_type # e.g. 'hat'; Burt can only wear one garment of a given type at a time
		""" Burt can wear() garments. He can only wear one garment of a given type at a time. Some garments may impart special powers.
		"""

	# *** getters & setters ***
	@property
	def garment_type(self):
		return self._garment_type

	# *** class identity methods ***
	def is_garment(self):
		return True

	# *** verb methods ***
	def wear(self, active_gs, mode=None):
		""" Places a garment in a creature's worn inventory and provides a description of any effects that result.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero
		
		creature.hand_lst_remove(self)
		creature.worn_lst_append(self)
		
		active_gs.io.buffer("Worn.")
		active_gs.io.buff_s(f"{creature.name}_wear_{self.descript_key}")
		return 


class Weapon(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, desc_lst):
		super().__init__(name, full_name, root_name, descript_key, writing, weight)
		self._desc_lst = desc_lst # descriptive terms associated with using the weapon to 'attack'
		""" A Weapon can be used to attack. Weapon is a subclass of Item. Attacking with a weapon is a serious threat.
		"""

	# *** getters & setters ***
	@property
	def desc_lst(self):
		return self._desc_lst

	# *** class identity methods ***
	def is_weapon(self):
		return True
