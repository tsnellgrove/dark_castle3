# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 28, 2023
# description: Invisible class deffinition module



### classes
class Invisible(object):
	def __init__(self, name):
		self._name = name # text str of each obj's canonical name; should be unique and immutable
		""" Invisible is the root object class. There are no instantiated objects of class Invisible but all objects in the game inherit the name attribute and some basic methods from Invisible. 
		"""

	# *** getters & setters ***
	@property
	def name(self):
		return self._name

	# *** simple methods ***
	def is_invisible(self):
		return True

	def is_item(self):
		return False

	def is_food(self):
		return False

	def is_liquid(self):
		return False

	def is_weapon(self):
		return False

	def	is_door(self):
		return False

	def	is_container(self):
		return False

	def is_portablecontainer(self):
		return False

	def is_surface(self):
		return False

	def is_creature(self):
		return False

	def is_switch(self):
		return False

	def is_timer(self):
		return False

	def is_mach(self):
		return False

	def is_garment(self):
		return False

	def is_seat(self):
		return False

	def get_title_str(self, active_gs):
		return None

	# *** standard errors ###	
	def err_invis_obj(self, creature, active_gs):
		if self.is_invisible():
			active_gs.buffer(f"During a brief moment of clarity, you see that the world around you is nothing but lines of code... vertical trails of glowing green characters tumble down across your vision... realizing that you are The One, you reach for the {self.full_name}... but just as your fingers approach it, the vision evaporates and your insight into Simulation Theory of Life fades from your mind and is forgotten forever...")
			return True
		return False

	def err_wrt_not_vis(self, creature, active_gs):
		room = active_gs.map.get_obj_room(creature)
		if self.is_writing() and not room.chk_wrt_is_vis(self, active_gs):
			active_gs.buffer(f"You can't see {self.full_name} written on anything here.")
			return True
		return False

	def err_wrt_not_in_reach(self, creature, active_gs):
		if self.is_writing() and creature.is_contained(active_gs) and not creature.get_contained_by(active_gs).chk_wrt_is_vis(self,active_gs):
			active_gs.buffer(f"You'll have to exit the {creature.get_contained_by(active_gs).full_name} to attempt that.")
			return True
		return False

	def err_wrt_class(self, creature, active_gs):
		if self.is_writing():
			active_gs.buffer(f"That's laudably creative but, truth be told, the only thing you can generally do with the {self.full_name} is to read it.")
			return True
		return False

	def err_not_vis(self, creature, active_gs):
		room = active_gs.map.get_obj_room(creature)
		if not self.is_writing() and room.chk_is_vis(self, active_gs) == False: 
			active_gs.buffer("You can't see a " + self.full_name + " here.")
			return True
		return False

	def err_not_in_reach(self, creature, active_gs):
		room = active_gs.map.get_obj_room(creature)
		if not self.is_writing() and creature.is_contained(active_gs) and self not in creature.get_contained_by(active_gs).get_vis_contain_lst(active_gs) + [room]:
			active_gs.buffer(f"You'll have to exit the {creature.get_contained_by(active_gs).full_name} to attempt that.")
			return True
		return False

	def err_not_in_hand(self, creature, active_gs):
		if not creature.chk_in_hand(self):
			active_gs.buffer("You're not holding the " + self.full_name + " in your hand.")
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
	def read(self, active_gs):
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
			active_gs.buffer(f"You can't read the {self.full_name}. Try using 'examine' instead.")
			return True
		return False

	def examine(self, active_gs):
		creature = active_gs.hero
		if self.err_not_vis(creature, active_gs):
			return True
		if self.err_wrt_not_vis(creature, active_gs):
			return True
		if self.is_writing():
			active_gs.buffer(f"You can't examine the {self.full_name}. Try using 'read' instead.")
			return True
		if self.err_not_in_reach(creature, active_gs):
			return True
		if self.err_wrt_not_in_reach(creature, active_gs):
			return True
		return False

	def take(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self.is_liquid():
			active_gs.buffer("You can't 'take' a liquid but you can 'drink' a liquid or you can 'take' a container that holds a liquid.")
			return True
		if not self.is_item():
			active_gs.buffer(f"Just how do you intend to pick up a {self.full_name}?")
			return True
		return False

	def drop(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self == creature.feature_lst[0]:
			active_gs.buffer(f"Burt, you can't drop your {creature.feature_lst[0].full_name} - you're quite attached to it.")
			return True
		if not self.is_item():
			active_gs.buffer(f"You can't even pick up the {self.full_name}... how could you possibly drop it??")
			return True
		return False

	def open(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_door():
			active_gs.buffer(f"The {self.full_name} cannot be openned.")
			return True
		return False
	
	def close(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_door():
			active_gs.buffer(f"The {self.full_name} cannot be closed.")
			return True
		return False

	def eat(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_food():
			active_gs.buffer(f"What kind of desperate individual tries to eat a {self.full_name}? Burt, if you keep this up you're going to give Adventurers a bad name!")
			return True
		return False

	def wear(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_garment():
			active_gs.buffer(f"With a keen eye for high fashion, you boldly attempt to accoutre yourself in the {self.full_name}... it doesn't really work out... but nothing is harmed... except maybe your ego...")
			return True
		return False

	def drink(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_liquid():
			active_gs.buffer(f"Your attempts to quaff the {self.full_name} do not meet with success.")
			return True
		return False

	def go(self, dir, active_gs):
		creature = active_gs.hero
		if dir not in ['north', 'south', 'east', 'west']:
			active_gs.buffer(f"'{dir}' is not a valid direction that you can go in.")
			return True
		if creature.is_contained(active_gs):
			active_gs.buffer(f"You'll have to exit the {creature.get_contained_by(active_gs).full_name} to attempt that.")
			return True
		return False

	def push(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_switch():
			active_gs.buffer(f"Pushing on the {self.full_name} has no effect.")
			return True
		return False

	def pull(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_switch():
			active_gs.buffer(f"Pulling on the {self.full_name} has no effect.")
			return True
		return False

	def lock(self, key_obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(key_obj, creature, active_gs):
			return True
		if not self.is_door():
			active_gs.buffer(f"The {self.full_name} cannot be locked.")
			return True
		if key_obj.is_switch():
			active_gs.buffer(f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True
		if not key_obj.is_item():
			active_gs.buffer(f"And just how do you intend to lock a {self.full_name} with a {key_obj.full_name}??")
			return True
		return False

	def unlock(self, key_obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(key_obj, creature, active_gs):
			return True
		if not self.is_door():
			active_gs.buffer(f"The {self.full_name} cannot be unlocked.")
			return True
		if key_obj.is_switch():
			active_gs.buffer(f"You'll need to be more specific about what you want to do with the {key_obj.full_name}.")
			return True
		if not key_obj.is_item():
			active_gs.buffer(f"And just how do you intend to unlock a {self.full_name} with a {key_obj.full_name}??")
			return True
		return False

	def put(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(obj, creature, active_gs):
			return True
		if not obj.is_item():
			active_gs.buffer(f"You can't even pick up the {obj.full_name}... how could you possibly put it somewhere?")
			return True
		if not self.is_container():
			active_gs.buffer(f"You can't put the {obj.full_name} in or on the {self.full_name}.")
			return True
		return False

	def enter(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self.is_item():
			active_gs.buffer(f"Despite twisting yourself into a pretzel you still can't manage to enter the {self.full_name}.")
			return True
		if not self.is_seat():
			active_gs.buffer(f"You can't use the 'enter' command on the {self.full_name}.")
			return True
		return False

	def exit(self, active_gs):
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
			active_gs.buffer(f"Despite twisting yourself into a pretzel you still can't manage to exit the {self.full_name}.")
			return True
		if not self.is_seat():
			active_gs.buffer(f"You can't use the 'exit' command on the {self.full_name}.")
			return True
		return False

	def show(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(obj, creature, active_gs):
			return True
		if not self.is_creature():
			active_gs.buffer(f"Exactly how would you expect the {self.full_name} to respond to the {obj.full_name}?")
			return True
		return False

	def give(self, obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(obj, creature, active_gs):
			return True
		if not obj.is_item():
			active_gs.buffer(f"You can't even pick up the {obj.full_name}... how could you possibly 'give' it?")
			return True
		if not self.is_creature():
			active_gs.buffer(f"And what do you expect the {self.full_name} to do with the {obj.full_name}?")
			return True
		return False

	def attack(self, src_obj, active_gs):
		creature = active_gs.hero
		if self.err_prep_std(src_obj, creature, active_gs):
			return True
		if not self.is_creature():
			active_gs.buffer(f"What kind of deranged person attacks a {self.full_name} with a {src_obj.full_name}?!?")
			return True
		return False

	# *** obj representation def ***
	def __repr__(self):
		return f"Object {self.name} is of class {type(self).__name__}"