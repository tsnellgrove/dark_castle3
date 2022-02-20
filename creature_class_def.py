# program: dark castle v3.59
# name: Tom Snellgrove
# date: Feb 18, 2022
# description: class deffinition module for Creatures

### import
from noun_class_def import ViewOnly
from static_gbl import descript_dict

### classes
class Creature(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, creature_state, mach_obj_lst, show_item_dict, give_item_dict, attack_trgt_dict, attack_src_dict, creature_items_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._creature_state = creature_state
				self._mach_obj_lst = mach_obj_lst
				self._show_item_dict = show_item_dict
				self._give_item_dict = give_item_dict
				self._attack_trgt_dict = attack_trgt_dict
				self._attack_src_dict = attack_src_dict
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
								descript_key = self.show_item_dict[dict_key]
								descript_str = descript_dict[descript_key]
								active_gs.buffer(descript_str)
						else:
								active_gs.buffer("The " + self.full_name + " shows no interest in the " + obj.full_name + ".")

