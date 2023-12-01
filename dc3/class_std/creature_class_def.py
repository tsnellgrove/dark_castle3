# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: class deffinition module for Creatures

### import
import random
from dc3.class_std.base_class_def import ViewOnly
from dc3.data.static_gbl import static_dict

### local functions
def attack_obj_category(obj, creature):
	if obj in creature.feature_lst:
		return 'unarmed'
	elif obj.is_weapon():
		return 'weapon'
	else:
		return 'item'

### classes
class Creature(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, state, hand_lst, bkpk_lst,
		worn_lst, feature_lst, invis_lst, give_dict, is_attackable, attacked_dict, weight, max_weight):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._state = state # not in use (v3.75) - for state machine functionality, hunger & thirst
		self._hand_lst = hand_lst # list of items in creature's hand; is typically only 1 item 
		self._bkpk_lst = bkpk_lst # list of items in creature's backpack
		self._worn_lst = worn_lst # list of items currently worn by the creature
		self._feature_lst = feature_lst # not vis via i or l; e.g. 'loyalty'; 1st = unarmed attack 
		self._invis_lst = invis_lst # invisible obj associated w creature; used for Modular Machines
		self._give_dict = give_dict # dict of creature reactions to gifts
		self._is_attackable = is_attackable # bool indicating weather Burt can attack the creature
		self._attacked_dict = attacked_dict # dict of creature reactions to being attacked
		self._weight = weight # represents the weight of the creature
		self._max_weight = max_weight # maximum weight for the creature + all items
		""" Creatures interact with the world of Dark Castle, move from room to room, and initiate actions. Burt is an object of class Creature.
		"""

	# *** getters & setters ***
	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, new_state):
		self._state = new_state

	@property
	def hand_lst(self):
		return self._hand_lst

	@hand_lst.setter
	def hand_lst(self, new_state):
		self._hand_lst = new_state

	@property
	def bkpk_lst(self):
		return self._bkpk_lst

	@bkpk_lst.setter
	def bkpk_lst(self, new_state):
		self._bkpk_lst = new_state

	@property
	def worn_lst(self):
		return self._worn_lst

	@worn_lst.setter
	def worn_lst(self, new_state):
		self._worn_lst = new_state

	@property
	def feature_lst(self):
		return self._feature_lst

	@property
	def invis_lst(self):
		return self._invis_lst

	@property
	def give_dict(self):
		return self._give_dict

	@property
	def is_attackable(self):
		return self._is_attackable

	@property
	def attacked_dict(self):
		return self._attacked_dict

	@property
	def weight(self):
		return self._weight

	@weight.setter
	def weight(self, new_weight):
		self._weight = new_weight

	@property
	def max_weight(self):
		return self._max_weight

	# *** attrib methods - hand ***
	def increment_weight(self, increment_by):
		""" Increments the weight of an Item by a given amount
		"""
		self.weight += increment_by
		return

	def decrement_weight(self, decrement_by):
		""" Decrements the weight of an Item by a given amount
		"""
		self.weight -= decrement_by
		return

	# *** attrib methods - hand ***
	def hand_lst_append(self, item):
		self.hand_lst.append(item)
		self.increment_weight(item.weight)
		return

	def hand_lst_remove(self, item):
		self.hand_lst.remove(item)
		self.decrement_weight(item.weight)
		return

	def hand_is_empty(self):
		return not bool(self.hand_lst)

	def get_hand_item(self):
		return self.hand_lst[0]

	def put_in_hand(self, new_item, active_gs):
		if self.weight + new_item.weight >= self.max_weight:
			room = active_gs.map.get_obj_room(self, active_gs)
			room.floor_lst_append(new_item)
			if self == active_gs.hero:
				active_gs.io.buffer(f"Your burden is too great. You drop the {new_item.full_name} on the floor.")
			else:
				active_gs.io.buffer(f"The {self.full_name} is overburdened and must drop the {new_item.full_name} on the floor.")
			return
		if not self.hand_is_empty():
			self.bkpk_lst_append(self.get_hand_item())
			self.hand_lst_remove(self.get_hand_item())
		self.hand_lst_append(new_item)
		return

	def chk_in_hand(self, obj):
		return obj in self.hand_lst

	def in_hand_is_weapon(self):
		if self.hand_is_empty():
			return False
		return self.get_hand_item().is_weapon()

	# *** attrib methods - bkpk ***
	def bkpk_is_empty(self):
		return not bool(self.bkpk_lst)

	def bkpk_lst_append(self, item):
		self._bkpk_lst.append(item)
		self.increment_weight(item.weight)
		return

	def bkpk_lst_remove(self, item):
		self._bkpk_lst.remove(item)
		self.decrement_weight(item.weight)
		return

	# *** attrib methods - worn ***
	def worn_lst_append(self, item):
		self._worn_lst.append(item)
		self.increment_weight(item.weight)
		return

	def worn_lst_remove(self, item):
		self._worn_lst.remove(item)
		self.decrement_weight(item.weight)
		return

	def worn_is_empty(self):
		return not bool(self.worn_lst)

	def chk_type_worn(self, item):
		return any(item.garment_type == garment.garment_type for garment in self.worn_lst)

	def chk_is_worn(self, garment):
		return(garment in self.worn_lst)

	# *** class identity methods ***
	def is_creature(self):
		return True

	def is_receptacle(self):
		return True

	# *** universal scope methods ***
	def get_vis_contain_lst(self, active_gs):
		""" Returns the list of visible objects contained in the referenced ('self') object
		"""
		contain_lst = []
		if self == active_gs.hero:
			node1_item_lst = self.hand_lst + self.worn_lst + self.bkpk_lst
		else:
				node1_item_lst = self.hand_lst + self.worn_lst
		[contain_lst.extend(obj.get_vis_contain_lst(active_gs)) for obj in node1_item_lst]
		return node1_item_lst + contain_lst + self.feature_lst

	def chk_contain_item(self, item):
		""" Evaluates whether the passed object is contained within the methed-calling object. Called by Room.remove_item()
		"""
		return item in self.hand_lst + self.bkpk_lst + self.worn_lst

	def get_contain_lst(self, active_gs):
		return self.hand_lst + self.bkpk_lst + self.worn_lst + self.feature_lst

	def remove_item(self, item, active_gs):
		""" Removes the passed object from the methed-calling object.
		"""
		if item in self.hand_lst:
			self.hand_lst_remove(item)
			return 
		if item in self.bkpk_lst:
			self.bkpk_lst_remove(item)
			return 
		if item in self.worn_lst:
			self.worn_lst_remove(item)
			return 
		raise ValueError(f"Can't remove item {item} from creature {self.name}")
		return 


	# *** creature-specific scope methods ***
	def is_contained(self, active_gs): # only works for Creature class; not generalized for other obj
		return self not in active_gs.map.get_obj_room(self, active_gs).floor_lst

	def get_contained_by(self, active_gs):
		if not self.is_contained:
			raise ValueError(f"{obj.full_name} is not in a container.")
		else:
			for obj in active_gs.map.get_obj_room(self, active_gs).floor_lst:
				if obj.is_seat() and self in obj.contain_lst:
					return obj
		raise ValueError(f"{obj.full_name} not found.")

	def chk_obj_in_reach(self, obj, active_gs):
		seat_item_lst = self.get_contained_by(active_gs).get_vis_contain_lst(active_gs)
		room = active_gs.map.get_obj_room(self, active_gs)
		in_reach_obj_lst = []
		for receptacle in self.get_contained_by(active_gs).in_reach_lst:
			if receptacle.is_container():
				in_reach_obj_lst = in_reach_obj_lst + receptacle.contain_lst + [receptacle]
			elif receptacle.is_room():
				for floor_obj in receptacle.floor_lst:
					if floor_obj.is_item():
						in_reach_obj_lst = in_reach_obj_lst + [floor_obj]
			elif receptacle.is_viewonly():
				in_reach_obj_lst = in_reach_obj_lst + [receptacle]
		return obj in (seat_item_lst + [room] + in_reach_obj_lst)

	def chk_wrt_in_reach(self, wrt, active_gs):
		wrt_in_seat = self.get_contained_by(active_gs).chk_wrt_is_vis(wrt, active_gs)
		in_reach_obj_lst = []
		for receptacle in self.get_contained_by(active_gs).in_reach_lst:
			if receptacle.is_container():
				in_reach_obj_lst = in_reach_obj_lst + receptacle.contain_lst + [receptacle]
			elif receptacle.is_room():
				for floor_obj in receptacle.floor_lst:
					if floor_obj.is_item():
						in_reach_obj_lst = in_reach_obj_lst + [floor_obj]
			elif receptacle.is_viewonly():
				in_reach_obj_lst = in_reach_obj_lst + [receptacle]
		wrt_in_reach = any(obj.writing == wrt for obj in in_reach_obj_lst)
		return wrt_in_seat or wrt_in_reach

	# *** universal display methods ***
	def has_cond(self, active_gs):
		return self.is_contained(active_gs)

	def disp_cond(self, active_gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		if self.has_cond(active_gs):
			if self == active_gs.hero:
				active_gs.io.buff_no_cr(f"You are seated in the {self.get_contained_by(active_gs).full_name}.")
				active_gs.io.buff_cr()
				active_gs.io.buff_cr()
			else:
				active_gs.io.buff_no_cr(f"The {self.full_name} is seated in the {self.get_contained_by(active_gs).full_name}.")
		else:
			pass

	def has_contain(self, active_gs):
		if self == active_gs.hero:
##			creature_lst = self.hand_lst + self.bkpk_lst + self.worn_lst
			return True
		return bool(self.hand_lst + self.worn_lst)

	def disp_contain(self, active_gs):
		""" Displays a description of the visible items held by the obj. Used in examine(). Variable output for burt vs. other creatures.
		"""
		if self == active_gs.hero:
			active_gs.io.buff_no_cr(f"In your off hand you hold a Brass Lantern.")
			if (not self.bkpk_is_empty()) or (not self.hand_is_empty()) or (not self.worn_is_empty()):
					active_gs.io.buff_cr()
					active_gs.io.buff_cr()
		if not self.hand_is_empty():
			if self == active_gs.hero:
				active_gs.io.buff_no_cr(f"You are holding a {self.get_hand_item().full_name}. ")
				for obj in self.hand_lst:
					obj.disp_contain(active_gs)
				active_gs.io.buff_cr()
			else:
				active_gs.io.buff_no_cr(f"The {self.full_name} is holding a {self.get_hand_item().full_name}. ")
				for obj in self.hand_lst:
					obj.disp_contain(active_gs)
		if self == active_gs.hero and not self.bkpk_is_empty():
			if not self.hand_is_empty():
				active_gs.io.buff_cr()
			bkpk_str_lst = [obj.full_name for obj in self.bkpk_lst]
			bkpk_str = ", ".join(bkpk_str_lst)
			active_gs.io.buff_no_cr(f"In your backpack you have: {bkpk_str}. ")
			for obj in self.bkpk_lst:
				obj.disp_contain(active_gs)
		if not self.worn_is_empty():
			worn_txt_lst = [obj.full_name for obj in self.worn_lst]
			worn_str = ", ".join(worn_txt_lst)
			if self == active_gs.hero:
				if (not self.bkpk_is_empty()) or (not self.hand_is_empty()):
					active_gs.io.buff_cr()
					active_gs.io.buff_cr()
				active_gs.io.buff_no_cr(f"You are wearing: {worn_str}.")
			else:
				active_gs.io.buff_no_cr(f"The {self.full_name} is wearing: {worn_str}.")
			for obj in self.worn_lst:
				obj.disp_contain(active_gs)
		return 

	# *** creature-specific display methods ***
	def disp_in_reach(self, active_gs):
		""" displays in_reach objects for seated creature
		"""
		if self != active_gs.hero:
			return
		seat_obj = self.get_contained_by(active_gs)
		in_reach_disp_obj_lst = []
		for in_reach_obj in seat_obj.in_reach_lst:
			if not in_reach_obj.is_room():
				in_reach_disp_obj_lst.append(in_reach_obj)
			else:
				for room_obj in in_reach_obj.floor_lst:
					if room_obj.is_item():
						in_reach_disp_obj_lst.append(room_obj)
		in_reach_disp_txt_lst = [obj.full_name for obj in in_reach_disp_obj_lst]
		in_reach_str = ", ".join(in_reach_disp_txt_lst)
		active_gs.io.buffer(f"From your position on the {seat_obj.full_name} you can just reach: {in_reach_str}")

	# *** verb methods ***
	def show(self, obj, active_gs, mode=None):
		""" Extends Writing.show(). Shows an item in your hand to another creature.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		try:
			active_gs.io.buff_a(f"{creature.name}_show_{self.name}_{obj.descript_key}")
		except:
			try:
				active_gs.io.buff_a(f"{creature.name}_show_{self.name}_default")
			except:
				active_gs.io.buffer(f"The {self.full_name} shows no interest in the {obj.full_name}.")
		return 

	def give(self, obj, active_gs, mode=None):
		""" Gives an item to another creature.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero

		# determine other creature's response
		try:
			active_gs.io.buff_a(f"{creature.name}_give_{self.name}_{obj.descript_key}")
			give_key = obj
		except:
			try:
				active_gs.io.buff_a(f"{creature.name}_give_{self.name}_default")
				give_key = 'def_give'
			except:
				active_gs.io.buffer(f"The {self.full_name} shows no interest in the {obj.full_name}.")
				return
		if not self.give_dict[give_key]['accept']:
			return

		# Other creature recieves gift and may give a gift in return
		creature.hand_lst_remove(obj)
		self.put_in_hand(obj, active_gs) # messes up goblin holding grimy_axe ; addressed with auto_action
		give_item = self.give_dict[give_key]['give']
		if give_item:
#			self.bkpk_lst_remove(give_item) # replace with remove_item() ??
			self.remove_item(give_item, active_gs)
			creature.hand_lst_append(give_item)

		# Update other creature description based on gift given
		new_descript_key = f"{creature.name}_give_{self.name}_{obj.name}_descript"
		if new_descript_key in static_dict:
			self.descript_key = new_descript_key
		return 

	def attack(self, src_obj, active_gs, src_creature=None, mode=None):
		""" Attacks a target_creature with an item
		"""

		# destermine src_creature, tgt_creature, and mode
		if mode is None:
			mode = 'std'
		if src_creature is None:
			src_creature = active_gs.hero
		tgt_creature = self
		
		# determine tgt_obj for tgt_creature (src_obj provided in method arguements)
		if tgt_creature.hand_is_empty():
			tgt_obj = tgt_creature.feature_lst[0] # feature_lst[0] is a creature's unarmed attack
		else:
			tgt_obj = tgt_creature.get_hand_item()

		# determine possible result keys
		# the intent is to allow keys based on obj names, obj categories, or wildcards
		src_obj_category = attack_obj_category(src_obj, src_creature)
		tgt_obj_category = attack_obj_category(tgt_obj, tgt_creature)
		
		src_obj_str_lst = [src_obj.name, src_obj_category, '*']
		src_creature_str_lst = [src_creature.name, '*']
		tgt_obj_str_lst = [tgt_obj.name, tgt_obj_category, '*']

		# determine actual result key
		# more specific keys have priority over less specific
		result_key = 'attack_method_default_result'
		break_flag = False	
		for src_obj_str in src_obj_str_lst:
			for src_creature_str in src_creature_str_lst:
				for tgt_obj_str in tgt_obj_str_lst:
					loop_key = f"{src_obj_str}_{src_creature_str}_{tgt_obj_str}"
					if loop_key in self.attacked_dict:
						result_key = loop_key
						break_flag = True
						break
				if break_flag:
					break	
			if break_flag:
				break

		# based on result_key, determine result_code and winner; implement combat actions
		room_obj = active_gs.map.get_obj_room(tgt_creature, active_gs)
		if result_key == 'attack_method_default_result':
			result_code = 'no_result'
		else:
			result_code = self.attacked_dict[result_key]

		if result_code[0 : 3] == 'src':
			win_obj = tgt_obj
			lose_creature = src_creature
		else:
			win_obj = src_obj
			lose_creature = tgt_creature			

		if lose_creature == active_gs.hero:
			if result_code in ['src_death', 'tgt_death']:
				active_gs.set_game_ending('death')
		else:
			if result_code in ['src_death', 'tgt_death']:
				room_obj.floor_lst_remove(lose_creature)
				room_obj.floor_lst_extend(lose_creature.bkpk_lst + lose_creature.hand_lst + lose_creature.worn_lst)
			if result_code == 'tgt_flee_dc':
				room_obj.floor_lst_remove(lose_creature)

		# if hero_creature not in current room, exit with no display
		if room_obj != active_gs.get_room():
			return 


		### Display Combat Text ###
		
		# create and buffer the 'attack initiation string'
		# describes the actions and the 'weapons' of both the attacker and the defender
		if src_creature == active_gs.hero:
			src_creature_disp = "You attack"
			if src_obj_category == 'unarmed':
				src_obj_disp = f"your {src_obj.full_name}"
		else:
			src_creature_disp = f"The {src_creature.full_name} attacks"
			if src_obj_category == 'unarmed':
				src_obj_disp = f"its {src_obj.full_name}"
		if src_obj_category != 'unarmed':
			src_obj_disp = f"the {src_obj.full_name}"
		
		if tgt_creature == active_gs.hero:
			tgt_creature_disp = "you attempt"
		else:
			tgt_creature_disp = f"the {tgt_creature.full_name} attempts"
		if tgt_obj_category == 'unarmed':
			tgt_obj_disp = f"dodge"
		else:
			tgt_obj_disp = f"parry with the {tgt_obj.full_name}"
		
		active_gs.io.buffer(f"{src_creature_disp} with {src_obj_disp} and {tgt_creature_disp} to {tgt_obj_disp}!")

		# buffer a 'custom attack response' if it exists
		# the response is unique to the deffender, attack obj, attacker, defense obj
		active_gs.buff_try_key(f"{tgt_creature.name}_{result_key}")

		# 'attack resolution first clause'
		# compose a string describing the 'winning' blow
		# provide additional verb and adj detail if src_creature weilding an obj of class Weapon
		if (win_obj in src_creature.feature_lst) or (win_obj in tgt_creature.feature_lst):
			resolution_strt_str = ""
		elif win_obj.is_weapon():
			weapon_verb, weapon_adj = win_obj.desc_lst[random.randint(0, len(win_obj.desc_lst) - 1)]
			resolution_strt_str = f"The {win_obj.full_name} {weapon_verb} through the air with a {weapon_adj}. "
		else:
			resolution_strt_str = f"The {win_obj.full_name} whizzes through the air. "			

		# 'attack resolution second clause'
		# based on result_code, describe the combat outcome for the 'losing' creature
		if lose_creature == active_gs.hero:
			lose_creature_disp = "You are"
		else:
			lose_creature_disp = f"The {lose_creature.full_name} is"
		resolution_end_str = f"{lose_creature_disp} {static_dict[result_code]} "

		# buffer the full 'attack resolution'
		active_gs.io.buffer(f"{resolution_strt_str}{resolution_end_str}")
		return 

	def stand(self, active_gs, mode=None):
		""" Enables a Creature to stand up from a Seat or Bed
		"""
		if mode is None:
			mode = 'std'

		room = active_gs.map.get_obj_room(self, active_gs)		
		room.remove_item(self, active_gs)
		room.floor_lst_append(self)

		# if hero_creature not in current room, exit with no display
		if room != active_gs.get_room():
			return 

		if self == active_gs.hero:
			active_gs.io.buffer(f"You are now standing in the {room.full_name}.")
		else:
			active_gs.io.buffer(f"The {self.full_name} is now standing.")
		return

	### debug methods ###


	def get_weight(self, active_gs, mode=None):
		""" Reports the weight of an Item. Only usable in debug mode.
		"""
		if mode is None:
			mode = 'std'
		
		active_gs.io.buffer(f"The weight of the {self.full_name} is {self.weight}.")
		return


