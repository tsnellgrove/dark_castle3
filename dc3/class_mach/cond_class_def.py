# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: class deffinition module for Conditions


### classes
class PassThruCond(object):
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		cond_state = True
		return cond_state

	def __repr__(self):
		return f'Object { self.name } is of class { type(self).__name__ } '


class WeaponInHandCond(PassThruCond):
	def __init__(self, name, weapon_match_cond):
		super().__init__(name)
		self._weapon_match_cond = weapon_match_cond # Whether is_weapon() should be true or false to match cond

	@property
	def weapon_match_cond(self):
		return self._weapon_match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		creature = gs.hero
		return creature.in_hand_is_weapon() == self.weapon_match_cond


class CreatureItemCond(PassThruCond):
	def __init__(self, name, creature_obj, item_obj, match_cond):
		super().__init__(name)
		self._creature_obj = creature_obj # creature to check for item ownership
		self._item_obj = item_obj # item creature must possess for condition to be true
		self._match_cond = match_cond # boolean state to be matched

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_obj):
		self._creature_obj = new_obj

	@property
	def item_obj(self):
		return self._item_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		cond_state = self.item_obj in self.creature_obj.hand_lst
		return cond_state == self.match_cond


class StateCond(PassThruCond):
	def __init__(self, name, mach_state_cond):
		super().__init__(name)
		self._mach_state_cond = mach_state_cond # boolean test for passed in boolean value

	@property
	def mach_state_cond(self):
		return self._mach_state_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		return mach_state == self.mach_state_cond


class IsWeaponAndStateCond(StateCond):
	def __init__(self, name, weapon_match_cond, mach_state_cond):
		super().__init__(name, mach_state_cond)
		self._weapon_match_cond = weapon_match_cond # list of items that will meet condition

	@property
	def weapon_match_cond(self):
		return self._weapon_match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		creature = gs.hero
		weapon_in_hand = not creature.hand_is_empty() and creature.get_hand_item().is_weapon()
		return (mach_state == self.mach_state_cond) and (weapon_in_hand == self.weapon_match_cond)


class SwitchStateCond(PassThruCond):
	def __init__(self, name, switch_state_val_lst):
		super().__init__(name)
		self._switch_state_val_lst = switch_state_val_lst # list of switch state values to meet condition

	@property
	def switch_state_val_lst(self):
		return self._switch_state_val_lst

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		switch_state_lst = []
		for switch in cond_swicth_lst:
			switch_state_lst.append(switch.switch_state)
		return switch_state_lst == self.switch_state_val_lst


class LeverArrayCond(SwitchStateCond):
	def __init__(self, name, switch_state_val_lst):
		super().__init__(name, switch_state_val_lst)

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		target_val = mach_state
		current_val = 0
		for lever in cond_swicth_lst:
			if lever.switch_state == 'up':
				temp_val = 1
			else:
				temp_val = 0
			index_num = cond_swicth_lst.index(lever)
			temp_val = temp_val * self.switch_state_val_lst[index_num]
			current_val += temp_val
		return current_val == target_val


class NotTimerAndItemCond(PassThruCond):
	def __init__(self, name, timer_obj, item_obj):
		super().__init__(name)
		self._timer_obj = timer_obj
		self._item_obj = item_obj

	@property
	def timer_obj(self):
		return self._timer_obj

	@property
	def item_obj(self):
		return self._item_obj

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		cond_state = False
		if self.item_obj in gs.map.get_hero_rm(gs).floor_lst:
			cond_state = not self.timer_obj.active
		return cond_state


class StateItemInRoomCond(PassThruCond):
	def __init__(self, name, state_match, item_obj, item_in_room_match):
		super().__init__(name)
		self._state_match = state_match # boolean test for passed in boolean value
		self._item_obj = item_obj
		self._item_in_room_match = item_in_room_match

	@property
	def state_match(self):
		return self._state_match

	@property
	def item_obj(self):
		return self._item_obj

	@property
	def item_in_room_match(self):
		return self._item_in_room_match

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		room_obj = gs.map.get_hero_rm(gs)
		item_in_room = self.item_obj in room_obj.floor_lst
		return (
			mach_state == self.state_match 
			and item_in_room == self.item_in_room_match
			)


class TimerActiveCond(PassThruCond):
	def __init__(self, name, timer_obj, timer_active_bool):
		super().__init__(name)
		self._timer_obj = timer_obj
		self._timer_active_bool = timer_active_bool

	@property
	def timer_obj(self):
		return self._timer_obj

	@property
	def timer_active_bool(self):
		return self._timer_active_bool

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		cond_state = self.timer_obj.active == self.timer_active_bool
		return cond_state


class RoomCond(PassThruCond):
	def __init__(self, name, match_room, match_cond):
		super().__init__(name)
		self._match_room = match_room
		self._match_cond = match_cond

	@property
	def match_room(self):
		return self._match_room

	@match_room.setter
	def match_room(self, new_obj):
		self._match_room = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		room_obj = gs.map.get_hero_rm(gs)
		match_state = room_obj == self.match_room
		return self.match_cond == match_state


class InWorldCond(PassThruCond): # note: only works for obj in room.floor_lst
	def __init__(self, name, exist_obj, match_cond):
		super().__init__(name)
		self._exist_obj = exist_obj
		self._match_cond = match_cond

	@property
	def exist_obj(self):
		return self._exist_obj

	@exist_obj.setter
	def exist_obj(self, new_obj):
		self._exist_obj = new_obj

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		match_state = gs.map.chk_obj_exist(self.exist_obj, gs)
		return match_state == self.match_cond


class InWorldStateCond(InWorldCond): # note: only works for obj in room.floor_lst
	def __init__(self, name, exist_obj, match_cond):
		super().__init__(name, exist_obj, match_cond)

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		panel_dispensed = mach_state
		if panel_dispensed == False:
			match_state = gs.map.chk_obj_exist(self.exist_obj, gs)
			return match_state == self.match_cond
		else:
			return False


class WornCond(PassThruCond):
	def __init__(self, name, worn_garment, match_cond):
		super().__init__(name)
		self._worn_garment = worn_garment
		self._match_cond = match_cond

	@property
	def worn_garment(self):
		return self._worn_garment

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		creature = gs.hero
		return (self.worn_garment in creature.worn_lst) == self.match_cond


class InRoomCond(PassThruCond):
	def __init__(self, name, creature, match_room, match_cond):
		super().__init__(name)
		self._creature = creature
		self._match_room = match_room
		self._match_cond = match_cond

	@property
	def creature(self):
		return self._creature

	@creature.setter
	def creature(self, new_val):
		self._creature = new_val

	@property
	def match_room(self):
		return self._match_room

	@match_room.setter
	def match_room(self, new_val):
		self._match_room = new_val

	@property
	def match_cond(self):
		return self._match_cond

	def cond_check(self, gs, mach_state, cond_swicth_lst):
		room = gs.map.get_obj_room(self.creature, gs)
		return (room is self.match_room) == self.match_cond


