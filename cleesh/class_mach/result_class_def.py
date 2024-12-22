# program: cleesh engine
# author: Tom Snellgrove
# module description: class deffinition module for Results

# *** summary of result classes ***

# Result class (x) : 		inherits from (Y) : result_exe() method performs (Z)
#-------------------    	-------------       ---------------------------------
# BaseResult :				Invisible :			buffer using result.name as key if event in rm; set mach_state
# DisableMach :				BaseResult :		base + set is_enabled == False for self.mach
# EndResult :				BaseResult :		base + set ending val, set is_end = True
# ChgDescriptResult	:		BaseResult :		base + change obj descript_key
# GiveItemResult : 			BaseResult :		base + give item_obj to tgt_creature
# TakeItemResult :			BaseResult :		base + creature_obj takes item_obj
# DispenseObjResult :		BaseResult :		base + dispense obj to room
# StartTimerResult :		BaseResult :		base + starts timer
# RemoveObjResult :			BaseResult :		base + remove obj from game [new result for timer combo]
# AttackHeroResult :		BaseResult :		base + loc_buff, creature_obj attacks hero w/ hand_obj
# OpenableToggleResult :	BaseResult :		base + loc_buff, toggles door state
# CreatureTravelResult :	BaseResult :		base + creature attempts to go dir [not called]


### imports ###
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class BaseResult(Invisible):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override):
		super().__init__(name)
		self._cmd_override = cmd_override # does the triggered pre-action over-ride the 'standard' response to player command?
		self._is_mach_state_set = is_mach_state_set # bool where True indicates that mach_state will be set
		self._mach_state_val = mach_state_val # value mach_state should be set to if is_mach_state_set is True; None if not set
		""" BaseResult class inherits from Invisible. All other result classes inherit from BaseResult. 
		"""

	@property
	def cmd_override(self):
		return self._cmd_override

	@property
	def is_mach_state_set(self):
		return self._is_mach_state_set

	@property
	def mach_state_val(self):
		return self._mach_state_val

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		if alert_anchor.is_room():
			event_rm = alert_anchor
		else:
			event_rm = gs.map.get_obj_room(alert_anchor, gs)
		if gs.map.hero_rm == event_rm:
			gs.io.buff_s(buff_key)
		if self.is_mach_state_set:
			mach_state = self.mach_state_val
		return mach_state, self.cmd_override

class DisableMach(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, mach):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._mach = mach # modular machine to be disabled

	@property
	def mach(self):
		return self._mach

	@mach.setter
	def mach(self, new_val):
		self._mach = new_val
		
	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		self.mach.is_enabled = False
		return super(DisableMach, self).result_exe(gs, mach_state, buff_key, alert_anchor)

class EndResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, ending):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._ending = ending # game ending - typically 'died' due to a room hazzard

	@property
	def ending(self):
		return self._ending

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		gs.end.game_ending = self.ending
		gs.end.is_end = True
		return super(EndResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)

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

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		self.obj.descript_key = self.new_descript_key
		return super(ChgDescriptResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


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

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		self.tgt_creature.put_in_hand(self.item_obj, gs)
		return super(GiveItemResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)
		# Note: if mach_state was a class attrib of BaseResult, 
			# could call super().result_exe() in GiveItemResult.result_exe body
			# and then return super().mach_state, super().cmd_override


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

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		gs.map.get_obj_room(self.creature_obj, gs).remove_item(self.item_obj, gs)
		self.creature_obj.put_in_hand(self.item_obj, gs)
		return super(TakeItemResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


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

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		self.room_obj.floor_lst_append(self.dispense_obj)
		return super(DispenseObjResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


class StartTimerResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, timer_obj):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._timer_obj = timer_obj # timer to be started

	@property
	def timer_obj(self):
		return self._timer_obj

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		self.timer_obj.start()
		return super(StartTimerResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


class RemoveObjResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, obj):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._obj = obj # the obj to be removed

	@property
	def obj(self):
		return self._obj

	@obj.setter
	def obj(self, new_val):
		self._obj = new_val

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		room = gs.map.get_obj_room(self.obj, gs)
		room.remove_item(self.obj, gs)
		return super(RemoveObjResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


class AttackHeroResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, creature_obj, hand_obj):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._creature_obj = creature_obj # creature to attack hero
		self._hand_obj = hand_obj # obj in creature hand used to attack hero

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_val):
		self._creature_obj = new_val

	@property
	def hand_obj(self):
		return self._hand_obj

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		gs.io.buff_s(self.name + "_pre-buff")
		gs.core.hero.attack(self.hand_obj, gs, self.creature_obj)
		return super(AttackHeroResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


class OpenableToggleResult(BaseResult):
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, openable_obj):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._openable_obj = openable_obj # door-like obj to be openned or closed

	@property
	def openable_obj(self):
		return self._openable_obj

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		if self.openable_obj.toggle(gs):
			buff_key = self.name + "_open"
		else:
			buff_key = self.name + "_close"
		return super(OpenableToggleResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)


class CreatureTravelResult(BaseResult): # note: never tested; not 'known good'
	def __init__(self, name, is_mach_state_set, mach_state_val, cmd_override, creature_obj, dir_str):
		super().__init__(name, is_mach_state_set, mach_state_val, cmd_override)
		self._creature_obj = creature_obj # the creature that is traveling
		self._dir_str = dir_str # direction of travle (i.e. "north", "south", "east", or "west")

	@property
	def creature_obj(self):
		return self._creature_obj

	@creature_obj.setter
	def creature_obj(self, new_val):
		self._creature_obj = new_val

	@property
	def dir_str(self):
		return self._dir_str

	def result_exe(self, gs, mach_state, buff_key, alert_anchor):
		room = gs.map.get_obj_room(self.creature_obj, gs)
		room.go(self.dir_str, gs, self.creature_obj)
		return super(CreatureTravelResult, self).result_exe(gs, mach_state, buff_key, alert_anchor)

