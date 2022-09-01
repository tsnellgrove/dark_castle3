To Do List - Dark Castle v3

Aug 10, 2022

*** Need a new IDE ***
- iPad / offline: Pyto
- Mac Air / Offline: MS VSCode
- Cloud / Online: CodeAnyWhere, Cloud9 (AWS)
- Reference article: '5 ways to use Python on an iPad'


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl


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
	- avoid the term 'scope' since there are different scopes for different actions... prefer terms like 'is_vis'
	- do NOT reference the class in the attribute - the attribute will always appear w/ the class: creature.state vs. creature.creature_state
	- do NOT attempt a rigorous and exhaustive naming conventions - this way lies madness and very long vars. Embrace function / method context! 
	- be biased towards shorter vars; bend naming rules as needed to achieve shorter vars; shorter vars == more readable code!
	- use consistent attribute and method naming across classes whenever possible - especially classes that could be grouped together.
		- This approach allows for easy itteration across an amorphous list of objects.
- classes:
	- prefer generic naming for classes (e.g. Container and Surface vs. Chest and Shelf)
	- class attributes should be named after physical features of the class, NOT their expected data types: hand_lst, bkpk_lst, worn_lst
		- class data types can be grouped via methods whose naming denotes the data type: vis_lst, all_lst, mach_lst
- attributes:
	- prefixes:
		- 'is' for bools
	- postfixes:
		- 'lst' for lists
		- 'dict' for dictionaries
		- 'str' for strings
		- do NOT use 'obj'; vars are assumed to be obj by default
			- If similar obj and non-obj vars appear in same function, diff w/ post-fix: e.g. worn_lst vs. worn_lst_str
- methods
	- prefixes:
		- 'is' for methods where no varriable is passed but a bool is returned; e.g. 'obj.is_item()'
		- 'chk' for a method where you will send an obj and get back a bool
		- 'get' for a method that will return a 'usuabl' obj var
	- postfixes:
		- 'disp' if a method's main purpose is to buffer content


*** NOTES ***


##########################
### VERSION 3.7x START ###
##########################

3.7x Goals
- implement validate module between interp() and cmd_exe()
- convert Burt to class Creature
- modularize Machs
- refactor all code
- document all code in-line with doc_strings


Learn about refactoring:
- DONE: Watch refactoring videos and take notes on advice
- DONE: Re-order and grouip refactoring advice

*** Refactoring Advice ***

- Function Design:
1) provide 'None' option for class attributes
2) provide 'match_value' for Conditions & Results

- Variable Assignment:
9) MOVE ASSIGNEMENTS CLOSER TO USAGE!! I need this one!!
15) return the conditional comparison itself! I do this now but my old code needs updating!! Note - can force boolean value with bool() function

- Strings
26) Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}" '. Can also do math in string: 'print(f"{i} squared is {i*i}")'. I NEED TO MAKE THIS SWITCH!!!
27) Concatenate strings with '.join': 'lst_of_str = ["Hi", "Tom"] ;; my_str = " ".join(lst_of_str)' => "Hi Tom"

- If Statements:
3) Merge nested if statements with 'and'
7) can use an 'if expression' with 'condition' statement: 'x = 1 if condition else 2'
8) use 'if guard statements' to return false cases immediately at the top of the if-then chain; reduces indentation
16) if 'if-else' blocks contain duplicate execution, use an 'or' to combine them
17) replace multiple value comparisons with 'in list' - or better yet, 'in set' ... since sets have unique values... I need to learn more about sets...
29) Simplify if-statements with 'if x in [a, b, c]'. I think I already do this. (same as 17)

- For Loops:
4) use 'any' to return boolean rather than for-looping through lists
5) pull variable assignments out of loops unless the variable will change within the loop
6) consider removing 'inline variables' that are only used once... just return the assigned value... I am guilty of this one a lot... I like how it looks but should reconsider
13) replace 'for i in range(len(lst)): lst_item = lst[i]' with 'for i, lst_item in enumerate(lst):' ; enumerate gives you both index and value as 
a tupple... need to see if I can use this?
19) iterate with enumerate to get index & value (same as 13)
14) replace manual loop counters of lists with enumerate... provides index and value... I think I am guilty of this in my Conditions / Results match-up

- Lists:
10) SIMPLIFY SEQUENCE CHECKS! don't need to check for if len(lst) > 0: ;; just use if lst:
11) When possible, declare a list with intended values... don't declare an empty list and then populate with append
20) use list comprehension: 'squares = [i*i for i in range(10)]'
21) sort complex iterables with sorted() functions: 'sorted_data = sorted(data)'
22) sort unique value with set();  sets are unordered and have unique values; can convert list to set: my_set = set(my_list)
25) Count 'hashable obj' w/ collectinos.Counter(). Need to import collections: 'counter = Counter(my_list)' => dict of unique list items as keys with number of occurences in list as values. 'print(counter(x))' returns number of occurences (0 if not in list). Can also: 'most_common = counter.most_common(1)' where argument tells how many most common values are desired => list of tupples. can call repeatedly to just get the number of occurences of the most common item.

- Dicts:
12) For cases where you need to reference both a dictionary's keys and their values: don't call values by keys manually... instead, use format 'for key, value in dict.items():' - I need to watch for this in my code - espeically older code
24) define default values in dicts with .get() and .setdefault(): 'count = my_dict.get("count", 0)' will return the default of '0' if there is no "count" key in my_dict; if there is no default it returns 'None';; Also, count = my_dict.setdefault("count", 0) will add "count" to my_dict with a value of 0
28) Merge dicts with {**d1, **d2}. if you have dict1 & dict 2, 'merged_dect = {**dict1, **dict2}' merges and eliminates duplicataes.

- Other:
18) learn more about 'yield' and 'yield from' for generators (only for very large data sets - I don't need this)
23) save memory with generators (for very large lists)

	
Learning Links:
- 1 & 2 = me
- 3 to 10 = https://youtu.be/rp1QR3eGI1k
- 11 to 18 = https://youtu.be/wd1JqBWm3lQ
- 19 - 29 = https://youtu.be/8OKTAedgFYg
- TBD: https://youtu.be/C-gEQdGVXbk
- TBD: https://youtu.be/KTIl1MugsSY (refactor starts about 7 min in)


Burt as an object
- why?
	- allows elimination of attack_burt() method of Creature class
	- suddenly inventory becomes much more elegant
	- this is the way
- when?
	- Maybe make Burt an object before making all the machine changes??
	- this is a big refactor => do this first
- how?
	- Burt to be obj type Creature


- N/A: Old thinking
	- today: interp() =(if no interp_error)=> pre_action() => cmd_exe() => post_action()
		- this works if there is an interp() error or if the command is successful... but what if there is a cmd_error ???
		- as a work-around, I end up re-testing command validity in pre_action() / post_action() - or accepting buggy code (eat_biscuits_warning)
	- to-be: interp() =(if no interp_error)=> cmd_error_check =(if no cmd_error)=> pre_action() => cmd_exe() => post_action()
		- so in noun_class, every verb method needs to return cmd_error (boolean) and be able to run in 2 'modes': 'ec_mode' or 'exe_mode'
		- cmd_error_check() runs the method in ec_mode and returns cmd_error
		- if not cmd_error: cmd_exe() runs method in exe_mode
		- can likely shortcut for non '2word' and 'prep' cases
		- one side effect: every method needs to either throw text on error or do something on success... we cannot take an action on failure (?) 

Basic Refactor Steps:
	- refactor pass - basics
		- shorten variable names
		- MOVE ASSIGNEMENTS CLOSER TO USAGE!
		- leverage if-then shield pattern 
		- provide 'None' options for variables and 'match' options for Conditions
		- Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}"
		- ensure graceful failure of missing key lookups
		- raise errors on 'impossible' outcomes
		- comment each new attribute
		- add tripple-quote doc_strings
	- refactor pass-advanced
		- auto-gen keys
		- return the conditional comparison value itself (bool)
		- Concatenate strings with '.join'
		- merge / shorten if-then-else with use of 'and' & 'or'
		- consider removing 'inline variables' that are only used once... just return the assigned value...
		- use enumerate to get index & value!
		- use 'any' to return boolean rather than for-looping through lists
		- don't need to check for if len(lst) > 0: ;; just use if lst: (Also, bool(None) == False
		- use list comprehension: 'squares = [i*i for i in range(10)]'


##########################
### VERSION 3.72 START ###
##########################

Version 3.72 Goals
- pre-Burt-to-creature conversion clean-up in Creature, Room, and Container classes and scope methods, std nouns
- keep exercising refactor skills!

- DONE: refactor Item
	- DONE: first-pass refactor of take()
		- DONE: var names:
			- DONE: room_obj => room
			- DONE: room_obj_lst => floor_lst
		- DONE: use f-string
		- DONE: use if-then shield pattern
		- CANCEL: refactor take from creature failure with any
		- DONE: create remove_item() method in room and call from take()
			- DONE: create chk_contain_item() and remove_item() method in Container, Creature, GameState (temp), and ViewOnly (False)
			- DONE: in room.remove_item(), check if item in floor_lst. If not, loop through floor_lst and  if chk_in_contain_lst, remove_contain_lst 
			- DONE: call room.remove from take
			- DONE: lots of testing!
		- DONE: org attrib vs. obj methods using comments
		- DONE: re-add worn removal message to active_gs.worn_lst_remove_item(self)
	- DONE: refactor drop()
	- DONE: doc_string
		- DONE: Imp Detail: only diff - take(), no attrib chg, all items takable, ways to stop take: swap w/ ViewOnly, Warning, Mach
		- DONE: turns out that any() does not work well here:
			- DONE: 2nd condition can't be undefined
			- DONE: I don't get access to 'obj' outside the expression (so I can't include the creature's name in the error string)
		- DONE: Room (not Item) should be authoritative for where an item can be found (since Room provides is_vis() )
			- CANCEL: should creature test be in room? unique error requires obj full_name so decided not
		- DONE: Game Design: Adventurers love Items, Zork tradition, Burt too, intrigue w/ out of reach Item, infuriate by taking away items
		- DONE: drop
- DONE: PortableContainer
	- DONE: introduce PortableContainer class (was Suitcase) (dual inheritance from Container & Item)
	- DONE: instantiate black_suitcase (test with rusty_key & cheese_wedge)
- DONE: refactor Beverage
	- DONE: rename class to Liquid
		- DONE: noun_class_def()
		- DONE: mk_def_pkl()
	- DONE: rename method is_beverage() to is_liquid()
		- DONE: noun_class_def()
		- DONE: validate()
	- DONE: org methods
	- DONE: if-then guard technique
	- DONE: f-string
	- DONE: elim temp vers (except hand_lst)
	- DONE: descript_key => auto-gen key
		- DONE: implement auto-gen key
		- DONE: elim attribute key
		- DONE: elim descript_dict entry for attribute key
	- DONE: doc_strings
- DONE: Create new PortableLiquidContainer to replace Jug (Container + Item => PortableContainer => PortableLiquidContainer)
	- DONE: testing fail on put non-liquid in glass_bottle; in cmd_exe debug mode
	- DONE: put() for jug fails if obj not is_beverage
	- DONE: elim print_contents_str() 
	- DONE: eliminate Jug (replaced by generically named PortableLiquidContainer)
	- DONE: elim obj_lst_to_str (move funct to *** local funcs *** in gs_class_def.py); move shared_class_func module to 'legacy' folder
- DONE: refactor map
	- DONE: create Map class
		- DONE: create map_class_def.py module
		- DONE: create Map class with attribute = map_lst
		- DONE: in mk_def_pkl, import Map
		- DONE: in mk_def_pkl, instantiate map lst of dicts
		- DONE: in gs_class_def, add map attribute
		- DONE: in mk_def_pkl, add instantiated map to active_gs
	- DONE: map.chk_obj_exist method (was chk_obj_in_map() then was map.chk_obj_in_any_floor_lst() )
		- DONE: create method map.chk_obj_in_any_floor_lst # checks of obj in floor_lst in each room in map
		- DONE: create method chk_name_exist( (was chk_name_in_any_floor_lst() )
		- DONE: rename Room room_obj_lst => floor_lst
		- DONE: update score to use mapchk_name_exist()
		- DONE: update cond with map.chk_obj_exist
		- DONE: confirm that active_gs.obj_exist and active_gs.obj_name_exist are no longer needed('goblin_dead' case also addressed in score() )
		- DONE: eliminate active_gs.obj_exist and active_gs.obj_name_exist
	- DONE: door_lst() method
		- DONE: create door_lst() method to provide list of doors in room
		- DONE: add map.door_lst() to active_gs scope method
		- DONE: add map.door_lst() to room.examine
		- DONE: remove doors from room.floor_lst in mk_def_pkl()
	- DONE: obj_cond_disp
		- DONE: create obj_cond_disp method to provide door condition (door / passage names and directions) for room
		- DONE: add to room.examine()
	- DONE: update go() method to use active_gs.map
		- DONE: create gs.map.is_valid_dir(self, room)
		- DONE: use gs.map.is_valid_dir(self, room) in go() method
		- DONE: create gs.map.get_door(room) method
		- DONE: use get_door() in go()
		- DONE: create gs.map.next_room(room) method
		- DONE: use get_next_room() in go
	- DONE: eliminate legacy attributes and methods
		- DONE: elim gs.room_lst
		- DONE: elim gs.map_dict attributes
		- DONE: elim room.door_dict
		- DONE: elim active_gs.is_valid_map_direction()
		- DONE: elim room.self.door_in_path()
		- DONE: elim room.get_door()
		- DONE: elim active_gs.get_next_room()
	- DONE: implement unreachable_room to resolve condition strings for Entrance (e, w, & s)
		- DONE: create 3x rooms: unreachable_1, unreachable_2, unreachable_3
		- DONE: update room condition str to read better for outside (replace 'door' = None with passage_str) [error - walked through portcullis!]
		- DONE: fix use of 'and' and 'commas'
		- DONE: update 'fake' descript of Entrance in startup()
	- DONE: go back and refactor Map class
		- DONE: review imports
		- DONE: std var names
		- DONE: comment attributes
		- DONE: nested for loops
		- DONE: list comprehension with nested for loops
		- DONE: use any() pattern for bool outcome
		- DONE: raise error if no return in loop
		- DONE: doc_strings
	- DONE: update doc_string for Door
- INPROC: refactor Room class
	- DONE: rename vars
		- DONE: features => feature_lst
			- DONE: noun_class_def
		- DONE: room_obj_lst => floor_lst
			- DONE: noun_class_def
			- DONE: gs_class_def
			- DONE: creature_class_def
			- DONE: cond_class_def
			- DONE: result_class_def
		- DONE: invis_obj_lst to invis_lst
			- DONE: noun_class_def
			- DONE: gs_class_def
	- DONE: refactor examine
		- DONE: exmine titles for rooms as separate buffer line (enables brief / verbose and also diff dict)
			- DONE: if obj.get_title_str() not None: gs.buffer(if obj.get_title_str()) ; for Room => def get_title_str(self): return self.full_name
		- DONE: should be able to get basic descriptions from Container and Creature classes
			- DONE: need methods in class for this - reuse in Container & Creature examine
		- DONE: for look, don't show container contents as 'nothing' if the container is_empty()
		- INPROC: universalize use of title, description, writing, condition, vis_obj_lst
			- DONE: update examine() with obj_cond_disp()
				- DONE: ViewOnly
					- DONE: Update ViewOnly.examine()
					- DONE: create default def obj_cond_disp(): => pass
				- DONE: Room
				- DONE: Door
				- DONE: Container
				- DONE: Creature
				- DONE: Switch
			- DONE: finalize approach to multiple conditions (e.g. Container)
				- DONE: extended obj_cond_disp() in Container
			- DONE: update examine() with self.vis_obj_disp(active_gs)
				- DONE: ViewOnly
					- DONE: Update ViewOnly.examine()
					- DONE: create default def vis_obj_disp(active_gs) => pass
				- DONE: Room
				- DONE: Container
				- DONE: Creature
			- DONE: Finalize change
				- DONE: update ViewOnly.examine() doc_string
					- DONE: 5x components of examine(); Why lock down examine()? 1) Codifies presentation, 2) enables brief and verbose
					- DONE: cons: leads to an outline-style description; harder to textify
				- DONE: rename obj_cond_disp() => cond_disp()
					- DONE: noun_class_def
					- DONE: switch_class_def
				- DONE: rename vis_obj_disp() => contain_disp()
					- DONE: noun_class_def
					- DONE: creature_class_def
				- DONE: clean up comments in noun_class_def.py, switch_class_def.py, & creature_class_def.py
				- DONE: update doc_strings for cond_disp() and contain_disp()
	- DONE: move GameState scope methods to Room
		- IDEA: scope method => room.vis_contain_lst = self + doors + Legacy + self.feature_lst + for obj in floor_lst: extend(obj.vis_contain_lst)
		- IDEA: post Burt to Creature move => if statement in Creature.vis_contain_lst to include self.bkpk_lst & additional node depth
		- DONE: rename vis_lst() => vis_contain_lst()
			- DONE: noun_class_def
			- DONE: creature_class_def
			- DONE: gs_class_def
		- DONE: create room.vis_contain_lst()
		- DONE: test room.vis_contain_lst()
			- DONE: interp
			- DONE: gs_class_def
			- DONE: noun_class_def
		- DONE: redirect scope calls to room.vis_contain_lst()
		- DONE: elim room_element_lst()
		- DONE: comment clean-up
	- DONE: move GameState chk_wrt_is_vis() to Room
		- DONE: crate chk_wrt_is_vis() in Room
		- DONE: migrate refs to Room
			- DONE: validate()
			- DONE: noun_class_def()
		- DONE: clean up comments
	- DONE: move GameState scope_check() to Room
		- DONE: in Room, rename to chk_is_vis()
		- DONE: migrate refs to Room
			- DONE: validate
			- DONE: mach_class_def
			- DONE: noun_class_def
			- DONE: gs_class_def
		- DONE: clean up comments
	- TBD: investigate room_mach_lst() vs. mach_obj_lst() - do I really need them both ???
	- TBD: move GameState mach_obj_lst() method to Room
		- TBD: rename to get_mach_lst() and create in Room
		- TBD: refactor as needed
		- TBD: migrate refs to Room
			- TBD: 
		- TBD: clean up comments
	- TBD: move remaining mach_list scope methods to Room
	- TBD: rename vis_contain_lst() to get_vis_contain_lst() ???
	- TBD: refactor room next steps
	- IDEA: element_lst refers to the first-pass list of obj available in the room (i.e. not including those obj in containers or creatures)
		- is node_lst a better term?
		- Yes!! node_lvl is the key... imagine an inverted tree... node_0 is at top (say room), node_1 are immedaite contents of node_0, and node_2 = the contents of node_1
		- we can also talk about relative vs. absolute node levels
		- the goal is for look to return information on node_lvl 0, 1, & 2 (i.e. describe the room, room contents, and items inside room containers / creatures); inventory is similar
		- however, we want all node levels to actually be in scope
		- we do NOT want node levels to go too deep... we already forbid containers from holding containers or creatues
		- we could also forbid creatures (other than Burt) from holding creatuers or containers...
		- This would make our max node level = 3: entrance => burt_hand => bottle => water
		- The limit could be imposed at the give(), show(), take(), and put_in_hand() mehtods
		- if this caused serius issues there could be a modular machine to swap in a dummy non-container obj
		- could also run a pre-start check on container & creature to throw errors on illegal contents
		- need to document (to self!) consistent approach to what is visible when Burt looks, examines, or inventories
	- IDEA: vis_element_lst == list of visible elements == room.floor_lst + room.feature_lst
	- TBD: move room to dedicated module ???

##########################
### VERSION 3.73 START ###
##########################

Version 3.73 Goals
- finish noun refactor
- create a class for descriptions
- create a Surface class
- rename active_gs => gs

- INPROC: class by class, reduce from double-tab to single tab
	- DONE: web_main.py
	- DONE: map_class_def.py
	- INPROC: noun_class_def.py
		- DONE: PortableContainer
		- DONE: PortableLiquidContainer
		- TBD: next!
- TBD: refactor Clothes => Garments
	- TBD: sort out error when already wearing crown... ideally should be "You're already wearing"... not "not in your hand"
	- CANCEL: create Garment class-specific remove() method that calls take() ??
	- TBD: auto-gen keys
		- TBD: implement try for auto-gen key on both append and remove methods
		- TBD: consider auto-gen keys for all verb methods (probably not)
		- TBD: Organize auto-gen keys together
		- TBD: consider creating a separate dict for autogen keys
- TBD: refactor Food
- TBD: refactor Weapon
- TBD: refactor Switch
- TBD: create Surface class!! (was 'Shelf')
	- similar to container but prep is 'on'; no open() or lock() ; has max_obj attribute
	- put initial shelf in Main Hall
	- implement Control Panel as Shelf !! (may need to add control_panel after guard_goblin dies)
- TBD: reorg noun_class_def into base (Invis, Writing, ViewOnly, & Liquid), Item (including Food & Weapon), Room, Door and Container, Surface ??
- TBD: refactor Creature / attack()
	- TBD: move to algorithmic key generation (gets rid of whole show_dict; big parts of give_dict)
	- TBD: re-org attack and attack_burt to enable modes: validate, exe_std, exe_silent, exe_creature
	- TBD: re-org to identify 'attacker' and 'winner' 
	- TBD: re-code attack / attack_burt response correctly based on in-line notes
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
- TBD: rename active_gs to gs

##########################
### VERSION 3.74 START ###
##########################

Version 3.74 Goals
- re-work app_main() flow with validate() module
- refactor app_main() modules

- related thinking:
	- Should really think through a 'validity test' for pre_actions - would like to leverage all the validation code I already have!
		- Should noun obj methods return a 'success' indicator (for pre & post actions)?
		- IDEA: do I need to check for kinging_scroll in hand since this is a post_act_cmd ???
		- Be able to call noun methods in non_buffer mode purely for pre & post action validation? 
		- for command-driven machines - especially pre-action - would like to have a systemic way to know if player command runs successfully
- IDEAS:
	- thinking systemically, can we pre-validate noun class methods?
		- validate() would run between interpreter() and pre_action()
		- e.g. for take() use case, can we check to see if obj is_item and is in <room>.obj_scope ?
		- (would also need to apply not already in <creature>.hand_lst and not in <other_creature>.hand_lst)
		- maybe need an is_takable() method? perhaps this is where the validation lives?? Returns bool and error message?
		- maybe broad command constraint list as well (e.g. obj must always be in room.in_scope?)
		- if fail validate() , buffer error and end app_main()

- TBD: introduce 'mode' attribute ('exe_std' and 'validate') to show, give, and put
- TBD: deploy 'mode' attribute ('validate' and 'std_exe') for all 2word commands
	- TBD: this will break the 'go south from Entrance' warning... probably the easiest fix is to create a re-usable unreachable_room to the south
- TBD: final clean-up
	- TBD: tune goblin and hedgehog text; maybe add a faded poster of ancient and unreasonale regulations to the antechamber wall?
	- TBD: fix eat_biscuits_warning so that it no longer lives in just entrance and main_hall and no longer triggers when biscuits not in hand
			- suggest making eat_biscuits_warning universal and enabling success feedback loop for cmd_exe
	- TBD: refactor active_gs. scope / mach_scope
			- Use list comprehension to eliminate for-loop? (link: https://medium.com/self-training-data-science-enthusiast/python-list-comprehensions-use-list-comprehension-to-replace-your-stupid-for-loop-and-if-else-9405acfa4404 )
	- maybe call verb methods with a 'mode' variable that can be validate, exe_std, exe_silent, or exe_creature ??
	- how can I make descript_dict modular so that other dicts can be chosen (if I want to temporarily tell adventure from another persepctive)
	- DECISION: writing perspective
		- With burt being a creature and all methods being rewritten to work with the Creature class, we have a choice
		- in theory, any creature could be used to play the game - and each might have its own description_dict
		- this would be fun for a short session in a single room but is not practical for extended play
		- realistically, nearly all descriptions will be from burt's perspective
		- but in some cases creatures will use methods to take actions and burt will *obeserve* there actions
		- this should be enabled by mode = 'exe_creature'
- TBD: refactor app_main() modules


##########################
### VERSION 3.75 START ###
##########################

Version 3.75 Goals
- refactor Burt as a creature object
- refactor coding as I go

- DONE: full review of all active_gs attributes to be moved to burt_obj
	- active_gs.state_dict['backpack', 'hand', 'worn']
	- active_gs.static_obj_lst = {'universal' : [backpack, burt, fist, conscience]} <= add brass_lantern ? "wouldn't want that to go out!"
	- methods:	
		def get_backpack_lst(self):
		def backpack_lst_append_item(self, item):
		def backpack_lst_remove_item(self, item):
		def get_hand_lst(self):
		def hand_lst_append_item(self, item):
		def hand_lst_remove_item(self, item):
		def hand_check(self, obj):
		def hand_empty(self):
		def put_in_hand(self, new_item):
		def get_worn_lst(self):
		def worn_lst_append_item(self, item):
		def worn_lst_remove_item(self, item):
		def clothing_type_worn(self, item):
		def get_static_obj(self, static_key):
		def inventory(self):
	- will also enable 'room scope' type methods to move to class Room

Refactor burt as a Creature class object
	4) instantiate burt_obj
			- TBD: create active_gs dict entry that defines hero = burt and create a get_hero() method to get this info
			- TBD: update creature.vis_lst() to get visible creature inventory
				- TBD: returns item_lst and worn_lst if creature == active_gs.get_hero()
		- TBD: create inventory() method for creature
		- TBD: burt_creature to be instantiated in entrance.feature_lst (can remove burt from scope_list() in active_gs.scope)
			- TBD: correction - burt to go in room.floor_lst (not feature_lst) but then exclude from room.vis_lst() [remove(gs.hero)]
	4.5) Analyze noun classes... which ones update burt inv vs. read from burt inv?
		- IDEA: start by implementing the burt inv updates in paralelle to active_gs updates
		- IDEA: create 'jinventory' and 'jlook' commands to confirm that burt_creature matches active_gs.burt
		- IDEA: now migrate the 'read' noun classes one-by-one to read from burt_creature (refactoring first as I go)
		- IDEA: lastly, when all methods point to burt_creature, I can comment out the active_gs.burt update methods and test
		- IDEA: Refactor as I go; provide a 'silent mode' for each method() for when it is called by a non-burt creature
	- IDEAS:
		- refactoring noun classes for burt-as-creature
			- think abour 'source' and 'desination'... e.g. for take(), source = is_item in <room>.obj_scope; destination = <creature>.hand_lst
			- can we have 'burt' be the default <creature> but other options available?
				- this would allow give() to become a noun class method... essentially a take() initiated by burt
				- likewise, show() becomes an examine initiated by burt
				- maybe each Creature has its own description list?
					- desc list as creature attribute ???
				- with a default examine() response similar to "the X is not interesting"
			- need to do a detailed mapping of what is required for success in each noun_class() method
		- IDEAS - future
			- does creature_state really have any value? Maybe build hedgehog before pulling the plug on this one
			- IDEA: for Creatures, instead of headgehog_distracted_mach, maybe I just need a creature_distracted attribute??? (NO)
			- non-humanoid monster could be a special weapon description case (fun new puzzle idea)
			- for burt maybe add brass_lantern - always trust and shining in your off hand... wouldn't want that to go out now would we? Grues...
			- princess 'poise' & 'moxie'
			- valor; caprecious and messy sort of valor - sort of show up three sheets to the wind but ready to save the day
			- create all_lst, item_lst, and mach_lst methods for creature class
		- TBD: in noun methods, do I need to pass init_creature to each verb method in order for mode = 'creature_exe' to work??
	5) integrate burt with active_gs (get_hero method)
		- How to pass burt obj? maybe active_gs.get_hero(); burt saved in dict
		- Note: get_hero() enables player to take on different characters in the game (e.g. Burt could become a mouse)
		- does get_hero bias us towards a search for current hero room? Or do we still cache 'room' in active_gs ???
	6) move burt_obj from room to room (features attribute) when active_gs moves
		- Burt to be in room features
	7) universal descriptors => burt_obj
	8) updaate burt hand & inventory changes in parallel to active_gs (create setter methods for creatures)
		- TBD: change goblin re-arm result to take() rather than put_in_hand()
	9) update module-by-module to read from active_gs to burt_obj (create getter methods for creatures)
	10) eliminate attack_burt method
	11) does room_scope now become a Room method?
	12) comment out active_gs hand & inv updates
	13) lots of testing!!!
	14) clean-up comments
	- TBD: move active_gs.universal_lst timer obj to burt.invis_lst
	- TBD: for ViewOnly create methoed 'vis_lst(): return []' to simplify Room.vis_lst() ???
	- TBD: create Chair class based on Surface
		- TBD: sit() method (depends on 'on' prep)
		- TBD: need to be able to determine which node Burt is in (i.e. the chair, not just the room); also need ot know room
		- TBD: look shows room with 'sitting in chair' condition
		- TBD: can only examine / take other items in the chair (burt's own inventory)
		- TBD: most other methods just generate "you'll have to stand up to do that"
		- TBD: vis_lst = chair.vis_lst + room.name
- TBD: improve natural language / paragraph (vs. outline) read of examine()
	- TBD: Room
	- TBD: Creature

##########################
### VERSION 3.76 START ###
##########################

Version 3.76 Goals
- refactor remaining app_main chain
- modularize remaining GameState class and declarations (???)

- TBD: rename active_gs => gs
- TBD: perhaps Map, Score, and Descript are classes w/ static dicts in mehod / class and actual obj in gs attributes
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
- TBD: refactor score
	- TBD: determine max_score from summ of all possible scores?
	- TBD: score = class with object being attribute in gs
	- TBD: print_score() a method of the Score class
	- TBD: instead of a dict of score achievements w/ T or F, just have a list of score achievemnts achieved
	- TBD: link front_gate score to opening door
- TBD: refactor GameState and dicts in static_gbl() with dunder methods (__getattr__ and __setattr__ ; see email to self on Aug 2, 2022)
- TBD: active_gs => gs renaming; point to same obj to start with ??
- TBD: active_gs holds list of smaller game state components? clock + scoreboard + map + printer ??
- TBD: modularize mk_def_pkl() and active_gs ( how about gs.sboard.get_score() )


##########################
### VERSION 3.77 START ###
##########################

Version 3.77 Goals
- Clean up machine, warning, and timer coding
- Create / update program documentation

- TBD: Machine coding clean-up
	- TBD: Machine 2.0 improvement ideas:
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


*** DECISIONS TO BE DOCUMENTED ***

*** Timer Decisions ***
- timers are set by machines rather than triggered by player commands
- other than providing description text, timers are dumb - they just count -  a machine takes all actions


*** SOMEDAY MAYBE IDEAS ***

first: scan puzzle ideas and decide on next puzzles; plan for required features

interpreter ideas:
- create a hint sub-system
- more abreviations: 'g' = 'again', 'z' = 'wait'
- TBD: no swearing in Dark Castle (with warning or else end of game)
	- cursing => end of game (requires warning_mach and usniversal scope)
- fix progromatic usage of "a" vs "an" (e.g. "There is a Iron Portcullis to the north")

naming conventions:
- TBD: re-name 'wrapper' to 'app_main'
- TBD: update pickle names
- TBD: out_buff => output (or possibly user_output)
- possibly rename modules to indicate usage first? i.e. creature_class_def.py => class_def_creature.py ???

mechanic features:
- 'try... except' standard descriptions for examine() method (similar to Warnings)
- TBD: perhaps create 'sit' and 'stand' methods for throne? Description when 'sit': "feels out of kilter - pushed or pulled out of alignment"
		- IDEA: would be a bit tricky... interaction with rest of room would be inhibitted while sitting?
		- IDEA: could possibly have sit be very brief with auto stand since it's not comfortable (not very satisfying) ???
		- default sit = on floor ('criss-cross-apple-sauce')
		- full implementation = 'sit on'
		- for most verbs, sit scope = self (i.e. creature_scope)
		- for examine (?), sit scope = room_scope
- TBD: elim hasattrib() in active_gs scope checks => is_cont(), is_mach(), is_creature() methods within classes
	- for active_gs.mach_obj_lst(), eliminate 'hasattrib' and create method to check for being machine
	- eliminate 'hasattrib' for containers in active_gs.scope_lst() too
	- have a default methods is_contain and is_mach for Invisible that returns False; overload to True for exception cases
- TBD: for doors and containers, use None option for no lock or no lid?
- Can I just set descript_key for Note in mk_def_pkl() with setter rather than whole dynamic_dict?
	- why do I need active_gs.dynamic_descript_dict again?
- investigate setters & getters for GameState class
- is there really any need for GameState room_mach_lst() ??
- TBD: auto_static_behavior for goblin? (e.g. "the goblin is eyeing you coldly") each turn - maybe should be a standard function??
- TBD: sort out more elegant assignment process for self referenced obj (e.g. re-assigning goblin to goblin_mach after goblin Creature instantiation)
- eliminate active_gs.move_dec() ?
- TBD: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
	- encumberance (post Burt as object?)
	- implement carying capacity / container cappacity; Also carry restriction passages, etc..
- fun idea - small creature - like a mouse - as an item
- more directions
- landscape / path changes
- food & drink system?
- darkness & light source system?
	- lantern (requires darkness travel tracker, timer, item_mach, univeral scope, death by grue)
- How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away
- create vehical puzzle?
- shiny sword glows near enemies?
- make goblin hand contents examinable (e.g. Grimy Axe)
- create 'jump' command with same response as Zork ('Whee!' I think?)

file handling:
- game saves (requires file clean up?)
- move doc to modules?
- org modules in directories?

web features:
- TBD: Figure out a way in web browser to show all adventure text in scrolling window

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
### VERSION 3.8x START ###
##########################

Version 3.8x Goals
- Introduce non-functional requirement code (e.g. saves and pkl clean-up)
- Integrate with web template
- Unit Testing (link: https://youtu.be/6tNS--WetLI ) ???

- TBD: Debug mode:
	- TBD: Need a debug mode that eliminates 'try' from 2word and prep commands
	- TBD: need a secret code to prevent regular player from falling into debug: 'debug poke53281,0'
- TBD: verbose / brief


##########################
### VERSION 3.9x START ###
##########################

Version 3.9x Goals
- New rooms and puzzles!!
- New ideas - ideally should leverage existing coding with minimal addiional feature requirements
-implement new ideas
- publish new version and get feedback


*** Awesome Words to Use ***
- find a use for the word "griffonage" (illegible handwriting)
- recreancy = shameful cowardice : perfidy
- aubade
- defenistrate
- consigliere
- consternation
- use phyisogamy in the game!!
- Gallivanter
- Solipsistic


*** possible new rooms ***
- upon_drawbridge
- entrance_hall (home base with well & shelf & hedgehog?)
- chapel (another possible home base?)
- courtyard
- library
- narrow / collapsed passage
- kitchen
- smithy
- maze
- wizards_tower
- dungeons

*** NEW PUZZLE IDEAS ***


Alter Terrain:
- Use Map room_pair updates to alter a room dramatically after a major change
	- e.g. Zork I resevoir post-dam opening
	- could use this after a cave in or rock collapse in the dungeons / mines?

Vehical:
- Bucket pulley / weight puzzle in wizard's tower
- need to adjust weight correctly going up and down
- need to grab staute (?) on way up / down?
- or else maybe mine cart / parachute??

Under Water:
- treasure at bottom of old well - but need a magical way to hold your breath?
- old_well as water source in entrance_hall and also passage to... where?
- can hold breath for 4 turns, locked grate is 2 moves down, get warning on half air and last turn
	- TBD: create LiquidContainer class
		- TBD: create new LiquidContainer class
		- TBD: instantiate old_well in the main_hall which contains fresh water
		- TBD: update drink() to allow / error for drinking from the old_well
- lantern is water proof
- should be like rope puzzle for Zork I... have everything you need in the remote room but can't get out without solving puzzle

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
- additional water verbs needed: 'fill' and 'pour the <water> on the <noun>'
	- Perhaps regular containers can't contain liquids?
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
### VERSION 4.xx START ###
##########################

Version 4.xx Goals:
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
### VERSION 5.xx START ###
##########################

v5.x IDEAS
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
