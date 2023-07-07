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
	
	def can_contain_temp(self):
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


### noun classes
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
			active_gs.buff_try_key(f"{creature.name}_enter_{self.name}")
		else:
			active_gs.buffer(f"The {creature.full_name} is now seated in the {self.full_name}.")
		return


	def exit(self, active_gs, mode=None, creature=None):
		""" Sits a creature in a Seat
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

