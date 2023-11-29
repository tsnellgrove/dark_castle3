# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: Invisible class deffinition module

### import
import random
from dc3.data.static_gbl import static_dict


### classes
class Invisible(object):
	def __init__(self, name):
		self._name = name # text str of each obj's canonical name; should be unique and immutable
		""" Invisible is the root object class. There are no instantiated objects of class Invisible but all objects in the game inherit the name attribute, class identity methods, and error sub-system from Invisible. 
		"""

	# *** getters & setters ***
	@property
	def name(self):
		return self._name


	# *** universal scope methods ***
	def get_contain_lst(self, active_gs):
		return []

	def get_vis_contain_lst(self, active_gs):
		return []

	def chk_contain_item(self, item):
		return False

	def remove_item(self, item, active_gs):
		pass
		return 

	# *** class identity methods ***
	def is_invisible(self):
		return True

	def is_writing(self):
		return False

	def is_viewonly(self):
		return False

	def is_item(self):
		return False

	def is_food(self):
		return False

	def is_liquid(self):
		return False

	def is_weapon(self):
		return False

	def	is_openable(self):
		return False
	
	def is_lockable(self):
		return False

	def	is_container(self):
		return False

	def is_room(self):
		return False

	def is_creature(self):
		return False

	def is_switch(self):
		return False

	def is_buttonswitch(self):
		return False

	def is_springsliderswitch(self):
		return False

	def is_leverswitch(self):
		return False

	def is_timer(self):
		return False

	def is_mach(self):
		return False

	def is_garment(self):
		return False

	def is_seat(self):
		return False
	
	def is_receptacle(self):
		return False

	# *** debug methods ###
	def where_is(self, active_gs, mode=None):
		""" Reports the weight of an Item. Only usable in debug mode.
		"""
		if mode is None:
			mode = 'std'
		creature = active_gs.hero
		
		if not active_gs.map.chk_obj_exist(self, active_gs):
			active_gs.io.buffer(f"The {self.full_name} does not currently exist in the game.")
			return
		room = active_gs.map.get_obj_room(creature, active_gs)
		if room.chk_is_vis(self, active_gs):
			active_gs.io.buffer(f"The {self.full_name} is visible in the {room.full_name}, where you are presently.")
		elif active_gs.map.get_obj_room(self, active_gs) == room:
			active_gs.io.buffer(f"The {self.full_name} is not visible to you but is in the {room.full_name}, where you are presently.")
		else:
			active_gs.io.buffer(f"The {self.full_name} is in the {active_gs.map.get_obj_room(self, active_gs).full_name}.")
		in_inv, inv_creature = active_gs.map.chk_obj_in_creature_inv(self, active_gs)
		if in_inv:
			active_gs.io.buffer(f"The {self.full_name} is in the inventory of the {inv_creature.full_name}.")
		return


	# *** standard errors ###	
	def err_invis_obj(self, creature, active_gs):
		if self.is_invisible():
			active_gs.io.buffer(f"During a brief moment of clarity, you see that the world around you is nothing but lines of code... vertical trails of glowing green characters tumble down across your vision... realizing that you are The One, you reach for the {self.full_name}... but just as your fingers approach it, the vision evaporates and your insight into Simulation Theory of Life fades from your mind and is forgotten forever...")
			return True
		return False

	def err_wrt_not_vis(self, creature, active_gs):
		room = active_gs.map.get_obj_room(creature, active_gs)
		if self.is_writing() and not room.chk_wrt_is_vis(self, active_gs):
			active_gs.io.buffer(f"You can't see {self.full_name} written on anything here.")
			return True
		return False

	def err_wrt_not_in_reach(self, creature, active_gs):
		if self.is_writing() and creature.is_contained(active_gs) and not creature.chk_wrt_in_reach(self, active_gs):
			active_gs.io.buffer(f"You'll have to exit the {creature.get_contained_by(active_gs).full_name} to attempt that.")
			return True
		return False

	def err_wrt_class(self, creature, active_gs):
		if self.is_writing():
			active_gs.io.buffer(f"That's laudably creative but, truth be told, the only thing you can generally do with the {self.full_name} is to read it.")
			return True
		return False

	def err_not_vis(self, creature, active_gs):
		room = active_gs.map.get_obj_room(creature, active_gs)
		if not self.is_writing() and room.chk_is_vis(self, active_gs) == False:
			active_gs.io.buffer("You can't see a " + self.full_name + " here.")
			return True
		return False

	def err_not_in_reach(self, creature, active_gs):
		if not self.is_writing() and creature.is_contained(active_gs) and not creature.chk_obj_in_reach(self, active_gs):
			active_gs.io.buffer(f"You'll have to exit the {creature.get_contained_by(active_gs).full_name} to attempt that.")
			return True
		return False

	def err_not_in_hand(self, creature, active_gs):
		if not creature.chk_in_hand(self):
			active_gs.io.buffer("You're not holding the " + self.full_name + " in your hand.")
			return True
		return False

	def err_xst(self, creature, active_gs):
		if self.err_invis_obj(creature, active_gs):
			return True
		if self.err_not_vis(creature, active_gs):
			return True
		if self.err_wrt_not_vis(creature, active_gs):
			return True
		if self.err_wrt_class(creature, active_gs):
			return True
		return False

	def err_rch(self, creature, active_gs):
		if self.err_not_in_reach(creature, active_gs):
			return True
		if self.err_wrt_not_in_reach(creature, active_gs):
			return True
		return False

	def err_std(self, creature, active_gs):
		if self.err_xst(creature, active_gs):
			return True
		if self.err_rch(creature, active_gs):
			return True
		return False

	def err_prep_std(self, obj, creature, active_gs):
		if obj.err_xst(creature, active_gs) or self.err_xst(creature, active_gs):
			return True
		if obj.err_rch(creature, active_gs) or self.err_rch(creature, active_gs):
			return True
		return False

	# *** verb error methods ***

	# *** two_word errors ***
	def read_err(self, active_gs):
		creature = active_gs.hero
		if self.err_wrt_not_vis(creature, active_gs):
			return True
		if self.err_wrt_not_in_reach(creature, active_gs):
			return True
		if self.err_not_vis(creature, active_gs):
			return True
		if self.err_not_in_reach(creature, active_gs):
			return True
		if not self.is_writing():
			active_gs.io.buffer(f"You can't read the {self.full_name}. Try using 'examine' instead.")
			return True
		return False

	def examine_err(self, active_gs):
		creature = active_gs.hero
		if self.err_not_vis(creature, active_gs):
			return True
		if self.err_wrt_not_vis(creature, active_gs):
			return True
		if self.is_writing():
			active_gs.io.buffer(f"You can't examine the {self.full_name}. Try using 'read' instead.")
			return True
		if self.err_not_in_reach(creature, active_gs):
			return True
		if self.err_wrt_not_in_reach(creature, active_gs):
			return True
		if not self.is_viewonly():
			active_gs.io.buffer(f"Your mind grapples with the ineffable... it is almost in your grasp when suddenly, unbidden, your favorite 'You Mama' joke from the pub tramples like a raging rhino across the delicate neural fibers that comprise your working memory. The vision is lost - the {self.full_name} is simply beyond your ken.")
			return True
		return False

	def take_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self.is_liquid():
			active_gs.io.buffer("You can't 'take' a liquid but you can 'drink' a liquid or you can 'take' a container that holds a liquid.")
			return True
		if not self.is_item():
			active_gs.io.buffer(f"Just how do you intend to pick up a {self.full_name}?")
			return True
		if creature.chk_in_hand(self):
			active_gs.io.buffer("You're already holding the " + self.full_name)
			return True
		for obj in active_gs.get_room().floor_lst:
			if obj.is_creature() and obj is not active_gs.hero and self in obj.get_vis_contain_lst(active_gs):
				active_gs.io.buffer(f"Burt, you can't take the {self.full_name}. It belongs to the {obj.full_name}!")
				return True
#		if creature.max_weight - creature.weight() - self.weight < 0:
		if  not creature.chk_contain_item(self) and (creature.weight + self.weight) > creature.max_weight:
			active_gs.io.buffer(f"You don't have enough capacity to take the {self.full_name} along with everything else you are carrying.")
			return True
		return False

	def drop_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self == creature.feature_lst[0]:
			active_gs.io.buffer(f"Burt, you can't drop your {creature.feature_lst[0].full_name} - you're quite attached to it.")
			return True
		if not self.is_item():
			active_gs.io.buffer(f"You can't even pick up the {self.full_name}... how could you possibly drop it??")
			return True
		if self.err_not_in_hand(creature, active_gs):
			return True
		if creature.is_contained(active_gs) and not creature.get_contained_by(active_gs).chk_has_capacity():
			active_gs.io.buffer(f"There's no room on the {creature.get_contained_by(active_gs).full_name} for another item.")
			return True
		return False

	def open_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_openable() and not self.is_container():
			active_gs.io.buffer(f"The {self.full_name} cannot be openned.")
			return True
		if not self.is_openable() and self.is_container():
			active_gs.io.buffer(f"The {self.full_name} has no closure. It is always open.")
			return True
		if self.is_open:
			active_gs.io.buffer(f"The {self.full_name} is already open.")
			return True
		if self.is_lockable() and self.is_unlocked == False:
			active_gs.io.buffer(f"The {self.full_name} is locked.")
			return True
		return False
	
	def close_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_openable() and not self.is_container():
			active_gs.io.buffer(f"The {self.full_name} cannot be closed.")
			return True
		if not self.is_openable() and self.is_container():
			active_gs.io.buffer(f"The {self.full_name} has no closure. It is always open.")
			return True
		if self.is_open == False:
			active_gs.io.buffer(f"The {self.full_name} is already closed.")
			return True
		if self.is_lockable() and self.is_unlocked == False:
			active_gs.io.buffer(f"The {self.full_name} is locked open.") # for Iron Portcullis
			return True
		return False

	def eat_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_food():
			active_gs.io.buffer(f"What kind of desperate individual tries to eat a {self.full_name}? Burt, if you keep this up you're going to give Adventurers a bad name!")
			return True
		if self.err_not_in_hand(creature, active_gs):
			return True
		return False

	def wear_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_garment():
			active_gs.io.buffer(f"With a keen eye for high fashion, you boldly attempt to accoutre yourself in the {self.full_name}... it doesn't really work out... but nothing is harmed... except maybe your ego...")
			return True
		if self in creature.worn_lst:
			active_gs.io.buffer(f"You're already wearing the {self.full_name}!")
			return True
		if self.err_not_in_hand(creature, active_gs):
			return True
		if creature.chk_type_worn(self):
			active_gs.io.buffer(f"You are already wearing a {self.garment_type}. You can't wear two garments of the same type at the same time.")
			return True
		return False

	def push_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_buttonswitch():
			active_gs.io.buffer(f"Pushing on the {self.full_name} has no effect.")
			return True
		return False

	def pull_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_springsliderswitch() and not self.is_leverswitch():
			active_gs.io.buffer(f"Pulling on the {self.full_name} has no effect.")
			return True
		return False

	def stand_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_creature():
			active_gs.io.buffer(f"And yet the {self.full_name} continues to just sit there...")
			return True
		if self != creature:
			active_gs.io.buffer(f"In your most bracing voice you declare: 'If you stand for nothing, what'll you fall for?' - but the {self.full_name} appears to be immune to your exhortations.")
			return True
		room = active_gs.get_room()
		if self in room.floor_lst:
			active_gs.io.buffer(f"You're already standing in the {room.full_name}!")
			return True
		return False

	def enter_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self.is_item():
			active_gs.io.buffer(f"Despite twisting yourself into a pretzel you still can't manage to enter the {self.full_name}.")
			return True
		if not self.is_seat():
			active_gs.io.buffer(f"You can't use the 'enter' command on the {self.full_name}.")
			return True
		if self.is_seat() and len(self.contain_lst) >= self.max_obj:
			active_gs.io.buffer(f"There's no room on the {self.full_name} to sit.")
			return True
		return False

	def exit_err(self, active_gs):
		creature = active_gs.hero
		if self.err_not_vis(creature, active_gs):
			return True
		if self.err_wrt_not_vis(creature, active_gs):
			return True
		if self.err_wrt_class(creature, active_gs):
			return True
		if self.err_wrt_not_in_reach(creature, active_gs):
			return True
		if not self.is_seat() and self.err_not_in_reach(creature, active_gs):
			return True
		if self.is_item():
			active_gs.io.buffer(f"Despite twisting yourself into a pretzel you still can't manage to exit the {self.full_name}.")
			return True
		if not self.is_seat():
			active_gs.io.buffer(f"You can't use the 'exit' command on the {self.full_name}.")
			return True
		if not creature.is_contained(active_gs):
			active_gs.io.buffer(f"You can't exit the {self.full_name} - you're not presently in it!")
			return True
		if creature.is_contained(active_gs) and creature.get_contained_by(active_gs) != self:
			active_gs.io.buffer(f"You can't exit the {self.full_name} - you're not presently in it!")
			return True
		return False

	def get_weight_err(self, active_gs):
		if not active_gs.state_dict['debug']:
			active_gs.io.buffer("Please start your sentence with a known verb!")
			return True
		if not (self.is_item() or self.is_creature()):
			active_gs.io.buffer("Only Items and Creatures have weight.")
			return True
		return False

	def capacity_err(self, active_gs):
		if not active_gs.state_dict['debug']:
			active_gs.io.buffer("Please start your sentence with a known verb!")
			return True
		if not self.is_container():
			active_gs.io.buffer("Only Containers have capacity.")
			return True
		return False

	def where_is_err(self, active_gs):
		if not active_gs.state_dict['debug']:
			active_gs.io.buffer("Please start your sentence with a known verb!")
			return True
		if self.is_writing():
			active_gs.io.buffer(f"The where_is command does not work for objects of Writing class")
			return True
		return False

	# *** prep errors ***
	def drink_err(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_liquid():
			active_gs.io.buffer(f"Your attempts to quaff the {self.full_name} do not meet with success.")
			return True
		if obj.name in ['moat']:
			active_gs.io.buffer(f"The very thought of drinking from the fetid {obj.full_name} makes you gag.")
			return True
		if not obj.is_container():
			active_gs.io.buffer(f"How could you possibly drink {self.full_name} from a {obj.full_name}?")
			return True
		if creature.hand_is_empty() or creature.get_hand_item() != obj:
			active_gs.io.buffer(f"You need to be holding the {obj.full_name} to drink from it.")
			return True
		if self not in obj.contain_lst:
			active_gs.io.buffer(f"The {obj.full_name} doesn't contain {self.full_name}.")
			return True
		return False

	def lock_err(self, key_obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(key_obj, creature, active_gs):
			return True
		if self.is_container() and not self.is_openable():
			active_gs.io.buffer(f"There's nothing to lock. The {self.full_name} is always open.")
			return True
		if not self.is_lockable():
			active_gs.io.buffer(f"The {self.full_name} cannot be locked.")
			return True
		if key_obj.is_switch():
			active_gs.io.buffer(f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True
		if not key_obj.is_item():
			active_gs.io.buffer(f"And just how do you intend to lock a {self.full_name} with a {key_obj.full_name}??")
			return True
		if key_obj.err_not_in_hand(creature, active_gs):
			return True
		if key_obj != self.key and key_obj.root_name != 'key':
			active_gs.io.buffer(f"You can't lock the {self.full_name} with the {key_obj.full_name}.")
			return True
		if self.is_unlocked is None or (self.is_openable() and not self.is_lockable()):
			active_gs.io.buffer(f"The {self.full_name} does not appear to have a lock.")
			return True
		if self.key is None:
			active_gs.io.buffer(f"You don't see a keyhole in the {self.full_name}.")
			return True
		if self.is_open == True:
			active_gs.io.buffer("You can't lock or unlock something that's open.")
			return True
		if key_obj != self.key and key_obj.root_name == 'key':
			active_gs.io.buffer("You aren't holding the correct key.")
			return True
		if self.is_unlocked == False:
			active_gs.io.buffer(f"The {self.full_name} is already locked.")
			return True
		return False

	def unlock_err(self, key_obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(key_obj, creature, active_gs):
			return True
		if self.is_container() and not self.is_openable():
			active_gs.io.buffer(f"There's nothing to unlock. The {self.full_name} is always open.")
			return True
		if not self.is_lockable():
			active_gs.io.buffer(f"The {self.full_name} cannot be unlocked.")
			return True
		if key_obj.is_switch():
			active_gs.io.buffer(f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True
		if not key_obj.is_item():
			active_gs.io.buffer(f"And just how do you intend to unlock a {self.full_name} with a {key_obj.full_name}??")
			return True
		if key_obj.err_not_in_hand(creature, active_gs):
			return True
		if key_obj != self.key and key_obj.root_name != 'key':
			active_gs.io.buffer(f"You can't unlock the {self.full_name} with the {key_obj.full_name}.")
			return True
		if self.is_unlocked is None or (self.is_openable() and not self.is_lockable()):
			active_gs.io.buffer(f"The {self.full_name} does not appear to have a lock.")
			return True
		if self.key is None:
			active_gs.io.buffer(f"You don't see a keyhole in the {self.full_name}.")
			return True
		if self.is_open:
			active_gs.io.buffer("You can't lock or unlock something that's open.")
			return True
		if key_obj != self.key and key_obj.root_name == 'key':
			active_gs.io.buffer("You aren't holding the correct key.")
			return True
		if self.is_unlocked:
			active_gs.io.buffer(f"The {self.full_name} is already unlocked.")
			return True
		return False

	def put_err(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(obj, creature, active_gs):
			return True
		if not obj.is_item():
			active_gs.io.buffer(f"You can't even pick up the {obj.full_name}... how could you possibly put it somewhere?")
			return True
		if not self.is_container():
			active_gs.io.buffer(f"You can't put the {obj.full_name} in or on the {self.full_name}.")
			return True
		if self == obj:
			active_gs.io.buffer(f"With all your might you attempt to bend the laws of time, space, and topology to your will... and in response you hear the ancient background radiation of the big bang itself respond: 'Nope, not gonna happen Burt.'")
			return True
		if obj.err_not_in_hand(creature, active_gs):
			return True
		if self.is_openable() and self.is_open == False:
			active_gs.io.buffer(f"The {self.full_name} is closed.")
			return True
		if self.chk_content_prohibited(obj):
			active_gs.io.buffer(f"You can't put the {obj.full_name} {self.prep} the {self.full_name}.")
			return True
		if self.is_container() and not self.chk_has_capacity():
			active_gs.io.buffer(f"There's no room {self.prep} the {self.full_name} for another item.")
			return True
		if self.max_weight - self.get_contained_weight() - obj.weight < 0:
			active_gs.io.buffer(f"The {self.full_name} doesn't have enough capacity to hold the {obj.full_name}.")
			return True
		return False

	def show_err(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(obj, creature, active_gs):
			return True
		if not self.is_creature():
			active_gs.io.buffer(f"Exactly how would you expect the {self.full_name} to respond to the {obj.full_name}?")
			return True
		if obj.err_not_in_hand(creature, active_gs):
			return True
		return False

	def give_err(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(obj, creature, active_gs):
			return True
		if not obj.is_item():
			active_gs.io.buffer(f"You can't even pick up the {obj.full_name}... how could you possibly 'give' it?")
			return True
		if not self.is_creature():
			active_gs.io.buffer(f"And what do you expect the {self.full_name} to do with the {obj.full_name}?")
			return True
		if obj.err_not_in_hand(creature, active_gs):
			return True
		if self == creature:
			active_gs.io.buffer(f"With great formality and many words of thanks, you hand the {obj.full_name} to yourself.")
			return True
		if self.weight + obj.weight > self.max_weight:
			active_gs.io.buffer(f"With a glum shake of their head, the {self.full_name} refuses the {obj.full_name}. You notice that the {self.full_name} appears to be overburdened already.")
			return True
		return False

	def attack_err(self, src_obj, active_gs):
		src_creature = active_gs.hero
		tgt_creature = self
		if self.err_prep_std(src_obj, src_creature, active_gs):
			return True
		if not self.is_creature():
			active_gs.io.buffer(f"What kind of deranged person attacks a {self.full_name} with a {src_obj.full_name}?!?")
			return True
		if not tgt_creature.is_attackable: # consider re-homing 'not_attackable' txt to creature obj
			try:
				active_gs.io.buff_a(f"not_attackable_{src_creature.name}_{tgt_creature.name}")
			except:
				active_gs.io.buffer("You consider attacking but then think better of it. There must be another path to victory.")
			return True
		if (not src_obj in src_creature.feature_lst) and (not src_creature.chk_in_hand(src_obj)):
			active_gs.io.buffer(f"You are not holding the {src_obj.full_name} in your hand.")
			return True
		if (src_obj in src_creature.feature_lst) and (not src_creature.hand_is_empty()):
			active_gs.io.buffer(f"You can't attack with your {src_obj.full_name} while you're holding the {src_creature.get_hand_item().full_name}.")
			return True
		if src_creature == tgt_creature:
			active_gs.io.buffer("You can't attack yourself!")
			return True
		return False


	# *** go_case error ***
	def go_err(self, dir, active_gs):
		creature = active_gs.hero
		if dir not in ['north', 'south', 'east', 'west']:
			active_gs.io.buffer(f"'{dir}' is not a valid direction that you can go in.")
			return True
		if creature.is_contained(active_gs):
			active_gs.io.buffer(f"You'll have to exit the {creature.get_contained_by(active_gs).full_name} to attempt that.")
			return True
		if not active_gs.map.chk_valid_dir(self, dir):
			active_gs.io.buff_e(f"dir_err_{random.randint(0, 4)}")
			return True
		door = active_gs.map.get_door(self, dir)
		if not isinstance(door, str) and door.is_open == False:
			active_gs.io.buffer(f"The {door.full_name} is closed.")
			return True
		return False


	# *** obj representation def ***
	def __repr__(self):
		return f"Object {self.name} is of class {type(self).__name__}"
