# program: dark castle
# author: Tom Snellgrove
# module description: Error class deffinition module

### import
import random
from cleesh.class_std.identity_class_def import Identity


### classes ###
class Error(Identity):
	def __init__(self, name):
		super().__init__(name)
		""" Error class inherits from Identity. All tangible classes inherit their 
		error sub-system from Error. 
		"""
		
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
			return True, False, ""
		if self.err_wrt_not_in_reach(creature, gs):
			return True, False, ""
		if self.err_not_vis(creature, gs):
			return True, False, ""
		if self.err_not_in_reach(creature, gs):
			return True, False, ""
		if not self.is_writing() and not self.has_writing():
			err_txt = (f"The {self.full_name} has nothing written on it.")
			return True, False, err_txt
		return False, False, ""

	def examine_err(self, gs):
		creature = gs.core.hero
		if self.err_not_vis(creature, gs):
			return True, False, ""
		if self.err_wrt_not_vis(creature, gs):
			return True, False, ""
		if self.err_not_in_reach(creature, gs):
			return True, False, ""
		if self.err_wrt_not_in_reach(creature, gs):
			return True, False, ""
		if not self.is_writing() and not self.is_viewonly():
			err_txt = (f"Your mind grapples with the ineffable... it is almost in your grasp when suddenly, unbidden, your favorite 'You Mama' joke from the pub tramples like a raging rhino across the delicate neural fibers that comprise your working memory. The vision is lost - the {self.full_name} is simply beyond your ken.")
			return True, False, err_txt
		return False, False, ""

	def take_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self.is_liquid():
			err_txt = ("You can't 'take' a liquid but you can 'drink' a liquid or you can 'take' a container that holds a liquid.")
			return True, False, err_txt
		if creature.chk_in_hand(self):
			err_txt = ("You're already holding the " + self.full_name)
			return True, False, err_txt
		if not self.is_item():
			# attemptable error: a non-item might look takeable - is reasonable to attempt - player gets info
			err_txt = (f"Just how do you intend to pick up a {self.full_name}?")
			return True, True, err_txt
		if not creature.chk_item_in_inv(self, gs) and (creature.weight + self.weight) > creature.max_weight:
			# attemptable error: player only learns obj is too heavy by trying to lift it
			err_txt = (f"You don't have enough capacity to take the {self.full_name} along with everything else you are carrying.")
			return True, True, err_txt
		for obj in gs.map.hero_rm.floor_lst:
			if obj.is_creature() and obj is not gs.core.hero and self in obj.get_vis_contain_lst(gs):
				# attemptable error: player can try to take another creature's possessions
				err_txt = (f"You can't take the {self.full_name}. It belongs to the {obj.full_name}!")
				return True, True, err_txt
		return False, False, ""

	def drop_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self == creature.feature_lst[0]:
			err_txt = (f"You can't drop your {creature.feature_lst[0].full_name} - you're quite attached to it.")
			return True, False, err_txt
		if self not in creature.hand_lst and self not in creature.bkpk_lst: # enable drop from pack
			err_txt = (f"You don't possess the {self.full_name}.")
			return True, False, err_txt
		if creature.is_contained(gs) and not creature.get_contained_by(gs).chk_has_capacity():
			err_txt = (f"There's no room on the {creature.get_contained_by(gs).full_name} for another item.")
			return True, False, err_txt
		return False, False, ""

	def stowe_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self == creature.feature_lst[0]:
			err_txt = (f"{creature.full_name}, you can't stowe your {creature.feature_lst[0].full_name} - you're quite attached to it.")
			return True, False, err_txt
		if self in creature.bkpk_lst:
			err_txt = (f"The {self.full_name} is already in your backpack!")
			return True, False, err_txt
		if self.err_not_in_hand(creature, gs):
			return True, False, ""
		return False, False, ""

	def eat_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self not in creature.hand_lst and self not in creature.bkpk_lst:
			err_txt = (f"You don't possess the {self.full_name}.")
			return True, False, err_txt

		if not self.is_food():
			# attemptable error: something might look edible - is reasonable to attempt - player gets info
			err_txt =(f"What kind of desperate individual tries to eat a {self.full_name}? If you keep this up you're going to give Adventurers a bad name!")
			return True, True, err_txt
		return False, False, ""

	def wear_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self in creature.worn_lst:
			err_txt = (f"You're already wearing the {self.full_name}!")
			return True, False, err_txt
		if self not in creature.hand_lst and self not in creature.bkpk_lst:
			err_txt = (f"You don't possess the {self.full_name}.")
			return True, False, err_txt
		if creature.chk_type_worn(self):
			err_txt = (f"You are already wearing a {self.garment_type}. You can't wear two garments of the same type at the same time.")
			return True, False, err_txt
		if not self.is_garment():
			# attemptable error: palyer can attempt to wear a non-wearable obj
			err_txt = (f"With a keen eye for high fashion, you boldly attempt to accoutre yourself in the {self.full_name}... it doesn't really work out... but nothing is harmed... except maybe your ego...")
			return True, True, err_txt
		return False, False, ""

	def open_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if not self.is_openable() and self.is_container():
			err_txt = (f"The {self.full_name} has no closure. It is always open.")
			return True, False, err_txt
		if not self.is_openable() and not self.is_container():
			# attemptable error: many possible cases; e.g. "open castle"
			err_txt = (f"The {self.full_name} cannot be openned.")
			return True, True, err_txt
		if self.is_open:
			err_txt = (f"The {self.full_name} is already open.")
			return True, False, err_txt
		if self.is_lockable() and self.is_unlocked == False:
			# attemptable error: player can typically only learn that a door is locked by trying to open it
			err_txt = (f"The {self.full_name} is locked.")
			return True, True, err_txt
		return False, False, ""

	def close_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if not self.is_openable() and self.is_container():
			err_txt = (f"The {self.full_name} has no closure. It is always open.")
			return True, False, err_txt
		if not self.is_openable() and not self.is_container():
			# attemptable error: a non-closable item might look closable; player gets info
			err_txt = (f"The {self.full_name} cannot be closed.")
			return True, True, err_txt
		if self.is_open == False:
			# NOT attemptable: it should be visually evident that the door is already closed
			err_txt = (f"The {self.full_name} is already closed.")
			return True, False, err_txt
		if self.is_lockable() and self.is_unlocked == False:
			# attemptable error: door likely appears closeable; player learns that it is not in attempt
			err_txt = (f"The {self.full_name} is locked open.") # for Iron Portcullis
			return True, True, err_txt
		return False, False, ""

	def push_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if not self.is_buttonswitch():
			# attempatable error: many non-pushable obj could, in theory, be pushed
			err_txt = (f"Pushing on the {self.full_name} has no effect.")
			return True, True, err_txt
		return False, False, ""

	def pull_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if not self.is_springsliderswitch() and not self.is_leverswitch():
			# attemptable error: many non-pullable obj likely appear pullable
			err_txt = (f"Pulling on the {self.full_name} has no effect.")
			return True, True, err_txt
		return False, False, ""

	def stand_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self in gs.map.hero_rm.floor_lst:
			err_txt = (f"You're already standing in the {gs.map.hero_rm.full_name}!")
			return True, False, err_txt
		return False, False, ""

	def enter_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if self.is_item():
			err_txt = (f"Despite twisting yourself into a pretzel you still can't manage to enter the {self.full_name}.")
			return True, False, err_txt
		if not self.is_seat():
			# attemptable error: there are many common uses of 'enter' that won't work in DC (e.g. "enter castle")
			err_txt = (f"You can't use the 'enter' command on the {self.full_name}.")
			return True, True, err_txt
		if self.is_seat() and len(self.contain_lst) >= self.max_obj:
			# NOT attemptable error: the capacity of the seat should be visually obvious
			err_txt = (f"There's no room on the {self.full_name} to sit.")
			return True, False, err_txt
		return False, False, ""

	def exit_err(self, gs):
		creature = gs.core.hero
		if self.err_not_vis(creature, gs):
			return True, False, ""
		if self.err_wrt_not_vis(creature, gs):
			return True, False, ""
		if self.err_wrt_class(creature, gs):
			return True, False, ""
		if self.err_wrt_not_in_reach(creature, gs):
			return True, False, ""
		if not self.is_seat() and self.err_not_in_reach(creature, gs):
			return True, False, ""
		if self.is_item():
			err_txt = (f"Despite twisting yourself into a pretzel you still can't manage to exit the {self.full_name}.")
			return True, False, err_txt
		if not self.is_seat():
			# attemptable error: there are many colloquial uses of 'exit' that won't work in DC
			err_txt = (f"You can't use the 'exit' command on the {self.full_name}.")
			return True, True, err_txt
		if not creature.is_contained(gs):
			err_txt = (f"You can't exit the {self.full_name} - you're not presently in it!")
			return True, False, err_txt
		if creature.is_contained(gs) and creature.get_contained_by(gs) != self:
			err_txt = (f"You can't exit the {self.full_name} - you're not presently in it!")
			return True, False, err_txt
		return False, False, ""


	# *** two_word debug errors ***
	def get_weight_err(self, gs):
		if not gs.core.is_debug:
			err_txt = ("Please start your sentence with a known verb!")
			return True, False, err_txt
		if not (self.is_item() or self.is_creature()):
			err_txt = ("Only Items and Creatures have weight.")
			return True, False, err_txt
		return False, False, ""

	def capacity_err(self, gs):
		if not gs.core.is_debug:
			err_txt = ("Please start your sentence with a known verb!")
			return True, False, err_txt
		if not self.is_container() and not self.is_creature():
			err_txt = ("Only Containers and Creatures have capacity.")
			return True, False, err_txt
		return False, False, ""

	def where_is_err(self, gs):
		if not gs.core.is_debug:
			err_txt = ("Please start your sentence with a known verb!")
			return True, False, err_txt
		if self.is_writing():
			err_txt = (f"The where_is command does not work for objects of Writing class")
			return True, False, err_txt
		return False, False, ""


	# *** prep errors ***
	def drink_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):
			return True, False, ""
		if not self.is_liquid():
			# attemptable error: non-liquids may appear to be drinkable
			err_txt = (f"Your attempts to quaff the {self.full_name} do not meet with success.")
			return True, True, err_txt
		if obj.name in gs.io.get_lst('reservoir_lst'):
			# attemptable errore: in some cases, drinking from a resevoir should enable a machine
			err_txt = (f"You are about to take a big gulp from the {obj.full_name} but then think better of it.")
			return True, True, err_txt
		if not obj.is_container():
			err_txt = (f"How could you possibly drink {self.full_name} from a {obj.full_name}?")
			return True, False, err_txt
		if creature.hand_is_empty() or creature.get_hand_item() != obj:
			err_txt = (f"You need to be holding the {obj.full_name} to drink from it.")
			return True, False, err_txt
		if self not in obj.contain_lst:
			err_txt = (f"The {obj.full_name} doesn't contain {self.full_name}.")
			return True, False, err_txt
		return False, False, ""

	def lock_err(self, key_obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(key_obj, creature, gs):
			return True, False, ""
		if self.is_container() and not self.is_openable():
			err_txt = (f"There's nothing to lock. The {self.full_name} is always open.")
			return True, False, err_txt
		if (self.is_openable() and not self.is_lockable()):
			# attemptable error: player can only learn that obj cannot be locked by attempting
			err_txt = (f"The {self.full_name} does not appear to have a lock.")
			return True, True, err_txt
		if not self.is_lockable():
			# attemptable error: in some cases, player can only learn something is not lockable by attempting
			err_txt = (f"The {self.full_name} cannot be locked.")
			return True, True, err_txt
		if self.is_open == True:
			err_txt = ("You can't lock or unlock something that's open.")
			return True, False, err_txt
		if key_obj.is_switch():
			err_txt = (f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True, False, err_txt
		if not key_obj.is_item():
			err_txt = (f"And just how do you intend to lock a {self.full_name} with a {key_obj.full_name}??")
			return True, False, err_txt
		if key_obj.err_not_in_hand(creature, gs):
			return True, False, ""
		if self.key is None:
			# attemptable error: player can only learn there is no lock by trying
			err_txt = (f"You don't see a keyhole in the {self.full_name}.")
			return True, True, err_txt
		if key_obj != self.key and key_obj.root_name != 'key':
			#attemptable error: player only learns obj is not key by attempting
			err_txt = (f"You attempt to lock the {self.full_name} with the {key_obj.full_name} without success.")
			return True, True, err_txt
		if key_obj != self.key and key_obj.root_name == 'key':
			# attemptable error: player must try with wrong key to learn it is wrong
			err_txt = (f"You attempt to lock the {self.full_name} but the {key_obj.full_name} appears to be the wrong key.")
			return True, True, err_txt
		if self.is_unlocked == False:
			# attemptable error: player can only learn that the obj is locked by attempting an action on it
			err_txt = (f"The {self.full_name} is already locked.")
			return True, True, err_txt
		return False, False, ""

	def unlock_err(self, key_obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(key_obj, creature, gs):
			return True, False, ""
		if self.is_container() and not self.is_openable():
			err_txt = (f"There's nothing to unlock. The {self.full_name} is always open.")
			return True, False, err_txt
		if (self.is_openable() and not self.is_lockable()):
			# attemptable error: player can only learn that obj cannot be unlocked by attempting
			err_txt = (f"The {self.full_name} does not appear to have a lock.")
			return True, True, err_txt
		if not self.is_lockable():
			# attemptable error: in some cases, player can only learn something is not lockable by attempting
			err_txt = (f"The {self.full_name} cannot be unlocked.")
			return True, True, err_txt
		if self.is_open:
			err_txt = ("You can't lock or unlock something that's open.")
			return True, False, err_txt
		if key_obj.is_switch():
			err_txt = (f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True, False, err_txt
		if not key_obj.is_item():
			err_txt = (f"And just how do you intend to unlock a {self.full_name} with a {key_obj.full_name}??")
			return True, False, err_txt
		if key_obj.err_not_in_hand(creature, gs):
			return True, False, ""
		if self.key is None:
			# attemptable error: player can only learn there is no lock by trying
			err_txt = (f"You don't see a keyhole in the {self.full_name}.")
			return True, True, err_txt
		if key_obj != self.key and key_obj.root_name != 'key':
			#attemptable error: player only learns obj is not key by attempting
			err_txt = (f"You attempt to unlock the {self.full_name} with the {key_obj.full_name} without success.")
			return True, True, err_txt
		if key_obj != self.key and key_obj.root_name == 'key':
			# attemptable error: player must try with wrong key to learn it is wrong
			err_txt = (f"You attempt to unlock the {self.full_name} but the {key_obj.full_name} appears to be the wrong key.")
			return True, True, err_txt
		if self.is_unlocked:
			# attemptable error: player can only learn that the obj is unlocked by attempting an action on it
			err_txt = (f"The {self.full_name} is already unlocked.")
			return True, True, err_txt
		return False, False, ""

	def put_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(obj, creature, gs):
			return True, False, ""
		if not obj.is_item():
			err_txt = (f"You can't even pick up the {obj.full_name}... how could you possibly put it somewhere?")
			return True, False, err_txt
		if not self.is_container():
			# attemptable error: non-container could be mistaken for container
			err_txt = (f"You can't put the {obj.full_name} in or on the {self.full_name}.")
			return True, True, err_txt
		if self == obj:
			err_txt = (f"With all your might you attempt to bend the laws of time, space, and topology to your will... and in response you hear the ancient background radiation of the big bang itself respond: 'Nope, not gonna happen.'")
			return True, False, err_txt
		if obj.err_not_in_hand(creature, gs):
			return True, False, ""
		if self.is_openable() and self.is_open == False:
			err_txt = (f"The {self.full_name} is closed.")
			return True, False, err_txt
		if self.chk_content_prohibited(obj):
			err_txt = (f"You can't put the {obj.full_name} {self.prep} the {self.full_name}.")
			return True, False, err_txt
		if self.is_container() and not self.chk_has_capacity():
			# attemptable error: player gets info
			err_txt = (f"There's no room {self.prep} the {self.full_name} for another item.")
			return True, True, err_txt
		if self.max_weight - self.get_contained_weight() - obj.weight < 0:
			# attemptable error: player gets info
			err_txt = (f"The {self.full_name} doesn't have enough capacity to hold the {obj.full_name}.")
			return True, True, err_txt
		return False, False, ""

	def show_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(obj, creature, gs):
			return True, False, ""
		if not self.is_creature():
			# attemptable error: is certainly possible to attempt (e.g. 'show tablet to statue')
			err_txt = (f"Exactly how would you expect the {self.full_name} to respond to the {obj.full_name}?")
			return True, True, err_txt
		if obj.err_not_in_hand(creature, gs):
			return True, False, ""
		return False, False, ""

	def give_err(self, obj, gs):
		creature = gs.core.hero
		if self.err_prep_std(obj, creature, gs):
			return True, False, ""
		if not obj.is_item():
			err_txt = (f"You can't even pick up the {obj.full_name}... how could you possibly 'give' it?")
			return True, False, err_txt
		if not self.is_creature():
			# attemptable error: concievable that 'giving' and obj to a non creature would seem reasonable
			err_txt = (f"And what do you expect the {self.full_name} to do with the {obj.full_name}?")
			return True, True, err_txt
		if obj.err_not_in_hand(creature, gs):
			return True, False, ""
		if self == creature:
			err_txt = (f"With great formality and many words of thanks, you hand the {obj.full_name} to yourself.")
			return True, False, err_txt
		if self.weight + obj.weight > self.max_weight:
			# attemptable error: player gets info
			err_txt = (f"With a glum shake of their head, the {self.full_name} refuses the {obj.full_name}. You notice that the {self.full_name} appears to be overburdened already.")
			return True, True, err_txt
		return False, False, ""

	def attack_err(self, src_obj, gs):
		src_creature = gs.core.hero
		tgt_creature = self
		if self.err_prep_std(src_obj, src_creature, gs):
			return True, False, ""
		if not self.is_creature():
			# attemptable error: could appear reasonable to attack a non-creature
			err_txt = (f"What kind of deranged person attacks a {self.full_name} with a {src_obj.full_name}?!?")
			return True, True, err_txt
		if not tgt_creature.is_attackable:
			# attemptable error: clearly attemptable, player gets info, may trigger complex events
			try:
				err_txt = gs.io.get_str_nr(f"not_attackable_{src_creature.name}_{tgt_creature.name}")
			except:
				err_txt = ("You consider attacking but then think better of it. There must be another path to victory.")
			return True, True, err_txt
		if (not src_obj in src_creature.feature_lst) and (not src_creature.chk_in_hand(src_obj)):
			err_txt = (f"You are not holding the {src_obj.full_name} in your hand.")
			return True, False, err_txt
		if (src_obj in src_creature.feature_lst) and (not src_creature.hand_is_empty()):
			err_txt = (f"You can't attack with your {src_obj.full_name} while you're holding the {src_creature.get_hand_item().full_name}.")
			return True, False, err_txt
		if src_creature == tgt_creature:
			err_txt = ("You can't attack yourself!")
			return True, False, err_txt
		return False, False, ""


	# *** go_case error ***
	def go_err(self, dir, gs):
		creature = gs.core.hero
		if dir not in ['north', 'south', 'east', 'west']:
			err_txt = (f"'{dir}' is not a valid direction that you can go in.")
			return True, False, err_txt
		if creature.is_contained(gs):
			err_txt = (f"You'll have to exit the {creature.get_contained_by(gs).full_name} to attempt that.")
			return True, False, err_txt
		if not gs.map.chk_valid_dir(self, dir):
			err_txt = gs.io.get_str(f"dir_err_{random.randint(0, 4)}", 'experience')
			return True, True, err_txt
		door = gs.map.get_door(self, dir)
		if not isinstance(door, str) and door.is_openable() and door.is_open == False:
			err_txt = (f"The {door.full_name} is closed.")
			return True, True, err_txt
		return False, False, ""

