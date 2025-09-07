# program: cleesh engine
# author: Tom Snellgrove
# module description: class deffinition module for Conditions

# *** summary of condition classes ***

# Condition class (x) : inherits from (Y) : cond_check() method returns (Z)
#-------------------    -------------       ---------------------------------
# TrueCond :			Invisible :			True
# WornCond :			TrueCond :			match garment is worn
# CreatureContainedCond:TrueCond :			match creature contained in obj
# ObjOnRmFlrCond:		TrueCond :			match obj on rm floor
# ObjInRmCond :			TrueCond :			match obj room to match_rm
# ObjInWorldCond :		TrueCond :			match obj in world
# ItemInHandCond :		TrueCond :			match obj in hand to match_cond
# ObjInInvCond :		ItemInHandCond:		match obj in creature inventory
# WeaponInHandCond : 	TrueCond :			match on creature holding weapon
# MachStateCond : 		TrueCond :		  	match mach_state
# TimerActiveCond :		TrueCond :			match timer_obj.active
# SwitchStateCond : 	TrueCond :		 	match switch_state_lst
# LeverArrayCond : 		SwitchStateCond :	sum of lever_val_lst == mach_state


### imports ###
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class TrueCond(Invisible):
	def __init__(self, name):
		super().__init__(name)
		""" TrueCond class inherits from Invisible. All other condition classes inherit from TrueCond. 
		"""

	def cond_check(self, gs, mach_state):
		return True
		# Note 1: can re-use in child Conds w/ super().cond_check() because super() only returns to local scope
		# Note 2: using super() approach allows for additional checks in TrueCond down the road
		# Note 3: if Cond does not inherit from TrueCond, then super() will NOT work; check is_valid directly
		# Note 4: (I may need to solve this down the road if I add more validation checks to TrueCond)


class WornCond(TrueCond):
	def __init__(self, name, worn_garment, creature_obj, match_cond):
		super().__init__(name)
		self._worn_garment = worn_garment
		self._creature_obj = creature_obj
		self._match_cond = match_cond

	@property
	def worn_garment(self):
		return self._worn_garment

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_obj):
		self._creature_obj = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (self.worn_garment in self.creature_obj.worn_lst) == self.match_cond


class CreatureContainedCond(TrueCond):
	def __init__(self, name, seat_obj, creature_obj, match_cond):
		super().__init__(name)
		self._seat_obj = seat_obj
		self._creature_obj = creature_obj
		self._match_cond = match_cond

	@property
	def seat_obj(self):
		return self._seat_obj

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_obj):
		self._creature_obj = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (self.creature_obj.is_contained(gs) and (self.creature_obj.get_contained_by(gs) == self.seat_obj)) == self.match_cond


class ObjOnRmFlrCond(TrueCond):
	""" Condition to check whether an object is on the floor of a specified room. Top-level only.
	"""
	def __init__(self, name, match_room, obj, match_cond):
		super().__init__(name)
		self._match_room = match_room
		self._obj = obj
		self._match_cond = match_cond

	@property
	def match_room(self):
		return self._match_room

	@match_room.setter
	def match_room(self, new_val):
		self._match_room = new_val

	@property
	def obj(self):
		return self._obj

	@obj.setter
	def obj(self, new_val):
		self._obj = new_val

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (self.match_room.chk_contain_item(self.obj, gs) == self.match_cond)


class ObjInRmCond(TrueCond):
	""" Uses map.get_obj_room() instead of room.chk_item_in_inv() to be more general.
	"""
	def __init__(self, name, match_room, obj, match_cond):
		super().__init__(name)
		self._match_room = match_room
		self._obj = obj
		self._match_cond = match_cond

	@property
	def match_room(self):
		return self._match_room

	@match_room.setter
	def match_room(self, new_val):
		self._match_room = new_val

	@property
	def obj(self):
		return self._obj

	@obj.setter
	def obj(self, new_val):
		self._obj = new_val

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (gs.map.get_obj_room(self.obj, gs) is self.match_room) == self.match_cond


class ObjInWorldCond(TrueCond):
	def __init__(self, name, obj, match_cond):
		super().__init__(name)
		self._obj = obj
		self._match_cond = match_cond

	@property
	def obj(self):
		return self._obj

	@obj.setter
	def obj(self, new_obj):
		self._obj = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (gs.map.chk_obj_exist(self.obj, gs) == self.match_cond)


class ItemInHandCond(TrueCond):
	def __init__(self, name, item_obj, creature_obj, match_cond):
		super().__init__(name)
		self._item_obj = item_obj # item creature must possess for condition to be true
		self._creature_obj = creature_obj # creature to check for item ownership
		self._match_cond = match_cond # boolean state to be matched

	@property
	def item_obj(self):
		return self._item_obj

	@item_obj.setter
	def item_obj(self, new_obj):
		self._item_obj = new_obj

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_obj):
		self._creature_obj = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (self.item_obj in self.creature_obj.hand_lst) == self.match_cond

class ObjInInvCond(ItemInHandCond):
	def __init__(self, name, item_obj, creature_obj, match_cond):
		super().__init__(name, item_obj, creature_obj, match_cond)

	def cond_check(self, gs, mach_state):
		return (self.creature_obj.chk_item_in_inv(self.item_obj, gs) == self.match_cond)

class WeaponInHandCond(TrueCond):
	def __init__(self, name, creature_obj, match_cond):
		super().__init__(name)
		self._creature_obj = creature_obj # creature to check for holding weapon
		self._match_cond = match_cond # Whether is_weapon() should be true or false to match cond

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_obj):
		self._creature_obj = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (self.creature_obj.in_hand_is_weapon() == self.match_cond)


class MachStateCond(TrueCond):
	def __init__(self, name, tgt_state, match_cond):
		super().__init__(name)
		self._tgt_state = tgt_state # target mach state value to test for match
		self._match_cond = match_cond # bool indicatting whether state should match or not macth

	@property
	def match_cond(self):
		return self._match_cond

	@property
	def tgt_state(self):
		return self._tgt_state

	def cond_check(self, gs, mach_state):
		return (mach_state == self.tgt_state) == self.match_cond


class TimerActiveCond(TrueCond):
	def __init__(self, name, timer_obj, match_cond):
		super().__init__(name)
		self._timer_obj = timer_obj
		self._match_cond = match_cond

	@property
	def timer_obj(self):
		return self._timer_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state):
		return (self.timer_obj.is_active == self.match_cond)


class SwitchStateCond(TrueCond):
	def __init__(self, name, cond_switch_lst, match_cond_lst):
		super().__init__(name)
		self._cond_switch_lst = cond_switch_lst # list of switches that impact condition
		self._match_cond_lst = match_cond_lst # list of switch state values to meet condition

	@property
	def cond_switch_lst(self):
		return self._cond_switch_lst

	@property
	def match_cond_lst(self):
		return self._match_cond_lst

	def cond_check(self, gs, mach_state):
		for idx, switch in enumerate(self.cond_switch_lst):
			if switch.switch_state != self.match_cond_lst[idx]:
				return False
		return True # if any switches in list are wrong value return Flase, else return True


class LeverArrayCond(SwitchStateCond):
	def __init__(self, name, cond_switch_lst, match_cond_lst): # target value lives in mach_state as a machine attribute
		super().__init__(name, cond_switch_lst, match_cond_lst) # match_cond_lst == list of values for levers that are up; same len as cond_swtch_lst

	def cond_check(self, gs, mach_state):
		array_val = 0
		for idx, lever in enumerate(self.cond_switch_lst):
			if lever.switch_state == 'up':
				array_val += self.match_cond_lst[idx]
		return (array_val == mach_state)

