# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for Results


### import



# *** summary of result classes ***

# Result class (x) : 		inherits from (Y) : result_exe() method performs (Z)
#-------------------    	-------------       ---------------------------------

# *** new ***
# BaseResult :				N/A (is parent) :	buffer using result.name as key if event in rm; set mach_state
# EndResult :				BaseResult :		base + set ending val, set is_end = True
# ChgDescriptResult	:		BaseResult :		base + change obj descript_key
# GiveItemResult : 			BaseResult :		base + give item_obj to tgt_creature
# TakeItemResult :			BaseResult :		base + creature_obj takes item_obj
# DispenseObjResult :		BaseResult :		base + dispense obj to room

# *** legacy ***
# BufferOnlyResult :		N/A (is parent) :	buffer value assiciated w/ result_name key

# *** simple cases ***
# StartTimerResult :		BufferOnlyResult :	buff, starts timer [not called]
# RemoveObjResult :			<TBD> :				remove obj from game [new result for timer combo]
# TravelResult :			BufferOnlyResult :	buff, creature attempts to go dir [not called]

# *** refactor cases ***
# AttackBurtResult :		BufferOnlyResult :	buff, creature attacks burt [REFACT?] [address in_hand in creature.attack()?]
# DoorToggleResult :		BufferOnlyResult :	toggles door state; buff output [REFACT?]

# *** combo cases ***
# TimerAndCreatureItemResult StartTimerResult :	buff, starts timer and removes obj from creature hand [REFACT w/ eat???] [COMBO]

# deleted
# BufferAndEndResult :		BufferOnlyResult :	buffer, set ending val, set is_end = True
# ChgCreatureDescAndStateResult BufferOnlyResult : buff, change creature descript, set mach_state = True
# BufferAndGiveResult :		BufferOnlyResult :	buff, obj => hero hand; sets mach_state = True [need creature attrib]
# PutItemInHandResult :		BufferOnlyResult :	buff, put item in creature hand, remove item from creature bkpk [REFACT w/ take?]
# AddObjToRoomResult :		BufferOnlyResult :	buff, obj => hero_rm.floor_lst; sets mach_state = True [get mach rm? atttrib name => obj not item?][not called]
# AddObjChgDescriptResult : BufferOnlyResult :	AddObjToRoomResult + chg obj descript key + mach_state = True [COMBO]
# AddObjToRoomAndDescriptResult : BOResult :	similar to AddObjChgDescriptResult; chg rm descript [COMBO] [DEDUP]

### classes

### *** NEW RESULT CLASSES ***

class BaseResult(object):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override):
		self._name = name
		self._cmd_override = cmd_override # does the triggered pre-action over-ride the 'standard' response to player command?
		self._is_mach_state_set = is_mach_state_set # bool where True indicates that mach_state will be set
		self._mach_state_val = mach_state_val # value mach_state should be set to if is_mach_state_set is True; None if not set

	@property
	def name(self):
		return self._name

	@property
	def cmd_override(self):
		return self._cmd_override

	@property
	def is_mach_state_set(self):
		return self._is_mach_state_set

	@property
	def is_mach_state_set(self):
		return self._is_mach_state_set

	@property
	def mach_state_val(self):
		return self._mach_state_val

	def result_exe(self, gs, mach_state, alert_anchor): # need to add alert_anchor attrib to call
		if alert_anchor.is_room():
			event_rm = alert_anchor
		else:
			event_rm = gs.map.get_obj_room(alert_anchor, gs)
		if gs.map.hero_rm == event_rm:
			gs.io.buff_s(self.name)
		if self.is_mach_state_set:
			mach_state = self.mach_state_val
		return mach_state, self.cmd_override

	def __repr__(self):
		return f'Object { self.name } is of class { type(self).__name__ } '


class EndResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, ending):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._ending = ending # game ending - typically 'died' due to a room hazzard

	@property
	def ending(self):
		return self._ending

	def result_exe(self, gs, mach_state, alert_anchor):
		gs.end.game_ending = self.ending
		gs.end.is_end = True
		return super(EndResult, self).result_exe(gs, mach_state, alert_anchor)


class ChgDescriptResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, obj, new_descript_key):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._obj = obj # the obj who's description will be changed
		self._new_descript_key = new_descript_key # the obj's new decript_key

	@property
	def obj(self):
		return self._obj

	@obj.setter
	def obj(self, new_val):
		self._obj = new_val

	@property
	def new_descript_key(self):
		return self._new_descript_key

	def result_exe(self, gs, mach_state, alert_anchor):
		self.obj.descript_key = self.new_descript_key
		return super(ChgDescriptResult, self).result_exe(gs, mach_state, alert_anchor)


class GiveItemResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, item_obj, tgt_creature):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._item_obj = item_obj # item to be given to tgt_creature
		self._tgt_creature = tgt_creature # creature to whom the item_obj will be given

	@property
	def item_obj(self):
		return self._item_obj

	@property
	def tgt_creature(self):
		return self._tgt_creature

	@tgt_creature.setter
	def tgt_creature(self, new_obj):
		self._tgt_creature = new_obj

	def result_exe(self, gs, mach_state, alert_anchor):
		self.tgt_creature.put_in_hand(self.item_obj, gs)
		return super(GiveItemResult, self).result_exe(gs, mach_state, alert_anchor) 
		# Note: if mach_state was a class attrib of BaseResult, 
			# could call super().result_exe() in GiveItemResult.result_exe body
			# and then return super()mach_state, super().cmd_override


class TakeItemResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, creature_obj, item_obj):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._creature_obj = creature_obj # creature that will take obj
		self._item_obj = item_obj # obj to be taken

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_val):
		self._creature_obj = new_val

	@property
	def item_obj(self):
		return self._item_obj

	def result_exe(self, gs, mach_state, alert_anchor):
		gs.map.get_obj_room(self.creature_obj, gs).remove_item(self.item_obj, gs)
		self.creature_obj.put_in_hand(self.item_obj, gs)
		return super(TakeItemResult, self).result_exe(gs, mach_state, alert_anchor)


class DispenseObjResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, dispense_obj, room_obj):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._dispense_obj = dispense_obj # obj to be dispensed to room.floor_lst
		self._room_obj = room_obj # room that obj will be dispensed to

	@property
	def dispense_obj(self):
		return self._dispense_obj

	@dispense_obj.setter
	def dispense_obj(self, new_val):
		self._dispense_obj = new_val

	@property
	def room_obj(self):
		return self._room_obj

	@room_obj.setter
	def room_obj(self, new_val):
		self._room_obj = new_val

	def result_exe(self, gs, mach_state, alert_anchor):
		self.room_obj.floor_lst_append(self.dispense_obj)
		return super(DispenseObjResult, self).result_exe(gs, mach_state, alert_anchor)



### *** NEW RESULT CLASSES ***



### *** OLD RESULT CLASSES TO REVIEW ***

class BufferOnlyResult(object):
	def __init__(self, name, cmd_override):
		self._name = name
		self._cmd_override = cmd_override # does the triggered pre-action over-ride the 'standard' response to player command?

	@property
	def name(self):
		return self._name

	@property
	def cmd_override(self):
		return self._cmd_override

	def result_exe(self, gs, mach_state):
		gs.io.buff_s(self.name)
		return mach_state, self.cmd_override

	def __repr__(self):
		return f'Object { self.name } is of class { type(self).__name__ } '


# class BufferAndEndResult(BufferOnlyResult):
#	def __init__(self, name, ending, cmd_override):
#		super().__init__(name, cmd_override)
#		self._ending = ending # game ending - typically 'died' due to a room hazzard

#	@property
#	def ending(self):
#		return self._ending

##	def results_exe(self, gs, mach_state):
##		gs.set_game_ending(self.ending)
##		super(BufferAndEndResult, self).results_exe(gs, mach_state)

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
#		gs.end.game_ending = self.ending
#		gs.end.is_end = True
#		return mach_state, self.cmd_override


# class ChgCreatureDescAndStateResult(BufferOnlyResult):
#	def __init__(self, name, cmd_override, creature_obj, new_desc_key):
#		super().__init__(name, cmd_override)
#		self._creature_obj = creature_obj
#		self._new_desc_key = new_desc_key

#	@property
#	def creature_obj(self):
#		return self._creature_obj

#	@creature_obj.setter
#	def creature_obj(self, new_val):
#		self._creature_obj = new_val

#	@property
#	def new_desc_key(self):
#		return self._new_desc_key

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
#		self.creature_obj.descript_key = self.new_desc_key
#		mach_state = True
#		return mach_state, self.cmd_override


# class BufferAndGiveResult(BufferOnlyResult):
#	def __init__(self, name, give_item, cmd_override):
#		super().__init__(name, cmd_override)
#		self._give_item = give_item # item to be given to Burt

#	@property
#	def give_item(self):
#		return self._give_item

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
#		creature = gs.core.hero
#		creature.put_in_hand(self.give_item, gs)
#		mach_state = True
#		return mach_state, self.cmd_override


# class PutItemInHandResult(BufferOnlyResult):
#	def __init__(self, name, cmd_override, creature_obj, item_obj):
#		super().__init__(name, cmd_override)
#		self._creature_obj = creature_obj
#		self._item_obj = item_obj

#	@property
#	def creature_obj(self):
#		return self._creature_obj

#	@creature_obj.setter
#	def creature_obj(self, new_val):
#		self._creature_obj = new_val

#	@property
#	def item_obj(self):
#		return self._item_obj

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
## need to eventually change this to 'creature.take' when this is enabled
#		self.creature_obj.put_in_hand(self.item_obj, gs)
#		if self.item_obj in self.creature_obj.bkpk_lst:
#			self.creature_obj.bkpk_lst_remove(self.item_obj)
#		return mach_state, self.cmd_override


# class AddObjToRoomResult(BufferOnlyResult):
#	def __init__(self, name, room_item, cmd_override):
#		super().__init__(name, cmd_override)
#		self._room_item = room_item # item to be added to floor_lst

#	@property
#	def room_item(self):
#		return self._room_item

#	@room_item.setter
#	def room_item(self, new_val):
#		self._room_item = new_val

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
#		gs.map.hero_rm.floor_lst_append(self.room_item)
#		mach_state = True
#		return mach_state, self.cmd_override


# class AddObjChgDescriptResult(BufferOnlyResult):
#	def __init__(self, name, room_item, descript_obj, new_descript, cmd_override):
#		super().__init__(name, cmd_override)
#		self._room_item = room_item # item to be added to floor_lst
#		self._descript_obj = descript_obj # object for which descript_key will be changed
#		self._new_descript = new_descript # new descript_key

#	@property
#	def room_item(self):
#		return self._room_item

#	@room_item.setter
#	def room_item(self, new_val):
#		self._room_item = new_val

#	@property
#	def descript_obj(self):
#		return self._descript_obj

#	@property
#	def new_descript(self):
#		return self._new_descript

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
#		gs.map.hero_rm.floor_lst_append(self.room_item)
#		mach_state = True
#		self.descript_obj.descript_key = self.new_descript
#		return mach_state, self.cmd_override


# class AddObjToRoomAndDescriptResult(BufferOnlyResult):
#	def __init__(self, name, room_item, cmd_override):
#		super().__init__(name, cmd_override)
#		self._room_item = room_item # item to be added to floor_lst

#	@property
#	def room_item(self):
#		return self._room_item

#	@room_item.setter
#	def room_item(self, new_val):
#		self._room_item = new_val

#	def result_exe(self, gs, mach_state):
#		gs.io.buff_s(self.name)
#		room_obj = gs.map.hero_rm
#		room_obj.floor_lst_append(self.room_item)

#		new_descript_key = f"{room_obj.name}_{self.name}"
#		if gs.io.chk_str_exist(new_descript_key):
#			room_obj.descript_key = new_descript_key

#		mach_state = True
#		return mach_state, self.cmd_override


### *** OLD RESULT CLASSES TO REVIEW ***

### *** TO BE REVIEWED ***


class DoorToggleResult(BufferOnlyResult):
	def __init__(self, name, door_obj, cmd_override):
		super().__init__(name, cmd_override)
		self._door_obj = door_obj # door to be openned or closed

	@property
	def door_obj(self):
		return self._door_obj

	def result_exe(self, gs, mach_state):
		if self.door_obj.is_open == True:
			self.door_obj.is_open = False
			descript_ending = "closes."
		else:
			self.door_obj.is_open = True
			descript_ending = "opens."
		try:
			descript_start = gs.io.get_str_nr(self.name)
			descript = descript_start + descript_ending
			gs.io.buffer(descript)
		except:
			pass

		return mach_state, self.cmd_override


class AttackBurtResult(BufferOnlyResult):
	def __init__(self, name, creature_obj, cmd_override):
		super().__init__(name, cmd_override)
		self._creature_obj = creature_obj # creature to attack burt

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_val):
		self._creature_obj = new_val

	def result_exe(self, gs, mach_state):
		gs.io.buff_s(self.name)
##			cmd_execute(gs, '2word', [self.creature_obj, 'attack_burt'])
		if self.creature_obj.hand_is_empty():
			hand_obj = self.creature_obj.feature_lst[0]
#			hand_obj = None
		else:
			hand_obj = self.creature_obj.get_hand_item()
		tgt_creature = gs.core.hero
#		self.creature_obj.attack_b(hand_obj, gs, tgt_creature)
#		tgt_creature.attack_b(hand_obj, gs, self.creature_obj)
		tgt_creature.attack(hand_obj, gs, self.creature_obj)
#		room.go(self.dir, gs, self.creature)
		return mach_state, self.cmd_override


class StartTimerResult(BufferOnlyResult):
	def __init__(self, name, timer_obj, cmd_override):
		super().__init__(name, cmd_override)
		self._timer_obj = timer_obj

	@property
	def timer_obj(self):
		return self._timer_obj

	def result_exe(self, gs, mach_state):
		gs.io.buff_s(self.name)
		self.timer_obj.start()
		return mach_state, self.cmd_override


class TimerAndCreatureItemResult(StartTimerResult):
	def __init__(self, name, timer_obj, cmd_override, creature_obj, ceature_item_obj):
		super().__init__(name, timer_obj, cmd_override)
		self._creature_obj = creature_obj
		self._ceature_item_obj = ceature_item_obj

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_val):
		self._creature_obj = new_val

	@property
	def ceature_item_obj(self):
		return self._ceature_item_obj

	def result_exe(self, gs, mach_state):
		gs.io.buff_s(self.name)
		self.timer_obj.start()
		self.creature_obj.hand_lst_remove(self.ceature_item_obj)
		return mach_state, self.cmd_override


class TravelResult(BufferOnlyResult):
	def __init__(self, name, cmd_override, creature, dir):
		super().__init__(name, cmd_override)
		self._creature = creature
		self._dir = dir

	@property
	def creature(self):
		return self._creature

	@creature.setter
	def creature(self, new_val):
		self._creature = new_val

	@property
	def dir(self):
		return self._dir

	def result_exe(self, gs, mach_state):
		gs.io.buff_s(self.name)
		room = gs.map.get_obj_room(self.creature, gs)
		room.go(self.dir, gs, self.creature)
		return mach_state, self.cmd_override

### *** OLD RESULT CLASSES TO REVIEW ***