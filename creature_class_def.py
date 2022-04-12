# program: dark castle v3.60
# name: Tom Snellgrove
# date: Mar 24, 2022
# description: class deffinition module for Creatures

### import
from noun_class_def import ViewOnly
from static_gbl import descript_dict

### classes
class Creature(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, creature_state, mach_obj_lst, show_item_dict, give_item_dict,
		attack_creature_dict, attack_burt_dict, creature_items_lst, dead_creature_obj):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._creature_state = creature_state
				self._mach_obj_lst = mach_obj_lst
				self._show_item_dict = show_item_dict
				self._give_item_dict = give_item_dict
				self._attack_creature_dict = attack_creature_dict
				self._attack_burt_dict = attack_burt_dict
				self._creature_items_lst = creature_items_lst
				self._dead_creature_obj = dead_creature_obj

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

		def creature_lst_append_item(self, item):
				self._creature_items_lst.append(item)

		def creature_lst_remove_item(self, item):
				self._creature_items_lst.remove(item)

		@creature_items_lst.setter
		def creature_items_lst(self, new_state):
				self._creature_items_lst = new_state

		@property
		def dead_creature_obj(self):
				return self._dead_creature_obj


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
				else:
						creature_has_response = True
						if obj in self.give_item_dict:
								dict_key = obj
						elif 'def_give' in self.give_item_dict:
								dict_key = 'def_give'
						else:
								creature_has_response = False
						if creature_has_response:
								response_key = self.give_item_dict[dict_key]['response_key']
								response_str = descript_dict[response_key]
								accept_item = self.give_item_dict[dict_key]['accept_item']
								give_item = self.give_item_dict[dict_key]['give_item']
								new_descript_key = self.give_item_dict[dict_key]['new_descript_key']
								if accept_item:
										active_gs.hand_lst_remove_item(obj)
										self.creature_lst_append_item(obj)
								if give_item != None:
										self.creature_lst_remove_item(give_item)
										active_gs.hand_lst_append_item(give_item)
								if new_descript_key != None:
										self.descript_key = new_descript_key
								active_gs.buffer(response_str)
						else:
								active_gs.buffer("The " + self.full_name + " shows no interest in the " + obj.full_name + ".")

		def attack(self, active_gs):
				if active_gs.hand_empty():
						burt_weapon_name = 'your fist'
						burt_weapon_obj = None
				else:
						hand_lst = active_gs.get_hand_lst()
						burt_weapon_obj = hand_lst[0]
						burt_weapon_name = 'the ' + burt_weapon_obj.full_name

				creature_has_response = True
				if burt_weapon_obj in self.attack_creature_dict:
						dict_key = burt_weapon_obj
				elif 'def_attack' in self.attack_creature_dict:
						dict_key = 'def_attack'
				else:
						creature_has_response = False

				active_gs.buffer("Fearlessly, you charge forward weilding " +  burt_weapon_name + "!")
				if creature_has_response:
						response_key = self.attack_creature_dict[dict_key]['response_key']
						response_str = descript_dict[response_key]
						active_gs.buffer(response_str)
						if self.attack_creature_dict[dict_key]['result_code'] == 'creature_flee':
								room_obj = active_gs.get_room()
								room_obj.room_obj_lst_remove(self)
						elif self.attack_creature_dict[dict_key]['result_code'] == 'burt_death':
								active_gs.set_game_ending('death')
						elif self.attack_creature_dict[dict_key]['result_code'] == 'creature_death':
								room_obj = active_gs.get_room()
								room_obj.room_obj_lst_remove(self)
								room_obj.room_obj_lst_extend(self.creature_items_lst)
								room_obj.room_obj_lst_append(self.dead_creature_obj)
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

				creature_has_response = True
				if burt_weapon_obj in self.attack_burt_dict:
						dict_key = burt_weapon_obj
				elif 'def_attack' in self.attack_burt_dict:
						dict_key = 'def_attack'
				else:
						creature_has_response = False

				active_gs.buffer("You attempt to parry the creature's attack with " +  burt_weapon_name + "!")
				if creature_has_response:
						response_key = self.attack_burt_dict[dict_key]['response_key']
						response_str = descript_dict[response_key]
						active_gs.buffer(response_str)
						if self.attack_burt_dict[dict_key]['result_code'] == 'creature_flee':
								room_obj = active_gs.get_room()
								room_obj.room_obj_lst_remove(self)
						elif self.attack_burt_dict[dict_key]['result_code'] == 'burt_death':
								active_gs.set_game_ending('death')
						elif self.attack_burt_dict[dict_key]['result_code'] == 'creature_death':
								room_obj = active_gs.get_room()
								room_obj.room_obj_lst_remove(self)
								room_obj.room_obj_lst_extend(self.creature_items_lst)
								room_obj.room_obj_lst_append(self.dead_creature_obj)
				else:
						active_gs.buffer("At the last minute you parry the attack from the " + self.full_name + " with " + burt_weapon_name + ".")