# program: dark castle
# author: Tom Snellgrove
# module description: provides mix in classes for interactive objects

### import statements
from cleesh.class_std.base_class_def import ViewOnly
from cleesh.class_std.item_class_def import Item

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

	# *** simple methods ***

	def toggle(self, gs):
		if self.is_open == True:
			self.is_open = False
		else:
			self.is_open = True
		return self.is_open

	# *** display methods ***
	def has_cond(self, gs):
		return True

	def disp_cond(self, gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		if self.is_open == False:
			gs.io.buff_no_cr(f"The {self.full_name} is closed. ")
			return
		gs.io.buff_no_cr(f"The {self.full_name} is open. ") # is_open == True
		return 

    # *** verb methods ***
	def open(self, gs, mode=None):
		""" Opens a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		self.is_open = True

		gs.io.buff_cr()
		gs.io.buff_no_cr("Openned. ")
		if self.is_container():
			self.disp_contain(gs)
		gs.io.buff_cr()
		return

	def close(self, gs, mode=None):
		""" Closes a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		gs.io.buffer("Closed")

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
	def unlock(self, key_obj, gs, mode=None):
		""" Unlocks a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		gs.io.buffer("Unlocked")

		self.is_unlocked = True
		return

	def lock(self, key_obj, gs, mode=None):
		""" Locks a Door object.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero

		gs.io.buffer("Locked")

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
	def contain_lst_append(self, item, gs):
		self.contain_lst.append(item)
		if self.is_item(): # Increment Portable Container weight if Item is added
			self.increment_weight(item.weight)
			in_creature_inv, creature = gs.map.chk_obj_in_creature_inv(self, gs)
			if in_creature_inv:
				creature.increment_weight(item.weight)
		return

	def contain_lst_remove(self, item, gs):
		self.contain_lst.remove(item)
		if self.is_item(): # Decrement Portable Container weight if Item is removed
			self.decrement_weight(item.weight)
			in_creature_inv, creature = gs.map.chk_obj_in_creature_inv(self, gs)
			if in_creature_inv:
				creature.decrement_weight(item.weight)
		return


	# *** class identity methods ***
	def	is_container(self):
		return True

	def is_receptacle(self):
		return True


	# *** universal scope methods ***
	def chk_contain_item(self, item):
		""" Evaluates whether the passed object is contained within the methed-calling object. Called by Room.remove_item(). Only single level deep - does not check in containers.
		"""
		return item in self.contain_lst

	def get_contain_lst(self, gs):
		return self.contain_lst

	def get_vis_contain_lst(self, gs):
		""" Returns the list of visible objects contained in the referenced ('self') object
		"""
		if self.is_content_vis():
			node2_lst = []
			[node2_lst.extend(obj.get_vis_contain_lst(gs)) for obj in self.contain_lst]
			return self.contain_lst + node2_lst
		return []

	def remove_item(self, item, gs):
		if item in self.contain_lst:
			self.contain_lst_remove(item, gs)
			return
		for obj in self.contain_lst:
			if obj.is_container() and item in obj.contain_lst:
				obj.contain_lst_remove(item, gs)
				print(f"{item} removed from {obj}")
				return
		raise ValueError(f"Can't remove item {item} from Container {self.name}")


	# *** receptacle inventory methods - for internal item mgmt ***
	def get_top_lvl_inv_lst(self, gs):
		""" Returns the list of accessable top-level items in the inventory of the methed-calling object.
		"""
		if self.is_container() and ((self.is_openable() and self.is_open) or not self.is_openable()):
			return self.contain_lst
		return []

	def get_inv_lst(self, gs):
		""" Returns the list of all accessable items in the inventory of the methed-calling receptacle.
		"""
		inv_lst = self.get_top_lvl_inv_lst(gs)
		for item in inv_lst:
			if item.is_container() and ((item.is_openable() and item.is_open) or not item.is_openable()):
				inv_lst.extend(item.get_contain_lst(gs)) # add all contained items
		return inv_lst

	def chk_item_in_inv(self, item, gs):
		""" Evaluates whether the passed object is within the accessable inventory of methed-calling object. Checks two levels deep.
		"""
		return item in self.get_inv_lst(gs)
#		if self.chk_contain_item(item): # check in container contain_lst
#			return True
#		for obj in self.get_top_lvl_inv_lst(gs): # check in portable containers
#			if obj.chk_contain_item(item): 
#				return True
#		return False


	# *** container-specific scope methods ***
	def is_empty(self):
		return not self.contain_lst

	def chk_has_capacity(self):
		return len(self.contain_lst) < self.max_obj

	def chk_content_prohibited(self, obj):
		if obj.is_creature(): # can't put creatures in containers
			return True
		if self.is_item() and obj.is_container(): # can't put portable containers in portable containers
			return True
		return False

	def get_contained_weight(self):
		return sum(element.weight for element in self.contain_lst)

	def is_content_vis(self):
		""" Checks whether the contents of the referenced object are visible.
		"""
		return (self.is_openable() and self.is_open) or not self.is_openable()

	def chk_wrt_is_vis(self, writing, gs):
		""" Evaluates whether the passed writing is visible within the methed-calling object.
		"""
		return any(obj.writing == writing for obj in self.get_vis_contain_lst(gs))


	# *** display methods ***
	def has_contain(self, gs):
		return True
	
	def disp_contain(self, gs):
		""" Displays a description of the visible items held by the obj. Used in examine().
		"""
		if self.is_content_vis():
			if self.is_empty():
				gs.io.buff_no_cr(f"The {self.full_name} is empty. ")
				return
			contain_txt_lst = [obj.full_name for obj in self.contain_lst if obj != gs.core.hero]
			if contain_txt_lst:
				contain_str = ", ".join(contain_txt_lst)
				gs.io.buff_no_cr(f"The {self.full_name} contains: {contain_str}. ")
			for obj in self.contain_lst:
				if obj != gs.core.hero:
					obj.disp_contain(gs)
		return 


	# *** verb methods ***
	def put(self, obj, gs, mode=None):
		""" Puts an Item in a Container or on a Surface.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero
		
		creature.hand_lst_remove(obj)
		self.contain_lst_append(obj, gs)

		gs.io.buffer("Done")
		return


	# *** debug methods ***
	def capacity(self, gs, mode=None):
		""" Reports the capacity of a Container. Only usable in debug mode.
		"""
		if mode is None:
			mode = 'std'
		
		gs.io.buffer(f"The weight capacity of the {self.full_name} is {self.max_weight}.")
		gs.io.buffer(f"The object count capacity of the {self.full_name} is {self.max_obj}.")
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

class ContainerFixedLidded(OpenableMixIn, ContainerFixedSimple):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep, is_open):
		ContainerFixedSimple.__init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_weight, max_obj, prep)
		OpenableMixIn.__init__(self, is_open)
		""" A non-takable container with a lid but no lock.
		"""

class ContainerFixedLockable(LockableMixIn, ContainerFixedLidded):
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

	# *** container-specific scope methods ***
	def chk_content_prohibited(self, obj):
		return obj.is_seat()

	# *** verb methods ***
	def enter(self, gs, mode=None, creature=None):
		""" Sits a creature in a Seat
		"""
		if mode is None: # destermine default attributes
			mode = 'std'
		if creature is None:
			creature = gs.core.hero

		room = gs.map.get_obj_room(creature, gs)
		room.floor_lst_remove(creature)
		self.contain_lst_append(creature, gs)

		if room != gs.map.hero_rm: # if hero_creature not in current room, exit with no display
			return 
		
		if creature == gs.core.hero:
			gs.io.buffer(f"You are now seated in the {self.full_name}.")
			gs.io.buff_s(f"{creature.name}_enter_{self.descript_key}")
			if len(self.in_reach_lst) > 0:
				creature.disp_in_reach(gs)
		else:
			gs.io.buffer(f"The {creature.full_name} is now seated in the {self.full_name}.")
		return

	def exit(self, gs, mode=None, creature=None):
		""" Enables a creature to exit a Seat
		"""
		if mode is None: # destermine default attributes
			mode = 'std'
		if creature is None:
			creature = gs.core.hero

		room = gs.map.get_obj_room(creature, gs)
		room.floor_lst_append(creature)
		self.contain_lst_remove(creature, gs)

		if room != gs.map.hero_rm: # if hero_creature not in current room, exit with no display
			return 
		
		if creature == gs.core.hero:
			gs.io.buffer(f"You are now standing in the {room.full_name}.")
			gs.io.buff_s(f"{creature.name}_exit_{self.name}")
		else:
			gs.io.buffer(f"The {creature.full_name} is now standing in the {room.full_name}.")
		return


