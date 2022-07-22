To Do List - Dark Castle v3

July 7, 2022


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl

	
*** NOTES ***


##########################
### VERSION 3.7x START ###
##########################

Version 3.7x Goals
- Plan out code refactoring
- Refactor code
- document code

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
4)use 'any' to return boolean rather than for-looping through lists
5) pull variable assignments out of loops unless the variable will change within the loop
6)consider removing 'inline variables' that are only used once... just return the assigned value... I am guilty of this one a lot... I like how it looks but should reconsider
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


##########################
### VERSION 3.70 START ###
##########################

Version 3.70 Goals
- extend Creature attributes and methods
- refactor Burt as a creature object
- refactor coding as I go

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

burt refactor order
- DONE: watch refactoring best-practices videos so I can refactor as I go (I will be re-coding a LOT)
- DONE: full review of all active_gs attributes to be moved to burt_obj
	- active_gs.state_dict['backpack', 'hand', 'worn']
	- active_gs.static_obj_lst = {'universal' : [backpack, burt, fist, conscience]}
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
- INPROC: update existing Creature class and creaatures (e.g. hand & worn)
	- IDEAS:
		- creature 'worn' attribute
			- how to track worn dict?
		- refactoring noun classes for burt-as-creature
			- think abour 'source' and 'desination'... e.g. for take(), source = is_item in <room>.obj_scope; destination = <creature>.hand_lst
			- can we have 'burt' be the default <creature> but other options available?
				- this would allow give() to become a noun class method... essentially a take() initiated by burt
				- likewise, show() becomes an examine initiated by burt
				- maybe each Creature has its own description list?
					- desc list as creature attribute ???
				- with a default examine() response similar to "the X is not interesting"
				- thinking systemically, can we pre-validate noun class methods?
					- validate() would run between interpreter() and pre_action()
					- e.g. for take() use case, can we checks to see if obj is_item and is in <room>.obj_scope ?
					- (would also need to apply not already in <creature>.hand_lst and not in <other_creature>.hand_lst)
					- maybe need an is_takable() method? perhaps this is where the validation lives?? Returns bool and error message?
					- maybe broad command constraint list as well (e.g. obj must always be in room.in_scope?)
				- need to do a detailed mapping of what is required for success in each noun_class() method
		- no action for now
			- does creature_state really have any value? Maybe build hedgehog before pulling the plug on this one
			- IDEA: for Creatures, instead of headgehog_distracted_mach, maybe I just need a creature_distracted attribute??? (NO)
			- non-humanoid monster could be a special weapon description case (fun new puzzle idea)
			- for burt maybe add brass_lantern - always trust and shining in your off hand... wouldn't want that to go out now would we? Grues...
			- princess 'poise' & 'moxie'
			- valor; caprecious and messy sort of valor - sort of show up three sheets to the wind but ready to save the day
			- create all_lst, item_lst, and mach_lst methods for creature class
	- DONE: Weapon class
		- IDEAS: 
			- reference weapon (e.g. "Grimy Sword") in attack text
			- could have a Weapon class based on Item; could have associatted adverbs and verbs for attack description
			- once we have a Weapon class, could test for is_weapon() for moat_mach
			- incorporate weapon class descriptions
		- DONE: creaate Weapon class (inherits from Item) with desc_lst attribute
		- DONE: create is_weapon() method; (False for Invisible; True for Weapon)
		- DONE: import Weapon into mk_def_kpl()
		- DONE: update grimy_axe to instantiate as class Weapon
		- DONE: update shiny_sword to instantiate as class Weapon
		- DONE: update entrance_moat_mach cond to use is_weapon()
		- DONE: updte GameState with weapon_in_hand() method
		- DONE: clean up comments in mk_def_pkl, cond_class_def
	- DONE: creature hand for existing creatures
		- IDEAS:
			- change hand from list to scalar (???) => decision: keep hand as a list
			- what should happen if Burt tries to take the axe from a living goblin? (general case)
			- if you try to take an obj from a creature's hand => 'The X belongs to the Y'
		- DONE: create creature.hand_obj_lst attribute
		- DONE: update instantiation of guard_goblin & royal hedgehog to in mk_def_pkl()
		- DONE: add grimy_axe to guard_goblin
		- DONE: clean-up is_container
		- DONE: create is_creature method
		- DONE: update room scope method
		- DONE: update examine room method
		- DONE: examine creature method
		- DONE: take method
			- DONE: clean up take method
			- DONE: clean up comments
			- DONE: add creature hand item to guard clause of take method
			- DONE: add ['take', 'grimy_axe'] to goblin_attack_mach triggers
		- DONE: update creature.give() method
			- DONE: clean up give method
			- DONE: create put_in_hand method
			- DONE: update give method to use creature.put_in_hand method
			- DONE: sort out hedgehog give mach (update CreatureItemCond and TimerAndCreatureItemResult)
			- DONE: clean up auto_action() - move switch reset to auto_action()
			- DONE: clean up auto_action() - create is_timer() method and test in auto_action()
			- DONE: create auto_action for goblin to re-draw sword
			- DONE: test case of giving sword to hedgehog
		- DONE: reconsider naming conventions; SHORTTEN!!! (bear in mind that method will always appear after obj)
			- DONE: hand_obj_lst => hand_lst
			- DONE: hand_obj_lst_append => hand_lst_append
			- DONE: hand_obj_lst_remove => hand_lst_remove
		- DONE: update attack_burt method to use weapon.desc_lst attributes
			- IDEAS: need to sort out attack_burt method to key off an identifier of the attacker (i.e. golblin attack v.s. other creature)
		- DONE: update attack method to use weapon.desc_lst attributes
			- DONE: add is_attackable attribute to Creature class and instantiate value as True for guard_goblin and royal_hedgehog
			- DONE: implement not_attackable code for attack method
			- DONE: re-org attack and burt_attack response into 3 sections:
				- DONE: attack attack_initiation
				- DONE: burt_attack attack_initiation
				- DONE: attack_burt attack_resolution (w/ defaults & custom)
					- DONE: rename response_key to custom_key
					- DONE: create custom resolution_key dict entry
					- DONE: create default attack_resolution txt entries in static_gbl()
					- DONE: update method (move resolution text to the very end - post result_key - which will provide resolution_key_default)
					- DONE: update custom_text in static_gbl()
					- DONE: clean up comments
				- DONE: burt attack_resolution (w/ defaults & custom)
					- DONE: apply code format from attack_burt() method to attack() method
					- DONE: testing (attack hedgehog)
					- DONE: update hedgehog cutom_attack descriptions
	- DONE: creature_items_lst => rename to item_lst
		- IDEAS:
			- rename to make similar to room?
			- need a 'cant_drop_lst' for backpack => creature_obj_lst (no need to worry about backpack as open container)
			- creature attribute for inventory_visible == True / False
			- i.e. should creatures have a visible_inventory_lst that is part of examine scope? [only 'hand' unless creature = active_gs.hero]
			- only visible if creature = active_gs.hero() ??
		- DONE: creature_lst_append_item => item_lst_append() and creature_lst_remove_item => item_lst_remove()
			- DONE: update creature_class_def()
			- DONE: uupdate result_class_def()
			- DONE: comment clean-up
		- DONE: naming convention change to obj_lst (no) or item_lst (yes)
			- DONE: update result_class_def()
			- DONE: updated creature_class_def()
		- DONE: argh! rename item_lst to bkpk_lst. Also update item_lst_append() to bkpk_lst_append() and item_lst_remove() to bkpk_lst_remove()
			- IDEA: class attributes should be descriptive in relation to the *main class* (e.g. a creature has hand_lst & bkpk_lst attributes)
			- IDEA: class methods can be descriptive in relation to the *attribute variable class* (e.g. a creature has item_lst and vis_lst methods)
				- IDEA: so for creature == burt, item_lst() = hand_lst + bkpk_lst + worn_lst
				- IDEA: methods for creature and room = item_lst(), vis_lst(), all_lst(), and mach_lst()
				- IDEA: the thinking here is that there could always be another category of 'stuff'... maybe next burt gets a fanny pack?
				- So we never know that for a given class, a given attribute encompasses *all* of the items
				- for room maybe we should have floor_lst (all the things on the floor ?)
	- INPROC: new feature_lst attribue
		- IDEAS:
			- creatures could have a 'features' attribute (like rooms) for ViewOnly attributes (e.g. burt's 'conscince')
			- (maybe goblin's "officiousness" ?)
			- is visible to outside world but not listed via 'examine'
		- DONE: add attribute & extend instantiation
		- DONE: create setters & getters
		- DONE: create ViewOnly obj and description text to put in goblin & hedgehog instantiation
			- DONE: goblin = officiouness
				- DONE: "hobgoblin of little minds"
			- DONE: hedgehog = loyal! scruffy and dog-like; not mafioso or sycophant
			- DONE: update text to hint at feature_lst obj
		- TBD: create vis_lst() method
			- TBD: create active_gs dict entry that defines hero = burt and create a get_hero() method to get this info
			- TBD: create vis_lst() to get visible creature inventory
				- TBD: returns hand_lst for all creatures
				- TBD: returns feature_lst for all creatuers
				- TBD: returns item_lst and worn_lst (eventually) if creature == active_gs.get_hero()
		- TBD: update active_gs.scope commands to use vis_lst() method
	- TBD: invisible_lst (new name for mach_obj_lst)
		- IDEAS:
			- creatures can have 'invisible' attribute for machs (like rooms)
			- change mach_obj_lst to 'invisible'? or 'invis_lst'?
		- TBD: rename mach_obj_lst => invisible_lst
		- TBD: create mach_lst() / all_lst method for creatures (based on vis_lst)
	- TBD: worn
	- TBD: refactor review for class Creature methods
	- TBD: shorten dict naming for all dicts - 2_word *max*!
	- TBD: review and shorten all attribute and method names; * remember that the method will always be associated with an object! *
		- TBD: creature_state => state
		- TBD: dead_creature_obj => corpse
	- TBD: re-order attributes for better flow
	4) instantiate burt_obj
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


##########################
### VERSION 3.71 START ###
##########################

Version 3.71 Goals
- modularize remaining GameState class and declarations

- TBD: active_gs holds list of smaller game state components? clock + scoreboard + map + printer ??
- TBD: modularize mk_def_pkl() and active_gs ( how about gs.sboard.get_score() )


##########################
### VERSION 3.72 START ###
##########################

Version 3.72 Goals
- re-work app_main() flow
	- today: interp() =(if no interp_error)=> pre_action() => cmd_exe() => post_action()
		- this works if there is an interp() error or if the command is successful... but what if there is a cmd_error ???
		- as a work-around, I end up re-testing command validity in pre_action() / post_action() - or accepting buggy code (eat_biscuits_warning)
	- to-be: interp() =(if no interp_error)=> cmd_error_check =(if no cmd_error)=> pre_action() => cmd_exe() => post_action()
		- so in noun_class, every verb method needs to return cmd_error (boolean) and be able to run in 2 'modes': 'ec_mode' or 'exe_mode'
		- cmd_error_check() runs the method in ec_mode and returns cmd_error
		- if not cmd_error: cmd_exe() runs method in exe_mode
		- can likely shortcut for non '2word' and 'prep' cases
		- one side effect: every method needs to either throw text on error or do something on success... we cannot take an action on failure (?) 

- related thinking:
	- Should really think through a 'validity test' for pre_actions - would like to leverage all the validation code I already have!
		- Should noun obj methods return a 'success' indicator (for pre & post actions)?
		- IDEA: do I need to check for kinging_scroll in hand since this is a post_act_cmd ???
		- Be able to call noun methods in non_buffer mode purely for pre & post action validation? 
		- for command-driven machines - especially pre-action - would like to have a systemic way to know if player command runs successfully

- TBD: fix eat_biscuits_warning so that it no longer lives in just entrance and main_hall and no longer triggers when biscuits not in hand
		- suggest making eat_biscuits_warning universal and enabling success feedback loop for cmd_exe


##########################
### VERSION 3.73 START ###
##########################

Version 3.73 Goals
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


*** NEW PUZZLE IDEAS ***

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

IDEA: use phyisogamy in the game!!

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
		- (don't want to code every room for being mouse sized)
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
