# program: dark castle v3.73
# name: Tom Snellgrove
# date: Oct 24, 2022
# description: room class deffinition module


### import
import random
from static_gbl import descript_dict, static_dict
from base_class_def import ViewOnly


### local functions


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

	# *** attribute methods ***
	def floor_lst_append(self, item):
		self._floor_lst.append(item)

	def floor_lst_extend(self, lst):
		self._floor_lst.extend(lst)

	def floor_lst_remove(self, item):
		self._floor_lst.remove(item)

	# *** simple object methods ***
	def get_title_str(self):
		return f"*** {self.full_name} ***"

	def has_cond(self):
		return True

	def has_contain(self, active_gs):
		return len(self.floor_lst) > 1

	# *** scope methods ***
	def get_vis_contain_lst(self, active_gs):
		""" Returns the list of visible objects contained in the method-calling object. In Room, provides the visible object scope.
		"""
		return_lst = []
		node1_only_lst = [self] + active_gs.map.get_door_lst(self) + self.feature_lst
		return_lst = return_lst + node1_only_lst
		for obj in self.floor_lst:
			return_lst += obj.get_vis_contain_lst(active_gs)
		return_lst = return_lst + self.floor_lst
		return return_lst

	def chk_wrt_is_vis(self, writing, active_gs):
		""" Evaluates whether the passed writing is visible within the methed-calling object.
		"""
		return any(obj.writing == writing for obj in self.get_vis_contain_lst(active_gs))

	def chk_is_vis(self, obj, active_gs):
		""" Evaluates whether the passed object is visible within the methed-calling object.
		"""
		return obj in self.get_vis_contain_lst(active_gs)

	def chk_contain_item(self, item, active_gs):
		""" Evaluates whether the passed object is contained within the methed-calling object.
		"""
		if item in self.floor_lst:
			return True
		if any(obj.chk_contain_lst(item) for obj in self.floor_lst):
			return True
		return False

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

	# *** complex object methods ***
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
		raise ValueError(f"Can't remove item {item} from room {self.name}")
		return 

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
				active_gs.buff_no_cr(f"There is a {obj.full_name} here. ")
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

	def go(self, dir, active_gs, creature = None):
		""" Moves a Creature from one room to another
		"""
		if creature is None:
			creature = active_gs.hero

		if not active_gs.map.chk_valid_dir(self, dir):
			active_gs.buffer(descript_dict[f"wrong_way_{random.randint(0, 4)}"])
			return
		door = active_gs.map.get_door(self, dir)
		if not isinstance(door, str) and door.is_open == False:
			active_gs.buffer(f"The {door.full_name} is closed.")
			return 

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


""" *** Module Documentation ***

	* Room class:

		Every space Burt can occupy is a 'room' - even if he is outside. All of the game's  visible objects (except Doors) are contained within Rooms. Rooms themselves (along with Doors) reside within the room-pairs of Map.
		
		Since everything Burt can interact with on a given turn (except Doors) is in the room that he's occupying, Room is the perfect place to determine object scope. All scope methods for both visible and invisble objects are in Room. Available exits are considered to be conditions of the Room and are presented when the Room is examined. The commands 'look' and 'examine room' have identical results.
						
		Program Architecture:
			Rooms are a good time to pause and discuss Receptacles and Nodes. 
			
			Any visible object that can hold an Item is a Receptacle (i.e. Containers, Creatures, and Surfaces). As discussed in the Container method, Receptacles are 'smart' (i.e. they know what they contain) and Items are 'dumb' (i.e. they know nothing about the container that holds them). This means that to generate a list of all visible objects in a room (e.g. via get_vis_contain_lst() ) we need to first compile a list of immediately available objects and then, if any of them are open Receptacles, we need to list all of the ojbects inside *them*. But what if one of the objects inside a Receptacle is, itself, a Receptacle? 
			
			In theory, this could get deeply recursive. One obvious way to avoid this is "Just don't create very many PortableContainers in the game." But, hypoetheically, the goal is here is to create a tool set that could be used by others to build their own text adventure games... so we would like to put in place some prescriptive guard rails.
			
			Before we solve the problem, we need some nomenclature to describe it. The terminology I've chosen is "Node", from the study of binary trees (though in this case we have a non-binary tree). Imagine an inverted "tree" with one "node" at the top. This is the Room object, node_0. One level below Room we have nodes for all the visible objects in the Room. These are the node_1 objects. Some of the node_1 objects may be Receptacles and their contents are represented by Nodes one level further down: the node_2 objects. By default when we reference a node_1 object we are discussing 'absolute' node level where the current Room is node_0. But it is also possible to talk about 'relative' node level - for example, if Burt is in the Main Hall and holding the shiny_sword, then the shiny_sword has an absolute node level of node_2 (Room => Creature => Item) but a node level of node_1 relative to Burt (Burt => Item). You will occasionally see node_1 or node_2 variables referenced in methods. In this case, absolute node level is being used.
			
			So now that we have have some terminology, the key question is: "How do we want the game to work?" Whe could use recursion to allow recepticales to be indefinitely nested... but tracking items like this is cumbersome and hard to represent to the user. At the other end of the spectrum, we could disallow any Receptacle nesting - but this seems heavy-handed. I've taken the capabilities and limitations of Zork are a source of guidance. Early in the game, when the player enters the Kitchen, they find a sack containing food and a bottle of water on a table. So PortableContainers nested on a Surface seems like a reasonable expectation. PortableContainers nested in Creatures and Containers also happens within the game. But there are no takable Creatures, few, if any, takable Surfaces, and few if any instances of PortableContainers nested in other PortableContainers. Adopting these limits allows us a fun simulation - but limits node level to 3 (Room => Receptacle => PortableContainer => Item) - which is a reasonable depth to manage and represent.
"""
