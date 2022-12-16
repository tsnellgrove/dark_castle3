# program: dark castle v3.74
# name: Tom Snellgrove
# date: Nov 5, 2022
# description: class deffinition module for Creatures

### import
import random
from base_class_def import ViewOnly
from static_gbl import descript_dict

### classes
class Creature(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, writing, state, hand_lst, bkpk_lst,
		worn_lst, feature_lst, invis_lst, give_dict, is_attackable, attacked_dict):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._state = state # creature state; not yet in use (v3.75) - intended for state machine functionality & hunger / thirst
		self._hand_lst = hand_lst # list of items in creature's hand; is typically only 1 item 
		self._bkpk_lst = bkpk_lst # list of items in creature's backpack
		self._worn_lst = worn_lst # list of items currently worn by the creature
		self._feature_lst = feature_lst # visible obj associated w creature but not shown in i or l; used for traits like 'loyalty'; first obj in lst is used for unarmed attack 
		self._invis_lst = invis_lst # list of invisible obj associated w creature; typically used for Modular Machines
		self._give_dict = give_dict # dict of creature reactions to gifts
		self._is_attackable = is_attackable # bool indicating weather Burt can attack the creature
		self._attacked_dict = attacked_dict # dict of creature reactions to being attacked
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

	# *** attrib methods - hand ***
	def hand_lst_append(self, item):
		self._hand_lst.append(item)

	def hand_lst_remove(self, item):
		self._hand_lst.remove(item)

	def hand_is_empty(self):
		return not bool(self.hand_lst)

	def get_hand_item(self):
		return self.hand_lst[0]

	def put_in_hand(self, new_item):
		if not self.hand_is_empty():
			self.bkpk_lst_append(self.get_hand_item())
			self.hand_lst_remove(self.get_hand_item())
		self.hand_lst_append(new_item)

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

	def bkpk_lst_remove(self, item):
		self._bkpk_lst.remove(item)

	# *** attrib methods - worn ***
	def worn_lst_append(self, item):
		self._worn_lst.append(item)

	def worn_lst_remove(self, item):
		self._worn_lst.remove(item)

	def worn_is_empty(self):
		return not bool(self.worn_lst)

	def chk_type_worn(self, item):
		return any(item.garment_type == garment.garment_type for garment in self.worn_lst)

	def chk_is_worn(self, garment):
		return(garment in self.worn_lst)

	# *** simple methods ***
	def is_creature(self):
		return True

	# *** scope methods ***
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

	# *** display methods ***
	def has_contain(self, active_gs):
		if self == active_gs.hero:
			creature_lst = self.hand_lst + self.bkpk_lst + self.worn_lst
		else:
			creature_lst = self.hand_lst + self.worn_lst
		return bool(creature_lst)

	def disp_contain(self, active_gs):
		""" Displays a description of the visible items held by the obj. Used in examine(). Variable output for burt vs. other creatures.
		"""
		if not self.hand_is_empty():
			if self == active_gs.hero:
				active_gs.buff_no_cr(f"You are holding a {self.get_hand_item().full_name}. ")
				for obj in self.hand_lst:
					obj.disp_contain(active_gs)
				active_gs.buff_cr()
			else:
				active_gs.buff_no_cr(f"The {self.full_name} is holding a {self.get_hand_item().full_name}. ")
				for obj in self.hand_lst:
					obj.disp_contain(active_gs)
		if self == active_gs.hero and not self.bkpk_is_empty():
			if not self.hand_is_empty():
				active_gs.buff_cr()
			bkpk_str_lst = [obj.full_name for obj in self.bkpk_lst]
			bkpk_str = ", ".join(bkpk_str_lst)
			active_gs.buff_no_cr(f"In your backpack you have: {bkpk_str}. ")
			for obj in self.bkpk_lst:
				obj.disp_contain(active_gs)
		if not self.worn_is_empty():
			worn_txt_lst = [obj.full_name for obj in self.worn_lst]
			worn_str = ", ".join(worn_txt_lst)
			if self == active_gs.hero:
				if (not self.bkpk_is_empty()) or (not self.hand_is_empty()):
					active_gs.buff_cr()
					active_gs.buff_cr()
				active_gs.buff_no_cr(f"You are wearing: {worn_str}.")
			else:
				active_gs.buff_no_cr(f"The {self.full_name} is wearing: {worn_str}.")
			for obj in self.worn_lst:
				obj.disp_contain(active_gs)
		return 

	# *** verb methods ***
	def take(self, active_gs):
		""" Provides a custom error in the case where the player attempts to take() an object of Creature class.
		"""
		active_gs.buffer(f"You can't take the {self.full_name}! How would you feel if someone 'took' you?")
		return 


	def show(self, obj, active_gs):
		""" Shows an item in your hand to another creature.
		"""
		creature = active_gs.hero
		try:
			active_gs.buffer(descript_dict[f"{creature.name}_show_{self.name}_{obj.name}"]) 
		except:
			try:
				active_gs.buffer(descript_dict[f"{creature.name}_show_{self.name}_default"])
			except:
				active_gs.buffer(f"The {self.full_name} shows no interest in the {obj.full_name}.")
		return 


	def give(self, obj, active_gs):
		""" Gives an item to another creature.
		"""
		# determine other creature's response
		creature = active_gs.hero
		try:
			active_gs.buffer(descript_dict[f"{creature.name}_give_{self.name}_{obj.name}"])
			give_key = obj
		except:
			try:
				active_gs.buffer(descript_dict[f"{creature.name}_give_{self.name}_default"])
				give_key = 'def_give'
			except:
				active_gs.buffer(f"The {self.full_name} shows no interest in the {obj.full_name}.")
				return
		if not self.give_dict[give_key]['accept']:
			return

		# Other creature recieves gift and may give a gift in return
		creature.hand_lst_remove(obj)
		self.put_in_hand(obj) # messes up goblin holding grimy_axe ; addressed with auto_action
		give_item = self.give_dict[give_key]['give']
		if give_item:
			self.bkpk_lst_remove(give_item) # replace with remove_item() ??
			creature.hand_lst_append(give_item)

		# Update other creature description based on gift given
		new_descript_key = f"{creature.name}_give_{self.name}_{obj.name}_descript"
		if new_descript_key in descript_dict:
			self.descript_key = new_descript_key
		return 


	def attack(self, src_obj, active_gs, src_creature = None):
		""" Attacks a target_creature with an item
		"""
		# destermine src_creature & tgt_creature
		if src_creature is None:
			src_creature = active_gs.hero
		tgt_creature = self

		# display error & return on command failures
		if not tgt_creature.is_attackable:
			try:
				active_gs.buffer(descript_dict[f"not_attackable_{src_creature.name}_{tgt_creature.name}"])
			except:
				active_gs.buffer(descript_dict['not_attackable_default'])
			return
		if (not src_obj in src_creature.feature_lst) and (not src_creature.chk_in_hand(src_obj)):
			active_gs.buffer(f"You are not holding the {src_obj.full_name} in your hand.")
			return 
		if (src_obj in src_creature.feature_lst) and (not src_creature.hand_is_empty()):
			active_gs.buffer(f"You can't attack with your {src_obj.full_name} while you're holding the {src_creature.get_hand_item().full_name}.")
			return 
		if src_creature == tgt_creature:
			active_gs.buffer("A creature can't attack itself!")
			return
		
		# determine tgt_obj for tgt_creature (src_obj provided in method arguements)
		if tgt_creature.hand_is_empty():
			tgt_obj = tgt_creature.feature_lst[0] # feature_lst[0] is a creature's unarmed attack
		else:
			tgt_obj = tgt_creature.get_hand_item()

		# determine possible result keys
		# the intent is to allow keys based on obj names, obj categories, or wildcards
		if src_obj in src_creature.feature_lst:
			src_obj_category = 'unarmed'
		elif src_obj.is_weapon():
			src_obj_category = 'weapon'
		else:
			src_obj_category = 'item'
		
		if tgt_obj in tgt_creature.feature_lst:
			tgt_obj_category = 'unarmed'
		elif tgt_obj.is_weapon():
			tgt_obj_category = 'weapon'
		else:
			tgt_obj_category = 'item'
		
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
		room_obj = active_gs.map.get_obj_room(tgt_creature)
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
				src_obj_disp = f"the {src_obj.full_name}"
		else:
			src_creature_disp = f"The {src_creature.full_name} attacks"
			if src_obj_category == 'unarmed':
				src_obj_disp = f"its {src_obj.full_name}"
			else:
				src_obj_disp = f"the {src_obj.full_name}"
		
		if tgt_creature == active_gs.hero:
			tgt_creature_disp = "you attempt"
			if tgt_obj_category == 'unarmed':
				tgt_obj_disp = f"parry with your {tgt_obj.full_name}"
			else:
				tgt_obj_disp = f"parry with the {tgt_obj.full_name}"
		else:
			tgt_creature_disp = f"the {tgt_creature.full_name} attempts"
			if tgt_obj_category == 'unarmed':
				tgt_obj_disp = f"dodge"
			else:
				tgt_obj_disp = f"parry with the {tgt_obj.full_name}"
		active_gs.buffer(f"{src_creature_disp} with {src_obj_disp} and {tgt_creature_disp} to {tgt_obj_disp}!")

		# buffer a 'custom attack response' if it exists
		# the response is unique to the deffender, attack obj, attacker, defense obj
		active_gs.buff_try_key(f"{tgt_creature.name}_{result_key}")

		# 'attack resolution first clause'
		# compose a string describing the 'winning' blow
		# provide additional verb and adj detail if src_creature weilding an obj of class Weapon
		if (win_obj in src_creature.feature_lst) or (win_obj in tgt_creature.feature_lst):
			resolution_strt_str = ""
		elif win_obj.is_weapon():
			weapon_wrd_count = len(win_obj.desc_lst) - 1
			weapon_wrd_idx = random.randint(0, weapon_wrd_count)
			weapon_verb = win_obj.desc_lst[weapon_wrd_idx][0]
			weapon_adj_noun = win_obj.desc_lst[weapon_wrd_idx][1]
			resolution_strt_str = f"The {win_obj.full_name} {weapon_verb} through the air with a {weapon_adj_noun}. "
		else:
			resolution_strt_str = f"The {win_obj.full_name} whizzes through the air. "			

		# 'attack resolution second clause'
		# based on result_code, describe the combat outcome for the 'losing' creature
		if lose_creature == active_gs.hero:
			lose_creature_disp = "You are"
		else:
			lose_creature_disp = f"The {lose_creature.full_name} is"
		resolution_end_str = f"{lose_creature_disp} {descript_dict[result_code]} "

		# buffer the full 'attack resolution'
		active_gs.buffer(f"{resolution_strt_str}{resolution_end_str}")
		return 


""" *** Module Documentation ***

	* Creature class:

		Overview: 
			I thought through two different approaches to creatures. 
			
			In one approach - I'll call it the "primatives" approach - I declare that each creature has wants and fears (e.g. the hedgehog wants the biscuits, the goblin fears the shiny sword). Under the primatives approach the creatures have innate personalities and the role of creature methods like 'show', 'give', and 'attack' are just to expose those personalities. This is attractive in that it makes the creatures more real and gives general guidance for their future behaviors. However, I don't think it's realistic. Dark Castle is not a life simulator... there is no ecosystem or food chain (I mean really, the castle has been abandoned for generations - what have they all been eating??). And the creature's wants and fears are quite idiosyncratic... the goblin is an autocrat who wants to prevent passage to the throne room or any rejuvination of the castle... the hedgehog, along with loving biscuits, is the keeper of Bright Castle's spirit and wants to see it restored. These are not easy desires to model in a simple python object!
			
			The other approach I considered - I'll call it the "mechanical" approach - is that a creature is wholy defined by its methods. There is no attempt to track and expose a creature's inner desires - their actions are their all - like early impressionism, their surface is their whole. I find this a little unsatisfying - but I also think it's much more implementable. So at least for version 3.x this is the approach I'll take. Perhaps in version 4.x I'll find away to capture the hedgehog's inner yearnings in code ;-D
			
			Based on the "mechanical" approach, creatures have three standard interaction methods: show(), give(), and attack()

	- take() method [Creature class]:

		Overview:
			take() in Creature class over-rides the Item method and provides guardrails to ensure that Creature class receptacles cannot be 'taken' even if a CreatureItem class is someday created.

	- show() method [Creature class]:

		Overview: 
			'Show' is meant to be informational in nature. The Player will learn something about the creature - what it desires and fears - based on its response to the item shown. Therefore the show() method provides only a text response. Provoking an action response (e.g. running away) is outside the standard use case and should be implemented via a Modular Machine.

		Implementation Detail:
			1) When creating a new creature, remember to create the show() response descriptions in descript_dict() using the auto-genertated key format. Auto-gen key format == "<player_creature>_show_<target_creature>_item"
			2) Creaatures are not allowed to have Creatures or Surfaces in their inventory
			
		Historic Note:
			show() is new to v3 (as are all commands requiring a preposition - since v1 / v2 only supported 2-word commands). Previously, the player's only insight into creature sentiment was the creature's description. Some test players of v2 felt that the act of giving the hedgehog the sword to get the silver key was pretty arbitrary - and they had a point - the clues (i.e. color of the keyhole on the craystal_box and the crest over the family_tree) were subtle.  show() enables richer creature interactions and a Dark Castle world of greater object variety - while still maintaining a feel of determinism.


	- give() method [Creature class]:

		Overview: 
			'Give' is meant to enable barter and trade. If the Player gives an item to a creature - particularly if that creature has shown interest in the item via show() - then the player can reasonably hope for some other useful item or information in return. Therefore the give() method enables a text response, determines whether the creature will accept the gift, and what, if anything, it will give Burt in return. Because give() can fulfill a creature's needs it also has the power to change the creature's mood and therefore update their description.

		Implementation specifics:
			1) When creating a new creature, remember to create the response descriptions and (if appropriate) the creature description updates in descript_dict() using the auto-genertated key format.
			2) It is assumed that if the creature 'shows no interest' in Burt's gift then they will not accept it, will not provide a gift in response, and will not change their demeanor as a result of the offer.
			3) It is assumed that if a creature won't accept an item from Burt, then they also won't have a gift to give in return and that their demeanor will not change.
			4) Creaatures are not allowed to have Creatures or Surfaces in their inventory
		
		Historic Note:
			Like show(), give() is new to v3. In v1 / v2 , Burt just dropped the 'stale_biscuits' on the floor of the 'main_hall' and the 'royal_hedgehog' charged forward and gobbled them up. With a new interpreter in v3 that enabled prepositions, give() seemed like a more intentional way to enable barter. It also provides more information about creature sentiment regarding objects.
		

	- attack() method [Creature class]:

		Overview: 
			The attack() method is a bit more complex and is intended to enable combat between Burt and creatures. The intent in Dark Castle is for combat to be a purely logical exercise... so if you attack a Creature with the correct weapon you will always win. Burt's "weapon" is whatever he is holding in his hand. If Burt's hand is empty he attacks with his Fist. For a given Creature and burt_weapon, attack() generates a result_code - which has options like 'creature_flee', 'creature_death', and 'burt_death' - and a response_key - which is the descript_dict[] key to the attack's description. As, with the other Creature methods, it's easy to imagine attack() provoking a more complex response than these outcomes - but those are outside the scope of the method and should be implemented via a Modular Machine.
			
			'attack_burt' is an awkward 'hidden' verb that enables a creature to proactively attack Burt. Among other things, this work-around highlights that Burt should really be an object himself - rather than an amorphous set of attributes distributed across game state. But this will not be a minor undertaking - so for now, we have the attack_burt() method - which enables 'attack' to remain a 2word command without requiring a 'burt' object to exist. Code-wise, 'attack_burt' is identical to 'attack' with some minor text differences ("You charge..." vs. "You attempt to parry..."). In general, the idea is that when Burt is being attacked he is on the defensive and likely needs the right weapon just to parry.

	attack() nots: 
	- order of operations = <attacker> => <custom> => <winner>
			
	- pronouns based on 3 possible cases:
		src_creature == gs.hero
		tgt_creature == gs.hero
		gs.hero != src_creature && gs.hero != tgt_creature

"""
