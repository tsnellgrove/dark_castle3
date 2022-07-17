# program: dark castle v3.68
# name: Tom Snellgrove
# date: July 7, 2022
# description: class deffinition module for Creatures

### import
import random
from noun_class_def import ViewOnly
from static_gbl import descript_dict

### classes
class Creature(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, creature_state, mach_obj_lst, show_item_dict, give_item_dict,
		attack_creature_dict, attack_burt_dict, creature_items_lst, dead_creature_obj, hand_lst, is_attackable):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._creature_state = creature_state
				self._mach_obj_lst = mach_obj_lst
				self._show_item_dict = show_item_dict
				self._give_item_dict = give_item_dict
				self._attack_creature_dict = attack_creature_dict
				self._attack_burt_dict = attack_burt_dict
				self._creature_items_lst = creature_items_lst
				self._dead_creature_obj = dead_creature_obj
				self._hand_lst = hand_lst
				self._is_attackable = is_attackable

# *** setters & getters ***

		@property
		def creature_state(self):
				return self._creature_state

		@creature_state.setter
		def creature_state(self, new_state):
				self._creature_state = new_state

		@property
		def mach_obj_lst(self):
				return self._mach_obj_lst

		@property
		def show_item_dict(self):
				return self._show_item_dict

		@property
		def give_item_dict(self):
				return self._give_item_dict

		@property
		def attack_creature_dict(self):
				return self._attack_creature_dict

		@property
		def attack_burt_dict(self):
				return self._attack_burt_dict

		@property
		def creature_items_lst(self):
				return self._creature_items_lst

		@creature_items_lst.setter
		def creature_items_lst(self, new_state):
				self._creature_items_lst = new_state

		@property
		def dead_creature_obj(self):
				return self._dead_creature_obj

		@property
		def hand_lst(self):
				return self._hand_lst

		@hand_lst.setter
		def hand_lst(self, new_state):
				self._hand_lst = new_state

		@property
		def is_attackable(self):
				return self._is_attackable

# *** class identification ***

		def is_creature(self):
				return True

# *** hand ***

		def hand_lst_append(self, item):
				self._hand_lst.append(item)

		def hand_lst_remove(self, item):
				self._hand_lst.remove(item)

		def hand_empty(self):
				return not bool(self.hand_lst)

		def hand_item(self):
				return self.hand_lst[0]

		def put_in_hand(self, new_item):
				if not self.hand_empty():
						hand_item = self.hand_item()
						self.creature_lst_append_item(hand_item)
						self.hand_lst_remove(hand_item)
				self.hand_lst_append(new_item)

# *** obj_lst ***

		def creature_lst_append_item(self, item):
				self._creature_items_lst.append(item)

		def creature_lst_remove_item(self, item):
				self._creature_items_lst.remove(item)

# *** complex methods ***

		def examine(self, active_gs):
				super(Creature, self).examine(active_gs)
				if not self.hand_empty():
						active_gs.buffer("The " + self.full_name + " is holding a " + self.hand_item().full_name)

		def show(self, obj, active_gs):
				if not active_gs.hand_check(obj):
						active_gs.buffer("You aren't holding the " + obj.full_name)
				else:
						creature_has_response = True
						if obj in self.show_item_dict:
								dict_key = obj
						elif 'def_show' in self.show_item_dict:
								dict_key = 'def_show'
						else:
								creature_has_response = False
						if creature_has_response:
								response_key = self.show_item_dict[dict_key]
								response_str = descript_dict[response_key]
								active_gs.buffer(response_str)
						else:
								active_gs.buffer("The " + self.full_name + " shows no interest in the " + obj.full_name + ".")

		def give(self, obj, active_gs):
				if not active_gs.hand_check(obj):
						active_gs.buffer("You aren't holding the " + obj.full_name)
						return

				creature_has_response = True
				if obj in self.give_item_dict:
						dict_key = obj
				elif 'def_give' in self.give_item_dict:
						dict_key = 'def_give'
				else:
						creature_has_response = False

				if not creature_has_response:
						active_gs.buffer("The " + self.full_name + " shows no interest in the " + obj.full_name + ".")
						return

				response_key = self.give_item_dict[dict_key]['response_key']
				response_str = descript_dict[response_key]
				accept_item = self.give_item_dict[dict_key]['accept_item']
				give_item = self.give_item_dict[dict_key]['give_item']
				new_descript_key = self.give_item_dict[dict_key]['new_descript_key']

				if accept_item:
						active_gs.hand_lst_remove_item(obj)
						self.put_in_hand(obj) # messes up goblin holding grimy_axe ; need an auto_action
				if give_item != None:
						self.creature_lst_remove_item(give_item)
						active_gs.hand_lst_append_item(give_item)
				if new_descript_key != None:
						self.descript_key = new_descript_key
				active_gs.buffer(response_str)
				return 

		def attack(self, active_gs):
				if not self.is_attackable:
						try:
								descript_key = 'not_attackable_' + self.full_name
								active_gs.buffer(descript_dict[descript_key])
						except:
								active_gs.buffer(descript_dict['not_attackable_default'])
						return

				if active_gs.hand_empty():
						burt_weapon_name = 'your fist'
						burt_weapon_obj = None
				else:
						hand_lst = active_gs.get_hand_lst()
						burt_weapon_obj = hand_lst[0]
						burt_weapon_name = 'the ' + burt_weapon_obj.full_name

				if self.hand_empty():
						hand_text = "!"
				else:
						hand_text = " with the " + self.hand_item().full_name + "!"

				attack_intiation_str = ("Fearlessly, you charge forward weilding " +  burt_weapon_name +
								" while the " + self.full_name + " attempts to parry" + hand_text)
				active_gs.buffer(attack_intiation_str)

				creature_has_response = True
				if burt_weapon_obj in self.attack_creature_dict:
						dict_key = burt_weapon_obj
				elif 'def_attack' in self.attack_creature_dict:
						dict_key = 'def_attack'
				else:
						creature_has_response = False

				if creature_has_response:
						custom_key = self.attack_creature_dict[dict_key]['custom_key']
						response_str = descript_dict[custom_key]
						active_gs.buffer(response_str)

# *** burt doesn't attack that often and generally has long descriptions when he does... maybe for burt attacks weapon words go in default? ***

						if self.attack_creature_dict[dict_key]['result_code'] == 'creature_flee':
								room_obj = active_gs.get_room()
								room_obj.room_obj_lst_remove(self)
								res_key = 'creature_flee_default_res_key'
						elif self.attack_creature_dict[dict_key]['result_code'] == 'burt_death':
								active_gs.set_game_ending('death')
								res_key = 'burt_death_default_res_key'
						elif self.attack_creature_dict[dict_key]['result_code'] == 'creature_death':
								room_obj = active_gs.get_room()
								room_obj.room_obj_lst_remove(self)
								room_obj.room_obj_lst_extend(self.creature_items_lst)
								room_obj.room_obj_lst_extend(self.hand_lst)
								room_obj.room_obj_lst_append(self.dead_creature_obj)
								res_key = 'creature_death_default_res_key'
						else:
								res_key = 'no_result_default_res_key'
				else:
						active_gs.buffer("At the last minute the " + self.full_name + " dodges your fearsome attack with " + burt_weapon_name + ".")

		def attack_burt(self, active_gs):
				if active_gs.hand_empty():
						burt_weapon_name = 'your fist'
						burt_weapon_obj = None
				else:
						hand_lst = active_gs.get_hand_lst()
						burt_weapon_obj = hand_lst[0]
						burt_weapon_name = 'the ' + burt_weapon_obj.full_name
				if self.hand_empty():
						hand_text = ""
				else:
						hand_text = " with the " + self.hand_item().full_name

				attack_intiation_str = ("The " + self.full_name + " attacks" + hand_text + " and you attempt to parry with " +  burt_weapon_name + "!")
				active_gs.buffer(attack_intiation_str)

				creature_has_response = True
				if burt_weapon_obj in self.attack_burt_dict:
						dict_key = burt_weapon_obj
				elif 'def_attack' in self.attack_burt_dict:
						dict_key = 'def_attack'
				else:
						creature_has_response = False

#				attack_intiation_str = ("The " + self.full_name + " attacks" + hand_text + " and you attempt to parry with " +  burt_weapon_name + "!")
#				active_gs.buffer(attack_intiation_str)

				if not creature_has_response:
						active_gs.buffer("At the last minute you parry the attack from the " + self.full_name + " with " + burt_weapon_name + ".")
						return

#				if creature_has_response:
				custom_key = self.attack_burt_dict[dict_key]['custom_key']
#						response_str = descript_dict[custom_key]
				try:
						custom_str = descript_dict[custom_key]
						active_gs.buffer(custom_str)
				except:
						pass
#				else:
#						active_gs.buffer("At the last minute you parry the attack from the " + self.full_name + " with " + burt_weapon_name + ".")

				if self.hand_empty():
						attack_start_str = ""
				elif self.hand_item().is_weapon:
						weapon_desc_max = len(self.hand_item().desc_lst) - 1
						weapon_desc_index = random.randint(0, weapon_desc_max)
						weapon_verb = self.hand_item().desc_lst[weapon_desc_index][0]
						weapon_adj_noun = self.hand_item().desc_lst[weapon_desc_index][1]
						attack_start_str = "The " + self.hand_item().full_name + " " + weapon_verb + " through the air with a " + weapon_adj_noun + ". "
				else:
						attack_start_str = "The " + self.hand_item().full_name + "whizzes through the air. "
#						attack_str = attack_start_str + response_str
#						active_gs.buffer(attack_str)

				if self.attack_burt_dict[dict_key]['result_code'] == 'creature_flee':
						room_obj = active_gs.get_room()
						room_obj.room_obj_lst_remove(self)
						res_key = 'creature_flee_default_res_key'
				elif self.attack_burt_dict[dict_key]['result_code'] == 'burt_death':
						active_gs.set_game_ending('death')
						res_key = 'burt_death_default_res_key'
				elif self.attack_burt_dict[dict_key]['result_code'] == 'creature_death':
						room_obj = active_gs.get_room()
						room_obj.room_obj_lst_remove(self)
						room_obj.room_obj_lst_extend(self.creature_items_lst)
						room_obj.room_obj_lst_append(self.dead_creature_obj)
						res_key = 'creature_death_default_res_key'
				else:
						res_key = 'no_result_default_res_key'

#				attack_str = attack_start_str + response_str
				attack_res_str = attack_start_str + descript_dict[res_key]
				active_gs.buffer(attack_res_str)

#				else:
#						active_gs.buffer("At the last minute you parry the attack from the " + self.full_name + " with " + burt_weapon_name + ".")
