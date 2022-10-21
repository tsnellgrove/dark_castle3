# program: dark castle v3.73
# name: Tom Snellgrove
# date: Oct 21, 2022
# description: base class deffinition module


### import
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

	def is_garment(self):
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



