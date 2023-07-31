To Do List - Dark Castle v3

May 22, 2022

*** Need a new IDE ***
- iPad / offline: Pyto
- Mac Air / Offline: MS VSCode [CHOSEN]
- Cloud / Online: CodeAnyWhere, Cloud9 (AWS)
- Reference article: '5 ways to use Python on an iPad'


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl


*** List Comprehension vs. Generators ***
- List comprehension is used to act on a list but returns a list as long as the original
	- Relevant Link: https://stackoverflow.com/questions/16632124/how-to-emulate-sum-using-a-list-comprehension
- A generator can be used to reduce the values of a list to a single value
	- Example: sum(c.a for c in c_list)
	- Example Link: https://stackoverflow.com/questions/10879867/sum-average-an-attribute-of-a-list-of-objects


*** Inheritance & Method Extension ***
- This solution recommended at this stackoverflow link: https://stackoverflow.com/questions/51249310/attributeerror-super-object-has-no-attribute

## class Child(Parent):
##		def __init__(self): # <== THIS DIDN'T WORK FOR PortableLiquidContainer
##		super().__init__()   # no arguments is almost always best in Python 3 <== THIS DIDN'T WORK FOR PortableLiquidContainer either

##		def do_something(self, some_parameter, next_parameter):
##				super(Child, self).do_something(some_parameter, next_parameter) # name the current class <== BUT THIS WAS VITAL!!!
##				return some_parameter + next_parameter 


*** Var and Method Naming Conventions ***
- general:
	- use singular, not the pluaral form of words in variable names (e.g. use 'object_lst', not "objects_lst')
	- avoid the term 'scope' since there are different scopes for different actions... prefer terms like 'vis'
	- do NOT reference the class in the attribute - the attribute will always appear w/ the class: creature.state vs. creature.creature_state
	- do NOT attempt a rigorous and exhaustive naming convention - this way lies madness and very long vars. Embrace function context! 
	- be biased towards shorter vars; bend naming rules as needed to achieve shorter vars; shorter vars == more readable code!
	- use consistent attribute and method naming across classes whenever possible - especially classes that could be grouped together.
		- This approach allows for easy itteration across an amorphous list of objects.
- classes:
	- prefer generic naming for classes (e.g. Container and Surface vs. Chest and Shelf)
	- class attributes should be named after physical features of the class, NOT their expected data types: hand_lst, bkpk_lst, worn_lst
		- class data types can be grouped via methods whose naming denotes the data type: vis_lst, mach_lst
- attributes:
	- prefixes:
		- 'is' for bools
	- postfixes:
		- 'lst' for lists
		- 'dict' for dictionaries
		- 'str' for strings
		- do NOT use 'obj'; vars are assumed to be obj by default
			- If similar obj and non-obj vars appear in same function, diff the non-obj case: e.g. worn_lst vs. worn_str_lst
- methods
	- prefixes:
		- 'is'/'has'/'can' for methods where no var is passed but a bool is returned; e.g. 'obj.is_item()'
		- 'chk' for a method where you will send an obj and get back a bool
		- 'get' for a method that will return a 'usuable' obj var
		- 'disp' if a method's main purpose is to buffer content
		- 'err' if method's main purpose is to test for an error, throw an error message, and return bool
	- postfixes:
		- 'err' if method's main purpose is to test for an error, throw an error message, and return bool


*** Standard Module Sections ***
Notes:
- Custom sections exist for some complex classes like Room, Creature, and Container
- Doulbe-spacing between module section; single-spacing between class sections

<header = program, name, date, description>
### import
### local functions
### classes
<within a class>
	# *** getters & setters ***
	# *** attrib methods ***
	# *** simple methods ***
	# *** class identity methods ***
	# *** scope methods ***
	# *** display methods ***
	# *** complex methods ***
	# *** general errors ###
	# *** verb error methods ***
	# *** verb methods ***
""" *** Module Documentation *** """


*** standard doc_string sections ***
""" *** Module Documentation ***
	* <ClassName> class:
	- <method_name>() method [<ClassName> class]:
		Overview:
		Implementation Detail:
		Program Architecture:
		Game Design:
		Historic Note:


*** Basic Refactor Steps ***
	- refactor pass - basics
		- shorten / standardize variable names
		- MOVE ASSIGNEMENTS CLOSER TO USAGE!
		- leverage if-then shield pattern 
		- provide 'None' options for variables and 'match' options for Conditions
		- Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}"
		- ensure graceful failure of missing key lookups
		- raise errors on 'impossible' outcomes
		- comment each new attribute
		- add tripple-quote doc_strings for classes, verbs, and in-depth doc
	- refactor pass-advanced
		- auto-gen keys
		- return the conditional comparison value itself (bool)
		- Concatenate strings with '.join' ; 'lst_of_str = ["Hi", "Tom"] ;; my_str = " ".join(lst_of_str)' => "Hi Tom"
		- merge / shorten if-then-else with use of 'and' & 'or'
		- consider removing 'inline variables' that are only used once... just return the assigned value...
		- use enumerate to get index & value! replace 'for i in range(len(lst)): lst_item = lst[i]' with 'for i, lst_item in enumerate(lst):'
		- use 'any' to return boolean rather than for-looping through lists
		- don't need to check for if len(lst) > 0: ;; just use if lst: (Also, bool(None) == False
		- use list comprehension: 'squares = [i*i for i in range(10)]'


*** NOTES ***


##########################
### VERSION 3.78 START ###
##########################

Version 3.78 Goals
- Auto-try unlock(), lock(), attack() with item in hand
- Convert interactive objects to MixIn class architecture (enables future complex obj)
- expand Perch class capabilities (reach concept)
- implement Throne as class SeatMach
- Minor arch tuning


- DONE: review & unify version to-dos

- DONE: auto-try prep 'tool verbs' with item in hand (see below)
	- DONE: for obj-in-hand prep verbs, try in_hand(); error on hand_empty()
		- IDEA: 'tool verbs' == prep verbs using 'with'
		- CANCEL: in interp(), create tool_verb_lst = ['lock', 'unlock', 'attack']
		- DONE: prep section of interp, if no tool & prep given, try contents of hand
		- CANCEL: for hand_empty and 'attack' => fist
		- DONE: for hand_empty => std 'no with' error
		- DONE: need to add "(with the <hand obj>)" to buffer
	- DONE: update help() to explain how this works
	- CANCEL: for Creature prep_verbs, if one creature in room guess that creature, else error
	- CANCEL: for Container / Surface prep_verbs, if one class obj in room guess it, else error

- DONE: sort through remaining notes considerations
	- NOTE: this is a sorted list - these misc notes have been incorporated elsewhere
	- IDEA: Probably want to introduce this when I add size / weight / capacity to items and Recepticles??
	- CANCEL: maybe need a general Creature container (Perch w/ Seat and Bed inheritting? i.e. MixIn?
		- IDEA: class name = Perch (Seat and Bed inherit from Perch)
		- IDEA: perch = Creature container with 'translucent' room access
		- Also need a class for opaque creature container... like a fireplace...
		- names like 'cavity' and 'nook' to describe negative space??
	- CANCEL: stand() => exit()
		- TBD: implement ['exit' = node up too ?] [maybe native = 'exit']
		- TBD: create Seat class exit method ?
		- IDEA: exit auto-brings creature up one node if receptical to exit is not specified?
	- DECISION: no, Creature Containers are a sepcial excpetion; exit() => room.floor_lst

- DONE: Design MixIn approach (e.g. OpenMixIn, LockMixIn, ContainMixIn) to door module classes
	- DONE need to work out max_count vs. max_bulk (or both)
		- IDEA: do we really need HoldMixIn & ContainMixIn ?
		- IDEA: do we really need both ContainerFixedSimple and Surface ? ('prep' = 'in' vs. 'on')
		- DECISION: how container and creature capacity limits will be implemented
			- DEC: weight will not be used - for now the 'small & heavy' / 'big & light' cases are too few
			- DEC: every Item will have a 'bulk' attribute
			- DEC: every container & creature will have attributes: 'max_bulk' and 'max_count'
			- DEC: in addition, containers will each have a 'prep' attribute (typically 'in' or 'on')
			- IMPLICATION: there is no need for HoldMixIn (with a separate version of put)
			- IMP: there is no need for Surface; ContainerFixedSimple is both a 'shelf' and a 'box'
	- IDEA: new name for module with doors & containers (interactive obj; interactive.py)
	- DONE: map out MixIns and inheritance
		- ViewOnly class provides 'name', full_name, root_name, descript_key, writing attributes
		- Creature class adds 'max_bulk' and 'max_count' attributes
		- Item class inherits from ViewOnly and provides take() method
			- 'bulk' attribute is added to Item
			- take() method has checks added for Creature 'max_bulk' and 'max_count'	
		- OpenableMixIn provides 'is_open' attribute and open(), close() methods
		- LockableMixIn provides 'is_unlocked' and 'key' attributes and lock(), unlock() methods
		- ContainsMixIn provides 'contain_lst', 'max_bulk', 'max_obj', and 'prep'; also put() method
			- interp() needs to be updated to reference prep attribute with put() verb
		- DoorSimple = ViewOnly + OpenableMixIn
		- DoorLockable = DoorSimple + LockableMixIn
		- ContainerFixedSimple = ViewOnly + ContainsMixIn
		- ContainerFixedLidded = ContainerFixedSimple + OpenableMixIn
		- ContainerFixedLockable = ContainerFixedLidded + LockableMixIn
		- ContainerPortableSimple = Item + ContainsMixIn
		- LiquidContainerMixIn provides Scope method (and someday verb methods like fill & pour)
		- Flask = ContainerPortableSimple + LiquidContainerMixIn
		- ContainerPortableLidded = ContainerPortableSimple + OpenableMixIn
		- ContainerPortabLockable = ContainerPortableLidded + LockableMixIn
		- Seat = inherits from ContainerFixedSimple; can contain Creatures; 
			- provides enter() and exit() methods
			- new 'in_reach' attribute
		- NEW: to be implemented this pass
			- Bed = inherits from Seat; supports lie(), sleep() => dream() ??
			- Nook = closely related to seat but completely isolated from room... how to implement?
		- CANCEL: 
			- CANCEL: Perch class - not really differentiated from Seat
			- CANCEL: HoldsMixIn provids 'contain_lst', 'max_count' and put() method
			- CANCEL: Surface = ViewOnly + HoldsMixIn
	
- INPROC: implement MixIn architecture in interactive module
	- MOVED: establish 'bulk' attribute for Item
		- IDEA: adding bulk as an attribute to Item is a good example of the need for MixIn classes
		- IDEA: rather than troubleshoot diamond inheritance for ages I will back this out and do MixIn 1st
		- DONE: back out Item, Food, Garment, Weapon, and ItemMach bulk attributes & assignments
		- DONE: move the 'bulk' to-dos to the bottom of the MixIn updates
	- DONE: create interactive.py module
		- DONE: create module file
		- DONE: import Item from item.py and ViewOnly from base.py
	- DONE: create OpenableMixIn class with is_open attribute and setters & getters
		- DONE: create attribute and display methods
		- DONE: create verb methods ( open() and close() )
		- DONE: create DoorSimple class
		- DONE: create screen_door of class DoorSimple
		- DONE: place screen_door between entrance_hall and antechamber to test DoorSimple
			- DONE: think about how open_err() and close_err() should distinguish between obj with lids vs. obj w/ lids & locks
			- IDEA: I think I need is_openable() and is_lockable() ??? So I can eventually eliminate is_door() ???
			- DONE: address existing is_door() vs. is_door_simple() case for open_err() and close_err()
		- DONE: create is_openable() in OpenableMixIn and Invisible() and add to open_err() & close_err()
		- DONE: create is_lockable() in Invisible() and add to open_err() & close_err()
		- DONE: introduce is_container() in Invisible(), open_err(), close_err()
		- DONE: for open(), sort out if is_containter() => is_contain() text... bake in "{} is empty"
		- DONE: clean up comments
	- DONE: create LockableMixIn class
		- DONE: create LockableMixIn class w/ attributes & setters & getters
		- DONE: create attribute, identity, and display methods
		- DONE: create verb methods ( lock() and unlock() )
		- DONE: create DoorLockable class
		- DONE: update err_verb methods 
		- DONE: convert Door object front_gate to LockableDoor class
		- DONE: convert Door object iron_portcullis to LockableDoor class (test with Mach)
	- DONE: create ContainsMixIn class
		- DONE: create ContainsMixIn class w/ attributes: contain_lst, max_bulk, max_obj, & prep 
		- DONE: create setters & getters
		- DONE: create attribute, identity, scope, and display methods
		- DONE: revert can_contain() to is_container()
			- IDEA: there's a lot of code that looks for is_container - best to re-use it
			- ISSUE: wrong error messages with open / close & unlock / lock
			- DONE: had to add is_openable() and is_lockable() identities to Door class
		- DONE: create verb methods ( put() )
		- DONE: update err_verb method
			- DONE: fix put() capacity check (introduce can_contain_temp() )
		- DONE: update interp() to reference prep attribute
		- DONE: create ContainerFixedSimple class
		- DONE: convert Surface obj shelf to ContainerFixedSimple class
			- DONE: troubleshoot enter room issue
			- DONE: debug 'put key on shelf'
			- DONE: sort out 'empty' condition for 'x shelf'
			- DONE: sort out use of Container.prep in interp()
		- DONE: clean up comments!
	- DONE: ContainerFixedLidded
		- DONE: create ContainerFixedLidded class
		- DONE: import ContainerFixedLidded into mk_def_pkl()
		- DONE: create cardboard_box of class ContainerFixedLidded for testing
		- DONE: add to object pickle!
		- DONE: add cardboard_box to Entrance
		- DONE: testing! (worked on first try - even openable has_cond() !!)
	- DONE: ContainerFixedLockable
		- DONE: create ContainerFixedLockable class
		- DONE: import ContainerFixedLockable into mk_def_pkl()
		- DONE: convert crystal_box to ContainerFixedLockable class
		- DONE: testing!
	- DONE: maybe now is the time to introduce Item bulk
		- IDEA: temporarily remove PortableContainer classes & obj from game and re-introduce as MixIns
		- DONE: update classes
			- DONE: Item
			- DONE: Food
			- DONE: Garment
			- DONE: Weapon
			- CANCEL: PortableContainer
			- CANCEL: PortableLiquidContainer
			- DONE: ItemMach
		- DONE: temporarily remove item-container classes and obj from game
			- DONE: comment out PortableContainer classes
				- DONE: PortableContainer
				- DONE: PortableLiquidContainer
			- DONE: comment out PortableContainer obj def
				- DONE: glass_bottle
				- DONE: black_suitcase
			- DONE: remove Portable objs from rooms & creatures
				- DONE: entrance (black suitcase)
				- DONE: burt inventory (glass_bottle)
		- DONE: assign 'bulk' attribute to all (remaining) Item obj (including kinging_scroll)
		- DONE: test bulk assignment
		- DONE: update put_err() to check for max_bulk capacity limits
		- DONE: test max_bulk limit
		- DONE: move current_contained_capacity to container method and call from put_err()
		- DONE: implement current_contained_capacity with list comprehension

	- DONE: ContainerPortableSimple
		- DONE: create class	
			- DONE: create ContainerPortableSimple class
			- DONE: import ContainerPortableSimple into mk_def_pkl()
		- DONE: deal with bulk
			- DONE: decide how to handle bulk for portable containers when they are holding obj
				- DECISION: portable container bulk = container bulk + contents bulk (i.e. like weight)
			- DONE: update put() verb method to add Item bulk for Portable Containers
			- DONE: update ContainsMixIn.remove() method to subtract Item bulk	
		- DONE: create test obj
			- DONE: created small_barrel of class ContainerPortableSimple
			- DONE: add to object pickle!
			- DONE: add small_barrel to Entrance
			- DONE: testing!
				- FINDING: 'put barrel on shelf' error
				- DONE: need to make bulk decrement remove a method extension in ContainerPortableSimple
				- DONE: move bluk increment on put() a method extension in ContainerPortableSimple
		- DONE: create debug verbs: weight() and capacity()
			- DONE: weight() in Item() and weight_err() in Invisible
			- DONE: capacity() in ContainerMixIn and capacity_err() in Invisible (i.e. capacity remaining)
			- DONE: 'help debug' mode that only works in debug mode ("The first rule of debug mode...")
				- DONE: in interp() , secret_verbs => debug_verbs ; list debug_verbs in 'help debug'
		- DONE: consider renaming bulk to weight
			- DONE: interactive(), invisible(), item(), mach()
			- DONE: testing!
		- DONE: comment clean up for all modules!

	- DONE: ContainerPortableLidded
		- DONE: create class ContainerPortableLidded
		- DONE: import ContainerPortableLidded into mk_def_pkl.py
		- DONE: create red_shoebox test object
		- DONE: add red_shoebox to obj pickle!
		- DONE: add red_shoebox to Entrance!
		- DONE: add restriction to ContainerPortableSimple to prohibit portable containers in same
		- DONE: test
		- DONE: try basing ContainerFixedLockable on ContainerFixedLidded

	- DONE: ContainerPortabLockable
		- DONE: create ContainerPortabLockable
		- DONE: import ContainerPortabLockable into mk_def_pkl.py
		- DONE: convert black_suitcase to ContainerPortabLockable class
		- DONE: put black_suitcase in Entrance
		- DONE: test!

	- DONE: short-term fix for LiquidContainer
		- DONE: liquid container
			- DECISION: maybe now is the time to convert glass bottle to Enchanter jug??
			- DONE: earthen_jug to be of class ContainerPortableSimple
			- DONE: make earthen_jug.max_weight = 0.5, max_obj = 5
			- DONE: add to burt inventory
			- DONE: add to mk_def_pkl() master obj list
			- DONE: add description
			- DONE: test!
		- DONE: convert Liquid class to inherit from Item
			- DONE: create Liquid class that inherits from Item
			- DONE: create drink() method
			- DONE: import new Liquid into mk_def_pkl
			- DONE: convert obj fresh_water to new Liquid; set fresh_water.weight = 0.5
			- DONE: add fresh_water to earthen_jug
			- DONE: test !
			- DONE: misc_class_deff.py module moved to /legacy
		- DONE: update drink method to prep verb: 'drink X' to 'drink X from Y' (guess if bottle in hand)
			- DONE: add obj attribute to drink() method
			- DONE: ref obj attribute in drink() remove command
			- DONE: add drink to interp() prep verbs with prep = 'from'; guess on creature hand
			- DONE: add obj to drink_err() attributes and add errors for non-container obj or no liquid
			- DONE: test!
			- DONE: custom 'moat' error for drink()
			- DONE: move drink_err() to prep section
			- DONE: fresh_water => well_water (update all refs in mk_def_pkl)
			- DONE: updated help() info for 'prepositions'
			- DONE: test!
			- DONE: clean up comments in interp(), invisible(), item()

	- DONE: Seat class
		- DONE: create parity Seat class in Interactive module
			- DONE: create class Seat which inherits from ContainerFixedSimple
			- DONE: chk_content_prohibited() returns obj.is_seat() (i.e. Creature class allowed)
			- DONE: add in enter() and exit() methods from door
			- DONE: convert test_chair to Interactive.Seat class
			- DONE: test!
		- DONE: define in_reach behavior
			- IDEA: in_reach enables a seated creature to access receptical contents as if standing
				- IDEA: the idea is that the surface / container / floor is close to the Seat
					- IDEA: this becomes important as the Seat will be the basis for Vehical...
					- IDEA: and many vehical puzzles hinge on a moving vehical passing close to a takable obj
					- IDEA: e.g. the buoy in the river in Zork
				- IDEA: in_reach_lst is a list of recepticles which creature in Seat can access contents
					- IDEA: however, the creature in the Seat cannot access the recepticle itself
					- IDEA: if in_reach_lst includes room_name then floor_lst is accessible
				- IDEA: there needs to be a description update when seated to let player know about access
		- DONE: in_reach_lst attribute
			- DONE: create Seat in_reach_lst attribute and update test_chair obj w/ wooden_shelf in_reach
			- DONE: chk_obj_in_reach()
				- DONE: Creature method
				- DONE: update invisible() std_err to use new in_reach() method
				- DONE: test!
			- DONE: chk_wrt_in_reach()
				- DONE: Creature method
				- DONE: update invisible() std_err to use new in_reach() method
				- DONE: test!
			- DONE: clean up comments
			- DONE: expand is_obj_in_reach() to include Seat in_reach_lst attribute
				- DONE: for is_container() => contain_lst
				- DONE: for is_room() => floor_lst
				- DONE: for is_door() => Door
			- DONE: test!
				- DONE: is_container()
				- DONE: is_room()
				- CANCEL: is_door()
					- FINDING: old is_door() refs in open_err & close_err causing errors
					- IDEA: switch to is_openable()
				- DONE: is_openable()
					- DONE: test
			- DONE: expand is_wrt_in_reach() to include Seat in_reach_lst attribute
				- DONE: for is_container() => contain_lst
				- DONE: for is_room() => floor_lst
				- DONE: for is_openable() => Door
				- DONE: test
			- DONE: update UI to enable player to know what is in reach when seated
				- DONE: establish UI goals
					- IDEA: alert player to in-reach under 2 circumstances:
						- IDEA: 1) when entering Seat
						- IDEA: 2) when examining room / 'look'ing
				- DONE: create Creature display method to show in_reach()
				- DONE: update enter() method to display in_reach
				- DONE: update examine() method to display in_reach if contained (and if title => room ?)
				- DONE: retune in_reach() methods using ViewOnly and elif
				- DONE: test!

	- DONE: clean-up from old Door class
		- DONE: clean-up is_door(), is_surface(), can_contain_temp(), and is_portablecontainer()
			- DONE: is_surface()
				- DONE: invisible()
			- DONE: is_portablecontainer()
				- DONE: invisible
			- DONE: can_contain_temp()
				- DONE: interp()
				- DONE: interactive()
				- DONE: invisible()
				- DONE: test!
				- DONE: clean-up comments
			- DONE: is_door()
				- DONE: interactive()
				- DONE: invisible()
				- DONE: test!
				- DONE: clean-up comments
		- DONE: door doc_strings => interactive()
		- DONE: door() module to legacy folder
		- DONE: ensure that no room descriptions indicate 'standing' in room (since you could be sitting)
		- DONE: update SurfaceMach to ContainerFixedSimpleMach
		
	- DONE: doc strings
		- DONE: update existing door() module doc_strings
			- DONE: overview
			- DONE: OpenableMixIn
			- DONE: LockableMixIn
			- DONE: ContainsMixIn
			- DONE: Door noun classes
			- DONE: ContainerFixed noun classes
			- DONE: ContainerPortable noun classes
		- DONE: seat doc_strings
			- DONE: doc_string for in_reach
			- DONE: address Seat as Creature Container (vs. Room node discussion)
			- DONE: Seat (nested-room) "translucent" scope (can't interact w/ Seat itself)
			- DONE: Seat as precursor to Vehical
			- DONE: Nested Rooms can't be nested (no chairs on stages)
			- DONE: Perch = translucent, Nook = opaque
			- DONE: weight only vs. weight + volume (encumberance)
			- DONE: best practices - max_obj for surfaces vs. max_wight for containers
			- DONE: nook gets light from room
			- DONE: Seat vs. Perch... perhaps Perch is more generic?? Seat to include under & behind ??
			- DONE: method write-up (synonyms, exit special case of std_err)

	- INPROC: general Interactive class clean-up
		- DONE: should identity methods only apply to noun classes, not MixIns? [DECISION = NO]
		- DONE: create 'weight' verb to return bulk of Item (only usable in debug mode) ??
		- DONE: fix ContainerFixed inheritance... Lidded & Lockable should inherit from Noun, not MixIns
		- DONE: autogen text based on Seat obj.descript
			- DONE: enter()
			- DONE: take(), wear(), drink(), eat()
			- DONE: show(), give()
		- DONE: can I get rid of Openable() method is_not_closed()
			- DECISION: yes, only exists because in Door class, is_open could take value None
			- DONE: replace obj.is_not_closed() with obj.is_open
				- DONE: ContainsMixIn.get_vis_contain_lst()
				- DONE: ContainsMixIn.disp_cond()
				- DONE: ContainsMixIn.disp_contain()
				- DONE: def
			- DONE: test
			- DONE: clean up comments		
		- DONE: group "empty" response with contains rather than condition
			- DONE: elim ContainsMixIn has_cond()
			- DONE: add "empty" option to has_contain()
			- DONE: Test
			- DONE: clean up comments
		- DONE: in debug mode, postfix Invisible errors with [INVIS]
		- IDEA: should MixIns like OpenableMixIn should have their own examine() states? like has_contain() ?
			- DECISION: "no" for now - not until actually needed - but does sort of make sense
		- DONE: clean-up comments
		- DONE: create an is_contain_vis() meth for ContainsMixIn
		- CANCEL: understand "fix display meth use of is_closed() "
		- DONE: consider whether in_reach methods would be better off in Seat rather than Creature
			- DECISION: Ultimately, we want to know if a Creature can reach an obj.
			- DEC: Instead of checking if a creature is contained and then checking in_reach of seat...
			- DEC: is better to simply check reach if in_reach to Creature and let Creature check seat cond
		- DONE: consider moving more of in_reach logic into class methods (linked to contain methods)
			- CLARIFICATION: i.e. eliminate checking if is_contained before checking in_reach
			- DECISION: For now, leave Invisible std err checks as is
			- DEC: Don't want to recreate and amalgamate "is vis" routines
			- DEC: Also, want in_reach() to funcition independently of is_contained()
		- TBD: probably time for a general refactor review of ContainsMixIn()

	- TBD: finish the max_weight deployment
		- TBD: assign 'max_weight' and 'max_count' to Creatures
		- TBD: create current_carried_cappacity() method for Creature
		- TBD: update take() to check for 'max_bulk' 
		- TBD: assign 'weight' attribute to Creatures


	- IDEA: in interp(), what about making prep check similar to put() for all prep verbs
		- IDEA: could have a prep attribute for each prep verb
		- IDEA: in interp(), have a list of all possible preps and use list to break sentence

- TBD: instantiate Creature Containers in actual game
	- TBD: decide - should creature.is_contained and creature.get_container be ViewOnly methods?
	- CANCEL: switch creature.stand() => creature.exit()
	- TBD: Throne
		- TBD: For throne, crystal_box is in_reach? Update room / throne text to indicate this?
		- TBD: instantiate throne as obj of class SeatMach
		- TBD: Description when 'sit': "feels out of kilter - pushed or pulled out of alignment"
		- TBD: autogen text would need to be conditional (i.e. before & after broach dispensed)
			- IDEA: add auto_gen description to over-ride (like messy_handwriting)
			- IDEA: or maybe base auto_gen key on descript_key and update that?
		- TBD: clean up test obj (e.g. test_chair, black_suitcase)
	- TBD: maybe a Bed in the Main Hall?
	- TBD: maybe a fireplace in the Main Hall (class = Nook)? Or better yet, Alcove as class Nook?
	- Stone Coffer => no-lid box ?
	- move test obj into dedicated section; instantiate but don't place





*** Unify Notes ***
*** Plan for interpreter update ***


- Long Term Pondering:
	- the whole 'hand' concept is looking increasingly dodgy... too much inventory mgmt...
	- maybe time to bite the recursive bullet and just allow portable containers in portable containers?

- decide if interactive() class objects should eventually have noun identities (e.g. is_door() )

- Liquid handling
	- INPROC: Research IF liquids
		- DONE: Infocom
			- Zork: Glass Bottle 
				- has one 'quantity of water'
				- bottle must be held to be drunk
				- bottle must be openned to be drunk
			- Enchanter: Jug
				- has multiple quantities of water
				- jug has no 'cap': "The jug has no cover. It can't be openned or closed."
				- must be at least a little 'thirsty' to drink water
			- Other uses (in Zork):
				- Water can be poured on flame to put it out
				- Water can be poured on the heated bell to cool it
		- TBD: how does TADS do it??
	- INPROC: Long-term Liquid plans
		- Liquid class
			- The primary liquid in the game will be water
			- An important point of awareness is that 'water' (unlike all other nouns) cannot be guaranteed to be unique
			- Main liquid verbs = drink(), pour(), fill()
				- where 'Y' is a Liquid and 'X' and 'Z' are containers / bodies of water
				- drink() : 'drink Y from X'
					- Liquid method
				- pour() : 'pour X from Y in / on Z'
					- ContainerPortableSimple method
				- fill() : 'fill X with Y from Z'
					- ContainsMixIn method
			- - IDEA: Advanced verbs: mix(), stir(), shake()	
		- Non Liquid class properties related to liquids
			- If water is poured in or on an object it has an effect:
				- no special results (if the obj is a Container then it holds the water)
				- Obj unimpacted but water 'evaporates'
				- Obj is ruined / disolved / rendered illegible (e.g. paper note); water "evaporates"
				- Heated obj is cooled (Zork example; future)
				- Flame is extinquished (Zork example; future)
				- note that these effects are properties of the objects - NOT the liquid class
			- Implementation:
				- for ViewOnly class and below, need an attribute: liquid_result
					- defines what happens to the obj when it contacts liquid
					- also defines what happens to the liquid when it contacts the obj
		- Special case of bodies of water
			- does an object sink or flat?
			- this can get complicated 
				- maybe keep the Entrance 'well' to a shallow rainwater-fed pool
				- test with Enchanter spring
		- Special case of immersion
			- You should be able to swim in water and diver under water
			- Breathing limits will apply
			- This will mostly be independent of Liquids... 
				- but anything with a 'ruin' liquid_result == 'ruin' should be destroyed by swimming

- TBD: static_gbl => tupple

- TBD: Given that creatures will be contained:
	- need to embrace a node-based awareness of creature location
	- need to embrace the use of recursion on methods like remove()
	- Apply this to concepts like drop() and stand() / exit()
	- DECISION: alternatively, just treat creature-containers as special exceptions

- TBD: the future list - future interactive obj updates / features to be implemented
	- framework for complex obj to contain sub-elements (e.g. drawer + surface + under == desk)
	- Could also have UnderMixIn and BehindMixIn
	- TBD: for UnderMixIn - need to include bulk capacity for negative space
	- would need to deal with the wording 'look under' and 'look behind'
	- 'look under' adds contents to room.feature_lst
	- additional 'under' commands = 'put under' and 'reach under'
	- for MixInHole have commands 'look in' and 'reach in'
		- can a 'hole' be dark if the room is light?
	- TBD: enable the 'behind' preposition (with multiple varients of obfustication)
		- IDEA: minor_behind = you can see but not reach
		- IDEA: moderate_behind = can see some
		- IDEA" major_behind = can't see
		- Presumably, all 3 flavors of behind impact availability of obj in room list
		- TBD: put the control_panel behind the goblin (check TADS implementation)
	- IDEA: 'hole' = contain, opaque from room, no light
		- 'nook' = 'hole' that can contain Creatures
		- 'under' = opaque from room but no lighting issues
		- use 'take from under' for 'under'
		- use 'reach in' for 'hol'
		- need to enter() 'nook' to get contents
	- IDEA: what to do on container (or other) loss of light?
		- e.g. put lantern in box, close box (no stuck)
		- had thought about lighting up box from interiour - but wouldn't work for switch
		- is safe to actually turn off lantern - because anything in your hand can still be accessed...
		- so alternate idea is that hedgehog has to come rescue you
		- but at least one inventory item gets scattered (hedgehog shrug)

- TBD: "what would your mothter say" error to "What would your Nana say?"

- TBD: make creature obj data more atomic
	- TBD: create weapon() method to provide adj & adv (vs reading weapon_dict via attack() )
		- IDEA: obj should be a black-box
	- TBD: same idea for 'can't attack error' for attack() in invisible(); should be creature() meth

- IDEA: think through code vs. data separation for static text
	- IDEA: imagine future adventure creation tooling where I update descriptions via a web front end
	- IDEA: I won't want all the description in a DB - that's too much overhead...
	- IDEA: But I will want all descriptions in one big centralized dictionary for ease of access & update
	- IDEA: to this end, consider the following:
		- TBD: move interp() help_dict back to static_gbl() descript_dict
		- DONE: consolidate val_err_dict from validate() back to static_gbl() descript_dict
		- TBD: consolidate dir_err_dict from invisible() back to static_gbl() descript_dict
		- TBD: consolidate static_dict into descript_dict
	- TBD: doc_string - error messages are hard to update - so I want them to be as generic as possible!

- INPROC: review TADS3 terms for Description and preposition

- IDEA: interesting updates for food & bulk
	- require eating
	- enable Water to be drunk in small amounts (multiple servers per filled bottle)
	- enable same partial consumption for bread loaf (calls back to Enchanter)
	- Make sips of water / bites of bread the one frational bulk amount in game
	- Enables interesting weight puzzle (4 gallons from 3 & 5 gallon buckets)
	- Maybe stale_biscuits => 3 biscuits in paper package (Nana sword & key logo; better than McV ref?)
	- Perhaps for bulk puzzle, have a Pywrong beaker - extremely fragile - breaks if put in pack or dropped

- IDEA: 'talk to creature' format:
	- IDEA: 'Ask X about Y'
	- IDEA: 'Tell X about Y'
	- IDEA: Say 'Z'
- IDEA: next interp() goals:
	- IDEA: noun synonyms (different than abreviations)
	- IDEA: global verb synonyms
	- IDEA: simple prep verbs ('sit_in')
	- IDEA: basic interp features: 'take all', 'again', 'wait'
	- IDEA: address 'I can't see a x_y' error
- IDEA: introduce a vs. an
- TBD: read() of obj w/ writing => "On the {obj}, written in {wrt}, you see: '{txt}'..."
- TBD: read() if no writing on obj => "There's nothing written on the {obj}."
- TBD: examine writing => "The {writing} reads as follows: n/"
- TBD: should it be possible to show() and obj of class Writing or ViewOnly ??
- TBD: should "put key in moat" do more? what about "enter moat"
- TBD: figure out 'behind' prep for case of control panel in alove behind goblin
- TBD: enable 'show writing to creature' is writing is on an item Burt is holding
- TBD: stand() as Perch synonym for exit()
- TBD: exit() should apply to chairs and doors => move to Perch / Nook class
- TBD: should have 'go in gate' and 'enter gate' as synonyms for 'go north' from entrance? (doors & rooms ??)
- TBD: update get_hand_item() to return None if hand_list is empty
- TBD: sort out active_gs.get_room() => move to .map & std w/ map.get_obj_room()
- TBD: implement global verb synonyms for 'sit in' or 'sit on' == enter()
	- TBD: also want to enable 'go in' and 'go out' of chair
- IDEA: consider converting Writing to Decorations (examine() vs. read() )
- TBD: create a version just for interp() updates and gather all interp updates there!!
- IDEA: verb synonyms per obj with 'move' as a broadly used and variable synonym??
	- verb synonuyms linked to class / class method?
	- perhaps additional, optional cusotm verb synonyms as an obj attribute?
- Do I need a gs.Gramarian class to deal with recurring display issues around pronouns and plurals?
	- e.g. pronoun_tobe(creature) => 'You are' or 'The <creature.full_name> is'
	- e.g. article_plural(obj) => 'a Grimy Axe' or 'Water' or 'an Apple'
	- maybe plural_dict is a local dict in the Gramarian class?
	- Or maybe a better class name is just Display (???)
	- Division of labor: player text => commands == Interp; obj => player response == Output
	- could put some recurring dispaly routines here (obj_lst => str_lst and such) ??
	- Display could also hold buffer commands???
	- Another possible class name == Output ???
	- Leaning towards Output... this helps distinguish from all the verb-linked Disp methods

- TBD: what about cases where I want a modular machine to operate despite an error
	- IDEA: e.g. 'go north' in antechamber triggers goblin
	- IDEA: i.e. should it ever be possible to override an error? If so, then how?
	- IDEA: the 'open portcullis' case is a special problem here - it will tell Burt it's locked...
		- IDEA: but the Goblin should attack before Burt can touch the Portcullis
	- IDEA: creation of a pre-validate() module called interupt() that can over-ride errors
	- IDEA: implication here is that modular machines should be designed so that it is easy to trigger & run them from interupt()
	- IDEA: the idea here is that narrative shoudld be able to trump simulation rules if desired (but it may take extra work)
	- DECISION: use fake_door for now and swap on goblin death
	- RECONSIDER: 'take axe' case is not easy to fake out... maybe I do need an interupt() module after all??
- TBD: update take_err() creature check - allow hostile reaction if burt attempts to take goblin axe?

- TBD: Description updates:
	- TBD: hedgehog updates
		- describe as "stallwart"
		- Have the hedgehog think burt is playing if he attacks with a non-weapon; starts making wax-on, wax-off motions with paws
		- Upate water_bottle to Enchanter jug
		- Update shiny_sword to Zork I elven sword
	- TBD: Updatate the trademark on the stale_biscuits... 
		- perhaps the biscuits say "Nana's" - or better yet, have a sword-and-key emblam on them?
		- backstory of Nana fondly feeding hedgehog biscuits back when she was at the castle?

- TBD: text UI updates:
	- TBD: sort out 'can't drop fist or brass_lantern issue
	- TBD: change backpack and worn lists to include 'a' and 'an'
		- IDEA: convert plurals to singulars for this???
		- IDEA: (given that there is water in the game maybe all singlulars is impossible?)
		- IDEA: maybe a txt_handling() module with a disp_lst() func that takes care of 1) "x", "x & y", "x, y, & z"; 2) 'a' or 'an'; 3) plurals
	- TBD: sort out approach to plurals
		- 1) perhaps this becomes a ViewOnly attribute??? (don't like this - way too many un-used cases of attribute)
		- 2) possibly ItemPlural class inherits from Item and has method is_plural() which returns True ??
		- 3) could just have a plural_tuning_lst in the txt_handling() module that checks for known plurals as a one-off?
			- `Note: the problem with defining plurals in classes is, what if I want to establish plurals for a non-obj (e.g. a path)
		- Maybe apply 'xxy' prefix on text list if plural??
	- TBD: drop node 3 (portable_containers in containers) disp?
		- TBD: can burt know about node 3 items he hasn't 'seen' in this game?
		- TBD: play through Zork kitchen to test out
	- TBD: glass_bottle to jug_from_enchanter

- TBD: misc updates:
	- TBD: make backpack a true container???
	- TBD: create a centralized doc file
	- CANCEL: reconsider showing Receptacle contents on look... maybe too much data? What does Zork do? Restrict to explicit examine??
	- TBD: hunger & thirst become Creature conditions to examine??
- TBD: learn how to use VS Code word wrap and other features for Python
- IDEA: maybe I should call validate() again between pre_action() and cmd_exe() and then again between cmd_exe() and post_action() ?


##########################
### VERSION 3.7x START ###
##########################

Version 3.7x Goals
- rename active_gs to gs
- modularize remaining GameState class and declarations (???)
- create a class for descriptions

- TBD: rename active_gs => gs
- TBD: perhaps Map, Score, and Descript are classes w/ static dicts in mehod / class and actual obj in gs attributes
- TBD: refactor buffer type commands into gs.io
- Refactor dicts
	- TBD: refactor active_gs.map
		- gs will have map as an attribute
		- subclass map_dict
		- use __getattr__ and __setattr__ methods to make dict accessible as obj
		- instantiate in start_up() and save in pickle in case map someday changes during game (fun idea)
		- methods:
			- next room
			- use dict keys to search for item in game world (see score() )
			- return room burt is in
- TBD: refactor descript_dict (=> static_dict), autogen_dict (new) and dynamic_dict to Descript class with descript instantiation
	- TBD: unify descript approach: how to make get_descript_str() [which has a default response] work with auto-gen descript keys [which depend on the possibility of failure]? Need a consistent solution
	- call with key and return string; will look like gs.descript(key)
	- all autogen keys & vals live in autogen_dict and are pre-fixed with "ag_" (note: the defining feature of autogen keys = try: buffer() )
		- Can autogen key try be incorporated into Descript method??
	- static_dict and autogen_dict live in class; dynamic_dict is lone class attribute and is instantiated in mk_def_pkl()
	- Use guard pattern and check in this order
		- 1) in dynamic_dict
		- 2) starts with "ag_" => autogen_dict (no "try", allow failure)
		- 3) try static_dic except f"the {obj.full_name} is simple indescribable"
	- CANCEL: create dict_class_def.py w/ StaticDict and __getattr___ (no set)
		- CANCEL: test w/ descript_dict => start with version 
		- can compound noun methods be created?
		- think abour 'source' and 'desination'... e.g. for take(), source = is_item in <room>.obj_scope; destination = <creature>.hand_lst
		- need to do a detailed mapping of what is required for success in each noun_class() method
		- this would allow give() to become a noun class method... essentially a take() initiated by burt
		- likewise, show() becomes an examine initiated by burt
		- TBD: change goblin re-arm result to take() rather than put_in_hand()
		- maybe each Creature has its own description list?
			- desc list as creature attribute ???
		- with a default examine() response similar to "the X is not interesting"
	- TBD: auto-gen keys
		- TBD: consider auto-gen keys for all verb methods (probably not)
		- TBD: Organize auto-gen keys together
		- TBD: consider creating a separate dict for autogen keys
- TBD: refactor score
	- TBD: determine max_score from summ of all possible scores?
	- TBD: score = class with object being attribute in gs
	- TBD: print_score() a method of the Score class
	- TBD: instead of a dict of score achievements w/ T or F, just have a list of score achievemnts achieved
	- TBD: link front_gate score to opening door
- TBD: refactor hero to gs.hero
	- TBD: get_room() method belongs to this class ?? (or pass active_gs to active_gs.map and move get_room there ??)
- TBD: refactor buffer and caching to gs.io
- TBD: refactor GameState and dicts in static_gbl() with dunder methods (__getattr__ and __setattr__ ; see email to self on Aug 2, 2022)
- TBD: active_gs => gs renaming; point to same obj to start with ??
- TBD: active_gs holds list of smaller game state components? clock + scoreboard + map + printer ??
- TBD: modularize mk_def_pkl() and active_gs ( how about gs.sboard.get_score() )
- TBD: end() => gamestate ???
- does creature_state really have any value? Maybe build hedgehog state machine before pulling the plug on this one
	- Could simplify 'give', remove description updates from give, and instead implement them as part of state machine?


##########################
### VERSION 3.78 START ###
##########################

Version 3.78 Goals
- refactor app_main() modules


- IDEA: score() and end() should be between post_action() and auto_action() [i.e. between move 'n' and 'n+1']
- TBD: interpreter - should all nouns be singular? Can 'a' vs. 'an' be fixed?
- TBD: final clean-up
	- TBD: tune goblin and hedgehog text; maybe add a faded poster of ancient and unreasonale regulations to the antechamber wall?
	- TBD: fix eat_biscuits_warning so that it no longer lives in just entrance and main_hall and no longer triggers when biscuits not in hand
			- suggest making eat_biscuits_warning universal and enabling success feedback loop for cmd_exe
	- TBD: refactor active_gs. scope / mach_scope
			- Use list comprehension to eliminate for-loop? (link: https://medium.com/self-training-data-science-enthusiast/python-list-comprehensions-use-list-comprehension-to-replace-your-stupid-for-loop-and-if-else-9405acfa4404 )
	- how can I make descript_dict modular so that other dicts can be chosen (if I want to temporarily tell adventure from another persepctive)
	- DECISION: writing perspective
		- With burt being a creature and all methods being rewritten to work with the Creature class, we have a choice
		- in theory, any creature could be used to play the game - and each might have its own description_dict
		- this would be fun for a short session in a single room but is not practical for extended play
		- realistically, nearly all descriptions will be from burt's perspective
		- but in some cases creatures will use methods to take actions and burt will *obeserve* there actions
		- this should be enabled by mode = 'exe_creature'
- TBD: refactor app_main() modules
- TBD: doc_string about why errors and actions must be clearly delineated (e.g. and error cannot change gamestate)
- TBD: considers re-distributing not-in hand & read errors back into verb methods ???


##########################
### VERSION 3.79 START ###
##########################

Version 3.79 Goals
- refactor remaining app_main chain: interp, pre_action, cmd_exe, post_action, auto_action, score (??), end (?)
- Interp deep dive including better solution to prep checking ('put in' vs. 'put on')


##########################
### VERSION 3.80 START ###
##########################

Version 3.80 Goals
- enable all verb methods for non-burt creatures

- TBD: doc_string about future 'silent_exe' for symetric creature commandsv
- TBD: test with test_frog holding test_box (PortableContainer) holding red_mcguffin Item
- TBD: tune pronouns
- IDEA: errors are only for burt
- IDEA: auto-gen descriptions (e.g. drink, eat, wear, sit) are only for burt
- TBD: doc_string on 'semi-symetric' methods
- TBD: enable non-burt creature use of all verb methods 
- TBD: how should creature be passed to Conditions & Results?
- TBD: how to deal with error messages for non-burt creatures (e.g. test_frog walks into door)
- IDEA: alternatives for how to to auto-move non-burt creatures: dir_lst, room_lst, room_dir_dict
- IDEA: for food, maybe have the biscuits take 3 turns to eat... but if burt eats some he gets less time to grab the sword... 
	- IDEA: maybe don't need warning so much... just keep describing them as tasting worse and worse? Food consistent within creatures?


##########################
### VERSION 3.81 START ###
##########################

Version 3.81 Goals
- Clean up machine, warning, and timer coding
- Create / update program documentation

- TBD: Machine coding clean-up
	- TBD: Machine 2.0 improvement ideas:
		- BaseCond => always check state
		- BaseResult => always do a buff_try()
		- Can we create a general purpose Dispenser machine - for use with Crown and Broach?
		- Do we really need to test for goblin in antechamber??? (will the goblin ever move)
		- Have simple, single-test / single-action 'Primative' Conditions and Results: prim_cond and prim_result
		- Composed Conditions & Results: comp_cond / comp_result == AND / OR of multiple primatives
		- All results capable of Buffering (rename Result classes appropriately)
		- if no conditions == True then default Result = nothing happens (no need for pass_result)
		- Establish switch triggers such that timer as trigger is more natural
		- Generalize in-hand vs. not-in-hand Condition (single primative)
		- Generalize creature-has-item vs. creature-does-not-have-item Conditions (single primative)
		- Establish clearer nomenclature for temp variables that will be fully assigned at end (e.g. 'royal_hedgehog-*temp*')
		- each 'primitive' cond only tests for *one* thing (but state of that thing is an attribute to be matched)
	- TBD: de-dup warning and timer classes
		- IDEA: after cleaning up some typos it appears that "selective inheritance" just isn't a thing. What now?
		- IDEA: this makes sense... in all other cases I inherit from simple parents to more complex children
		- IDEA: WarnClass is simpler... so it should be the parent
		- IDEA: Actually - how about a TrigDetectMixIn that is inherited by both WarnClass and MachineMixIn and only has trig_check method?
		- IDEA: A MixIn of a MixIn seems over-complicated... 
		- IDEA: perhaps right now I'll just make an independent class with duplicate trig_check code base
		- IDEA: as a future activity, I can look to de-dup in a more elegant fashion
	- more Modular Machine ideas:
		- Modular Triggers? (named after intent; match cond, result, & mach)
		- Primative Conditions (named after condition) [always include single attribute & value] 
		- Compound Conditions [and / or) (named after intent; match mach, result, & trig) {trig_check() method links primatives}
		- Primative Results (named after result) [always include single attribute & value] 
		- Compound Results (named after intent; match cond, trig, & mach) {trig_check() method links primatives}
		- The basic goal of the primative & compound structure is to increase re-use of Cond & Result classes (too many class-per-var cases)
	- Wildcard clean-ups
		- Extend trig_check wildcards to 'post_act_cmd' & 'auto_act_cmd'
		- Extend trig_check wildcards to work with Warnings (or better yet, de-dup Warning's trig_check)
		- guard against multiple wildcaards per list
	- Results
		- extend BufferOnlyResult result_exe method in BufferAndEndResult and BufferAndGiveResult
		- TBD: extend child methods in results_class_def ?
		- in machines, should conditions and results just be key-value pairs in a dictionary?
			- As opposed to needing 2 separate lists with identical indexes?
	- Shorter cond & result names!!
	- move switch_reset to auto_action() ???
	- 'trigger_type' => 'trig_type' ??
	- naming conventions: need to avoid confusion between match_state and mach_state
	- naming conventions: cond & result name should be same except post-fix
	- sort out ability to push button / pull levers while goblin is guarding
	- need to implement hedgehog state machine based on creature state
- TBD: list of 'contained' internal_switches in MachMixIn attributes?
	- NOTE: (i.e. add to scope and remove levers & button from features?)
	- NOTE: [this is a good idea but hold off until at least one more control_panel type machine gets created]
- TBD: broaden hedgehog response to interacting with sword (e.g. "pull sword" should trigger)


##########################
### VERSION 3.82 START ###
##########################

Version 3.82 Goals
- Clean up documentation and incorporate into doc_strings
- final code clean-up for version 3.x

- TBD: documentation:
	- TBD: updeate creature doc
		- discuss creature state
	- TBD: update timer doc with trigger changes from 3.64
	- TBD: update mach doc with wildcaard cahnges from 3.64
	- TBD: update class diagram
	- TBD: update module diagram
	- TBD: create machine diagram
		- hedgehog => state machine idea
	- TBD: create creature diagram
	- TBD: Timer Decisions
		- timers are set by machines rather than triggered by player commands
		- other than providing description text, timers are dumb - they just count -  a machine takes all actions
- TBD: naming updates:
	- TBD: re-name 'wrapper' to 'app_main'
	- TBD: update pickle names
	- TBD: out_buff => output (or possibly user_output)
	- TBD: possibly rename modules to indicate usage first? i.e. creature_class_def.py => class_def_creature.py ???
	- TBD: create directory structure for modules (e.g. all class definitions in a single directory)
- TBD: elim hasattrib() in active_gs scope checks => is_cont(), is_mach(), is_creature() methods within classes
	- for active_gs.mach_obj_lst(), eliminate 'hasattrib' and create method to check for being machine
	- eliminate 'hasattrib' for containers in active_gs.scope_lst() too
	- have a default methods is_contain and is_mach for Invisible that returns False; overload to True for exception cases
- DONE: for doors and containers, use None option for no lock or no lid?
- CANCEL: Can I just set descript_key for Note in mk_def_pkl() with setter rather than whole dynamic_dict?
	- CANCEL: why do I need active_gs.dynamic_descript_dict again?
- mechanic clean-up
	- investigate setters & getters for GameState class
	- DONE: is there really any need for GameState room_mach_lst() ??
	- TBD: auto_static_behavior for goblin? (e.g. "the goblin is eyeing you coldly") each turn - maybe should be a standard function??
	- TBD: sort out more elegant assignment process for self referenced obj (e.g. re-assigning goblin to goblin_mach after goblin Creature instantiation)
	- eliminate active_gs.move_dec() ?
	- 'try... except' standard descriptions for examine() method (similar to Warnings) (???)


##########################
### VERSION 4.x START ###
##########################

Version 4.x Goals
- Introduce non-functional requirement code (e.g. saves and pkl clean-up)
- Integrate with web template
- webify

file handling:
- game saves (requires file clean up?)
- move doc to modules?
- org modules in directories?

web features:
- TBD: Figure out a way in web browser to show all adventure text in scrolling window (???)


##########################
### VERSION 5.x START ###
##########################

Version 5.x Goals
- Research existing IF languages (TADS & INFORM)
- Plan out expanded adventure
- Establish new base code needed for new adventure
- Write new code!


first: scan puzzle ideas and decide on next puzzles; plan for required features

interpreter ideas:
- can I store variables in descript_dict strings? (in f-string format)
- can I return method errors based on verb method (e.g. "Burt, what kind of person would try to attack a Throne?")
- should synonyms be an obj attribute??
- create a hint sub-system
- more abreviations: 'g' = 'again', 'z' = 'wait'
- TBD: no swearing in Dark Castle (with warning or else end of game)
	- cursing => end of game (requires warning_mach and usniversal scope)
- fix progromatic usage of "a" vs "an" (e.g. "There is a Iron Portcullis to the north")
- unlock => 'unlock with' prep  command
- default prep behavior = try command with obj in hand
- New interp() Ideas:
	- interp() refacto shoud be based on objects (contents of rooom)
	- each obj should have noun syns (in place of root_word)
	- if user input has multiple obj, determine noun vs. dir_obj from prep usage (i.e. to vs with)
	- have global verb syns and class-based verb syns (start with global; much easier!)
		- e.g. 'get' is gbl verb syn for take() but 'sit on' is a Seat class verb syn for enter()
	- based on verb, validate prep usage
	- Order of Op: 1) obj noun syns, 2) gbl verb syns

- TBD: Debug mode:
	- TBD: Need a debug mode that eliminates 'try' from 2word and prep commands
	- TBD: need a secret code to prevent regular player from falling into debug: 'debug poke53281,0'
	- TBD: maybe debug opens a menu where you can choose start room & choose to disable method and / or description guards
- TBD: verbose / brief

- Unit Testing (link: https://youtu.be/6tNS--WetLI ) ???

mechanic features:


python techniques:
- Do a refactoring code review (look into the 'any' command in place of for loops)
- TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )
- TBD: Try tupples for descript_dict
	- NOTE: Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
- TBD: learn about Super()
- TBD: read this article: https://sangeeta.io/posts/a-super-post-on-python-inheritance/

pipeline & testing:
- create 'win' test routine with checksum
- TBD: Jenkins integration to automatically update "v3 alpha" tab with latest commits


##########################
### VERSION 6.x START ###
##########################

Version 6.x Goals
- New rooms and puzzles!!
- New ideas - ideally should leverage existing coding with minimal addiional feature requirements
-implement new ideas
- publish new version and get feedback


*** Awesome Words to Use ***
- stalwart (hedgehog)
- griffonage (illegible handwriting)
- recreancy (shameful cowardice; perfidy)
- aubade
- defenistrate
- consigliere
- consternation
- phyisogamy (from 3 Muskateers)
- Gallivanter
- Solipsistic
- Bamboozled
- Flabbergasted
- Discombobulated
- Cattywampus
- Lollygag
- Makarkey
- Kerfluffle
- Brouhaha
- Nincompoop
- Skedaddle
- Pumpernickel
- rolly-polly (hedgehog)
- Coddiwomple
- Sockdolager (forceful blow)
- sagaciate (get along)
- sockdolager

*** possible new rooms ***
- upon_drawbridge
- entrance_hall (home base with well & safe shelf & hedgehog?)
- chapel (another possible home base?)
- courtyard
- library
- narrow / collapsed passage
- kitchen
- smithy
- maze
- wizards_tower
- dungeons

*** RESEARCH ***
- read The Craft of Adventure
- Play at least 5 games
- Read the Digital Antiquiarian reviews

- PUZZLE: perhaps at some point Burt needs to bake biscuits??
	- would involve finding and mixing ingredients, right order, starting fire, baking right time / temp

- PUZZLE: Under Water Puzzle:
	- treasure at bottom of old well - but need a magical way to hold your breath?
	- old_well as water source in entrance_hall and also passage to... where?
	- can hold breath for 4 turns, locked grate is 2 moves down, get warning on half air and last turn
		- TBD: create LiquidContainer class
			- TBD: create new LiquidContainer class
			- TBD: instantiate old_well in the main_hall which contains fresh water
			- TBD: update drink() to allow / error for drinking from the old_well
	- lantern is water proof
	- should be like rope puzzle for Zork I... 
		- you have everything you need in the remote room but can't get out without solving puzzle

*** DEBUG TOOLS ***
- work room for testing similar to tcrf.net Hollywood Hijinx


*** INTERPRETER ENHANCEMENT ***
- TBD: sort out synonyms like 'stand' and 'sit' and 'lie'
- Interpreter enhancements:
	- noun synonyms (list in place of base_name)
	- verb synonyms (attribute of Class? Should verbs associated with obj???)
	- enable "take all", "drop all"
	- randomize frequent responses (e.g. "in your spell book you see...")
- re-institue remove() verb for Garment; 'take' as synonym
	- worn obj take() => "You're already wearing it"
	- obj on floor remove() => "Taken" (i.e. is synonym)
- assume that item in hand will be used for activity (e.g. attack)
- move() command ?
- enable 'take all'
- create 'jump' command with same response as Zork ('Whee!' I think?)
- randomize description of Burt shown during 'inventory'
- convert words like 'look' to 2word in interp(), rather than cmd(), if possible

*** STORY IDEAS ***
- link lantern, sword, and jug to Infocom history but unify with fantasy genre (no battery)
- valor; caprecious and messy sort of valor - sort of show up three sheets to the wind but ready to save the day
- shiny sword glows near enemies?
- meet the wizard from Enchanter who is searching for a scroll


*** ARCHITECTURE ***
- What would a decoupled, micro=services based DC look like? What are the consumers / providers?


*** AMBIENT SIM ***
- for light sources:
	- "(providing light)" in inventory; also is a condition (on)
	- can move into a dark room, but can't open a container in the dark
- for FlamableItem: light & burn (e.g. matches)
- PaperItem: burns; also, if writing, ink runs and becomes unreadable
- maybe sleep in bed (after min # of moves) to dream to get hints? But light must be on so you loose turns of light and wake up hungry and thirsty? Hint is provided randomly based on points not yet accrued?
- need to check Enchanter to find length of days, when sleep needed, food & drink, etc
- For dream hint: Burt has dream / memory of Nana teaching him the binary code she would use with Willy while secretly courting (she was a lunch lady?) to set a time to sneak off with him. Would involve 2 types of biscuits on counter... Nana's Own and McVittles (which were awful)... she only had room for 3 biscuits but had to show times from 0 to 7... 
- non-humanoid monster could be a special weapon description case (fun new puzzle idea)???
- TBD: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
	- encumberance (post Burt as object?)
	- implement carying capacity / container cappacity; Also carry restriction passages, etc..
- food & drink system?
- darkness & light source system?
	- lantern (requires darkness travel tracker, timer, item_mach, univeral scope, death by grue)
	- honestly, Grues don't make sense in DC... I intend for there to be a fair number of creatures around the place... why haven't they been eaten by Grues? (one could ask the same about the Troll and the Thief of Zork - but presumably these are dangerous creatures that can fend off Grues?). Instead, I think I'll use the same mechanic (2 dark rooms in a row == death) but the textual explanation will be Nana's warning to young burt "Burty, you mind gallavanting around in the darkness - you'll trip and break your neck!"
- DONE: How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away
	- DONE: eliminate universal_scope => just add these to Burt's invis_lst
- DONE: make goblin hand contents examinable (e.g. Grimy Axe)



*** DC1 PUZZLE IDEAS ***
Misc:
- Randomization feature like the spinning room in Zork 2 ? With way to turn it off
- Physics puzzles - see-saws, pulleys, and ceterfugal force
- Dragon is bored because it has read every book in the library - need to find a new book to interest it
- Ferret is named Bartleby
- landscape / path changes
- create vehical puzzle?



*** DC2 PUZZLE IDEAS ***
- maybe, in DC2, before the ball, the princess is missing (hiding from evil prince) and is diguised as a black cat that burt needs to befriend?
- it would be cool to have an invisibility cloak / spell (probably need to keep it short term / contained)
- Note: active_gs.hero enables player to take on different characters in the game (e.g. Burt could become a mouse)
- princess 'poise' & 'moxie'
- fun idea - small creature - like a mouse - as an item
- more directions
- Princess takes 3 forms:
	1) Cat => Burt must get her collar
	2) Raven => ring
	3) Cockney goth waif (castle servant) => boots
	- Then princess arrives at ball wearing collar, ring, and boots
- Burt must also foil evil Prince plan to murder princess (perhaps swap fake dagger for real one?)
- Burt himself is taken for a lowly Baker (in past time)
- Basically, Burt and the Princess (in various forms) wander around the castle doing chores learning info
- Also, Burt has a chance to demonstrate himself as kind and helpful - or not - to disguised princess
- Meanwhile, the whole castle is in an uproar getting ready for big ball and princess arrival
- some scattered rumors that princess has "mysterious magical powers"
- Meeting Nana
	- Also, somewhere in the mix, Burt must prove who he is to a (much younger) Nana
	- he needs to get (Willy's) broach, and put it behind the throne
- Burt is given most of his hot/cold direction via a portrait of himself & princess
	- As Burt makes right decisions the portrait gets clearer; fades with wrong decisions
	- Portrait is taken of Burt and waif-princess by great artist who needs stand ins for Prince & Princess wedding portrait
	- Burt originally (in modeern times) finds the portrait on the pedistal next to the throne and *MUST* put it back there during time travel just before arriving back or else the closed time loop fails (gets multiple hints that there's "something he must do")
- Dungeon key
	- in modern times, the one room Burst still can't get into is the dungeon
	- main key was lost years ago during the "great ball fiasco" and spare has never been found
	- not viewed as very important since the dungeon side-wall parially collapsed and was flooded by moat
	- Dungeon is now the lair of the evil croc in the moat 
	- Burt needs to get the dungeon key in past times
	- he must somehow get it back to modern times so he can rescue princess in flooded dungeon from croc
		- why can't she just turn into a fast fish?? need to think through her magic limits
	- impossible to keep it so must hide it behind a brick (where he will retrieve it in the future)

Princess Time-Travel Quest:
- Princess asks Burt if he's an assassin, spy, or suitor => answer = 'baker'
- Back in time, need to hide key behind brick (otherwise princess arrives but time travels back behind locked door)
- Get key from chief guard via cheesecake?
- Both Burt and the Princess need to eat food before time travel (nod to hitchhikers guide)
- Juanty hat to escape guards at just the right time

IDEA: have a 'jaunty hat' that enables you to move 'twice per time click' (i.e. no pre or post actions or move increments for one turn)
	- would necesitate default responses to attacks and things like that
	- could solve nearly any puzzle so need to deliver late in the game
	- maybe especially useful for solving a '2 button' puzzle

- Back to the Future - time machine chariot idea
	- chariot is in stable hooked up to old_mare
	- feed old_mare 1.7 boxes of jigga-whats special speed feed and chariot charges forward... at 8.9 mph blue light and time change
	- dial in chariot picks year
	- chariot is shiny metal and has a label on is saying "from the grande dutchy of Lorean" (remember, only chariots from the Grande Dutchy can truly call themselves 'De Lorean' - all others are merely fast, shiny chariots)
	- Special easter eggs... there are 2 full boxes of jigga-what's special feed and 2 70% full boxes on an old dusty shelf (current time). They appear ancient and you've heard that for some reason or other this brand was outlawed 100 years ago - you didn't think any was left in the world... if Burt goes back in time he can feed the 1.7 jw to the old mare to get back in time - at this point, all 4 boxes are consumed (Burt will, in fact remember there as only having been 2 in current time)... but, if Burt attempts to bring a box with him back to the future he will fragment the space-time-continum and find himself sitting at a computer, playing a text adventure... with all of his memories fading and end with the statement "it must have been just a game all along..." with no score = "N/A" and title = time traveller

DCII Time Travel Ideas:
- In past, burt must convince young_nana to give him Willy's broach in order to drop it behind throne or else timeline is doomed!
- Perhaps burt first travels fwd in time a week and can pick up an unfinished portrait of burt & princess that gives future status (similar to Back to the Future)


Alter Terrain:
- Use Map room_pair updates to alter a room dramatically after a major change
	- e.g. Zork I resevoir post-dam opening
	- could use this after a cave in or rock collapse in the dungeons / mines?

Vehical:
- Bucket pulley / weight puzzle in wizard's tower
- need to adjust weight correctly going up and down
- need to grab staute (?) on way up / down?
- or else maybe mine cart / parachute??

Zork Thief = Ferret:
- dextrous, loves colorful objects, likes to fidtet / fiddle with things, clever
- will steal an object from burt (or that burt has touched) each time it randomly runs into him (some items off limits?)
- Some item on a high shelf or complexly locked (like the Zork egg) can only be opened by the ferret
- burt can indefinitely / eternally distract the ferret (*after* it has solved its puzzle) by giving it a rubks cube (described not named)
- the ferrets treasures can be found in a hole that burt needs to reach his arm into (scary warnings - could be a grue)
- maybe the shelf in the main hall is the one place safe from the ferret
- or else the object is in the courtyard and ferret gets it after burt sees it through window?? (seems like less agency?)
- hedgehog chases ferret away from Entrance Hall any time it randomely attempts to enter (entrance hall has well & shelf too)

hedghog:
- perhaps the hedgehog greets you every time you walk into the main_hall once you return the sword?

Food:
- bread for Burt (save piecs of cheese for the mice)
- maybe need to keep feeding biscuits to the hedgehog?
- perhaps loaf of bread and bottle of water can each provide multiple servers (similar to enchanter)
- additional bread verbs needed: bake ???

Special Glasses / Dream form:
- let burt see a room using descriptions from another dict


Carry Cappacity Constraints:
- item 'size' limits (invent point values) for Containers and Narrow Passages
- instead of big_rock could have sea_chest in main_hall tht burt can barely lug
	- maybe it's locked but has no key
	- can be the solution to the Wumpus_bat puzzle
	- Also, when the bat drops the chest, it smashes open... maybe revealing the rubiks cube (too soon??)
- Could have a narrow_passage - perhaps a collapsed passage that connects the north and south halves of the castle?
	- burt can only squeeze through with a few items (no sword)... perhaps the ruby for the smithy mouse is in the north side?

Window:
- would be need to have a Window class that allows burt to see what he can't take
- could allow burt to peer into a courtyard with a tree and fountain
- maybe 2 guard dogs - one with red hat, one with blue hat - that are constantly paroling a passage
- if burt observest the window for a few turns he can see when to zip past the patrol
- (when the blue-hat dog looks up expectantly)
- perhaps window is in the collapsed_passage ??

Writing / engraving:
- would be nice to have a way to write / engrave on something
- maybe make a weapon useful against a particular foe by engraving it??
- or put the dragon to work clearing a passage by making a sign that says 'cheese cake'

Vanishing cabinets:
- enable limited travel to another part of the dungeon?
- maybe only work one way (because broken?)
- or maybe can only bring very little gear?

Game Ending:
- Kinging Scroll glows faintly... and can only read when sitting on the Royal Leturn... which also glows slightly
	- lecturn found in the Library (Willy's favorite room in the castle)
	- But only one thing can be _on_ the lecturn at a time... and there is currently a stuborn_snail there
	- snaill can only be encouraged to move by showing it the salt from the Kitchen
	- Depends on class Shelf (example obj = table, counter, lecturn - anything with a surface); needs a max_items attribute?

Glum Dragon
- how about a glum / bored / enui-ladden dragon that is blocking the libary entrance with its bulk
	- the dragon is too tough to be harmed by - or even to notice - being attacked
	- instead it just bemoans its misery - misquoting hamlet, and camus ("The underworld is other people")
	- If given cheesecake (baked in the royal bakery) it can be cheered up - and will go work on its to-do list and read a book and such
	- note: all other creatures like cheesecake too?

- map
	- maybe room beyond the Main Hall is the round room with many collapsed / ruined exits
	- can go east through mouse hole to bakery or smithy
	- or west to libary - which will then connect player back to cooridor that leads to anti-chamber


- Peter Pan puzzle where you catch and make use of your shadow / mirror image?

IDEA: Junk mail puzzle (multi-element solution); all for "chariot warranties"

IDEA: Thief puzzle (can take from backpack)

IDEA: chess puzzle - player first has to figure out that room is chess board ("statuary on a parquet floor" and then mate (probably smoother mate) to get through door. Replay button is broken (so only play once). other side has mate next turn so loose if you make wrong move. Possibly a small, wizzened gnome shows up to scold the player if they make an illegal move?

IDEA: create a jaunty_cap that makes Burt move twice as fast as everything else in the world - maybe essential for escaping the time travel ball?

IDEA: create a fun scenario where TravelEffect take item gets used... maybe a giant brid comes along and takes whatever's in Burts hand and scares him off until he carries a lead weight (or a heavy rock?) - which tires the bird out so much Burt can go in the room and get back his stuff and enter the room? Maybe this could be a room between main hall and antechamber that the maze / mouse hole is off of? Maybe nest is in corner of room of class Box (not open / close or lock / unlock).
- Make it a Wumpus Bat - a reference to Hunth the Wumpus and Adventure!!
- Takes an item from Burt's hand and sends him back the way he came to take cover; item is randomly placed in another (reachable) room
- Solution is to enter room carrying a heavy rock - Bat will take but leaves rock by its nest with a note "Tired out from lugging big rocks - leaving Dark Castle for a while to visit the Wumpus"
- Heavy Rock allows introduction of carrying capacity... playing can't carry *anything* else while carrying Heavy Rock
- some useful treasure found in the nest 
- Nest could be a container with open_state = None and lock_state = None

- Can sharpen and clean sword in mouse hole - maybe only way to get past goblin
- Until sharpened, sword can only parry goblin?
- need a non-shrunken ruby to pay for sword sharpening (turns up nose at cheese - says he never touches it because it gives him indigestion)
- mini Zork maze to get to blacksmith mouse
- maybe random mouse keeps appearing and if you give it cheese it runs off and can be followed to the blacksmith
- maybe mouse in maze is from Who Moved my Cheese
- references to grafitti in maze?? (e.g. "what would you do if you weren't afraid?")
	- IDEA: grafitti on Room wall = disp_writing()
- Potion cabinet => maze => sharpen payment; cabinet: Royal Potions Maker: Danni Igotyour , potion: 867-5 => combo
	- Give clues - mention that you hear a boppy tune in your head on description; give some lyrics after 5th attempt
- Sign on mousehole mentions royal blacksmith and royal baker
- Can only find royal baker by NOT taking the signed "exit" route from the blacksmith (easy east)
- Machine in bakery makes cheese (for mouse) or biscuits (for hedgehog) by adding ingredients and pushing correct button
	- Need to have "hatch" closed in order to run machine
	- Takes 3 turns to create food
	- if start biscuits turn after starting cheese then 5 turns later produces cheesecake! (only once - machine brakes after)
	- Everyone wants cheesecake! Can be used to solve any creature puzzle (even goblin) and takes 5 turns to eat
- potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
	- 3 turns of shrink in Main Hall; 30 turns in mouse hole
	- maybe 2 potions in cabinet
	- Need to keep the magic shrink potion from traveling... maybe have it in a basin with a chain-attached cup?
	- or maybe you shrink for 3 turns or as long as you're in a confined space - whichever comes later??
		- (don't want to code every room for being mouse sized)
- maybe 2nd mouse, every once in a while, gets up from his nap at the table near the blacksmith and sneaks off to the bakery
	- bakery very hard to find... go to a corner of the maze and then go 'up'!!
- Maybe a magic radio (a machine entity like the baking machine) in the Maine Hall that plays "Danni I've got your numbrer" when tuned correctly? Gives clue for potion chest. Also maybe acts as distraction during time travel puzzel - plays over gentle lilting of harp, violins, and triange - which enables Burt to cut in and dance with princess (evil prince is off gyrating hips wildly)? Perhaps the magic radio used to live in the throne room but got moved to the main hall after the 'incident' (note could indicate this) ;-D
- Radio damaged during move from throne room (speaker out; etc)
	- Radio volume goes to 11 (crossed out?)
	- On time travel need right station & full volume to distract prince (learn songs during future time investigation; maybe "moany moany" or "old time rock and roll"?)
	- Perhaps wearing Hedgehog brooch (and smiling) are key to winning princess' trust durning time travel?

5.x Additional rooms
	Have portait of Willie revealed in throne room and give player mouse hole and time travel quest
	5th room
		mouse hole - to exercise existing capabilities (e.g. "food" that can be eaten)
		copper key opens cabinet which holds potion
		find a use for 'close' verb; maybe potion refill
		possibly create 'return' verb to put things back (or maybe 'swap')
		potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
		enter mouse hole
		maybe fight mouse?
		silver key in mouse trap; need to swap with copper key
		find a use for close command?
		would be fun to use every verb ;-D
		maybe a guard mouse that only lets you past if you're wearing the hedgehog_broach
		Indiana Jones reference for mouse trap and ball chasing you out ;-D
		make hedgehog_broach wearable
		link puzzle to total number of moves? Or to score?
		repeat option like 'again' / 'g' in Zork (JE request)
	Possibly add a room 6 with time travel??
		Opportunity to include princess in game - perhaps have Willie give her the hedgehog_broach to time travel
		Depict future (opportunity but challenges) by painting to portrait
		Also get key from time travel - put in container and then refind 100 years later
		loose brick in dark_alcove - "appears not to have been disturbed for 100 years"
		guard with key_detector in main hall
		trade keys with princess? give her the hedgehog broach? maybe during dance in throne room
		dungeon down stairs from throne room
		use the world "balter" (dance poorly but having fun)
		save hedgehog from evil prince?
		final question from princess "you look like you woke up an a stable" - final choice of response from Burt to princess - down to earth or prim
		in throne room 3 paintings of past and 1 blank space for future
		key to open dungeon?
		keys same colors as ready player 1


##########################
### VERSION X.x START ###
##########################

Version X.x Goals:
	- DB back end
	- "dungeon bulder" web interface (?)
	- Run on AWS EC2

DONE: Watch YouTube vid on SQLAlchemy: https://youtu.be/51RpDZKShiw
	DONE: Create practice file
	DONE: Watch video

DONE: instantiate sqlalchemy DB
	DONE: Queue huge sdk issues due to ancient version of sqlalchemy...
	DONE: Have upgraded to version 1.1.2 using Stash but still getting issues in sqlite compiler
	DONE: Think I might have to upgrade to 1.4.x to get JSON support for sqlalchemy.dialect.sqlite (installed 1.4.18)
	DONE: now requires install of importlib_metadata (installed via 'pip install')
	DONE: now I need to 'pip install typing_extensions'
	NOTE: APPEARS TO WORK!!!

TBD: now start working with sqlalchemy again in place of txt files
	TBD: How do I setup a DB that continues to persist independent of an app running??
	TBD: Before returning values, Interpreter must save stateful_dict to DB
	TBD: Before running code, must load the value of stateful_dict from DB
	IDEA: default object values should start as a DB entry (or txt files) and be loaded on new game



##########################
### VERSION Y.y START ###
##########################

vY.y IDEAS
- runs on AWS with API GW, Lambda, and DynamoDB!





*** Demo Object Commands ***

# entrance.examine()
# print(entrance.valid_paths)
# entrance.go('south')
# entrance.go('north')

# entrance.examine()
# dark_castle.examine()
# gate.examine()
# gate.read_writing()
# sword.examine()
# sword.take()
# print(hand)
# sword.take()
# sword.drop()
# gate.open()
# gate.unlock()
# rusty_key.examine()
# rusty_key.take()
# print(hand)
# gate.unlock()
# gate.open()
# gate.open()
# print(eval(room).room_stuff)

# sword = Item('sword','The sword is shiny.', True, 5)
# sword.examine()
# sword.change_desc('The sword is rusty.')
# sword.examine()
# print(sword.takeable)
# print(sword.weight)
# sword.add_writing('dwarven runes', 'Goblin Wallaper')
# sword.examine()
# sword.read_writing()
# gate = Door('front gate', 'The front gate is daunting', False, False)
# gate.examine()
# gate.change_desc('The front gate is HUGE!')
# gate.examine()
# gate.read_writing()
# gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
# gate.read_writing()


### test ###
# rusty_letters.read(stateful_dict)
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
