# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 28, 2023
# description: Invisible class deffinition module


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

	# *** simple methods ***
	def get_title_str(self, active_gs):
		return None

	# *** class identity methods ***
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
	def read(self, active_gs, mode):
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

	def examine(self, active_gs, mode):
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

#	def take(self, active_gs, mode):
	def take_err(self, active_gs):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if self.is_liquid():
			active_gs.buffer("You can't 'take' a liquid but you can 'drink' a liquid or you can 'take' a container that holds a liquid.")
			return True
		if not self.is_item():
			active_gs.buffer(f"Just how do you intend to pick up a {self.full_name}?")
			return True
		if creature.chk_in_hand(self):
			active_gs.buffer("You're already holding the " + self.full_name)
			return True
		for obj in active_gs.get_room().floor_lst:
			if obj.is_creature() and obj is not active_gs.hero and self in obj.get_vis_contain_lst(active_gs):
				active_gs.buffer(f"Burt, you can't take the {self.full_name}. It belongs to the {obj.full_name}!")
				return True
		return False

	def drop(self, active_gs, mode):
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

	def open(self, active_gs, mode):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_door():
			active_gs.buffer(f"The {self.full_name} cannot be openned.")
			return True
		return False
	
	def close(self, active_gs, mode):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_door():
			active_gs.buffer(f"The {self.full_name} cannot be closed.")
			return True
		return False

	def eat(self, active_gs, mode):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_food():
			active_gs.buffer(f"What kind of desperate individual tries to eat a {self.full_name}? Burt, if you keep this up you're going to give Adventurers a bad name!")
			return True
		return False

	def wear(self, active_gs, wear):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_garment():
			active_gs.buffer(f"With a keen eye for high fashion, you boldly attempt to accoutre yourself in the {self.full_name}... it doesn't really work out... but nothing is harmed... except maybe your ego...")
			return True
		return False

	def drink(self, active_gs, mode):
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

	def push(self, active_gs, mode):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_buttonswitch():
			active_gs.buffer(f"Pushing on the {self.full_name} has no effect.")
			return True
		return False

	def pull(self, active_gs, mode):
		creature = active_gs.hero
		if self.err_std(creature, active_gs):
			return True
		if not self.is_springsliderswitch() and not self.is_leverswitch():
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

	def enter(self, active_gs, mode):
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

	def exit(self, active_gs, mode):
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


""" *** Module Documentation ***

	* Invisible class:
		
		Overview:
			name is a text string that represents the canonical name of an object. It should be identical to the declared object label, unique, and immutable. For object rusty_key, rusty_key.name = 'rusty_key'. For reasons that remain a little murky to my beginner brain, objects in Python have no way of actually knowing their own names. As I understand it, object names are merely labels that are pointers to the actual object... and the object itself has no idea what labels are pointing to it at any given time. In any case, the perceived wisdom is that if you want to be able to reference an object by its name, you'd better give it a name attribute - hence 'name'.
			
			The object tree of Dark Castle forks from Invisible. One trunk leads to Writing, then ViewOnly, and then all the other visible objects in the game that Burt can interct with. The other trunk leads to a collection of invisible objects that manage the automated behavior of the game. It might surprise a player of Dark Castle to learn that there are about as many invisible objects in the game as there are visible ones. However if you inspect the take() method you'll see that there's no code there that could trigger the royal_hedgehog to guard the shiny_sword. Likewise, there's no code in go() that could tell Burt about the Rusty Key when he tries to head south from the Entrance. These behaviors and many more are all enabled by invisible objects. See mach_class_def() for more information on these objects.

		Program Architecture:
			Becase Invisible is the root of the class inheritance tree and is also a class from which no objects are directly instantiated, it is the ideal place for methods that should always be available. There are 2 main classes of these:
				
				1) Class Identity Methods: these are the simple class identifyer methods (e.g. is_item() ) that returns True or False and which Dark Castle uses to verrify whether an object belongs to a given class. Within each class in the inheritance tree, the appropriate Class Identity Method is over-ridden with True but in Invisible, all of them are (except is_invisible() ) are set to False.

				2) The Error Sub-System. This is where Method Mis-Match errors are handled for all verb methods. The Error Sub-System spans the whole of Dark Castle but the foundation is laid in Invisible so this is a good place to discuss how it works. It's covered in more detail than anyone but myself could possibly desire in a section of its own.

	* Error Sub-System
		- Overview:
			Handling incorrect commands is an innate requirement of any text adventure. The error subsystem performs this duty.

		- Game Design:
			The Purpose of Errors:
				There are vastly more wrong command strings that can be given than right ones. When the valid command set is small enough, it works to simply accept the correct commands and throw a generic error on everything else. But as the vocabulary grows, the opportunity for genuine mis-wordings increses exponentially (e.g. if Burt can 'enter Throne', why can't he 'enter Moat' ??). At this point, the error sub-system becomes responsible for providing verb usage guidance. Lastly, anyone who plays the full game will recieve quite a few errors - so, in additiona to being instructive, errors should also be varried, fun, and amusing.

			Error Hierarchy:
				Along with providing guidance and humor, the error sub-system should present the player with the intuitively most obvious issue concerning their proposed action. For example, suppose the players issues the command "unlock gate with silver key". There could be several reasons why this command doesn't succeed: Maybe you aren't holding the key. Maybe the door is already open (in Dark Castle you can't lock or unlock an open door). Maybe the Silver Key is the wrong key for the Gate. In fact, all three of these could be true at once. But we only want to throw one error - and we want that error to reflect the "most obvious" problem (in this case, the fact that you aren't holding the Silver Key that you intended to unlock the Gate with).

				The error hierarchy for a given class can be intricate and even debatable (in the above example, one could argue that the door being open is a more obvious issue than not having the Silver Key in hand). But for most verbs there are some broad initial errors (these are the Generic Command Errors described under Implementation Details) to check that have a standard hierarchy:
					1. A referenced object is not visible in the room
					2. A referenced object is of class Writing (and the command is not read() )
					3. A referenced object is not in reach (for example, because Burt is in a Seat)
					4. A referenced object is not a member of the verb method class but merrits a custom error (e.g. take(obj) where obj is of class Liquid)
					5. A referenced object is not a member of the verb method class (generic case). (e.g. take(obj) where obj is not of class Item)

			Errors Are for User Input:
				One of the issues with traditional text adventures like Zork is that they are often set in vest empty terrains. The Great Underground Empire is fascinating... but nearly devoid of life. I suspect the reason for this is simple: programming creatures is hard. One of my goals is for Dark Castle to feel more "lived in" than Zork... so I intend to make all verb methods "symetric" - meaning that they can optionally take 'creature' as an arguemnt and can be used for any creature in the game - not just Burt. Hopefully, this makes programming creatures easier and encourages a more populous dungeon. 
				
				However, there are limits. Errors are tricky. Creatures are tricky. For now at least, throwing gramatically accurate errors for non-Burt creatures is simply out of scope. For non-Burt creatures, errors should be silencable (future feature) - but if not silenced, they will appear to be directed at the user - and at Burt in particular - in second person tense. It is up to the Implementor to avoid programming other creatures to perform error generating tasks!

		- Implementation Detail:
			There are 2 Error Types:

				1) Interpreter Errors: The interpreter is unclear what command the player is trying to issue.
				
				2) Command Errors: The command is understood but cannot be carried out.
			
			There are 4 flavors of Command Error:
				1) Generic Command Errors: Command failure cases that occur across multiple methods. e.g. very few commands will run if the noun of the command is not in the room's scope. Catching these errors in validate() avoids needing to re-write the same error-checking code repeatedly in multiple methods.
				
				2) Custom Command Errors: Command failure cases specific to a given method. e.g. Burt tries to unlock a container with the wrong key. This is a specific type of error that is best addressed in the unlock() method code itself. The error text is buffered and the fail condition is returned to validate() - which then returns False to app_main() - so that no command is actually run.
				
				3) Generic Method Mis-Match Errors: The player attempts to use a method on an incompatible object. These are usually acts of experimentation or silliness on the player's part. e.g. when Burt tries to 'take castle' no one really expects the command to work. So we throw a random, appropriately snide error.
				
				4) Custom Method Mis-Match Errors: In a few specific cases, player confusion over which methods can be used with which objects is quite justified. e.g. it's not unreasonable for the player to attempt to take the 'water'. In these cases we would like to give an explanitory error - but we can't provide a Custom Method Failure as the method cannot run at all. So, we trap the error in advance in the validate() method so that a helpful response can be given.

			No actions should be performed via errors:
				As a general rule, no actions should be taken - and no in-game information should be provided - via errors. The error sub-system is intended as a 'pre-check' for user commands, which then aborts from command execution if the command is not valid. Time does not pass on error-generating turns and there are no pre-actions, post-actions, or auto-actions. 

				While it is technically possible to update object state within error code, this is not intended and should be avoided. If a state change will be triggered, it should be handeled within the class verb method - or possibly by a modular machine. Ideally, the same would be true for providing in-game information (e.g. examine() or read() ). An exception to this rule can be made for game meta-information where the player appears to need a usage hint (e.g. "use read() rather than examine() on objects of class Writing"). 

		- Program Architecture:
			We need to deal with two mai variants of Command Errors: 1) Custom Command Errors that are are specific to the verb method and its class and 2) Those errors that are based on Method Mis-Match or are Generic in nature. As mentioned in Implemntation Details, Custom Command Errors are dealt with in the body of the verb method itself. But where to address the other three flavors of Command Errors?
			
			Invistible is the top of the class inheritance tree. So this is an obvious place to catch any Method Mis-Match Error. As a result, every verb method has two error code blocks: One for Custom Command Errors that lives in the verb method itself, and another in Invisible that deals with Method Mis-Match Errors and Generic Command Errors.

			These two error code blocks are not independent. Instead, the verb method code block (which addresses class-specific Custom Command Errors) calls (arguably, extends) the Invisible error block. The Invisible code block returns True if there is an error and Falso on no errors. So the first thing the verb method error block does it to call the Invisible block and exit on true.

			This structure is perhaps a bit heavy-handed but it has the following advantages:
			
				1) All Command Errors are generated in only one of two possible code blocks

				2) Re-use of the Generic Command Error / Method Mis-Match Error code block when checking for Custom Command Errors

				3) Because all Command Errors are called within a method (vs. in validate() ), Custom Method Mis-Match errors can easily be generated based on referenced object class.

		- A Not-so-Brief History of Error Handling:
			From the start, the verb methods themselves were the home for all Generic and Custom Command Errors. I addressed Method Mis-Match cases in cmd_exe() where I simply wrapped the verb method call in a try... except... routine that called a random, non-specific, humorous error. 
			
			However, as time passed, and I created more verb methods - and periodically went back to refactor them - the repetition of Generic Command Errors began to bother me. Also, the unfairness of the Custom Method Mis-Match cases (especially examine() for Writing) became clearer. So I began to look for a central pre-verb-method "home" for these error checks.

			Originally, cmd_exe() fit this purpose. I simply checked for the Generic Command Error cases and the Custom Method Mis-Match cases in advance of the try... except... verb method call.
			
			This worked acceptably well right through v3.68 (precedural parity version). However, as coding progressed a couple issues made it clear this was non-ideal:

				1) Once timers were introduced, time tracking became important.	

				2) The bigger problem was the more advanced use of pre_action machines. (see validte() for more info)

			For both these reasons, validate() was inserted between interp() and pre_action() during refactoring and became the new home for Generic Command Errors, Generic Method Mis-Match Errors, and Custom Method Mis-Match Errors.

			Over time, it began to click for me that a better solutino for Custom Method Mis-Match Errors was to instantiate them in the problem class. So in created a separate take() method in class Liquid that did nothing but throw an error explaining the the use that they were not able to 'take' a liquid and recommending that they try 'drink' instead. Of course, for this to work, I needed to exclude these special cases from any general Method Mis-Match cases that were handled in validate().

			Also, around this time, I began repalying Hollywood Hijinx with my youngest son, Joshua. I'd never played it all the way through before and we had a lot of fun solving it (though I did need hints on both the penguin and the buzz saw - both of which felt like iffy puzzles to me). In playing it I was reminded that Infocom did a nice job of throwing verb-specific errors... where-as Dark Castle still threw generic "Burt, I have no idea what you're talking about" errors for the vast majority of Method Mis-Matches.

			So, this was the state of DC errors when I started coding the Seat class... which required a whole slew of new Generic Command errors. Here, the complexity sins of my past caught up with me. I had error messages being triggered from interp(), validate(), verb classes, and non-verb classes. I struggled repeatedly to troubleshoot bugs because I couldn't easily figure out which bit of code (false) errors were getting triggered from. I eventually got class Seat working but I was so frustrated with the error situation that I pushed off the othe work I had been planning to do and immediately started working on the (hoefully) comprehensive and systemic error solution. I initially put the foundation of the Error Sub-System in Writing (the highest visible class in the inheritance tree), but quickly realized that Invisible wouild be a better home.

"""