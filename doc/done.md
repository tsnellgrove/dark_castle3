Done List - Dark Castle v3
Feb 9, 2022


##########################
### VERSION 3.01 START ###
##########################

NEXT: Tom Example
inheritance
Create Door as child of Item [DONE]
Create ViewOnly as parent to Item [DONE]
Create Container as child to door [DONE]
Create take & drop methods for Item [DONE]
Create unlock method for Door & Container [DONE]
Create open method for Door [DONE]
Create a Room child class of view_only... focus on inventory only - not movement [DONE]
Exercise inventory management using Room.room_objects and hand and take and drop [IN-PROC]
	Update Room examine, take, and drop [DONE]
	DONE: Test implementation
	DONE: add takability to the 'take item' method
DONE: More tutorials before this gets out of hand!
Note: I think I'm doing something wrong... 
	inventory management with objects is not as elegant as I was expecting

DONE: Too many calsses already... think about consolidation
Decision: Inheritance is complicated, Multi-Inheritance is more complicated, 
	and multi inheritance from inherited classes... is just right out!
DONE: So => make 'takable' a local attribute of container

Idea: Rooms are really just conneectd containers...
DONE: Link travel to doors or to rooms? For now deciding on rooms
DONE: Troubleshooting movement
DONE: Implemnt doors in rooms

DONE: Implement While True input loop
DONE: Fix input conversion
DONE: Fix go command - interpreter
DONE: Description of new room on change rooms
DONE: Enforce room.examine() based on location
DONE: Implement 'look'
DONE: Update room based on go (try global room)
DONE: Pass room variable to class methods (state_dict)
DONE: Troubleshoot "examine gate"... maybe implemnt room across all methods first??

DONE: Think through writing attribute for ViewOnly 
	(i.e. should be read dwarven_runes instead of read sword)
IDEA: Maybe what I want to do is create a method that can put one item *on* another... 
	so that I can put the writing *on* the item?
IDEA: Similar problem to a container... need a list of things that can be *on* the item - 
IDEA: should be at the ViewOnly level since many objects can have writing on them...
IDEA: nead a name... maybe 'features'
IDEA: this could also be used for control panel

DONE: Extend examine() for class Door to include open or close state
DONE: Fix read_writing => read
DONE: Implement 'close'
DONE: Implement 'lock'

DONE: Implement features
DONE: Writing as class
DONE: Implement read for ViewOnly class
DONE: Extend examine method for classes Room and Door (vs. replace)
DONE: Test read for Door class
DONE: Move 'features' to Room class (since we only examine room features)
DONE: Re-add 'features' to ViewOnly class - 
	because otherwise there is no way to include it in examine_lst
DONE: Add presence checking for examine on Door and Room classes

DONE: Implement containers
DONE: Decide how container contents should be presented and added to examine and take scope
DEC: Show container contents with hasattr upon open and then add to room objects
DONE: Implement 'open' case for containers (troubleshoot and implement case of empty containers)
DONE: Implement / Troubleshoot 'close' case for containers
NOTE: Implemented close reduction of room_objects via sets which leads to re-order

DONE: Reconsider restricting 'features' to class Room using hasattr
DONE: dis-allow locking when Door / Container object is open?
DONE: Represent container elements as sub elements of container in room
NOTE: Now I have a few more container problems:
DONE: First I need to make items in containers takable... 
	but not list them in the room_objects inventory... 
	perhaps I have an open_container_obj list? 
	Or perhaps better yet, 
	dynamically add contents of open containers to takeable scope? [YES!!]
IDEA: Next, when I take the item from the container,
	I need to remove it from <container>.contains
DONE: I think this in turn means 
	that the *item* needs to know what container it's in (like writing)?...
	No... let's keep items 'dumb'... 
	it's the room's job to know what's in the room 
	and it's the container's job to know what's in the container... 
	to implement this we just reverse the take scope process... 
	we start with a for loop of open containers and remove from there if possible
	else remove from room_objects
NOTE: I didn't have these issues in the old Dark Castle 
	because I had no 'close' command... 
	so I could safely dump the contents of any container 
	into room_obj the moment the container was openned. 
	Now that containers can be closed I need to actually solve this problem.
NOTE2: Should writing work this same way?
	No - I think it makes sense for writing to know what it's on..
	Because the two are entwined... 
	the writing on one object can never move to another
DONE: Add 'the container is empty' description for empty containers
DONE: Can't examine items in open containers... 
	need to add open container contents to examine_lst

DONE: Redirect prints to buffer
DONE: Create stateful_dict['out_buff']
DONE: Create buffer() helper function
DONE: "Bufferize" classes ViewOnly and Writing
DONE: "Bufferize" classes Room and Item
DONE: "Bufferize" class Door method examine
DONE: "Bufferize" class Door remaining methods

DONE: functionalize interpreter
DONE: "Bufferize" interpreter

DONE: Added open containers to read scope 
DONE: Functionalize container scan, perhaps look in room first


##########################
### VERSION 3.10 START ###
##########################

At this point, STOP(!!!), and start researching how others have implemented OOP text adventures
	DONE: Watch this non-oop text adventure tutorial: https://youtu.be/miuHrP2O7Jw
		Basic but good start
	DONE: OOP text adv tut: https://youtu.be/VxhZZHnig8U
		I can't stand this instructor's code style - more lessons after this one but can't face them
	DONE: 2013 advanced OOP Txt Adv: https://youtu.be/8CDePunJlck
		Great lesson! But all about console so need to pick and choose ideas
	NOTE: Did a bit of research - looks like cmd can be used with Flask; need to learn more about NLTK
	DONE: NLTK vid: https://youtu.be/1taCGR3_jlA
	DONE: Found Jeffery Armstrong from 2013 PyOhio Text Adv: https://github.com/ArmstrongJ?tab=overview&from=2021-03-01&to=2021-03-06
	NEXT: Understand robotadventure code better... learn about interpreter, DB, and JSON descriptions

new ideas:
	use a display_intro function
	import pprtint from pprint | pprint(vars(<object>))
	check https://github.com/ArmstrongJ/pyohio2013
	get to know cmd module - can cmd be used with flask??
	rooms to have lists of neighbors, objects, characters
	store rooms in json using json module? (import json) [see adv OOP at 15:30]
	room descriptions in json but then json-based rooms in sql DB??
	read through 2013 code in detail!!!
	make a copy of game DB for each player - enables "saved game"... 
	but will still need to differentiate static from stateful?
	modules for making file copy: tempfile, shutil
	curses module for status bar ??
	"nltk" (?) for interpreter??
	sqlite3 for DB?
	check out "robotadventure" from end of 2013 presentation
	how to eliminate eval()

Decisions:
	No need for curses in a flask app
	Don't use nltk - is overkill (and besides, I want to write me own interpreter)
	For now, don't use cmd - want more practice with classes
	Do figure out how to avoid using eval()

To Decide:
	Rooms in JSON?
	How to use DB??
		- Since I'm designing a web game, I need to separate stateful and static

Next to dos
DONE: Figure out how to replace eval() w/ getattr() => use str_to_class() snippet
DONE: Replace eval() usage w/ str_to_class()
DONE: 'take' is broken post eval() remove
DONE: 'take' removal logic doesn't check for item_obj being in container before attempting to remove it
DONE: Why does close need to remove container items from room_obj? Old legacy logic
DONE: Wouldn't it be a lot simpler if we just stored room_obj in stateful_dict rather than room_str ?
	DONE: Try using .name property of Room instead of tracking room in stateful_dict
DONE: Simplify open_cont_scan

DONE: new naming convention to clarify between room_obj and room_objects ?? Need a new term for "objects"
	DONE: Sort out whole naming convention of name_type vs. name_objects (containter too)
	DONE: room_objects => room_elements
	DONE: items in room_elements loop => elements
	DONE: room_element => objects?
		DONE: Initial troubleshooting in entrance
		DONE: unlock, lock, open, close
		DONE: Containers
		DONE: What about directions / doors
		DONE: Testing & Clean-up
		DONE: Should hand and room_objects also contain actual objects instead of text? 

DONE: if type() => hasattrib
DONE: Can I buffer at the end of each method?? // Buffer to one line
DONE: Naming convention for lst, dict, and obj?
	DONE: Thinking about this more... I don't want to type post-fix my primary variables... just my local ones
	DONE: Variable renames for stateful_dict and helper functions
	DONE: Variable renames for methods for ViewOnly and Writing
	DONE: Variable renames for methods for class Room
	DONE: Variable renames for methods for class Item
	DONE: Variable renames for methods for class Door
DONE: am I testing class Door methods (unlock, lock, open, close) for door in room?
DONE: Create separate doc file for to-do notes
DONE: Make examine scope check a function (include hand_lst, container_lst, room_obj_lst, & features_lst ?) (boolean for buffer)
DONE: drop => scope_check function
DONE: for Door class examine and open and Room class examine - functionalized container code
DONE: take => check room_stuff first
DONE: Extend use of open_cont_scan to all methods (how?)
DONE: Std solution for null for writing (vs. text 'null') => None

*** Interpreter Basics ***
DONE: 0) Functionalize Interpreter and use out_buff
DONE: 0.2) Should burt be an object??? (for now, No)
DONE: 0.3) Create a list of true one-word commands from dkv2:
	DONE: simple, true one-word commands: 'score', 'version'
	DONE: complex, true, one-word commands:	'inventory', 'look'
DONE: 0.31) Concept of 'universal scope' variables which should always be viewable - check dkv2
	Things burt always has with him: 'backpack', 'burt', 'hand', 'conscience' 
	Meta-game entities that should always be available: 'credits', 'help' 
DONE: 0.315) think through synonyms (e.g. 'n' == 'north' == 'go north' ) (n, s, e, w, i = inventory)
DONE: 0.32) one-word commands to be converted to two words
	simple: 'help', 'credits', 'north', 'south', 'east', 'west'
DONE: 0.33: first handle true one-word commands, then dict lookup word 2 for converted words and pass to 2-word code
DONE: 0.4) handle articles (a, an, the)

*** Time for some code maintenance / plubming ***
DONE: 0.6) time to implement backpack?
DONE: 0.63) Every scope search happens in a room, and every room has a feature list - so why are features different in scope function?
DONE: 0.65) review dkv2 verb methods... maybe move fail statements to top??
		DONE: Door Class
		DONE: Item Class
		DONE: Room Class
		DONE: Other Classes
DONE: 6.7) Remove buffer from scope_check function... reads more clearly inline in method
DONE: 0.7) convert to true flask vs. app structure (but don't worry about passing yet) [see version 2.1.4 for ideas]
	DONE: 0.71) introduce end function
	DONE: introduce move counter
	DONE: 0.73) fix 'quit' and add 'q' abreviation
	DONE: 0.76 fix 'start'
	DONE: add github remote
	DONE: email Franco to ask about pythonic approach to storing objects with multi-line string attributes; maybe store as JSON and import?

Structure Big Picture:
A-1) Create Helper module
A-2) Create Class module
A-3) Object Instantiation module
B) Refine main Interpreter function
C) Sort out prepositions
D) Create interpreter function module

*** Interpreter Adjectives & Preposistions ***
Fini 1-word commands
DONE: 1) Sort out 1 word vs. 2 word commands and error out all non-defined one-word commands

Word commands:
DONE: 3) use lists to identify words as verbs; (adjectives and prepositions later; nouns never?)
DONE: 4) if sentence does not start with a verb => please start with a verb

Adjectives:
IDEA: Every noun as an obj_name, full_name, root_name
	DONE: 5) add adjective to all items, doors, and containers => Extend to view_only
	DONE: 5.5) add full_name for all items, doors, and containers => Extend to view_only
	DONE: 5.7) Update to buffer full_name
	DONE: 6) Handle special cases of 3 words by converting adj + noun (word2 & 3) => obj_name and handle as 2-word case

IDEA: Enable use of root nouns? With error code if multiple same root in scope?
	DONE: 6.5) add root name for all items, doors, and containers => Extend to view_only
	DONE: 6.55) Restructure Interpreter 2-word processing for clarity
	DONE: 6.6) for 2 word commands, test to see if word2 is a known obj_name - if not, test for root_word
	DONE: 6.7) Create function that returns # of instances of root_word in scope and obj_name of last intance
	DONE: 6.8) if returned value = 1 then word2 = obj_name
	DONE: 7.5) If value > 1 Error code could be "I see more than one root_name. Please use the object's full name" (moves - 1)
	DONE: 7.6) if value < 1 then "I don't see a word2 here"
	DONE: Solve for special case of read / writing (is not currently in scope list)

IDEA: Introduce modules
	DONE: Helper functions
	DONE: Research config modules
IDEA: Change approach: class definitions, object instantiation, and helper functions are modules - Interpreter calls them
	DONE: Undo Interpreter module approach
	DONE: Classes module
	DONE: Create config moduel to instantiate object variables
	DONE: Clean up modules

Preposistions
NOTE: All room-based validation happens in the method - the Interpreter just enforces language roles and converts English to method calls
DONE: 7.7) Restructure interpreter to call functions
DONE: 7.8) create put method for container
IN-PROC: 8) in interpreter use lists to identify words as prepositions  ("put")
	DONE: 8.05) Convert noun_handling section into function
	DONE: Create a special handling case for word1 == "put"
	DONE: 8.1) if "in" not in user_input_lst => "I don't see the word 'in' in that sentence"
	DONE: 8.2) send input list between "put" and "in" to noun handling
	DONE: 8.3) send input list from "in" to "end" to noun handling
	DONE: 8.6) try calling put method of container; error out on except
	DONE: Troubleshooting - carefully map out class to getattr in working cases
	DONE: detailed testing - still haven't figured out why trying to put object not in hand doesn't trigger class error??
		DONE: maybe issue is use of hand_lst.remove instead of stateful_dict['hand'] ??
		DONE: Still don't understand problem... put not currently working
		DONE: All that trouble over in hand_lst == False vs. not in hand_lst !!
	DONE: Clean up intpreter
		DONE: noun handling returns too much
		DONE: word2 declaration only for go
	DONE: Create module for most interpreter functions
		DONE: create interp_helper module
		DONE: Test noun_handler in interp_helper - this worked!!

DONE: How to handle a container in a container?
	REJECTED: Only closed containers allowed in containers?
	DONE: You can't open a container in a container?

DONE: 10) Learn what import sys does! (well, I read about it at least)
DONE: 11) error on take of something you already have in hand
DONE: 11.5) maybe need a function to reduce move count on error?
DONE: 11.7) Need a better place to call end... ideally part of a loop independent of main module??
	- No: end as a function called during end condition is fine
DONE: Created static_dict and added it to helper() module
DONE: 11.8): Consider moving 'if hasattr(contains) code to container class?? (e.g. Door examine & open methods)
DONE: 12) Help subsystem: 
		IDEA: The one-word command "help" gives you a list of 2-word help commands: 
		IDEA: "basics", help abreviations", "help verbs", "help one-word-commands", "help preposistions", adjectives, articles
		DONE: Implement 1-word command
		DONE: Implement as 2-word special case call to help function
		DONE: help() function created; 'basics' option written & tested
		DONE: 'verbs' and 'one-word-commands' options written & tested
		DONE: articles & adjectives
		DONE: abreviations, prepositions 
IN-PROC: move stateful_dict['universal'] to static_dict['universal'] ???
	IDEA: This will be harder than I thought - because I am not passing static_dict everywhere
	IDEA: Either I need to start packing variables or I need to stuff everything in stateful_dict???
	IDEA: how about a module that declares static_dict and is called by all other modules?
	NOTE: Right idea but still needs to be sorted out... it's turtles all the way down
	NOTE: static_dict[] holds objects... so static_init() depends on init() which depends on classes() which depends on helper() which depends on static_init() !!!!
	NOTE: The only way to resolve this dependency is to pass the variable... so I will move universal[] back to stateful_dict 
		NOTE: (to be honest, I might want to add to it durin the course of the game anyhow)
		NOTE: The fundamental rule here is that any global variable that holds objects will need to be in stateful_dict 
	DONE: create dc3_static_init
	DONE: clean up universal[] mess and move it back to stateful_dict
	DONE: clean up comments
	DONE: Move descriptions_dict to static_init
DONE: Centralize all descriptions into a description_dict declared in a dedicated module
	DONE: copy descriptions to static_init() descript_dict
	DONE: change description source from self.desc to description_dict
	DONE: clean up comments in classes()
	DONE: eliminate self.desc attribute in classes() and init()
TBD: At this point declare v3.10 done (update version, clean up files, truncate to-do)
	DONE: create dc3_done.md and move 3.01 to-dos to it
	DONE: Create old_versions and docs folders and move files to them
	DONE: Update version number to 3.10 in static_dict and comments
	DONE: move 3.10 to-dos to done
	DONE: Commit to git with version 3.10 tag	


##########################
### VERSION 3.20 START ###
##########################

NOTE: 3.20 to be all about serialization and main / interpreter separation

IN-PROC: So what data do I need to save between sessions?
	DONE: stateful_dict, Door open & lock states, room contents, container contents
	THINKING: How to load and unload data between moves? where to store it? Need to outline plan
		IDEA: Get started by saving stateful_dict to as JSON to a DB and dumping and loading it each turn
		IDEA: Then maybe programaticaly dump and load stateful object data to a dict? Then save dict as JSON in DB?
		IDEA: Now I'm passing stateful_dict between main and interpreter... but goal is to pass only session ID (end_of_game and out_buff too?)
		IDEA: So how does this actuall work... what is the order?
		IN-PROC: First step is to isolate stateful_dict to the server side...
			IDEA: main should only send user_input and input should only return out_buff and end_of_game
			IDEA: But interpreter has a *lot* of returns... 
			DONE: Maybe the answer is to create a "wrapper" function that calls interpreter?
				IDEA: This works... but now, of course, stateful_dict is always reset to starting values...
		DONE: Once they are isolated, I need to decide where to initiate stateful_dict - perhaps in wrapper?	

TOPIC: serialization
	DONE: I need to learn a lot more about how this works; Things I need to learn:
		DONE: More in general about how DBs are used (Tech with Tim Flask 7 & 8)
		DONE: JSON or Pickle serialization? Investigate Marshmallow!! (YouTube video)
			DONE: watched marshmallow video: https://youtu.be/Gl-5m1_eVjI
			IDEA: Very helpful way to serialize / de-serialize.. from complex to dict...
			IDEA: but how do I handle complex objects that *hold* complex objects???
			DONE: Test multi-level objects with Pet class attribute for Person; focus on Nested format for troubleshooting
			DONE: Can serialize and de-serialize but not to a nested object???
			DONE: Got it working by removing schema def many=True !
			DONE: rationalize tutorial code

Clean Up Code:
	DONE: temporarily re-integrate main & interpreter
		DONE: clean up main
	DONE: introduce print options for classes
	Done: fix object hierarchy
		DONE: Sort out object model - objects should not need to know about things outside of them
			DONE: So writing shouldn't need 'written-on' - just search through objects for matching item (like containers)
				DONE: Created writing_check() to search for writing on objects in scope
				DONE: Elim use of written on
				DONE: Clean up writing changes
				DONE: Make Writing the parent class of View_Only
				DONE: Clean up writing class & init changes
				DONE: create obj_scope helper routine to be used by both scope_check and writing_check
				DONE: clean up helper routine
			DONE: And rooms shouldn't know what they're connected to... perhaps a Map class to hold room connections?
				DONE: decided to implement room connections as a 'path' sub-dict in stateful_dict (no need for actual object)
				DONE: implemented path sub-dict
				DONE: Clean-up commented code
				DONE: Comment out valid_paths attribute
				DONE: Clean-up commented code

DONE: introduce serialization and de-serialization
	IDEA: start from serialized state for stateful_dict and stateful classes
	IDEA: Or maybe just class_to_string as needed before export for stateful_dict??
	DONE: Test serializing to JSON in marshmallow_tut
		DONE: import json
		DONE: convert pet_data back and forth to json
		DONE: convert person_data back and forth to json
	DONE: Start by serializing to JSON and printing stateful_dict
		DONE: Sort out path dict in stateful_dict
			DONE: made all path keys String() to sort out mm Dict requirements
			DONE: Clean up code comments
		DONE: add 'doors' and 'containers' attributes to Room class (and "look" code) to sort out polymorphism issues
				DONE: Convert room_stuff -> room_items
				DONE: Add rooom_doors
				DONE: Add room_containers
				DONE: Clean up code comments
				DONE: Test and update as needed to address room_stuff change
				DONE: Update dc3_mm room schema
				DONE: Add dc3_mm container schema
				DONE: Test dc3_mm json conversion
		DONE: after dumping dict to json, looad the json back to dict and compare to original
			DONE: Initial troubleshooting; add allow_none=True for writing
			DONE: Add post_loads
			DONE: Sort out takeable for Item and Container (changed to takable)
			DONE: Detailed before & after compare
				NOTE: identical by manual inspection but not identical by programatic comparision (i.e. stateful_dict == result_dict => False)
	IN-PROC: Serialize to JSON and print class objects
		NOTE: identical by manual inspections but not identical by programatic comparision (i.e. stateful_dict == result_dict => False)
		DONE: Saved JSON to dict
		IDEA: How reading & writing serialized json stateful_dict to file should work:
			1) If start_of_game == True: load stateful_dict from dc3_default_stateful_json.txt
				DONE: Initial coding
				DONE: troubleshootin of obj id == vs. 'is' compare issues
				DONE: clean-up of troubleshooting comments
			2) Else: load stateful_dict from save_stateful_json.txt
				DONE: Initial coding
			3) At end of wrapper(): Write stateful_dict to save_stateful_json.txt (in overwrite mode)
				DONE: Initial coding
			
ISSUE: I am creating many duplicate objects during de-serialization	
	DONE: Sent email inquiry to Franco to see if I'm taking the right general appraoch to persisting objects - he's not familiar with issue
		DONE: Troubleshoot duplicate object issue (i.e. gate reports as both open and closed)
			IDEA: I can solve the stateful_dict problem by storing only string values and converting to objects after de-serializing (loading)
			IDEA: but when I go to persist the objects themselves I think I will create many more duplicates during de-serialization :(
			DONE: Find a way to list all objects for troubleshooting
			IN-PROC: Try using child schema's in Marshmallow to reduce the count of duplicate objects?
				NOTE: Getting errors due to Nested "base" value (??); How to solve?
			DONE: Return to pre-serialization case and test object counts
				NOTE: Only 1 feront_gate
			DONE: Create stackoverflow ID
			DONE: Create an mwe (minimal workable example)
			DONE: Write up problem for stackoverflow post
			DONE: Post problem on stackoverflow
			DONE: Added pickle to question tags
			DONE: Edited post for output clarity. Read up on reputation (short answer is that I don't have enough to offer a bounty)
			DONE: A bit more research and tuned my post. If no answers soon then I need to go earn some rep and offer a bounty
			DONE: Appears that Pickle will meet my needs - but still no anwsers to my question :(
			N/A: Respond to posts as needed to get answers (no one ever answered)
			DONE: If nothing works for marshmallow, try pickle - sure enough, pickle worked
	DONE: Detailed answer:
		https://stackoverflow.com/questions/68439591/marshmallow-creating-duplicate-python-custom-objects-on-de-serialization/68510952#68510952

DONE: implement pickle for stateful text files
	DONE: comment marshmallow refs and move stateful_dict to init
	DONE: Work out the details of interp_helper declaration calls... maybe re-org interp?? Merge helper files??
		DONE: Move code around to prepare for separate merged module for interpreter and interp_helper
		DONE: clean up old code comments!!!
		DONE: merge interp_helper and interpreter
	IDEA: Approach to Serializing with pickle
		DONE: 1) Have dc3_init put all objects & stateful_dict in obj_lst and write obj_lst to default_obj_pickle file
		DONE: 2) On First Run: load default_obj_pickle; 
		DONE: 3) On finish, call routine to save obj_lst to save_obj_pickle file
		DONE: 4) On Subsequent runs: load save_obj_pickle
		DONE: As feared, obj variable declaration is a challenge... for now, just merge wrapper & interp and do it ugly
		DONE: comment out dc3_init import, comment out stateful_dict passing; Test!!!
		DONE: Still struggling with globalizing object variables... maybe make first pass a special case?? real interpreter always loads save?
			IDEA: Maybe 'if... else...' in main... 
			IDEA: call startup.py module if first pass - which loads defaul, buffers opening, and saves save file... else call interpreter
			IDEA: interpreter assumes load from save pickle and calls config module from module imports
			DONE: created startup() for initial load and then called updated object values from pickle save
			DONE: main and interpreter in separate modules
			DONE: troubleshoot "none itterable" error on "i" or "n"
			NOTE: turns out I wasn't returning values on many of the interpreter returns
		DONE: Amazingly, clode is running - but really shouldn't be - I am frequently NOT saving state on return
			DONE: Need to institute some sort of wrapper() function in interpreter module that will call interpreter and ensure state saves
			DONE: Now save_obj_pickle is not getting over-written in start_me_up() - need to sort that out
			IN-PROC: Turns out I'm not writing pickle_obj_save for some reason... need to give directory??
			IDEA: I get it now... not a directory problem
			IDEA: for some reason (probably because I import wrapper in main) obj_init2 is getting called before start_me_up()
			IDEA: This means that we are reading the OLD values of save_obj_pickle before we over-write them with defaults in start_me_up()
			DONE: How to fix???
			DONE: Got it working - just moved the import of obj_init2 to *after* start_me_up() !!
			DONE: Comment troubleshooting prints
			DONE: Comments clean up!!
	DONE: v3.20 complete!!


##########################
### VERSION 3.30 START ###
##########################

Version 3.30 Goals:
	Create antechamber room and contents
	Start of game assignment for torn note code
	Do some code housekeeping (re-instate polymorphism, elim coding duplication)
	(no creatures, state machines, or conditional events)

DONE: figure out why Working Copy isn't showing old git commits (had to upgrade to Pro)
DONE: for all objects create descript_key field
DOEN: Create base classes and objects
	DONE: create antechamber, torn_note, and messy_handwriting
	DONE: Create protcullis, alcove, and control panel
		DONE: iron_portcullis = Class Door (locked but no key)
DONE: Fix paths dictionary - can't have multiple identical keys
DONE: Eliminate start_me_up
DONE: Sort out initial print - all printing needs to happen in main!!
DONE: Clean up print sort-out comments
DONE: create random number code and attach to messy_handwriting
DONE: Change room objects back to polymorphism (will be glad I did this when switches arrive)
DONE: Clean up comments in classes, demo, & helper
DONE: Clean up double instance of scope check (helper & demo)
DONE: Comment clean-up


##########################
### VERSION 3.33 START ###
##########################

Version 3.33 Goals:
	Update first 3 rooms with full desciptions and view-only objects
	Add 4th room and contents
	Code clean-up / function isolation demo module (??)
	(no creatures, state machines, or conditional events)

DONE: Go back and update descriptions and view-only objects from DCv2
	DONE: Update Entrance and Universal descriptions
		DONE: Add moat object to entrance
		DONE: Capitalize usable nouns in the Entrance
	DONE: Update Main Hall descriptions
		DONE: Remove test objects (chest, brass key, potion)
	DONE: Update Antechamber descriptions
		DONE: How to "lock open" the Iron Portcullis? Need to alter the Class Method to check for locked on close?
	DONE: Add Throne Room and ViewOnly descriptions
		DONE: Add Throne Room items: Throne, Silver Key, Scroll, Letters
		DONE: Add throne_room container: Crystal Box and Calligraphy


##########################
### VERSION 3.35 START ###
##########################

Version 3.35 Goals
	New class for Food

DONE: New Class
	DONE: create Food Class (child of Item) with eat method
		DONE: Crete cheese_wedge obj
		DONE: create stale_biscuits obj (with Trademark)
DONE: Pull eat description from descript_dict
DONE: provide useful error on trying to examine writing (advise player to 'read')
	NOTE: Is non-trivial since 'Writing' does not have an examine method. Added guidance in 'help basic' instead


##########################
### VERSION 3.38 START ###
##########################

Version 3.38 Goals
	New class for Beverage
	random responses to wrong direction commands ;-D

IDEAS: Portcullis Door:
- For portcullis, maybe fix unlock method to say “no keyhole” in key == None ?

IDEAS: For Drink Class
	- Containers can never be taken because they are children of Doors which are children of ViewOnly
	- and we don't want container methods anyhow (open, close, lock, unlock)
	- So create new Jug class as child of Item
	- inspect container scope check… I think it just checks for ‘contains’ attribute? 

DONE: Add "no keyhole" error message on key == NONE (portcullis case)
DONE: Create Jug class to support takeable containers that can't hold anything but Beverage
DONE: Create Beverage Class (child of ViewOnly) with drink method
		DONE: Create glass_bottle obj filled with water obj
DONE: Random wrong direction responese


##########################
### VERSION 3.40 START ###
##########################

Version 3.40 Goals:
	Review interpreter code to understand flow and cases
	Extract method 'execution' and move to a separate routine called by wrapper
	Clean-up unneeded 'return's in bottome portion of interpreter
	implement unknown word random responses

IDEAS (structure):
- Naming convention: Room Events, Warnings, Machines, and Creatures are all types of Conditional Events (CEs)
- Different types of CEs (Conditional Events):
	- Room Events = always pre-action
	- Warnings = always pre-action
	- Machines = always post-action (exisitng machines = control panel, throne, kinging scroll)
	- Creatures = pre-action and post action

FINDINGS (from reviewing interpreter code (true for now at least):
- an error will never trigger a CE
- a true_one_word command will never trigger a CE
+ converted_one_word commands CAN trigger Room Events
	- Note: In this case, "north" is converted to "go north" and is then handled as special case 'go' below
* special case 'go' can trigger a Room Event
* for now at least, no CEs are triggered by special case 'put' commands (but they could be!)
- CEs are not triggered by special case 'help' commands
* final 'try' is where all non-Room Event CEs are triggered

IDEAS (implementation):
- don't need to return to wrapper command strings - could just return case (error, tru_1word, go, help, put, 2_word) and word_lst
- for case == error, tru_1word, or help no need for execution
- for case == go, put, or try - wrapper sends case and word_lst to cmd_execution()
- Check for Room Event triggers before (possibly in place of) cmd_execution()
- Check for Warning triggers before (possibly in place of) cmd_execution()
- Check for Machine triggers after cmd_execution()
- Check for Creature triggers both before and after cmd_execution()

MORE IDEAS: Maybe implement Room Events similar to paths via dictionary in each room obj?
- Still need an obj to hold data for CE and a function to execute it
- Idea is that death by croc would be the Room Event and Saved by Weapon would be a pre-action trigger?

DONE: Review interpreter code to understand flow and cases
DONE: Clean-up 'return's in interpreter to support case approach
IN-PROC: Separate 'interpret' and 'execute method' portions of interpreter()
	DONE: Return 'case' and 'word_lst' to wrapper from interpreter
	DONE: Create cmd_execution() function in demo module; pass it 'case', 'word_lst', and stateful_dict
	DONE: Comment out 'tries' in interpreter()
	DONE: Clean up comments
	DONE: Review / optimize interpreter() code
DONE: Provied 'read help' option that explains where to use examine vs. read
DONE: Improve read error
DONE: implement unknown word random responses in cmd_execute() and interpreter()
IN-PROC: Create a scope_error() function for Class socope checks (they repleat a lot!)
	DONE: put case
	DONE: clean up comments
	DONE: 2word case (non-read)
	DONE: 2word case (read)
	DONE: Fix 2word case
	DONE: Fix water scope checks in class
	DONE: Clean up comments


##########################
### VERSION 3.42 START ###
##########################

Version 3.42 Goals
- Create methods to get & set game_state attributes & introduce GameState class

IDEA (Suggestions from Franco):
- container hasattrib => method in Writing
- implement gets & sets (see Writing get_description example)
- think about implementing stateful_dict as Class = GameState; Could hold dict and create gets and sets to change / access game_state
- Franco: think about using dictionary of functions
- Make scope_check() a method of game_state (which is an obj of class GameState)
- Use gets and sets for objects (including CEs)!! => obj are black boxes
	- Maybe not needed in many cases but since I want to convert code to DB back end is a good idea for my use case
- Franco: consider having a 'game turn' across all or many objects

PRINICPLES:
- encapsulate the sets and gets of all custom object attributes
	- direct object access is a standard pythonic trait... but in my case I plan to eventually move obj attributes to a DB - so this is vital
- If a routine acts on a custom object it should be a method of the object's (or it's parent object's) class
	- Example: get_contents_str()
- if a rountine acts strictly on a Python primative class (e.g. a list) - then it should be a function. 
	- Often this is the case when a routine applies to the attribute of multiple different classes.
	- Example: obj_lst_to_str()
- make methods and functions as functional as possible while still being broadly applicable.
	- For example, if you always need to handle a case for len(list) == 0, handle it in the same function code that produces the non-0 result

IN-PROC: Simple Refactoring
	- DONE: replace hasattr() with is_container() methond [should not be inspecting obj directly]
		- DONE: Create is_container() method in class Writing
		- DONE: Replace hasattr intances
		- DONE: Clean-up comments
	- IN-PROC: search for obj method opportunities in class & demo modules - classes should be black boxes
			- DONE: @property and setters & getters for Writing & ViewOnly
				- DONE: get_full_name(), has_writing(), get_writing_full_name()
				- DONE: invetigate @properties for get_full_name()
				- DONE: convert classes and demo modules back to using full_name via @properties
				- DONE: Clean up comments
				= DONE: Try passing stateful_dict to description routine
				- DONE: Clean up comments
				- DONE: @property for descript_key
				- DONE: clean up comments
				- DONE: reamining setters for Writing & ViewOnly
					- DONE: _name
					- DONE: clean up comments
					- DONE: _root_name
					- DONE: clean up comments
			- DONE: Room class
				- DONE: @property for _features, _room_obj_lst, and _door_paths
				- DONE: clean up comments
				- DONE: container_desc() func => get_contents_str() method of Writing with is_container and is_open tests
				- DONE: clean up comments
				- DONE: obj_lst_to_str() func => obj_lst_to_str() func w/ lst test (ErrorValue) via instance(self, list) ; inlucde str convert
				- DONE: clean up comments
				- DONE: incorporate "nothing" condition into obj_lst_to_str()
				- DONE: Clean up comments
				- DONE: remove room examine scope check - already taken care of via execute scope check
				- DONE: Clean up comments
				- DONE: encapsulate room.door_path access in get methods
			- DONE: Create GameState class & game_state obj
			- DONE: attributes = dynamic_desc_dict, map_dict, static_obj_dict (holds universal), state_dict
			- DONE: implement dynamic_desc_dict
				- DROP: figure out @property usage for dicts
				- DONE: create setter & getter for dynamic_desc_dict
				- DONE: Figure out where to declare game_state and how to reference it in classes... send email to Franco
				- DONE: implement boostrap routine as suggested by Franco
				- DONE: comment clean-up
				IN-PROC: implement map_dict
					- DONE: Create getters
					- DONE: Initial troubleshooting
					- DONE: more complex troubleshooting
					- DONE: obj ID not being retained with game_state... 
					- DONE: have proven that obj start with same IDs (in dc3_init module)
					- DONE: investigate wrapper save... maybe call save module??
					- DONE: Now antechamber fails after Entrance but works after Throne Room... need review class coding carefully
						- IDEA: This happens because I am testing with game_state for 'passages' but 'stateful_dict' for open doors...
						- IDEA: so Entrance => Main Hall = open door = works
						- IDEA: Main Hall => Antechamber = passage = fails
						- IDEA: Antechamber => Throne Room = open door = works
						- IDEA: Throne Room => Antechamber = open door = works
					- DONE: setup testing to print Antechamber id vs. game_state Antechamber id every turn and figure out where they diverge
						- DONE: map out module calls
						- DONE: ensure that game_state is not declared multiple times during classes moduel calls (didn't seem to change anything)
						- IDEA: fundamentally I think I am defining all variables twice somehow... 
						- IDEA: and because game_state is declared early it is getter the first assignment and conflicting with the 2nd
						- DONE: create print statements to track pickle dumps and loads
						- DONE: Review and confirm module model
						- DONE: looks like pickle is only loaded once during wrapper import (???); try moving pickle load to wrapper loop
						- IDEA: investigated creating a separate dc3_wrapper module that would then call interpreter & cmd_execute from demo...
							- IDEA: this won't work... wrapper needs access to stateful dict...
							- NOTES: I confirmed that, by default, pickled objects don't retain their obj id
							- IDEA: I'm thinking here's what I need to do:
								- DONE: 1) return to pickle loading in wrapper at the start of every loop (and stop calling init2)
								- DONE: 2) pack obj variables and pass them to interp and cmd_exe (or maybe pass as master_obj_lst ??)
						- NOTES: I am now pickle dumping & loading every turn in wrapper and formally passing obj to interpreter - an am *still* getting dups in classes get_next_room() method... I need to double down on troubleshooting this method in ugly detail 
							- DONE: check if there is a duplicate of of game_state - there is
							- DONE: Determine when duplicate game_state is created => after init but before middle of wrapper
							- NOTE: One version of game_state keeps the same id from the start... presumably this is not the pickled version?
							- TBD: Keep troubleshooting to find out exactly where the duplicate game_state shows up; special focus on classes declaration
						- NOTES: So, the original game_state is not getting deleted, and now that I'm instantiating a new version I get 2 old game_state versions... need to dig deep into the classes bootstrap - that's where the issue lives... game_state1 never gets deleted and game_state2 gets created twice... ???
						- I fundamentally need to reconsider my bootstrap approach... I will go back to adding values....
						- NOTES: turns out I have duplicates of other obj (Doors) as well
						- DONE: figure out why delete is not working in init; also, why dups?? - learning more about gc.get_objects() and sys.refcount()
						- DONE: Try checking refs on problem version of obj?? - Both obj sets have many ref (but first static set has more)
						- NOTE: there are 2 obj sets - the initial one from init declaration that never changes id; And a 2nd set that changes every move... presumably loaded from the pickle? It appears that we don't actually need to load from pickle?
						- DONE: track problem antechamber obj id - so the PROBLEM is the FIRST set of objects... the ones that never change... perhaps they never get updated?? For some reason, game_state._paths is pointing to this first set... and when they are called no room_obj can be interacted with... ???
						- DONE: tested running dc3_init on its own (to initialize the pickle dump), commenting out the import of dc3_init, and then running main - worked great until tried to go to antechamber (key error on game_state._paths)... so this seems to be the answer!
						- DONE: check refs on gamestate at end of class (5 references)
						- DONE: Create start_of_game variable in main and pass to wrapper
						- DONE: Move initial room print to wrapper start of game routine
						- IN-PROC: Still need to figure out how to avoid game_state dup... that's my one problem case... maybe delete at end of class?
							- IDEA: maybe a custom start_of_game case where defautl_pickle doesn't include game_state (NO GAMESTATE IN DEFAULT PICKLE)
							- IDEA: game_state gets updated and added to new game pickle? then pickle is immediately loaded in main routine?
							- DONE: Create a "default pickle" file to load (and a script to gen it up)
							- DONE: in start_of_game section of wrapper, load default_obj_pickle (NO game_state included)
							- DONE: in start_of_game section of wrapper, configure game_state
							- DONE: in start_of_game section of wrapper, dump save_obj_pickle2 (WITH game_state included!)
						- NOTE: Again, there are 2 obj sets - the initial one from init declaration in the start-up section of wrapper, that never changes id; And a 2nd set that changes every move... the PROBLEM is the FIRST set of objects... the ones that never change... For some reason, game_state._paths is pointing to this first set... and when they are called no room_obj can be interacted with... ???
							- NOTE: I seem to be back where I started... I think the next step is to make wrapper "start-up" a separate module... if that doesn't work - and I don't think it will - I need to go back and re-diagram the whole thing based on what I now understand about variables and objects
							- DONE: Create start-up module (no change in duplicates)
							- IDEA: so now I have isolated the initial object declarations in start_me_up() and the every-turn declarations in wrapper() in separate modules... and I still have the duplicates issue...
							- DONE: clean up comments and trouble-shooting - need to make the code readable again
							- DONE: v1 detailed module / imports mapping
							- DONE: v2
							- DONE: Track program flow to determine order of ops
							- DONE: Analyze code run order - in what order does my code actually run? Number on diagram
							- IDEA: Maybe classes, static, and helper in memory from main?? Convert calsses to function??
							- DONE: tired converting classes to a function in a classes2 module... 
								- NOTES: this doesn't work either because the class definition remains in the scope of the classes2 module... 
								- NOTES: so start_me_up knows nothing about GameState...
							- IDEA: Instead, I need to make 2 separate modules: define_class_gs and define_class_other..
								- IDEA: then I import each in the body of start_me_up and wrapper
								- IDEA: in start_me_up, between the class definitions, I declare game_state
								- DONE: create define_class_gs and define_class_other
								- NOTES: Making progress but now define_class_other knows nothing about game_state... need to find a way to pass it in?
								- NOTES: No, issue is that game_state has not yet been defined in wrapper
								- DONE: updated description method so that game_state is not required
								- DONE: pass game_state in to go method!!! (suggested by JE)
								- NOTES: Yes - THIS WORKS!!! NO DUPS!!! 
							- DONE: full implementation of game_state._paths
							- DONE: rename game_state to active_gs
							- DONE: comment clean up
							- DONE: now that I'm passing active_gs, simplify classes => single standard import
							- DONE: Mark unused modules
							- DONE: move active_gs declaration to default_pickle
							- DONE: clean up comments
							- DONE: Declare v3.42 complete!


##########################
### VERSION 3.44 START ###
##########################

Version 3.44 Goals
- After the massive mess that was the introduction of GameState in v3.42 the goals of 3.44 are hopefully simpler
- 1. With troubleshooting messages still in place, re-architect modules
- 2. sort out efficient variable handling
- 3. eliminate bad usage (e.g. eval and global)
- 4. re-map module calls
- 5. clean-up troubleshooting prints and comments 

DONE: move wrapper() to its own module
DONE: fully comment out old wrapper within dc3_demo
DONE: sort out interpreter()
	DONE: Sort out "put" command
	DONE: Sort out interpreter master_obj_lst declaration & passing - commented out
	DONE: found and fixed small_print => small_printing error (root_name conflicted with reserved command 'print')
	DONE: move stateful_dict and active_gs to front of declarations
	DONE: sort out use of eval
	DONE: sort out noun_handling master_obj_lst declaration & passing
	DONE: clean up comments
	DONE: update word2 => word2_txt in noun_handling()
	DONE: do I really need to pass stateful_dict to interpreter() & noun_handling() if I'm already passing master_obj_lst
		- DONE: stop explicitly passing stateful_dict to interpreter()
		- DONE: clean up comments
		- DONE: stop explicitly passing stateful_dict to noun_handling()
		- DONE: clean up comments
	DONE: examine limits to declarations in start_me_up and wrapper
		- DONE: remove full obj declarations from start_me_up() and just declare stateful_dict and active_gs
		- NOTE: garbage collection still has all obj in scope once master_obj_lst is unpickled!
		- DONE: comment clean-up
		- DONE: remove full obj declarations from wapper() and just declare stateful_dict and active_gs
		- DONE: comment clean-up
	DONE: move help, error, and tru_1word case execution from interpreter() to cmd_execute()
		DONE: move help routine to cmd_execute()
			DONE: move help() call to cmd_execute()
			DONE: clean up comments
			DONE: clean up help() routine
			DONE: clean up comments
		DONE: move tru_1word routines to cmd_execute()
			DONE: move true_one_word() call to cmd_execute()
			DONE: move true_one_word() to cmd_execute() and move inventory() to dc3_helper()
			DONE: clean up comments
		DONE: move error output & turn decrementing to cmd_execute()
			DONE: exit_state => error_state in both noun_handling() and interpreter
			DONE: pass interpreter() errors to cmd_execute() and update wrapper and add move_dec()
			DONE: pass noun_handling() errors to cmd_execute()
			DONE: clean-up comments
			DONE: update wrapper
			DONE: move random routine to cmd_execute()
			DONE: clean-up comments
	DONE: move interpreter() to its own module
		DONE: create dc3_interpreter()
		DONE: migrate interpreter() routines to dc3_interpreter module
DONE: sort out cmd_execute()
	DONE: move ALL case execution to this module
	DONE: move cmd_execute() to its own module
DONE: fix any remaining 'Someday's below
DONE: make end() a module and call from wrapper()
DONE: create dc3_score() module based on stateful_dict values and call from wrapper
	DONE: create score_val_dict in dc3_static
	DONE: create points_earned_dict in stateful_dict (same key as score_val_dict)
	DONE: call score() from wrapper()
	DONE: complete and test score(
DONE: Full testing (note: there's still an extra call of helper() from main that I don't quite understand: SOLVED! artifact from helper in end)
DONE: re-map modules and var passing
DONE: clean up troubleshooting comments & prints!!!
DONE: move un-unsed modules to 'old versions' directory
DONE: finalize version

Someday: fix game_state as global
Someday: fix root-word var passing of master_obj_lst
Someday: clean up *very* ugly master_obj_lst passing 
	- really the only function that needs this is the one that converts strings to obj...
	- maybe I can solve that by just passing master_obj_lst and checking to see if str = the name of a member of master_obj_lst
	- or Someday: Eliminate eval using class-based-dict; link: https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
someday: do we really need to declare objs in wrapper??
	- can I just load master_obj_lst from the pickle and pull from it selectively?
	- the only thing I really need to use all the time out of master_obj_lst is stateful_dict and active_gs
someday: ditto for start_me_up


##########################
### VERSION 3.46 START ###
##########################

Version 3.46 Goals:
- Refactor code to migrate variables from stateful_dict => active_gs

Notes:
- Approach is to migrate variables one sub-dict at a time
- Within main dict, migrate one var at a time

DONE: Refactor stateful_dict['paths']
DONE: Refactor stateful_dict['points_earned_dict']
	DONE: add points_earned_dict to GameState vars and define active_gs values in make_default_pickle()
	DONE: pass active_gs to dc3_score
	DONE: create method to get and set score state for a given score_key
	DONE: For items - update score() to use active_gs score state
	DONE: For rooms - update score() to use active_gs score state
	DONE: comment out stateful_dict points_earned_dict
	DONE: clean up comments
DONE: "Easy" use cases = 'current_score', 'score', 'move_counter', 'end_of_game', 'game_ending'
	DONE: current_score & score
		DONE: add 'score' to active_gs.state_dict (and clean up class_deff comments & prints)
		DONE: create increase_score() method for GameState
		DONE: update score() function to call increase_score() method
		DONE: create get_score() method in GameState
		DONE: update print_score() func in helper module to call get_score() method
		DONE: comment out 'score' in stateful_dict
		NOTE: is stateful_dict['score'] even being used???
		DONE: comment out 'score'
		DONE: clean up comments
	DONE: 'move_counter'
		DONE: add 'move_counter' to active_gs.state_dict
		DONE: create 'move_inc' method in GameState to increment moves
		DONE: create 'move_dec' method in GameState to decrement moves
		DONE: update wrapper() with move_inc
		DONE: update cmd_exe() 'errors' and 'quit' with move_dec
		DONE: create 'get_moves' method in GameState
		DONE: update end() with get_moves
		DONE: comment out 'move_counter' in stateful_dict
		DONE: clean up comments
	DONE: 'end_of_game' & 'game_ending'
		DONE: add 'end_of_game' & 'game_ending' to active_gs.state_dict and run mk_default_pkl()
		DONE: create get & set 'end_of_game' in GameState
		DONE: create get & set 'game_ending' in GameState
		DONE: update 'quit' in cmd_exe() with set_game_ending
		DONE: update wrapper() with get_game_ending & get_end_of_game
		DONE: update end() with get_game_ending and set_end_of_game
		DONE: update start_me_up()
		DONE: test updates
		DONE: comment out 'end_of_game' & 'game_ending' in stateful_dict & run mk_defaul_pkl()
		DONE: clean up comments
DONE: 'universal'
	DONE: add 'universal' to active_gs.state_dict and run mk_default_pkl()
	DONE: create get_static_obj method in GameState
	DONE: in cmd_exe() '2word' and 'put' cases pass active_gs to scope_check() & writing_check()
	DONE: in helper() pass in active_gs to scope_check() & writing_check() and pass active_gs to scope_list()
	DONE: in helper() pass in active_gs to scope_list and update 'universal_lst' with get_universal_scope
	DONE: from noun_handling(), pass active_gs to root_word_count()
	DONE: from root_word_count, pass active_gs to scope_lst()
	DONE: test updates
	DONE: comment out 'universal' in stateful_dict and run mk_default_pkl()
	DONE: test updates
	DONE: clean up comments
DONE: pass active_gs to all class verb methods
	DONE: troubleshoot examine.door error
		DONE: solve bug (scope_check in examine sub for door)
		DONE: clean-up comments
	DONE: '2word' case = read
		DONE: in "try" from '2word' case create if 'read'
		DONE: add active_gs to method
		DONE: test
	DONE: '2word' case = eat
	DONE: '2word' case = drink
	DONE: '2word' case = take
	DONE: '2word' case = drop
	DONE: '2word' case = close
	DONE: '2word' case = lock
	DONE: '2word' case = unlock
	DONE: '2word' case = open (2 methods)
		NOTE: learned I need to pass active_gs in super
	DONE: '2word' case = examine (many methods!)
		DONE: Update in cmd_exe() tru_1word() too
		DONE: Update in Room 'go' method in class_def()
	DONE: remove if & try for 2-word case
	DONE: clean-up comments
	DONE 'put' case
		DONE: put => active_gs
	DONE: in cmd_exe() create rand_error() function
DONE: Refactor stateful_dict['dynamic_desc_dict']
	DONE: move dynamic_desc_dict from stateful_dict to active_gs
	DONE: comment out stateful_dict sub-dict and re-run mk_default_pkl
	DONE: clean up comments
IN-PROC: 'backpack'
	DONE: add 'backpack' to active_gs
	DONE: investigate 'backpack' usage
	DONE: create get_backpack_lst method in GameState
	DONE: create backpack_lst_append method in GameState
	DONE: create backpack_lst_remove in method GameState
	DONE: add active_gs backpack methods to modules and comment out stateful_dict
		DONE: Update scope_lst() in helper(), inventory() in helper(), take() method in Item class_def()
		DONE: comment out stateful_dict
		DONE: clean up comments
DONE: 'hand'
	DONE: add 'hand' to active_gs
	DONE: create methods: get, append, remove
	DONE: Update helper(), class_def(), & score()
	DONE: comment out stateful_dict 'hand'
	DONE: testing!!
	DONE: clean-up comments
TBD: 'room'
	DONE: add 'room' to active_gs
	DONE: create methods: get & set
	DONE: update score(), helper(), cmd_exe(), interpret(), class_def()
	DONE: comment out stateful_dict 'room'
	DONE: detailed testing: score(), helper(), cmd_exe(), interpret(), class_def()
	DONE: clean-up comments
IN-PROC: 'out_buff' & buffer()
	DONE: add 'out_buff' to active_gs
	DONE: create methods: get & buffer
	DONE: in wrapper(), get and combine both stateful_dict and active_gs buffers and pass the combined out_buff to main()
	IN-PROC: update modules:
		DONE: document N/A modules: score(), interpret(), mk_default_pkl(), wrapper(), static(), main()
		DONE: end()
		DONE: create reset_buff method in GameState and call it in wrapper()
		DONE: start_me_up()
		DONE: helper()
			DONE: print_score()
			DONE: inventory()
		DONE: cmd_exe()
			DONE: help()
			DONE: true_one_word()
			DONE cmd_exe()
		IN-PROC: class_def()
			DONE: Writing()
				DONE: print_contents_str()
				DONE: read()
			DONE: ViewOnly()
				DONE: examine()
			DONE: Room()
				DONE: examine()
				DONE: go()
			DONE: Item()
				DONE: take()
				DONE: drop()
			DONE: Door()
			DONE: Container()
			DONE: Food()
			DONE: Beverage()
	DONE: test without stateful_dict buffer being added to out_buff		
	DONE: comment out stateful_dict 'buffer'
	DONE: detailed testing
	DONE: clean-up comments
	DOEN: update version comment, version static value, and tag in repo, more doc => done


##########################
### VERSION 3.47 START ###
##########################

Version 3.47 Goals:
- Eliminate stateful_dict

DONE: remove stateful_dict
	DONE: helper()
	DONE: score() and end()
	DONE: help() in cmd_exe()
	DONE: interpret()
	DONE: cmd_exe() and class_def()
	DONE: wrapper() and start_me_up()
	DONE: mk_default_pkl() and run
	DONE: update pkl obj index in wrapper() and start_me_up() and interpreter() including noun_handling()
	DONE: search for all master_obj_lst refs
	DONE: final search in every module for stateful_dict


##########################
### VERSION 3.48 START ###
##########################

Version 3.48 Goals
- Migrate most helper() functions to methods of active_gs
- sets and gets for rest of class definitions

IN-PROC: start migrating helper() functions to GameState methods
	DONE: print_score()
	DONE: move obj_lst_to_str() function to class_def() module
	DONE: inventory()
	DONE: integrate open_cont_scan() into scope_lst() {still in helper()}
	DONE: migrate scope_check and writing_check to class_def() GameState methods
		DONE: writing_check moved
		DONE: scope_check moved
	DONE: migrate scope_lst() to class_def() GameState method
	DONE: mark helper() module inactive
	DONE: comment out helper imports
	DONE: clean up comments
IN-PROC: sets & gets for remaining classes
	DONE: Item
		DONE: troubleshooting 'takable'
		DONE: takable eliminated
		DONE: clean-up comments
	DONE: Door
		DONE: troubleshooting (still working on it)
		NOTE: solved it!! After each class def change I need to re-run mk_default_pkl() !!!
		DONE: open_state
		DONE: unlock_state
		DONE: key
	DONE: Container
		DONE: Eliminate takable
		DONE: clean up contents
		DONE: Contains
			DONE: @property getter
			DONE: investigate room_obj append & remove
			DONE: investigate contains append & remove
	DONE: Food
	DONE: Jug
	DONE: Beverage


##########################
### VERSION 3.49 START ###
##########################

Version 3.49 Goals
- code improvement tweaks

DONE: re-order and consolidate 3.50+ plans and ideas
DONE: search "somedays" for others
DONE: Is the Item class worth having? (decision = 'yes')
DONE: obj-not-in-hand error in cmd_exe()
	DONE: Strange "blank line" error on trying to put item in box if item is already in box
	NOTE: Very conflicted re balance between less repitition vs. less readible & less customizable; Pondering
	DECISION: Now that I've started to standardize hand_check() I've realized the code was more readable & customizable before
		IDEA: maybe implement a simple boolean function instead
	DONE: drop, unlock, lock reversed
	DONE: reverse put
	DONE: solve the 'blank response if try to put item in closed container when it's already in the container' (problem in scope_lst() I think)
		NOTE: turns out blank happens any time you try to put a not-in-scope noun in box
		NOTE: Appears the cmd_exe() put routine never runs if obj_noun is not in scope???
		NOTE: works for put "full name" cases but NOT for put "root name" cases
		DONE: check root_word_count() in interpreter()
		NOTE: found it! problem is that noun_obj generates the error BUT, I am showing the dir_obj error_msg (doesn't exist because there is a box)
		NOTE: need to generate a global "put" error_msg based on whichever clause triggers an error = True
		DONE: fix it
		DONE: clean up troubleshooting print statements
	DONE: clean up old hand_check()
	DONE: boolean version of hand_check()
	DONE: clean up comments
	DONE: maybe also a hand_empty() ?
DONE: create 'coding decisions' file
DONE: Better errors for "read note" and "get water" and "examine lettering"
	IDEA: maybe a 'special errors' funciton in cmd_exe() ??
	DONE: 'read' <non-writing>
	DONE: 'examine' <writing>
	DONE: 'take' <beverage>
		DONE: create method is_beverage() in Writing
		DONE: create 'take' <beverage> special error
	DONE: function for special errors
	DONE: clean up comments
DONE: fix dup Room 'go' code for doorways and passages
	DONE: clean up comments
DONE: clean up use of "import *"
	DONE: static_init
		DONE: move score dicts / lists to score() module
		DONE: clean up comments
		DONE: move help() to interpreter()
		DONE: clean up comments
		DONE: move languate dict & lst to Interpeter
		DONE: clean up comments
		DONE: write up code decision
	DONE: class_def
		DONE: module other than intperter() and cmd_exe()
		DONE: interpreter() & cmd_exe()
		NOTE: to my surprise, class_def() is not needed in any module other than mk_default_pkl() - who knew!
		DONE: clean up comments
DONE: move & rename modules
	DONE: create \dark_castle3 directory at git root
		DONE: create \doc sub-directory
	DONE: populate \docs
		DONE: dc3_done.md => done.md
		DONE: dc3_doc.md => to_do.md
		DONE: dc3_coding_decs.md => decisions.md
	DONE:npopulate \dark_castle3
		DONE: dc3_static_init.py => static_gbl.py
		DONE: dc3_main.py => web_main.py
		DONE: dc3_class_deff.py => class_def.py
		DONE: dc3_ wrapper.py => app_main.py
		DONE: dc3_start_me_up.py => start_up.py
		DONE: dc3_interpreter.py => interp.py
		DONE: dc3_cmd_execute.py => cmd_exe.py
		DONE: dc3_score.py => score.py
		DONE: dc3_end.py => ending.py
		DONE: make_default_pickle.py => mk_def_pkl.py
	DONE: create other std sub-dierectories (model off of dc2)
	DONE: rename all module imports within code
	DONE: make default pickle
	DONE: test
DONE: Determine need for 'import sys'
	NOTE: wasn't really neaded - I wasn't using any sys commands.. so removed all sys imports for now
DONE: map object attributes, verb methods, and inheritance visually
DONE: re-map modules


##########################
### VERSION 3.50 START ###
##########################

Version 3.50 Goals
- create travel effects interactive obj

DONE: implement RoomEffect for simplest case (go south from entrance)
	DONE: add invis_obj_lst as Room attribute
		DONE: update class definition & create @property
		DONE: update mk_def_pkl Room instantiations
		DONE: run mk_def_pkl
	DONE: add Invisible class as parent of Writing (attributes = name)
		DONE: run mk_def_pkl
		DONE: clean up comments
	DOEN: add TravelEffect class as child of Invisible class
		DONE: initial attributes = cmd_trigger_lst, effect_desc, cmd_override, inter_obj_type
	DONE: in mk_def_pkl instantiate TravelEffect obj
		DONE: declare entrance_south
		DONE: in mk_def_pkl add TravelEffect obj to entrance Room obj
		DONE: add entrance_south to def_pkl dump
		DONE: effect_desc to descript_dict
		DONE: run mk_def_pkl 
	DONE: create TravelEffect methods
		DONE: create trigger_check() method for TravelEffect
		DONE: create initial trigger() method for TravelEffect
			DONE: buffer  effect_desc
	DONE: create method in active_gs to return list of in-scope inter_obj
	DONE: create pre-action_cmd() module
		DONE: for inter_obj in pre_action_lst: trigger_state = trigger_check() method
		DONE: if trigger_state, cmd_override = trigger() method
		DONE: return cmd_override
	DONE: update app_main
		DONE: add cmd_override = pre_action_cmd()
		DONE: cmd_exe() only gets called if cmd_override == False
	DONE: test

DONE: entrance_east and eantrance_west (simple death cases)
	DONE: add attributes to TravelEffect
		DONE: add game_ending attribute to TravelEffect class (including assignment and @property getter)
		DONE: update entrance_south with game_ending = None
		DONE: run mk_def_pkl
		DONE: test
	DONE: create new TravelEffect obj
		DONE: create entrance_east and entrance_west with game_ending = 'death'
		DONE: add entrance_east and entrance_west to entrance.invis_obj_lst
		DONE: add entrance_east and entrance_west to def_pkl dump
		DONE: add entrance_east and entrance_west to descript_dict
		DONE: run mk_def_pkl
		DONE: test
	DONE: update TravelEffect trigger()method
		DONE: if game_ending not None: active_gs.set_game_ending(game_ending)
		DONE: test

IDEA: east / west TravelEffect obj I will eventually want:
- entrance_east_no_weap
- entrance_east_weap_1st
- entrance_east_weap_repeat

IDEA: additional capabilities I need to go from entrance_east to entrance_east_no_weap
- additional attribute = not_in_hand_cond

DONE: entrance_east_no_weap and eantrance_west_no_weap (full death cases)
	DONE: add attributes to TravelEffect
		DONE: add in_hand_lst and in_hand_cond attribute to TravelEffect class (including assignment and @property getter)
		DONE: update entrance_south with in_hand_cond = None and in_hand_lst = []
				DONE: update entrance_east with in_hand_lst = [shiny_sword, grimy_axe] and in_hand_cond = False
				DONE: update entrance_west with in_hand_lst = [shiny_sword, grimy_axe] and in_hand_cond = False
		DONE: run mk_def_pkl
		DONE: test
	DONE: update TravelEffect trig_check() method
		DONE: update to check if in_hand_cond not None: and, if not, for loop to confirm in_hand_lst obj in active_gs.hand_lst matches in_hand_cond
		DONE: test

DONE: can I used active_gs.hand_check() in TravelEffect method trig_check() ?

IDEA: additional capabilities I need to go from entrance_east to entrance_east_weap?
- give_or_take, give_item, put_place
IDEA: to start with, test entrance_east_weap_1st with random mcguffin

DONE: entrance_east_weap and eantrance_west_weap (get item case but no counter yet)
	DONE: create random_mcguffin obj for testing
		DONE: run mk_def_pkl
	DONE: add attributes to TravelEffect
		DONE: give_or_take, give_item, and put_place attribute to TravelEffect class (including assignment and @property getter)
		DONE: update entrance_south, entrance_east_no_weap, and entrance_west_no_weap with new attributes = all None
				DONE: update entrance_east_weap with new attributes = 'give', random_mcguffin, and None
				DONE: update entrance_west_weap with new attributes = 'give', random_mcguffin, and None
		DONE: run mk_def_pkl
		DONE: test
	DONE: create active_gs.put_in_hand(item) method
		DONE: if not hand_empty(), swap current hand_lst to backpack
		DONE: active_gs.hand_lst_append_item(item) 
	DONE: update TravelEffect trigger() method
		DONE: define room_obj
		DONE: check for take_or_give and either active_gs.put_in_hand(give_item) 
				or, if not hand_empty(), put_place.append(hand_lst[0]) and hand_lst[0].remove
		DONE: test

CANCEL: entrance_east_weap_1st (full get item case with counter on first count)
CANCEL: entrance_east_weap_repeat (full get item case with counter after first count)
NOTE: ending v 3.50 early... I have a new modular idea for how to implement machines (with TravelEffect as an invisible machine)


##########################
### VERSION 3.51 START ###
##########################

Version 3.51 Goals
- implement new, modular appraoch to machines in place of RoomEffect

IDEA: taking another run at how machines should work
IDEA: machines should be modular... a bit like rooms
IDEA: instead of counter, implement as got_crown = False => True

DONE: non-destructively disable v3.50 TravelEffect coding
	DONE: comment out app_main() call for pre_action_cmd() module
	DONE: comment out object defs, entrance Room invisble items, and obj adds to def_pickle (and re-run mk_def_pkl)
	DONE: comment out TravelEffect class in class_def() module
	DONE: test
DONE: create machine condition classes, obj, & methods for entrance_east & entrance_west TravelEffect cases
	DONE: NotInHandCond class
		DONE: NotInHandCond is child of Invisible; add attributes & property
		DONE: attributes = not_in_hand_lst
		DONE: in mk_def_pkl(), instantiate hand_no_weap_cond and add to def_pkl
		DONE: run mk_def_pkl()
		DONE: create cond_check() method
	DONE: InHandAndBoolCond class
		DONE: InHandAndBoolCond is child of Invisible; add attributes & property
		DONE: attributes = in_hand_lst, bool_test
		DONE: in mk_def_pkl(), instantiate hand_weap_1st_cond & hand_weap_repeat_cond and add to def_pkl
		DONE: run mk_def_pkl()
		DONE: create cond_check() method
DONE: create machine results classes, obj, & methods
	DONE: BufferAndEndResult class
		DONE: BufferAndEndResult is child of Invisible; add attributes & property
		DONE: attributes = result_descript, ending, cmd_override
		DONE: in mk_def_pkl(), instantiate die_in_moat and moat_crocs_scared
		DONE: run mk_def_pkl()
		DONE: create results_exe() method
	DONE: BufferAndGiveResult class
		DONE: BufferAndGiveResult is child of Invisible; add attributes & property
		DONE: attributes = result_descript, give_item, cmd_override
		DONE: in mk_def_pkl(), instantiate moat_get_crown_result
		DONE: run mk_def_pkl()
		DONE: create results_exe() method
DONE: create InvisMach class & obj
	DONE: Create class
		DONE: class = InvisMach(Invisible)
		DONE: attributes = machine_type, machine_state, cmd_triggers_lst, cmd_cond_lst, result_lst
		DONE: create @properties definitions
	DONE: create obj and add condition and tirgger obj to it
		DONE: create entrance_moat_mach
		DONE: machine_type => pre_action_trigger
		DONE: machine_state => False (got_crown)
		DONE: cmd_triggers_lst => [['go', 'go', 'east'], ['go', 'go', 'west']]
		DONE: cmd_cond_lst => [hand_no_weap, hand_weap_1st, hand_weap_repeat]
		DONE: result_lst => [die_in_moat, moat_get_crown, moat_crocs_scared]
		DONE: add entrance_moat_mach to Room entrance
		DONE: add entrance_moat_mach to def_pkl
	DONE: create InvisMach trig_check() and trigger() methods
		DONE: create trig_check() method
		DONE: create trigger() method
DONE: create pre_action_cmd() module & function
DONE: enable pre_action_cmd() in app_main module
DONE: testing!
	DONE: code runs!
	DONE: die_in_moat cases works!
	DONE: troubleshoot get_crown case
	DONE: troubleshoot crocs_scared case
DONE: create machine condition classes, obj, & methods for entrance_south TravelEffect case
	DONE: PassThruCond class
		DONE: PassThruCond is child of Invisible; add attributes & property
		DONE: attributes = name
		DONE: in mk_def_pkl(), instantiate pass_thru_cond and add to def_pkl
		DONE: run mk_def_pkl()
		DONE: create cond_check() method
	DONE: instantiate object based on BufferAndEndResult class with ending = None
		DONE: name = cant_turn_back, 
	DONE: create machine obj and add condition and result obj to it
		DONE: machine_type => pre_action_trigger
		DONE: machine_vars => None
		DONE: cmd_triggers => [['go', 'south']]
		DONE: cmd_cond_lst => None
		DONE: result_lst => [cant_turn_back] => buffer message, return override == True
	DONE: testing
DONE: clean up all troubleshooting comments & prints
DONE: delete commented out v3.50 code
DONE: test to see if condition and result objects don't need to be in def_pkl independent of the machine obj they're assigned to
DONE: extend player_cmd_key cases in trig_check() method of InvisMach


##########################
### VERSION 3.52 START ###
##########################
Version 3.52 Goals
- Create class, methods, obj, and inventory updates for 'crown' object
- Mini code clean-up

DONE: create crown object
	DONE: review crown functionality in dark_castle2
	DONE: create Clothes class as child of Item
	DONE: attributes = wear_descript, remove_descript, clothing_type
	DONE: create crown obj = royal_crown
	DONE: Add royal_crown to game world
	DONE: update score for crown in hand  (10 pts) [note: in dc2, 5 pts for getting crown & 5 for wearing crown]
	DONE: Update active_gs to include 'worn' attribute
	DONE: Update inventory() function in cmd_exe() module to show 'worn' in inventory
	DONE: test inventory
	DONE: create wear method (should check if other items of same clothing_type are already worn)
	DONE: test
	DONE: clean up test hat
	DONE: create remove method
	DONE: test
	DONE: clean up test hats
	DONE: switch score for royal_crown to 'wear' (10 pts)
DONE: code clean-up
	DONE: Organize GameState class into sections
	DONE: Put active_gs.put_in_hand() in Item class take() method
	DONE: Test
	DONE: Clean up comments
	DONE: Update take() method to include clothes (with remove text)
	DONE: create and implement BufferOnlyResult (make BufferAndEndResult a child)
		DONE: test multi-line imports
		DONE: BufferOnlyResult obj created; BufferAndEndResult is a child
		DONE: change class of entrance_south result to BufferOnlyResult
			DONE: update obj
			DONE: add class to import list
		DONE: clean up comments
	DONE: make BufferAndGiveResult a child of BufferOnlyResult
		DONE: clean up comments
	DONE: extend BufferOnlyResult result_exe method in BufferAndEndResult and BufferAndGiveResult
		IDEA: consider using text 'none' instead of true None 'no state' condition?
			IDEA: didn't seem to be the issue
			IDEA: I think the problem is the return?
		DONE: commented out the 'if not None' clause - no longer need None cases since I have BufferOnlyResult
		DONE: try swapping the position of super() to the end - didn't work - and woouldn't be desired result anyhow...
		DECISION: going to move this one to "Someday Maybe" and call it done for now
DONE: Clothing tweak
	DONE: kill 'remove' method and update 'help basics' to explain that take will get clothes? (otherwise, why not 'remove' from backpack?)


##########################
### VERSION 3.54 START ###
##########################
Version 3.54 Goals
- Create class, methods, and obj for throne room throne machine

DONE: update classes and types of pre and post actions
	DONE: pre_action_com.py module => pre_action.py
	DONE: pre_action_trig => pre_action_cmd_trig
	DONE: comment clean-up
	DONE: cmd_cond_lst => cond_lst
	DONE: comment clean-up
DONE: create class ButtonSwitch  (child of ViewOnly)
	DONE: attributes = switch_state (values = 'pushed', 'pulled', 'neutral') and machine_type (values = 'pre_action_auto_reset')
	DONE: create method push
		DONE: add 'push' to interp() verb list
		DONE: create method def
		DONE: updates switch_state to 'pushed'
		DONE: buffer "Pushed."
DONE: create class SpringSliderSwitch (child of ButtonSwitch)
	DONE: create SpringSliderSwitch method pull (updates switch_state to 'pulled')
	DONE: update throne obj => SliderSwitch class with dark_castle2 description
	DONE: test throne slider
DONE: update pre_action() to check for machine_type 'pre_action_auto_reset' and reset value
	DONE: test throne slider
	DONE: comment out prints
	DONE: Clean up comments
DONE: create class InvisSwitchMach
	DONE: InvisSwitchMach is child of InvisMach
	DONE: standard attributes
	DONE: additional attributes = trig_switch, cond_switch_lst
	DONE: getter properties
DONE: create methods
	CHANGED: update trigger_check() method to check for trig_switch.switch_state != 'neutral'
	CHANGED: update trigger() method to pass cond_switch_lst
	UPDATE: will try to re-use existing InvisMach trig_check() and trigger() as much as possible
	UPDATE: don't think I'll actually need attribute trig_switch_lst
	UPDATE: probably do still need cond_switch_lst and to pass this to conditions in trigger()?
DONE: re-map machines => unify cmd_machine and switch_machine models (if reasonable)
	IDEA: machine types = pre_action_cmd, pre_action_auto, pre_action_swtich, post_action_cmd, post_action_switch, post_action_auto
	IDEA: trigger inputs == case, trig_lst [means that a machine can be triggered by a command or a switch but not BOTH]
	IDEA: cond inputs == game state, condition switch, play commands
	DONE: create updated diagram
DONE: update & define machine variable names and attributes
	DONE: pre_action() local variables:
		DONE: mach_obj_lst == list of in scope machine objects
		DONE: cmd_override == boolean returned from pre_action() function that determines whether or not player command is over-ridden
		DONE: local_override == boolean that ensure if *any* in-scope machine overrides the player command then player command is over-ridden
	DONE: InvisMach attributes:
		DONE: name == name of the machine
		DONE: machine_type => trigger_type == defines machine trigger type and timing. Options include:
			VALS: pre_act_cmd, pre_act_switch, pre_act_auto, pre_act_switch_reset
			VALS: post_act_cmd, post_act_switch, post_act_auto 
		DONE: machine_state == internal state of machine; can be boolean or integer
		DONE: cmd_triggers_lst => trig_vals_lst == list of trigger values that will start the machine; can be player commands or switch values
		DONE: cond_lst == list of condition obj to test for; should cover all trigger cases
		DONE: result_lst == list of possible result obj ordered by assciated condition
		DONE: trig_switch_lst == list of switches associated with the machine that can be used to trigger it
		DONE: cond_swicth_lst == list of switches associated with the machine with states that contribute to conditions
	DONE: trig_check()
		DONE: player_cmd_key => trig_key_lst == trigger state to be compared with trig_vals_lst
DONE: create condition classes & obj:
	DONE: case = broach_already_dispensed => machine_state == True
		DONE: create StateCond class
		DONE: create obj broach_dispensed_cond
	DONE: throne_push_pre_dispensed => switch_state = pushed => cond_switch_lst[0] == 'pushed'
		DONE: create SwitchStateCond
		DONE: create throne_push_cond obj
	DONE: throne_pull_pre_dispense: switch_state = pulled => cond_switch_lst[0] == 'pulled'
		DONE: use SwitchStateCond
		DONE: create throne_pull_cond obj
DONE: create results classes & obj
	DONE: throne_push and nothing_happens => BufferOnly
	DONE: throne_pull_result => new class => AddObjToRoomResult
DONE: broach_dispenser_mach
	DONE: create broach_dispenser obj of class InvisMach
	DONE: trig_switch = throne
	DONE: cond_switch_lst = [throne]
	DONE: machine_type = post_action_switch_trig
	DONE: machine_state = False (# broach_dispensed)
	DONE: cmd_triggers_lst = ['pushed', 'pulled']
	DONE: cond_lst: broach_already_dispensed, throne_push_pre_dispense, throne_pull_pre_dispense
	DONE: result_lst: throne_push, nothing_happens, dispense_broach
DONE: create post_action() module and function [very similar to pre_action()]
	DONE: for case = 'switch', pass list of trigger values => ['pushed', 'pulled']
DONE: Lots of testing!!!
	DONE: troubleshoot post_action 
	DONE: troubleshoot class_deff => throne works now but Room Events in Entrance don't??
	DONE: sorted out Entrance Room Events
	DONE: Clean up prints & comments
	DONE: clean up InvisSwitchMach 
DONE: create broach obj of class Clothes and clothing type 'pin'
	DONE: create borach object (class = Clothes)
	DONE: add broach description and wear and remove description
	DONE: Allow broach to be worn but hint in wear_descript and remove_descript that it's only of sentimental value
	DONE: troubleshoot broach being examined (currently throwing error) [try royal_crown instead to localize issue]
	DONE: update score dicts to grant 5 pts on broach in hand
	
	
##########################
### VERSION 3.56 START ###
##########################

Version 3.56 Goals
- Clean up machine coding

DONE: move GameState class definition to a separate module
	DONE: move GameState class def to gs_class_def
	DONE: change mk_def_pkl import to gs_class_def
	DONE: initial testing
	DONE: delete GameState class def from class_def
	DONE: more testing
DONE: move Conditions class definitions to a separate module (cond_class_def.py)
	DONE: move Condition class def to cond_class_deff
	DONE: make PassThruCond the base Condition
		NOTE: Now, all other Condition classes inherit from PassThruCond except InHandAndStateCond which is a child of StateCond 
	DONE: initial testing
	DONE: delete comments
	DONE: delete Condition classes from class_def
	DONE: more testing
DONE: move Results class definitions to a separate module
	DONE: create results_class_def.py
	DONE: copy Results class definitions to results_class_def
	DONE: create initial PassThruResult class
	DONE: update BufferOnlyResult classes to inherit from PassThruResult
	DONE: update remaing Result classes to inherit from BufferOnlyResult (was already the case)
	DONE: update mk_def_pkl to import from results_class_def
	DONE: run mk_def_pkl
	DONE: initial testing
	DONE: delete comments
	DONE: delete Result classes from class_def
	DONE: final testing
DONE: move InvisMach class def & methods to a separate module
	DONE: create mach_class_def.py
	DONE: copy Results class definitions to mach_class_def
	DONE: create initial InvisMach class
	DONE: update mk_def_pkl to import from mach_class_def
	DONE: run mk_def_pkl
	DONE: initial testing
	DONE: delete comments
	DONE: delete Result classes from class_def
	DONE: final testing
DONE: update mach_class_def to use MixIn concept
	DONE: Redo InvisMach => MachineMixin with no name
	DONE: Create InvisMach as child of Invisible and MachineMixIn
	DONE: test!
	DONE: clean up comments
DONE: updated class_def.py
	DONE: rename class_def.py => noun_class_def.py
	DONE: update imports
	DONE: test
TBD: code clean-up and consistency
	DONE: make InHandAndStateCond a child of StateCond
	DONE: do we really need to pass machine_state to result_exe() method?? 
		=> Yes; need to update sometimes so need to pass in for no change
		=> Alternatively, could just pass new state or None for no change... but really simpler to just pass machine_state in
	DONE: mix-in inheritance for ViewOnly or Item Machines
	DONE: can ViewOnlyMach be in mach_class_def ?? => YES
	DONE: decision on which is better... shallower or deeper class inheritance? => SHALLOW
	DONE: dedup obj_lst_to_str() across class modules
		DONE: reviewed all class modules => only noun_class_def and gs_class_def use obj_lst_to_str()
		DONE: created shared_class_func.py
		DONE: copied obj_lst_to_str() to shared_class_func.py
		DONE: import shared func and comment out local func
		DONE: run mk_def_pkl
		DONE: test
		DONE: clean up comments
		DONE: re-test


##########################
### VERSION 3.58 START ###
##########################
Version 3.58 Goals
- Create class, methods, and obj antechamber control_panel machine

DONE: create Lever class and objects
	IDEA: keep all the smarts in machine; lever only knows if it's up or down
	DONE: create LeverSwitch class
	DONE: create left_lever, middle_lever, right_lever and add to antechamber room_obj_lst
	DONE: test
DONE: create red_button of class ButtonSwitch
	DONE: create obj
	DONE: add obj to room and pickle
	DONE: test
DONE: create Condition classes & objects
	DONE: create LeverArrayCond class based on SwtichStateCond
		DONE: attributes are same as parent but cond_check method is over-ridden
		DONE: cond_check converts switch state to current_val and returns current_val == target_val
		DONE: create correct_lever_array_cond obj based on LeverArrayCond class
		DONE: switch_state_val_lst == [4,2,1]
		DONE: machine_state == target_val
	DONE: create wrong_lever_array_cond obj based on PassThruCond
DONE: create Results classes & objects
	DONE: create DoorToggleResult class
	DONE: run mk_def_pkl
	DONE: create toggle_portcullis_result obj based on ToggleDoorResult class
	DONE: create portcullis_doesnt_open_result obj based on BufferOnlyResult class
	DONE: run mk_def_pkl
DONE: create ViewOnlyMach class
DONE: create machine obj
	DONE: create control_panel obj
	DONE: update machine_state = target_val in start_me_up
	DONE: perhaps move levers and button to features once control_panel exists?
		IDEA: perhaps part of control_panel purpose is to isolate description of switch elements from main room inventory?
	DONE: test
	DONE: clean up comments
DONE: create a module just for switch class def
	DONE: create switch_class_def with import of ViewOnly
	DONE: copy Switch class definitions to switch_class_def (ViewOnly remains parent)
	DONE: update mk_def_pkl to import from switch_class_def
	DONE: run mk_def_pkl
	DONE: initial testing
	N/A: delete comments
	DONE: delete Switch classes from noun_class_def
	DONE: final testing
DONE: can we harmonize or use MixIn for switches? ( https://python-textbok.readthedocs.io/en/1.0/Object_Oriented_Programming.html )
	DONE: create SwitchMixIn class
	DONE: ButtonSwitch class
		DONE: create new ButtonSwitch based on ViewOnly & SwitchMixIn
		DONE: comment out old ButtonSwitch
		DONE: run mk_def_pkl
		DONE: Test
	DONE: LeverSwitch
		DONE: create new ButtonSwitch based on ViewOnly & SwitchMixIn
		DONE: comment out old ButtonSwitch
		DONE: run mk_def_pkl
		DONE: Test
	DONE: delete comments
	
	
##########################
### VERSION 3.59 START ###
##########################

Version 3.59 Goals
- Create / update machine documentation
- fine tune machine code

DONE: documentation:
	DONE: write up thinking and decisions on machines and switches
	DONE: Machine Code Updates
		DONE: move machine_state to first Machine attribute
			DONE: comment old code
			DONE: write new code
			DONE: full test
			DONE: delete comments
		DONE: standardize 'result' vs. 'results'
			DONE: results_exe => resulte_exe
			DONE: full test
			DONE: delete comments
		DONE: change results_class_def => result_class_deff
			DONE: change file name
			DONE: change import from mk_def_pkl()
			DONE: run mk_def_pkl()
			DONE: full test
		DONE: trigger() => run_mach()
			DONE: rename trigger() in mach_class_def
			DONE: rename trigger() call in pre_action() and post_action()
			DONE: full test
			DONE: delete comments
		DONE: result_num => result_index
			DONE: in the mach_class_def module, run_mach() function, change result_num => result_index
			DONE: run mk_def_pkl()
			DONE: test
			DONE: clean up comments
		DONE: clean up post_action trig_switch_state_lst assignment
			DONE: multi-value code retained in case of future changes
		DONE: machine_state => mach_state
			DONE: in the mach_class_def module, update machine_state => mach_state
			DONE: run mk_def_pkl()
			DONE: full test
			DONE: clean up comments
			DONE: in cond_class_def and result_class_def modules, update machine_state => mach_state
			DONE: test
		DONE: full test (portcullis button failing)
			DONE: backed out trigger_type value changes... button still misbehaving... need to examine "mach_state" change
			DONE: Review mach_state => updated in cond_class_def and result_class_def but still doesn't work right
			INFO: now door only works on zero value lever array... ???
			INFO: throne switch appears to work correctly
			DONE: deep dive on LeverArrayCond
				DONE: Don't forget to run mk_def_pkl after updates!!!
			NOTE: solved it! had forgotten to updat machine_state => mach_state assignment in start_up()
			DONE: full test
		DONE: using trigger_type is *very* efficient... maybe just change attribute value to 'pre_act_auto_switch_reset' ???
			DONE: change value in pre_action()
			DONE: change value in mk_def_pkl()
			DONE: run mk_def_pkl()
			DONE: full test
		CANCEL: re-name Switch trigger_type to switch_reset
			CANCEL: update mach_obj_lst() in gs_class_def() to include switch_reset attribute
			CANCEL: update pre_action module
				CANCEL: add switch_reset check
			CANCEL: updates SwitchMixIn in switch_class_def() to replace trigger_type with switch_reset
				CANCEL: attribute
				CANCEL: declaration
				CANCEL: @properties
			CANCEL: full test
			CANCEL: delete comments
		DONE: Machine naming convention... no '_mach' after control_panel ??
			DONE: documented in Machine Decisions
		DONE: Run switch re-sets w/ regular pass-thru machines (?)
			CANCEL: add pre_act_auto code to pre-action
			CANCEL: create SwitchResetResult
			CANCEL: create switch_neutral_reset_result obj
			IDEA: thinking through this further... I don't want to have to create a separate reset trigger for every "standard" switch
			IDEA: standard switches should be pretty painless... I can make a complex switch later if I need special behaviors
			IDEA: as a compromise, how about if I add a def_switch_state attribute to SwitchMixIn (standard value == 'neutral')
			IDEA: then, in the pre_action() test, if obj.switch_state != obj.def_swicth_state: obj.switch_state = obj.def_switch_state
			IDEA: this allows for non-'neutral' default switch states
			DONE: add def_switch_state attribute to SwitchMixIn and ViewOnlySwitch
			DONE: update switch obj values in mk_def_pkl
			DONE: run mk_def_pkl
			DONE: update reset code in pre_action 
			DONE: Test
			DONE: clean up comments
	DONE: Finalize documentation
		DONE: Update Machine Notes based on Code Updates
		DONE: Separate document for Machine Notes
		DONE: Sort out rough Machine ideas


##########################
### VERSION 3.60 START ###
##########################

Version 3.60 Goals
- Create class, methods, obj, and machines for goblin creature

DONE: Ideate
	DONE: share updates with Franco
	DONE: consolidate / formalize rough Creature ideas => beginning pseudo-code
DONE: create base class
	DONE: create creature_class_def.py
	DONE: define base Creature class (no methods yet)
	DONE: add Creature to mk_def_pkl() imports
	DONE: run mk_def_pkl()
	DONE: troubleshoot
DONE: create base object
	DONE: instantiate goblin in mk_def_pkl() 
	DONE: add goblin to antechamber room
	DONE: add goblin obj to master_obj_lst in mk_def_pkl
	DONE: run mk_def_pkl()
	DONE: add base goblin description to static_gbl
	DONE: test
DONE: create show() method
	DONE: evaluate updates needed in interpreter to support "show x to y"
	DONE: create show method
	DONE: add show attributes to goblin
	DONE: add show_response text to static_gbl
	DONE: add 'show' to verb_lst in interp()
	DONE: interp() updates
	DONE: cmd_exe() updates
	DONE: run mk_def_pkl()
	DONE: test show method
	DONE: update help function for prepositions
DONE: add a default option to show() method
	DONE: add 'def_show' entry to the show_item_dict attribute
	DONE: update the show() method
	DONE: update static_gbl
	DONE: run mk_def_pkl()
	DONE: test
DONE: redo default option code to avoid duplication (prep for give method)
	DONE: update the show() method
	DONE: run mk_def_pkl()
	DONE: test
DONE: add a biscuit-specific show() response (in support of future give() behavior) to avoid a quest-breaking scenario.
DONE: implement give() method
	DONE: create give() method
		DONE: confirm that item is in hand
		DONE: implement Creature def_give behavior
		DONE: if accept_item: remove item from hand and add to creature_item_lst
		DONE: buffer descript_dict[response_key]
		DONE: if exchange_item != None: removie item from creature_item_lst and add to hand
		DONE: if new_descript_key != None: update self.descript_key
		DONE: method default response = "the <creature> is not interested in the <item>"
	DONE: add 'give' to verb_lst in interp()
	DONE: add give() attributes (including creature_item_lst) to goblin
	DONE: add give_response text to static_gbl
	DONE: update interp() => elif word1 in ['show', 'give']
	DONE: update cmd_exe() => elif word1 in ['show', 'give']
	DONE: run mk_def_pkl()
	DONE: test give() method (uses method default for un-named obj; errors out on biscuits and sword)
		DONE: method default for un-named obj solved
		DONE: solved it!
	DONE: update help function for prepositions
	DONE: full final test
DONE: create attack() method
	IDEA: attack_creature_dict = {burt_weapon : result_code, response_key}
	IDEA: result_code options = 'creature_flee', 'creature_death', 'burt_death', None
	DONE: remove attack_src_dict attribute
	DONE: create attack() method
		DONE: burt_weapon = hand_item ('Fist' if hand is empty)
		DONE: implement 'def_attack' behavior
		DONE: buffer descript_dict[response_key]
		DONE: if result_code == 'creature_flee': remove creature from room_obj_lst
		DONE: if result_code == 'creature_death': 
			DONE: creature_items_lst => room_obj_lst
			DONE: remove creature from room_obj_lst
			DONE: add dead_creature obj to room_obj_lst
			DONE: add dead_creature_obj to Creature class attributes
			DONE: update goblin obj
			DONE: create dead_goblin ViewOnly obj
		DONE: if result_code == 'burt_death': active_gs.set_game_ending('death')
		DONE: method default response = "At the last minute the <creature> dodges your vicious attack with the <burt_weapon>"
	DONE: add 'attack' to verb_lst in interp()
	DONE: add attack() attributes (including creature_item_lst) to goblin
	DONE: add attack_response text to static_gbl
	DONE: add descript_dict entry for dead_goblin
	DONE: run mk_def_pkl()
	DONE: test attack() method
		DONE: troubleshoot double show and give
		DONE: troubleshoot attack command
			DONE: able to ref shiny_sword
			DONE: attack works but list add of goblin_items_lst is now an issue
			DONE: fix extend function
			DONE: fix dead_goblin 'goblin' short name
			DONE: fix 'def_attack'
		DONE: add buffer of weapon used in attack() method
		DONE: fix 'fist' gramar (i.e. "the <weapon>" vs. "your fist")
	DONE: create help function for 'attack'
	DONE: reduce duplication in cmd_exe() put, give, take, 2word cases
	DONE: de-dup 'prep' code
	DONE: examine 'show' case return in interp() - what to do about 'give'? change case name? => 'prep' case
	DONE: comment clean-up
DONE: create goblin machines
	DONE: Plan out attack_burt method & attack_burt_dict
		IDEA: Instead of a separate method for burt_attacks, just have a separate dict??
			IDEA: but how could I pass in who the attacker was?? (without needing a new interp() case)
		IDEA: Ultimately, a separat attack_burt() method is simplest... but this is another arguement for 'burt' as an obj
			IDEA: will still need a spearate attack_burt_dict
			IDEA: replace "Fearlessly you charge.." text with "You attempt to parry the creature's attack with "
			IDEA: 'pary' is really just text and and result_key == None
	DONE: implement attack_burt() method and attack_burt_dict
		DONE: create attack_burt() method
		DONE: attack attack_burt_dict to Creature class
		DONE: update guard_goblin obj to include attack_burt_dict
		DONE: all entries for attack_burt_dict
		DONE: add response_key text for goblin attack_burt_dict
		DONE: solve how to add 'attack_burt' to verb_list in interp() => create a secret_verb_list ?
			DONE: verbs_lst => known_verbs_lst
			DONE: create secret_verbs_lst = ['attack_burt']
			DONE: full_verbs_lst = known_verbs_lst + secret_verbs_lst
			DONE: update checks to full_verbs_lst
		DONE: manually test attack_burt() => 'attack_burt goblin'
	DONE: plan pre_act_mach
		IDEA: room will be a condition component
		IDEA: can pass creature into result_exe()
			IDEA: text will be situation-specific (e.g. "The goblin does not take kindly to your presence in the north side of the Antechamber.")
			IDEA: rest of the result is just calling self.creature.attack_burt()
			IDEA: creatures are weapon-locked (always assumed to use the same weapon)
	DONE: implement goblin pre_act_mach
		DONE: create machine obj
		DONE: create cond class
		DONE: add cond class to mk_def_pkl() imports
		DONE: create cond objs
		DONE: test & troubleshoot
			IDEA: room obj are not yet defined - maybe just put this one cond after rooms? and then this one creature after cond
			IDEA: except this doesn't work - because then goblin has to be after room... but the goblin is IN a room - argh!!
			IDEA: consider room_name conversion ???
			DONE: attribute = room_name rather than room_obj
		DONE: create result class
		DONE: add result class to mk_def_pkl() imports
		DONE: create result objs
		DONE: create buffer text for result
		DONE: test!
		DONE: create base trigger cmd attributes
		DONE: test & tune
			DONE: test & troubleshoot!
				DONE: added machine to goblin
				DONE: extended mach scope search to creatures but not sure this is working (scope is working now)
				DONE: test print() statements in RoomCond but they never run
				IDEA: problem appears to be in trigger - this is the first time triggering on 2word case - it has not worked before
				DONE: sort out trigger for condition
			DONE: expand on trigger options
			DONE: re-test
			DONE: change goblin => guard_goblin
				DONE: update instantiation obj name
				DONE: update obj name in antechamber
				DONE: update obj name in pkl save
				DONE: search for any other solo usage of 'goblin'
				DONE: re-test
		DONE: clean up comments & troubleshooting prints!
DONE: create help function for creatures (include fact that creatures can attack)
DONE: full final test
DONE: update creature doc
	DONE: Creature Method Philosopy updated
	DONE: created dump_doc.md and moved the legacy creature ideas there
	DONE: organized the active creature doc a bit better
	DONE: move creature doc to a dedicated file



