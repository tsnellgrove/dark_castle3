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
		self._is_open = is_open # state of the door; True for door open
		""" The OpenablehMixIn can be combined with other classes (most typically ViewOnly) to produce doors and lidded containers.
		"""

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
		if self.is_container():
			self.disp_open(active_gs)
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


class LockableMixIn(object):
	def __init__(self, is_unlocked, key):
		self._is_unlocked = is_unlocked # True if the door is unlocked, False if the door is locked, None if there is no lock
		self._key = key # the key obj required to unlock the door; None means the door is not locked by a key
		""" The LockablehMixIn can be combined with other classes (most typically ViewOnly) to produce lockable doors and containers. Unlocking an object typically requires the correct key.
		"""

	# *** getters & setters ***
	@property
	def is_unlocked(self):
		return self._is_unlocked

	@is_unlocked.setter
	def is_unlocked(self, new_state):
		self._is_unlocked = new_state

	@property
	def key(self):
		return self._key

	@key.setter
	def key(self, new_key):
		self._key = new_key

	# *** class identity methods ***
	def is_lockable(self):
		return True

	# *** verb methods ***
	def unlock(self, key_obj, active_gs, mode=None):
		""" Unlocks a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		active_gs.buffer("Unlocked")

		self.is_unlocked = True
		return

	def lock(self, key_obj, active_gs, mode=None):
		""" Locks a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		active_gs.buffer("Locked")

		self.is_unlocked = False
		return

class ContainsMixIn(object):
	def __init__(self, contain_lst, max_weight, max_obj, prep):
		self._contain_lst = contain_lst # list of objects in the container
		self._max_weight = max_weight # maximum combined weight the container can hold
		self._max_obj = max_obj # maximum number of objects the container can hold
		self._prep = prep # prep to be used when addign obj to container; typically 'in' or 'on'
		""" The ContainsMixIn can be combined with other classes to hold items.
		"""

	# *** getters & setters ***
	@property
	def contain_lst(self):
		return self._contain_lst

	@contain_lst.setter
	def contain_lst(self, new_obj):
		self._contain_lst = new_obj

	@property
	def max_weight(self):
		return self._max_weight

	@property
	def max_obj(self):
		return self._max_obj

	@property
	def prep(self):
		return self._prep

	# *** attrib methods ***
	def contain_lst_append(self, item):
		self._contain_lst.append(item)

	def contain_lst_remove(self, item):
		self._contain_lst.remove(item)

	def is_empty(self):
		return not self.contain_lst

	# *** class identity methods ***
	def	is_container(self):
		return True

	# *** scope methods ***
	def get_vis_contain_lst(self, active_gs):
		""" Returns the list of visible objects contained in the referenced ('self') object
		"""
		if (self.is_openable() and self.is_not_closed()) or (not self.is_openable()):
			node2_lst = []
			[node2_lst.extend(obj.get_vis_contain_lst(active_gs)) for obj in self.contain_lst]
			return self.contain_lst + node2_lst
		return []

	def chk_wrt_is_vis(self, writing, active_gs):
		""" Evaluates whether the passed writing is visible within the methed-calling object.
		"""
		return any(obj.writing == writing for obj in self.get_vis_contain_lst(active_gs))

	def chk_contain_item(self, item):
		""" Evaluates whether the passed object is contained within the methed-calling object. Called by Room.remove_item()
		"""
		return item in self.contain_lst

	def chk_has_capacity(self):
		return len(self.contain_lst) < self.max_obj

	def remove_item(self, item, active_gs):
		self.contain_lst_remove(item)

	def chk_content_prohibited(self, obj):
		return obj.is_creature()

	def get_contained_weight(self):
		return sum(element.weight for element in self.contain_lst)

	# *** display methods ***
	def has_contain(self, active_gs):
		return bool(self.contain_lst)

	def has_cond(self, active_gs):
		return True

	def disp_cond(self, active_gs):
		super(ContainsMixIn, self).disp_cond(active_gs)
		""" Displays object-specific conditions. Used in examine().
		"""
		if ((self.is_openable() and self.is_not_closed()) or not self.is_openable()) and self.is_empty():
			active_gs.buff_no_cr(f"The {self.full_name} is empty. ")
		return 

	def disp_contain(self, active_gs):
		""" Displays a description of the visible items held by the obj. Used in examine().
		"""
		if ((self.is_openable() and self.is_not_closed()) or not self.is_openable()) and not self.is_empty():
			contain_txt_lst = [obj.full_name for obj in self.contain_lst if obj != active_gs.hero]
			if contain_txt_lst:
				contain_str = ", ".join(contain_txt_lst)
				active_gs.buff_no_cr(f"The {self.full_name} contains: {contain_str}. ")
			for obj in self.contain_lst:
				if obj != active_gs.hero:
					obj.disp_contain(active_gs)
		return 

	def disp_open(self, active_gs):
		if self.is_empty():
			active_gs.buff_no_cr(f"The {self.full_name} is empty.")
		self.disp_contain(active_gs)

	# *** verb methods ***
	def put(self, obj, active_gs, mode=None):
		""" Puts an Item in a Container or on a Surface.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero
		
		creature.hand_lst_remove(obj)
		self.contain_lst_append(obj)

		active_gs.buffer("Done")
		return


	def capacity(self, active_gs, mode=None):
		""" Reports the capacity of a Container. Only usable in debug mode.
		"""
		if mode is None:
			mode = 'std'
		
		active_gs.buffer(f"The weight capacity of the {self.full_name} is {self.max_weight}.")
		active_gs.buffer(f"The object count capacity of the {self.full_name} is {self.max_obj}.")
		return


### generic noun classes
class DoorSimple(OpenableMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, is_open):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		OpenableMixIn.__init__(self, is_open)
		""" A simple door with no lock.
		"""

class DoorLockable(LockableMixIn, DoorSimple):
	def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key):
		DoorSimple.__init__(self, name, full_name, root_name, descript_key, writing, is_open)
		LockableMixIn.__init__(self, is_unlocked, key)
		""" A door that can be locked or unlocked.
		"""

class ContainerFixedSimple(ContainsMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		ContainsMixIn.__init__(self, contain_lst, max_weight, max_obj, prep)
		""" A simple non-takable container with no lid or lock. Can be a box or a shelf depending on 'prep'
		"""

class ContainerFixedLidded(ContainsMixIn, OpenableMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, is_open):
		ContainerFixedSimple.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep)
		OpenableMixIn.__init__(self, is_open)
		""" A non-takable container with a lid but no lock.
		"""

class ContainerFixedLockable(LockableMixIn, ContainsMixIn, OpenableMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, is_open, is_unlocked, key):
		ContainerFixedLidded.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, is_open)
		LockableMixIn.__init__(self, is_unlocked, key)
		""" A non-takable container with a lid and a lock.
		"""

class ContainerPortableSimple(ContainsMixIn, Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, contain_lst, max_weight, max_obj, prep):
		Item.__init__(self, name, full_name, root_name, descript_key, writing, weight)
		ContainsMixIn.__init__(self, contain_lst, max_weight, max_obj, prep)
		""" A simple, takable container with no lid or lock. Can be a box or a surface (e.g. a tray) depending on 'prep'
		"""

	# *** scope method extensions ***
	def remove_item(self, item, active_gs):
		super(ContainerPortableSimple, self).remove_item(item, active_gs)
		""" Decrements Portable Container weight when an Item is removed from the Container.
		"""
		self.weight -= item.weight
		return

	def chk_content_prohibited(self, obj):
		return super(ContainerPortableSimple, self).chk_content_prohibited(obj) or (obj.is_container() and obj.is_item)

	# *** verb method extensions ***
	def put(self, obj, active_gs, mode=None):
		super(ContainerPortableSimple, self).put(obj, active_gs, mode=None)
		""" Increments Portable Container weight when an Item is put in the Container.
		"""
		if mode is None:
			mode = 'std'

		self.weight += obj.weight
		return

class ContainerPortableLidded(OpenableMixIn, ContainerPortableSimple):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, contain_lst, max_weight, max_obj, prep, is_open):
		ContainerPortableSimple.__init__(self, name, full_name, root_name, descript_key, writing, weight, contain_lst, max_weight, max_obj, prep)
		OpenableMixIn.__init__(self, is_open)
		""" A takable container with a lid but no lock.
		"""

class ContainerPortableLockable(LockableMixIn, ContainerPortableLidded):
	def __init__(self, name, full_name, root_name, descript_key, writing, weight, contain_lst, max_weight, max_obj, prep, is_open, is_unlocked, key):
		ContainerPortableLidded.__init__(self, name, full_name, root_name, descript_key, writing, weight, contain_lst, max_weight, max_obj, prep, is_open)
		LockableMixIn.__init__(self, is_unlocked, key)
		""" A takable container with a lid and a lock.
		"""

### custom noun classes
class Seat(ContainerFixedSimple):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, in_reach_lst):
		ContainerFixedSimple.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep)
		self._in_reach_lst = in_reach_lst # list of receptacles that are reachable when seated in the seat
		""" A seat on which a Creature can sit.
		"""

	# *** getters & setters ***
	@property
	def in_reach_lst(self):
		return self._in_reach_lst

	@in_reach_lst.setter
	def in_reach_lst(self, new_lst):
		self._in_reach_lst = new_lst

	# *** class identity methods ***
	def is_seat(self):
		return True

	# *** scope methods ***
	def chk_content_prohibited(self, obj):
		return obj.is_seat()

	# *** verb methods ***
	def enter(self, active_gs, mode=None, creature=None):
		""" Sits a creature in a Seat
		"""
		# destermine default attributes
		if mode is None:
			mode = 'std'
		if creature is None:
			creature = active_gs.hero

		room = active_gs.map.get_obj_room(creature)
		room.floor_lst_remove(creature)
		self.contain_lst_append(creature)

		# if hero_creature not in current room, exit with no display
		if room != active_gs.get_room():
			return 
		
		if creature == active_gs.hero:
			active_gs.buffer(f"You are now seated in the {self.full_name}.")
			creature.disp_in_reach(active_gs)
			active_gs.buff_try_key(f"{creature.name}_enter_{self.name}")
		else:
			active_gs.buffer(f"The {creature.full_name} is now seated in the {self.full_name}.")
		return

	def exit(self, active_gs, mode=None, creature=None):
		""" Enables a creature to exit a Seat
		"""
		# destermine default attributes
		if mode is None:
			mode = 'std'
		if creature is None:
			creature = active_gs.hero

		room = active_gs.map.get_obj_room(creature)
		room.floor_lst_append(creature)
		self.contain_lst_remove(creature)

		# if hero_creature not in current room, exit with no display
		if room != active_gs.get_room():
			return 
		
		if creature == active_gs.hero:
			active_gs.buffer(f"You are now standing in the {room.full_name}.")
			active_gs.buff_try_key(f"{creature.name}_exit_{self.name}")
		else:
			active_gs.buffer(f"The {creature.full_name} is now standing in the {room.full_name}.")
		return


""" *** Module Documentation ***

* Module Overview *
	
'interactive' is a vauge term. Hopefully I'll think of a better module name down the road. But the intent is along the vein of 'standardized and prepositionally / combinatorally, interactive'. Hence, not foundational classes like ViewOnly or Item. Not custom objects like Machines. Not classes like Food and Liquid for which there are highly specific, non-combinatorial verb methods (eat() and drink() respectively). Rather, the goal here is to address objects like doors, surfaces, and containers... which all operate in a standard fashion but potentially have some functionality overlap (e.g. doors and containers both open, surfaces and containers both hold Items, etc).

In early DCv3 versions I treated this as an inheritance chain of monolithic classes: Surface inherited from Container which inherited from Door (in fact, all of these classes lived in a module named door_class_def() ). This approach worked but wasn't very elegant - by the time you got to Surface, all of the attributes related to openning and locking had to be set to None. Ditto for doors and containers without locks. And portable containers were sketchy at best. The final straw was my attempt to add a 'weight' attribute to the Item class. The already sketchy implementation of portable containers completely broke down. It was time for a fresh start.

Durring refactoring I took a new approach: I created MixIn classes for 'openable', 'lockable', and 'contains'. Then noun classes were built by combining ViewOnly or Item with one or more MixIn.

* Current MixIn Classes:
	- OpenableMixIn
		attributes = is_open
		methods = 
			- open()
			- close()
	- LockableMixIn
		attributes = 
			- is_unlocked
			- key
		methods =
			- lock()
			- unlock()
	- ContainsMixIn
		attributes = 
			- contain_lst
			- max_weight
			- max_obj
			- prep
		methods = put()

* Current Generic Noun Classes:
	- DoorSimple = ViewOnly + OpenableMixIn
		examples = screen_door
	- DoorLockable = DoorSimple + LockableMixIn
		examples = front_gate
	- ContainerFixedSimple = ViewOnly + ContainsMixIn
		examples = wooden_shelf or stone_coffer
	- ContainerFixedLidded = ContainerFixedSimple + OpenableMixIn
		examples = cardbaord_box
	- ContainerFixedLockable = ContainerFixedLidded + LockableMixIn
		examples = crystal_box
	- ContainerPortableSimple = Item + ContainsMixIn
		examples = small_barrel or silver_tray
		methods =
			- put() extension to address weight
			- remove_item() extension to address weight
			- chk_content_prohibited() extension to prohibit portable containers
	- ContainerPortableLidded = ContainerPortableSimple + OpenableMixIn 
		examples = red_shoebox
	- ContainerPortableLockable = ContainerPortableLidded + LockableMixIn
		examples = black_suitcase
	
* Current Custom Noun Classes:
	- Seat (I know, the naming goes a bit sideways here) = ContainerFixedSimple for Creatures
		examples = test_chair
		attributes = in_reach_lst
		methods = 
			- chk_content_prohibited() over-ride to allow creatures
			- enter()
			- exit()

			
*** MixIn Classes
* OpenableMixIn class:
	- Overview:
		An openable object can be opened and closed. In doing so, the player may reveal either a new passage or one or more new objects to investigate. The most fundamental openable object is the Door. Finding a way to open a door is one of the most basic puzzle elements in interactive fiction.

		Most containers can also be openned and closed. By implementing the open and close functionality as a MixIn, the same code can be applied to many different base objects - from imposing locked-and-barred front gates to champagne bottles.

	- Class Attributes:
		OpenableMixIn has a single attribute: 'is_open'. 'is_open' is a boolean which can be either True or False (None, was a valid value in the Door class but is no longer supported or used).
		
	- open() and close() methods [OpenaableMixIn class]:
		Overview:
			open() and close() are quite simple. When called, they set the state of the is_open attribute to True or False respectively and provide confirmational output. Most of the heavy lifting gets done in open_err() and close_err() which check for obj which are not opennable / closeable, or are already openned or closed, or are locked.
	
		Implementation Detail:
			For the purposes of examine(), an Openable object has a 'condition' (i.e. obj.has_cond() = True) and examine() => disp_cond() will indicate whether the object is openned or closed.
	
		Program Architecture:
			On the topic of OpenableMixIn, let's take a moment to meniton where Doors 'live'. Unlike most other large objects (e.g. Creatures), doors do not reside in room.floor_lst. This is because doors don't really exist in just one room. Instead, they are contained within "room pairs" - which in turn reside in the map_lst attribute of the GameState map object. See map_class_def.py for details.

		Game Design:
			Regarding open() in particular, let's consider UI. A core goal in IF is to anticipate and meet player expectations. In the case of open(), if a player opens a chest, they are keen to know what is in it. To this end, in the open() method, we check for obj.is_container() and, if True, display the contents.
			
		Historic Note:
			In v1 and v2 of Dark Castle, doors could be unlocked and opened but not closed or locked. The problem wasn't actually room doors - it would have been easy to code them to close and lock - the real problem was containers, which were based on the same code base as doors (as is still the case in v3). Containers were the last and most complicated thing I coded in v1 (v2 just being the web version of v1). I was running into the limits of writing the program in procedural code and by this time I knew I was going to do a full re-write in OOP. So faced with the prospect of writing a 'put' verb and more complicated room inventory management, I totally dialed it in. Containers in v1 / v2 simply dumped their contents into the room inventory the moment you managed to open them. But of course that meant you couldn't close the container - because the the objects 'in' the container would still be in the room... hence the lack of 'close' and 'lock'. From a gameplay and puzzle point of view, this was never a problem. But the asymetry always annoyed me - I pictured Nana calling out to Burt across the years "For goodness sake Burtie, close the door behind you!" Properly working Containers and Doors were one of my first goals for v3.

			
* OpenableMixIn class:
	- Overview:
		When applied to an existing object, makes it lockable or unlockable. The typical intent is that the existing object also be Openable. However, this is not mandated. In theory, you could have have a car ignition Machine that was Lockable and is_unlocked == True could be the Machine trigger to start the car. 

	- Class Attributes:
		- is_unlocked: The boolean state of the lock. True => unlocked; False => locked; None is not a valid value (unlike in the previous case of the Door class). 
		- key: The object that can lock() or unlock() the target Door or Container. If key == None, there is no keyhole and the Door or Container must be openned by some other means (e.g. the iron_portcullis). 

	- lock() and unlock() methods [OpenableMixIn class]:
		Overview:
			Prepositional verb methods that expect a command in the form of: 'unlock front_gate with rusty_key'. If a key is not specified and Burt is holding something in his hand, that hand object will be assumed to be the key.

		Implementation Detail:
			The is_unlocked atribut is stated as a negative (i.e. is_*un*locked) so that the player's typically desired state == True.

		Program Architecture:
			Initially, all doors and containers were lockable. Since, in practace, not many doors or containers in IF are *not* lockable (even though it's a common occurence in real life) this seemed like a reasonable compromise. But once it became clear that the Surface class would be commonly used, it became clear that the Lockable state should be a MixIn class rather than directly baked into a Noun class.
		
		Game Design:
			There are no fewer than 11 custom errors for lock_err() and unlock_err(). This is partly because, as a prepositional verb method, there are twice as many objects that could be non-sensical (e.g. 'lock moat with cheese') and partly to give the player a helpful nudge when possible (e.g. when they use the *wrong* key). A concerted effort is made to visualize someone walking up to a door to unlock it and to give errors in the order of "least user astonishment" (e.g. the player is warned that an opened door can't be locked before they are warned that they are holding the wrong key).
		
		Historic Note:
			See historic note for OpenableMixIn().


* ContainsMixIn class:
	- Overview:
		Like doors, containers are fundamental puzzle elements. Doors are obstacles to entering rooms. Containers are obstacles to getting items.

		In Dark Castle v1/2, containers were just a coding slight of hand. So when I finally coded them for real, I needed to decide in what way a container and its contents were aware of each other. Presumably the crystal_box knew it contained the kinging_scroll... but did the kinging_scroll 'know' it was in the crystal_box? 
		
		Ultimately, I decided on two axioms:
			1) Within the constraints of acceptable performance, data should always live in one and only one location
			2) An object should know about the objects contained directly within it.
		
		From these axioms it becomes clear that containers should know what they contain but items are location 'ignorant': the kinging_scroll has no idea that it's in the crystal_box... or if it gets moved to Burt's hand or to the floor of the throne_room. Along with meeting our 'data in only one place' constraint, this approach also has the benefit of keeping most objeccts simple. There's no need to assign and update an extra 'location' attribute for every object. The down side is that recepatacle entities (i.e. Containers, Creatures, Rooms) become more complicated - and we end up frequently searching them for their contents. This hierarchal approach to containers is fundamental and has been applied to all aspects of the game (e.g. rooms know about the objects within them but know nothing about other rooms outside of them).
		
	- Class Attributes:
		- contain_lst: A list of obj in / on the container

		- max_weight: The maximum combined weight of obj that the container can hold. Notice that here, weight is being used as a proxy for volume. At some point, it may become necessary to add an additional 'bulk' attribute to the Item class but for now this seems like a reasonable generalization.

		- max_obj: The maximum count of obj the container can hold. The maximum is independent of max_weight and either limit can make it impossible to place an obj in / on a container. For the sake of simplicity, I typically make only one limit the constraining value and set the other to 999. My default is to constrain "enclosed contaiers" via obj weight and "surfaces" via obj count.

		- prep: The preposition that should be used when putting and object 'in' or 'on' a container - so generally either "in" or "on". The need for 'prep' arrises from the fact that, from an IF topology standpoint, the only difference between an unlidded but "enclosed" container like cardboard_box and a "surface" like wooden_shelf is the preposition used when adding an object to them. Previously, Surface was a class of its own that inherited from Container. Under the MixIn approach, they are both containers - only differentiated by attribute 'prep'.

	- put() method [ContainsMixIn class]:
		Overview:
			Used to add obj to containers.
		
		Implementation Detail:
			Container.chk_content_prohibited() is used to limit what can be put in a container and is extended for 'ContainerPortableSimple'. For details on why Containers can't hold Creatures and why 'ContainerPortableSimple' can't hold 'ContainerPortableSimple' obj, please see the explanation on node hierarchy under the Room class.

		Program Architecture:
			It might appear that put() could just as well be a method of Item as it is of Container. Code-wise this would certainly work. But what becomes clear when developing verb methods is that the code for testing error cases and buffering error messages is often longer than the code for actually executing the command. A corollary to this realization is that we always want to associate a method with its most restrictive noun - which in the case of put() is Container. This means that we don't need to test to see if the target location for put() is a Container - the method simply can't run if it isn't. This same logic applies to other preposition type verb methods like show() and give() - which in theory could be methods of Item but which are more efficiently coded when naturally limited in use by being methods of Creature.
			
			With Burt now being of class Creature, this principle can be generalized. Nearly every command actually involves Burt as the subject (e.g. "Burt, put the Rusty Key in the Crystal Box"). So while it's tempting to ask "who or what is performing the action?" - this line of reasoning would lead to every verb method being of class Creature. Instead, we generally want to ask "who or what is being acted on?" We can formalize this logic as follows:
				
				The 3 rules of method association:
				1) It's (almost) never the actor - because the actor is (almost) always Burt
				2) Ask, who or what is being acted on
				3) Choose the noun that is most restrictive
					
			When we apply this razor to "Burt, put the Rusty Key in the Crystal Box", Burt is immediately excluded and, between Rusty Key (class Item) and Crystal Box (class Container) we see that container is more restrictive. So put() is implemented as a verb method of Container.

		Game Design:
			ContainsMixIn has a number of scope and display "helper methods" that control what the player sees when they examine() a container, how obj are removed from a container, and how container capacity behaves.
		
			The ContainsMixIn class also sees the very first debug-only verb method: capacity(). capacity() gives the remaining weight and obj count capacity of any Container but can only be run in debug mode.
		
		Historic Note:
			put() was the very first preposition-based command in DCv3. After ages of two-word commands it very exciting to be able to type 'put the rusty key in the crystal box' and have a working result!

			Since the Surface class has been subsumed into the ContainsMixIn class, I will give its history here as well. My initial reason for creating the Surface class was that control_panel was previously an annoying hack. control_panel itself was of ViewOnlyMach class. This was fine but what to do with left_lever, middle_lever, right_lever, and red_button? The work-around was to mention them explicitly in the control_panel description but then stuff them in antechamber.feature_lst. This always irked me... and the more consistently behaved the Container class became the more unacceptable this work-around felt. One day I started thinking that control_panel should just be a container... but with no lid - and voila - the insight that a Surface class was needed arrived!		


* Generic Noun class:
	- Overview:
		There are eight Generic Noun classes: DoorSimple, DoorLockable, ContainerFixedSimple, ContainerFixedLidded, ContainerFixedLockable, ContainerPortableSimple, ContainerPortableLidded, ContainerPortableLockable. With the exception of ContainerPortableSimple, each works as expected based on MixIns and their base class (ViewOnly or Item) with no additional attributes or methods.

	- Methods:	
		ContainerPortableSimple is an excpetion because it needs to establish how a portable container's weight changes as a result of having Items added or removed. This is accomplished via extensions to put() and remove_item(). chk_content_prohibited() is also extended to prohibit portable containers from holding other portable containers - which sets an upper bound on receptacle nesting.

	- Implementation Detail:
		Some special mention should be made here regarding Liquids. As part of refactoring Doors and Containers, teh PortableLiquidContainr class was eliminated and Liquid itself was converted from inheriting from ViewOnly (as the only member of the misc_class_def.py module) to inheriting from Item in item_class_def.py. This enables Liquid to have the newly created 'weight' attribute. Players still can't take() Liquids - but this limit is now enforced by take_err() rather than ViewOnly class membership. At present, the earthen_jug is the only portable container that with a weight limit < 1 and well_water is the only Item with a weight low enough to fit into it - so earthen_jug's unique role as a liquid container remains (albeit via kludgy work-around). I have outlined the (many) features needed to fully implement Liquids in the game and plan to deploy them in a future version.


* Seat class:
	- Overview:
		The Seat class inherits from ContainerFixedSimple but overrides chk_content_prohibited() to allow the receptacle to hold Creatures. Creatures use the class verb methods enter() and exit() to sit in / on a Seat obj. 

	- Implementation Detail:
		Conceptually, Seat is a new topology for Dark Castle. Before Seat, the player was either in a room  or they weren't and rooms were treated as hermetically sealed from each other. So if you were in the Entrance you could attempt any action on any obj that was present. And if you weren't in the Entrance, any reference to an obj that was there would only generate a "I can't see a <obj X> here" response.

		By contrast, Seat introduces a level of transluscence to the environment. When you are seated in a chiar, you can reasonably expect to see all the objects in the (modest-sized) room you are sitting in - but unless they are nearby and in-reach, you can't necessarily examine them closely, read text on them, or pick them up.

		The Seat class seeks to replicate the expected transluscent behavior - but much of the heavy lifting actually gets done in the Creature class and, of course, Invisible. Creature contains scope methods is_contained() and get_contained_by() to determine if a creature is seated and, if so, in / on what Seat obj. Creature also contains the chk_obj_in_reach() and chk_wrt_in_reach() methods to determine if a given object is in-reach of the seated creature. In Invisible, the standard error checking applied to nearly every err method includes an in_reach check and an admonition that "You'll have to exit the <Seat obj> to attempt that." if the object or writing is not in reach. 

	- Program Architecture:
		In addition to the introduction of 'translucence', there are a few other architectural consioderations around Seat. One is light. As of this writing, I haven't yet introduced a lighting system to Dark Castle but I do intend to. The idea is that, as part of being 'translucent', Seat will inherit light from the room. But traditional IF also includes small enclosed non-room spaces that are opaque (e.g. the Closet and Fireplace in Hollywood Hijinks). These can be useful for some puzzles and  I'm planning to introduce them down the road. My current proposed class name is Nook.

		Speaking of class names, I debated heavily between Seat and Perch (naming is hard). Perch seems more generic. Seat comes with more expectations that something will be chair-like. But I had already started using Seat by the time I thought of Perch so Seat it is.

		Other MixIns are possible - for example BehindMixIn and UnderMixIn - and I am considering eventually building complex and specific furniture by combining these with Seat. IF also traditionally contains Bed objects. In fact Enchanter has a sleep() mechanic that requires a Bed and I am intending to implement something similar in DC. The intention is that Bed will inherit from Seat and include the sleep() method. I like the idea that the games hint system can be embeded in sleep() generated dreams.

		A final architectural decision I had to make regarding Seat was whether it would be a one-off special case or whether I would finally sucumb to an infinite-depth of recursive receptacles. Someday I will probably need to do the latter but for now I am going with the special-case approach. So no chairs on diases on stages floating in pools for Dark Castle... at least not yet! For now, Seat is a Creature Container - not a universal deeper level of room node.

	- Game Design:
		Chairs are present in traditional IF but are not typically a vital feature. The Seat class has been a lot of work so one might reasonably ask "why bother?" The answer is that Seat is really the precursor of Vehicle. In fact, a Vehicle is just a Seat that moves from room to room - with all of the same 'translucency' challenges as Seat. And the archtypal Vehicle puzzle is for the player to need to grab an object that can only be reached from thw moving Vehicle (e.g. the inflatable boat in Zork).

		I'm not planning to add vehicle in the immediate future, but reading Tim Anderson's wonderful 'The History of Zork' (https://gunkies.org/wiki/History_of_Zork) brought home for me how complicated vehicles could be if I didn't plan for them from the start. So, since I was refactoring Doors, Containers, and Surfaces already, this seemed like the right time to sort out Seats.

	- Class Attributes:
		in_reach_lst: in_reach_lst provides a list of Containers or ViewOnly objects that are in-reach to the Seat obj. If the room name is given then all Items in Room.floor_lst are treated as in-reach. Interestingly, unlesses explicitly added to in_reach, the Seat itself is not in_reach (if you wanted to examine a chair closely you would probably stand up first).

	- enter() and exit() methods [Seat class]:
		Overview: 
			put() can only place an obj in / on a Container if the object is an Item held in the putting creature's hand. take() has similar requirements. Since Creatures are not Items... how do they get in and out of a Seat? The answer is enter() and exit() - which work pretty much as you'd expect put() and take() commands for creatures to function.

		Implementation Detail:
			One interesting highlight to exit() is that exit_err() cannot use the std_err() call. This is because exit() is a method of Seat and, unless explicitly added to in_reach_lst, the Seat obj itself is not accessible when sitting. As a result, a special exception to this scope exclusion needs to be baked into exit_err().

			It's worth noting that in addition to the Seat.exit() verb method - which is specific to the Seat that the command-issueing creature is in / on - there is also a universal Creature.stand() method which will place a contained Creature in the Room.floor_lst independent of the Seat in question. This seemed a bit duplicative but 'stand' is a standard one-word 'get up from whereever' IF command so I replicated it in Dark Castle to follow convention.

		Program Architecture:	
			Perhaps what is highlighted most by enter() and exit() is the intereter blank space they expose. A player walking up to Dark Castle for the first time and wanting to sit in chair - even a player well versed in IF - would not initially use 'enter' or 'exit' commands. They would type 'sit on chair' or something similar.

			So why not use sit() rather than enter()? The challenge is that there will likely be other Creature-containing obj that inherit from Seat (e.g. Bed) where sit() would be the wrong command. So my intention with enter() and exit() is to create generic commands that can then be pointed to via object or class-specific synonyms (i.e. 'sit').

			This seems like a reasonable plan but it should be noted that, as of this writing, no such obj or class-specific synonym system exists and I don't really have a clear idea in my mind as to how to implement one. Thus begins the voyage ;-D
"""