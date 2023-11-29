Done List - Dark Castle v3
Nov 5, 2022


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
	DONE: copy descriptions to static_init() static_dict
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
DONE: Pull eat description from static_dict
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
		DONE: effect_desc to static_dict
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
		DONE: add entrance_east and entrance_west to static_dict
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
		DONE: buffer static_dict[response_key]
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
		DONE: buffer static_dict[response_key]
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
	DONE: add static_dict entry for dead_goblin
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


##########################
### VERSION 3.61 START ###
##########################

Version 3.61 Goals
- IDEA: Theme of 3.61 is some supporting coding that will prep for the hdegehog in 3.62
- DONE: warning class
	- IDEA: what are we trying to do here and how will we do it?
		- IDEA: goal of warnings is to produce a streamlined, simpler machine type just for warnings
		- IDEA: counter can be 1, 2, or infinite (warning_count = None => infinite)
		- IDEA: if not infinite, then after last warning gives an "I told you so"
		- IDEA: during infinite or count return cmd_override == True; else cmd_override == False
	- DONE: create warning class
		- DONE: in mach_class.py create WarnClass (inherits attribute sub-set from InvisClass)
		- DONE: create WarnClass attributes
			- DONE: Total Attributes include: name, trigger_type, trig_vals_lst, warn_max, warn_count, warn_key_1, warn_key_2
			- DONE: name, trigger_type, trig_vals_lst from InvisClass
			- DONE: warn_max, warn_count, warn_key_1, warn_key_2 = local attributes
			- DONE: create setters for local (and getter for warn_count)
		- DONE: override run_mach with warn-specific code (buffer static_dict[warn_key], return override value)
	- N/A: update pre_action() code to handle warning case (maybe warnings before machs???)
	- DONE: instantiate warn obj: eterance_south_warn
		- DONE: add WarnClass to mk_def_pkl imports
		- DONE: in mk_def_pkl create warning object for going south from entrance
		- DONE: in static_gbl add text for entrance_south_warn
		- DONE: comment out entrance_south_mach
		- DONE: remove entrance_south_mach from entrance room
		- DONE: add warn obj to Entrance invisible
	- DONE: Initial Testing
		- DONE: class based errors not resolved when trying to run mk_def_pkl()
	- DONE: New warning class ideas
		- IDEA: after cleaning up some typos it appears that "selective inheritance" just isn't a thing. What now?
		- IDEA: this makes sense... in all other cases I inherit from simple parents to more complex children
		- IDEA: WarnClass is simpler... so it should be the parent
		- IDEA: Actually - how about a TrigDetectMixIn that is inherited by both WarnClass and MachineMixIn and only has trig_check method?
		- IDEA: A MixIn of a MixIn seems over-complicated... 
		- IDEA: perhaps right now I'll just make an independent class with duplicate trig_check code base
		- IDEA: as a future activity, I can look to de-dup in a more elegant fashion
	- DONE: Class re-do
		- DONE: rename class to Warning
		- DONE: update class name in mk_def_pkl() import and obj instantiation
		- DONE: implement with code dup of MachineMixIn
		- DONE: run mk_def_pkl()
	- DONE: testing
	- DONE: clean-up
		- DONE: comment out entrance_south_mach result and conditions obj
- DONE: more scalable approach to warnings:
	- DONE: warning improvement ideation
		- IDEA: obj_name+str(count); if exist static_dict[key]: active_gs.io.buffer(static_dict[key]); else: buffer default
		- IDEA: or maybe the pythonic approach here is "try" ?
		- IDEA: initial Warning attributes = name, trigger_type, trig_vals_lst, warn_max, warn_count, warn_key_1, warn_key_2
		- IDEA: should be able to eliminate warn_key_1, warn_key_2
		- IDEA: if warn_max = 0: key = name_1 ; else try key = name + "_" + warn_count except name_1 (i.e. name_1 is the default)
	- DONE: code warning improvements
		- DONE: add increment for warn_count (how did I forget this??)
		- DONE: eliminate warn_key_1 and warn_key_2 attributes
		- DONE: update obj instantiation
		- DONE: update static_dict key
		- DONE: test infinite case
		- DONE: test limited case
		- DONE: create static warn_default = "I'm not sure that's a good idea Burt..."
		- DONE: add try and except coding
		- DONE: test infinite case
		- DONE: test limited case
		- DONE: clean up test prints
		- DONE: clean up comments
- DONE: timers
	- DONE: timer design goals
		- IDEA: can be triggered by function call timer_obj.start()
		- IDEA: run for a set amount of time timer_max
		- IDEA: increment timer_count each time a turn successfully passes (watch out for errors that don't count!)
		- IDEA: if silent_timer == False: active_gs.io.buffer(timer_descript_key) where timer_descript_key = name + str(timer_count)
		- IDEA: timer attributes: name, active (T or F), timer_count, timer_max, message_type ('silent', 'variable', 'constant'), trigger_type = 'auto_pre_act'
		- IDEA: like buttons, timers should be 'dumb' - the smarts live in a machine
	- DONE: create Timer class
		- DONE: create header and attribute setters & getters
		- DONE: import Timer class into mk_def_pkl()
	- DONE: create timer methods (start, run_mach, etc)
		- DONE: create run_mach()
		- DONE: create start()
		- DONE: create reset()
	- DONE: update pre_act() to check for active timers
	- DONE: instantiate timer obj
		- DONE: create test_timer
		- DONE: create test_timer_# dict entries
	- DONE: create test rig
		- TBD: create ViewOnlyMach obj big_bomb
			- DONE: create blue_button, add to noun list, and place in entrance
			- DONE: create big_bomb ViewOnlyMach and place in entrance
			- DONE: trigger = pushing blue button
			- DONE: condition = pass_thru
			- DONE: result = start and check timer
	- DONE: base timer functionality test
		- CANCEL: add test_timer to invisible attribute of Antechamber room
		- CANCEL: call test_timer.start() from DoorToggleResult class
		- DONE: can push blue_button and get result
		- ISSUE: pre_action() only runs machine code that is in mach_obj_lst
		- ISSUE: but test_timer is an attribute of a Result, which is an attribute of a ViewOnlyMach obj...
		- ISSUE: so mach_obj_lst never knows about test_timer
		- IDEA: where should I place test_timer? Since ViewOnly obj can't move maybe place in Room? Yes, this works!!
		- DONE: achieve base timer functionality
	- DONE: detailed timer testing
		- DONE: test timer on no-turn-error
			- FINDING: this fails... which makes sense... pre_action() is called before cmd_exe()... and cmd_exe() is where moves are decremented
			- IDEA: I can check for case == error and case == 1word && word = 'quit' in pre_act() and, if so, return override = False
			- IDEA: but there's no graceful way to check for errors and 2word or prep... so I think I need to cancel the move_dec() on those
			- DONE: solved pre_action() and post_action() skip and also need for move_dec in app_main()
			- DONE: comments cleaned up
		- CANCEL: test timer with pass_thru condition; then test with timer_aware condition
		- DONE: test all three message modes
		- DONE: clean up testing print statements
		- DONE: added timer_done attribute
- DONE: alert_scope
	- DONE: alert_scope design goals
		- IDEA:	most machines only react to Burt's actions - and their reaction is immediate - so Burt will always see the results
		- IDEA: but timers (and, perhaps in the future, 'auto's) mean that visible alerts could be generated in a room that Burt is no longer in
		- IDEA: in this case, Burt should not actually be notified
		- IDEA: e.g. the Hedgehog will eat the biscuits for 3 turns but Burt shouldn't hear about it if he's left the room
		- IDEA: So, to start with at least we will set the "alert scope" to the room the timer / auto event is happening in
		- IDEA: if Burt is in a room he sees and hears the events in the room. If he's outside the room he sees and hears nothing.
		- IDEA: So we need an active_gs method that can determine if a given timer / auto is in the same room as Burt
		- IDEA: since we can get mach scope for the room Burt is in, it shouldn't be too hard to check if a given timer / auto is in the mach_lst
		- IDEA: this addresses alerts but maybe not results... 
		- IDEA: for example if Burt lights a fuse and walks away - Burt may not be harmed but the room should be changed...
		- IDEA: but that can be dealt with in the future...
- DONE: implement alert_scope for test timer
	- DONE: in active_gs, create method auto_in_alert_scope(self): which checks to see if self is in mach_lst and returns True or False
	- PROB: test_timer stops ticking when Burt leaves the room...
		- IDEA: universal scope to solve timer not running when Burt out of room
		- IDEA: today, the timer only ticks if it is in mach_lst... which is based on machines, warnings, & auto in the same room as Burt
		- IDEA: so the moment Burt leaves the room that big_bomb is in, the timer stops ticking...
		- IDEA: to solve this I need a universal_mach_lst that is available in all places
		- IDEA: I add test_timer to universal_mach_lst, and in turn universal_mach_lst gets added to mach_lst
		- IDEA: under this scenario, Burt can only trigger big_bomb with the blue_button in the entrance... but the timer ticks even if he leaves
	- SOLN: universal_mach_lst
		- DONE: add universal_mach_lst attribute to GameState class
		- DONE: create getter
		- DONE: update mach_lst method to extend mach_lst with contents of universal_mach_lst
		- DONE: instantiate universal_mach_lst
		- DONE: remove test_timer from entrance room and add it to universal_mach_lst
		- DONE: run mk_def_pkl()
		- DONE: test timer behavior when Burt leaves room
			- PROB: Test runs but still see 'ticks' in Main Hall because auto_in_alert_scope uses mach_obj_lst !
			- DONE: created room_mach_lst to be checked bay auto
			- PROB: So now test does not show 'tick' because test_timer is NOT in the room... it is in mach_obj list...
			- IDEA: I need to think through this more... what do I want to check for in the room?
			- IDEA: maybe I need to create an attribute alert_anchor that is the obj auto_in_alert_scope needs to check for?
			- DONE: created alert_anchor and got it working!
- DONE: should timer be pre or post?
	- IDEA: it makes sense that autos go before Burt...
	- IDEA: but it feels wrong that the user enters text and then the auto happens and then the user command happens...
	- IDEA: this feels non-causal... and the user doesn't get to know what the auto did as an input to their command choice
	- IDEA: instead... I think I need a new auto_action() module that runs *before* user input
	- IDEA: this allows the player to see the auto action before choosing their action... and their action response feels more causal
	- IDEA: however app_web() calls app_main() *after* getting input... so I can't actually 'auto move' before getting input...
	- IDEA: so how about going *after* post_action()?
	- DONE: create auto_action() => works!!
- DONE: clean up prints & comments
	- DONE: comment out prints
	- DONE: delete comments
- DONE: write up notes for warnings, timers, and auto_scope
	- DONE: warnings
	- DONE: timers
	- DONE: final doc review
	- DONE: move to machines doc file


##########################
### VERSION 3.62 START ###
##########################
Version 3.62 Goals
- Instantiatie base royal_hedgehog creature (including key trading and attack warning)

- DONE: instantiate royal_hedgehog
	- DONE: base instantiation based on guard_goblin
		- DONE: royal_hedgehog posesses silve_key
		- DONE: add hedgehog to noun pkl
		- DONE: add hedgehog to Main Hall
		- DONE: run mk_def_pkl()
		- DONE: base description for hungry_hedgehog
	- DONE: special show for stale_biscuits, shiny_sword
		- DONE: stale_biscuits
		- DONE: shiny_sword
	- DONE: special give:
		- DONE: biscuits: accept biscuits, description key, andupdate creature descirption to *eating*
		- DONE: shiny_sword: accept sword, give key, description key, and update creature description
		- DONE: removed silver_key from Throne Room
	- DONE: attack response
		- DONE: default = no response / text adomonition
		- DONE: shiny sword = flee
	- DONE: point reduction (-20) for attacking hedgehog?
		- DONE: added 'hedgehog_attack' to score_val_dict in score()
		- DONE: added 'hedgehog_attack' to active_gs dict in mk_def_pkl()
		- DONE: created "custom scoring" section in score()
		- DONE: only active_gs is passed into score() so royal_hedgehog and main_hall are undefined
			- DONE: create room_lst in active_gs
			- DONE: create an active_gs method obj_exist() that can evaluate whether an obj is in the game (in any room's room_obj_lst)
			- DONE: call active_gs.obj_exist(royal_hedgehog) from the "custom scoring" section of score()
			- ISSUE: I have a room search... but royal_hedgehog is *still* undefined... so I guess I need a room search based on obj name
				- IDEA: is this getting silly? Should I just pass master_obj_lst to score()?
				- IDEA: no... there's a value to being able to search rooms by name - and it's ultimately shorter than searching all obj
				- DONE: create obj_name_exist() methd in active_gs()
				- DONE: update score()
	- DONE: sword attack warning
		- DONE: sort out warning scheme
			- IDEA: if I want attack_hedgehog_warning to be a simple warning then I can't test for what Burt is holding...
			- IDEA: so, let's have the hedgehog fee on *any* attack (not just the shiny_sword)
			- IDEA: (which makes sense given that the royal_hedgehog is not a dangerous fighter who can only be defeated by a mighty weapon)
			- IDEA: and let's make the current text for a non-shiny_sword attack apply the first warning of 2
		- DONE: update current hedgehog attack based on warning decisions
		- DONE: create attack_hedgehog_warning - which gives 2 warnings
		- DONE: create warning text for warnings 1 & 2
		- DONE: add attack_hedgehog_warning to royal_hedgehog.mach_obj_lst
		- DONE: test!


##########################
### VERSION 3.64 START ###
##########################

Version 3.64 Goals
- Create complex machine for hedgehog creature (including bisuit eating and timer; note that eating must override show & give)

- DONE: map out desired conditions & results
	- Case 1: hedgehog_eats_timer is active, Burt tries to take sword:
		- Result = Burt gets sword (standard case)
	- Case 2: Burt gives (or drops) biscuits:
		- Result = hedgehog_eats_timer started
	- Case 3: hedgehog_eats_timer not active, Burt tries to take sword:
		- Result = hedgehog guards sword (Warning ?)
	- Case 4: hedgehog_eats_timer is active, Burt tries to give or show to hedgehog:
		- Result = hedgehog is eating; response is inhibited
	- Case 5: special machine to update hedgehog description at end of timer
		- description depends on whether the hedgehog has kept the sword???
- DONE: create hedgehog_eats_timer (4 turns long, presents text if in scope)
	- DONE: create hedgehog_eats_timer in mk_def_pkl(); set alert_anchor to royal_hedgehog
	- DONE: add hedgehog_eats_timer to mk_def_timer() universal_mach_lst
	- DONE: add timer text descriptions to static_gbl()
	- DONE: run mk_def_pkl()
- DONE: create hedgehog_eats_mach (starts timer if give or drop)
	- DONE: decide whether I will support 'drop biscuits' (leaning towards 'no')
		- DECISION: 'drop biscuits' will NOT trigger hedgehog_eats_mach
	- DONE: create Condition for hedgehog_eats_mach 
		- DONE: create class CreatureItemCond (parent = PassThruCond)
		- DONE: test for hedgehog has biscuits in cond_check() 
		- DONE: instantiate hedgehog_has_biscuit_cond in mk_def_pkl()
		- DONE: add CreatureItemCond to mk_def_pkl() imports and use creature object re-assignment work-around
		- DONE: run mk_def_pkl()
	- DONE: create Results for hedgehog_eats_mach (start timer; remove biscuits from hedgehog)
		- DONE: create class TimerAndCreatureItemResult (parent = StartTimerResult)
		- DONE: start time and remove creature_item
		- DONE: fix descript & buffer for StartTimerResult()
			- DONE: Check existing Results classes
			- FINDINGS: no Result obj use PassThru, all Result classes inherit from BufferOnlyResult, all Result obj use name as descript_key
			- DONE: eliminate PassThruResult / update BufferOnlyResult to inherit from 'object' or Invisible
			- DONE: update BufferOnlyResult to use 'try... except...' buffer approach used in Timer & Warning
			- DONE: clean up commented code (lots of it!)
		- DONE: instantiate start_hedgehog_timer_results in mk_def_pkl()
		- DONE: add TimerAndCreatureItemResult to mk_def_pkl() imports and use creature object re-assignment work-around
		- DONE: run mk_def_pkl()
	- DONE: create machine for hedgehog_eats_mach (will be a post_action() mach; class = InvisMach)
		- DONE: add hedgehog_eats_mach to hedgehog
		- DONE: test!
- DONE: create hedgehog_guard_mach (if timer not active, hedgehog guards sword)
	- DONE: Create Condition
		- DONE: Create Condition class for hedgehog_eats_timer.active (TimerNotActiveCond)
		- DONE: instantiate hedgehog_guard_cond
		- DONE: import TimerActiveCond, run mk_def_pkl()
	- DONE: create Result
		- DONE: instantiate hedgehog_guard_result (class = BufferOnlyResult)
	- DONE: create Mach
		- DONE: instantiate hedgehog_guard_mach (class = InvisMach)
		- DONE: type = pre_act_cmd
		- DONE: add hedgehog_guard_mach to royal_hedgehog
	- DONE: testing
		- DONE: std condition testing
		- DONE: address case of "get sword" producing 'guard' Condition when Burt has already gotten the sword
			- FINDING: this happens if Burt has the sword in the main_hall after the timer has expired
			- DONE: update Condition to solve this
			- DONE: remove TimerNotActiveCond
- DONE: create hedgehog_done_eating_mach (update hedgehog description after eating based on presence of shiny_sword)
	- DONE: Timer as Trigger
		- IDEA: need to enable Timer ending to trigger a Machine
		- IDEA: in pre_action() create timer case
		- IDEA: trig_check() method (which is in mach_class_def() module), check for 'timer' case
		- IDEA: use mach_state in Condition to only implement timer_done based Result once
		- DONE: update pre_action() to include timer case for Machine type == 'pre_act_timer'
		- DONE: in mach_class_def() update trig_check() method to include case == 'timer'
	- DONE: Conditions
		- CANCEL: instantiate hedgehog_desc_update_cond of class StateCond
		- IDEA: **** HANG ON - MAYBE 2 DIFFERENT DESCRIPTIONS SHOULD BE 2 DIFFERENT RESULTS??? ****
		- DONE: create StateItemInRoomCond class
		- DONE: instantiate hedgehog_keeps_sword_cond
		- DONE: instantiate hedgehog_loses_sword_cond
		- DONE: run mk_def_pkl()
	- DONE: Results
		- DONE: create ChgCreatureDescResult class
		- DONE: Update hedgehod descript based on shiny_sword condition
		- DONE: Toggle Machine state to True (so that description is only changed once)
		- DONE: instantiate fed_hedgehog_loses_sword_result and fed_hedgehog_keeps_sword_result
		- DONE: run mk_def_pkl()
		- DONE: create description entries for all (4) keys
		- DONE: maybe update desc name to indicate Result State change?
	- DONE: Machine
		- DONE: create hedgehog_done_eating_mach of class InvisMach
		- DONE: assigne hedgehog_done_eating_mach to royal_hedgehog
		- DONE: testing!
- DONE: create hedgehog_distracted_mach (if timer active, inhibits show & give)
	- IDEA: to enable match on 'show' or 'give' <any>, creature wildcard ('*') functionality within trig_check() method
	- DONE: Update trig_check() method in Machine class to recognize '*' as a wildcard
		- DONE: MachineMixIn trig_check() updated (NOTE: Warning trig_check() not yet updated!!)
	- DONE: Conditions
		- DONE: create TimerActiveCond class (include condition match)
		- DONE: import TimerActiveCond to mk_def_pkl()
		- DONE: instantiate hedgehog_distracted_cond in mk_def_pkl()
		- DONE: run mk_def_pkl()
	- DONE: Results
		- DONE: instantiate hedgehog_distracted_result of class BufferOnlyResult
		- DONE: create description entry for 'hedgehog_distracted_result'
	- DONE: Machine
		- DONE: instantiate hedgehog_distracted_mach
		- DONE: add hedgehog_distracted_mach to royal_hedgehog
		- DONE: run mk_def_pkl()
		- DONE: testing! 
			- DONE: appears that list_of_lists loop is not working as expected => use enumerate() for indexes!!
			- DONE: solved 'only one letter' issue - had double loop operating on single list
			- DONE: how and why is wcard_lst caching the intermediate '*' values?!?
			- DONE: need to apply '*' updates to all list members
			- DONE: comment out test print statements
			- DONE: comments cleaned up


##########################
### VERSION 3.66 START ###
##########################

Version 3.66 Goals
- create ItemMach class
- create Conditions, Results, and Machine for kinging_scroll (class == ItemMach)

- DONE: create class
	- DONE: create ItemMach class (identical attributes to ViewOnlyMach)
	- DONE: in mach_class_def(), import Item class from noun_class_def()
- DONE: big picture:
	- trigger == read letters
	- conditions == kinging_scroll in hand and:
		- if room != throne_room => wrong_room_error
		- elif hedgehog not exist => no_hedgehog_error
		- elif royal_crown not worn => crown_not_worn_error
		- else win_game, score += 15, end_game
- DONE: conditions
	- DONE: create Condition class InHandAndRoomCond and import class in mk_def_pkl()
	- DONE: create Condition class InHandAndExistInWorldCond and import class in mk_def_pkl()
	- DONE: create InHandAndGarmentWornCond and import class in mk_def_pkl()
	- DONE: instantiate read_scroll_in_throne_room_cond of class InHandAndRoomCond and run mk_def_pkl()
	- DONE: instantiate read_scroll_hedgehog_exist_cond of class InHandAndExistInWorldCond and run mk_def_pkl()
	- DONE: instantiate read_scroll_crown_worn_cond of class InHandAndGarmentWornCond and run mk_def_pkl()
	- DONE: instantiate read_scroll_win_cond of class PassThruCond and run mk_def_pkl()
- DONE: results
	- CANCEL: create Result class WinGameResult and import class in mk_def_pkl() [use class BufferAndEndResult instead]
	- DONE: instantiate scroll_wrong_room_result of class BufferOnlyResult and run mk_def_pkl()
	- DONE: instantiate scroll_no_hedgehog_result of class BufferOnlyResult and run mk_def_pkl()
	- DONE: instantiate scroll_crown_not_worn_result of class BufferOnlyResult and run mk_def_pkl()
	- DONE: instantiate scroll_win_game_result of class BufferAndEndResult and run mk_def_pkl()
- DONE: mach
	- IDEA: mach = post_act_cmd
	- DONE: instantiate kinging_scroll of class ItemMach and run mk_def_pkl()
	- DONE: update conditions with match_value variable == False to test for False condition
		- DONE: update InHandAndRoomCond with match_cond
		- DONE: update InHandAndExistInWorldCond with match_cond
		- DONE: update InHandAndGarmentWornCond with match_cond
	- DONE: testing
		- DONE: 'look' post silver_key => index error
		- CANCEL: need to update active_gs.mach_obj_lst() to check for class ItemMach
		- FINDING: kinging_scroll not triggering on read but should show as a mach (hasattrib trigger_type)
		- DONE: print out machs found from post_action and troubleshoot => trigger_val => ['read','illuminated_letters']
		- DONE: correct re-assignment variable for 1st Condition
		- DONE: clean up comments


##########################
### VERSION 3.68 START ###
##########################
Version 3.68 Goals
- finish replicating original console game
- in-depth testing

- DONE: update score()
	- DONE: create custom score based on ending == 'won'
	- DONE: add in 5 pts for defeating goblin (to get to 75 total)
- DONE: Create title() routine and static_dict to be referenced in ending()
- DONE: sort out kinging_scroll machine implementation
	- IDEA: for kinging_scroll mach, correct cond from 'scroll in hand' to 'scroll in room scope'?
	- IDEA: Does the 'error' case eliminate the need for "noun testing" / "scroll in scope" in post_action(); Can I drop term?
	- IDEA: kinging_scroll *is* the machine... so if it can be *run* it can be *read* => no need for item check!!!
	- DONE: eliminate item element of scroll Conditions
		- DONE: InHandAndRoomCond() => RoomCond()
			- DONE: comment clean-up
			- DONE: dedup RoomCond()
			- DONE: comment clean-up
		- DONE: InHandAndExistInWorldCond() => InWorldCond()
			- DONE: refactor
			- DONE: comment clean-up
		- DONE: InHandAndGarmentWornCond => WornCond()
			- DONE: refactor
			- DONE: comment clean-up
- DONE: remove big_bomb test object
- DONE: eliminate RoomCond from goblin_attack machine?
	- DONE: refactor
	- DONE: clean-up comments
- DONE: match DCv3 room description to DCv2
	- DONE: refactor
	- DONE: clean up comments
- DONE: description updates
	- DONE: in the end scene, the hedgehog places the sword before Burt's feet and kneels?
	- DONE: also update hedgehog key trade to place key in Burt's hand
	- DONE: highlight in Moat description how east or west off the drawbridge will lead to a fall into the moat
- DONE: "beginner's mind" testing
	- DONE: text updates
	- DONE: verbs in alphabetical order
	- DONE: When in antechamber and 'x portcullis', pary comes before attack?? => solved
	- DONE: should have a warning for 'eat biscuits' => with issues... grrr... see 3.7.2 to-dos
- DONE: submit final version of 3.68 - procedural code parity achieved!!


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


##########################
### VERSION 3.70 START ###
##########################

Version 3.70 Goals
- extend existing Creature attributes and methods to include existing attributes for burt

- DONE: watch refactoring best-practices videos so I can refactor as I go (I will be re-coding a LOT)
- DONE: update existing Creature class and creaatures (e.g. hand & worn)
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
	- DONE: new feature_lst attribue
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
		- DONE: create vis_lst() method
			- DONE: create vis_lst() to get visible creature inventory
				- DONE: returns hand_lst for all creatures
				- DONE: returns feature_lst for all creatuers
		- DONE: update active_gs.scope commands to use vis_lst() method
	- DONE: worn_lst
		- DONE: add attribute & extend instantiation
		- DONE: create setters & getters
		- DONE: create append & remove methods
		- DONE: create examples for hedgehog & goblin
			- DONE: red_bandana, half gold retriever, half retro martial arts master
			- DONE: big_medal; writing = gold_capitals = "'GUARD GOBLIN OF THE FORTNIGHT: FOR MERITORIOUS MEMORANDUMS AND THE VIOLENT SUPPRESSION OF MINOR INFRACTIONS'"
		- DONE: add new obj to mk_def_pkl() pickle statement and also to creature worn_lst attribute
		- DONE: add worn_lst to vis_lst()
		- DONE: add to creature examine
		- DONE: test
		- DONE: add to look
		- DONE: test
	- DONE: invis_lst (new name for mach_obj_lst)
		- IDEAS:
			- creatures can have 'invisible' attribute for machs (like rooms)
			- change mach_obj_lst to 'invisible'? or 'invis_lst'?
		- DONE: create is_mach() method and assign to classes (MachineMixIn, Warning, & Timer classes return True; all others False)
		- DONE: rename mach_obj_lst => invis_lst
			- DONE: creature_class_def.py
			- DONE: gs_class_def.py
		- DONE: create mach_lst() / all_lst method for creatures (based on vis_lst)
		- DONE: update active_gs. mach scope commands to use mach_lst() method
	- DONE: refactor Creature methods
		- DONE: review and shorten all attribute and method names; * remember that the method will always be associated with an object! *
			- DONE: creature_state => state
			- DONE: dead_creature_obj => corpse
			- DONE: shorten dict naming for all dicts - 2_word *max*!
		- DONE: re-order attributes for better flow
		- DONE: use not-in-hand generic validation for put, show, & give in cmd_exe prep case code


##########################
### VERSION 3.71 START ###
##########################

Version 3.71 Goals
- pre-Burt-to-creature conversion clean-up in Invisibe to Container classes and scope methods
- start exercising refactor skills!

- DONE: create validate.py module
	- DONE: simplify app_main.py
		- DONE: guard pattern for start_up.py call
		- DONE: guard pattern for user_input == 'quit' or user_input == 'q' 
			- DONE: extract quit from abreviations and one_word
			- DONE: move cmd_override closer to usage
	- DONE: create validate() module
		- DONE: move case = 'error' code from cmd_exe() to validate()
		- DONE: guard pattern the case == 'error' if-else
		- DECISION: no clock tick for *any* error in validate()
			- time_incr(), pre_action, cmd_exe, post_action, and auto_action only run if validate returns True and not 'quit'	
		- DONE: combine move_valid code from app_main() & cmd_exe() => validate()
		- DONE: move special_errors from cmd_exe() and in-line prep case error checking in cmd_exe() to validate()
		- DONE: analyze existing special_errors
		- DONE: sort out specail_errors that deal with method limitations
			- DONE: move read-not-writing error to read method (currently commented out)
			- DONE: maybe eliminate random interpreter errors?
			- DONE: create a multi-line docstring per PEP257
			- DONE: create mini doc for remaining special / generic errors (4x different kinds of errors - 1x interp & 3x command)
			- DONE: document brief history of validate: errors were run from cmd_exe but 1) time issues and 2) pre_action / post_action issues
		- DONE: clean up validate; use guard pattern (a lot!)
		- CANCEL: improve / expand generic error checking
- DONE: refactor review for show() and give() methods
	- DONE: move to algorithmic key generation (gets rid of whole show_dict; big parts of give_dict)
		- DONE: show
		- DONE: give (shorten 'accept_item' to 'accept')
		- DONE: update show & give to reject item if is_container or is_creature
	- DONE: refactor pass - basics
		- DONE: shorten variable names
		- DONE: MOVE ASSIGNEMENTS CLOSER TO USAGE!
		- DONE: leverage if-then shield pattern 
		- DONE: provide 'None' options for variables and 'match' options for Conditions
		- DONE: Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}"
		- DONE: ensure graceful failure of missing key lookups
		- DONE: comment each new attribute
		- DONE: add tripple-quote doc_strings
	- DONE: refactor pass-advanced
		- DONE: auto-gen keys
		- DONE: return the conditional comparison value itself (bool)
		- DONE: Concatenate strings with '.join'
		- DONE: merge / shorten if-then-else with use of 'and' & 'or'
		- DONE: consider removing 'inline variables' that are only used once... just return the assigned value...
		- DONE: use enumerate to get index & value!
		- DONE: use 'any' to return boolean rather than for-looping through lists
		- DONE: don't need to check for if len(lst) > 0: ;; just use if lst: (Also, bool(None) == False
		- DONE: use list comprehension: 'squares = [i*i for i in range(10)]'
	- DONE: write brief essay on naming conventions (!!!) (what about give_dict 'accept' case?)
- DONE: refactor next phase
	- DONE: refactor door() (same detailed refactor approach as give() & show() above)
		- DONE: shorten variable names
			- DONE: open_state => is_open
				- DONE: noun_class_def()
				- DONE: result_class_def()
			- DONE: unlock_state => is_unlocked
				- DONE: noun_class_def()
		- N/A: move var assignments closer to usage
		- DONE: leverage if-then shield pattern
		- DONE: provide None options for attributes (flexible implementation for inherited classes like Container)
		- DONE: format strings w/ f-strings
		- DONE: comment each new class-specific attribute
		- DONE: add tripple-quote doc_strings
		- DONE: detailed testing
	- DONE: refactor ViewOnly
		- DONE: format strings w/ f-strings
		- DONE: comment each new class-specific attribute
		- DONE: add tripple-quote doc_strings
	- DONE: historic notes on show() & give() - didn't exist in v2
	- DONE: refactor Writing (explain why not a MixIn)
		- DONE: rewrite writing_check() in GameState using any()
		- DONE: variable names
			- DONE: rename writing_check() => chk_wrt_is_vis()
				- DONE: gs_class_def.py
				- DONE: noun_class_def.py
				- DONE: validate.py
		- DONE: created is_writing()
		- DONE: rework read() error checking with use if is_writing()
			- not is_writing && not check_obj_scope() => not here
			- not is_writing && is check_obj_scope() => use x
			- not check_writing_scope() => don't see it written anywhere
			- => read writing
		- DONE: if-then shielf pattern
		- DONE: f-strings
		- DONE: refactor get_dynamic_desc_dict in active_gs()
			- DONE: rename dynamic_desc_dict => dyn_static_dict
				- gs_class_def()
			- DONE: rename get_dynamic_desc_dict => get_dyn_descript
				- gs_class_def()
				- noun_class_def()
			- DONE: rename set_dynamic_desc_dict => set_dyn_descript
				- gs_class_def()
				- start_up()
		- DONE: refactor get_dyn_descript and set_dyn_descript in GameState (use if-then shield)
		- DONE: refactor get_descript_str in noun_class_def() (eliminate interim var descript_str)
		- DONE: comment all vars
		- DONE: string_doc:
			- DONE: writing()
			- DONE: read() (note that read() is uniquely excluded in validate() ) ; also note the idea that writing diff from contents; peering to read
			- DONE: get_descript_string()
	- DONE: refactor Invisible
		- DONE: Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}"
		- DONE: comment each new attribute
		- DONE: add tripple-quote doc_strings
	- DONE: create vis_obj_display for Creature class and re-use in Room
	- DONE: refactor Container (vars, add None options, etc), put() method
		- DONE: shorten variable names
			- DONE: contains => contain_lst
				- DONE: mk_def_pkl()
				- DONE: noun_class_def()
			- DONE: in_container() => chk_in_contain_lst()
				- DONE: noun_class_def()
		- DONE: refactor vis_lst
		- DONE: refactor examine; move print_contents local
		- DONE: refactor put
		- DONE: attributes commented
		- DONE: consolidate contain_str into vis_obj_dispaly
		- DONE: consolidate worn_str into vis_obj_display
		- DONE: add vis_obj_disp() to ViewOnly as pass function so that Room.examine() can run vis_obj_disp() for all non-Items
		- DONE: doc_strings
			- DONE: put: why put() is a method of Container not Item (want to constrain to required obj); similar for show() & give() for Creature
			- DONE: put: if curious about why no containers in containers see node hierarchy in room
			- DONE: other complex methods
			- DONE: container: obj know what's in them; keep data in one place
	- DONE: misc clean-up
		- DONE: Writing descript_key doc_string => Zork tradition of purple prose - leaning in on this
		- DONE: final decision on renaming Classes to 'generic' names (choice is 'generic')
			- Suitcase => PortableContainer
			- Jug => PortableLiquidContainer
			- Beverage => Liquid
			- Shelf => Surface
		- DONE: update 'inventory' to equate to 'examine burt'
			- DONE: description update: "You take stock. Manly rough-and-tumble good looks - check, finely-honed baking skills - check, affable and rougish demeanor - check! If not for the..."
		- DONE: capitalize Creature traits? - Yes!
			- DONE: goblin descript => 'viscious Officessness', 'petty Officiousness'


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
		- DONE: elim static_dict entry for attribute key
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
- DONE: refactor Room class
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
		- DONE: universalize use of title, description, writing, condition, vis_obj_lst
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
	- DONE: investigate all 3 mach scope methods in GameState
		- DONE: it appears that def auto_in_alert_scope() is never called
		- DONE: it appears that only mach_obj_lst() and auto_in_alert_scope() ever call room_mach_lst()
	- DONE: simplify mach scope methods in GameState
		- DONE: merge room_mach_lst() => mach_obj_lst()
		- DONE: elim auto_in_alert_scope()
		- DONE: testing
		- DONE: clean up comments
	- DONE: move GameState mach_obj_lst() method to Room
		- DONE: troubleshoot use of is_mach()
			- DONE: clean up comments
		- DONE: rename mach_obj_lst() to get_mach_lst() and create in Room
		- DONE: refactor as needed
			- DONE: prefer use of mach_lst.append(Creature.invis_lst) over Creature all_lst() => mach_lst()
		- DONE: migrate refs to Room
			- DONE: pre_action()
			- DONE: post_action()
			- DONE: auto_action()
			- DONE; gs_class_def()
		- DONE: clean up comments (creature_class_def, pre_action(), post_action(), auto_action() )
		- DONE: comment out / elim Creature all_lst() and mach_lst()
	- DONE: rename vis_contain_lst() to get_vis_contain_lst() ???
		- DONE: noun_class_def
		- DONE: creature_class_def
		- DONE: interp
	- DONE: refactor room next steps
		- DONE: comment each attribute
		- DONE: simple doc_strings
		- DONE: update creature & container restrictions
			- DONE: container can't hold container or creature (or, someday, surface) [limit in put()]
			- DONE: creature can't hold creature (or, someday, surface) [limit in show() & give()]
			- DONE: update get_vis_contain_lst()
				- DONE: sort out contain_lst list comprehension
			- DONE: update contain_disp()
			- DONE: test royal_hedgehog with hand_lst == [glass_bottle]
		- DONE: New node level rules:
			- containers can't hold containers or creatures (or, someday, surfaces)
			- creatures can't hold creatures (or, someday, surfaces)
			- someday, surfaces can't hold creatures or surfaces
			- This aligns all creatures with Burt definition and means a max search depth of node 3
				- e.g. Room => Creature => PortableContainer => obj or Room => Surface => PortableContainer => obj
		- DONE: New, NEW, node level rules
			- Creatures and Surfaces can't be put in Containers
			- PortableContainers CAN be put in Containers
			- But PortableContainers CAN'T be put in PortableContainers
			- Zork Kitchen as key reference
		- INPROC: Not thrilled with 3 independent versions of put()
			- DONE: how about creating a chk_content_prohibited() method in Container
			- DONE: next, extend in PortableContainer
			- DONE: extend in PortableLiquidContainer
			- DONE: clean up comments
	- DONE: node doc_string
		- IDEA: Node Level (node_lvl) refers to the first-pass list of obj available in the room
			- (i.e. not including those obj in containers or creatures)
		- Imagine an inverted tree... node_0 is at top (say room)
			- node_1 are immedaite contents of node_0
			- node_2 = the contents of node_1 obj
		- we can talk about relative vs. absolute node levels
			- the goal is for look to return information on node_lvl 0, 1, & 2
				- receptacle = container, creature, surface
				- (i.e. describe the room, room contents, and items inside room receptacles)
				- inventory is similar - it is the node_lvl 0, 1, & 2 description of Burt
			- however, we want all node levels to actually be in scope
				- we do NOT want node levels to go too deep... we already forbid containers from holding containers or creatues
				- we could also forbid creatures (other than Burt) from holding creatuers or containers...
				- This would make our max node level = 3: entrance => burt_hand => bottle => water
				- The limit could be imposed at the give(), show(), take(), and put_in_hand() mehtods
			- if this caused serius issues there could be a modular machine to swap in a dummy non-container obj
			- could also run a pre-start check on container & creature to throw errors on illegal contents
- DONE: make 'disp' a method prefix???
	- DONE: contain_disp => disp_contain
		- DONE: creature_class_def
		- DONE: noun_class_def
		- DONE: test
	- DONE: cond_disp => disp_cond
		- DONE: switch_class_def
		- DONE: noun_class_def
		- DONE: test
- DONE: update 'version', modeule dates, to_do.md, and done.md; commit and tag!


##########################
### VERSION 3.73 START ###
##########################

Version 3.73 Goals
- refactor Burt as a creature object
- refactor coding as I go

- DONE: full review of all active_gs attributes to be moved to burt_obj
	- DONE: will also enable 'room scope' type methods to move to class Room
- Refactor burt as a Creature class object
	- DONE: create burt obj and make him visible
		- DONE: instantiate burt in mk_def_pkl() (on attack dicts)
		- DONE: burt_creature to be instantiated in entrance.room.floor_lst
		- DONE: create active_gs dict entry that defines hero == burt and create a get_hero() method to get this info
		- DONE: update creature.vis_lst() to include bkpk_lst for self == active_gs.hero
		- DONE: update disp_contain() method for creature to include backpack for self == active_gs.hero
	- DECISION: on initial refactor, all 'action' methods except attack() will be implicitly excuted by active_gs.hero
		- IDEA: making action methods applicable to arbitrary creatures can be considered on a 2nd pass
	- CANCEL: address duplicate obj issue
		- IDEA: we can't test other methods because the interpreter is confused by creature_burt having duplicat items
		- IDEA: to solve this, we need a temporary exception in vis_contain_lst() that excludes obj possessed by Burt
		- IDEA: then maybe we need to create a custom jinv() method in Creature to describe burt's inventory?
		- NEW-PLAN: let's just give burt 1 simple obj in his hand and start by updating eat(), drink(), and drop()
- DONE: map classes and verb methods
- DONE: update verb methods to reference creature_burt
	- DONE: update eat to creature_burt
		- DONE: food in burt's hand
		- DONE: update eat for creature_burt
		- DONE: minor refacto of eat()
		- DONE: update validate() to include active_gs.hero.chk_in_hand() as part of its hand check
		- DONE: clean up comments 
	- DONE: update drink to creature_burt
		- DONE: update drink() method
		- DONE: update creature_burt & gs_burt
		- DONE: clean up comments
	- DONE: update drop() to creature_burt
		- DONE: update drop() method
		- DONE: update creature_burt & gs_burt
		- DONE: clean up comments
	- DONE: update unlock() to creature_burt
		- DONE: update unlock() method
		- DONE: update creature_burt & gs_burt
		- DONE: clean up comments
	- DONE: pause to update Creature method names
		- DONE: creature.hand_item() to creature.get_hand_item()
		- DONE: creature.hand_empty() to creature.hand_is_empty()
			- DONE: creature_class_def()
			- DONE: noun_class_def()
		- DONE: creature.bkpk_empty() to creature.bkpk_is_empty
			- DONE: creature_class_def()
		- DONE: creature.worn_empty() to creature.worn_is_empty()
			- DONE: creature_class_def()
	- DONE: update lock() to creature_burt
		- DONE: update lock() method
		- DONE: clean up comments
	- NOTE: open(), close(), examine(), and read() have no reference to Burt so they do not need to be updated
	- DONE: update take() to creature_burt
		- DONE: update take() method
		- DONE: clean up comments
		- DONE: after updating take(), don't forget to update hand references in score()
	- DONE: update go() to creature_burt
		- DONE: update go() method
	- DONE: update validate() to include active_gs.hero.chk_in_hand() as part of its hand check for prep case (put, show, give)
		- NOTE: show is now fully functional for creature_burt
	- DONE: update give() to creature_burt
		- DONE: update give() method
		- DONE: update creature_burt & gs_burt
		- DONE: clean up comments
	- DONE: fix entrance_moat_mach
		- DONE: update WeaponInHandCond
		- DONE: update IsWeaponAndStateCond
		- DONE: update BufferAndGiveResult
		- DONE: clean up comments
	- DONE: update wear() for creature_burt
		- DONE: update wear() method
		- DONE: clean up comments
	- DONE: update attack() for creature_burt
		- DONE: clean up attack() a bit
		- DONE: update attack() method
		- DONE: clean up comments
	- DONE: update attack_burt() for creature_burt
		- DONE: update attack_burt() method
		- DONE: clean up comments
	- DONE: test push & pull to confirm they have no creature_burt dependencies
	- DONE: update put() for creature_burt
		- DONE: update put() method
		- DONE: clean up comments
	- DONE: fix worn score for burt_creature
	- DONE: fix kinging_scroll machine
		- DONE: update WornCond for creature_burt
		- NOTE: FULL GAME IS NOW PLAYABLE VIA CREATURE_BURT!!
	- DONE: switch 'inventory' => examine.burt
		- DONE: update cmd_exe True-One-Word command
		- DONE: update Creature disp_contain()
		- DONE: clean up comments
	- DONE: can exclude burt from room.disp_contain() using remove(active_gs.hero)
- DONE: review burt => creature plans and clean-up
- DONE: move active_gs.universal_lst timer obj to burt.invis_lst
- DONE: active_gs.get_room() => active_gs.map.get_hero_room()
	- DONE: in active_gs.map create get_hero_room() initial version
	- DONE: test get_hero_room() in read() method
		- NOTE: had issues because active_gs.map does not have a way to reference active_gs; moved get_hero_room() to active_gs with hero for now
	- DONE: find all modules using active_gs.get_room()
		- DONE: noun_class_def() <both get_room and set_room>
		- DONE: interp()
		- DONE: validate()
		- DONE: pre_action()
		- DONE: cmd_exe()
		- DONE: post_action()
		- DONE: auto_action()
		- DONE: score()
		- DONE: gs_glass_def() <method defined here>
		- DONE: creature_class_def()
		- DONE: mach_class_def()
		- DONE: cond_class_def()
		- DONE: result_class_def()
	- DONE - NEW-IDEA: re-use existing active_gs.get_room() calls
		- DONE: replace get_room() code with get_hero_rooom()
		- DONE: Also need to comment out set_room() in Room.go() and in active_gs
		- DONE: And need to convert Read get_hero_room() back to get_room()
		- DONE: comment 'room' out of active_gs.state_dict
- DONE: comment out legacy refs
	- DONE: sort out active_gs hand refs
		- DONE: def get_hand_lst(self):
			- DONE: gs_class_def (def)
			- DONE: cond_class_def
			- DONE: noun_class_def
		- DONE: def hand_empty(self):
			- DONE: gs_class_def (def)
			- DONE: creature_class_def
		- DONE: def hand_check(self, obj):
			- DONE: gs_class_def (def)
			- DONE: validate()
		- DONE: def hand_lst_append_item(self, item):
			- DONE: gs_class_def (def)
		- DONE: def hand_lst_remove_item(self, item):
			- DONE: gs_class_def (def)
		- DONE def put_in_hand(self, new_item):
			- DONE: gs_class_def (def)
		- DONE: def weapon_in_hand(self):
			- DONE: gs_class_def (def)
		- DONE: def inventory(self):
				- DONE: gs_class_def (def)
		- DONE: full test run
	- DONE: sort out active_gs backpack refs
		- DONE: def get_backpack_lst(self):
			- DONE: gs_class_def (def)
			- DONE: noun_class_def
		- DONE: def backpack_lst_append_item(self, item):
			- DONE: gs_class_def (def)
		- DONE: def backpack_lst_remove_item(self, item):
			- DONE: gs_class_def() (def)
		- DONE: full test run
	- DONE: sort out active_gs worn refs
		- DONE: def clothing_type_worn(self, item):
			- DONE: gs_class_def() (def)
		- DONE: def get_worn_lst(self):
			- DONE: gs_class_def() (def)
		- DONE: def worn_lst_append_item(self, item):
			- DONE: gs_class_def() (def)
		- DONE: def worn_lst_remove_item(self, item):
			- DONE: gs_class_def() (def)
		- DONE: light test run
	- DONE: sort out remaining active_gs burt refs
		- DONE: active_gs.state_dict['backpack', 'hand', 'worn']
		- DONE: def get_static_obj(self, static_key):
		- DONE: active_gs.static_obj_lst = {'universal' : [backpack, burt, fist, conscience]}
		- DONE: light test run
	- DONE: sort out old active_gs room refs
		- DONE: def get_room()
		- DONE:	def set_room()
		- DONE: active_gs.state_dict['room']	
	- DONE: full test run
- DONE: clean up all comments
- DONE: review and org all *** MAYBE *** items
- DONE: Update methods to pass 'creature' to them (including Conditions??)
	- IDEA: use 'None' approach shown here: https://stackoverflow.com/questions/42718870/defining-a-default-argument-as-a-global-variable
	- IDEA: don't need an 'exe_silent' mode - just check in method for whether cereature is burt or is in the same room as burt
	- IDEA: if creature == burt: buffer("std txt")  else: if creature in burt_room: buffer("creature txt")
	- IDEA: burt to be default value
	- DONE: go
		- DONE: add default creature attribute and use None state to set to active_gs.hero
		- DONE: add alternate text for creature is not burt
		- DONE: add conditional for text if creature is not in the same room as burt
		- DONE: create test_frog
		- DONE: create machine to move test_frog (start in main_hall and have it walk back & forth between main_hall & antichamber)
		- DONE: test_frog test
			- DONE: test_frog code runs
			- DONE: get test_frog mach to run when Burt is not in the room 
	- IDEA: maybe only enable non-burt creature use of go() method for now?
- DONE: add brass_lantern ?? mention of grues?? "wouldn't want that to go out!")
	- DONE: add brass_lantern ? "wouldn't want that to go out!"
	- DONE: use Zork lantern description and ref of Nana scaring off some pesky "prowler" years ago; "battery-powered brass lantern"
	- DONE: mention of brass langern in inventory
	- DONE: for burt maybe add brass_lantern - always trusty and shining in your off hand... wouldn't want that to go out now would we? Grues...
- DONE: comment out test_frog
- DONE: improve natural language / paragraph (vs. outline) read of examine() for Room & Creature
	- DONE: need a buff_no_cr() method in gs.io for this?
	- DONE: sort out bottle (how should cr work for portable_container)
	- DONE: nearly there - just need to sort out openning container and test burt wearing crown
- DONE: write doc_string essays
	- DONE: verb method / class association
		- Move Container essay to Room & expand with examples
			- Burt, take the Key
			- Burt, put the Cheese in the Box
			- Burt, show the Biscuits to the Hedgehog
			- Burt, go north from the Entrance
		- 3 rules of method association:
			- 1) It's (almost) never the actor - because the actor is (almost) always Burt
			- 2) Ask, who or what is being acted on
			- 3) Choose the noun that is most restrictive


##########################
### VERSION 3.74 START ###
##########################

Version 3.74 Goals
- post Burt => class module neatening
- improve text UI

- IDEA: reorg noun_class_def into base (Invis, Writing, ViewOnly, & Liquid), Item (including Food & Weapon), Room, Door and Container, Surface ??
- DONE: Base
	- DONE: move 'base' (Invis, Writing, ViewOnly) to dedicaated module
		- DONE: Invis
		- DONE: Writing
		- DONE: ViewOnly
	- DONE: reduce 'base' indent to 1 tab
		- DONE: Invis
		- DONE: Writing
		- DONE: ViewOnly
	- DONE: clean up doc_strings for readability
	- DONE: elim from noun_class_def using tripple-quotes
	- DONE: update imports in mk_def_pkl, noun_class_def() & others 
	- DONE: testing
	- DONE: clean up comments
- DONE: Misc (Liquid)
	- DONE: move Liquid to dedicated module
	- DONE: reduce Liquid indent to 1 tab
	- N/A: clean up doc_strings for readability
	- DONE: elim from noun_class_def using tripple-quotes
	- DONE: update imports in mk_def_pkl, noun_class_def() & others 
	- DONE: testing
	- N/A: clean up comments
- DONE: Room
	- DONE: move room to dedicated module
	- DONE: reduce Room indent to 1 tab
	- DONE: clean up doc_strings for readability
	- DONE: elim from noun_class_def using tripple-quotes
	- DONE: update imports in mk_def_pkl, noun_class_def() & others 
	- DONE: testing
	- N/A: clean up comments
- DONE: item_class_def() [Item, Food, Clothes, Weapon]
	- DONE: move to dedicated module
	- DONE: reduce indent to 1 tab
	- DONE: clean up doc_strings for readability
	- DONE: elim from noun_class_def using tripple-quotes
	- DONE: update imports in mk_def_pkl, noun_class_def(), mach_class_def()
	- DONE: testing
	- N/A: clean up comments
- DONE: D&C (door_class_def.py = Door, Container, PortableContainer, and PortableLiquidContainer
	- DONE: move Doors & Containers to dedicated module
	- DONE: reduce D&C indent to 1 tab
	- DONE: clean up doc_strings for readability
	- DONE: elim from noun_class_def using tripple-quotes
	- DONE: update imports in mk_def_pkl, noun_class_def() & others 
	- DONE: testing
	- DONE: clean up comments
- DONE: remove all refs to noun_class_def.py and move module to /legacy folder
- DONE: create new visible class / verb-method map showing module boundaries
- INPROC: tune description spacing
	- TBD: fix 'examine bottle' text
	- TBD: text 'examine box'
	- IDEA: today, upon examine, Door / Container conditions, writing, and contents are spread across multiple lines.
	- IDEA: combine to one line?
	- IDEA: If so, should Writing be last (rather than first)?
	- IDEA: Proposal = each object (other than burt), upon examination, should have:
		- one line for Title (rooms only) 
		- one line for Description
		- one line for Condition, Contents, and Writing (in that order)
		- one line for user input 
		- with one open line between each line of text
	- DONE: standardize examine() of Writing via disp_writing()
	- TBD: in ViewOnly, create chk_writing()
		- DONE: has_writing() => chk_writing()
			- DONE: interp()
			- DONE: base_class_def()
	- DONE: in ViewOnly, create chk_cond()
		- DONE: ViewOnly (False)
		- DONE: Door (True)
		- DONE: Room (True)
		- DONE: LeverSwitch (True)
	- DONE: in ViewOnly, create chk_contain(active_gs)
		- DONE: ViewOnley (False)
		- DONE: Container (variable based on contain_lst)
		- DONE: Room (variable based on floor_lst)
		- DONE: Creature (variable based on lists and if burt)
	- DONE: convert 'chk' to 'has'
		- DONE: has_contain()
		- DONE: has_writing()
		- DONE: has_cond()
	- DONE: in examine(), test for if self.has_writing() or self.has_cond() or self.has_contain: buff_cr, <disp>, buff_cr
	- DONE: testing
		- DONE: solve 'i' (examine burt)
		- DONE: solve creatures in room (problem is in Room disp_contain() )
		- DONE: changed examine() order from <cond> => <contain> => <writing> to <cond> => <writing> => <contain>
			- IDEA: we want to first know everything about the obj we are examining... then about the other objs it contains
		- DONE: full test
			- DONE: fix 'x button' (no description)
			- DONE: fix 'x lever' (double space before and after lever condition)
			- DONE: fix 'open box' when locked (tripple space after 'is locked' response) [need another Container open() 'if... then' for 'locked']
	- DONE: clean up comments
	- DONE: update examine() doc_string
		- DONE: emphasize sepparation of content and presentation (allows for custom display of burt obj)
		- DONE: explain spacing methods
- DONE: final test and version update


##########################
### VERSION 3.75 START ###
##########################

Version 3.75 Goals
- finish non-mach class refactor
- post Burt => Creature updates to Creature class (elim attack_burt() method)

- DONE: reload all tabs post iOS update (16.1)
- DONE: org already refactored classes into consistent sections
	- DONE: create a 'display' section
	- DONE: create template for all comment setions - but delete un-used comment setions
- DONE: consistent sections for doc_strings
- DONE: Dedup methds:
	- DONE: chk_contain_item() and chk_in_contain_lst() in Container class
		- INFO: chk_contain_item() appears in ViewOnly, Room, Creature, Container
		- INFO: chk_in_contain_lst() appears in Container
	- DONE: Comment out chk_in_contain_lst()
	- DONE: full test
	- DONE: clean up comments
- DONE: refactor Weapon
- DONE: refactor Food
	- IDEA: auto-gen descript for eat() ?
	- IDEA: will I ever want the description to varry?
	- DONE: for now at least, use auto-gen description!
	- DONE: clean up comments
- DONE: refactor Clothes => Garment
	- DONE: rename class Clothes => Garment
		- DONE: item_class_def
		- DONE: mk_def_pkl
	- DONE: decision about auto-gen try
		- IDEA: try_buff() takes obj_spec, obj_def, and class_def attributes?
		- DONE: review how implemented in Creature show() and give()
		- DONE: consider centralizing into a special buffer comment (e.g. active_gs.buff_try()  ) [for case of 'if try fails then pass']
		- DONE: cretae buff_try_key() in GameState class
	- DONE: update wear() to use buff_try_key()
		- DONE: comment out wear_descript
		- DONE: updaate obj declarations in mk_def_pkl.py
		- DONE: testing
	- DONE: update take() to use buff_try_key()
		- DONE: update take() method and implement auto-gen using buff_try_key()
		- DONE: comment out remove_descript
		- DONE: updaate obj declarations in mk_def_pkl.py
		- DONE: testing
	- DONE: gen org
		- DONE: attribute clothing_type => garment_type 
		- DONE: Creature chk_clothing_type_worn() method => chk_type_worn()
		- CANCEL: Creature chk_is_worn() method => chk_garment_worn
		- DONE: organize all auto-gens together in static_gbl.py
	- DONE: doc_strings
		- DONE: base doc_strings for Garment class and wear() method
		- DONE: doc_string on where to include buffer text
			- CANCEL: add 'remove descript' for Creature.remove_item() on royal_crown
			- IDEA: essay should be in Garment class, wear() method
			- IDEA: example = wear / remove text
			- IDEA: tempting to put this in the append / remove methods - but then there's no way to silence them
			- IDEA: instead, all buffering should be centralized into the noun methods where 'silence mode' can be enforced 
		- DONE: also doc_string on why NOT remove() command (too many wrong ways to use)
			- CANCEL: create Garment class-specific remove() method that calls take() ??
	- DONE: full test
- DONE: update Food eat() with buff_try_key approach
- DONE: refactor Liquid
- DONE: refactor Switch
	- DONE: fix indenting
	- DONE: implement std comment sections
	- DONE: review ButtonSwitch auto-action
	- DONE: basic doc_strings
		- DONE: class doc_strings
		- DONE: verb doc_strings
	- DONE: extensive doc_strings
		- DONE: overview / is_mach()
		- DONE: mix-in pattern
		- DONE: switches are dumb
		- DONE: Where do switches reside?
- INPROC: refactor Creature
	- DONE: move long doc_strings to end
	- DONE: fix indentation - up to verb methods
	- DONE: fix indentation - show() and give()
	- DONE: fix indentation - attack()
	- DONE: fix indentation - attack_burt()
	- DONE: post-indent testing
	- DONE: elim Creature corpse attribute (we can simply put the dead_goblin in goblin.bkpk_lst)
	- DONE: clean up comments
	- DONE: refactor up to verb methods
	- DONE: create take() method override error
	- DONE: refactor show()
		- DONE: review / document recepatacle policy re: Creatures & Surfaces vs. PortableContainers
		- DONE: clean up comments
		- DONE: org auto-gen descriptions
		- CANCEL: general refactor
		- CANCEL: re-usable approach for double-try ?
		- DONE: update all doc_strings
	- DONE: refactor give()
		- DONE: clean up comments
		- DONE: update auto-gen descriptions
		- DONE: org auto-gen descriptions
		- DONE: general refactor
		- DONE: update all doc_strings
- INPROC: create attack_b() method
	- DONE: create def for attack_b() method using 'attack x with y' format and active_gs.hero as default base_creature
	- DONE: test base attack_b() method
	- DONE: add 'attack_b' to validate check for in_hand
	- DONE: explore use of src_creature and tgt_creature
	- DONE: outline planned sections using comments
		- DONE: initially, replicate existing sections via comments
		- DONE: re-org method to separate actions vs. text ressponse
		- DONE: re-org to identify 'attacker' and 'winner' 
	- DONE: figure out how to reference fist obj? Maybe just first element of tgt_creature.feature_lst ????
	- DONE: update hedgehog attacked_dict to work with new dict_keys
		- IDEA: could have def_unarmed, def_item, def_weapon responses
		- IDEA: can we differentiate between weapon and non-weapon for results
		- DONE: update src_obj with fist obj option
	- DONE: implement results
		- IDEA: creature_flee => creature_flee_rm and creature_flee_dc
		- DONE: refactor old code
	- DONE: implement more rigorous result matrix
		- IDEA: thus far, for a given tgt_creature, result_key has been based purely on src_obj
		- IDEA: this works for a 4 room dungeon with 2 creatures but is inherently limited
		- IDEA: per tgt_creature, result_key should be a combo of <src_obj>_<src_creature>_<tgt_obj>
			- IDEA: where <src_obj> = [src_obj.name, 'weapon', 'unarmed', 'item', '*']
			- IDEA: <src_creature> = [src_creature.name, '*']
			- IDEA: <tgt_obj> = [tgt_obj.name, 'weapon', 'unarmed', 'item', '*']
			- IDEA: else result_key = 'method_default_result'
			- IDEA: options should loop such that more specific options are tried first and the loops are in order of src_obj, src_creature, tgt_obj
			- IDEA: break (flag variant) to exit loop once first hit is found
		- EXAMPLE: hedgehog => 'weapon'_'burt'_* = 'flee_dc' ; 'unarmed'_'burt'_'*' = None <karate kid> ; '*'_'*'_'*' = None <dodge>
			- IDEA: the result key will also be used as an auto-gen key for the custom description
		- DONE: comemnt out / clean up old code
		- DONE: result_code2 => result_code
		- DONE: update result coding
		- DONE: elim interim hedgehog entry
		- DONE: clean up comments
	- DONE: return on gs.hero not in current room
	- DONE: construct and buffer attack initiation string
		- DONE: varry response based on whether src_creature == gs.hero
	- DONE: buffer custom response string
		- IDEA: move to algorithmic key generation for attack_b() responses
		- IDEA: Maybe hedgehog laughs at an attack with a non-weapon?
	- DONE: attack resolution string
		- DONE: implement resolution initiation string for hedgehog
		- DONE: implement resolution ending string for hedgehog
			- DONE: need to rewrite / recode outcomes from consistent (tgt or src) perspective
			- DONE: sort out weapon verb / adj description for hedgehog
	- DONE: test attack_b with burt attacking goblin
		- DONE: burt attacks goblin with key
		- DONE: burt attacks goblin with fist
		- DONE: burt attacks goblin with sword
		- DONE: sort out custom text for burt attacking goblin
	- DONE: test attack_b with goblin attacking burt
		- DONE: update burt obj with attack_dict
		- N/A: update custom attack entries for burt in static_dict
		- DONE: update Result to call attack_b() instead of attack_burt()
		- DONE: fixed goblin_guard obj w/ 'guard_goblin' name; all => guard_goblin
		- DONE: test [not seeing burt keys; key-gen good; need to investigate self.attacked_dict]
			- DONE: next try = copy / paste guard_goblin.name text ???
		- DONE: clean up comments / troubleshooting prints
	- DONE: refine attack output
		- DONE: implement error condition to prevent attacking self
		- DONE: general attack grammar fixes; "You are" vs. "The X is"
		- DONE: for result_code == None, sort out dodge vs. parry
		- DONE: easy parry vs. hard parry?
		- DONE: customize the attack_initiation to work for hedgehog's defense of the shiny_sword
			- DONE: create unarmed obj for hedgehog (Teeth)
			- DECISION: use existing attack response system for royal_hedgehog sword defense
			- DONE: create 'jump_back' result code, static entry, and Burt attacked_dict entry
			- DONE: create custom response for sword defense
			- DONE: instantiate hedgehog_attacks_result of class AttackBurtResult
			- DONE: update Result code to implement attack_b on take() shiny_sword
	- DONE: replace attack() and attack_burt() with attack_b()
		- DONE: attack_b() => attack()
			- DONE: rename attack() => attack_c()
			- DONE: rename acttack_b() => attack()
			- DONE: search for attack_b() usage and update to attack()
				- DONE: interp
				- DONE: validate
			- DONE: test new attack()
		- DONE: eliminate attack_c() and attack_burt() method
		- DONE: clean-up unused custom keys and creature keys
		- DONE: clean up comments - including hedgehog_guard_result
		- DONE: elim attacking dict in Creature class
		- DONE: elim 'attack_burt' in secret_verbs_lst in interp
	- DONE: refactor and simplify new attack code
		- DONE: decide about introducing unarmed attribute holding unarmed obj (i.e. Fist)
			DECISION: document unarmed attack obj as first list in creature.feature_lst
		- DONE: general clean-up / org of static_gbl and delet of un-used creature keys
		- DONE: comment each section of attack()
		- DONE: refactor results
		- DONE: create obj_category function
		- DONE: refactor display
			- DONE: attack initiation display
			- DONE: clean up comments
			- DONE: refactor resolution_strt_str for weapon
			- DONE: clean up comments
		- DONE: fine tune attack display language
			- DONE: if burt unarmed, dodge, not parry
			- DONE: pro-noun for 'not_attackable_default'
			- DONE: clean-up comments
		- DONE: exit debug mode in cmd_exe (prep)
	- DONE: update trigger & code for attack_hedgehog_warning
	- CANCEL: tune creature_class_def code for word-wrap (this is bigger than I thought)
	- DONE: doc_strings
		- DONE: doc_string edit of existing files
		- DONE: doc_string on details of result matrix (and evolution from original version)
		- DONE: doc_string on attack display components
		- DONE: attack() use of hand_inv elevates impact of hand inv; creatures form opinions
		- DONE: doc_string history of attack() as a hot mess and driver for burt as Creature class
- DONE: address 'first item in feature_lst is unarmed attack item' hack (it's a hack but so be it)


##########################
### VERSION 3.76 START ###
##########################

Version 3.76 Goals
- create Surface class
- create Seat class
- pull errors out of validate()
- implement Seat, Bed, and Nook in game

- DONE: create Surface class!! (was 'Shelf')
	- GOAL: similar to container but prep is 'on'; no open() or lock() ; has max_obj attribute
	- DONE: create Surface class inheriting from Container in door_class_def
		- DONE: is_surface() = True; is_container() = False (?); ViewOnly is_surface = False
			- NOTE: decided not to make is_container) = False for class Surface
		- N/A: update forbidden obj for Creature and Container to include Surface
			- NOTE: not needed; just need to not make a PortableSurface class (see Room doc_str)
		- DONE: write over-loading error methods for open(), close(), lock(), unlock()
		- DONE: also need to over-load disp_cond ? Maybe a reason to make is_container() = False ?
			FINDING: does not impact is_container ; just need to over-load
		- DONE: on second thought, let's add Surface class to prohibited... can't hurt right?
		- DONE: update put() in Container to implement max_obj restriction
		- DONE: update display prepositions to be 'in' or 'on' based on is_surface()
		- DONE: update Interp to check for 'on' prep if is_surface(noun_obj)
		- DONE: confirm 'put' still works for validate()
	- DONE: put initial shelf in Main Hall
		- DONE: instantiate shelf obj
		- NONE: is_open and is_unlocked both = None; max_obj = 20
		- NONE: testing!!
		- DONE: clean up comments in Interp
	- DONE: implement Control Panel as Surface!!
		- DONE: create SurfaceMach class in mach_class_def (import Surface class)
		- DONE: instantiate control_panel based on SurfaceMach (import SurfaceMach class)
		- DONE: remove switches from Antechamber feature_lst
		- DONE: tune text
		- DONE: add control_panel to room after guard_goblin dies? (so burt can't push button)
			- DONE: instantiate dispense_panel_mach based on class InvisMach
			- DONE: create InWorldStateCond class
			- DONE: instantiate goblin_exist_cond() based on InWorldStateCond
			- DONE: instantiate dispense_panel_result based on AddObjToRoomResult
			- DONE: add cond & result to mach; add mach to room (remove control_panel from room)
			- DONE: test
			- DONE: update text
		- DONE: create a new result class to also update descriptions of Antechamber
		- DONE: clean up comments in mk_def_pkl, cond_class_def, & static_gbl
	- DONE: sort out how Creatures are prohibitted from holding Creatures or Surfaces?
		- DONE: extended custom take() error to Surface class
	- DONE: doc_strings
		- DONE: Overview
		- DONE: implementation detail
		- DONE: program architecture
		- DONE: historic note

- DONE: define Seat class which inherits from Surface
	- DONE: Seat requirements
		- REQ: basically, Seat is a surface that can hold a creature
			- REQ: will need to update prohibited_obj
		- REQ: by default, seat.max_item = 1
		- REQ: sit() method ('in' or 'on' prep)
		- REQ: determine which node Burt is in (i.e. the seat, not just the room)
			- REQ: having determined node using Creature method, get scope from that node
				- REQ: should all obj have a 'determine node above' ablilty? Just Creature?
			- REQ; also need to know room
			- REQ: burt can 'see' the room; but only interact (including 'x') w items in 'i' / seat
			- REQ: if obj vis but out of reach: "You'll need to stand up to attempt that"
		- REQ: Also need to update the "find burt" method in .map to find him in a seat
			- REQ: would be nice if searched-for obj had a method to define where to look for it
		- REQ: look shows room with 'sitting in seat' condition
		- REQ: seated should be a creature condition
		- CANCEL: vis_lst = seat.vis_lst + room.name
		REQ: also need a stand() method
		REQ: should provide auto-gen text as well

- DONE: create Seat class which inherits from Surface
	- DONE: define Seat class
	- DONE: create sit() method
	- DONE: add auto-gen buff_try for sit() (similar to drink) - but only for burt
	- IDEA: stand should be a Creature method
		- IDEA: don't need seat info, just room; error on in floor_lst already
	- DONE: create stand() method
	- DONE: update "find burt" method in active_gs.map
	- DONE: instantiate test_chair in entrance
	- DONE: test sit with burt
		- PROB: interp hangs because 'prep' verbs expect noun & dir_obj
			- IDEA: 'sit in chair' (or 'sit on chair') is really a 2word command
			- IDEA: for case of sit(), check for 'in' or 'on', then remove them => 2word
			- IDEA: if no 'in' or 'on' error out: "I don't see an 'on' in that sentence"
		- NEW-IDEA: replace sit() with enter()
			- IDEA: mn the future, make 'sit in' a Seat class-based verb synonym for 'enter'
	- DONE: test 'enter chair' with burt
	- DONE: test stand with burt
	- DONE: tweaked 'remove' text for class Garment (in Item verb method take() )
	- DONE: address sit 'look' issues
	- DONE: create method Creature.is_contained()
	- DONE: create method Creature.get_container()
	- DONE: address sit 'i' issues (seated in Seat.full_name condition)
	- DONE: move "in your off hand... brass lantern" to Creature class disp_contain
	- DONE: sort out special case of not displaying lantern if nothing in hand or backpack
		- IDEA: for burt set has_contain() to True
		- IDEA: also need to sort out the spacing for nothing in hand or backpack
		- IDEA: move a buff_cr() to disp_contain for hand
	- DONE: address sit out of scope issues
		- CANCEL: create room.is_reachable()
		- DONE: in validate() check scope after is_vis for 2word => error
		- DONE: why does 'look' work from chair but 'x entrance' does not???
		- DONE: Decide if you can you interact with a Seat while you're sitting in it?
			- DECISION: No
		- DONE: test for 'water' (node_3 obj)
		- DONE: update 'look' to reference Seat state - include "(which you are sitting in)"
		- DONE: validate check for prep case
	- DONE: address sit in scope issues
		- IDEA: update room.remove() to enable burt to interact with inventory & Seat contents
		- DONE: fix remove() for Container
		- DONE: all verbs tested by burt in chair
		- DONE: sort out read() in chair (special properties of class Writing)
			- DONE: in validate(), exclude read() command
			- DONE: create chk_wrt_is_vis() for Container class
			- DONE: check for burt contained and wrt not vis in Container in read() 
		- DONE: sort out drop() and take() of obj in Seat
			- IDEA: Seat could hold obj in addition to burt (i.e. preparing for vehical)
			- IDEA: take() is already limited by validate() to contents of Seat
			- IDEA: however drop() currently always puts items in the room.floor_lst
			- DONE: need to check for containment and spaace in drop method
		- DONE: update room title to f", in the {Seat}"
			- DONE: confirm that get_title_str() is only used in base() and room()
			- DONE: update get_title_str() to include active_gs
			- DONE: update room.get_title_str() to check for creature.is_contained()
			- DONE: update room.get_title_str() to buffer ", in the {Seat}" if contained
			- DONE: test

- DONE: move examine() to Writing class from validate() [because they irk me]
	- DONE: need to sort out how to deal with validate() check on on writing
	- DONE: move validate() 'take liquid' error to class Liquid take() method
	- DONE: stand() => exit()
	- DONE: create context-specific default verb errors in ViewOnly
	- DONE: move exit() to Perch class; maybe re-constitute stand() ?
		- DONE: stand() re-instated
		- DONE: also update interp verb list, interp one_word list, and command on_word function
		- DONE: create exit()
	- DONE: Writing-specific error => validate()
	- DONE: push remaining specific errors out of of validate
		- DONE: obj not in hand
			- DONE: create ViewOnly not_in_hand general error
			- DONE: elim validate() 2word not_in_hand error
			- DONE: elim validate() prep not_in_hand error
			- DONE: update error method name to chk_not_in_hand() [resisted chk_and_disp_not_in_hand ]
		- PAUSE: obj not visible error
			- DONE: in ViewOnly, create chk_not_vis(self, active_gs):
			- DONE: in method, check for vis and then buffer error
			- PAUSE: call error methods from verb methods
				- PAUSE: 'examine', Item class verbs, Door class verbs, 
		- CANCEL: Creature.is_contained == True
		- CANCEL: add base errors (vis, not sitting, not writing) to base_class verb error calls
		- DONE: new plan for errors:
			- DONE: Create std error list:
				- DONE: writing not vis => don't see
				- DONE: non-writin obj not vis => don't see
				- DONE: if creature.is_contained => must exit
			- DONE: Move base verb errors to Writing
				- DONE: move to Writing
				- DONE: test std erros and is_writing on 'show' (final test!)
					- DONE: incorporate writing while contained into std_err?
					- IDEA: method verbs as *extensions* (not overpowers) of error verbs??
					- IDEA: if not self.is_creature(): buffer non-creature error
					- DONE: extend creature.show() off of writing.show()
					- DONE: resolve double error issue (e.g. 'show grimy axe to hedgehog')
						- DONE: Return True on Writing.show() and check at start of Creature.show()
					- DONE: clean up comments
				- DONE: consolidate / fix ViewOnly general errors
					- DONE: chk_not_vis() => err_not_vis()
					- DONE: chk_not_in_hand() => move to Writing; change to err_not_in_hand()
				- DONE: extend new error approach to all verbs
					- N/A: true1word / 'help'
					- DONE: Writing / 'read'
					- DONE: ViewOnly / 'examine'
					- DONE: Item:
						- DONE: 'take'
						- DONE: 'drop'
					- DONE: Door
						- DONE: 'open'
						- DONE: 'close'
						- DONE: convert lock() and unlock() to prep verbs ('with {key}') [update validate]
						- DONE: 'lock'
						- DONE: 'unlock'
					- DONE: Food / 'eat'
					- DONE: move custom enter() and exit() errors from class Item to class Writing
					- DONE: Garment / 'wear'
					- DONE: Liquid / 'drink'
					- DONE: move custom take() Liquid error => Writing
					- DONE: Room / 'go'
					- DONE: Switch
						- DONE: 'push'
						- DONE: 'pull'
					- DONE: Container / 'put'
					- DONE: Seat
						- DONE: 'enter'
						- DONE: 'exit'
					- DONE: Creature
						- DONE: stand => update interp() module to throw error on tru_1word + more words
						- DONE: show
						- DONE: give
						- DONE: attack
		- DONE: decide how to address special errors
			- DONE: fix error w/ container open extension runs even if container already open error plays
				- DONE: found problem - needed to update state first
				- DONE: sort out language & CRS
				- DONE: clean up comments
			- DONE: error order for prep verbs when in Seat (e.g. 'put gate in calligraphy')
				- DONE: review existing errors and re-order based on hierarchy
				- DONE: clean up comments
				- CANCEL: create prep_error() that takes both nouns, chks  exist / wrt 1st; then rch
				- DONE: test and fix in show
					- INFO: test fails because I need to call the *method* from the obj...
					- IDEA: insted, make a func... or make sub methods for top vs. bot cases & call w/ OR
					- DONE: create err_xst() and err_rch()
					- DONE: update err_std() with err_xst() and err_rch()
					- DONE: test use of err_std()
					- DONE: test show() with OR calls of err_xst() and err_rch()
				- DONE: implement for all prep verbs
					- DONE: lock(), unlock(), put(), give(), attack()
				- DONE: clean up comments
		- DONE: update Writing & Validate doc_strings
			- DONE: update error history
			- DONE: doc_string error hierarchy: (not_in_rm, is_wrt, not_in_reach, wrong_class), class_spec
			- DONE: doc_string on validate just for user_input (i.e. Burt)
			- DONE: update validate doc_string to reflect current approach => method & repeating vs. logic
		- DONE: clean up comments in validate
	- DONE: figure out how to commit Git tag
	- DONE: Move 3.76 doc to done


##########################
### VERSION 3.77 START ###
##########################

Version 3.77 Goals
- finish error message tuning by updating validate() and introducting verb method modes
- finish tuning error subsystem
- Add Debug Mode


- DONE: implement validate() pre-test
	- DONE: ideate validate() goals
		- IDEA: need a systemic way to know if player command runs successfully
			- IDEA: needed for command-triggered machines - especially pre-action
		- IDEA: pull verb method 'try' from cmd_exe into validate()
		- IDEA: create an optional verb method mode attribute ('validate', 'std_exe', 'silent_exe')
			- IDEA: enable calling verb methods in non_buffer mode just for pre & post action validation
		- IDEA: introduce 'mode' attribute ('exe_std' and 'validate') to show, give, and put
			- IDEA: call verb methods with a 'mode' variable that can be 'validate'
			- IDEA: mode options = exe_std, exe_silent, or exe_creature (?)
		- IDEA: pass 'mode' into verb methods
	- DONE: finalize plan verb method modes
		- IDEA: initially, 'mode' = 'validate', 'exe_std', and 'exe_silent'
		- IDEA: mode attribute is optional and defaults to 'exe_std'
		- IDEA: error blocks are *only* run from validate() - so are *only* run for players
			- CANCEL: need to figure out how to implement silence mode in Writing error blocks
		- DONE: consider consolidating errors in Writing / Invisible?
			- DECISION: no, seems right to keep class response in class
		- DONE: fully envision / flow-chart validate loop
			- FINDING: intention is to only call error subsystem on mode == 'validate'
	- DONE: validate() clean-up
		- DONE: move doc_string to end
		- DONE: fix indents
		- DONE: elim interp() "random error" option / else option?

	- DONE: tune up error coding
		- DONE: in validate(), prepend "[INTERP]" for interp errors
		- DONE: in base(), combine err_xst() and err_rch() into err_prep_std() ??
			- DONE: lock(), unlock(), put(), show(), give(), attack()
			- DONE: clean up comments
		- DONE: move Writing error blocks to Invisible class
			- DONE: create def is_invisible(self): return True / False in Invisible / Writing
			- DONE: create err_invis_obj() and add to err_xst()
			- DONE: move standard errors to Invisible class
			- DONE: move verb errors to Invisible class
			- DONE: update read() [maybe add in wrt_err as a more special case??]
			- DONE: clean up comments
		- DONE: separate module for Invisible class?
			- DONE: create invis_class_def.py module
			- DONE: move Invisible class to invisible_class_def.py
			- DONE: update imports for Invisible in base_class_def, mk_def_pkl.py, & mach_class_def.py
			- DONE: move error sub-system doc-strings here too
			- DONE: update doc_string to ref errors in Invisible
			- DONE: review base doc_string
			- DONE: doc_string about how errors messages should never *do* anything (time does not pass)
			- DONE: clean up unused imports in door_class_def.py, item_class_def.py, misc_class_def.py
			- DONE: update comment title for all: *** class identity methods ***

	- DONE: implement validate() modes
		- DONE: implement try <cmd>... except... for specific list of word1 and with mode = 'validate'
		- INPROC: update case = '2word' verb methods to use 'mode' and be called by validate()
			- DONE: take(), eat(), drop(), wear(), read(), examine(), open(), close(), drink()
			- DONE: push(), enter(), exit(), pull()
				- DONE: update def
					- DONE: update def to include mode = None as last attribute
					- DONE: move doc_string under def
					- DONE: below doc_string add: if mode is None: mode = 'std_exe'
					- DONE: move creature attribute assignment to below 'if mode is None: '
					- DONE: pre-fix method errors with mode == validate check
					- DONE: update base_error call of method with mode attribute
					- DONE: merge base_error call and local error methods within mode == 'validate'
					- DONE: return True on errors, return False at end of method errors
					- DONE: for lock(), & unlock(): in Surface error add mode & ret True
				- DONE: in Invisible error method, add mode attribute to def
				- DONE: in validate(), add verb to two_word_lst or prep_word_lst
				- DONE: in verb meth, if creature=None is defined, re-order mode=None
			- CANCEL: merge pull() methods in Switch
			- DONE: fix 'pull button', 'push switch' errors
			- DONE: decide about whether to call Invisible error methods with optional mode attribute
				- IDEA: google default attributes in method extension; diff attributes in method extension
				- IDEA: thinking at scale, probably best NOT to declare optional attributes where not used
				- DECISION: don't declare optional attributes that will not be use
				- FINDING: can't remove mode... validate() calls Invis errs w/ mode for non-vrb methods
				- IDEA: how about instead having 2 different methods: <verb> and <verb>_err
				- IDEA: centralize all error coding to <verb>_err in Invisible and call from validate()
				- IDEA: eliminates the need for mode (?) or at least for passing 'validate' as a mode value
				- DONE: check for values needed in method errors
				- DONE: decision on error merge approach => Do It
			- DONE: test shelf w/ no local Surface error for open() or close()
			- DONE: recode '2word' case in validate() with no word1 check
			- DONE: merge method errors with Invisible errors & order verb method response last (post do)
				- DONE: take(), drop(), eat(), wear(), read(), examine(), open(), close(), drink()
				- DONE: push(), enter(), exit(), pull()
					- DONE: update Invis def to _err
					- DONE: confirm non verb method fencing
					- DONE: copy verb meth errs to Invis err
					- DONE: comment out verb meth errs
					- DONE: update validate two_word_lst_2
				- DONE: update validate() add process based on updates
				- DONE: clean up comments
		- DONE: update case = 'prep' verb methods to use 'mode'; call *_err() from validate()
			- DONE: updated validate() 'if word1 in prep_lst:'
			- DONE: lock(), unlock(), put(), show(), give(), attack()
				- DONE: update def to include mode=None as last attribute
				- DONE: comment out base_err refs
				- DONE: below doc_string add: if mode is None: mode = 'std'
				- DONE: move creature attribute assignment to below 'if mode is None: '
				- DONE: return True on verb method errors
				- DONE: update Invis def to _err
				- DONE: confirm non verb method fencing
				- DONE: cut-paste verb meth errs to Invis err
				- DONE: update validate pre_lst
			- DONE: change mode from 'std_exe' to 'std'
			- DONE: remove prep_lst from validate() once all prep cases are complete
		- DONE: update case = 'go' verb methods to use 'mode' and be called by validate()
			- DONE: update 'go' case in validate()
			- DONE: updated go() in room_class_deff()
			- DONE: update go_err() in invisible_class_deff()
		- DONE: update case = 'tru1word' verb methods to use 'mode' and be called by validate()
			- DONE: create one_word_convert_lst in interp()
			- DONE: update interp() one_word_convert for cardinal directions
			- DONE: update interp() one_word_convert for inventory
			- DONE: removed 'inventory' from one_word_only & from cmd_exe
			- DONE: update interp() one_word_convert for look
			- DONE: removed 'look' from one_word_only & from cmd_exe
			- DONE: convert stand() to two_word case: 'stand burt'
			- DONE: create one_word_convert for stand()
		- DONE: update validate()
			- DONE: refactor validate()
			- DONE: update cmd_exe() to single indent
			- DONE: refactor cmd_exe()
			- DONE: maybe need a 'try' block around cmd_exe verb call just in case? (a 3rd error type)
			- DONE: maybe unify tru1word with main code block in cmd_exe() ?
			- DONE: re-refactor cmd_exe()
			- DONE: clean-up un-used code in cmd_exe()
			- DONE: resolve 'help <option>' error and simplify 'help' to run first all in interp()
			- DONE: make validate() random error dict & function local? (post move of 'try')	
			- DONE: make wrong-way errors local to invisible()
			- DONE: clean-up un-used static_dict errors

	- DONE: validate() testing
		- DONE: this will break the 'go south from Entrance' warning... 
			- DONE: probably the easiest fix is to create a re-usable unreachable_room to the south
		- DONE: should be some way to simplify the repeated 'try: ... except:' in validate
		- DONE: clean-up room() imports
		- DONE: validate should resolve get sword while in chair error
		- CANCEL: do I need to check for kinging_scroll in hand since this is a post_act_cmd ???
			- IDEA: address this during modular machine refactoring
		- DONE: update goblin_attack_mach trigger for non-error cmd (e.g. 'x portcullis' and 'x alcove')

- DONE: error sub-system enhancements
	- DONE: interp() error tuning
		- DONE: identify interp() errors with "[INTERP]"
		- DONE: normalize case
	- DONE: error output tuning
		- DONE: sort out validate() error when already wearing crown... 
			- DONE: ideally should be "You're already wearing"... not "not in your hand"
		- CANCEL: elim "can't see an X here" from interp errors?
		- DONE: specific put() error for "put suitcase in suitcase"
	- DONE: better localize dict data (in retrospect, this was not the best idea)
		- DONE: move 'help' responses to help_dict in interp()
		- DONE: 'help' text updates
		- CANCEL: move 'tru_1word' responses and 'version' to cmd_exe() ???
		- CANCEL: move 'introductin' to start_up() ???
		- CANCEL: move 'score' to gs_class_def() ???

- DONE: Debug Mode
	- DONE: add debug boolean to state_dict in mk_def_pkl()
	- DONE: add 1word debug command ('debug_poke53281,0') to one_word_dict
	- DONE: create setter & getter for state_dict in gs_class_def()
	- DONE: code for one_word_command that tells state and sets bool in cmd_exe()
		- DONE: examample: "Debug Mode is now set to True"
	- DONE: use debug mode to change UI
		- DONE: investigate whether error text can be piped to std output => traceback import
		- DONE: in interp(), if debug, set error source pre-fixes & print error to export 
		- DONE: move random errors back to static_gbl().static_dict
		- DONE: in cmd_exe(), if debug, set error source pre-fixes & print error to export (3 cases)
		- DONE: in validate(), figure out how to use buffer rather than print for except error debug
		- DONE: update cmd_exe() except error to buffer traceback and test error cases
		- DONE: create a buff_debug_err() method in gs that takes err msg & performs the if... else
		- DONE: clean up comments and imports in cmd_exe() and validate()

	- DONE: validate() doc_strings
		- CANCEL: interp() doc_string regarding all 'help' cases being handeled locally
		- DONE: determine needed doc_string updates - perhaps overview of errors across INTERP, VAL, & CMD
		- DONE: update Invis err doc_string
		- DONE: doc_string how validate() works
		- DONE: doc_string on debug
		- DONE: doc_string hazzard of non cmd_override pre_action if errors not checked during cmd_exe()
		- DONE: update Switch doc_string regarding where buttons reside
		- DONE: Switch doc_string entry explaining goals
			- IDEA: verb methods should live in switch_x obj and not need to know about each other
			- IDEA: the SwitchMixIn class should not need to know about all sub-classes
			- IDEA: thus, SpringSliderSwich.pull() and LeverSwitch.pull() over-rides are valid compromise
		- CANCEL: doc_string about fake_door option to address error over-ruling goblin_attack case
			- IDEA: this is maybe not the best approach - maybe skip for now and fix with interupt() later

- DONE: update to v3.77


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
	
- DONE: implement MixIn architecture in interactive module
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

	- DONE: general Interactive class clean-up
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
		- DONE: probably time for a high-level refactor review of ContainsMixIn()
			- DONE: review of pre-verb methods
				- DECISION: makes sense to have is_container() and has_contain()
				- FINDING: similar to is_openable() and has_cond()
				- FINDING: identity vs. display status
			- DONE: review of put()

	- DONE: finish the max_weight deployment
		- DONE: assign 'weight' attribute to Creature
			- NOTE: need to include weight of std items
			- DECISION: assign weigth directly to Creature - not to inventory obj (e.g. 'fist')
			- DONE: add 'weight' attribute to Creature class
			- DONE: add 'weight' setters & getters to Creature class
			- DONE: update Creature obj with weight
		- DONE: assign max_weight attribute to Creatures
			- DONE: add max_weight attribute to Creature class
			- DONE: add max_weight setters & getters to Creature class
			- DONE: update Creature obj with max_weight
				- DECISION: burt = 150, goblin = 999, hedgehog = 999
			- DONE: test!
		- CANCEL: create current_carried_cappacity() method for Creature
			- DECISION: Doesn't make sense; Container was diff - was ViewOnly so had no weight attrib of own
		- DONE: update take_err() to check for 'max_bulk'
			- DONE: update take_err() method
			- DONE: testing!
				- DONE: create big_rock with weight = 40
				- DONE: add big_rock to entrance
				- DONE: Test taking big_rock
		- DONE: update take() to increment Creature.weight
			- NOTE: actually, maybe need to update 'append' method to account for modular machines
			- NOTE: key method to update may be Creature.put_in_hand()
			- DONE: update Creature.put_in_hand()
		- DONE: create get_weight() debug methods for Creature
			- DONE: test!
		- DONE: update drop() and put() to decrement 'weight'
			- NOTE: actually, maybe need to update 'remove' method to account for machines, eat(), drink()
			- DONE: decrement weight on Creature.hand_lst_remove()
			- DONE: test
				- FINDING: Creature.hand_lst_remove() won't reduce burt's weight below starting val ???
				- DONE: troubleshoot (prints and long-form math)
				- DONE: move Creature weight increment to hand append method
			- DONE: address case of item taken from backpack (weight should not change)
			- DONE: address special case of drink()
				- NOTE: needs to be addressed for both Creature and Item
				- IDEA: [Container.contain_lst_remove()]
				- DONE: set earthen_jug weight to 1.5
				- DONE: change drink() => remove_item()
				- DONE: update drink() to decrement Creature weight
		- DONE: weight inc / dec for garment / wear
			- DONE: add baseball_cap to entrance
			- DONE: test!
				- FINDING: weight drops when wearing cap; then increments when taking it
			- DONE: fix
			- DONE: test
		- DONE: standardize portable container weight increment / decrement
			- DONE: move hand weight increment to append method
			- DONE: move Container increment and decrement to append and remove with conditional on is_item()
			- DONE: do I really need an extension for portable container? Can I conditionalize probhibited?
		- DONE: handle case where burt takes item from portable container in his inventory
			- IDEA: ref creature.weight in remove_contain_lst()
			- DONE: create map.get_obj_room(self, obj)
			- DONE: update std_vis_err to give room of non-vis obj if debug == True
			- DONE: test
				- IDEA: need to enhance map.chk_obj_exist() to search containers in containers
				- FINDING: works for 1 layer of container but not 2; need to solve resursive search
				- DONE: troubleshoot chk_obj_exist_recursive
					- DONE: create is_receptical (T for Container, Room, & Creature)
					- DONE: get_contain_lst() (= None execept for Container, Room, & Creature)
					- DONE: create recursive search routine
					- DONE: test gen
						- DONE: works for Entrance
						- DONE: get working for all rooms
					- DONE: Decide on non-Item cases (like Fist, Alcove, front_gate)
						- DECISION: include Room.feature_lst and Creature.feature_lst in get_contain_lst()
						- DONE: update Room.get_contain_lst() and Creature.get_contain_lst()
					- DONE: clean-up comments
					- DONE: optimize code
						- DONE: set default value of lst to room_lst
						- DONE: collapse two functions into 1 recursive!
						- DONE: clean-up
				- CANCEL: normalize Room.chk_contain_item()
					- DECISION: works for now - leave chk_contain_item() as is till refactor of remove()
				- DONE: update map.get_obj_room() to be recursive
					- DONE: updated
					- DONE: check for get_obj_room() call
						- cond_class_def()
						- creature_class_def()
						- interactive_class_def()
						- invisible_class_def()
						- map_class_def() [multiple]
						- result_class_def()
					- DONE: reconsider options to pass just room
						- DECISION: do this!
					- DONE: update code to return room only
					- CANCEL: research how to best dump returned var
					- CANCEL: update get_obj_room() call to accept to 2 vars returned
					- DONE: find obj test!
					- DONE: clean-up code
					- DONE: full game playthrough test
			- DONE: create map.chk_obj_in_creature_inv() [returns bool, creature]
			- DONE: test map.chk_obj_in_creature_inv()
				- DONE: troubleshoot method
				- DONE: full test of method
				- DONE: clean-up method
			- DONE: update remove_contain_lst() to pass active_gs (found only in interactive_class_def)
			- DONE: udate append_contain_lst() to pass active_gs
				- DONE: interactive_class_def()
				- DONE: item_class_def()
			- DONE: update remove_contain_lst() for port container if obj_in_creature to dec creature.weight
			- DONE: create debug wher_is() function and move obj search methods to it
			- DONE: create methods for creatures and items to manipulate weight attribute and apply
				- DONE: Item / Portable Container
					- DONE: create new wethods under Item
					- DONE: add methods under Container
					- DONE: test
					- DONE: clean-up
				- DONE: Creature
					- DONE: create new methods under Creature
					- DONE: add new methods under Creature attribute methods and Container remove (?)
					- DONE: test
					- DONE: clean-up
		- DONE: address give() method if target creature is beyond max_weight
			IDEA: "the X refuses the item. They appear to be overburdened."
		- DONE: handle edge cases (e.g. 1 lb diff order of operations issues)
			- NOTE: very hard to be certain of all cases but I've reviewed; now always remove before append
		- DONE: update Creature.hand_lst_append() to deal with case where Burt will be overburdened by gift
			- NOTE: can happen as result of gift (return gift) or modular machine (e.g. royal_crown)
			- DONE: to pass active_gs to hand_lst_append() I first need to pass it to put_in_hand():
				- DONE: creature_class_def()
				- DONE: item_class_def()
				- DONE: result_class_def()
			- CANCEL: need to update hand_lst_append() to pass active_gs [ just creature_class_def() ]
				- IDEA: keep hand_lst_append() simple and update put_in_hand() with "drop if heavy"
			- DONE: update put_in_hand() to include "drop on floor" (with variable txt for burt / non-burt)
			- DONE: testing!!
		- DONE: drop take test if taking from bkp_lst or worn_lst
		- DONE: is there any reason for Interactive.remove_item() ?
			- FINDING: yes, is a universal scope method called in Invisible, Creature, Interactive, & Room
			- DONE: consistently organized all universal scope methods together for clarity
			- DONE: testing
			- DONE: clean-up
		- DONE: organize universal display methods
			- DONE: testing
		- DONE: use remove_item() in give() ?
		- DONE: doc_strings
			- DONE: purpose for max_weight & max_count: physics puzzles, perlilous travel, finite surfaces
			- DONE: max_weight vs. max_count for creatures
			- DONE: compare weight in dark castle to Zork inventory capacity 
			- DONE: update doc_string for Portable Containers (extensions gone)

- DONE: Clean up from testing and instantiate Creature Containers in actual game
	- DONE: clean up test obj (making it clear which still exist in game)
		- DONE: remove test obj from Entrance
		- DONE: remove screen_door between main_hall and antechamber
	- DONE: move test obj into dedicated section; instantiate but don't place
	- DONE: decide - should creature.is_contained and creature.get_container be ViewOnly methods?
		- DECISION: leave as is (creature method) for now - is only used by Creatures
	- CANCEL: switch creature.stand() => creature.exit()
	- DONE: Throne
		- DONE: create class SeatMach
		- CANCEL: instantiate throne as obj of class SeatMach
		- DONE: reconsider SwitchMixIn... how to make SpringSliderSwitch a true MixIn?
			- NOTE: apparently I created these MixIns before I understood that methods should be included
		- DONE: ViewOnlyButtonSwitch
			- DONE: create ButtonSwitchMixIn
			- DONE: create ViewOnlyButtonSwtich
			- DONE: update red_button to class ViewOnlyButtonSwtich
			- DONE: test / troubleshoot (currently "no effect")
			- DONE: clean-up
		- DONE: SeatSpringSliderSwitch
			- DONE: create SpringSliderSwitchMixIn
			- DONE: create SeatSpringSliderSwitch
			- DONE: update throne to class SeatSpringSliderSwitch
				- DONE: base functionality
				- DONE: For throne, crystal_box is in_reach? Update room / throne text to indicate this?
				- DONE: base functionality test
				- DONE: Description when 'sit': "feels out of kilter - pushed or pulled out of alignment"
					- IDEA: autogen text would need to be conditional (i.e. before & after broach dispensed)
					- DONE: 'throne' descript_key => 'throne_pre_broach'
					- DONE: create 'throne_post_broach' descript_key w/out secrets sentence in static_dict
					- DONE: create static_dict entry (in dynamic section) for Enter method
					- DONE: test
					- DONE: update throne_mach result to change descript_key
						- DONE: create new AddObjToRoomResult class with descript update; pass obj throne
						- DONE: in mk_def_pkl.py, update class referenced by Result and by Mach
						- DONE: test
						- DONE: clean-up
						- NOTE: this is another case that drives a fix / modularization of Machs! 
		- DONE: clean up test_chair class
- DONE: update to v3.78



##########################
### VERSION 3.79 START ###
##########################

Version 3.79 Goals
- General clean-up
- Centralize doc (it's past time!)
- Fix / unify indent
- Create updated app diagram
- Organize module into package


- DONE: create a centralized doc file
	- DONE: create doc.md file in /doc
	- DONE: cut / paste content into doc.md
		- DONE: web_main.py
		- DONE: validate.py
		- DONE: map_class_def.py
		- DONE: invisible_class_def.py
		- DONE: base_class_def.py
		- DONE: item_class_def.py
		- DONE: interactive_class_def.py
		- DONE: room_class_def.py
		- DONE: creature_class_def.py
		- DONE: switch_class_def.py
		- DONE: mach_class_def.py
	- DONE: no doc to move
		- DONE: app_main.py
		- DONE: start_up.py
		- DONE: interp.py
		- DONE: cmd_exe.py
		- DONE: pre_action.py
		- DONE: post_action.py
		- DONE: auto_action.py
		- DONE: score.py
		- DONE: ending.py
		- DONE: mk_def_pkl.py
		- DONE: static_gbl.py
		- DONE: gs_class_def.py
		- DONE: cond_class_def.py
		- DONE: result_class_def.py
- DONE: Fix indent in all modules! (way past time!!)
	- DONE: app_main.py
	- DONE: auto_action.py
	- DONE: cond_class_def.py
	- DONE: ending.py
	- DONE: gs_class_def.py
	- DONE: interp.py 
	- DONE: mach_class_def.py
	- DONE: mk_def_pkl.py
	- DONE: post_action.py
	- DONE: pre_action.py
	- DONE: result_class_def.py
	- DONE: score.py
	- DONE: start_up.py
	- DONE: static_gbl.py
	- DONE: web_main.py
- DONE: don't need to fix
	- DONE: base_class_def.py
	- DONE: cmd_exe.py
	- DONE: creature_class_def.py
	- DONE: interctive_class_def.py
	- DONE: invisible_class_def.py
	- DONE: item_class_def.py
	- DONE: map_class_def.py
	- DONE: room_class_def.py
	- DONE: switch_class_def.py
	- DONE: validate.py
	- DONE: web_main.py
- DONE: diagram modules
	- DONE: in web_main() => while not end_of_game:
	- DONE: in app_main() rename wrapper method to app_main()
	- DONE: comment clean-up
	- DONE: web_main, class_def modules, mk_def_pkl()
	- DONE: app_main [start], static_gbl(), start_up, pickles, 
	- DONE: app_main [rest]
	- DONE: move run chain
- DONE: package modules based on diagram
	- IDEA: create directory structure for modules (e.g. all class definitions in a single directory)
	- DONE: start learning about python packages
	- DONE: first pkg: /dc3/app_main
	- INPROC: based on diagram, group modules together into 'dc3' dir
		- DONE: app_main = __init__.py, app_main, start_up
		- DONE: app_turn = __init__.py, interp, validate, pre_act, cmd_exe, post_act, score, auto_act, end
		- DONE: class_std = __init__.py, Invisible, Base, Item, Interactive, Room, Creature
		- DONE: class_mach = __init__.py, Switches, Mach, Cond, Result
		- DONE: class_gs = __init__.py, GameState, Map
		- DONE: data = __init__.py, static_gbl
		- DONE: tools = mk_def_pkl
			- DONE: solve "No module named 'dc3'" (see dc3/tools/test_import.py)
		- DONE: <root> = __init__.py, web_main, doc.md
		- DONE: move pkls to 'data' and rename
			- DONE: def_pkl
			- DONE: sav_pkl

