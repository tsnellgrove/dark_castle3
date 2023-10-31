# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: room class deffinition module


### import
from dc3.class_std.base_class_def import ViewOnly


### classes
class Room(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, feature_lst, floor_lst, invis_lst):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._feature_lst = feature_lst # list of descriptive obj in the room (can be examined but not interacted with)
		self._floor_lst = floor_lst # list of obj on the floor of the room that the player can interact with
		self._invis_lst = invis_lst # list of invisible obj in room
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

	# *** attrib methods ***
	def floor_lst_append(self, item):
		self._floor_lst.append(item)

	def floor_lst_extend(self, lst):
		self._floor_lst.extend(lst)

	def floor_lst_remove(self, item):
		self._floor_lst.remove(item)

	# *** identity method ***
	def is_room(self):
		return True

	def is_receptacle(self):
		return True

	# *** universal scope methods ***
	def get_vis_contain_lst(self, active_gs):
		""" Returns the list of visible objects contained in the method-calling object. In Room, provides the visible object scope.
		"""
		return_lst = []
		node1_only_lst = [self] + active_gs.map.get_door_lst(self) + self.feature_lst + self.floor_lst
		return_lst = return_lst + node1_only_lst
		for obj in self.floor_lst:
			return_lst += obj.get_vis_contain_lst(active_gs)
#		return_lst = return_lst + self.floor_lst
#		return return_lst
#		return return_lst + self.floor_lst
		return return_lst

	def chk_contain_item(self, item, active_gs):
		""" Evaluates whether the passed object is contained within the methed-calling object. Called by Room.remove_item()
		"""
		if item in self.floor_lst:
			return True
		if any(obj.chk_contain_lst(item) for obj in self.floor_lst):
			return True
		return False

	def get_contain_lst(self, active_gs):
		return self.floor_lst + self.feature_lst + active_gs.map.get_door_lst(self)

	def remove_item(self, item, active_gs):
		""" Removes the passed object from the methed-calling object. In Room, is used to enable the take() method.
		"""
		if item in self.floor_lst:
			self.floor_lst_remove(item)
			return 
		for obj in self.floor_lst:
			if obj.chk_contain_item(item):
				obj.remove_item(item, active_gs)
				return
			for cont_obj in obj.get_vis_contain_lst(active_gs):
				if cont_obj.chk_contain_item(item):
					cont_obj.remove_item(item, active_gs)
					return
		raise ValueError(f"Can't remove item {item} from room {self.name}")
		return 


	# *** room-specific scope methods ***
	def chk_wrt_is_vis(self, writing, active_gs):
		""" Evaluates whether the passed writing is visible within the methed-calling object.
		"""
		return any(obj.writing == writing for obj in self.get_vis_contain_lst(active_gs))

	def chk_is_vis(self, obj, active_gs):
		""" Evaluates whether the passed object is visible within the methed-calling object.
		"""
		return obj in self.get_vis_contain_lst(active_gs)

	def get_mach_lst(self, active_gs):
		""" Returns the list of Machine objects contained in the method-calling object. In Room, provides the Machine object scope.
		"""
		mach_lst = []
		scope_lst = self.get_vis_contain_lst(active_gs) + self.invis_lst
		for obj in scope_lst:
			if obj.is_mach():
				mach_lst.append(obj)
			if obj.is_creature():
				for invis_obj in obj.invis_lst:
					if invis_obj.is_mach():
						mach_lst.append(invis_obj)
		return mach_lst


	# *** universal display methods ***
	def get_title_str(self, active_gs):
		if active_gs.hero.is_contained(active_gs):
			return f"*** {self.full_name}, in the {active_gs.hero.get_contained_by(active_gs).full_name} ***"
		else:
			return f"*** {self.full_name} ***"

	def has_cond(self, active_gs):
		return True

	def has_contain(self, active_gs):
		return len(self.floor_lst) > 1

	def disp_cond(self, active_gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		active_gs.buff_no_cr(active_gs.map.get_door_str(self))

	def disp_contain(self, active_gs):
		""" Displays a description of the visible items held by the obj. Used in examine().
		"""
		room_item_lst = []
		for obj in self.floor_lst:
			if obj == active_gs.hero:
					pass
			elif not obj.is_item():
				active_gs.buff_cr()
				active_gs.buff_cr()
				active_gs.buff_no_cr(f"There is a {obj.full_name} here")
				if active_gs.hero.is_contained(active_gs) and active_gs.hero.get_contained_by(active_gs) == obj:
					active_gs.buff_no_cr(" (which you are presently occupying)")
				active_gs.buff_no_cr(". ")
				obj.disp_contain(active_gs)
			else:
				room_item_lst.append(obj)
		if room_item_lst:
			active_gs.buff_cr()
			active_gs.buff_cr()
			room_txt_lst = [obj.full_name for obj in room_item_lst]
			room_item_str = ", ".join(room_txt_lst)
			active_gs.buff_no_cr(f"The following items are here: {room_item_str}. ")
			for obj in room_item_lst:
				obj.disp_contain(active_gs)
		return

	# *** verb methods ***
	def go(self, dir, active_gs, creature=None, mode=None):
		""" Moves a Creature from one room to another
		"""
		if mode is None:
			mode = 'std'
		if creature is None:
			creature = active_gs.hero

		next_room = active_gs.map.get_next_room(self, dir)
##			active_gs.set_room(next_room)
		next_room.floor_lst_append(creature)
		self.floor_lst_remove(creature)

		if creature == active_gs.hero:
			next_room.examine(active_gs)
			return 
		if self == active_gs.get_room():
			active_gs.buffer(f"The {creature.full_name} goes {dir}")
		return 
