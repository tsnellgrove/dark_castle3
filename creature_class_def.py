# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 20, 2023
# description: class deffinition module for Creatures

### import
import random
from base_class_def import ViewOnly
from static_gbl import descript_dict

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
		worn_lst, feature_lst, invis_lst, give_dict, is_attackable, attacked_dict):
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

	# *** class identity methods ***
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

	# NOTE: only works for Creature class; not generalized for other obj
	def is_contained(self, active_gs):
		return self not in active_gs.map.get_obj_room(self).floor_lst

	def get_contained_by(self, active_gs):
		if not self.is_contained:
			raise ValueError(f"{obj.full_name} is not in a container.")
		else:
			for obj in active_gs.map.get_obj_room(self).floor_lst:
				if obj.is_seat() and self in obj.contain_lst:
					return obj
		raise ValueError(f"{obj.full_name} not found.")

	# *** display methods ***
	def has_cond(self, active_gs):
		return self.is_contained(active_gs)

	def disp_cond(self, active_gs):
		""" Displays object-specific conditions. Used in examine().
		"""
		if self.has_cond(active_gs):
			if self == active_gs.hero:
				active_gs.buff_no_cr(f"You are seated in the {self.get_contained_by(active_gs).full_name}.")
				active_gs.buff_cr()
				active_gs.buff_cr()
			else:
				active_gs.buff_no_cr(f"The {self.full_name} is seated in the {self.get_contained_by(active_gs).full_name}.")
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
			active_gs.buff_no_cr(f"In your off hand you hold a Brass Lantern.")
			if (not self.bkpk_is_empty()) or (not self.hand_is_empty()) or (not self.worn_is_empty()):
					active_gs.buff_cr()
					active_gs.buff_cr()
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
	def show(self, obj, active_gs, mode=None):
		""" Extends Writing.show(). Shows an item in your hand to another creature.
		"""
		if mode is None:
			mode = 'std'
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
		base_error = super(Creature, self).give(obj, active_gs)
		""" Gives an item to another creature.
		"""
		if base_error:
			return
		# determine other creature's response
		creature = active_gs.hero
		if obj.err_not_in_hand(creature, active_gs):
			return
		if self == creature:
			active_gs.buffer(f"With great formality and many words of thanks, you hand the {obj.full_name} to yourself.")
			return
		
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
		base_error = super(Creature, self).attack(src_obj, active_gs)
		""" Attacks a target_creature with an item
		"""
		if base_error:
			return
		# destermine src_creature & tgt_creature
		if src_creature is None:
			src_creature = active_gs.hero
		tgt_creature = self

		# display error & return on command failures
		# it is assumed (pronoun-wise) that only the player will attack in an unallowed fashion
		if not tgt_creature.is_attackable:
			try:
				active_gs.buffer(descript_dict[f"not_attackable_{src_creature.name}_{tgt_creature.name}"])
			except:
				active_gs.buffer("You consider attacking but then think better of it. There must be another path to victory.")
			return
		if (not src_obj in src_creature.feature_lst) and (not src_creature.chk_in_hand(src_obj)):
			active_gs.buffer(f"You are not holding the {src_obj.full_name} in your hand.")
			return 
		if (src_obj in src_creature.feature_lst) and (not src_creature.hand_is_empty()):
			active_gs.buffer(f"You can't attack with your {src_obj.full_name} while you're holding the {src_creature.get_hand_item().full_name}.")
			return 
		if src_creature == tgt_creature:
			active_gs.buffer("You can't attack yourself!")
			return
		
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
		resolution_end_str = f"{lose_creature_disp} {descript_dict[result_code]} "

		# buffer the full 'attack resolution'
		active_gs.buffer(f"{resolution_strt_str}{resolution_end_str}")
		return 

	def stand(self, active_gs):
#	def exit(self, active_gs):
		""" Enables a Creature to stand up from a Seat or Bed
		"""
		room = active_gs.map.get_obj_room(self)
		if self in room.floor_lst:
			active_gs.buffer(f"You're already standing in the {room.full_name}!")
			return
		
		room.remove_item(self, active_gs)
		room.floor_lst_append(self)

		# if hero_creature not in current room, exit with no display
		if room != active_gs.get_room():
			return 

		if self == active_gs.hero:
			active_gs.buffer(f"You are now standing in the {room.full_name}.")
		else:
			active_gs.buffer(f"The {self.full_name} is now standing.")
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
			The attack() method is a bit more complex and is intended to enable combat between creatures. In Dark Castle, combat is a purely logical exercise. If you attack a Creature with the correct weapon at the correct time in the correct place, you will always win. Attack is a prepositional command in the form of 'Attack <creature> with <object>'. The attack object must match whatever the attacker is holding in their hand. If the attacker's hand is empty, then unarmed strikes are supported (but often not very effective). The results of an attack include the attacked creature dodging or fleeing and extend all the way up to or or the other creatures being slain. it's easy to imagine attack() provoking a more complex response than these outcomes - but those are outside the scope of the method and should be implemented via a Modular Machine.
		
		Implementation Detail:
			As verb methods go, attack() is fairly complex and perhaps it is over-engineered. The complexity comes from several sources.
			
			For one, it is a symetric method that can be used by any creature - not just by Burt. This means that Burt could attack a creature. Or a creature could attack Burt. Or possibly one creature could attack another without Burt even being in the room (Burt attacking Burt is not allowed and is handedled as a command error). This variety of possible combatants drives the need for a lot of case checking and pronoun tuning. It also forces the method to be rigorous about output... all game state changes must be performed first, then we check to see if Burt is even in the room, and if not we return without displaying any text (silent mode).

			Another complexity driver is the variety of object types that Burt can attack with. Attack objects are categorized as 'weapon' (i.e. they are of class Weapon), 'unarmed' (i.e. they reside in a creature's feature_lst), or 'item' (everything else). Attack results can then varry based on the attacking creature, and the exact object or object category that each combatant is holding. It's a felixble system... but again, arguably over engineered. 

			A final driver for complexity is the wealth of description that an attack() generates. Assuming that Burt is in the room to witness (or participate in) the proceedings, there are a total of four separately generated display strings for a given attack():
				1) The attack initiation string - which states who is attacking with what and what the attacked creature attempts to do (i.e. parry or dodge).
				2) Custom attack response - this is an auto-gen string which may or may not exist and is displayed if it does.
				3) Attack Resolution First Clause - this describes the attack stroke of the winner of the combat round. For weapons, randomly chosen custom text is used that's specific to the weapon object.
				4) Attack Resolution Second Clause - describes the results for the combat looser (which can varry from "easily dodges" to "is slain").
			Again, quite possibly over-engineered - but hopefully enjoyable to read when combat does breat out!
			
			In the context of historic text adventure combat, I'm guess that DCv3 is simpler than Zork's D&D-based attack scheme but more complex than other Infocom games that came after it.


		Program Architecture:
			The attack() method has the following sections:
			1) Command Errors. This section detects command errors, displays error text, and then exits. This is the one part of the method that is *not* fully symetric. All errors are written with the premise that Burt is attacking - the assumption here is that if a designer is using attack() for a creature then it is there job to use it correctly.
			2) Results. A list of possible result_keys is generated. This list is compared to the keys in the tgt_creature's attacked_dict (e.g. 'shiny_sword_burt_*') and the first hit is used to lookup the result_code value (e.g. 'tgt_death') with a default value used if no key hit occurs. Based on the result code, the attack results are carried out (e.g. in the case of 'tgt_death', the creature is removed from the game and the creature's inventory is droped on the floor of the room).
			3) Silent mode check. We check to see if Burt is in the room; if not, we exit.
			4) Display attack strings. Determine the win_obj and lose_creature and set pronouns appropriately (see Implementation Detail for more info).

		Game Design:
			It is said that one flouts convention at one's peril. If so, I am indeed courting doom with my approach to hand inventory. Inventory management in general is deemed to be a necessary evil of the Text Adventures genre... and to the best of my knowledge Dark Castle is unique in making the player manage an entire separate hand inventory on top of their inventory of carried items and worn garments.

			My rational is that I am trying to make Dark Castle more populated than your typical Infocom adventure - and also more interactive. Being able to see what a creature is carying in their hand gives the player more information about them. And creatures in the game can react to Burt based on what *he* is carrying in his hand. Perhaps a store keeper will close up their shop if they see Burt approaching with a weapon. But on the other hand, if Burt is attcked and not carrying a weapon, he is much more likely to perish. The intent here is to create a tesnsion between being prepared in a perilous environment and adhering to the social contract of a community.

			Time will tell whether any of these good intentions warrant yet more inventory management... but this is what I was aiming for.

		Historic Note:
			In the first functional version of DCv3, Burt was not an object - just a collection of dictionary entries in the GameState object. From a developement standpoint this makes sense... the Creature class was the last and most complex non-machine class I created. The initial player state information needed to be as simple as possible as I learned how on earth OOP worked.

			My first hint that Burt should be a variable came from reading Tim Anderson's wonderful History of Zork (https://gunkies.org/wiki/History_of_Zork). Among other things, this mentioned that from early on in Zork, there was a player entitiy that could move from room to room. I didn't have one of these and began to wonder if I should - but clearly it would be a big effort so I pushed it off for a later update.

			The real revelation came as I was wrapping up the very last, most complex, Modular Machine for DCv3, goblin_attack_mach. It seemed straight-forward - if the conditions were met, the Goblin would simply use the attack() command (which back then was 2_word, not prep) to attack the Burt object - and I'd be all set. But of course, once I got to coding it, I was reminded that there *was* no Burt object. The short term hack was to create a secret_verb method called attack_burt() - which was very similar to attack() but with different pronouns, the ability to access the burt GameState dictionary keys, and no target creature argument... since, of course, it was only ever used to attack_burt...

			That got the game to 'done' - but it was such an egregious hacke that I knew I'd have to come back and fix it. At the time I wrote: 

				"'attack_burt' is an awkward 'hidden' verb that enables a creature to proactively attack Burt. Among other things, this work-around highlights that Burt should really be an object himself - rather than an amorphous set of attributes distributed across game state. But this will not be a minor undertaking - so for now, we have the attack_burt() method - which enables 'attack' to remain a 2word command without requiring a 'burt' object to exist."
			
			The obvious solution was to make Burt an object of class Creature - but this was a significant undertaking given how primative the original Creature class was (at the time, Creature objects did not have hand or worn attributes - among others). More challenging yet, every single method that impacted Burt's inventory and location (e.g. take, drop, wear, go, etc..) had to be heavily re-written. It was daunting, but it was also very clearly the 'the way' - so making burt a Creature object became one of the tentpole objectives of the DCv3 refactoring.

			go() was actually the very first verb method re-written to be 'symetric' (i.e. a verb method that could be called by either the burt object or another Creature object). attack() is now the second. The goal is to eventually make all verb methods (except perhaps examine() and read()) symetric so that Creature interaction can be as organic and uniform as possible.
"""
