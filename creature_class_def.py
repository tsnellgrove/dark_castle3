# program: dark castle v3.59
# name: Tom Snellgrove
# date: Feb 18, 2022
# description: class deffinition module for Creatures

### import
from noun_class_def import ViewOnly
from static_gbl import descript_dict

### classes
class Creature(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, creature_state, mach_obj_lst, show_item_dict, give_item_dict, 
		attack_creature_dict, creature_items_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._creature_state = creature_state
				self._mach_obj_lst = mach_obj_lst
				self._show_item_dict = show_item_dict
				self._give_item_dict = give_item_dict
				self._attack_creature_dict = attack_creature_dict
				self._creature_items_lst = creature_items_lst

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
		def attack_trgt_dict(self):
				return self._attack_trgt_dict

		@property
		def attack_src_dict(self):
				return self._attack_src_dict

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
				if active_gs.hand_empty:
						burt_weapon = 'fist'
				else:
						hand_lst = active_gs.get_hand_lst()
						burt_weapon = hand_lst[0]
				creature_has_response = True
				if burt_weapon in self.attack_creature_dict:
						dict_key = burt_weapon
				elif 'def_attack' in self.attack_creature_dict:
						dict_key = 'def_attack'
				else:
						creature_has_response = False
				if creature_has_response:
						response_key = self.attack_creature_dict[dict_key]['response_key']
						response_str = descript_dict[response_key]
						active_gs.buffer(response_str)

				else:
						active_gs.buffer("At the last minute the " + self.full_name + " dodges your fearsome attack with the " + burt_weapon + ".")
