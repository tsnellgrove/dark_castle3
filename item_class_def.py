# program: dark castle v3.75
# name: Tom Snellgrove
# date: Dec 23, 2022
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

	# *** verb error methods ***
	def enter(self, active_gs):
		active_gs.buffer(f"Despite twisting yourself into a pretzel you still can't manage to enter the {self.full_name}.")
		return

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
			active_gs.buffer(f"You are no longer wearing the {self.full_name}.")
			active_gs.buff_try_key(f"{creature.name}_remove_{self.name}")

		active_gs.get_room().remove_item(self, active_gs)
		creature.put_in_hand(self)
		return

	def drop(self, active_gs):
		""" Drops an object from Burt's hand to the floor of the room.
		"""
		creature = active_gs.hero
		if creature.is_contained(active_gs) and not creature.get_contained_by(active_gs).chk_has_capacity():
			active_gs.buffer(f"There's no room on the {self.full_name} for another item.")
			return

		creature.hand_lst_remove(self)
		if creature.is_contained(active_gs):
			creature.get_contained_by(active_gs).contain_lst_append(self)
		else:
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
		active_gs.buffer(f"Eaten.")
		active_gs.buff_try_key(f"{creature.name}_eat_{self.name}")
		return 


class Garment(Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, garment_type):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._garment_type = garment_type # e.g. 'hat'; Burt can only wear one garment of a given type at a time
		""" Burt can wear() garments. He can only wear one garment of a given type at a time. Some garments may impart special powers.
		"""

	# *** getters & setters ***
	@property
	def garment_type(self):
		return self._garment_type

	# *** simple methods ***	
	def is_garment(self):
		return True

	# *** verb methods ***
	def wear(self, active_gs):
		""" Places a garment in a creature's worn inventory and provides a description of any effects that result.
		"""
		creature = active_gs.hero
		if creature.chk_type_worn(self):
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


	# Garment class:

		Overview:
			The Garment class was initially named Clothing and, originally, was only used to enable the royal_crown to be worn. But as the Creature class came more into focus, I made the decision that I wanted Dark Castle to be more vibrantly inhabited than Zork or Enchanter. Since  conversation in IF is extremely challenging, this meant providing more clues to the player about the personality and needs of creatures that Burt meets. Clothing became a key mechanism to display these traits.

		Implementation Detail:
			For magic garments, like the royal_crown, we want to provide a clue to the player that the garment has special powers. When using the wear() command this is easy. But, for reasons explained under Program Architecture, I decided that there should be no remove() command. Instead, to remove a garment, Burt would just take it. I still wanted to alert that player that the magic effects of the royal_crown had ceased when the garment was removed - but this meant distinguishing between 'take royal_crown' (from the floor_lst) and 'take royal_crown' (from burt's worn_lst).
			
			This made linking the magic power alerts to the Creature worn_list_append() and worn_lst_remove() methods very tempting. But, here too, we run into an issue: the long-term goal for Dark Castle as a toolset is to enable every verb method to be executable for any creature. In some cases, the creature may not even be in the same room as Burt... so we need to be able to silence user feedback from a verb method when appropriate.
			
			The upshot of all this pondering is taht I ended up incorporating the alert-on-removing-garment into the take() method using the chk_is_worn() method. The key take-away from this thought process is:

			"All user output from verb actions MUST be centralized in the verb method!"

		Program Architecture:
			We usually focus on the reasons for the solutions we have implemented. But sometimes, the most important decisions are about what we choose NOT to do - and why. After creating the wear() method it seemed very natural to create a remove() method. Not only did it make alerting players to the royal_crown's magic powers easy, it also felt like natural language... when we take off an article of clothing we 'remove' it. And lastly, it increased the verb-count of Dark Castle... which feels like an innately good metric to increase in an interpreter-driven game.
			
			But there's a catch... how should remove() work for non-Garment objects? Can you remove() an object from a room's floor? If so, then remove() is actually just an oddly-chosen synonym for take (just like 'get') and does nothing to solve our alert-on-removing-garment problem. Alternatively, maybe remove() only works for class Garment... and it seems fair to throw an error on 'removing' an object from the floor... but what about 'remove kinging_scroll from crystal_box'? That absolutely sounds like valid usage. And while we're at it, what about 'removing' something from Burt's hand? Language usage gets frought fast! 
			
			Ultimately, the alternative to having remove() be a synonym for take() is to make it only work for class Garment. But this latter option is far from ideal. The underlying driver behind increasing Dark Castle's verb count is a less artificial language interaction... but the only thing more artificial than a small verb-count is a bunch of general-purpose verbs that can only ever be used in very narrowly defined contexts.

			The result of this thinking is that remove() was eliminated as a verb - if burt wants to take off a garment he just uses the take() command. The broader mantra that accompanies this decision is:

			"When in doubt, expand the applicability of existing verbs rather than co-opting new general-purpose verbs for narrow purposes."


	# Weapon class:

		Overview:
			Unlike Zork, which embraced a D&D-style dice-rolling approach to combat, in Dark Castle, fights are decided by pure logic. If Burt attacks a particular creature with a particular object, he will prefail. However, it seems fitting that some objects (shiny_sword, grimy_axe) are innately more likely to be effective than others (stale_biscuits, cheese_wedge, rusty_key). You can attack with the latter but the results are more likely to be comical than deadly.

			The Weapon class also includes the attribute desc_lst, which provides elaborate verbs and adjectives for your attack.

"""
