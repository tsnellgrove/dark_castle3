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
			worn_lst, feature_lst, invis_lst, give_dict, is_attackable, attacked_dict, attacking_dict):
		super().__init__(name, full_name, root_name, descript_key, writing)
		self._state = state # creature state; not yet in use (v3.75) - intended for state machine functionality & hunger / thirst
		self._hand_lst = hand_lst # list of items in creature's hand; is typically only 1 item 
		self._bkpk_lst = bkpk_lst # list of items in creature's backpack
		self._worn_lst = worn_lst # list of items currently worn by the creature
		self._feature_lst = feature_lst # list of visible obj associated w creature but not included in i or l; used for traits like 'loyalty' 
		self._invis_lst = invis_lst # list of invisible obj associated w creature; typically used for Modular Machines
		self._give_dict = give_dict # dict of creature reactions to gifts
		self._is_attackable = is_attackable # bool indicating weather Burt can attack the creature
		self._attacked_dict = attacked_dict # dict of creature reactions to being attacked
		self._attacking_dict = attacking_dict # dict of results from creature attacking Burt; no longer needed once type(burt) == creature
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
	def attacking_dict(self):
		return self._attacking_dict

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


	def attack_b(self, src_obj, active_gs, src_creature = None):
		""" Attacks a target_creature with an item
		"""
		if src_creature is None:
			src_creature = active_gs.hero
		tgt_creature = self

		# ERROR & RETURN ON COMMAND FAILURES
		if not tgt_creature.is_attackable:
			try:
				active_gs.buffer(descript_dict[f"not_attackable_{tgt_creature.name}"])
			except:
				active_gs.buffer(descript_dict['not_attackable_default'])
			return
		if (not src_obj in src_creature.feature_lst) and (not src_creature.chk_in_hand(src_obj)):
			active_gs.buffer(f"You're not holding the {src_obj.full_name} in your hand.")
			return 
		if (src_obj in src_creature.feature_lst) and (not src_creature.hand_is_empty()):
			active_gs.buffer(f"You can't attack with your fist while you're holding the {src_creature.get_hand_item().full_name}.")
			return 

		# IMPLEMENT RESULTS
		
		# <determine tgt_obj for tgt_creature>
		if tgt_creature.hand_is_empty():
			tgt_obj = None
		else:
			tgt_obj = tgt_creature.get_hand_item()

		# <determine type of attack obj - unarmed, item, or weapon>
		if src_obj in self.attacked_dict:
			dict_key = src_obj
		elif (src_obj in src_creature.feature_lst) and 'def_unarmed' in self.attacked_dict:
			dict_key = 'def_unarmed'
		elif (src_obj.is_weapon()) and 'def_weapon' in self.attacked_dict:
			dict_key = 'def_weapon'
		elif 'def_item' in self.attacked_dict:
			dict_key = 'def_item'
		else:
			dict_key = 'no_response'

		print(dict_key)

		# <determine & implement result / winner>
		room_obj = active_gs.get_room()

		if self.attacked_dict[dict_key]['result_code'] == 'creature_flee_dc':
			room_obj.floor_lst_remove(self)
		elif self.attacked_dict[dict_key]['result_code'] == 'burt_death':
			active_gs.set_game_ending('death')
		elif self.attacked_dict[dict_key]['result_code'] == 'creature_death':
			room_obj.floor_lst_remove(self)
			room_obj.floor_lst_extend(self.bkpk_lst + self.hand_lst + self.worn_lst)


		# <IF SILENT MODE, RETURN>

		# <OUTPUT COMBAT TEXT>
		
			# <determine pronouns based on 3 possible cases:
					# <src_creature == gs.hero>
					# <tgt_creature == gs.hero>
					# <gs.hero != src_creature && gs.hero != tgt_creature>
		
			# <buffer attack initiation>

			# <buffer custom response>

			# <buffer winner result>


		# create and buffer attack_initiation_str

		# determine if creature has an attack response and if so what response key to use

		# if no response, buffer default text and exit

		#	if creature_has_response, buffer custom_str if it exists

		# implement the results of the attack_response result_code and compose the 2nd half of the attack resolution string

		# compose the start of the attack resolution string with verb and adj detail if the creature is weilding a weapon

		# buffer the full attack resolution string

### NOTE: GENERATING win_weapon DOESN'T REALLY SOLVE THE PROBLEM... I ACTUALLY NEED TO DETERMINE 'WINNER' AND BASE DESC OFF THEIR 'HAND'
### NOTE: ALSO NOT DETERMINING IF hand_is_empty() IN CONJUNCTION WITH 'WINNER' AND ATTACK RESOLUTION
### NOTE: REALLY NEED TO FIGURE OUT 'WINNER' *FIRST* - THEN HAND STATE AND WEAPON ADJ FLOW FROM THERE
### NOTE: order of operations = <attacker> => <custom> => <winner>

		active_gs.buffer(f"{src_creature.full_name} attacks the {tgt_creature.full_name} with the {src_obj.full_name}.")
		return 



	def attack(self, active_gs):
		""" Attacks a target_creature with an item
		"""
		# determine if creature is_attackable; if not, buffer response and exit
		if not self.is_attackable:
			try:
				descript_key = 'not_attackable_' + self.name
				active_gs.buffer(descript_dict[descript_key])
			except:
				active_gs.buffer(descript_dict['not_attackable_default'])
			return

		# create and buffer attack_initiation_str
		creature = active_gs.hero
		if creature.hand_is_empty():
			burt_weapon_name = 'your fist'
			burt_weapon_obj = None
		else:
			hand_lst = creature.hand_lst
			burt_weapon_obj = hand_lst[0]
			burt_weapon_name = 'the ' + burt_weapon_obj.full_name
		if self.hand_is_empty():
			hand_text = "!"
		else:
			hand_text = " with the " + self.get_hand_item().full_name + "!"
		attack_intiation_str = ("Fearlessly, you charge forward weilding " +  burt_weapon_name +
				" while the " + self.full_name + " attempts to parry" + hand_text)
		active_gs.buffer(attack_intiation_str)

		# determine if creature has an attack response and if so what response key to use
		creature_has_response = True
		if burt_weapon_obj in self.attacked_dict:
			dict_key = burt_weapon_obj
		elif 'def_attack' in self.attacked_dict:
			dict_key = 'def_attack'
		else:
			creature_has_response = False

		# if no response, buffer default text and exit
		if not creature_has_response:
			active_gs.buffer(f"At the last minute the {self.full_name} dodges your fearsome attack with {burt_weapon_name}.")
			return 

		#	if creature_has_response, buffer custom_str if it exists
		custom_key = self.attacked_dict[dict_key]['custom_key']
		try:
			custom_str = descript_dict[custom_key]
			active_gs.buffer(custom_str)
		except:
			pass

### NOTE: GENERATING win_weapon DOESN'T REALLY SOLVE THE PROBLEM... I ACTUALLY NEED TO DETERMINE 'WINNER' AND BASE DESC OFF THEIR 'HAND'
### NOTE: ALSO NOT DETERMINING IF hand_is_empty() IN CONJUNCTION WITH 'WINNER' AND ATTACK RESOLUTION
### NOTE: REALLY NEED TO FIGURE OUT 'WINNER' *FIRST* - THEN HAND STATE AND WEAPON ADJ FLOW FROM THERE
### NOTE: order of operations = <attacker> => <custom> => <winner>

		# implement the results of the attack_response result_code and compose the 2nd half of the attack resolution string
		if self.attacked_dict[dict_key]['result_code'] == 'creature_flee':
			room_obj = active_gs.get_room()
			room_obj.floor_lst_remove(self)
			res_key = 'creature_flee_default_res_key'
			if creature.hand_is_empty(): # NOTE: IS AN INCOMPLETE SOLUTION - NEED TO FIX WHEN COMBINING attack() and attack_burt()
				win_weapon = ""
			else:
				win_weapon = burt_weapon_obj.full_name
		elif self.attacked_dict[dict_key]['result_code'] == 'burt_death':
			active_gs.set_game_ending('death')
			res_key = 'burt_death_default_res_key'
			win_weapon = self.get_hand_item().full_name
		elif self.attacked_dict[dict_key]['result_code'] == 'creature_death':
			room_obj = active_gs.get_room()
			room_obj.floor_lst_remove(self)
			room_obj.floor_lst_extend(self.bkpk_lst)
			room_obj.floor_lst_extend(self.hand_lst)
			room_obj.floor_lst_extend(self.worn_lst)
			res_key = 'creature_death_default_res_key'
			win_weapon = burt_weapon_obj.full_name						
		else:
			res_key = 'no_result_default_res_key'
			win_weapon = burt_weapon_obj.full_name

		# compose the start of the attack resolution string with verb and adj detail if the creature is weilding a weapon
		hand_lst = creature.hand_lst
		if creature.hand_is_empty():
			attack_start_str = ""
		elif hand_lst[0].is_weapon():
			hand_item = hand_lst[0]
			weapon_desc_max = len(hand_item.desc_lst) - 1
			weapon_desc_index = random.randint(0, weapon_desc_max)
			weapon_verb = hand_item.desc_lst[weapon_desc_index][0]
			weapon_adj_noun = hand_item.desc_lst[weapon_desc_index][1]
##			attack_start_str = "The " + hand_item.full_name + " " + weapon_verb + " through the air with a " + weapon_adj_noun + ". "
			attack_start_str = "The " + win_weapon + " " + weapon_verb + " through the air with a " + weapon_adj_noun + ". "
		else:
##			attack_start_str = "The " + hand_item.full_name + " whizzes through the air. "
			attack_start_str = "The " + win_weapon + " whizzes through the air. "

		# buffer the full attack resolution string
		attack_res_str = attack_start_str + descript_dict[res_key]
		active_gs.buffer(attack_res_str)
		return 


	def attack_burt(self, active_gs):
		# create and buffer attack_initiation_str
		creature = active_gs.hero
		if creature.hand_is_empty():
			burt_weapon_name = 'your fist'
			burt_weapon_obj = None
		else:
			hand_lst = creature.hand_lst
			burt_weapon_obj = hand_lst[0]
			burt_weapon_name = 'the ' + burt_weapon_obj.full_name
		if self.hand_is_empty():
			hand_text = ""
		else:
			hand_text = " with the " + self.get_hand_item().full_name

		attack_intiation_str = ("The " + self.full_name + " attacks" + hand_text + " and you attempt to parry with " +  burt_weapon_name + "!")
		active_gs.buffer(attack_intiation_str)

		# determine if creature has an attack response and if so, what response key to use
		creature_has_response = True
		if burt_weapon_obj in self.attacking_dict:
			dict_key = burt_weapon_obj
		elif 'def_attack' in self.attacking_dict:
			dict_key = 'def_attack'
		else:
			creature_has_response = False

		# if no response, buffer default text and exit
		if not creature_has_response:
			active_gs.buffer("At the last minute you parry the attack from the " + self.full_name + " with " + burt_weapon_name + ".")
			return

		#	if creature_has_response, buffer custom_str if it exists
		custom_key = self.attacking_dict[dict_key]['custom_key']
		try:
			custom_str = descript_dict[custom_key]
			active_gs.buffer(custom_str)
		except:
			pass

		# implement the results of the attack_response result_code and compose the 2nd half of the attack resolution string
		if self.attacking_dict[dict_key]['result_code'] == 'creature_flee':
			room_obj = active_gs.get_room()
			room_obj.floor_lst_remove(self)
			res_key = 'creature_flee_default_res_key'
			win_weapon = burt_weapon_obj.full_name
		elif self.attacking_dict[dict_key]['result_code'] == 'burt_death':
			active_gs.set_game_ending('death')
			res_key = 'burt_death_default_res_key'
			win_weapon = self.get_hand_item().full_name
		elif self.attacking_dict[dict_key]['result_code'] == 'creature_death':
			room_obj = active_gs.get_room()
			room_obj.floor_lst_remove(self)
			room_obj.floor_lst_extend(self.bkpk_lst)
			room_obj.floor_lst_extend(self.hand_lst)
			room_obj.floor_lst_extend(self.worn_lst)
			room_obj.floor_lst_append(self.corpse)
			res_key = 'creature_death_default_res_key'
			win_weapon = burt_weapon_obj.full_name
		else:
			res_key = 'no_result_default_res_key'
			win_weapon = self.get_hand_item().full_name

### NOTE: GENERATING win_weapon DOESN'T REALLY SOLVE THE PROBLEM... I ACTUALLY NEED TO DETERMINE 'WINNER' AND BASE DESC OFF THEIR 'HAND'

		# compose the start of the attack resolution string with verb and adj detail if the creature is weilding a weapon
		if self.hand_is_empty():
			attack_start_str = ""
		elif self.get_hand_item().is_weapon:
			weapon_desc_max = len(self.get_hand_item().desc_lst) - 1
			weapon_desc_index = random.randint(0, weapon_desc_max)
			weapon_verb = self.get_hand_item().desc_lst[weapon_desc_index][0]
			weapon_adj_noun = self.get_hand_item().desc_lst[weapon_desc_index][1]
##		attack_start_str = "The " + self.get_get_hand_item().full_name + " " + weapon_verb + " through the air with a " + weapon_adj_noun + ". "
			attack_start_str = "The " + win_weapon + " " + weapon_verb + " through the air with a " + weapon_adj_noun + ". "
		else:
##	attack_start_str = "The " + self.get_hand_item().full_name + "whizzes through the air. "
			attack_start_str = "The " + win_weapon + "whizzes through the air. "

		# buffer the full attack resolution string
		attack_res_str = attack_start_str + descript_dict[res_key]
		active_gs.buffer(attack_res_str)
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

"""
