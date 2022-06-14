# program: dark castle v3.64
# name: Tom Snellgrove
# date: June 7, 2022
# description: class deffinition module for Conditions


### import


### classes
class PassThruCond(object):
		def __init__(self, name):
				self._name = name

		@property
		def name(self):
				return self._name

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = True
				return cond_state

		def __repr__(self):
				return f'Object { self.name } is of class { type(self).__name__ } '

class NotInHandCond(PassThruCond):
		def __init__(self, name, not_in_hand_lst):
				super().__init__(name)
				self._not_in_hand_lst = not_in_hand_lst # list of items that will not meet condition

		@property
		def not_in_hand_lst(self):
				return self._not_in_hand_lst

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = True
				hand_lst = active_gs.get_hand_lst()
				for item in self.not_in_hand_lst:
						if item in hand_lst:
								cond_state = False
				return cond_state

class CreatureItemCond(PassThruCond):
		def __init__(self, name, creature_obj, item_obj):
				super().__init__(name)
				self._creature_obj = creature_obj # creature to check for item ownership
				self._item_obj = item_obj # item creature must possess for condition to be true

		@property
		def creature_obj(self):
				return self._creature_obj

		@creature_obj.setter
		def creature_obj(self, new_obj):
				self._creature_obj = new_obj

		@property
		def item_obj(self):
				return self._item_obj

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = self.item_obj in self.creature_obj.creature_items_lst
				return cond_state


class StateCond(PassThruCond):
		def __init__(self, name, mach_state_cond):
				super().__init__(name)
				self._mach_state_cond = mach_state_cond # boolean test for passed in boolean value

		@property
		def mach_state_cond(self):
				return self._mach_state_cond

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				return mach_state == self.mach_state_cond

class InHandAndStateCond(StateCond):
		def __init__(self, name, in_hand_lst, mach_state_cond):
				super().__init__(name, mach_state_cond)
				self._in_hand_lst = in_hand_lst # list of items that will meet condition

		@property
		def in_hand_lst(self):
				return self._in_hand_lst

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = False
				if mach_state == self.mach_state_cond:
						hand_lst = active_gs.get_hand_lst()
						for item in self.in_hand_lst:
								if item in hand_lst:
										cond_state = True
				return cond_state

class SwitchStateCond(PassThruCond):
		def __init__(self, name, switch_state_val_lst):
				super().__init__(name)
				self._switch_state_val_lst = switch_state_val_lst # list of switch state values to meet condition

		@property
		def switch_state_val_lst(self):
				return self._switch_state_val_lst

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				switch_state_lst = []
				for switch in cond_swicth_lst:
						switch_state_lst.append(switch.switch_state)
				return switch_state_lst == self.switch_state_val_lst

class LeverArrayCond(SwitchStateCond):
		def __init__(self, name, switch_state_val_lst):
				super().__init__(name, switch_state_val_lst)

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
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

class RoomCond(PassThruCond):
		def __init__(self, name, match_room_name):
				super().__init__(name)
				self._match_room_name = match_room_name # room being checked for

		@property
		def match_room_name(self):
				return self._match_room_name

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				room_obj = active_gs.get_room()
				room_name = room_obj.name
				return room_name == self.match_room_name

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

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = False
				if self.item_obj in active_gs.get_room().room_obj_lst:
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

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				room_obj = active_gs.get_room()
				item_in_room = self.item_obj in room_obj.room_obj_lst
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

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = self.timer_obj.active == self.timer_active_bool
				return cond_state

class InHandAndRoomCond(PassThruCond):
		def __init__(self, name, in_hand_lst, match_room_name):
				super().__init__(name)
				self._in_hand_lst = in_hand_lst # list of items that will meet condition
				self._match_room_name = match_room_name
				
		@property
		def in_hand_lst(self):
				return self._in_hand_lst

		@in_hand_lst.setter
		def in_hand_lst(self, new_lst):
				self._in_hand_lst = new_lst

		@property
		def match_room_name(self):
				return self._match_room_name

		@match_room_name.setter
		def match_room_name(self, new_obj):
				self._match_room_name = new_obj

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = False
				hand_lst = active_gs.get_hand_lst()
				in_hand = hand_lst[0]
				room_obj = active_gs.get_room()
				if (room_obj.name == match_room_name and in_hand in self.in_hand_lst):
						cond_state == True
				return cond_state

class InHandAndExistInWorldCond(PassThruCond):
		def __init__(self, name, in_hand_lst, exist_obj):
				super().__init__(name)
				self._in_hand_lst = in_hand_lst # list of items that will meet condition
				self._exist_obj = exist_obj

		@property
		def in_hand_lst(self):
				return self._in_hand_lst

		@in_hand_lst.setter
		def in_hand_lst(self, new_lst):
				self._in_hand_lst = new_lst

		@property
		def exist_obj(self):
				return self._exist_obj

		@exist_obj.setter
		def exist_obj(self, new_obj):
				self._exist_obj = new_obj

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = False
				hand_lst = active_gs.get_hand_lst()
				in_hand = hand_lst[0]
				if in_hand not in in_hand_lst:
						return cond_state
				for room in active_gs.room_lst:
						if self.exist_obj in room.room_obj_lst:
								cond_state = True
				return cond_state

class InHandAndGarmentWornCond(PassThruCond):
		def __init__(self, name, in_hand_lst, worn_garment):
				super().__init__(name)
				self._in_hand_lst = in_hand_lst # list of items that will meet condition
				self._worn_garment = worn_garment
				
		@property
		def in_hand_lst(self):
				return self._in_hand_lst

		@property
		def worn_garment(self):
				return self._worn_garment

		def cond_check(self, active_gs, mach_state, cond_swicth_lst):
				cond_state = False
				hand_lst = active_gs.get_hand_lst()
				in_hand = hand_lst[0]
				worn_lst = active_gs.get_worn_lst()
				if (self.worn_garment in worn_lst and in_hand in self.in_hand_lst):
						cond_state == True
				return cond_state
