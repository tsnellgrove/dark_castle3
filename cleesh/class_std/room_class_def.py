# program: dark castle
# author: Tom Snellgrove
# module description: room class deffinition module


### import
from cleesh.class_std.invisible_class_def import Invisible
from cleesh.class_std.base_class_def import ViewOnly


### classes
class Room(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, feature_lst, floor_lst, invis_lst, init_desc_lst):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._feature_lst = feature_lst # list of descriptive obj in the room (can be examined but not interacted with)
		self._floor_lst = floor_lst # list of obj on the floor of the room that the player can interact with
		self._invis_lst = invis_lst # list of invisible obj in room
		self._init_desc_lst = init_desc_lst # list of InitDesc objects that provide the initial description of obj in the room
		""" Rooms are where everything happens in Dark Castle.
		"""

	# *** getters & setters ***
	@property
	def feature_lst(self):
		return self._feature_lst

	@property
	def floor_lst(self):
		return self._floor_lst

	@property
	def invis_lst(self):
		return self._invis_lst

	@property
	def init_desc_lst(self):
		return self._init_desc_lst

	# *** attrib methods ***
	def floor_lst_append(self, item):
		self.floor_lst.append(item)

#	def floor_lst_extend(self, lst):
#		self.floor_lst.extend(lst)

	def floor_lst_remove(self, item):
		self.floor_lst.remove(item)

#	def is_obj_on_floor(self, obj):
#		return (obj in self.floor_lst)

	# *** identity method ***
	def is_room(self):
		return True

	def is_receptacle(self):
		return True

	# *** universal scope methods ***
	def get_vis_contain_lst(self, gs):
		""" Returns the list of visible objects contained in the method-calling object. In Room, provides the visible object scope.
		"""
		return_lst = []
		node1_only_lst = [self] + gs.map.get_door_lst(self) + self.feature_lst + self.floor_lst
		return_lst = return_lst + node1_only_lst
		for obj in self.floor_lst:
			return_lst += obj.get_vis_contain_lst(gs)
		return return_lst

	def chk_contain_item(self, item, gs):
		""" Evaluates whether the passed object is contained within the methed-calling object. Called by Room.remove_item(). Only single level deep - does not check in containers.
		"""
		return item in self.floor_lst
##		if item in self.floor_lst:
##			return True
#		for obj in self.floor_lst: # based on how remove works, don't need to check for sub-containers
#			if obj.chk_contain_item(item):
#				return True
#		if any(obj.chk_contain_lst(item) for obj in self.floor_lst): # chk_contain_lst() is not defined in Room, so this will always return False
#			return True
##		return False


	def get_contain_lst(self, gs):
		return self.floor_lst + self.feature_lst + gs.map.get_door_lst(self)

	def remove_item(self, item, gs):
		""" Removes the passed object from the methed-calling object. In Room, is used to enable the take() method.
		"""
		if item in self.floor_lst:
			if self.init_desc_lst:
				for init_desc in self.init_desc_lst:
					if init_desc.linked_item == item:
						self.init_desc_lst.remove(init_desc)
			self.floor_lst_remove(item)
			return 
		for obj in self.floor_lst:
			if obj.chk_contain_item(item):
				obj.remove_item(item, gs)
				return
			for cont_obj in obj.get_vis_contain_lst(gs):
				if cont_obj.chk_contain_item(item):
					cont_obj.remove_item(item, gs)
					return
		raise ValueError(f"Can't remove item {item} from room {self.name}")
		return 

	
	# *** receptacle inventory methods - for internal item mgmt ***
	def get_top_lvl_inv_lst(self, gs):
		""" Returns the list of top-level objects in the inventory of the methed-calling object.
		"""
		return self.floor_lst

	def chk_item_in_inv(self, item, gs):
		""" Evaluates whether the passed object is within the inventory of methed-calling object. Checks three levels deep.
		"""
		if self.chk_contain_item(item): # check in foom floor_lst
			return True
		for obj in self.get_top_lvl_inv_lst(gs):
			if obj.is_receptacle(): # check in fixed containers and creatures
				if obj.chk_contain_item(item): 
					return True
				for deep_item in obj.contain_lst: # check in portable containers
					if deep_item.chk_contain_item(item):
						return True
		return False


	# *** room-specific scope methods ***
	def chk_wrt_is_vis(self, writing, gs):
		""" Evaluates whether the passed writing is visible within the methed-calling object.
		"""
		return any(obj.writing == writing for obj in self.get_vis_contain_lst(gs))

	def chk_is_vis(self, obj, gs):
		""" Evaluates whether the passed object is visible within the methed-calling object.
		"""
		return obj in self.get_vis_contain_lst(gs)

	def get_mach_lst(self, gs):
		""" Returns the list of Machine objects contained in the method-calling object. In Room, provides the Machine object scope.
		"""
		mach_lst = gs.core.univ_invis_lst.copy()
		for obj in self.get_vis_contain_lst(gs):
			if (obj.is_switch()) or (obj.is_mach() and obj.is_enabled): # in future, may add is_enabled attrib to Switch class
				mach_lst.append(obj)
			if obj.is_creature():
				for invis_obj in obj.invis_lst:
					if invis_obj.is_mach() and invis_obj.is_enabled:
						mach_lst.append(invis_obj)
		for obj in self.invis_lst:
			if (obj.is_mach() and obj.is_enabled):
				mach_lst.append(obj)
		return mach_lst

	def get_take_all_lst(self, gs):
		take_all_lst = []
		temp_lst = self.floor_lst.copy()
		for obj in self.floor_lst:
			if not obj.is_creature() and not (obj.is_container() and obj.is_item()):
				temp_lst += obj.get_vis_contain_lst(gs)
		for obj in temp_lst:
			if obj.is_item() and not obj.is_liquid():
				take_all_lst.append(obj)
		return take_all_lst


	# *** universal display methods ***
	def get_title_str(self, gs):
		if gs.core.hero.is_contained(gs):
			return f"*** {self.full_name}, in the {gs.core.hero.get_contained_by(gs).full_name} ***"
		else:
			return f"*** {self.full_name} ***"

	def has_cond(self, gs):
		return True

	def has_contain(self, gs):
		return len(self.floor_lst) > 1

	def disp_cond(self, gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		gs.io.buff_no_cr(gs.map.get_door_str(self))

	def disp_contain(self, gs):
		""" Displays a description of the visible items held by the obj. Used in examine().
		Order of display is from most to least static: 
			1. Initial Descriptions for viewonly & items (in order listed in init_desc_lst)
			2. ViewOnly (i.e. imovable furniture)
			3. Items (which are movable and may have already been moved)
			4. Creatures (which may move of their own volition)
		"""

		### organize floor_lst by type
		rm_item_lst = []
		rm_viewonly_lst = []
		rm_creature_lst = []
		for obj in self.floor_lst:
			if obj == gs.core.hero:
					pass
			elif obj.is_creature():
				rm_creature_lst.append(obj)
			elif not obj.is_item():
				rm_viewonly_lst.append(obj) # new
			else:
				rm_item_lst.append(obj)

		### buffer descriptions by type
		for init_desc in self.init_desc_lst:
			if init_desc.linked_item in rm_item_lst or rm_viewonly_lst:
				gs.io.buff_cr()
				gs.io.buff_cr()
				gs.io.buff_d_no_cr(init_desc.init_desc_key, init_desc.linked_item.full_name)
				if init_desc.linked_item in rm_item_lst:
					rm_item_lst.remove(init_desc.linked_item)
				else:
					rm_viewonly_lst.remove(init_desc.linked_item)
		for obj in rm_viewonly_lst:
			gs.io.buff_cr()
			gs.io.buff_cr()
			gs.io.buff_no_cr(f"There is a {obj.full_name} here")
			if gs.core.hero.is_contained(gs) and gs.core.hero.get_contained_by(gs) == obj:
				gs.io.buff_no_cr(" (which you are presently occupying)")
			gs.io.buff_no_cr(". ")
			obj.disp_contain(gs)
		if rm_item_lst:
			gs.io.buff_cr()
			gs.io.buff_cr()
			room_txt_lst = [obj.full_name for obj in rm_item_lst]
			room_item_str = ", ".join(room_txt_lst)
			gs.io.buff_no_cr(f"The following items are here: {room_item_str}. ")
			for obj in rm_item_lst:
				obj.disp_contain(gs)
		for creature in rm_creature_lst:
			gs.io.buff_cr()
			gs.io.buff_cr()
			gs.io.buff_no_cr(f"The {creature.full_name} is here. ")
			creature.disp_contain(gs)
		return

	# *** verb methods ***
	def go(self, dir, gs, creature=None, mode=None):
		""" Moves a Creature from one room to another
		"""
		if mode is None:
			mode = 'std'
		if creature is None:
			creature = gs.core.hero

		next_room = gs.map.get_next_room(self, dir)
		gs.map.hero_rm = next_room
		next_room.floor_lst_append(creature)
		self.floor_lst_remove(creature)

		if creature == gs.core.hero:
			next_room.examine(gs)
			return 
		if self == gs.map.hero_rm:
			gs.io.buffer(f"The {creature.full_name} goes {dir}")
		return 


class InitDesc(Invisible):
	def __init__(self, name, linked_item, init_desc_key):
		super().__init__(name)
		self._linked_item = linked_item # item the init_desc is associated with
		self._init_desc_key = init_desc_key # dict key for the initial description
		""" InitDesc class inherits from Invisible. It is used to provide the initial description of an item in a room. 
		"""

	# *** getters & setters ***
	@property
	def linked_item(self):
		return self._linked_item
	
	@linked_item.setter
	def linked_item(self, new_item):
		self._linked_item = new_item

	@property
	def init_desc_key(self):
		return self._init_desc_key




