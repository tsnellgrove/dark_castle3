# program: dark castle v3.72
# name: Tom Snellgrove
# date: Sept 10, 2022
# description: class deffinition module


### import
import random
from static_gbl import descript_dict, static_dict


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

		# *** simple obj methods ***
		def is_item(self):
				return False

		def is_liquid(self):
				return False

		def is_weapon(self):
				return False

		def	is_container(self):
				return False

		def is_portablecontainer(self):
				return False

		def is_creature(self):
				return False

		def is_timer(self):
				return False

		def is_mach(self):
				return False

		def get_title_str(self):
				return None

		def __repr__(self):
				return f"Object {self.name} is of class {type(self).__name__}"

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
						It is worth noting that writing is treated a bit differently than other 'noun' objects. Writing is not treated as being 'contained' in the object it is written on. Instead it is treated as an object 'Condition' (similar to a Door being open or closed) and as such it can only be observed via the exameine() method. This is partly to avoid over-cluttering the room descriptions and partly to provide a sense of discovery when an object is examined. Also, I picture Burt needing to peer closely at writing to make it out in the dim lantern light. See the ViewOnly examine() doc_string for details on Active vs. Passive Observation.
				
				Game Design:
						The introduction of descript_key is a good time to say a word about descriptions in general: they are the heart of Interactive Fiction. If you've ever read an IF walk-through it is dull as dust - because the interpreter's vocabulary is tiny and the commands to play the game are simple and repetative. It's the descriptions and the writing that create the illusion of a complex world. 
						
						Zork itself was often accused of 'purple prose' - which some claimed was all the more egrigious a sin given that the Zork interpreter could only understand a minute fraction of the words in its descriptions. I disagre with - yay verilly, gainsay! - this trait being claimed a fault. Now more than ever, anyone who's playing a text adventure game must have a deep and abiding love of words. Let us lean in and double-down on the 'purple-prose' and paint our digital landscapes with intense and vivid language - hopefully to the delight of logophiles and philologists the world over!
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

		# *** simple obj methods ***
		def is_writing(self):
				return True

		# *** complex obj methods ***
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

		def read(self, active_gs):
				""" Reads text found on an object. Read is the first player-accessible method. For the reasons mentioned above in Writing, writing objects are treated a bit differently than other 'nouns' and therefore the error checking in read() is a bit different as well (writing has it's own unique scope check method, chk_wrt_is_vis). Note that read is uniquely excluded from the 2word generic command failure routines in validate(). 
				"""
				room = active_gs.get_room()
				if not self.is_writing() and not room.chk_is_vis(self, active_gs):
						active_gs.buffer(f"You can't see a {self.full_name} here.")
						return 
				if not self.is_writing() and room.chk_is_vis(self, active_gs):
						active_gs.buffer(f"You can't read the {self.full_name}. Try using 'examine' instead.")
						return 
				if not room.chk_wrt_is_vis(self, active_gs):
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

		# *** attrib methods ***		
		def has_writing(self):
				return self.writing is not None

		# *** simple obj methods ***
		def is_writing(self):
				return False

		def get_vis_contain_lst(self, active_gs):
				return []

		def chk_contain_item(self, item):
				return False

		def remove_item(self, item, active_gs):
				pass
				return 

		def disp_cond(self, active_gs):
				pass
				return 

		def disp_contain(self, active_gs):
				pass
				return 

		# *** complex obj methods ***
		def examine(self, active_gs):
				""" Describes an object. examine() is the most fundamental command for gameplay and is the second method available for visible objects after read(). ViewOnly is the ancestor of all visible classes except Writing and quite a few of them expand upon examine() (e.g. in class Door, examine() is extended to describe Condition of the door - i.e. whether it is open or closed).
				
				Game Design / Theory:
						The examine() method is probably as good a place as anywhere to discuss the game design intentions of what Burt sees and how he sees it. In the Room method we will delve into the notion of node hierarchy - which is also related to what Burt sees - but for now we'll ignore nodes and speak in generalities.
						
						Let's start with *what* burt can see. There are many Python classes of visible objects. But from a description perspective there are basically only two types of visible object:
								
								Interactive Objects: These are objects that Burt can somehow interact with. This includes all Items, Doors, Containers, Switches, Creatures, and, every once in a while, a ViewOnly object. Solving puzzles and winning the game requires Burt to manipulate Interactive Objects.
								
								Descriptive Objects: These are always ViewOnly. In fact, most ViewOnly objects are Descriptive Objects. Burt can never manipulate Descriptive Objects and the whole game could be played through without ever paying any attention to them. They exist only to provide a bit of narrative color, to offer some in-game hints, and to provide some geeky humor. In Rooms and Creatures, ViewOnly Descriptive Objects are stored in the feature_lst attribute.
								
						Now lets talk about the two types of observation that Burt can engage in:
						
								Passive Observaation: This is what happens when Burt uses 'look' to examine a room or 'inventory' to examine himself. The game design goal of Passive Observaation is to provide the player with a broad awareness of what they can currently do in the game. To this end, 'look' + 'inventory' provide a listing of all Interactive Objects currently visible to Burt. However we don't want to drown the player in details every time they 'look' and we do want to encourage them to explore the Dark Castle world closely. So object Descriptions, Writing, and Conditions are not provided via Passive Observation. Also, Passive Observation does not provide a listing of Descriptive Objects - they are only mentioned in object Descriptions and must then be explicitly examined.
								
								Active Observation:  This is when Burt is examining a specific object. e.g. 'examine the front gate'. Burt can only examine one object at a time. The idea is that he is inspecting the object closely. Active Observaation will provide the following:
										- The object Title (rooms only)
										- The object Description
										- Writing on the object
										- The object Condition (i.e. open, closed, up, down, empty, etc)
										- A List of any Interactive Objects 'contained' within the examined object (including objects held / worn by Creatures)
				
						The hope is that, for the player, all of this theory results in intuitive game play. When you want a list of the 'stuff' in a room you 'look'... when you want to know everything about a specific object you 'examine' it... descriptions should be read carefully because, occasionally, they include references to things you can look at that aren't mentioned otherwise... But if you're actually reading through the code and wondering "Why aren't Writing objects, the state of Doors, or most ViewOnly objects listed via 'look' or 'inventory'?" - well, now you know.
				
				Historic Note:
						Originally, examine() was extended by most classes and there was no clear definition of what Burt saw when he examined an object. Codifying what was presented by examine() seemed valuable so I broke it into parts (Title, Description, Writing, Condition, Contained) and defined functions for those in each class. The also has the benefit of making it easier to enable or disable part of the examine() output based on settings like 'brief' and 'verbose'. The down side to this formal approach is that the descriptions have a bulleted feel and are hard to unify into paragraphs.
				"""
				if self.get_title_str() is not None:
						active_gs.buffer(self.get_title_str())
				active_gs.buffer(self.get_descript_str(active_gs))
				if self.has_writing():
						active_gs.buffer(f"On the {self.full_name} you see: {self.writing.full_name}")
				self.disp_cond(active_gs)
				self.disp_contain(active_gs)
				return

class Room(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing, feature_lst, floor_lst, invis_lst):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._feature_lst = feature_lst # list of descriptive obj in the room (can be examined but not interacted with)
				self._floor_lst = floor_lst # list of obj on the floor of the room that the player can interact with
				self._invis_lst = invis_lst # list of invisible obj in room
				""" Rooms are where everything happens in Dark Castle. Every space Burt can occupy is a 'room' - even if he is outside. All of the game's  visible objects (except Doors) are contained within Rooms. Rooms themselves (along with Doors) reside within the room-pairs of Map.
				
				Since everything Burt can interact with on a given turn (except Doors) is in the room that he's occupying, Room is the perfect place to determine object scope. All scope methods for both visible and invisble objects are in Room. Available exits are considered to be conditions of the Room and are presented when the Room is examined. The commands 'look' and 'examine room' have identical results.
								
				Program Architecture:
						Rooms are a good time to pause and discuss Receptacles and Nodes. Any visible object that can hold an Item is a Receptacle (i.e. Containers, Creatures, and Surfaces). As discussed in the Container method, Receptacles are 'smart' (i.e. they know what they contain) and Items are 'dumb' (i.e. they don't know what contains them). This means that to generate a list of all visible objects in a room (e.g. via get_vis_contain_lst() ) we need to first compile a list of immediately available objects and then, if any of them are open Receptacles, we need to list all of the ojbects inside *them*. But what if one of the objects inside a Receptacle is, itself, a Receptacle? 
						
						In theory, this could get deeply recursive. One obvious way to avoid this is "Just don't create very many PortableContainers in the game." But, hypoetheically, the goal is here is to create a tool set that could be used by others to build their own text adventure games... so we would like to put in place some prescriptive guard rails.
						
						Before we solve the problem, we need some nomenclature to describe it. The terminology I've chosen is "Node" from the study of binary trees (though in this case we have a non-binary tree). Imagine an inverted "tree" with one "node" at the top. This is the Room object, node_0. One level below Room we have nodes for all the visible objects in the Room. These are the node_1 objects. Some of the node_1 objects may be Receptacles and their contents are represented by Nodes one level further down: the node_2 objects. By default when we reference a node_1 object we are discussing 'absolute' node level where the current Room is node_0. But it is also possible to talk about 'relative' node level - for example, if Burt is in the Main Hall and holding the shiny_sword, then the shiny_sword has an absolute node level of node_2 (Room => Creature => Item) but a node level of node_1 relative to Burt (Burt => Item). You will occasionally seed node_1 or node_2 variables referenced in methods. In this case, absolute node level is being used.
						
						So now that we have have some terminology, the key question is: "How do we want the game to work?" Whe could use recursion to allow recepticales to be indefinitely nested... but tracking items like this is cumbersome and hard to represent to the user. At the other end of the spectrum, we could disallow any Receptacle nesting - but this seems heavy-handed. The capabilities and limitations of Zork help bring the objective into focus. Early in the game when the player enters the Kitchen they find a sack containing food and a bottle of water on a table. So PortableContainers nested on a Surface seems like a reasonable expectation. PortableContainers nested in Creatures and Containers also happens within the game. But there are no takable Creatures, few, if any, takable Surfaces, and few if any instances of PortableContainers nested in other PortableContainers. Adopting these limits allows us a fun simulation - but limits node level to 3 (Room => Receptacle => PortableContainer => Item) - which is a reasonable depth to manage and represent.
				"""

		# *** getters & setters ***
		@property
		def feature_lst(self):
				return self._feature_lst

		@property
		def floor_lst(self):
				return self._floor_lst

		@property
		def invis_lst(self):
				return self._invis_lst

		# *** attribute methods ***
		def floor_lst_append(self, item):
				self._floor_lst.append(item)

		def floor_lst_extend(self, lst):
				self._floor_lst.extend(lst)

		def floor_lst_remove(self, item):
				self._floor_lst.remove(item)

		# *** simple object methods ***
		def get_title_str(self):
				return f"*** {self.full_name} ***"

		# *** scope methods ***
		def get_vis_contain_lst(self, active_gs):
				""" Returns the list of visible objects contained in the method-calling object. In Room, provides the visible object scope.
				"""
				return_lst = []
				legacy_node1_lst = active_gs.get_hand_lst() + active_gs.get_backpack_lst() + active_gs.get_worn_lst() 
				for obj in legacy_node1_lst:
						return_lst += obj.get_vis_contain_lst(active_gs)
				return_lst = return_lst + legacy_node1_lst + active_gs.get_static_obj('universal')
				node1_only_lst = [self] + active_gs.map.get_door_lst(self) + self.feature_lst
				return_lst = return_lst + node1_only_lst
				for obj in self.floor_lst:
						return_lst += obj.get_vis_contain_lst(active_gs)
				return_lst = return_lst + self.floor_lst
				return return_lst

		def chk_wrt_is_vis(self, writing, active_gs):
				""" Evaluates whether the passed writing is visible within the methed-calling object.
				"""
				return any(obj.writing == writing for obj in self.get_vis_contain_lst(active_gs))

		def chk_is_vis(self, obj, active_gs):
				""" Evaluates whether the passed object is visible within the methed-calling object.
				"""
				return obj in self.get_vis_contain_lst(active_gs)

		def chk_contain_item(self, item, active_gs):
				""" Evaluates whether the passed object is contained within the methed-calling object.
				"""
				if item in self.floor_lst:
						return True
				if any(obj.chk_contain_lst(item) for obj in self.floor_lst):
						return True
				if item in active_gs.get_backpack_lst() + active_gs.get_worn_lst():
						return True
				return False

		def get_mach_lst(self, active_gs):
				""" Returns the list of Machine objects contained in the method-calling object. In Room, provides the Machine object scope.
				"""
				mach_lst = []
				scope_lst = self.get_vis_contain_lst(active_gs) + self.invis_lst
				for obj in scope_lst:
						if obj.is_mach():
								mach_lst.append(obj)
						if obj.is_creature():
								for invis_obj in obj.invis_lst:
										if invis_obj.is_mach():
												mach_lst.append(invis_obj)												
				mach_lst.extend(active_gs.universal_mach_lst) # Legacy
				return mach_lst

		# *** complex object methods ***
		def remove_item(self, item, active_gs):
				""" Removes the passed object from the methed-calling object. In Room, is used to enable the take() method.
				"""
				if item in self.floor_lst:
						self.floor_lst_remove(item)
						return 
				for obj in self.floor_lst:
						if obj.chk_contain_item(item):
								obj.remove_item(item, active_gs)
								return 
				if item in active_gs.get_backpack_lst():
						active_gs.backpack_lst_remove_item(item)
						return 
				if item in active_gs.get_worn_lst():
						active_gs.worn_lst_remove_item(item)
						return 
				raise ValueError(f"Can't remove item {item} from room {self.name}")
				return 

		def disp_cond(self, active_gs):
				""" Displays object-specific conditions. Used in examine().
				"""
				active_gs.buffer(active_gs.map.get_door_str(self))

		def disp_contain(self, active_gs):
				""" Displays a description of the visible items held by the obj. Used in examine().
				"""
				room_item_lst = []
				for obj in self.floor_lst:
						if obj == active_gs.hero:
								pass
						elif not obj.is_item():
								active_gs.buffer("There is a " + obj.full_name + " here.")
								obj.disp_contain(active_gs)
						else:
								room_item_lst.append(obj)
				if room_item_lst:
						room_txt_lst = [obj.full_name for obj in room_item_lst]
						room_item_str = ", ".join(room_txt_lst)
						active_gs.buffer("The following items are here: " + room_item_str)
				for obj in room_item_lst:
						obj.disp_contain(active_gs)
				return 

		def go(self, dir, active_gs):
				""" Moves a Creature from one room to another
				"""
				creature = active_gs.hero
				if not active_gs.map.chk_valid_dir(self, dir):
						active_gs.buffer(descript_dict[f"wrong_way_{random.randint(0, 4)}"])
						return
				door = active_gs.map.get_door(self, dir)
				if not isinstance(door, str) and door.is_open == False:
						active_gs.buffer(f"The {door.full_name} is closed.")
						return 
				next_room = active_gs.map.get_next_room(self, dir)
				active_gs.set_room(next_room)
				next_room.floor_lst_append(creature)
				self.floor_lst_remove(creature)
				next_room.examine(active_gs)


class Item(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key, writing)
				""" Items can be 'taken' and 'dropped'. Item inherits from ViewOnly and has no new attributes - just new methods: take() and drop(). 
				
				Implementation Details:
						All objects of class Item are takable - there's no 'is_takable' attribute to prevent this. To temporarily prevent an Item from being taken you could:
								1) Initially provide a ViewOnly object and then, when appropriate, swap in an Item object with the same full_name
								2) Prevent the take() method via a Warning
								3) Prevent the take() method via a Modular Machine
				
				Game Design:
						Adventurers love Items. This tradition dates back to Zork I itself, where the sole mission of the game was to collect 20 (or 19, depending on who you talk to) treasures and safely store them in a trophy case. Although Dark Castle theoretically follows the Enchanter tradition of saving the land, truthfully, Burt showed up at Dark Castle to score some loot and that desire is never far from his heart. Good game design leverages this love of Items. 
						
						Want to intrigue and excite an Adventurer? Show them an out-of-reach item. Want to infuriate an Adventurer? Pilfer their hard won items! Want to make a puzzle hard? Require that the Adventurer surrender an Item to solve it. Dark Castle leans heavily on each of these standard Adventurer herding techniques.
				"""

		# *** simple object methods ***
		def is_item(self):
				return True

		# *** complex object methods ***
		def take(self, active_gs):
				""" Takes an object from either the room or from Burt's inventory and places it into Burt's hand
				
				Implementation Detail:
						take() used to be a more complex method. Adding the object into Burt's hand is trivial but finding where to remove it from takes some serching. I initially did all that searching in take(). During refactoring it became clear that it made sense to do this in Room instead since the Room class is already responsible for providing visible object scope and therefore is already required to know all the places an object could be.
						
						I initially thought that the 'Can't take another creature's stuff' error would be a great use case for the any(if x == y for x in z) pattern. This proved to be incorrect. For one thing, the any() pattern is a one-liner - so 'x' does not exist outside that line - but I need it for the error message on the next line. Also, curiously, it turns out that Python's magic ability to have an 'if x and y' statement where 'y' can be undefined so long as 'x' is False does not work within any(). Code and learn!
						
						It may initially be surprising how few tests we need to conduct before performing the method. The logic works as follows:
								1) We confirm that 'obj' in visible to Burt in validate()
								2) 'obj' must either be of class Item or inherit from class Item or else the method could not run
								3) Local error checking ensures that 'obj' is not already in Burt's hand or held / worn by another creature
								4) Therefore, 'obj' must be a takable Item
				"""
				creature = active_gs.hero
				if creature.chk_in_hand(self):
						active_gs.buffer("You're already holding the " + self.full_name)
						return 
				for obj in active_gs.get_room().floor_lst:
						if obj.is_creature() and obj is not active_gs.hero and self in obj.get_vis_contain_lst(active_gs):
								active_gs.buffer(f"Burt, you can't take the {self.full_name}. It belongs to the {obj.full_name}!")
								return 
				active_gs.get_room().remove_item(self, active_gs)
				creature.put_in_hand(self)
				active_gs.buffer("Taken")
				return

		def drop(self, active_gs):
				""" Drops an object from Burt's hand to the floor of the room.
				"""
				creature = active_gs.hero
				creature.hand_lst_remove(self)
				active_gs.get_room().floor_lst_append(self)
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
						Before we talk about how doors work, let's take a moment to meniton where they 'live'. Unlike most other large objects (e.g. Creatures), doors do not reside in room.floor_lst. This is because doors don't really exist in just one room. Instead, they are contained within "door pairs" - which in turn reside in the map_lst attribute of the GameState map object. See map_class_def.py for details.
						
						The actual functioning of doors is pretty straight forward. Whether they are open or closed, locked or unlocked, and what key is required to unlock them are goverened by three method-specific attributes: 'is_open', 'is_unlocked', and 'key'. Generally, 'is_open' and 'is_unlocked' are boolean; 'key' points to an Item object.
						
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

		# *** attribute methods ***
		def is_not_closed(self):
				return self.is_open is not False

		# *** complex obj methods ***
		def disp_cond(self, active_gs):
				""" Displays object-specific conditions. Used in examine().
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
				creature = active_gs.hero
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
				if not creature.chk_in_hand(self.key) and not creature.hand_is_empty() and creature.get_hand_item().root_name == 'key':
						active_gs.buffer("You aren't holding the correct key.")
						return 
				if not creature.chk_in_hand(self.key):
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
				creature = active_gs.hero
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
				if not creature.chk_in_hand(self.key) and not creature.hand_is_empty() and creature.get_hand_item().root_name == 'key':
						active_gs.buffer("You aren't holding the correct key.")
						return 
				if not creature.chk_in_hand(self.key):
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
				self._contain_lst = contain_lst # list of objects in the container
				""" Containers hold items. Like Door (from which Container inherits), they are ViewOnly and, as a class, can be opened, closed, locked, and unlocked. Also like doors, containers are fundamental puzzle elements. Doors are obstacles to entering rooms. Containers are obstacles to getting items.
				
				Program Architecture:
						In Dark Castle v1/2, containers were just a coding slight of hand. So when I finally coded them for real, I needed to decide in what way a container and its contents were aware of each other. Presumably the crystal_box knew it contained the kinging_scroll... but did the kinging_scroll 'know' it was in the crystal_box? 
						
						Ultimately, I decided on two axioms:
								1) Within the constraints of acceptable performance, data should always live in one and only one location
								2) An object should know about the objects contained directly within it.
						
						From these axioms it becomes clear that containers should know what they contain but items are location 'ignorant': the kinging_scroll has no idea that it's in the crystal_box... or if it gets moved to Burt's hand or to the floor of the throne_room. Along with meeting our 'data in only one place' constraint, this approach also has the benefit of keeping most objeccts simple. There's no need to assign and update an extra 'location' attribute for every object. The down side is that container-type entities (i.e. Containers, Creatures, Rooms) become more complicated - and we end up frequently searching them for their contents. This hierarchal approach to containers is fundamental has been applied to all aspects of the game (e.g. rooms know about the objects within them but know nothing about other rooms outside of them).
				"""

		# *** getters & setters ***
		@property
		def contain_lst(self):
				return self._contain_lst

		@contain_lst.setter
		def contain_lst(self, new_obj):
				self._contain_lst = new_obj

		# *** attribute methods ***
		def chk_in_contain_lst(self, obj):
				return obj in self.contain_lst

		def contain_lst_append(self, item):
				self._contain_lst.append(item)

		def contain_lst_remove(self, item):
				self._contain_lst.remove(item)

		def is_empty(self):
				return not self.contain_lst

		def chk_contain_item(self, item):
				return item in self.contain_lst

		# *** simple obj methods ***
		def	is_container(self):
				return True

		def chk_content_prohibited(self, obj):
				return obj.is_creature()

		def remove_item(self, item, active_gs):
				self.contain_lst_remove(item)

		# *** complex obj methods ***
		def get_vis_contain_lst(self, active_gs):
				""" Returns the list of visible objects contained in the referenced ('self') object
				"""
				if self.is_not_closed():
						node2_lst = []
						[node2_lst.extend(obj.get_vis_contain_lst(active_gs)) for obj in self.contain_lst]
						return self.contain_lst + node2_lst
				return []

		def disp_contain(self, active_gs):
				""" Displays a description of the visible items held by the obj. Used in examine().
				"""
				if self.is_not_closed() and not self.is_empty():
						contain_txt_lst = [obj.full_name for obj in self.contain_lst]
						contain_str = ", ".join(contain_txt_lst)
						active_gs.buffer(f"The {self.full_name} contains: {contain_str}")
						for obj in self.contain_lst:
								obj.disp_contain(active_gs)
				return 

		def disp_cond(self, active_gs):
				super(Container, self).disp_cond(active_gs)
				""" Displays object-specific conditions. Used in examine().
				"""
				if self.is_empty() and self.is_not_closed():
						active_gs.buffer(f"The {self.full_name} is empty.")
				return 

		def open(self, active_gs):
				super(Container, self).open(active_gs)
				""" Extends Door.open(). Upon opening a container, the player's natural question is "What's in it?". Open for containers answers this question whenever a container is opened. If the container is empty that information is displayed as well.
				"""
				if self.is_empty():
						active_gs.buffer(f"The {self.full_name} is empty.")
				self.disp_contain(active_gs)

		def put(self, obj, active_gs):
				""" Puts an Item in a Container.
				
				Implementation Details:
						Container.chk_content_prohibited() is used to limit what can be put in a container and is extended further by PortableContainer and PortableLiquidContainer. For details on why Containers can't hold Surfaces or Creatures and why PortableContainers can't hold PortableContainers, please see the doc_string on node hierarchy under the Room class.
				
				Class Design:
						It might appear that put() could just as well be a method of Item as it is of Container. Code-wise this would certainly work. But what quickly becomes clear when developing verb methods is that the code for testing error cases and buffering terror messages is often longer than the code for executing the command. The corollary to this realization is that we always want to associate a method with its most restrictive noun - which in the case of put() is Container. This means that we don't need to test to see if the target location for put() is a Container - the method simply can't run if it isn't. This same logic applies to other preposition type verb methods like show() and give() - which in theory could be methods of Item but which are more efficiently coded when naturally limited in use by being methods of Creature.
				
				Historic Note:
						put() was the very first preposition-based command in DCv3. After ages of two-word commands it very exciting to be able to type 'put the rusty key in the crystal box' and have a working result!
				"""
				creature = active_gs.hero
				if self.is_open == False:
						active_gs.buffer(f"The {self.full_name} is closed.")
						return
				if self.chk_content_prohibited(obj):
						active_gs.buffer(f"You can't put the {obj.full_name} in the {self.full_name}.")
						return 
				creature.hand_lst_remove(obj)
				self.contain_lst_append(obj)
				active_gs.buffer("Done")

class PortableContainer(Container, Item):
	def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key, contain_lst):
		Container.__init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key, contain_lst)
		"""A container that can be taken.
		"""

	# *** simple object methods ***
	def is_item(self):
		return True

	def is_portablecontainer(self):
		return True

	def chk_content_prohibited(self, obj):
		return super(PortableContainer, self).chk_content_prohibited(obj) or obj.is_portablecontainer()

class PortableLiquidContainer(PortableContainer):
	def __init__(self, name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key, contain_lst):
		super().__init__(name, full_name, root_name, descript_key, writing, is_open, is_unlocked, key, contain_lst)
		"""A container that holds liquids and can be taken.
		"""

	def chk_content_prohibited(self, obj):
		return super(PortableLiquidContainer, self).chk_content_prohibited(obj) or not obj.is_liquid()

class Food(Item):
		def __init__(self, name, full_name, root_name, descript_key, writing, eat_desc_key):
				super().__init__(name, full_name, root_name, descript_key, writing)
				self._eat_desc_key = eat_desc_key # keys to description of eating food (stored in descript_dict)

		@property
		def eat_desc_key(self):
				return self._eat_desc_key

		def eat(self, active_gs):
				creature = active_gs.hero
				creature.hand_lst_remove(self)
				active_gs.buffer(f"Eaten. The {self.full_name} {descript_dict[self.eat_desc_key]}")

class Liquid(ViewOnly):
		def __init__(self, name, full_name, root_name, descript_key, writing):
				super().__init__(name, full_name, root_name, descript_key, writing)
				""" Liquids are ViewOnly objects. You cannot take a Liquid but you can drink() it from a Container.
				"""

		# *** simple obj methods ***
		def is_liquid(self):
				return True

		# *** complex obj methods ***
		def drink(self, active_gs):
				""" Consumes a liquid if it is in a Container that Burt is holding in his hand.
				"""
				creature = active_gs.hero
				if not creature.hand_is_empty():
						hand_item = creature.get_hand_item()
				if (creature.hand_is_empty()) or (hand_item.is_container() == False):
						active_gs.buffer(f"You don't seem to be holding a container of {self.full_name} in your hand.")
						return 
				if self not in hand_item.contain_lst:
						active_gs.buffer(f"The container in your hand doesn't contain {self.full_name}.")
						return 
				hand_item.contain_lst.remove(self)
				active_gs.buffer("Drunk.")
				try:
						active_gs.buffer(descript_dict["drink_"+self.name])
				except:
						pass
				return 

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
				creature = active_gs.hero
				if creature.chk_clothing_type_worn(self):
						active_gs.buffer(f"You are already wearing a {self.clothing_type}. You can't wear two garments of the same type at the same time.")
						return 
				creature.worn_lst_append(self)
				creature.hand_lst_remove(self)
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
