# program: dark castle v3.74
# name: Tom Snellgrove
# date: Nov 5, 2022
# description: item class deffinition module


### import
from static_gbl import descript_dict, static_dict
from base_class_def import ViewOnly


### classes
class Item(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing):
		super().__init__(name, full_name, root_name, descript_key, writing)
		""" Items can be 'taken' and 'dropped'. Item inherits from ViewOnly and has no new attributes - just new methods: take() and drop(). 
		"""

	# *** simple object methods ***
	def is_item(self):
		return True

	# *** verb methods ***
	def take(self, active_gs):
		""" Takes an object from either the room or from Burt's inventory and places it into Burt's hand
		"""
		creature = active_gs.hero
		if creature.chk_in_hand(self):
			active_gs.buffer("You're already holding the " + self.full_name)
			return 
		for obj in active_gs.get_room().floor_lst:
			if obj.is_creature() and obj is not active_gs.hero and self in obj.get_vis_contain_lst(active_gs):
				active_gs.buffer(f"Burt, you can't take the {self.full_name}. It belongs to the {obj.full_name}!")
				return 

		active_gs.buffer("Taken")		
		if creature.chk_is_worn(self):
			active_gs.buff_try_key(f"{creature.name}_remove_{self.name}")

		active_gs.get_room().remove_item(self, active_gs)
		creature.put_in_hand(self)
		return

	def drop(self, active_gs):
		""" Drops an object from Burt's hand to the floor of the room.
		"""
		creature = active_gs.hero
		creature.hand_lst_remove(self)
		active_gs.get_room().floor_lst_append(self)
		active_gs.buffer("Dropped")
		return 


class Food(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing):
		super().__init__(name, full_name, root_name, descript_key, writing)
		""" Burt can eat() food. Food may be of interest to other creatures in Dark Castle as well. Food inherits from Item and can be taken.
		"""

	# *** verb methods ***
	def eat(self, active_gs):
		""" Removes the Food object from the game and provides a description of how the food tasted.
		"""
		creature = active_gs.hero
		creature.hand_lst_remove(self)
		eat_desc_key = f"{creature.name}_eat_{self.name}"
		active_gs.buffer(f"Eaten. {descript_dict[eat_desc_key]}")
		return 


class Garment(Item):
#	def __init__(self, name, full_name, root_name, descript_key, writing, clothing_type):
	def __init__(self, name, full_name, root_name, descript_key, writing, garment_type):
		super().__init__(name, full_name, root_name, descript_key, writing)
#		self._clothing_type = clothing_type # e.g. 'hat'; Burt can only wear one garment of a given type at a time
		self._garment_type = garment_type # e.g. 'hat'; Burt can only wear one garment of a given type at a time

	# *** getters & setters ***
	@property
#	def clothing_type(self):
#		return self._clothing_type
	def garment_type(self):
		return self._garment_type

	# *** simple methods ***	
	def is_garment(self):
		return True

	# *** verb methods ***
	def wear(self, active_gs):
		creature = active_gs.hero
#		if creature.chk_clothing_type_worn(self):
		if creature.chk_type_worn(self):
#			active_gs.buffer(f"You are already wearing a {self.clothing_type}. You can't wear two garments of the same type at the same time.")
			active_gs.buffer(f"You are already wearing a {self.garment_type}. You can't wear two garments of the same type at the same time.")
			return 
		creature.worn_lst_append(self)
		creature.hand_lst_remove(self)
		active_gs.buffer("Worn.")
		active_gs.buff_try_key(f"{creature.name}_wear_{self.name}")
		return 


class Weapon(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, desc_lst):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._desc_lst = desc_lst # descriptive terms associated with using the weapon to 'attack'
		""" A Weapon can be used to attack. Weapon is a subclass of Item. 
		"""

	# *** getters & setters ***
	@property
	def desc_lst(self):
		return self._desc_lst

	# *** simple methods ***
	def is_weapon(self):
		return True


""" *** Module Documentation ***

	* Item class:

		Implementation Detail:
			All objects of class Item are takable - there's no 'is_takable' attribute to prevent this. To temporarily prevent an Item from being taken you could:
				1) Initially provide a ViewOnly object and then, when appropriate, swap in an Item object with the same full_name
				2) Prevent the take() method via a Warning
				3) Prevent the take() method via a Modular Machine
		
		Game Design:
			Adventurers love Items. This tradition dates back to Zork I itself, where the sole mission of the game was to collect 20 (or 19, depending on how you count) treasures and safely store them in a trophy case. Although Dark Castle theoretically follows the Enchanter tradition of saving the land, truthfully, Burt showed up at Dark Castle to score some loot and that desire is never far from his heart. Good game design leverages this love of Items. 
			
			Want to intrigue and excite an Adventurer? Show them an out-of-reach Item. Want to infuriate an Adventurer? Pilfer their hard won Items! Want to make a puzzle hard? Require that the Adventurer surrender an Item to solve it. Dark Castle leans in heavily on each of these standard Adventurer manipulation techniques.

		
	- take() method [Item class]:

		Implementation Detail:
			take() used to be a more complex method. Adding the object into Burt's hand is trivial but finding where to remove it from takes some serching. I initially did all that searching in take(). During refactoring it became clear that it made sense to do this in Room instead since the Room class is already responsible for providing visible object scope and therefore is already required to know all the places an object could be.
			
			I initially thought that the 'Can't take another creature's stuff' error would be a great use case for the any(if x == y for x in z) pattern. This proved to be incorrect. For one thing, the any() pattern is a one-liner - so 'x' does not exist outside that line - but I need it for the error message on the next line. Also, curiously, it turns out that Python's magic ability to have an 'if x and y' statement where 'y' can be undefined so long as 'x' is False does not work within any(). Code and learn!
			
			It may initially be surprising how few tests we need to conduct before performing the method. The logic works as follows:
				1) We confirm that 'obj' is visible to Burt in validate()
				2) 'obj' must either be of class Item or inherit from class Item or else the method could not run
				3) Local error checking ensures that 'obj' is not already in Burt's hand or held / worn by another creature
				4) Therefore, 'obj' must be a takable Item!

	# Food class:

		Overview: 
			Food currently has no purpose in the game other than to distract the hedgehog and provide some color. But I eventually envision creating an old-school game like Enchanter where Burt needs to keep eating and hydrating as he plays the game. This will eventually require that food have a quantity attribute (i.e. it takes 3 bites to finish the stale_biscuits) which can be percieved via examine() as a condition.

	# Weapon class:

		Overview:
			Unlike Zork, which embraced a D&D-style dice-rolling approach to combat, in Dark Castle, fights are decided by pure logic. If Burt attacks a particular creature with a particular object, he will prefail. However, it seems fitting that some objects (shiny_sword, grimy_axe) are innately more likely to be effective than others (stale_biscuits, cheese_wedge, rusty_key). You can attack with the latter but the results are more likely to be comical than deadly.

			The Weapon class also includes the attribute desc_lst, which provides elaborate verbs and adjectives for your attack.

"""
