# program: dark castle
# author: Tom Snellgrove
# module description: Invisible class deffinition module

### import
import random


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
	def get_contain_lst(self, gs):
		return []

	def get_vis_contain_lst(self, gs):
		return []

	def chk_contain_item(self, item):
		return False

	def remove_item(self, item, gs):
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

	def is_warning(self):
		return False

	def has_trigger(self):
		return False

	def has_cond(self):
		return False

	def has_switch(self):
		return False

	def is_garment(self):
		return False

	def is_seat(self):
		return False
	
	def is_receptacle(self):
		return False
	
	def has_writing(self):
		return False

	# *** debug methods ###
	def where_is(self, gs, mode=None):
		""" Reports the location of an obj. Only usable in debug mode.
		"""
		if mode is None:
			mode = 'std'
		creature = gs.core.hero
		
		if not gs.map.chk_obj_exist(self, gs):
			gs.io.buffer(f"The {self.full_name} does not currently exist in the game.")
			return
		room = gs.map.get_obj_room(creature, gs)
		if room.chk_is_vis(self, gs):
			gs.io.buffer(f"The {self.full_name} is visible in the {room.full_name}, where you are presently.")
		elif gs.map.get_obj_room(self, gs) == room:
			gs.io.buffer(f"The {self.full_name} is not visible to you but is in the {room.full_name}, where you are presently.")
		else:
			gs.io.buffer(f"The {self.full_name} is in the {gs.map.get_obj_room(self, gs).full_name}.")
		in_inv, inv_creature = gs.map.chk_obj_in_creature_inv(self, gs)
		if in_inv:
			gs.io.buffer(f"The {self.full_name} is in the inventory of the {inv_creature.full_name}.")
		return


	# *** standard errors ###	
	def err_invis_obj(self, creature, gs):
		if self.is_invisible():
			gs.io.buffer(f"During a brief moment of clarity, you see that the world around you is nothing but lines of code... vertical trails of glowing green characters tumble down across your vision... realizing that you are The One, you reach for the {self.full_name}... but just as your fingers approach it, the vision evaporates and your insight into Simulation Theory of Life fades from your mind and is forgotten forever...")
			return True
		return False

	def err_wrt_not_vis(self, creature, gs):
		room = gs.map.get_obj_room(creature, gs)
		if self.is_writing() and not room.chk_wrt_is_vis(self, gs):
			gs.io.buffer(f"You can't see {self.full_name} written on anything here.")
			return True
		return False

	def err_wrt_not_in_reach(self, creature, gs):
		if self.is_writing() and creature.is_contained(gs) and not creature.chk_wrt_in_reach(self, gs):
			gs.io.buffer(f"You'll have to exit the {creature.get_contained_by(gs).full_name} to attempt that.")
			return True
		return False

	def err_wrt_class(self, creature, gs):
		if self.is_writing():
			gs.io.buffer(f"That's laudably creative but, truth be told, the only thing you can generally do with the {self.full_name} is to read it.")
			return True
		return False

	def err_not_vis(self, creature, gs):
		room = gs.map.get_obj_room(creature, gs)
		if not self.is_writing() and room.chk_is_vis(self, gs) == False:
			gs.io.buffer("You can't see a " + self.full_name + " here.")
			return True
		return False

	def err_not_in_reach(self, creature, gs):
		if not self.is_writing() and creature.is_contained(gs) and not creature.chk_obj_in_reach(self, gs):
			gs.io.buffer(f"You'll have to exit the {creature.get_contained_by(gs).full_name} to attempt that.")
			return True
		return False

	def err_not_in_hand(self, creature, gs):
		if not creature.chk_in_hand(self):
			gs.io.buffer("You're not holding the " + self.full_name + " in your hand.")
			return True
		return False

	def err_xst(self, creature, gs):
		if self.err_invis_obj(creature, gs):
			return True
		if self.err_not_vis(creature, gs):
			return True
		if self.err_wrt_not_vis(creature, gs):
			return True
		if self.err_wrt_class(creature, gs):
			return True
		return False

	def err_rch(self, creature, gs):
		if self.err_not_in_reach(creature, gs):
			return True
		if self.err_wrt_not_in_reach(creature, gs):
			return True
		return False

	def err_std(self, creature, gs):
		if self.err_xst(creature, gs):
			return True
		if self.err_rch(creature, gs):
			return True
		return False

	def err_prep_std(self, obj, creature, gs):
		if obj.err_xst(creature, gs) or self.err_xst(creature, gs):
			return True
		if obj.err_rch(creature, gs) or self.err_rch(creature, gs):
			return True
		return False

	# *** verb error methods ***

	# *** two_word errors ***
	def read_err(self, gs):
		creature = gs.core.hero
		if self.err_wrt_not_vis(creature, gs):
			return True
		if self.err_wrt_not_in_reach(creature, gs):
			return True
		if self.err_not_vis(creature, gs):
			return True
		if self.err_not_in_reach(creature, gs):
			return True
		if not self.is_writing() and not self.has_writing():
			gs.io.buffer(f"The {self.full_name} has nothing written on it.")
			return True
		return False

	def examine_err(self, gs):
		creature = gs.core.hero
		if self.err_not_vis(creature, gs):
			return True
		if self.err_wrt_not_vis(creature, gs):
			return True
		if self.err_not_in_reach(creature, gs):
			return True
		if self.err_wrt_not_in_reach(creature, gs):
			return True
		if not self.is_writing() and not self.is_viewonly():
			gs.io.buffer(f"Your mind grapples with the ineffable... it is almost in your grasp when suddenly, unbidden, your favorite 'You Mama' joke from the pub tramples like a raging rhino across the delicate neural fibers that comprise your working memory. The vision is lost - the {self.full_name} is simply beyond your ken.")
			return True
		return False

	def take_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if self.is_liquid():
			gs.io.buffer("You can't 'take' a liquid but you can 'drink' a liquid or you can 'take' a container that holds a liquid.")
			return True
		if not self.is_item():
			gs.io.buffer(f"Just how do you intend to pick up a {self.full_name}?")
			return True
		if creature.chk_in_hand(self):
			gs.io.buffer("You're already holding the " + self.full_name)
			return True
		for obj in gs.map.hero_rm.floor_lst:
			if obj.is_creature() and obj is not gs.core.hero and self in obj.get_vis_contain_lst(gs):
				gs.io.buffer(f"You can't take the {self.full_name}. It belongs to the {obj.full_name}!")
				return True
		if  not creature.chk_contain_item(self) and (creature.weight + self.weight) > creature.max_weight:
			gs.io.buffer(f"You don't have enough capacity to take the {self.full_name} along with everything else you are carrying.")
			return True
		return False

	def drop_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if self == creature.feature_lst[0]:
			gs.io.buffer(f"You can't drop your {creature.feature_lst[0].full_name} - you're quite attached to it.")
			return True
		if not self.is_item():
			gs.io.buffer(f"You can't even pick up the {self.full_name}... how could you possibly drop it??")
			return True
		if self.err_not_in_hand(creature, gs):
			return True
		if creature.is_contained(gs) and not creature.get_contained_by(gs).chk_has_capacity():
			gs.io.buffer(f"There's no room on the {creature.get_contained_by(gs).full_name} for another item.")
			return True
		return False

	def stowe_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if creature.hand_is_empty():
			gs.io.buffer(f"{creature.full_name}, your hand is empty!")
			return True
		if self == creature.feature_lst[0]:
			gs.io.buffer(f"{creature.full_name}, you can't stowe your {creature.feature_lst[0].full_name} - you're quite attached to it.")
			return True
		if not self.is_item():
			gs.io.buffer(f"You can't even pick up the {self.full_name}... how could you possibly put it in your backpack??")
			return True
		if self.err_not_in_hand(creature, gs):
			return True		
		return False


	def open_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_openable() and not self.is_container():
			gs.io.buffer(f"The {self.full_name} cannot be openned.")
			return True
		if not self.is_openable() and self.is_container():
			gs.io.buffer(f"The {self.full_name} has no closure. It is always open.")
			return True
		if self.is_open:
			gs.io.buffer(f"The {self.full_name} is already open.")
			return True
		if self.is_lockable() and self.is_unlocked == False:
			gs.io.buffer(f"The {self.full_name} is locked.")
			return True
		return False
	
	def close_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_openable() and not self.is_container():
			gs.io.buffer(f"The {self.full_name} cannot be closed.")
			return True
		if not self.is_openable() and self.is_container():
			gs.io.buffer(f"The {self.full_name} has no closure. It is always open.")
			return True
		if self.is_open == False:
			gs.io.buffer(f"The {self.full_name} is already closed.")
			return True
		if self.is_lockable() and self.is_unlocked == False:
			gs.io.buffer(f"The {self.full_name} is locked open.") # for Iron Portcullis
			return True
		return False

	def eat_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_food():
			gs.io.buffer(f"What kind of desperate individual tries to eat a {self.full_name}? If you keep this up you're going to give Adventurers a bad name!")
			return True
		if self.err_not_in_hand(creature, gs):
			return True
		return False

	def wear_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_garment():
			gs.io.buffer(f"With a keen eye for high fashion, you boldly attempt to accoutre yourself in the {self.full_name}... it doesn't really work out... but nothing is harmed... except maybe your ego...")
			return True
		if self in creature.worn_lst:
			gs.io.buffer(f"You're already wearing the {self.full_name}!")
			return True
		if self.err_not_in_hand(creature, gs):
			return True
		if creature.chk_type_worn(self):
			gs.io.buffer(f"You are already wearing a {self.garment_type}. You can't wear two garments of the same type at the same time.")
			return True
		return False

	def push_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_buttonswitch():
			gs.io.buffer(f"Pushing on the {self.full_name} has no effect.")
			return True
		return False

	def pull_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_springsliderswitch() and not self.is_leverswitch():
			gs.io.buffer(f"Pulling on the {self.full_name} has no effect.")
			return True
		return False

	def stand_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_creature():
			gs.io.buffer(f"And yet the {self.full_name} continues to just sit there...")
			return True
		if self != creature:
			gs.io.buffer(f"In your most bracing voice you declare: 'If you stand for nothing, what'll you fall for?' - but the {self.full_name} appears to be immune to your exhortations.")
			return True
		if self in gs.map.hero_rm.floor_lst:
			gs.io.buffer(f"You're already standing in the {gs.map.hero_rm.full_name}!")
			return True
		return False

	def enter_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if self.is_item():
			gs.io.buffer(f"Despite twisting yourself into a pretzel you still can't manage to enter the {self.full_name}.")
			return True
		if not self.is_seat():
			gs.io.buffer(f"You can't use the 'enter' command on the {self.full_name}.")
			return True
		if self.is_seat() and len(self.contain_lst) >= self.max_obj:
			gs.io.buffer(f"There's no room on the {self.full_name} to sit.")
			return True
		return False

	def exit_err(self, gs):
		creature = gs.core.hero
		if self.err_not_vis(creature, gs):
			return True
		if self.err_wrt_not_vis(creature, gs):
			return True
		if self.err_wrt_class(creature, gs):
			return True
		if self.err_wrt_not_in_reach(creature, gs):
			return True
		if not self.is_seat() and self.err_not_in_reach(creature, gs):
			return True
		if self.is_item():
			gs.io.buffer(f"Despite twisting yourself into a pretzel you still can't manage to exit the {self.full_name}.")
			return True
		if not self.is_seat():
			gs.io.buffer(f"You can't use the 'exit' command on the {self.full_name}.")
			return True
		if not creature.is_contained(gs):
			gs.io.buffer(f"You can't exit the {self.full_name} - you're not presently in it!")
			return True
		if creature.is_contained(gs) and creature.get_contained_by(gs) != self:
			gs.io.buffer(f"You can't exit the {self.full_name} - you're not presently in it!")
			return True
		return False

	def get_weight_err(self, gs):
		if not gs.core.is_debug:
			gs.io.buffer("Please start your sentence with a known verb!")
			return True
		if not (self.is_item() or self.is_creature()):
			gs.io.buffer("Only Items and Creatures have weight.")
			return True
		return False

	def capacity_err(self, gs):
		if not gs.core.is_debug:
			gs.io.buffer("Please start your sentence with a known verb!")
			return True
		if not self.is_container() and not self.is_creature():
			gs.io.buffer("Only Containers and Creatures have capacity.")
			return True
		return False

	def where_is_err(self, gs):
		if not gs.core.is_debug:
			gs.io.buffer("Please start your sentence with a known verb!")
			return True
		if self.is_writing():
			gs.io.buffer(f"The where_is command does not work for objects of Writing class")
			return True
		return False

	# *** prep errors ***
	def drink_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True
		if not self.is_liquid():
			gs.io.buffer(f"Your attempts to quaff the {self.full_name} do not meet with success.")
			return True
		if obj.name in ['moat']:
			gs.io.buffer(f"The very thought of drinking from the fetid {obj.full_name} makes you gag.")
			return True
		if not obj.is_container():
			gs.io.buffer(f"How could you possibly drink {self.full_name} from a {obj.full_name}?")
			return True
		if creature.hand_is_empty() or creature.get_hand_item() != obj:
			gs.io.buffer(f"You need to be holding the {obj.full_name} to drink from it.")
			return True
		if self not in obj.contain_lst:
			gs.io.buffer(f"The {obj.full_name} doesn't contain {self.full_name}.")
			return True
		return False

	def lock_err(self, key_obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(key_obj, creature, gs):
			return True
		if self.is_container() and not self.is_openable():
			gs.io.buffer(f"There's nothing to lock. The {self.full_name} is always open.")
			return True
		if not self.is_lockable():
			gs.io.buffer(f"The {self.full_name} cannot be locked.")
			return True
		if key_obj.is_switch():
			gs.io.buffer(f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True
		if not key_obj.is_item():
			gs.io.buffer(f"And just how do you intend to lock a {self.full_name} with a {key_obj.full_name}??")
			return True
		if key_obj.err_not_in_hand(creature, gs):
			return True
		if key_obj != self.key and key_obj.root_name != 'key':
			gs.io.buffer(f"You can't lock the {self.full_name} with the {key_obj.full_name}.")
			return True
		if self.is_unlocked is None or (self.is_openable() and not self.is_lockable()):
			gs.io.buffer(f"The {self.full_name} does not appear to have a lock.")
			return True
		if self.key is None:
			gs.io.buffer(f"You don't see a keyhole in the {self.full_name}.")
			return True
		if self.is_open == True:
			gs.io.buffer("You can't lock or unlock something that's open.")
			return True
		if key_obj != self.key and key_obj.root_name == 'key':
			gs.io.buffer("You aren't holding the correct key.")
			return True
		if self.is_unlocked == False:
			gs.io.buffer(f"The {self.full_name} is already locked.")
			return True
		return False

	def unlock_err(self, key_obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(key_obj, creature, gs):
			return True
		if self.is_container() and not self.is_openable():
			gs.io.buffer(f"There's nothing to unlock. The {self.full_name} is always open.")
			return True
		if not self.is_lockable():
			gs.io.buffer(f"The {self.full_name} cannot be unlocked.")
			return True
		if key_obj.is_switch():
			gs.io.buffer(f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True
		if not key_obj.is_item():
			gs.io.buffer(f"And just how do you intend to unlock a {self.full_name} with a {key_obj.full_name}??")
			return True
		if key_obj.err_not_in_hand(creature, gs):
			return True
		if key_obj != self.key and key_obj.root_name != 'key':
			gs.io.buffer(f"You can't unlock the {self.full_name} with the {key_obj.full_name}.")
			return True
		if self.is_unlocked is None or (self.is_openable() and not self.is_lockable()):
			gs.io.buffer(f"The {self.full_name} does not appear to have a lock.")
			return True
		if self.key is None:
			gs.io.buffer(f"You don't see a keyhole in the {self.full_name}.")
			return True
		if self.is_open:
			gs.io.buffer("You can't lock or unlock something that's open.")
			return True
		if key_obj != self.key and key_obj.root_name == 'key':
			gs.io.buffer("You aren't holding the correct key.")
			return True
		if self.is_unlocked:
			gs.io.buffer(f"The {self.full_name} is already unlocked.")
			return True
		return False

	def put_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(obj, creature, gs):
			return True
		if not obj.is_item():
			gs.io.buffer(f"You can't even pick up the {obj.full_name}... how could you possibly put it somewhere?")
			return True
		if not self.is_container():
			gs.io.buffer(f"You can't put the {obj.full_name} in or on the {self.full_name}.")
			return True
		if self == obj:
			gs.io.buffer(f"With all your might you attempt to bend the laws of time, space, and topology to your will... and in response you hear the ancient background radiation of the big bang itself respond: 'Nope, not gonna happen.'")
			return True
		if obj.err_not_in_hand(creature, gs):
			return True
		if self.is_openable() and self.is_open == False:
			gs.io.buffer(f"The {self.full_name} is closed.")
			return True
		if self.chk_content_prohibited(obj):
			gs.io.buffer(f"You can't put the {obj.full_name} {self.prep} the {self.full_name}.")
			return True
		if self.is_container() and not self.chk_has_capacity():
			gs.io.buffer(f"There's no room {self.prep} the {self.full_name} for another item.")
			return True
		if self.max_weight - self.get_contained_weight() - obj.weight < 0:
			gs.io.buffer(f"The {self.full_name} doesn't have enough capacity to hold the {obj.full_name}.")
			return True
		return False

	def show_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(obj, creature, gs):
			return True
		if not self.is_creature():
			gs.io.buffer(f"Exactly how would you expect the {self.full_name} to respond to the {obj.full_name}?")
			return True
		if obj.err_not_in_hand(creature, gs):
			return True
		return False

	def give_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(obj, creature, gs):
			return True
		if not obj.is_item():
			gs.io.buffer(f"You can't even pick up the {obj.full_name}... how could you possibly 'give' it?")
			return True
		if not self.is_creature():
			gs.io.buffer(f"And what do you expect the {self.full_name} to do with the {obj.full_name}?")
			return True
		if obj.err_not_in_hand(creature, gs):
			return True
		if self == creature:
			gs.io.buffer(f"With great formality and many words of thanks, you hand the {obj.full_name} to yourself.")
			return True
		if self.weight + obj.weight > self.max_weight:
			gs.io.buffer(f"With a glum shake of their head, the {self.full_name} refuses the {obj.full_name}. You notice that the {self.full_name} appears to be overburdened already.")
			return True
		return False

	def attack_err(self, src_obj, gs):
		src_creature = gs.core.hero
		tgt_creature = self
		if self.err_prep_std(src_obj, src_creature, gs):
			return True
		if not self.is_creature():
			gs.io.buffer(f"What kind of deranged person attacks a {self.full_name} with a {src_obj.full_name}?!?")
			return True
		if not tgt_creature.is_attackable: # consider re-homing 'not_attackable' txt to creature obj
			try:
				gs.io.buff_f(f"not_attackable_{src_creature.name}_{tgt_creature.name}")
			except:
				gs.io.buffer("You consider attacking but then think better of it. There must be another path to victory.")
			return True
		if (not src_obj in src_creature.feature_lst) and (not src_creature.chk_in_hand(src_obj)):
			gs.io.buffer(f"You are not holding the {src_obj.full_name} in your hand.")
			return True
		if (src_obj in src_creature.feature_lst) and (not src_creature.hand_is_empty()):
			gs.io.buffer(f"You can't attack with your {src_obj.full_name} while you're holding the {src_creature.get_hand_item().full_name}.")
			return True
		if src_creature == tgt_creature:
			gs.io.buffer("You can't attack yourself!")
			return True
		return False


	# *** go_case error ***
	def go_err(self, dir, gs):
		creature = gs.core.hero
		if dir not in ['north', 'south', 'east', 'west']:
			gs.io.buffer(f"'{dir}' is not a valid direction that you can go in.")
			return True
		if creature.is_contained(gs):
			gs.io.buffer(f"You'll have to exit the {creature.get_contained_by(gs).full_name} to attempt that.")
			return True
		if not gs.map.chk_valid_dir(self, dir):
			gs.io.buff_e(f"dir_err_{random.randint(0, 4)}")
			return True
		door = gs.map.get_door(self, dir)
		if not isinstance(door, str) and door.is_open == False:
			gs.io.buffer(f"The {door.full_name} is closed.")
			return True
		return False


	# *** obj representation def ***
	def __repr__(self):
		return f"Object {self.name} is of class {type(self).__name__}"
