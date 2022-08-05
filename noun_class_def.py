# program: dark castle v3.70
# name: Tom Snellgrove
# date: July 24, 2022
# description: class deffinition module


### import
import random
from static_gbl import descript_dict, static_dict
from shared_class_func import obj_lst_to_str


### local functions


### classes
class Invisible(object):
		def __init__(self, name):
				self._name = name # text str of each obj's canonical name; should be unique and immutable
				""" Invisible is the root object class. There are no instantiated objects of class Invisible but all objects in the game inherit the name attribute and some basic methods from Invisible. 
				
				name is a text string that represents the canonical name of an object. It should be identical to the declared object label, unique, and immutable. For object rusty_key, rusty_key.name = 'rusty_key'. For reasons that remain a little murky to my beginner brain, objects in Python have no way of actually knowing their own names. As I understand it, object names are merely labels that are pointers to the actual object... and the object itself has no idea what labels are pointing to it at any given time. In any case, the perceived wisdom is that if you want to be able to reference an object by its name, you'd better give it a name attribute - hence 'name'.
				
				The object tree of Dark Castle forks from Invisible. One trunk leads to Writing, then ViewOnly, and then all the other visible objects in the game that Burt can interct with. The other trunk leads to a collection of invisible objects that manage the automated behavior of the game. It might surprise a player of Dark Castle to learn that there are about as many invisible objects in the game as there are visible ones. However if you inspect the take() method you'll see that there's no code there that could trigger the royal_hedgehog to guard the shiny_sword. Likewise, there's no code in go() that could tell Burt about the Rusty Key when he tries to head south from the Entrance. These behaviors and many more are all enabled by invisible objects. See mach_class_def() for more information on these objects.
				"""

		# *** getters & setters ***
		@property
		def name(self):
				return self._name

		# *** simple methods ***
		def is_item(self):
				return False

		def is_beverage(self):
				return False

		def is_weapon(self):
				return False

		def	is_container(self):
				return False

		def is_creature(self):
				return False

		def is_timer(self):
				return False

		def is_mach(self):
				return False

		def __repr__(self):
				return f"Object {self.name} is of class {type(self).__name__}"

		# *** temp method - be moved to Container ***
		def	print_contents_str(self, active_gs):
				if self.is_container() and self.is_open == True:
						container_str = obj_lst_to_str(self.contain_lst)
						active_gs.buffer("The " + self.full_name + " contains: " + container_str)

class Writing(Invisible):
		def __init__(self, name, full_name, root_name, descript_key):
				super().__init__(name)
				self._full_name = full_name # the object name presented to the player. Typical format = "Adj Noun". First character capitalized
				self._root_name = root_name # the one-word abreviation for the canonical adj_noun formulated name. e.g. rusty_key => key; not unique 
				self._descript_key = descript_key # the key used to look up the object description in descript_dict
				""" Writing objects represent text which can be read().
				
				It may seem counter-intuitive that the first visible object class in the hierarchy is Writing - but when one remembers that all other visible objects can have Writing as an attribute the order makes sense. As the first class that Burt can interactive, Writing introduces three critical attributes:
						
						full_name is a text string that represents the object name the player will see. the full_name for object rusty_key is 'Rusty Key'. All object full_names are capitalized as a convention intended to help players recognize which entities in the room descriptions they can interact with.
						
						root_name is a text string that represents the one-word "short name" for an object. The root_name for object rusty_key is 'key'. The player can refer to the object by its root_name so long as there are no other visible objects with the same root_name. root_name is used within the interpreter().
						
						descript_key is a text string that is used to lookup the description of an object (or in the case of the Writing class, the text of an object) in descript_dict. By default, descript_key == name (i.e. the descript_key for object rusty_key is 'rusty_key'). However, by making descript_key and independent attribute from name, we enable the descriptions (or text) associated with an object to change over time.
						
				Historic Note:				
						The tradition of copous writing samples in text adventures dates right back to Zork itself. In Zork the first interactive object you come across is a mailbox. And within the mailbox is a leaflet you can read and which welcomes you to the game. Dark Castle cleaved tightly to this tradition. From the earliest implementation, the front_gaate had rusty_lettering... which is both a reference to the similar gates of hades in Zork I and of course a nod to good ol' Dante.
				
				Implementation Details:
						It is worth noting that writing is treated a bit differently than other 'noun' objects. In theory, you could think of every ViewOnly and decendent object as 'containing' up to one writing object. But for other open containers (i.e. Containers and Creatures), the contents are listed when Burt enters a room. This is not the case for writing. Writing not included in a creature, room, or container's vis_lst and is only ever mentioned when the object it is written on is examined. This is partly to avoid over-cluttering the room descriptions and partly to provide a sense of discovery when an object is examined. Also, I picture Burt needing to peer closely at writing to make it out in the dim lantern light.
				"""

		# *** getters & setters ***
		@property
		def full_name(self):
				return self._full_name

		@property
		def root_name(self):
				return self._root_name

		@property
		def descript_key(self):
				return self._descript_key

		@descript_key.setter
		def descript_key(self, new_descript):
				self._descript_key = new_descript

		# *** simple methods ***
		def is_writing(self):
				return True

		def get_descript_str(self, active_gs):
				"""Provides the current description of an object.
				
				One might reasonably think that getting the description of an object would be a simple matter of looking up obj.descript_key in descript_dict. This does indeed work the vast majority of the time. And because an object's descript_key is independent of its canonical 'name', we can can change the value of descript_key (and therefore the description value) any time we want to. However, it should be noted that descript_dict lives in a module name static_gbl() - so named because all of its contents are indeed static. This is extremely useful logisticaly. It means that we never need to worry about saving any of the text in descript_dict - because it never changes. Instead we just change obj.descript_key and point to a different ready-made descript_dict value. Alternatively, if we need to dynamically generate a description, we can do that within a method based on current GameState (e.g. the description provided by inventory() ).
				
				But what if we want to dynamically generate a description *once* and then be able to reference it again in the future? An example of this is the 'secret code' on the guard_goblin's torn_note. We generate a random value between 0 and 7 for the iron_portcullis at the beginning of the game in start_up() and save that value to control_panel state... but how do we store the description for messy_handwriting? There are only 8 possible values so we could have 8 static dictionary entries in descript_dict - but a general solution to the problem seems desireable. My approach is to keep a small dyn_descript_dict in GameState where it is saved every turn. Then whenever we examine() or read() we try looking up obj.descript_key in dyn_descript_dict first. If this fails, then we check the static descript_dict. Hence the need for get_descript_str() in Writing.
				"""
				try:
						return active_gs.get_dyn_descript_dict(self.descript_key)
				except:
						try:
								return descript_dict[self.descript_key]
						except:
								return f"The {self.full_name} is simply indescribable."

		# *** complex methods ***
		def read(self, active_gs):
				""" Reads text found on an object. Read is the first player-accessible method. For the reasons mentioned above in Writing, writing objects are treated a bit differently than other 'nouns' and therefore the error checking in read() is a bit different as well (writing has it's own unique scope check method, chk_wrt_is_vis). Note that read is uniquely excluded from the 2word generic command failure routines in validate(). 
				"""
				if not self.is_writing() and not active_gs.scope_check(self):
						active_gs.buffer(f"You can't see a {self.full_name} here.")
						return 
				if not self.is_writing() and active_gs.scope_check(self):
						active_gs.buffer(f"You can't read the {self.full_name}. Try using 'examine' instead.")
						return 
				if not active_gs.chk_wrt_is_vis(self):
						active_gs.buffer(f"You can't see {self.full_name} written on anything here.")
						return 
				active_gs.buffer(self.get_descript_str(active_gs)) # is_writing() and chk_wrt_is_vis() 

class ViewOnly(Writing):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key)
				self._writing = writing # Writing obj associated with the ViewOnly object; writing = None if there is nothing to read on the obj
				""" ViewOnly objects can be examined and text on them can be read, but they can not interacted with in any other way
				
				ViewOnly is the most basic class that represents actual entities in the Dark Castle world. It introduces the all-important examine() method. However, the take() method is not yet defined so there's no hazard that Burt will make off with a ViewOnly object. This is actually quite handy. Adventures are inveterate pillagers but with ViewOnly you can be sure that an object will stay where you put it.
				
				Because the writing attribute is introduced in the ViewOnly class, any object that Burt can see is capable of holding text. I originally debated this approach. Of all attributes, writing is probably the one most often set to None. This seemed like a good case for a MixIn class... but then it became clear that I would have at least one member of nearly every class that had writing on it. Two versions of every class - one with writing and one without - certainly didn't seem desirable. Also, I often found myself adding text to objects later on as I realized that a puzzle was too obscure (e.g. the small_printing on the grimy_axe). As of v3.70 there's no conversation in the game - and none likly in the near future - so often it's left to writing to make the Dark Castle world feel explicable and lived in. Ultimately, in a game based on words, enabling lots of in-game text turns out to be pretty important.
				"""

		# *** getters & setters ***
		@property
		def writing(self):
				return self._writing

		# *** simple methods ***
		def is_writing(self):
				return False
		
		def has_writing(self):
				return self.writing is not None

		# *** complex methods ***
		def examine(self, active_gs):
				""" Describes an object. examine() is he most fundamental command for gameplay and is the second method available for visible objects after read(). ViewOnly is the ancestor of many other classes and quite a few of them expand upon examine() (e.g. in class Door, examine() is extended to describe whether the door is open or closed).
				"""
				active_gs.buffer(self.get_descript_str(active_gs))
				if self.has_writing():
						active_gs.buffer(f"On the {self.full_name} you see: {self.writing.full_name}")
				return

class Room(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, features, room_obj_lst, door_paths, invis_obj_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._features = features # list of non-items in room (can be examined but not taken)
				self._room_obj_lst = room_obj_lst # list of obj in the room that the player can interact with
				self._door_paths = door_paths # dictionary of {direction1 : door1}
				self._invis_obj_lst = invis_obj_lst # list of invisible obj in room

		# *** getters & setters ***
		@property
		def features(self):
				return self._features

		@property
		def room_obj_lst(self):
				return self._room_obj_lst

		def room_obj_lst_append(self, item):
				self._room_obj_lst.append(item)

		def room_obj_lst_extend(self, lst):
				self._room_obj_lst.extend(lst)

		def room_obj_lst_remove(self, item):
				self._room_obj_lst.remove(item)

		@property
		def door_paths(self):
				return self._door_paths
		
		def	door_in_path(self, direction):
				return direction in self.door_paths

		def get_door(self, direction):
				return self.door_paths[direction]

		@property
		def invis_obj_lst(self):
				return self._invis_obj_lst

		# *** simple methods ***
		def vis_element_lst(self):
				return self.room_obj_lst + self.features
		
		# *** complex methods ***
		def examine(self, active_gs):
				super(Room, self).examine(active_gs)
				room_item_obj_lst = []
				for obj in self.room_obj_lst:
						if not obj.is_item():
								active_gs.buffer("There is a " + obj.full_name + " here.")
								obj.print_contents_str(active_gs)
								if obj.is_creature() and not obj.hand_empty():
										active_gs.buffer("The " + obj.full_name + " is holding a " + obj.hand_item().full_name)
								if obj.is_creature() and not obj.worn_empty():
										active_gs.buffer("The " + obj.full_name + " is wearing: " + obj.worn_str())
						else:
								room_item_obj_lst.append(obj)
				if room_item_obj_lst:
						room_item_str_lst = obj_lst_to_str(room_item_obj_lst)
						active_gs.buffer("The following items are here: " + room_item_str_lst)
				for obj in room_item_obj_lst:
						obj.print_contents_str(active_gs)

		def go(self, direction, active_gs):
				room_obj = active_gs.get_room()
				door_in_path = self.door_in_path(direction)
				if door_in_path:
						door_obj = self.get_door(direction)
				if not active_gs.is_valid_map_direction(room_obj, direction):
						num = random.randint(0, 4)
						wrong_way_key = 'wrong_way_' + str(num)
						active_gs.buffer(descript_dict[wrong_way_key])
				elif (door_in_path) and (door_obj.is_open == False):
						active_gs.buffer("The " +  door_obj.full_name + " is closed.")
				else:
						next_room_obj = active_gs.get_next_room(room_obj, direction)
						active_gs.set_room(next_room_obj)
						next_room_obj.examine(active_gs)

class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key, writing)

		def is_item(self):
				return True

		def take(self, active_gs):

				if active_gs.hand_check(self):
						active_gs.buffer("You're already holding the " + self.full_name)
						return 

				room_obj = active_gs.get_room()
				room_obj_lst = room_obj.room_obj_lst
				backpack_lst = active_gs.get_backpack_lst()
				worn_lst = active_gs.get_worn_lst()

				if self not in room_obj_lst + backpack_lst + worn_lst:
						for obj in room_obj_lst: # handle case of obj in creature hand
								if obj.is_creature() and self in obj.vis_lst():
										active_gs.buffer("Burt, you can't take the " + self.full_name + 
														" it belongs to the " + obj.full_name + "!")
										return

				active_gs.put_in_hand(self)
				active_gs.buffer("Taken")
				if self in backpack_lst: # if taken from backpack, remove from backpack
						active_gs.backpack_lst_remove_item(self)
				elif self in worn_lst: # if taken from worn_lst, remove from worn_lst
						if self.remove_descript is not None:
								active_gs.buffer(descript_dict[self.remove_descript])
						active_gs.worn_lst_remove_item(self)
				elif self in room_obj_lst: # if taken from room, remove from room
						room_obj.room_obj_lst_remove(self)
				else:
						for obj in room_obj_lst: # else remove item from container it's in
								if obj.is_container() and obj.chk_in_contain_lst(self):
										obj.contain_lst_remove(self)
				return

		def drop(self, active_gs):
				active_gs.hand_lst_remove_item(self)
				room_obj = active_gs.get_room()
				room_obj.room_obj_lst_append(self)
				active_gs.buffer("Dropped")

class Door(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._is_open = is_open # True if the door is open, False if the door is closed, None if there is no door (useful for Container)
				self._is_unlocked = is_unlocked # True if the door is unlocked, False if the door is locked, None if there is no lock
				self._key = key # the key obj required to unlock the door; None means the door is not locked by a key
				""" Doors allow access to rooms and objects. They can be openned, closed, locked, or unlocked. Locked doors require the correct key to open. Finding a way to open a door is one of the most basic puzzle elements in the game.
				
				Historic Note:
						In v1 and v2 of Dark Castle, doors could be unlocked and opened but not closed or locked. The problem wasn't actually room doors - it would have been easy to code them to close and lock - the real problem was containers, which were based on the same code base as doors (as is still the case in v3). Containers were the last and most complicated thing I coded in v1 (v2 just being the web version of v1). I was running into the limits of writing the program in procedural code and by this time I knew I was going to do a full re-write in OOP. So faced with the prospect of writing a 'put' verb and more complicated room inventory management, I totally dialed it in. Containers in v1 / v2 simply dumped their contents into the room inventory the moment you managed to open them. But of course that meant you couldn't close the container - because the the objects 'in' the container would still be in the room... hence the lack of 'close' and 'lock'. From a gameplay and puzzle point of view, this was never a problem. But the asymetry always annoyed me - I pictured Nana calling out to Burt across the years "For goodness sake Burtie, close the door behind you!" Properly working Containers and Doors were one of my first goals for v3.
				
				Implementation Details:
						Standard doors are pretty straight forward. Whether they are open or closed, locked or unlocked, and what key is required to unlock them are goverened by three method-specific attributes: 'is_open', 'is_unlocked', and 'key'. Generally, 'is_open' and 'is_unlocked' are boolean; 'key' points to an Item object.
						
						However, all three variables can also take the value of None and invoke special interpretation when they do:
							
								'key is None'' => There's no keyhole in this door. The Iron Portcullis is an example of this - it is locked, but not by a key.
								
								'is_locked is None' => The door has no lock and cannot be locked. Although this kind of door is pretty rare in adventure games we see it in our daily lives all the time.
								
								'is_open is None' => There is no door to open, close, lock, or unlock. This can probably best be visualized as a doorframe. 
								
						The value of the 'is_open is None' case is initially hard to see since it behaves as nothing more than an archway that Burt can walk through. It makes more sense when you rmemember that the Container class inherits from the Door class and only contributes the additional attribute of 'contain_lst'. So a Container with 'is_open is None' is just a box without a lid. Again, a somewhat rare phenomenon in the world of Interactive Fiction dungeons, but a common object in our daily lives. Container inheritance also explains why the error messages for  Door are a bit vague... they need to encompass actions directed to not only the 'front_gate' and 'iron_portcullis' but also the 'crystal_box' and the 'glass_bottle'.
						
						A final note on evaluating the difference between None and False:
								'if var:' is the same as 'if bool(var):', and 'bool(None)' evalutates to False. This means that there's a subtle risk of our conditional interpreting 'is_open == None' as 'is_open == False'. For clarity, we always test for the 'is None' cases first. And we always test for 'if var == False:' (as opposed to 'if not var:')							
				"""

		# *** getters & setters ***
		@property
		def is_unlocked(self):
				return self._is_unlocked

		@is_unlocked.setter
		def is_unlocked(self, new_state):
				self._is_unlocked = new_state

		@property
		def is_open(self):
				return self._is_open

		@is_open.setter
		def is_open(self, new_state):
				self._is_open = new_state

		@property
		def key(self):
				return self._key

		@key.setter
		def key(self, new_key):
				self._key = new_key

		# *** complex methods ***
		def examine(self, active_gs):
				super(Door, self).examine(active_gs)
				""" Door-specific examine() responses to be provided in addition to the base examine() method in ViewOnly  
				"""
				if self.is_open is None:
						active_gs.buffer(f"The {self.full_name} has no closure. It always remains open.")
						return				
				if self.is_open == False:
						active_gs.buffer(f"The {self.full_name} is closed.")
						return
				active_gs.buffer(f"The {self.full_name} is open.") # is_open == True
				return

		def unlock(self, active_gs):
				""" Unlocks a Door object.
				"""
				if self.is_open is None:
						active_gs.buffer(f"There's nothing to unlock. The {self.full_name} is always open.")
						return 
				if self.is_unlocked is None:
						active_gs.buffer(f"The {self.full_name} does not appear to have a lock.")
						return 
				if self.key is None:
						active_gs.buffer(f"You don't see a keyhole in the {self.full_name}.")
						return
				if self.is_open:
						active_gs.buffer("You can't lock or unlock something that's open.")
						return 
				if self.is_unlocked:
						active_gs.buffer(f"The {self.full_name} is already unlocked.")
						return 
				if not active_gs.hand_check(self.key) and not active_gs.hand_empty() and active_gs.get_hand_lst()[0].root_name == 'key':
						active_gs.buffer("You aren't holding the correct key.")
						return 
				if not active_gs.hand_check(self.key):
						active_gs.buffer("You aren't holding the key.")
						return 
				active_gs.buffer("Unlocked") # correct key in hand, is_open == False, is_unlocked == False
				self.is_unlocked = True

		def open(self, active_gs):
				""" Opens a Door object.
				"""
				if self.is_open is None:
						active_gs.buffer(f"The {self.full_name} has no closure. It is always open.")
						return 
				if self.is_open:
						active_gs.buffer(f"The {self.full_name} is already open.")
						return 
				if self.is_unlocked == False:
						active_gs.buffer(f"The {self.full_name} is locked.")
						return 
				self.is_open = True
				active_gs.buffer("Openned") # is_open == False, is_unlocked == True

		def close(self, active_gs):
				""" Closes a Door object.
				"""
				if self.is_open is None:
						active_gs.buffer(f"The {self.full_name} has no closure. It is always open.")
						return 
				if self.is_open == False:
						active_gs.buffer(f"The {self.full_name} is already closed.")
						return 
				if self.is_unlocked == False: # for Iron Portcullis
						active_gs.buffer(f"The {self.full_name} is locked open.")
						return 
				self.is_open = False
				active_gs.buffer("Closed") # is_open == True, is_unlocked == True

		def lock(self, active_gs):
				""" Locks a Door object.
				"""
				if self.is_open is None:
						active_gs.buffer(f"There's nothing to lock. The {self.full_name} is always open.")
						return 
				if self.is_unlocked is None:
						active_gs.buffer(f"The {self.full_name} does not appear to have a lock.")
						return 
				if self.key is None:
						active_gs.buffer(f"You don't see a keyhole in the {self.full_name}.")
						return
				if self.is_open == True:
						active_gs.buffer("You can't lock or unlock something that's open.")
						return
				if not active_gs.hand_check(self.key) and not active_gs.hand_empty() and active_gs.get_hand_lst()[0].root_name == 'key':
						active_gs.buffer("You aren't holding the correct key.")
						return 
				if not active_gs.hand_check(self.key):
						active_gs.buffer("You aren't holding the key.")
						return 
				if self.is_unlocked == False:
						active_gs.buffer(f"The {self.full_name} is already locked.")
						return 
				active_gs.buffer("Locked") # correct key in hand, is_open == False, is_unlocked == True
				self.is_unlocked = False

class Container(Door):
		def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key, contain_lst):
				super().__init__(name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key)
				self._contain_lst = contain_lst # list of items in the container

		# *** getters & setters ***
		@property
		def contain_lst(self):
				return self._contain_lst

		@contain_lst.setter
		def contain_lst(self, new_obj):
				self._contain_lst = new_obj

		# *** simple methods ***
		def chk_in_contain_lst(self, obj):
				return obj in self.contain_lst

		def contain_lst_append(self, item):
				self._contain_lst.append(item)

		def contain_lst_remove(self, item):
				self._contain_lst.remove(item)

		def	is_container(self):
				return True

		def vis_lst(self):
				if self.is_open:
						return self.contain_lst
				return []

		# *** complex methods ***
		def examine(self, active_gs):
				super(Container, self).examine(active_gs)
				self.print_contents_str(active_gs)

		def open(self, active_gs):
				super(Container, self).open(active_gs)
				self.print_contents_str(active_gs)

		def put(self, obj, active_gs):
				if self.is_open == False:
						active_gs.buffer("The " + self.full_name + " is closed.")
				elif obj.is_container():
						active_gs.buffer("You can't put a container in a container")
				elif obj.is_creature():
						active_gs.buffer("You can't put a creature in a container")
				else:
						active_gs.hand_lst_remove_item(obj)
						self.contain_lst_append(obj)
						active_gs.buffer("Done")
						
class Food(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, eat_desc_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._eat_desc_key = eat_desc_key # keys to description of eating food (stored in descript_dict)

		@property
		def eat_desc_key(self):
				return self._eat_desc_key

		def eat(self, active_gs):
					active_gs.hand_lst_remove_item(self)
					output = "Eaten. The " + self.full_name + " " + descript_dict[self.eat_desc_key]
					active_gs.buffer(output)

class Jug(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, is_open, contain_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._is_open = is_open # is the jug uncapped?
				self._contain_lst = contain_lst # obj in the jug

		@property
		def contain_lst(self):
				return self._contain_lst

		@property
		def is_open(self):
				return self._is_open

		def	is_container(self):
				return True

		def vis_lst(self): # DUP FROM CONTAINER CLASS
				vis_lst = []
				if self.is_open:
						vis_lst = self.contain_lst
				return vis_lst

		def examine(self, active_gs):
				super(Jug, self).examine(active_gs)
				self.print_contents_str(active_gs)

class Beverage(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, drink_descript_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._drink_desc_key = drink_descript_key # key to description of drinking the beverage (stored in descript_dict)

		@property
		def drink_desc_key(self):
				return self._drink_desc_key

		def is_beverage(self):
				return True

		def drink(self, active_gs):
				hand_lst = active_gs.get_hand_lst()
				if (active_gs.hand_empty()) or (hand_lst[0].is_container() == False):
						output = "You don't seem to be holding a container of " + self.full_name + " in your hand."
						active_gs.buffer(output)
				elif self not in hand_lst[0].contain_lst:
						output = "The container in your hand doesn't contain " + self.full_name + "."
						active_gs.buffer(output)
				else:
						hand_lst[0].contain_lst.remove(self)
						output = "Drunk. The " + self.full_name + " " + descript_dict[self.drink_desc_key]
						active_gs.buffer(output)

class Clothes(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, wear_descript, remove_descript, clothing_type):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._wear_descript = wear_descript # description when wearing garment (can be None)
				self._remove_descript = remove_descript # description when removing garment (can be None)
				self._clothing_type = clothing_type # e.g. 'hat'; Burt can only wear one garment of a given type at a time

		@property
		def wear_descript(self):
				return self._wear_descript

		@property
		def remove_descript(self):
				return self._remove_descript

		@property
		def clothing_type(self):
				return self._clothing_type

		def wear(self, active_gs):
				if active_gs.clothing_type_worn(self): # was 'elif' before special error
						output = "You are already wearing a " + self.clothing_type + ". You can't wear two garments of the same type at the same time."
						active_gs.buffer(output)
				else:
						active_gs.worn_lst_append_item(self)
						active_gs.hand_lst_remove_item(self)
						active_gs.buffer("Worn.")
						if self.wear_descript is not None:
								active_gs.buffer(descript_dict[self.wear_descript])

##		def remove(self, active_gs):
##				if self not in active_gs.get_worn_lst():
##						output = "You're not wearing the " + self.full_name + "."
##						active_gs.buffer(output)
##				else:
##						active_gs.put_in_hand(self)
##						active_gs.worn_lst_remove_item(self)
##						active_gs.buffer("Removed.")
##						if self.remove_descript is not None:
##								active_gs.buffer(descript_dict[self.remove_descript])


class Weapon(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, desc_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._desc_lst = desc_lst # descriptive terms associated with using the weapon to 'attack'

		@property
		def desc_lst(self):
				return self._desc_lst

		def is_weapon(self):
				return True
