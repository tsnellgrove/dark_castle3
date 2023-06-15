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
	def __init__(self, contain_lst, max_bulk, max_obj, prep):
		self._contain_lst = contain_lst # list of objects in the container
		self._max_bulk = max_bulk # maximum combined bulk the container can hold
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
	def max_bulk(self):
		return self._max_bulk

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
#		if self.is_item:
#			self.bulk -= item.bulk

	def chk_content_prohibited(self, obj):
		return obj.is_creature()

	def get_contained_bulk(self):
		return sum(element.bulk for element in self.contain_lst)

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
#		if self.is_item:
#			self.bulk += obj.bulk

		active_gs.buffer("Done")
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
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_bulk, max_obj, prep):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		ContainsMixIn.__init__(self, contain_lst, max_bulk, max_obj, prep)
		""" A simple non-takable container with no lid or lock. Can be a box or a shelf depending on 'prep'
		"""

class ContainerFixedLidded(ContainsMixIn, OpenableMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_bulk, max_obj, prep, is_open):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		ContainsMixIn.__init__(self, contain_lst, max_bulk, max_obj, prep)
		OpenableMixIn.__init__(self, is_open)
		""" A non-takable container with a lid but no lock.
		"""

class ContainerFixedLockable(LockableMixIn, ContainsMixIn, OpenableMixIn, ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, contain_lst, max_bulk, max_obj, prep, is_open, is_unlocked, key):
		ViewOnly.__init__(self, name, full_name, root_name, descript_key, writing)
		ContainsMixIn.__init__(self, contain_lst, max_bulk, max_obj, prep)
		OpenableMixIn.__init__(self, is_open)
		LockableMixIn.__init__(self, is_unlocked, key)
		""" A non-takable container with a lid and a lock.
		"""

class ContainerPortableSimple(ContainsMixIn, Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, bulk, contain_lst, max_bulk, max_obj, prep):
		Item.__init__(self, name, full_name, root_name, descript_key, writing, bulk)
		ContainsMixIn.__init__(self, contain_lst, max_bulk, max_obj, prep)
		""" A simple, takable container with no lid or lock. Can be a box or a surface (e.g. a tray) depending on 'prep'
		"""

	# *** scope method extensions ***
	def remove_item(self, item, active_gs):
		super(ContainerPortableSimple, self).remove_item(item, active_gs)
		""" Decrements Portable Container bulk when an Item is removed from the Container.
		"""
		self.bulk -= item.bulk
		return


	# *** verb method extensions ***
	def put(self, obj, active_gs, mode=None):
		super(ContainerPortableSimple, self).put(obj, active_gs, mode=None)
		""" Increments Portable Container bulk when an Item is put in the Container.
		"""
		if mode is None:
			mode = 'std'

		self.bulk += obj.bulk
		return

