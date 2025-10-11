Done List - Dark Castle v3
Feb 11, 2024


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
							- DONE: rename game_state to gs
							- DONE: comment clean up
							- DONE: now that I'm passing gs, simplify classes => single standard import
							- DONE: Mark unused modules
							- DONE: move gs declaration to default_pickle
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
	DONE: move stateful_dict and gs to front of declarations
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
		- DONE: remove full obj declarations from start_me_up() and just declare stateful_dict and gs
		- NOTE: garbage collection still has all obj in scope once master_obj_lst is unpickled!
		- DONE: comment clean-up
		- DONE: remove full obj declarations from wapper() and just declare stateful_dict and gs
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
	- the only thing I really need to use all the time out of master_obj_lst is stateful_dict and gs
someday: ditto for start_me_up


##########################
### VERSION 3.46 START ###
##########################

Version 3.46 Goals:
- Refactor code to migrate variables from stateful_dict => gs

Notes:
- Approach is to migrate variables one sub-dict at a time
- Within main dict, migrate one var at a time

DONE: Refactor stateful_dict['paths']
DONE: Refactor stateful_dict['points_earned_dict']
	DONE: add points_earned_dict to GameState vars and define gs values in make_default_pickle()
	DONE: pass gs to dc3_score
	DONE: create method to get and set score state for a given score_key
	DONE: For items - update score() to use gs score state
	DONE: For rooms - update score() to use gs score state
	DONE: comment out stateful_dict points_earned_dict
	DONE: clean up comments
DONE: "Easy" use cases = 'current_score', 'score', 'move_counter', 'end_of_game', 'game_ending'
	DONE: current_score & score
		DONE: add 'score' to gs.state_dict (and clean up class_deff comments & prints)
		DONE: create increase_score() method for GameState
		DONE: update score() function to call increase_score() method
		DONE: create get_score() method in GameState
		DONE: update print_score() func in helper module to call get_score() method
		DONE: comment out 'score' in stateful_dict
		NOTE: is stateful_dict['score'] even being used???
		DONE: comment out 'score'
		DONE: clean up comments
	DONE: 'move_counter'
		DONE: add 'move_counter' to gs.state_dict
		DONE: create 'move_inc' method in GameState to increment moves
		DONE: create 'move_dec' method in GameState to decrement moves
		DONE: update wrapper() with move_inc
		DONE: update cmd_exe() 'errors' and 'quit' with move_dec
		DONE: create 'get_moves' method in GameState
		DONE: update end() with get_moves
		DONE: comment out 'move_counter' in stateful_dict
		DONE: clean up comments
	DONE: 'end_of_game' & 'game_ending'
		DONE: add 'end_of_game' & 'game_ending' to gs.state_dict and run mk_default_pkl()
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
	DONE: add 'universal' to gs.state_dict and run mk_default_pkl()
	DONE: create get_static_obj method in GameState
	DONE: in cmd_exe() '2word' and 'put' cases pass gs to scope_check() & writing_check()
	DONE: in helper() pass in gs to scope_check() & writing_check() and pass gs to scope_list()
	DONE: in helper() pass in gs to scope_list and update 'universal_lst' with get_universal_scope
	DONE: from noun_handling(), pass gs to root_word_count()
	DONE: from root_word_count, pass gs to scope_lst()
	DONE: test updates
	DONE: comment out 'universal' in stateful_dict and run mk_default_pkl()
	DONE: test updates
	DONE: clean up comments
DONE: pass gs to all class verb methods
	DONE: troubleshoot examine.door error
		DONE: solve bug (scope_check in examine sub for door)
		DONE: clean-up comments
	DONE: '2word' case = read
		DONE: in "try" from '2word' case create if 'read'
		DONE: add gs to method
		DONE: test
	DONE: '2word' case = eat
	DONE: '2word' case = drink
	DONE: '2word' case = take
	DONE: '2word' case = drop
	DONE: '2word' case = close
	DONE: '2word' case = lock
	DONE: '2word' case = unlock
	DONE: '2word' case = open (2 methods)
		NOTE: learned I need to pass gs in super
	DONE: '2word' case = examine (many methods!)
		DONE: Update in cmd_exe() tru_1word() too
		DONE: Update in Room 'go' method in class_def()
	DONE: remove if & try for 2-word case
	DONE: clean-up comments
	DONE 'put' case
		DONE: put => gs
	DONE: in cmd_exe() create rand_error() function
DONE: Refactor stateful_dict['dynamic_desc_dict']
	DONE: move dynamic_desc_dict from stateful_dict to gs
	DONE: comment out stateful_dict sub-dict and re-run mk_default_pkl
	DONE: clean up comments
IN-PROC: 'backpack'
	DONE: add 'backpack' to gs
	DONE: investigate 'backpack' usage
	DONE: create get_backpack_lst method in GameState
	DONE: create backpack_lst_append method in GameState
	DONE: create backpack_lst_remove in method GameState
	DONE: add gs backpack methods to modules and comment out stateful_dict
		DONE: Update scope_lst() in helper(), inventory() in helper(), take() method in Item class_def()
		DONE: comment out stateful_dict
		DONE: clean up comments
DONE: 'hand'
	DONE: add 'hand' to gs
	DONE: create methods: get, append, remove
	DONE: Update helper(), class_def(), & score()
	DONE: comment out stateful_dict 'hand'
	DONE: testing!!
	DONE: clean-up comments
TBD: 'room'
	DONE: add 'room' to gs
	DONE: create methods: get & set
	DONE: update score(), helper(), cmd_exe(), interpret(), class_def()
	DONE: comment out stateful_dict 'room'
	DONE: detailed testing: score(), helper(), cmd_exe(), interpret(), class_def()
	DONE: clean-up comments
IN-PROC: 'out_buff' & buffer()
	DONE: add 'out_buff' to gs
	DONE: create methods: get & buffer
	DONE: in wrapper(), get and combine both stateful_dict and gs buffers and pass the combined out_buff to main()
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
- Migrate most helper() functions to methods of gs
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
	DONE: create method in gs to return list of in-scope inter_obj
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
		DONE: if game_ending not None: gs.set_game_ending(game_ending)
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
		DONE: update to check if in_hand_cond not None: and, if not, for loop to confirm in_hand_lst obj in gs.hand_lst matches in_hand_cond
		DONE: test

DONE: can I used gs.hand_check() in TravelEffect method trig_check() ?

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
	DONE: create gs.put_in_hand(item) method
		DONE: if not hand_empty(), swap current hand_lst to backpack
		DONE: gs.hand_lst_append_item(item) 
	DONE: update TravelEffect trigger() method
		DONE: define room_obj
		DONE: check for take_or_give and either gs.put_in_hand(give_item) 
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
	DONE: Update gs to include 'worn' attribute
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
	DONE: Put gs.put_in_hand() in Item class take() method
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
		DONE: if result_code == 'burt_death': gs.set_game_ending('death')
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
		- IDEA: obj_name+str(count); if exist static_dict[key]: gs.io.buffer(static_dict[key]); else: buffer default
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
		- IDEA: if silent_timer == False: gs.io.buffer(timer_descript_key) where timer_descript_key = name + str(timer_count)
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
		- IDEA: So we need an gs method that can determine if a given timer / auto is in the same room as Burt
		- IDEA: since we can get mach scope for the room Burt is in, it shouldn't be too hard to check if a given timer / auto is in the mach_lst
		- IDEA: this addresses alerts but maybe not results... 
		- IDEA: for example if Burt lights a fuse and walks away - Burt may not be harmed but the room should be changed...
		- IDEA: but that can be dealt with in the future...
- DONE: implement alert_scope for test timer
	- DONE: in gs, create method auto_in_alert_scope(self): which checks to see if self is in mach_lst and returns True or False
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
		- DONE: added 'hedgehog_attack' to gs dict in mk_def_pkl()
		- DONE: created "custom scoring" section in score()
		- DONE: only gs is passed into score() so royal_hedgehog and main_hall are undefined
			- DONE: create room_lst in gs
			- DONE: create an gs method obj_exist() that can evaluate whether an obj is in the game (in any room's room_obj_lst)
			- DONE: call gs.obj_exist(royal_hedgehog) from the "custom scoring" section of score()
			- ISSUE: I have a room search... but royal_hedgehog is *still* undefined... so I guess I need a room search based on obj name
				- IDEA: is this getting silly? Should I just pass master_obj_lst to score()?
				- IDEA: no... there's a value to being able to search rooms by name - and it's ultimately shorter than searching all obj
				- DONE: create obj_name_exist() methd in gs()
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
		- CANCEL: need to update gs.mach_obj_lst() to check for class ItemMach
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
			- i.e. should creatures have a visible_inventory_lst that is part of examine scope? [only 'hand' unless creature = gs.core.hero]
			- only visible if creature = gs.core.hero() ??
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
		- DONE: update gs.scope commands to use vis_lst() method
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
		- DONE: update gs. mach scope commands to use mach_lst() method
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
		- DONE: refactor get_dynamic_desc_dict in gs()
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
		- DONE: re-add worn removal message to gs.worn_lst_remove_item(self)
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
		- DONE: in mk_def_pkl, add instantiated map to gs
	- DONE: map.chk_obj_exist method (was chk_obj_in_map() then was map.chk_obj_in_any_floor_lst() )
		- DONE: create method map.chk_obj_in_any_floor_lst # checks of obj in floor_lst in each room in map
		- DONE: create method chk_name_exist( (was chk_name_in_any_floor_lst() )
		- DONE: rename Room room_obj_lst => floor_lst
		- DONE: update score to use mapchk_name_exist()
		- DONE: update cond with map.chk_obj_exist
		- DONE: confirm that gs.obj_exist and gs.obj_name_exist are no longer needed('goblin_dead' case also addressed in score() )
		- DONE: eliminate gs.obj_exist and gs.obj_name_exist
	- DONE: door_lst() method
		- DONE: create door_lst() method to provide list of doors in room
		- DONE: add map.door_lst() to gs scope method
		- DONE: add map.door_lst() to room.examine
		- DONE: remove doors from room.floor_lst in mk_def_pkl()
	- DONE: obj_cond_disp
		- DONE: create obj_cond_disp method to provide door condition (door / passage names and directions) for room
		- DONE: add to room.examine()
	- DONE: update go() method to use gs.map
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
		- DONE: elim gs.is_valid_map_direction()
		- DONE: elim room.self.door_in_path()
		- DONE: elim room.get_door()
		- DONE: elim gs.get_next_room()
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
			- DONE: update examine() with self.vis_obj_disp(gs)
				- DONE: ViewOnly
					- DONE: Update ViewOnly.examine()
					- DONE: create default def vis_obj_disp(gs) => pass
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

- DONE: full review of all gs attributes to be moved to burt_obj
	- DONE: will also enable 'room scope' type methods to move to class Room
- Refactor burt as a Creature class object
	- DONE: create burt obj and make him visible
		- DONE: instantiate burt in mk_def_pkl() (on attack dicts)
		- DONE: burt_creature to be instantiated in entrance.room.floor_lst
		- DONE: create gs dict entry that defines hero == burt and create a get_hero() method to get this info
		- DONE: update creature.vis_lst() to include bkpk_lst for self == gs.core.hero
		- DONE: update disp_contain() method for creature to include backpack for self == gs.core.hero
	- DECISION: on initial refactor, all 'action' methods except attack() will be implicitly excuted by gs.core.hero
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
		- DONE: update validate() to include gs.core.hero.chk_in_hand() as part of its hand check
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
	- DONE: update validate() to include gs.core.hero.chk_in_hand() as part of its hand check for prep case (put, show, give)
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
	- DONE: can exclude burt from room.disp_contain() using remove(gs.core.hero)
- DONE: review burt => creature plans and clean-up
- DONE: move gs.universal_lst timer obj to burt.invis_lst
- DONE: gs.map.get_hero_rm(gs) => gs.map.get_hero_room()
	- DONE: in gs.map create get_hero_room() initial version
	- DONE: test get_hero_room() in read() method
		- NOTE: had issues because gs.map does not have a way to reference gs; moved get_hero_room() to gs with hero for now
	- DONE: find all modules using gs.map.get_hero_rm(gs)
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
	- DONE - NEW-IDEA: re-use existing gs.map.get_hero_rm(gs) calls
		- DONE: replace get_room() code with get_hero_rooom()
		- DONE: Also need to comment out set_room() in Room.go() and in gs
		- DONE: And need to convert Read get_hero_room() back to get_room()
		- DONE: comment 'room' out of gs.state_dict
- DONE: comment out legacy refs
	- DONE: sort out gs hand refs
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
	- DONE: sort out gs backpack refs
		- DONE: def get_backpack_lst(self):
			- DONE: gs_class_def (def)
			- DONE: noun_class_def
		- DONE: def backpack_lst_append_item(self, item):
			- DONE: gs_class_def (def)
		- DONE: def backpack_lst_remove_item(self, item):
			- DONE: gs_class_def() (def)
		- DONE: full test run
	- DONE: sort out gs worn refs
		- DONE: def clothing_type_worn(self, item):
			- DONE: gs_class_def() (def)
		- DONE: def get_worn_lst(self):
			- DONE: gs_class_def() (def)
		- DONE: def worn_lst_append_item(self, item):
			- DONE: gs_class_def() (def)
		- DONE: def worn_lst_remove_item(self, item):
			- DONE: gs_class_def() (def)
		- DONE: light test run
	- DONE: sort out remaining gs burt refs
		- DONE: gs.state_dict['backpack', 'hand', 'worn']
		- DONE: def get_static_obj(self, static_key):
		- DONE: gs.static_obj_lst = {'universal' : [backpack, burt, fist, conscience]}
		- DONE: light test run
	- DONE: sort out old gs room refs
		- DONE: def get_room()
		- DONE:	def set_room()
		- DONE: gs.state_dict['room']	
	- DONE: full test run
- DONE: clean up all comments
- DONE: review and org all *** MAYBE *** items
- DONE: Update methods to pass 'creature' to them (including Conditions??)
	- IDEA: use 'None' approach shown here: https://stackoverflow.com/questions/42718870/defining-a-default-argument-as-a-global-variable
	- IDEA: don't need an 'exe_silent' mode - just check in method for whether cereature is burt or is in the same room as burt
	- IDEA: if creature == burt: buffer("std txt")  else: if creature in burt_room: buffer("creature txt")
	- IDEA: burt to be default value
	- DONE: go
		- DONE: add default creature attribute and use None state to set to gs.core.hero
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
	- DONE: in ViewOnly, create chk_contain(gs)
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
		- DONE: consider centralizing into a special buffer comment (e.g. gs.buff_try()  ) [for case of 'if try fails then pass']
		- DONE: cretae buff_s() in GameState class
	- DONE: update wear() to use buff_s()
		- DONE: comment out wear_descript
		- DONE: updaate obj declarations in mk_def_pkl.py
		- DONE: testing
	- DONE: update take() to use buff_s()
		- DONE: update take() method and implement auto-gen using buff_s()
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
	- DONE: create def for attack_b() method using 'attack x with y' format and gs.core.hero as default base_creature
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
	- DONE: return on gs.core.hero not in current room
	- DONE: construct and buffer attack initiation string
		- DONE: varry response based on whether src_creature == gs.core.hero
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
	- DONE: update "find burt" method in gs.map
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
			- DONE: update get_title_str() to include gs
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
			- DONE: in ViewOnly, create chk_not_vis(self, gs):
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
			- DONE: update remove_contain_lst() to pass gs (found only in interactive_class_def)
			- DONE: udate append_contain_lst() to pass gs
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
			- DONE: to pass gs to hand_lst_append() I first need to pass it to put_in_hand():
				- DONE: creature_class_def()
				- DONE: item_class_def()
				- DONE: result_class_def()
			- CANCEL: need to update hand_lst_append() to pass gs [ just creature_class_def() ]
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

##########################
### VERSION 3.80 START ###
##########################

Version 3.80 Goals
- Refactor gbl_static and buffering
- Create class just for io that abstracts the io process for the rest of the app

- DONE: Pre-Planning:
	- DONE: org all descript content into one place
	- DONE: decide whether to use __getattr__ (link): 
	- DONE: think through goals of centralized data from tools perspective
	- DONE: think through isolation of static vs. dynamic data
	- DONE: think through modularization of gs
	- DONE: think through desire to modularize descriptions by Creature()
	- DONE: research how to efficiently rename gs.io.buffer() => gs.<x>.buffer()
		LINK: https://www.youtube.com/watch?v=M6EPqUctGrU

- DONE: should static_dict actually be a tupple / namedtupple?
	- DECISION: *NO* - because I do want to be able to alter Tupple entries with tool functions
	- DECISION: I want static_gbl to be centralized for update purposes
	- IDEA: maybe make static_dict() a class with return and update methods?

- DONE: in app_main, rename out_buff => user_output

- INPROC: centralize all static data into static_gbl.py
	- IDEA: think through code vs. data separation for static text
	- IDEA: imagine future adventure creation tooling where I update descriptions via a web front end
	- IDEA: I won't want all the description in a DB - that's too much overhead...
	- IDEA: But I will want all descriptions in one big centralized dictionary for ease of access & update
	- DONE: to this end, investigate centralizing the following dicts:
		- DONE: consolidate val_err_dict from validate() back to static_gbl() static_dict
		- DONE: move interp() help_dict back to static_gbl() static_dict
		- DONE: consolidate dir_err_dict from invisible() back to static_gbl() static_dict
		- DONE: consolidate static_dict into static_dict
			- DONE: static_gbl.py
			- DONE: cmd_exe.py
			- DONE: gs_class_def.py
			- DONE: result_class_def.py
		- DONE: End dict
		- DONE: Score dictionary
			- DONE: move score_val_dict to static_dict
			- DONE: update score routines to call static_dict
			- DONE: migrate item list to static_dict
			- DONE: migrate room list to static_dict
			- DONE: migrate wear list to static_dict
		- DONE: check for other dictionaries to consolidate?
			- DECISION: for now, keep interp() dicts local
	- DONE: [DOC] error messages are hard to update - so I want them to be as generic as possible!
	- DONE: [DOC] tooling plan / central dict

- DONE: rename descript_dict => static_dict

- DONE: should I make static_dict modular so that other dicts can be chosen? 
	IDEA: helpful if I want to temporarily tell adventure from another persepctive
	- TBD: [DOC] writing perspective (need to update doc):
		- burt being a creature and all methods being rewritten to work with Creature class, we have a choice
		- in theory, any creature could be used to play the game - each might have its own description_dict
			- maybe each Creature has its own description list?
			- desc list as creature attribute ???
			- with a default examine() response similar to "the X is not interesting"
			- this would be fun for a short session in a single room but is not practical for extended play
		- realistically, nearly all descriptions will be from burt's perspective
		- but in some cases creatures will use methods to take actions and burt will *obeserve* their actions
		- CANCEL: this should be enabled by mode = 'exe_creature'
	- DECISION: part of making verb methods 'symetric', 'creature' should be checked for in each method

- DONE: create IO class
	- DONE: create class IO
	- DONE: add io as attribute of gs
	- DONE: define io in mk_def_pkl()
	- DONE: test

- DONE: move dyn_dict to io
	- DONE: add dyn_dict as attribute of IO class
	- DONE: add get & set methods for dyn_dict
	- DONE: add dyn_dict to attribute def of io in mk_def_pkl()
	- DONE: update startup() to call gs.io.dyn_dict
	- DONE: update base_class_def() to call gs.io.dyn_dict
	- DONE: test
	- DONE: clean-up gs_class_def(), mk_def_pkl(), startup(), base_class_def()

- DONE: unify descript approach:
	- DONE: investigate auto-gen entries in static_dict
	- DONE: instantiate get_descript_str() in io
	- DONE: redirect read() to gs.io.get_str()
	- DONE: test
	- DONE: redirect examine() to gs.io.get_str()
	- DONE: test
	- DONE: clean-up base_class_def()
	- DONE: test exception case and also torn note case

- DONE: think through a buff_d() method that auto-buffers the called description
	- DECISION: Yes - this makes sense and leads to a natural link of descript & buffer

- DONE: decide if descript & buffer should both be in io... or should each have its own sub-class?
	- DECISION: yes, they belong together

- DONE: migrate buffer() methods to io
	- DONE: add buff_dict attribute to IO class
	- DONE: update mk_def_pkl() with buff_dict definition
	- DONE: update existing buff_get() and buff_reset() methods (in gs) to act on io.buff_dict
	- DONE: update existing buffer methods (in gs) to action io.buff_dict
	- DONE: test
	- DONE: comment out gs.state_dict['out_buff']
	- DONE: get_buff()
		- DONE: create io method for get_buff
		- DONE: update existing get_buff calls to point to io method
			- DONE: app_main
			- DONE: start_up
		- DONE: test
		- DONE: comment out gs.get_buff
		- DONE: test
		- DONE: clean up comments in gs, app_main, and start_up
	- DONE: reset_buff()
		- DONE: create io method for buff_reset
		- DONE: update existing reset calls to point to io method
			- DONE: app_main
		- DONE: test
		- DONE: comment out gs.reset_buff
		- DONE: test
		- DONE: clean-up comments in gs & app_main()
	- DONE: std buffer() method in IO class
		- DONE: create buffer method in IO class
		- DONE: create unified buff_d() method in IO class
		- DONE: update read() and examine() to call buff_d()
		- DONE: test
		- DONE: clean up comments in base_class_def()
	- DONE: buffer calls
		- DONE: investigate how to best update gs.io.buffer(static_dict['x']) calls
		- DONE: maybe create an gs.io.buff_e() method for events (no 'ref' attribute needed)
		- DONE: create buff_f() routine so that calling methods with failure fall-backs can use them
		- DONE: update existing gs.io.buffer(static_dict['x']) with gs.io.buff_e('x')
			- DONE: start_up()
			- DONE: cmd_exe()
			- DONE: ending()
			- DONE: interp()
			- DONE: invisible_class_def()
			- DONE: creature_class_def()
			- DONE: mach_class_def()
			- DONE: result_class_def()
			- 	DONE: sort out DoorToggle result with compound dict lookup and local buffer
		- DONE: investigate whether remaining gs.io.buffer("x") calls can be mass-updated with io
		- DONE: update existing buffer() calls to point to IO class
	- DONE: custom buff calls
		- DONE: migrate custom buffer() methods to IO class
			- DONE: buff_no_cr()
				- DONE: create in IO class
				- DONE: test call in IO class
				- DONE: find / replace calls gs.buff => gs.io.buff
				- DONE: test run game
			- DONE: buff_cr()
				- DONE: create in IO class
				- DONE: test call in IO class
				- DONE: find / replace calls gs.buff => gs.io.buff
				- DONE: test run game
			- DONE: buff_s()
				- DONE: create in IO class
				- DONE: test call in IO class
				- DONE: find / replace calls gs.buff => gs.io.buff
				- DONE: test run game
			- DONE: decide if buff_debug_err() stays or moves to io (will need to pass gs.debug if moves)
				- DECISION: yes, migrate to buff_d() ; must pass 'debug' value
			- DONE: buff_debug_err() => buff_dbg()
				- DONE: create in IO class
				- DONE: test call in IO class
				- DONE: create gs.is_dbg()
				- DONE: find / replace calls gs.buff => gs.io.buff
				- DONE: test run game
	- DONE: clean-up gs(), mk_def_pkl(), validate()
	- DONE: normalize buff options
		- DONE: reconsider integration of get_str() and buffer(); is it consistent??
		- DONE: update buff_s() to check dyn_dict
		- DONE: rename buff_s() => buff_s ['s' for silent failure]
		- DONE: rename buff_f() => buff_f() ['f' for fail]
		- DONE: review buff_f() cases and convert to buff_s() if failure state is pass
			- DONE: convert buff_f()... pass => buff_s()
			- DONE: test
			- DONE: clean-up result_class_def()
		- DONE: decide whether to rename buffer() => buff()
			- DECISION: keep full name buffer() - is easier to distinguish from buff_x() options

- DONE: eliminate direct calls to static_dict()
	- DONE: investigate how many still exist (42 total)
	- DONE: think through approach
		- DECISION: migrate all text calls
		- DECISION: leave dict & lst look-ups as is for now - resolve with end & score class migrations
	- DONE: shorten get_str_no_ref() => get_str_nr()
	- DONE: centralize all text-based static_dict calls to gs.io.get_str_nr() method
		- DONE: interp()
		- DONE: creature()
	- DONE: create list & dict lookups for score & ending
		- DONE: create get_dict_val() in IO class
		- DONE: replace direct calls to static_dict dicts
		- DONE: create get_lst in IO class
		- DONE: replace direct calls to static_dict lists
	- DONE: clean up unneeded imports of static_gbl()
	- DONE: fix result_class() and creature() calls of static_dict
		- DONE: create chk_str_exist()
		- DONE: result_class_def()
		- DONE: creature()
		- DONE: clean up imports of static_dict

- DONE: review old notes and determine which, if any, still need to be done

- DONE: long over-due game_state clean-up
	- DONE: rename gs_class => gs
	- DONE: finally fix get_room => rename and move to gs.map
		- DONE: create get_hero_rm(self, gs) in gs.map
		- DONE: test redirect gs.map.get_hero_rm(gs) calls to gs.io.get_hero_rm() [in score()]
		- DONE: migrate all calls to gs.io.get_hero_rm()
		- DONE: clean-up gs.map.get_hero_rm(gs)
	- DONE: how can sub-classes (IO & Map) call to main class (GameState) [e.g. buff_dbg()]
		- FINDING: just need to pass gs
		- DONE: update io.buff_dbg() => io.buff_dbg(gs)

- DONE: new IO-based features:
	- DONE: Cache last user input and enable 'again' / 'g' command
		- CANCEL: create gs.io.set_prev_buff()
		- CANCEL: call gs.io.set_prev_buff() from end of app_main()
		- IDEA: need to cach input, not output!!!
		- DONE: add 'again' to one_word list; add 'g' to abbreviations_dict (both in interp())
		- DONE: add last_input_str as attribute of gs.io
		- DONE: update app_main() to set gs.io.last_input_str
		- DONE: handle 'again' case in app_main (below gs assignment & quit but above set for last_input_str)
		- DONE: test (fails to cache commands that gen errors; e.g. 's', 'g', 'n', 'g'; does not cache 'n')
			- SOLVED: needed to save obj state on valid_cmd == False in order to cach last_input_str
			- IDEA: this is too bad - I liked forced statelessness for invalid cmds - but no way around it
		- DONE: clean up 'again' one_word and 'g' abreviation
		- DONE: re-add 'again' and 'g' to interp() lists to enable help documentation
		- DONE: clean up set_pre_buff (in gs.io) and set_prev_buff() call (in app main)
		- DONE: clean up 'again' case in interp()
		- DONE: updated buffer to be a str rather than a dict ?
	- DONE: Enable 'wait' / 'z' command
		- DONE: wait command, in app_main... but only process auto_action() & move_incr ??
		- DONE: need to include 'wait' & 'z' in interp() lists for help doc
		- DONE: testing

- INPROC: fix some interp() / help() aspects (revisit why 'help' is in interp() )
	- DONE: copy lists & dicts from interp() to static_dict
	- DONE: call static_dict interp lists & dict
		- DONE: articles_lst
		- DONE: known_verbs_lst
		- DONE: debug_verb_lst
		- DONE: abbreviations_dict
		- DONE: one_word_only_lst
		- DONE: one_word_convert_lst
	- DONE: move help() funtion to cmd_exe()
	- IDEA: do we really need the start-up command as a defined 'one-word-command' ?
		- DONE: eliminate secret start-up code from one_word_only_lst
	- IDEA: lots of specific lists
		- DONE: create one_or_two_word_lst ('help')
		- DONE: pre_interp_word_lst ('quit', 'wait', 'again')
		- DONE: one_word_secret_lst ('debug_poke53281,0)
	- DONE: use cmd_exe() help case for 1-word-help but check for 1 word option first
	- DONE: check on one_word_only_list + one_word_secret_lst on interp() one-word-only case
	- DONE: fix 'wait'
		- DONE: implement 'wait' in app main pre-interp()
		- DONE: remove 'wait' from one_word_only_lst
		- DONE: convert pre-interp commands to lower case
		- DONE: enable 'again' of 'wait' => fix user_input_lc assignment!!
	- DONE: incorporate multiple word lists: 
		- DONE: for 'help one-word-commands': (including one_word_convert_lst)
		- DONE: for 'too many words...' error (not including one_or_two_word_lst)
	- DONE: other word list tuning
		- DONE: improve code efficency of cmd_exe() help case
		- DONE: update 'help basics' to include 'go north' => 'north'
		- DONE: add 'restart' command to app_main
			- DONE: add 'restart' routine in app_main()
			- DONE: in web_main(), key off output to reset start_of_game = True
		 	- DONE: add restart to  pre_interp_word_lst
		- DONE: possibly eliminate use of secret word to trigger startup()
			- DONE: add start_of_game attribute to app_main()
			- DONE: eliminate magic word
			- DONE: clean up comments
		- CANCEL: briefly document the purpose of interp lists in-line in static_dict

- DONE: doc updates
	- DONE: [DOC] purpose of dyn_dict
	- DONE: [DOC] thinking behind isolating static_dict from dyn_dict
	- DONE: [DOC] IO abstraction allows for changes in static_dict structure in the future with min impact
	- DONE: [DOC] long-term DB strat
	- DONE: [DOC] decisions to search for hero rather than cache location
	- DONE: [DOC] update doc about where 2-word help is executed ( interp() => cmd_exe() )
	- DONE: [DOC] eliminate ref to magic word

### OLD NOTES RVIEWED IN V3.80 ###

- DONE: REVIEW OLD NOTES
	- DONE: how to make get_descript_str() [which has a default response] work with auto-gen descript keys [which depend on the possibility of failure]? Need a consistent solution
		- DONE: call with key and return string; will look like gs.descript(key)
		- CANCEL: all autogen keys & vals live in autogen_dict and are pre-fixed with "ag_" (note: the defining feature of autogen keys = try: buffer() ) => consolidate to central dict
	- CANCEL: Can autogen key try be incorporated into Descript method??
		- CANCEL: refactor static_dict 
		- CANCEL: idea was to store (static_dict), autogen_dict (new) and dynamic_dict in Descript class
		- CANCEL: with descript instantiation; i.e. create a gs class (gs_active.io) for descriptions
		- CANCEL: have decided to keep static_gbl.py independent
		- CANCEL: static_dict and autogen_dict live in class
		- CANCEL: dynamic_dict is lone class attribute and is instantiated in mk_def_pkl()

	- DONE: i.o. sub-class:
		- DONE: want an i.o. subclass that stores dyn descriptsions (gs today) and had methods to get descriptions (in base() today) / dyn-descripts (in gs today) and also performs all buffering (in gs today); Would point to universal, centralized static dict (static_gbl)
		- DONE: refactor buffer type commands into gs.io
		- DONE: refactor buffer and caching to gs.io
		- DONE: out_buff => user_output
		- DONE: Use guard pattern and check dicts in this order
			- 1) in dynamic_dict
			- 2) starts with "ag_" => autogen_dict (no "try", allow failure)
			- 3) try static_dic except f"the {obj.full_name} is simply indescribable"

	- CANCEL: alternate descript return ideas for alternate, noun-based methods
		- DECISION: this was a clever idea but actual language is not so symetric
		- CANCEL: test w/ static_dict => start with version 
		- CANCEL: can compound noun methods be created?
		- CANCEL: think abour 'source' and 'desination'... 
		- CANCEL: e.g. for take(), source = is_item in <room>.obj_scope; destination = <creature>.hand_lst
		- CANCEL: need to do a detailed mapping of what is required for success in each noun_class() method
		- CANCEL: this would allow give() to become a noun class method... a take() initiated by burt
		- CANCEL: likewise, show() becomes an examine initiated by burt
		- CANCEL: change goblin re-arm result to take() rather than put_in_hand()

	- DONE: more gs sub-class ideas:
		- DONE: rename gs to gs
		- DONE: modularize remaining GameState class and declarations (???)
		- DONE: perhaps Map, Score, and Descript are classes w/ static dicts in mehod / class and actual obj in gs attributes
		- DONE: Refactor dicts
			- DONE: refactor gs.map
				- gs will have map as an attribute
				- subclass map_dict
			- CANCEL: methods:
				- next room
				- use dict keys to search for item in game world (see score() )
				- return room burt is in

		- DONE: auto-gen keys
			- DONE: consider auto-gen keys for all verb methods (probably not)
			- DONE: Organize auto-gen keys together
			- CANCEL: consider creating a separate dict for autogen keys

		- DONE: refactor hero to gs.core.hero
			- AGREE: get_room() method belongs to this class ?? (or pass gs to gs.map and move get_room there ??)
	- DONE: email to self on Aug 2, 2022)
		- DONE: gs => gs renaming; point to same obj to start with ??
		- DONE: gs holds list of smaller game state components? clock + scoreboard + map + printer ??
		- DONE: modularize mk_def_pkl() and gs ( how about gs.sboard.get_score() )
		- DONE: end() => gamestate ???

### END OF OLD NOTES RVIEWED IN V3.80 ###


##########################
### VERSION 3.81 START ###
##########################

Version 3.81 Goals
- Create gamestate sub-class just for scoring & turn count
- Refactor score sub-class to make it more efficient

- DONE: Problem definition
	- DONE: Review and order all existing notes
	- IDEA: score = class with object being attribute in gs

- DONE: migrate score to sub-class of gs:
	- DONE: create score sub-class
	- DONE: add score as attribute of gs
	- DONE: in mk_def_pkl(): import Score, define score of class Score, add score as attribute of gs
	- DONE: call gs.score.check_score(gs)
		- DONE: fix strange indent error in Score class (had to replace initial tabs with 4-space tabs)
	- DONE: refactor check_score() - first pass
		- DONE: apply code re-use
		- DONE: figure out way to capture custom score pts via standard lists that reside in static_dict
	- DONE: migrate score() data and methods to score_class()
		- DONE: migrate score lists / dicts from gs_class() to score_class()
			- DONE: add points_earned_dict to score_class() attributes
			- DONE: add dict getters & setters to score_class()
			- DONE: redirect score.check_score() to call gets & sets from self
			- DONE: remove points_earned_dict from gs_class() and mk_def_pkl(); clean up check_score()
		- DONE: migrate score attribute and methods
			- DONE: add score to score_class() attributes
			- DONE: add getters & setters
			- DONE: migrate methods
			- DONE: update method calls from gs_class() to score_class()
			- DONE: redirect method calls to gs.score()
			- DONE: clean-up gs_class(), score_class(), mk_def_pkl(), app_main(), ending(), cmd_exe()
	- DONE: clean-up
		- DONE: score.py => legacy folder

- DONE: refactor score() code:
	- DONE: update score dict in gs => list that starts empty and holds achieved score items
		- DONE: create pts_earned_lst attribute in score_class() and mk_def_pkl()
		- DONE: create chk_pts_earned() and set_pts_earned() methods in score_class()
		- DONE: replace score calls in check_score()
		- DONE: clean up points_earned_dict attribute & methods in score_class() and mk_def_pkl()
	- DONE: eliminate get_score() [already have a getter routine, don't need a 2nd]
	- DONE: eliminate update_score()
	- DONE: determine max_score from sum of all possible scores?

- INPROC: additional ideas:
	- IDEA: seems ineficient to check every turn for every point... 
	- IDEA: can I bake scoring into verb methods (e.g. take, go, attack, open)
	- IDEA: better yet, triiger from cmd_exe() and post_act() ?
	- TBD: score_check() to be called from verb methods
		- DONE: create 'score_event_dict' in static_dict
			- IDEA: lookup scorable events in dict of lists with key = verb (e.g. 'take')
		- DONE: create alt score method in score_class
		- DONE: call from cmd_exe() and post_action()
			- DONE: call from cmd_exe() 'go' case
			- DONE: call from cmd_exe() '2-word' case
				- DONE: link front_gate score to opening front_gate
			- DONE: call from cmd_exe() 'prep' case (attack)
				- IDEA: new ideas for 'prep verbs':
					- IDEA: prep case may sometimes require noun and dir_obj
					- IDEA: other times, noun and '*'
					- IDEA: also, some prep verbs don't have simple outcomes (e.g. attack =/ oppenent killed)
					- IDEA: in case of hedgehog, would be nice to use dir_obj.is_weapon()
					- IDEA: among other things, this is maybe a driver to identify prep verbs in static_dict
					- IDEA: for prep case, need to send dir_obj
					- IDEA: universalize score_disp() or crete custom prep_score_disp() ??
					- IDEA: for attack in particular, maybe just check game existence of noun score_disp()
				- DONE: static list updates
					- DONE: create 'prep_verb_lst' in static_dict and call from interp()
					- DONE: create 'var_outcome_verb_lst' in static_dict
				- DONE: update score_disp() for std 'prep verb' case:
					- DONE: add dir_obj attribute to score_disp(); call with None from case 'go' & '2_word'
					- DONE: create score check for standard 'prep_verb' case (list of lists struct)
					- DONE: test 'unlock gate with rusty_key' case
					- DONE: set 'entrance' points to trigger on 'open gate'
				- DONE: address architecture
					- DONE: merge score_event_dict and score_val_dict
						- DONE: address 'go' and '2_word' cases
						- DONE: address basic 'prep' cases
						- DONE: clean-up score_class() and static_gbl()
						- DONE: fix max score calc
					- DONE: update score.pts_earned_lst to store 'noun_str'-'verb_str'-'dirobj_str'
						- CANCEL: replace dirobj = None with alt str (maybe 'none')
						- DONE: alternatively, maybe convert pts_earned_dict to holding tupples?
				- DONE: add vanilla case of 'give' and 'attack'
					- DONE: 'attack guard_goblin' case (dir_obj = 'shiny_sword')
					- DONE: 'give shiny_sword to hedgehog' case (silver_key pts)
					- DONE: 'attack hedgehog' case (dir_obj = 'shiny_sword', 'grimy_axe)
			- DONE: call from post_action()
				- IDEA: for post_action() call, key = mach name
				- IDEA: for post action, final 15 pts should be based on mach run - not win or 'read'
				- DONE: pts for winning mach
					- DONE: update run_mach() to return result.name
					- DONE: update pre_act() and post_act() to accept result.name return
					- DONE: update post_act() (cmd case) to call score_disp(mach.name, result.name, None)
					- DONE: update post_act() (switch case) to call score_disp(mach.name, result.name, None)
					- DONE: update score_dict in static_dict to include entry for 'mach' {'result' : <score>}
					- DONE: test ('get sword' not working)
					- DONE: elminate 'unlock' score
					- DONE: clean-up app_main(), score_dict & static_dict
			- DONE: address special case of 'var_outcome_verb_lst' (?)
				- DONE: address variable outcome verbs
					- CANCEL: add check for 'var_outcome_verb_lst' in score_disp
					- DONE: for 'attack', check for target not exist in game in 'var_outcome' case
					- DONE: for 'give', check for 'noun' in target creature inv
					- DONE: test false cases
				- DONE: implement '*' case for dir_obj
					- DONE: normalize score_dict keys (all tupples)
					- DONE: 'attack hedgehog' case (dir_obj = '*')
						- DONE: troubleshooting => need to update subj_key for pts at bottom of method
						- IDEA: need to sort out correct key (regular or wildcard) early in disp_score()
					- DONE: clean-up score_class(), static_dict
		- DONE: fixes
			- DONE: fix double-dict call - create io_class() method
			- DONE: clean up score_class(), static_gbl(), interp()
	- DONE: document
		- DONE: [DOC] updated approach to score
			- score refactor from module & gs attributes to subclass of gs w/ attributes & methods
			- state-based scoring => action-based scoring (state takes code to inspect)
			- instead of checking every score item every turn, from app_main()...
			- just check relevant actions from cmd_exe() and post_act() [because are validate successful]
			- scoring should also be the result of palyer action so don't need to check on pre_act / auto_act
			- store earned points as tupples of verb, noun, dir_obj 
			- max_score calculation assumes that all positive points are available in a single game
			- (provides unique identifier vs. only one score per noun - e.g. open vs. unlock front_gate)
			- some verbs - even when succuessful - have variable outcomes (e.g 'give', 'attack')...
			- best to check these for successful execution 
			- also nice to have '*' option for dir_obj (avoids listing all weapons for 'attack hedgehog')
			- also, update run_mach doc to mention result.name return

- CANCEL: moves and titles (=> NO, keep these where they are)
	- CANCEL: incorporate move count into score sub-class and create get_moves() method
	- CANCEL: migrate title to score()
	- CANCEL: turn title calc into get_title() method as well (pull from ending() )


##########################
### VERSION 3.82 START ###
##########################

Version 3.82 Goals
- Create gamestate sub-class just for ending
- Refactor score sub-class to make it more efficient

*** end sub-class ***
- DONE: make end routine a sub-class of gs
	- DONE: create end_class_def() including setters & getters
	- DONE: add end as attribute of GameState in gs_class_def()
	- DONE: instantiate End of class end_class_def() in mk_def_pkl()
	- DONE: move GameState end attributes to End class
		- DONE: end_of_game from gs.state_dict => gs.end.is_end_of_game
			- DONE: web_main()
			- DONE: app_main()
			- DONE: start_up()
			- DONE: ending()
		- DONE: game_ending from gs.state_dict => gs.end.end_of_game
			- DONE: app_main()
			- DONE: results()
			- DONE: creature()
		- DONE: testing
	- DONE: additional updates
		- DONE: comment out gs_class_def() and mk_def_pkl()
		- DONE: clean mk_def_pkl, gs_class_def, ending, web_main, app_main, start_up, creature, results
		- DONE: reconsider.... is_end_of_game => is_end ; also, in web_main, is_start
			- DONE: web_main(), app_main(), start_up(), ending(), end_class_def()
		- DONE: why return is_end from start_me_up() ???? (just return False)
- DONE: refactor gs.end()
	- DONE: move end() from ending() to gs.end()
	- DONE: update end() calls in app_main()
	- DONE: test
	- DONE: clean up comments in End and app_main()
	- DONE: ending() => Legacy folder
	- DONE: initial clean-up of end()
	- DONE: set is_end in end() but at top of method
	- DONE: end() => disp_end() # really, the main purpose of method is to display ending text
	- DONE: change initial value of game_ending from 'tbd' => None
	- DONE: convert game_ending to dis_end() sentence: "You have <game_ending>" [died]
	- CANCEL: raise error case if none of end types holds
	- DONE: avoid triggering end state off of game_end != 'tbd' 
		- CANCEL: if game_ending is being changed, just call end() then and there?
		- CANCEL: fix in app_main()
		- IDEA: calling disp_end() immediately after setting game_ending risks score coming after end text
		- IDEA: end text should always be last
		- DONE: should results() and creature() set is_end rather than game_ending?
		- DONE: so work around is setting is_end inline and then calling disp_end based on is_end in app_main
	- DONE: do NOT run auto_act() if is_end == True ??	
	- DONE: incorporate 'restart' into game ending options
		- DONE: add score, moves, and title to 'restart' ending (but this will impact web_main trigger...)
		- CANCEL: trigger restart based on end_of_game attribute rather than user_output => won't work
		- DONE: alternatively, pull specific text string from use_output and trigger restart off of that
- DONE: [DOC] for End class
	- DONE: purpose of disp_end() is to calc title, and present ending text
	- DONE: when facing an end state, set end.is_end, end.game_ending and call end.disp_end()
- DONE: clean up GameState
	- DONE: move debug from state_dict to attribute is_debug
		- DONE: create is_debug attribute and setters & getters
		- DONE: update mk_def_pkl()
		- DONE: is_dbg() => just check state of gs.is_debug bool
		- DONE: update calling methods / functions from gs.state_dict['debug'] => gs.is_debug
		- DONE: test error (gs_class_def), help (cmd_exe), set (cmd_exe)
		- DONE: clean-up gs_class_def, io_class_def, cmd_exe, validate, invistible(), mk_def_pkl()
	- DONE: move move_count from state_dict to attribute
		- DONE: create move_count attribute and setters & getters
		- DONE: update mk_def_pkl()
		- DONE: comment out get_move()
		- DONE: update calling methods / functions
		- DONE: clean up gs_class_def(), end_class_def(), mk_def_pkl()
	- DONE: elim state_dict
		- DONE: elim in gs and mk_def_pkl()
		- DONE: clean up gs and mk_def_pkl()


##########################
### VERSION 3.83 START ###
##########################

Version 3.83 Goals
- Create gamestate sub-class just for core attributes and methods (debug, hero, move_count)
- Refactor early run modules (web_main(), app_main(), and startup() )

- DONE: create Core class and migrate debug, hero, and move_count attributes and methods to it
	- DONE: create core_class_def() including setters & getters
	- DONE: import Core from core_class_def() into mk_def_pkl()
	- DONE: instantiate core of class Core in mk_def_pkl()
	- DONE: add core as attribute of GameState in gs_class_def() and mk_def_pkl()
	- DONE: move GameState end attributes to Core class
		- DONE: move_count from gs => gs.core 
			- DONE: redirect gs.move_count calls to gs.core.move_count
			- DONE: remove move_count attribute from GameState and mk_def_pkl()
			- DONE: clean up gs_class_def() and end_class_def()
		- DONE: migrate move_count methods to Core class
			- DONE: copy move_count methiods to Core class
			- CANCEL: add gs as an attribute of move_count methods
			- DONE: eliminate gs.move_dec() ?
			- DONE: redirect method calls
			- DONE: clean up gs_class_def() and app_main()
		- DONE: is_debug from gs => gs.core
			- DONE: update call gs.is_debug calls to gs.core.is_debug
			- DONE: test
			- DONE: clean up gs.is_debug in gs_class_def() and mk_def_pkl()
			- DONE: clean up comments
		- DONE: hero from gs => gs.core
			- DONE: prep for find & replace
			- DONE: find and replace gs.core.hero => gs.core.hero
			- DONE: clean up gs.hero in gs_class_def() and mk_def_pkl()
			- DONE: clean up comments

- DONE: gs attribute class clean-up / standardize
	- DONE: standardize gs attribute classes in mk_def_pkl()
	- DONE: add name attribute for Map
	- DONE: consistent commenting

- DONE: over-due early code refactoring
	- DONE: refactor of web_main
		- DONE: return is_start from app_main()
	- DONE: refactor of app_main (reverse shield approach? unify)
		- IDEA: key if / then values = is_end, is_wait, is_valid, is_stateful, is_interp_cmd
		- IDEA: # non-interp command # section with elifs
		- DONE: pseudo-code new structure in comments
		- DONE: create to-be comment sections
		- DONE: code it!
		- DONE: [DOC] app_main refactor notes - if-then-shield pattern reversal
	- DONE: [DOC] gs modularization - GameState only holds classes as attributes
	- DONE: refactor of start_up (should all be game instance focussed)
		- DONE: tune post-intro spacing
		- DONE: general refactor clean-up
		- DONE: elim manual text
		- DONE: comment clean-up
		- CANCEL: elim user_output return from start_me_up() [just call get_buff from app_main() ]
			- NOTE: can't call gs.io.get_buff() from app_main() in startup return because don't have gs yet
- DONE: clean up comments in app_main()
- DONE: solve 'z' followed by 'g' / make 'again' work for error cases


##########################
### VERSION 3.84 START ###
##########################

Version 3.84 Goals
- Review minor bug-fix list and set goals for 3.84
- Fix the random bugs!

*** minor bug-fix ***
- DONE: change version & date comments to just web_main() and static_dict (add date to 'version')
- DONE: make title increment (currently 10) a game-settable constant?
- DONE: implement 'stowe' command => put obj in hand into backpack
	- DONE: create stowe() as method of Item
	- DONE: add 'stowe' to verb list
	- DONE: create stowe_err() in Invisible
	- DONE: enable assume contents of hand for drop, stowe, eat, wear
	- DONE: fix 'drop key' & 'wear crown' (2word commands not working for new convert commands)
- DONE: add hero_rm as Map attribute
	- DONE: sort out gs.map.get_hero_rm(gs) => move to .map & std w/ map.get_obj_room()
		- DONE: add hero_rm as attribute of gs.map
		- DONE: setters and getters
		- DONE: set hero_rm to entrance in mk_def_pkl()
		- DONE: update hero_rm on move 
		- DONE: test with print() statement
	- DONE: find cases where hero is searched for and fix
		- DONE: up to and including map_class_def()
		- DONE: remaining cases
		- DONE: test
		- DONE: gs.map.hero_rm => gs.map.hero_rm ???
		- DONE: elim commented 'get_hero_rm('
	- DONE: [DOC] decision to cache hero_rm
- DONE: fix 'attack X' so that it defaults to using Fist if hand is empty
- DONE: add confirmation prompt for 'quit' and 'restart' ?
	- CANCEL: do check in web_main() based on returned exit_req value
	- CANCEL: if exit_req: validate_exit = (Y/N); if validate_exit => end_of_game = True
	- IDEA: all user input must happen in web_main()... so confirmation must happen in web_main()
	- IDEA: but, if 'quit' or 'restart' confirmed, want to show disp_end() text
	- IDEA: so, need to confirm in web_main() and, if confirmed, pass on to app_main()
	- DONE: to simplify web_main() , call start_me_up() directly from web_main()
	- DONE: else statement for getting user_input
	- DONE: if user_input.lower() in ['quit', 'q', 'restart']: confirm w/ 'Y' or 'y'; else break
	- DONE: no longer need to pass is_start to app main; elim
	- DONE: test
	- DONE: clean-up web_main(), app_main()
- DONE: debug
	- DONE: fix debug capacity() (for max_weight only) to work with creatures
- DONE: simplify read() vs. examine()
	- DONE: read() of obj w/ writing => "On the {obj}, written in {wrt}, you see: '{txt}'..."
		- DONE: define has_writing() to return false in Invisible (evaluates writing attribute in Base)
		- DONE: in read(), handle case of not is_writing but has_writing
		- DONE: test
		- DONE: clean up Base and Invisible
	- DONE: read() if no writing on obj => "There's nothing written on the {obj}."
		- DONE: implement in Invisible err
	- DONE: examine writing => "The {writing} reads as follows: n/"
		- DONE: remove is_writing() case from examine_err() in Invisible
		- DONE: create Writing version of examine()
		- DONE: test (error)
		- DONE: clean up Base and Invisible
	- DONE: [DOC]
		- DONE: stowe() commnad
		- DONE: read() vs. examine()
		- DONE: include 'read scroll' as win condition (still need to test 'x lettering')
		- DONE: help for read
- CANCEL: update get_hand_item() to return None if hand_list is empty
	- DECISION: this doesn't really solve the problem...
	- DECISION: we just end up having to check get_hand_item() for None vs. checking is_hand_empty() for T
	- DECISION: if there was just one use case for hand_item we could do it in a function and decide there...
	- DECISION: but there are MANY uses for hand_item...
	- DECISION: the real question here is whether the hand concept itself is worth keeping?

*** already done ***
- DONE: do we need user_input == secret word to trigger startup()? Can't we just pass boolean?
- DONE: naming updates:
	- DONE: re-name 'wrapper' to 'app_main'
	- DONE: update pickle names
- DONE: investigate setters & getters for GameState class
- DONE: is there really any need for GameState room_mach_lst() ??
- DONE: 'try... except' standard descriptions for examine() method (similar to Warnings) (???)
- DONE: refactor app_main() modules
- DONE: refactor app_main() modules
- DONE: put score() & end() between post_action() and auto_action() [i.e. between move 'n' and 'n+1']


##########################
### VERSION 3.85 START ###
##########################

Version 3.85 Goals
- Review to-dos and set precise goals for 3.85
- Isolate game engine vs. game vs. game instance
- create game menu interface
- create mini game 2 (A Cup of Tea)

- IDEA: big picture thinking
	- IDEA: think engine that supports multi-game, multi-player, multi-instance
		- IDEA: engine = modules & static_dict
		- IDEA: game = obj_pkl & game_ver_static_dict
		- IDEA: user = user_id, game_instance_saves
		- IDEA: instance = save games
	- IDEA: most static data is based on game version (e.g. most text; also max_score)
	- IDEA: but some static data is based on game instance (e.g. random # for portcullis => gs)
	- IDEA: for now, don't worry about multi-user - focus is on multi-game

- DONE: instantiate map in mk_def_pkl() and save in pickle in case map someday changes during game (fun idea)

- DONE: decide on game folder structure
	- IDEA: separate folder for game; contains game_static_dict
	- DONE: need a name for my game engine: cleesh (Enchanter spell to turn creature into small amphibian)
	- DONE: cleesh logo = red spotted newt
	- DONE: create games/dark_castle directory
	- DONE: create games/dark_castle/game_file and games/dark_castle/working
	- DONE: change top level directory from 'dc3' => 'cleesh' 
		- NOTE: could have just changed and accepted auto update
	- DONE: test
	- DONE: clean up comments

- DONE: Separate static_dicts for game vs. engine
	- IDEA: planning for tooling in the future
	- IDEA: want to separate what game designer can update vs. what platform / engine designer can update
	- DONE: game_static_dict = game-specific static content
	- DONE: curent game directory as attribute of gs.core
	- DONE: in static_gbl() and io_class_def() update static_dict => engine_static_dict
	- DONE: decide whether to enable explicit dict choice - or just always try game first, engine 2nd
		- DECISION: in general, always try game_static_dict first; on except => engine_static_dict
		- DECISION: should also have an explicit engine-only lookup: get_str_e() [or dict / lst equiv]
	- DONE: consider - separate methods or via passed in mode w/ default = 'std' / alt = 'eng'?
		- DONE: determine & list cases where answer will always be in engine_static_dict (e.g. interp() )
		- FINDING: key cases = get_str, get_lst, get_dict, get_dict_val
		- IDEA: highly unlikely but don't want to enable a case where game designer could over-ride engine
		- IDEA: implication is that all IO methods should be able to support 'enging only' case
		- DECISION: implement as 'mode' that gets passed with default = 'std' (vs. 'eng')
	- DONE: implement get_str() with mode
		- DONE: import game_static_dict
		- DONE: add mode attribute
		- DONE: add additional try-except clause for game_static_dict
		- DONE: test
		- DONE: add if-then clause for mode == eng
		- DONE: implement and test for 'version'
		- DONE: update static dicts => 'game_version' & 'engine_version'
		- DONE: update version() command to show 'engine_version' and, if exist, 'game_engine'
		- DONE: test
	- DONE: create a non-ref version of get_str()
		- DONE: review get_str() method and usage
		- FINDING: can just use get_str_nr()
		- DONE: update get_str_nr() with mode option
		- DONE: test get_str_nr() with version
		- DONE: simplify (remove mode option from) get_str()
	- DONE: implement get_lst() with mode
		- DONE: add optional mode attribute to get_lst()
		- DONE: update standard get_lst() calls for eng_static_dict to include over-ride
			- DONE: cmd_exe()
			- DONE: interp()
		- DONE: clean up comments
	- DONE: implement get_dict() with mode
		- DONE: add optional mode attribute to get_dict()
		- DONE: update get_dict() calls in cmd_exe() and interp() to include 'eng' mode
		- DONE: clean up comments
	- DONE: in cmd_exe() and interp(), convert get_dict_val('dict','key')) => get_dict('dict','eng')[key]
	- DONE: delete unused portion of each static dict
		- DONE: clean-up engine_static_dict
		- DONE: clean-up game_static_dict
		- DONE: full game test
	- DONE: [DOC] game vs. engine approach
	- DONE: [DOC] small number of methods that can guarantee 'eng' mode to avoid risk of rouge game dev

- DONE: de-burt engine / error messages
	- DONE: eng_static_dict = interp, version, help, errors (remove "Burt" ref from errors)
	- DONE: review error messages / engine text not in static_dict and remove any "burt" refs

- DONE: separate version numbers for game and engine
	- DONE: assume a 'lazy game designer' who doesn't create custom values; should work anyhow
	- DONE: create version for each dict
	- DONE: update version() cmd to display both game & enging versions

- DONE: sort out home for game data files and the modules that update them
	- DONE: finalize vision of pkl_sav & pkl_def vs. mk_def_pkl vs. start_me_up() for game
		- IDEA: at this point, we only want to discern between engine, game, and session
		- IDEA: in the future, I will need to implement multi-user
		- mk_def_pkl() =rename=> mk_start_pkl => games\dark_castle\game_file (creates start_pkl) 
		- pkl_def =rename=> start_pkl => games\dark_castle\game_file (generic starting game obj)
		- start_up() => games\dark_castle\game_file (converts start_pkl to active_pkl)
		- pkl_sav =rename=> active_pkl => games\dark_castle\working (holds obj for specific session)
	- DONE: where to keep data like game_name, game_full_name, game_path?
		- IDEA: gs.game_menu class module
			- IDEA: only attribute == game_name ?
			- IDEA: instead, just replace gs.core.game_dir (not yet in use) with game_name
		- IDEA: need a game_menue directory
		- IDEA: in \game_menue , need a gm_menu_static_dict that contains game_lst
			- IDEA: what if game_lst lives in engine_static_dict ?
		- IDEA: gm_menue_static_dict also holds dict of list of [game_full name, game_descript, game_path]
			- IDEA: and game_name, game_full_name, and game_descript live in game_static_dict ?
			- IDEA: and game path always == game_name ??
		- IDEA: need outer game_name loop for web_main() ; set to None at start; if None, go to menu
		- IDEA: menue shows list of games - each with a number, and asks user to choose or quit
		- IDEA: on game_menu choice, populate values of game_menu_class_def()
		- IDEA: on quit from game, game_name is reset to None
	- DONE: create static_dict entries:
		- DONE: engine_static_dict (game_lst)
		- DONE: game_static_dict (game_name, game_full_name, game_descript)
	- DONE: re-purpose gs.core.game_dir => gs.core.game_name
		- DONE: update gs.core()
		- DONE: update mk_def_pkl()
	- DONE: extend web_main() with menu wrapper (no double check on Q for quit)
		- IDEA: initially, just pull list from engine_static_dict and print to screen
		- IDEA: input = table_int or Q to quit 
		- IDEA: don't really need to save game_name ... just need to pass it in to app_main for start_up path
		- DONE: add game menue prompt to web_main()
			- DONE: get user game choice input
				- DONE: re-loop if response is out of range int
				- IDEA: user_num = 0; if userchoice == 'q', break; else try: user_num = int(user_choice); 	except: user_num = 0  ; if usernum > 0 and user_num <= len(game_lst): <good> ; 
				- DONE: handle response is real num
				- DONE: handle resposne is letter
				- DONE: quite on 'q'
	- DONE: create game_menu() module in \app_main to display game menue using PrettyTable
		- LINK: https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
		- LINK: https://amrinarosyd.medium.com/prettytable-vs-tabulate-which-should-you-use-e9054755f170#:~:text=Tabulate%20requires%20you%20to%20import,function%20to%20print%20the%20table.&text=PrettyTable%20allows%20you%20to%20customize,%2C%20alignment%2C%20and%20border%20style.

	- DONE: finalize menue
		- DONE: fix game choice issue (2x option 1 in a row)
		- DONE: clean-up spacing

	- DONE: move game files => /game
		- DONE: copy mk_def_pkl to dark_castle/game_files dir; rename to game_update()
		- DONE: update game_update() to create game_pkl in dark_castle/game_files dir
		- DONE: move start_up() to dark_castle\game_files
		- NOTE: vscode auto-updates web_main() to import start_up() from correct dir
		- DONE: update start_up() to point create active_pkl in dark_castle/working
		- DONE: update app_main() to open active_pkl from dark_castle/working
		- DONE: clean-up
			- DONE: clean up mk_def_pkl() and def_pkl
			- DONE: clean up sav_pkl
			- DONE: clean up comments in game_update() and start_up()
			- DONE: clean up comments in app_main()

- DONE: dynamic pathing
	- DONE: return game_lst from game_menu()
	- DONE: determine game_name from game_lst and validated user_num
	- DONE: update all game file imports to import based on gs.core.game_name
		- DONE: web_main()
		- DONE: gs.io()
			- IDEA; mabybe need to make game_name an attribute of IO ??
			- DONE: move game_name attribute from core to io
			- DONE: create io import funciton ( get_game_dict() ) to import game_static_dict
			- DONE: call import function from io get_str() / get_lst() / get_dict() methods
			- DONE: comment out static import of game_static_dict
			- DONE: clean-up comments
	- DONE: update all pickle paths based on gs.core.game_name
		- CANCEL: game_update [is dedicated to dark_castle => can be static]
		- CANCEL: start_up [is dedicated to dark_castle (for now) => can be static]
		- DONE: app_main
			- DONE: in web_app(), pass game_name to app_main()
			- DONE: in app_main(), compose pickle load string based on game_name
			- DONE: test
			- DONE: clean up comments

- DONE: create alternate (very simple!) game called cup_of_tea
	- IDEA: the only way to really make a muliti-game system is to create a 2nd game
	- IDEA: alt game == cup_of_tea - you play as Cecily who, with her sister, runs the pub
	- IDEA: Cecily is bookish; sister is very popular with lads; Cecily just want peace before pub opens
	- IDEA: wears a cloak with pockets
	- IDEA: initial game: very simple
		- IDEA: single room (pub), obj = tea_cup, hot_tea, rusty_key, comfy_chair; hero = Cecily
		- IDEA: tea writing = "A drink with jam and bread"
		- IDEA: win = drink tea
	- DONE: create adventure
		- DONE: create cup_of_team directory in games/
		- DONE: create game_file/ and working/ directories in cup_of_tea
		- DONE: copy __init__.py file into all 3 directories
		- DONE: create game_update.py template
		- DONE: simplify game_update.py for cup_of_tea obj
		- DONE: obj game_static_gbl() for cup_of_tea obj
		- DONE: start_up() for cup_of_tea obj
		- DONE: create machine for win
		- DONE: win dict entry for game_static_gbl()
		- DONE: add cup_of_tea to game menu (engine_static_dict)
		- DONE: testing!
			- DONE: test 'score' command
			- DONE: add 'help' notice
			- DONE: fix tea_cup
			- DONE: fix chair (add sit descript, address reach)
			- DONE: test 'drink tea' and win condition
			- DONE: fix 'drink tea' score
			- DONE: address door bug
- DONE: wrap on 3.85 and set goals for 3.86 (post multi-game clean-up) and beyond (cup_of_tea enahnce)


##########################
### VERSION 3.86 START ###
##########################

Start Date: May 22, 2024
End Date: Jun 9, 2024

Version 3.86 Goals
- solve the name-to-obj challenge systemically
- tune start-up
- Introduce save & restore features

- DONE: clean up game menu:
	- DONE: add 'any key to return to the game menu' after "THANKS FOR PLAYING"
	- DONE: add row dividers in game menu

- DONE: one-time setup function (game_update() ) that calculates static values for a game version
	- DONE: max_score
		- CANCEL: max_score; => game_static_dict (calc max_score in mk_def_pkl() & cache in static_dict)
		- IDEA: want to have as little code as possible in game update (now that we have 1 per game)
		- DONE: convert max_score to game_static_dict value
		- DONE: update gs.score call for max_score
		- DONE: clean up comments 
	- DONE: str_to_obj_dict
		- DONE: confirm that every obj has a name attribute (confirmed)
		- DONE: in start_up(), create str_to_obj_dict = dict => gs.core attrib
			- DONE: add str_to_obj_dict to gs.core attributes
			- DONE: setters & getters (manual since is dict)
			- DONE: add empty assignment to game_update for both games
			- DONE: create start_up routine that creates dict and assigns to gs.core attrib (both games)
			- DONE: test via print
	- DONE: elim getattr() and other strange obj lookups
		- DONE: fix dark_castle start_up
		- DONE: fix cup_of_tea start_up
		- CANCEL: elim getattr in cmd_exe() [still need getattr to convert string to method call]
		- CANCEL: elim getattr in validate() [still need getattr to convert string to method call]
		- DONE: create gs.core method to return bool based on whether string is in str_to_obj_dict
		- DONE: elim loop-based txt-to-obj conversion in interp() [2 cases]
		- DONE: comment clean-up

- DONE: move start_up() back to app_main; calls session_code() from game
	- IDEA: implement start_up_dict for each game and make start_up() part of engine (=> /app_main)
		- IDEA: engine start_up coppies game_files/game_pkl => working/active_pkl
		- IDEA: engine start_up calls game_files/session_code()
		- IDEA: engine start_up buffers game_static_dict['intro']
		- CANCLE: engine start_up buffers examine of gs.core.start_rm (create as gs.core attrib)
			- IDEA: just use gs.map.hero_rm.name
		- IDEA: session_file is attribute of of gs.core ; if gs.core.session_file == None then don't call
	- DONE: move start_up back to /app_main
		- DONE: make start_up pickle load dynamic based on game_name
		- DONE: call room description based on gs.map.hero_rm.name
		- DONE: create game_session_vars() in game start_up
		- DONE: create gs.core.has_session_vars attrib
		- DONE: programatically import session values assignment based on gs.core.session_file
		- DONE: call game_session_vars() from clessh start_up
		- DONE: cut-over change
		- DONE: redirect web_main() to call cleesh start_up()
		- DONE: testing
		- DONE: clean-up web_main(), start_up(), elim cup_of_tea/start_up
		- DONE: test
		- DONE: dark_castle/game_start_up()
		- DONE: rename start_up() => game_start_up() and update string 
		- DONE: testing

- DONE: implement game save & restore
	- DONE: add 'save' and 'restore' to static_gbl() 'pre_interp_word_lst'
	- DONE: add 'help_save' to help respones
	- DONE: create file_io() module in ~/app_main/
	- DONE: create <game_name>/saves folder and __init__.py for both games
	- DONE: create save_game(game_name) function in file_io
	- DONE: create restore_game(game_name) function in file_io()
	- DONE: import save_game and restore_game from file_io()
	- DONE: create 'save' response in web_main()
	- DONE: create 'restore' response in webmain()
	- DONE: test
	- DONE: create a standard confirm_choice() function in web_main()
		- IDEA: on != 'y', f"{user_input.capitalize()} aborted."
		- IDEA: returns confirm bool, user_output
	- DONE: call confirm_choice(warn_str) from main web_main() routine
	- DONE: clean-up web_main()

- DONE: Misc clean-up
	- DONE: comment on Q / Restart being sent to app_main (for score)
	- DONE: solve no-save-to-restore issue
		- IDEA: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
		- IDEA: for save & restore, move user_output generation to file_io()
	- DONE: fix spacing for save & restore options
	- DONE: press any key to continue on restart?
	- DONE: separate help category for move_commands (i.e. separate from one_word_commands)
		- DONE: create 'one_word_travel_lst' : ['north', 'south', 'east', 'west']
		- DONE: in static_gbl() , update one-word 'help' to include travel commands
		- DONE: in cmd_exe() , create help response for 'help travel'
		- DONE: test "help" and "help travel"
		- DONE: in interpreter() , combine 'one_travel_move_lst' as needed
		- DONE: test
		- DONE: in static_gbl(), remove directions from 'one_word_convert'
		- DONE: test 'help one_word_commands'
		- DONE: clean-up interpreter(), static_gbl()
	- DONE: debug error in validate() that hints that obj_name is not in pickle


*** already done ***
- in gs scope checks => is_cont(), is_mach(), is_creature() methods within classes
- for gs.mach_obj_lst(), eliminate 'getattr' and create method to check for being machine
- eliminate 'getattr' for containers in gs.scope_lst() too
- have default methods is_contain and is_mach for Invisible that returns False; 
	- overload to True for exception cases

*** unused code from score_class_def() ***
#    def get_max_score(self, gs):
#        max_score = 0
#        for verb in gs.io.get_dict('score_dict'):
#            for subj_key in gs.io.get_dict_val('score_dict', verb):
#                if gs.io.get_ddict_val('score_dict', verb, subj_key) > 0:
#                    max_score += gs.io.get_ddict_val('score_dict', verb, subj_key)
#        return max_score

#        output2 = (" out of " + str(self.get_max_score(gs)))

*** unused code in dark_castle/.../start_up() ***
#	for obj in master_obj_lst[1:]:
#		if obj.name == 'control_panel':
#			obj.mach_state = portcullis_code
#		if obj.name == 'entrance':
#			obj.examine(gs)

*** unused code from web_main ***
#	import_str = f"cleesh.games.{game_name}.game_file.start_up"
#	user_output = import_module(import_str).start_me_up()

*** unused code from web_main ***

#				cmd_conf_input = input('Save overwrites old save. Confirm? (Y / N): ')
#				if cmd_conf_input.lower() not in ['y', 'yes']:
#					user_output = "Save aborted."
#				else:


############################
### VERSION 3.87.0 START ###
############################

Start Date: Jun 10, 2024
End Date: Dec 11, 2024

Version 3.87.0 Goals:
- review all mod-mach ideas / TBD to data
- introduce standard versioning nomenclature
- review current mod-mach functioning
- review of Switch class
- improve machine modularization
- incorporate Warnings and Timers into mod-mach code
- address response limitations due to std machines
- mod-mach bug fixes
- update mod-mach doc

*** to do org ***
- DONE: std version nomenclature 
	- IDEA: start using std versioning format: x.y.z (build #) => api.features.bug-fix (internal)
		- REF: https://softwareengineering.stackexchange.com/questions/368643/should-we-assign-version-numbers-for-internal-releases
	- IDEA: Reversion cleesh and games with new starting numbers
	- DONE: cleesh reversion 
		- DONE: from '3.86 (6/9/2024)' to '3.8.0 (build 0001)'
	- DONE: dark_castle reversion 
		DONE: from '3.86 (6/9/2024)' to '3.1.0 (build 0001)'
	- DONE: cup_of_tea reversion 
		- DONE: from '0.15 (5/22/2024)' to '0.1.0 (build 0001)'
	- IDEA: since the game code has not changed since last release, there should be no build #
		- DONE: updated

- DONE: setup new MacBook Air for coding
	- DONE: install VS Code
	- DONE: install homebrew
	- DONE: install git
	- DONE: git clone dark_castle3 repo
	- DONE: git stage / commit / push

- DONE: read existing mod-mach doc
	- DONE: read and update 'Road to' section
	- DONE: read 'Components' section
	- DONE: read 'Example' section
	- DONE: read 'Warnings' section
	- DONE: read 'Timers' section

- DONE: new mac updates (build 0001)
	- DONE: fix root_path_str issue
		- DONE: define new root_path_str
		- DONE: update all path calls
		- DONE: test
		- DONE: install pretty table: "pip3 install prettytable"
		- DONE: re-test
		- DONE: clean-up web_main(), app_main(), file_io(), start_up(), both game_updates()
		- DONE: elim engine static_global entry for root_path_str - this never gets used
- DONE: game install routine
	- DONE: pass root_path_str from web_main() to all other modules:
		- DONE: web_main(), app_main(), file_io(), start_up()
		- DONE: test
		- DONE: clean-up web_main(), app_main(), file_io(), start_up()
		- CANCEL: incorporate game_name into obj save in game_update() modules (no need; file is game-specific)
	- DONE: auto-localization
		- LINK: https://stackoverflow.com/questions/21259070/struggling-to-append-a-relative-path-to-my-sys-path
		- DONE: got web_main() working with import os ability
		- DONE: game_update() for cup_of_tea
		- DONE: game_update() for dark_castle
		- DONE: clean up comments in web_main(), & both game_update()
	- DONE: document install dependencies somewhere: set root_path_str & install prettytable

- DONE: switch class (build 0002)
	- DONE: review existing switch class
	- DONE: make LeverSwitch a true MixIn
		- DONE: remove ViewOnly from LeverSwitch
		- DONE: create ViewOnlyLeverSwitch
		- DONE: update import and assignment in dark_castle
		- DONE: text & fix errors
		- DONE: update version build #

- DONE: refactor app_turn modules (mach code only) (build 0003) [Jun 25, 2024]
	- DONE: refactor pre_action()
	- DONE: refactor post_action()
		- DONE: initial clean-up
		- DONE: reverse result_name (verb) and obj_name (noun) in score_disp() call
		- DONE: test
		- DONE: clean-up comments
	- DONE: refactor auto_action()
	- DONE: update version build #

- INPROC: review existing mach class (build 0004) [Jun 28, 2024]
	- DONE: trig_check()
	- DONE: refactor run_mach()
		- DONE: update code to eliminate dual index creation
		- DONE: test
		- DONE: exit and re-test
		- NOTE: was worried that returning a method arguement would cause a circular ref but apparently not
		- DONE: comment clean-up
	- DONE: need a deep dive on trig_check() wildcard routine
		- DONE: test existing wildcard routine via hedgehog_distracted_mach => does not appear to work
		- DONE: troubleshoot hedgehog_distracted_mach
			- DONE: confirm '*' issue by replacing w/ shiny_sword => works; '*' is the issue
			- DONE: fix / refactor hedgehog_distracted_mach / trig_check() wildcard routine
			- DECISION: wildcards will only be valid for nouns
			- DONE: clean up comments
	- DONE: update version build #

- DONE: cond review (build 0005) [Jul 17, 2024]
	- DONE: review and categorize existing conditions
	- DONE: refactor / rename simple conditions
		- DONE: PassThruCond => TrueCond
			- DONE: cup_of_tea
			- DONE: dark_castle
		- DONE: WornCond
			- DONE: refactor cond
			- DONE: update dark_castle
				- DONE: troubleshoot error on read scroll with no crown (indent error? try w/out creature)
				- FINDING: I think the issue was lack of a setter to over-write the 'temp_burt' placeholder
				- DONE: clean up comments
		- DONE: RoomCond & InRoomCond
			- DONE: cond usage eval - do we really need both?
				- FINDING: no - InRoomCond is better written but was only used for test_frog
				- FINDING: RoomCond and InRoomCond duplicate functionality
				- DECISION: re-purpose InRoomCond to inherit from TrueCond and match std WornCond format
			- DONE: refactor cond
			- DONE: update dark_castle
			- DONE: clean up comments
			- DONE: creature_obj => obj (InRoomCond could be used for any obj)
			- DONE: InRoomCond => ObjInRmCond ??
			- DONE: test
		- DONE: CreatureItemCond => ItemInHandCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
		- DONE: WeaponInHandCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
		- DONE: InWorldCond => ObjInWorldCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
			- DONE: sort out InWorldCond dependencies of InWorldStateCond
			- DONE: clean up comments
		- DONE: StateCond => MachStateCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
			- DONE: sort out dependant Cond classes
			- DONE: test & clean up comments
		- DONE: TimerActiveCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
		- DONE: SwitchStateCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
			- DONE: sort out dependant Cond classes
			- DONE: test & clean up comments
		- DONE: LeverArrayCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
	- DONE: sort out combo cond
		- IDEA: perhaps cond_lst is a list-of-lists; 
			- IDEA: i.e. each cond is in a list; if len(cond) > 0 then 'and' them?
			- IDEA: so this happens at the Machine class / run_mach level
			- IDEA: this way, there is no class of combo_and_cond... which would just add complexity
			- IDEA: cond_combo_lst = [cond_1, 'and', cond_2] or [cond_1, 'or', cond_2] (etc, left to right)
		- DONE: update combo cond 1-by-1
			- DONE: IsWeaponAndStateCond
				- DONE: update run_mach() for element is_list case
				- DONE: loop through list
				- DONE: evaluate combo based on list[0] logic operator
				- CANCEL: create individual conditions for IsWeaponAndStateCond
				- CANCEL: create combo list obj for IsWeaponAndStateCond
				- CANCEL: implement IsWeaponAndStateCond case in dark_castle
				- FINDING: embarassing but it turns out I don't even need IsWeaponAndStateCond
				- DONE: update moat_mach with use of MachStateCond
				- DONE: elim IsWeaponAndStateCond
			- DONE: redo SwitchStateCond w/ enumerate and false check on each switch in list
			- DONE: elim InWorldStateCond
				- DONE: rewrite panel dispenser cond to no longer need combo condition
				- DONE: elimn combo condition
				- DONE: clean up comments
			- DONE: investigte need for StateItemInRoomCond
				- DONE: refeacto pre_action() with update for 'pre_act_timer' case
				- DONE: test
				- DONE: clean-up comments
				- DONE: do I really need to check mach_state in hedgehog_done_eating_mach ??
					- IDEA: is this just to avoid running every move?? [need a state machine!]
					- IDEA: if so, should check mach_state first, followed by 2x obj_in_rm cases
					- DONE: update hh_descript_update_mach mach_state to False
					- DONE: create new ObjOnRmFlrCond class
					- DONE: create new obj_is_on_floor() method in Room class
					- DONE: create new simple conditions based on MachStateCond and ObjOnRmFlrCond classes
					- DONE: test
					- DONE: clean up comments
					- DONE: troubleshooting of new hh_descript_mach()
					- DONE: fix attribute methods in Room class (why ref self._floor_lst ?)
			- DONE: sort out dispense_panel_mach (broach conds => panel conds)
			- DONE: investigate need for NotTimerAndItemCond
				- DONE: eliminate NotTimerAndItemCond
	- DONE: if no current need for complex cond, archive code at bottom of method via comments plug-in
	- DONE: update cond & mach to assume "pass" result if cond not listed
		- EXAMPLE: in dispense_panel_mach , should not need broach_dispensed_cond
		- NOTE: need to address this in run_mach() cond_check() => False if no cond == True
		- NOTE: proceed with caution - game currently errors if not all conditions provided
		- DONE: update machs so that true_cond => pass_cond is always last
	- DONE: clean up Cond class module
	- DONE: summary of deleted condition classes:
# PassThruCond : 		parent class :	 	True ==> DONE (legacy parent class)
# RoomCond :			PassThruCond :		match hero_rm
# CreatureItemCond : 	PassThruCond :	 	match on creature holding item
# StateCond : 			PassThruCond :  	match mach_state
# IsWeaponAndStateCond : MachStateCond :	(match mach_state) && (match weapon in hero hand) > [combo]
# InWorldStateCond :	ObjInWorldCond :	(not mach_state) and (match chk_obj_exist) [combo]
# StateItemInRoomCond :	PassThruCond :		(match item_obj in hero_rm.floor_lst) && (match mach_state) > [combo]
# NotTimerAndItemCond :	PassThruCond :	 	(item_obj in hero_rm.floor_lst) && (not timer_obj.active) > [combo]
	- DONE: update version build #


- DONE: update Mach class (build 0006) [Jul 23, 2024]
	- DONE: add alert_anchor and is_active attribs to MachMixIn
	- DONE: setters & getters
	- DONE: add attribs to all 4 resultant classes (e.g. InvisMach)
	- DONE: update Room.get_mach_lst() to ref 'active'
	- DONE: update cup_of_tea game machs
	- DONE: test
	- DONE: update dark_castle3 game machs
	- DONE: test
		- DONE: troubleshooting issue #1
			- FINDING: timers and warnings are effectively of class Mach (even though inedependent for now)
			- FINDING: this means that they will also be tested for is_active by Room.get_mach_lst()
			- FINDING: but Mach.is_active and Timer.active mean two very different things:
			- FINDING: Mach.is_active refers to whether or not the game should consider the mach to exist
			- FINDING: Timer.active refers to whether or not the timer is currently running
			- FINDING: this nomenclature is innately confusing
			- CANCEL: choose better nomenclature (e.g. perhaps Timer.active => Timer.is_running)
				- DECISION: too many timer.active references
			- DONE: mach.is_active => mach.is_enabled
				- DONE: mach_class
				- DONE: room_class
			- DONE: add is_enabled attribute to Warning
				- DONE: add to attributes
				- DONE: add setters & getters
				- DONE: add in game_update
			- DONE: add is_enabled attribute to Timer
				- DONE: add to attributes
				- DONE: add setters & getters
				- DONE: add in game_update
		- DONE: troubleshooting issues #2
			- FINDING: now I am running into issues with Switches - since they have identity is_mach
			- FINDING: this is true to enable auto-switch restes in auto_action()
			- FINDING: however, since (today) all switches are physical, is_enabled attrib seems wrong
			- FINDING: attempted to use get_mach_lst() logic for enabled machs or switches in Room
			- FINDING: but this is throwing errors (appears that Room is being added to mach_lst)
			- DONE: figure out why Room is being added to mach_lst; fix or create separate get_switch_lst()
				- FINDING: was calling obj.is_switch [i.e. and attrib] instead of ob.is_switch() [a method]
				- FINDING: also, needed to put switch option first in 'or' logic - to avoid is_enabled() eval
	- DONE: clean up comments in mach_class(), room_class(), post_action()

- DONE: result review + simple cases (build 0007) [Aug 7, 2024]
	- DONE: review and categorize existing results
	- DONE: initial result decision-making
		- DONE: decide if I should attempt to use super() on inherited results
			- DECISION: yes, attempt to use super()
		- DONE: decide if results should be symetric... can they be operated by non-players?
			- DECISION: no, don't attempt symetric - non-hero creatures receiving results is rare and tricky
		- DONE: even if machs only opperated by hero, what if opp from another rm? If so, buff only if in rm?
			- DECISION: yes, need to be room aware for result buffering
		- DONE: should BufferResult have a is_mach_state_set attrib?
			- DECISION: yes, BaseResult should do room-aware buffer + option to set mach_state
	- DONE: test git branching for new feature developemnt
		- LINK: https://www.split.io/blog/understanding-the-feature-branching-strategy-in-git/
		- LINK: https://www.linkedin.com/pulse/using-git-implement-new-featurechange-without-affecting-michel-noel/
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch branching_test' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout branching_test' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm that focus in on branching_test
		- DONE: Commit via VS Code to commit changes locally
		- DONE: Push via VS Code to push branch changes to origin (GitHub)
		- DONE: 2nd commit & push test
		- DONE: 3rd commit & push test
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "5th update"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge branching_test -m "branch test merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: 'git branch -d branching_test' to clean-up local branch
		- DONE: 'git push origin --delete branching_test' to clean up origin
	- DONE: BufferOnlyResult => BaseResult (buffer w/ alert_anchor) + set mach_state option (set vs. reset)
		- DONE: create new BaseResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch BaseResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout BaseResult_feature' to switch focus to branching_test branch
			- CANCEL: 'git push' to push new branch to origin
				- FINDING: failed: "fatal: The current branch BaseResult_feature has no upstream branch."
				- FINDING: but Push via VS Code button worked fine
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "5th update"
			- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: create BaseResult in results_class()
			- DONE: create BaseResult based on BufferOnlyResult
			- DONE: add alert_anchor to result_exe() call
			- DONE: test for hero in same room as event before buffering
			- DECISION: no descript_key attrib - keep simple - just buffer based on resutl_name as key
			- DONE: add attribs for mach_state
				- IDEA: bool attrib => is_mach_state_set
				- IDEA: val attrib => mach_state_val
				- DONE: add attribs
				- DONE: create setters & getters
			- FINDING: result_exe() never uses mach_state() [why whould it?]
				- CANCEL: elim mach_state attrib in result_exe() call
				- FINDING: actually, do need it - to pass back mach_state when not set
		- DONE: convert BufferOnlyResult to BaseResult
			- DONE: add BaseResult to import in game_update() for both games
			- DONE: dark_castle/game_files/game_update()
				- DONE: updated all BufferOnlyResult obj => BaseResult
			- DONE: test
		- DONE: git branch merge with master
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge BaseResult_feature -m "branch BaseResult_feature merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d BaseResult_feature' to clean-up local branch
		- DONE: 'git push origin --delete BaseResult_feature' to clean up origin
		- DONE: post-branch-delete run test
	- DONE: BufferAndEndResult => inherit from BaseResult & use super()
		- DONE: create new BufferAndEndResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch BufferAndEndResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout BufferAndEndResult_feature' to switch focus to branching_test branch
			- DONE: but Push via VS Code button
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DON: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc update"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub
		- DONE: add BufferAndEndResult result names to run_mach call for result_exe()
			- DONE: update BufferAndEndResult to inherit from BaseResult
			- DONE: update BufferAndEndResult attrib list and order
			- DONE: update cup_of_tea game_update() to use new BufferAndEndResult
				- DONE: update result obj attribs
				- DONE: add cup_of_tea BufferAndEndResult result to run_mach result_exe list
				- DONE: resolve error (need to explicityl return after super() )
			- DONE: update dark_castle game_update to use new BufferAndEndResult
				- DONE: update result obj attribs
				- DONE: add dark_castle BufferAndEndResult result to run_mach result_exe list
				- DONE: test
			- DONE: result class update: BufferAndEndResult => EndResult
				- DONE: update in result_class()
				- DONE: update in cup_of_tea
				- DONE: update in dark_castl
			- DUNE: comment clean-up: result_class, cup_of_tea//game_update, dark_castle//game_update
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge BufferAndEndResult_feature -m "branch BufferAndEndResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d BufferAndEndResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete BufferAndEndResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: ChgCreatureDescAndStateResult => ChgDescriptResult
		- DONE: create new ChgDescriptResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch ChgDescriptResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout ChgDescriptResult_feature' to switch focus to branching_test branch
			- DONE: Push via VS Code button
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc update"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub
		- DONE: refactor ChgCreatureDescAndStateResult => ChgDescriptResult
			- DONE: result class updates
				- DONE: copy ChgCreatureDescAndStateResult; change parent to BaseResult
				- DONE: change creature_obj => obj (class should change descript_key for any obj)
				- DONE: use super() call BaseResult buffer and mach_state change
				- DONE: update result_exe() attribs
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- DONE: add result obj to mach_run() exception list
				- DONE: update post-attrib assignment if needed
				- DONE: comment out old result class
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class()
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge ChgDescriptResult_feature -m "branch ChgDescriptResult merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d ChgDescriptResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete ChgDescriptResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: BufferAndGiveResult => GiveItemResult
		- DONE: create new BufferAndGiveResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch BufferAndGiveResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout BufferAndGiveResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc update"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub
		- DONE: refactor BufferAndGiveResult => GiveItemResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update setters and getters
				- DONE: <specific changes>: introduce tgt_creature attrib
				- DONE: use super() call BaseResult buffer and mach_state change
				- DONE: update result_exe() attribs
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- DONE: set mach_state appropriately
				- DONE: add result obj to mach_run() exception list
				- DONE: update post-attrib assignment if needed
				- DONE: comment out old result class and remove from import (in nnew name)
			- DONE: test & clean-up
				- DONE: test
					- FINDING: appears that mach_state is not getting set in BaseResult (suspected this)
					- FINDING: mach_state is getting set in BaseResult - but set is not sticking => mach_class
					- FINDING: solved it! Neet to return super().result_exe() !!!
				- DONE: extend lesson-learned to other chile classes of BaseResult
					- DONE: ChgDescriptResult
					- DONE: EndResult
				- DONE: clean-up game_update(), result_class(), mach_class()
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge BufferAndGiveResult_feature -m "branch BufferAndGiveResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d BufferAndGiveResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete BufferAndGiveResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: PutItemInHandResult => TakeItemResult
		- DONE: create new PutItemInHandResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch PutItemInHandResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout PutItemInHandResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is  now ahead of master
		- DONE: refactor PutItemInHandResult => TakeItemResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update attribs and setters and getters
				- DONE: update result_exe() attribs
				- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- DONE: specific class changes - code from take() method:
					- DONE: gs.map.hero_rm.remove_item(self, gs) => get_obj_room(creature_obj)
					- DONE: creature_obj.put_in_hand(self, gs)				
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- DONE: update Result obj name if appropriate => goblin_takes_axe_result
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- DONE: set mach_state appropriately
				- DONE: update post-attrib assignment if needed
				- DONE: add result name to mach_run() exception list
				- DONE: comment out old result class and remove from import (in new name)
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class(), mach_class() [??]
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge PutItemInHandResult_feature -m "branch PutItemInHandResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d PutItemInHandResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete PutItemInHandResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: AddObjToRoomResult => DispenseObjResult Update
		- DONE: create new AddObjToRoomResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch AddObjToRoomResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout AddObjToRoomResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master
		- DONE: refactor AddObjToRoomResult => DispenseObjResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update attribs and setters and getters
				- DONE: update result_exe() attribs
				- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- DONE: specific class changes: room_item => dispense_obj; include room_obj as class attrib
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- N/A: update Result obj name if appropriate
				- N/A: update game_update result obj classes, attribs, and post-assignment updates
				- N/A: set mach_state appropriately
				- N/A: update post-attrib assignment if needed
				- N/A: add result name to mach_run() exception list
				- DONE: comment out old result class and remove from import (in new name)
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class(), mach_class() [??]
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge AddObjToRoomResult_feature -m "branch AddObjToRoomResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d AddObjToRoomResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete AddObjToRoomResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test


- DONE: combo Result cases (build 0008) [8/14/2024]
	- DONE: update Mach class to accept a list of results and run all results in the list
	- DONE: sort out AddObjChgDescriptResult and AddObjToRoomAndDescriptResult combos
		- DONE: create new git branch for AddObjChgDescriptResult_feature
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch AddObjChgDescriptResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout AddObjChgDescriptResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master
		- DONE: AddObjChgDescriptResult => ChgDescriptResult + DispenseObjResult
			- DONE: create ChgDescriptResult obj game_update
			- DONE: create DispenseObjResult obj game_update
			- DONE: comment out old AddObjChgDescriptResult obj in game_update
			- DONE: set mach_state appropriately
			- DONE: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: test
			- DONE: comment out old result class and remove from import (in new name)
			- DONE: clean up  comments in result_class, game_update
		- DONE: AddObjToRoomAndDescriptResult => ChgDescriptResult + DispenseObjResult
			- DONE: create ChgDescriptResult obj game_update
			- DONE: create DispenseObjResult obj game_update
			- DONE: comment out old AddObjToRoomAndDescriptResult obj in game_update
			- DONE: set mach_state appropriately
			- DONE: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: test
			- DONE: comment out old result class and remove from import (in new name)
			- DONE: clean up  comments in result_class(), game_update(), game_static_gbl()
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge AddObjChgDescriptResult_feature -m "branch AddObjChgDescriptResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d AddObjChgDescriptResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete AddObjChgDescriptResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: sort out TimerAndCreatureItemResult combo result
		- DONE: git branch for TimerAndCreatureItemResult_feature
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch TimerAndCreatureItemResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout TimerAndCreatureItemResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master
		- DONE: refactor StartTimerResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update attribs and setters and getters
				- DONE: update result_exe() attribs
				- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- N/A: specific class changes: <list here>
			- DONE: update game files
				- N/A: add new result class to game_update imports (same name)
				- DONE: update Result obj name if appropriate
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- N/A: set mach_state appropriately
				- N/A: update post-attrib assignment if needed
				- DONE: add result name to mach_run() exception list			
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class(), mach_class() [??]
		- DONE: create RemoveObjResult
			- DONE: base off of StartTimerResult
			- DONE: key attribute is obj
			- DONE: include setter in case obj is mach or creature
			- DONE: find obj room using Map method and then remove obj using Room remove method
		- DONE: TimerAndCreatureItemResult => StartTimerResult + RemoveObjResult
			- DONE: add new RemoveObjResult class to game_update imports
			- DONE: create result obj based on RemoveObjResult class
			- DONE: add names of new result objs to run_mach()
			- DONE: comment out old result class
			- DONE: comment out old combo result class and remove from import
			- DONE: replace old combo result obj with list of primitive result obj
			- DONE: test [first try!]
			- DONE: clean up clean-up game_update(), result_class(), mach_class() [??]
		- DONE: merge git branch for TimerAndCreatureItemResult
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge TimerAndCreatureItemResult_feature -m "branch <FEATURE_NAME> merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d TimerAndCreatureItemResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete TimerAndCreatureItemResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: update version and complete build

- DONE: final result class build for refactor cases including travel (build 0009 [8/22/2024])
	- DONE: create new git branch for result_refactor_feature
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch result_refactor_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout result_refactor_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master
	- DONE: refactor AttackBurtResult => AttackHeroResult
		- DONE: result class updates
			- DONE: copy existing class; change parent to BaseResult and update class name <AttackHeroResult>
			- DONE: update attribs and setters and getters
			- DONE: update result_exe() attribs
			- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
			- DONE: specific class changes: <make hand_obj an explicit attrib>
		- DONE: update game files
			- DONE: add new result class to game_update imports
			- N/A: update Result obj name if appropriate
			- DONE: update game_update result obj classes, attribs, and post-assignment updates
			- N/A: set mach_state appropriately
			- N/A: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: comment out old result class and remove from import (in new name)
		- DONE: test & clean-up
			- DONE: test
			- DONE: clean-up game_update(), result_class(), mach_class() [??]
	- DONE: refactor DoorToggleResult => OpenableToggleResult
		- DONE: result class updates
			- DONE: copy existing class; change parent to BaseResult and update class name
			- DONE: update attribs and setters and getters
			- DONE: update result_exe() attribs
			- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
			- DONE: specific class changes: <move toggle() method into door class?; return display str?>
				- DONE: create door.toggle() method that returns is_open [True or False]
				- DONE: DoorToggleResult sets and buffs display str based on door.toggle() return
		- DONE: update game files
			- DONE: add new result class to game_update imports
			- DONE: update Result obj name if appropriate
			- DONE: update game_update result obj classes, attribs, and post-assignment updates
			- N/A: set mach_state appropriately
			- N/A: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: comment out old result class and remove from import (in new name)
		- DONE: test & clean-up
			- DONE: test
			- DONE: clean-up game_update(), result_class(), mach_class() [??]
	- DONE: refactor TravelResult => CreatureTravelResult
		- DONE: result class updates
			- DONE: copy existing class; change parent to BaseResult and update class name
			- DONE: update attribs and setters and getters
			- DONE: update result_exe() attribs
			- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
			- N/A: specific class changes: <list here>
		- DONE: update game files
			- DONE: add new result class to game_update imports
			- N/A: update Result obj name if appropriate
			- N/A: update game_update result obj classes, attribs, and post-assignment updates
			- N/A: set mach_state appropriately
			- N/A: update post-attrib assignment if needed
			- N/A: add result name to mach_run() exception list
			- DONE: comment out old result class and remove from import (in new name)
		- DONE: test & clean-up
			- N/A: test
			- DONE: clean-up game_update(), result_class(), mach_class() [??]
	- DONE: merge result_refactor_feature git branch
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge result_refactor_feature -m "branch result_refator_feature merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d result_refactor_feature' to clean-up local branch
		- DONE: 'git push origin --delete result_refactor_feature' to clean up origin
		- DONE: confirm origin is cleaned up
		- DONE: post-branch-delete run test
	- DONE: update cleesh engine version build
		- DONE: web_main.py
		- DONE: static_gbl.py

- DONE: final result class updates (build 0010 [8/25/2024])
	- DONE: create new result_class_feature git branch
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch result_class_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout result_class_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master
	- DONE: refactor result class
		- DONE: update call from run_mach(); self.mach_state => self.alert_anchor
			- DONE: comment out elif
			- DONE: test
			- DONE: clean-up comments
		- DONE: solve buffer issues:
			- DONE: need to sort out variable buff (e.g. DoorToggleResult)
				- DONE: pass buff_key as attrib to result_exe() in BaseResult
				- DONE: update BaseResult buff_s(buff_key)
				- DONE: update result_exe() return call in all child classes
				- DONE: update result_exe() call in mach_class() to pass result.name as buff_key
				- DONE: test
				- DONE: update OpenableToggleResult to modify buff_key
				- DONE: update game_static_gbl to provide two different buff_key entries
				- DONE: test
				- DONE: clean up comments in result_class(), mach_class(), game_static_gbl()
			- DONE: How to buffer first rather than last? (e.g. AttackHeroResult)
				- DONE: gs.io.buff_s(self.name + "_pre-buff")
		- DONE: clean-up all the result_class() module comments
	- DONE: git branch merge with master
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge result_class_feature -m "branch result_class_feature merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d result_class_feature' to clean-up local branch
		- DONE: 'git push origin --delete result_class_feature' to clean up origin
		- DONE: confirm origin is cleaned up
		- DONE: post-branch-delete run test
	- DONE: update cleesh engine version build
		- DONE: web_main.py
		- DONE: static_gbl.py

- DONE: mach inheritance refactor (build 0011 [])
	- DONE: for Mach class, create an 'is_enabled' attribute
	- DONE: general Mach class review
		- DONE: analyze dark_castle machs
			- FINDING: auto could be parent of cmd which could be parent of switch
		- DONE: analyze dark_castle warnings 
			- FINDING: Warning could be 'proto' class for Mach
			- FINDING: Warning run_mach() needs re-factor
			- FINDING: warning_count has some similarities to mach_state
			- FINDING: warn_max is similar to timer_max
		- DONE: analyze timers
			- CANCEL: Timer needs a reset_timer() method
				- FINDING: exists
			- FINDING: existing Timer run_mach() auto-resets at count == max_count... is this desired?
			- FINDING: Timer is harder to incorporate into parent-child relationship with Mach and Warning
			- FINDING: timer_count has some similarities to mach_state
			- FINDING: active could likely be a method (not an attribute)
			- FINDING: timer_max is similar to warn_max
			- FINDING: timer_done could be replaced by run_count ... which might be useful elsewhere too...
				- IDEA: but this is only useful if we pass run_count to cond_check()
				- IDEA: if timer_count == mach_state, there is no way to pass info about multiple timer runs
				- IDEA: but how far ahead of real use-case do I want to get? Can add as a new feature when needed
			- FINDING: feels like message type (constant vs. variable) could be inferred?
				- IDEA: if message_0 exists => constant message
		- IDEA: inheritance big picture
			IDEA: MachProtoMixIn => (Timer, Warning, MachCmdMixIn), MachCmdMixIn => MachSwitchMixIn
		- DONE: summarize attribs and methods for each type; propose unifying Proto class
			- IDEA: MachProtoMixIn:
				- STD: mach_state, trigger_type, trig_vals_lst, alert_anchor, is_enabled
				- METH: run_mach(), trigger_check()
			- IDEA: Timer(MachProtoMixIn)
				- From Proto:
					- ATTRIB: name, mach_state, trigger_type, alert_anchor, is_enabled
					- MAP: timer_count => mach_state
					- METH: run_mach()
				- Proto Unused:
					- ATTRIB: trig_vals_lst
					- METH: trigger_check()
				- Timer Unique: 
					- ATTRIB: name, active, timer_max, message_type, timer_done
					- METH: over-load run_mach()
			- IDEA: Warning(MachProtoMixIn)
				- From Proto:
					- ATTRIB: name, mach_state, trigger_type, trig_vals_lst, is_enabled
					- MAP: warn_count => mach_state
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: alert_anchor
				- Warning Unique: 
					- ATTRIB: name, warn_max
					- METH: over-load run_mach()
			- IDEA: Mach_auto(MachProtoMixIn)
				- From Proto:
					- ATTRIB: mach_state, trigger_type, alert_anchor, is_enabled
					- MAP: None
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: trig_vals_lst
				- Mach_auto Unique: 
					- ATTRIB: cond_lst, result_lst
					- METH: over-load run_mach()
			- IDEA: Mach_cmd(MachProtoMixIn)
				- From Proto:
					- ATTRIB: mach_state, trigger_type, trig_vals_lst, alert_anchor, is_enabled
					- MAP: None
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: None
				- Mach_cmd Unique: 
					- ATTRIB: cond_lst, result_lst
					- METH: over-load run_mach()
			- IDEA: Mach_switch(MachCmdMixIn)
				- From Proto:
					- ATTRIB: mach_state, trigger_type, trig_vals_lst, cond_lst, result_lst, 
						alert_anchor, is_enabled
					- MAP: None
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: None
				- Mach_cmd Unique: 
					- ATTRIB: trig_switch, cond_switch_lst
					- METH: None

- DONE: plan out which mach ideas to act on and which order to perform them in (inheritance first)
	- DONE: re-read all remaining mach ideas and incorporate as appropriate
		- IDEA: org mach to-dos
		- IDEA: Sort out parrent-child inheritance
		- IDEA: triggers
		- IDEA: Cases where I want a modular machine to run despite an error standard
		- IDEA: state machine for hedgehog
		- IDEA: event bus for goblin dies => dispense panel	
		- IDEA: mod-mach bug fixes
		- IDEA: debug ideas:
		- IDEA: in mk_def_pkl(), sort out more elegant assignment process for self referenced obj
		- IDEA: update modular machine doc!

- DONE: Sort out parrent-child inheritance
	- DONE: create new mach_inherit_feature git branch
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch mach_inherit_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout mach_inherit_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master
	- DONE: create ProtoMachMixIn class
		- DONE: attribs = mach_state, trig_type, alert_anchor, is_enabled
			- IDEA: 'trigger_type' => 'trig_type' ??
			- IDEA: hold off on trig_vals_lst for now
		- DONE: methods = run_mach()
			- IDEA hold off on trigger_check() => trig_chk() for now
	- DONE: create TimerX class (inherits from ProtoMachMixIn + Invisible)
		- IDEAS: TimerX class
			- IDEA: existing Timer run_mach() auto-resets at count == max_count... is this desired?
			- IDEA: Timer is harder to incorporate into parent-child relationship with Mach and Warning
			- FINDING: timer_count => mach_state
			- FINDING: active could likely be a method (not an attribute)
				- IDEA: Do I want timers to be stoppable? [w/ stop() method]. If so, need 'active' attirb
			- FINDING: timer_max is similar to warn_max
			- FINDING: timer_done could be replaced by run_count ... which might be useful elsewhere too...
				- IDEA: but this is only useful if we pass run_count to cond_check()
				- IDEA: if timer_count == mach_state, there is no way to pass info about multiple timer runs
				- IDEA: but how far ahead of real use-case do I want to get? Can add as a new feature when needed
			- FINDING: feels like message type (constant vs. variable) could be inferred?
				- IDEA: if message_0 exists => constant message
		- DONE: create TimerX class
			- DONE: class + setters & getters
			- DONE: update chk_str_exist() in IO class to check game_static_gbl
			- DONE: refactor mach_run() method
				- DONE: elim "Beep!" default
				- DONE: elim message_type attrib
				- DONE: base refactor
				- DONE: create set_timer(num) method
				- DONE: create stop() method
			- IDEA: timer 'ding'
				- IDEA: basically, in auto_act() , when the timer is done counting to timer_max, it should 'ding'
				- IDEA: it should stay in 'ding' state for 1 turn so that any mach listening for ding can hear it
				- IDEA: then, in auto_act, at top of timer mach_run, if 'ding' == True; reset and turn 'ding' off
				- IDEA: tricky part is that would be nice to start timer and react to ding both in auto_act
				- IDEA: maybe new 'auto_act_timer_trig' mach trigger that always goes after auto_act ???
			- DONE: sort out 'ding' idea
				- DONE: create is_dinging()
				- DONE: at start of run_mach(), if self.is_dinging(), self.reset and then return
				- DONE: refactor auto_action() and update to enable is_enabled()
				- DONE: enable trig_type = 'pre_act_timer' in auto_action()
				- DONE: create timer.is_active() method (to be used by TimerActiveCond)
			- DONE: update dark_castle timers
				- DONE: first test / doc exact timing of existing Timer obj
				- DONE: update class and attribs and pre_act_timer mach
				- DONE: update TimerActiveCond: active => is_active
				- DONE: test
					- FINDING: Description updates are foobarred
					- FINDING: game starting with hedgehog_eats_timer evaluating to is_active == True
					- DONE: duplicate name for is_active attrib and method causing issues; elim method
				- DONE: try moving pre_act_timer to auto_act_timer
		- DONE: clean-up
			- DONE: comment out old Timer class
			- DONE: update TimerX => Timer
			- DONE: clean up auto_act(), game_update(), pre_act(), cond_class(), mach_class() 
		- DONE: update timer doc
	- DONE: TrigMixIn
		- IDEA: TrigMixIn idea
			- IDEA: inherited by both Warning and CmdMachMixIn
			- IDEA: contains just trig_vals_lst attrib and trigger_check() method
			- IDEA: multiple MixIn sources seems complicated but appears to be best approach
		- DONE: create TrigMixIn class with setters & getters and methods
		- DONE: eliminate 'timer' option from trig_check()
	- DONE: create WarningX class 
		- DONE: create WarningX class (inherits from ProtoMachMixIn + TrigMixIn + Invisible
		- DONE: setters & getters
		- DONE: update mach_run() to use mach-state
		- DONE: refactor mach_run()
			- DONE: custom hero name (vs. "Burt")
			- DONE: elim str-creation variables
			- DONE: cmd_override as default
			- DONE: try / except w/ default for all 3 cases (0, < max, == max) => freedom on last command
			- CANCEL: consider warning reset options
				- DECISION: if resets end up being needed I can add them
				- FINDING: the main goal of Warnings is just to *avoid* a consequence on the first few incidents
		- DONE: update each existing warning
			- DONE: import WarningX
			- DONE: entrance_south_warn 
				- DONE: update attribs
				- DONE: post-assign alert_anchor
				- DONE: test
			- DONE: attack_hedgehog_warning
				- DONE: update attribs
				- DONE: post-assign alert_anchor
				- DONE: test
			- DONE: eat_biscuits_warning
				- DONE: update attribs
				- N/A: post-assign alert_anchor
				- DONE: test
		- DONE: final Warning class updates
			- DONE: comment out old Warning class and swap WarningX => Warning
			- DONE: in mach_class() , WarningX => Warning
			- DONE: in game_update() , WarningX => Warning , elim WarningX import
			- DONE: final test
		- DONE: clean up mach_class(), game_static_gbl(), game_update()
		- DONE: for trigger_type == 'pre_act_cmd' , check for warning.is_enabled in pre_action()
		- DONE: in run_mach(), set is_enabled = False after mach_state == warn_max
		- DONE: update warning doc
	- DONE: create AutoMachMixIn (inherits from ProtoMachMixIn but adds cond_lst & result_lst)
		- DONE: create AutoMachMixIn class w/ setters & getters
		- DONE: update run_mach()
		- DONE: refactor run_mach ()
		- DONE: creaate InvisAutoMach
		- DONE: migrate existing AutoMachs
			- DONE: import new class
			- DONE: dispense_panel_mach
				- DONE: migrate mach obj / attribs
				- DONE: test
			- DONE: re_arm_goblin_mach
				- DONE: migrate mach obj / attribs
				- DONE: test
		- CANCEL: comment out old class and remove from imports
		- DONE: clean up mach_class(), game_update()
	- DONE: can I combine CmdMachMixIn and SwitchMachMixIn into TrigMachMixIn ?
		- DONE: investigate elim of switch_cond_lst as attrib ( vs. regular conditions )
			- FINDING: possible
		- DONE: can trig_switch + trig_vals_lst be combined for case = 'switch' ?
			- FINDING: will complicated trig_vals_switch usage in check_cond() but is possible
	- DONE: ceate TrigMachMixIn (inherits from AutoMachMixIn + TrigMixIn
		- DONE: create MixIn class
		- DONE: create InvisTrigMach class
		- DONE: import InvisTrigMach
		- DONE: migrate existing InvisMach cmd obj
			- DONE: hedgehog_guard_mach
				- DONE: test (trig_vals_lst == [timer_cond]... due to attrib order???)
				- FINDING: I think maybe I just forgot to run the game_update after swapping attrib order
			- DONE: hedgehog_distracted_mach
				- DONE: test
			- DONE: goblin_attack_mach
				- DONE: test
			- DONE: entrance_moat_mach
				- DONE: test
			- DONE: hedgehog_eats_mach
				- DONE: update post_action()
				- DONE: test
		- DONE: migrate existing "ItemMach" obj to ItemTrigMach
			- DONE: create ItemTrigMach class
			- DONE: import ItemTrigMach class
			- DONE: migrate existing ItemMach obj
		- DONE: migrate "timer" mach obj
			- DECISION: InvisTrigMach => InvisSwitchMach
				- IDEA: timer_obj.is_dinging() is really a trigger and should be treated as such
				- IDEA: also, we want the freedom to match on NOT is_dinging()
				- DECISION: do need a 'switch' variant of MachMixIn after all => un-natural to pack trig_vals_lst
			- DONE: update auto_action:
				- DONE: for trigger_type == 'auto_act_timer' and mach_obj.is_enabled == True:
					- DONE: from mach_obj.trig_vals_lst, unpack timer_obj (trig_vals_lst[0])
					- DONE: call timer_obj.trig_check() w/ case = 'timer' ; word_lst = [timer_obj]
			- DONE: update trig_check()
				- DONE: for case = 'timer', trig_key_lst = [timer_obj.is_dinging()]
			- DONE: create SwitchMachMixIn class (inherit from TrigMachMixIn = trig_switch attrib)
			- DONE: create InvisSwitchMach class (inherit from SwitchMachMixIn + Invisible)
			- DONE: import InvisSwitchMach
			- DONE: update auto_action() : word_lst = [switch.is_dinging()]
			- DONE: update trig_check() : elim loc_trig_vals_lst ; trig_vals_lst => [True] or [False]
			- DONE: migrate existing auto_act_timer => InvisTrigMach
				- CANCEL: trig_vals_lst = [timer_obj, <is_dinging_bool>]
				- DONE: solve attrib count error
			- DONE: test
			- DONE: document format for trig_vals_lst in comments ( auto_action() )
	- DONE: migrate existing "switch" mach obj
		- DONE: investigate existing 'switch' case
			- DONE: update post_action()
			- DONE: Test
			- DONE*: invstigate 'switch' case in trig_check()
				- DECISION: make trig_vals_lst a list-of-lists
				- DONE*: update game_update
				- DONE*: update trig_check()
			- DONE: create ContainerFixedSimpleTrigMach
			- DONE: update control_panel mach obj
			- DONE: update mach_run to elim cond_switch_lst attrib passed to cond_check()
			- DONE: in cond_check(), update LeverArrayCond to pass it's own cond_switch_list attrib
			- DONE: in cond_class, elim cond_check() cond_switch_lst attrib
			- DONE: update game_update LeverArrayCond call with local cond_switch_list
			- DONE: add setters & getters to LeverArrayCond
			- DONE: test => fix lever_array cond
			- DONE: in cond_check(), update SwitchStateCond to pass it's own cond_switch_list attrib
			- DONE: add setters & getters to SwitchStateCond
			- DONE: update game_update SwitchStateCond call with local cond_switch_list
			- CANCEL: rework SwitchStateCond cond_check() to allow for all False values => default (if on True)
				- FINDING: I was right the first time ;-D
			- DONE: test (never getting to cond_check() - need to look at trig_check() )
		- DONE: clean up and optimize
			- DONE: sort out cup_of_tea game_update
			- DONE: comment out old Mach code
			- DONE: comment out old imports in game_updates
			- DONE: test dark castle
			- DONE: test cup_of_tea
			- DONE: elim cond_switch_lst from AutoMachMixIn cond_check() call			
			- DONE: clean up web_main, game_update (both)
			- DONE: clean up mach_class, pre_act, post_act, auto_act, cond_class
			- N/A: update post_action() trig_check() call as needed
			- DONE: update TrigMixIn trig_check() as needed
			- DONE: check to see if 'Warning' is reserved word in python => it's not
			- DONE: review and standardize pre_action(), post_action() and auto_action()
			- DONE: in cond_class(), update LeverArrayCond to inherit from SwitchStateCond
			- DONE: test
			- DONE: decide whether to harmonize 'timer' & 'switch' cases in trig_check() ?
				- DEC: no change
			- DONE: rethink keeping individual lists in trig_vals_lst
				- IDEA: it is tempting to have a list of lists for SwitchMachMixIn trig_vals_list...
				- IDEA: because we have this for cmd cases (i.e. a list per commands, multiple triggering cmds)
				- IDEA: but, there is only one switch (trig_switch) passed to SwitchMachMixIn... 
				- IDEA: it can have diff vals but only 1 at time
				- IDEA: therefore, there is no value to having a list of list... it only serves to confuse
				- DEC: eliminate nested list-of-lists for SwitchMachMixIn trig_vals_lst
				- DONE: update game_update, auto_act(), post_act()
			- DONE: test
			- DONE: comment clean-up mach_class(), pre_act(), cond_class(), game_update, post_act(), auto_act()
			- DONE: document format for trig_vals_lst in comments ( auto_action() and game_update() )
			- DONE: update mach doc for AutoMachMixIn, TrigMachMixIn, and SwitchMachMixIn

- DONE: review other inheritance ideas
	- DONE: review existing Warning class - refactor / integrate with Mach class
		- DONE: refactor app_turn modules (warning & timer code)
		- DONE: review existing Timer class - refactor / integrate with Mach class
		- N/A: update version build #
	- DONE: reconsider parent / child mach classes / MixIns
		- IDEA: can Warning be a parent of Mach?
		- IDEA: is Timer truly an independent class?
		- IDEA: do I want different types of Mach based on trigger_type = proto vs. auto vs. cmd vs. switch
		- IDEA: but if so, then how many MixIn varients do I end up with? Too many?	
		- DONE: de-dup warning and timer classes
	- DONE: it appears that "selective inheritance" just isn't a thing. What now?
		- IDEA: makes sense... in all other cases I inherit from simple parents to more complex children
		- IDEA: WarnClass is simpler... so it should be the parent
		- IDEA: perhaps right now I'll just make an independent class with duplicate trig_check code base
		- IDEA: as a future activity, I can look to de-dup in a more elegant fashion
- DONE: full test play
- DONE: git branch merge with master
	- DONE: 'git checkout master' to switch focus to master
	- DONE: 'git branch: to confirm focus
	- DONE: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
	- DONE: 'git push' to push merge to origin (GitHub)
	- DONE: confirm that origin is updated
	- DONE: confirm that code is updated and still runs
	- DONE: 'git branch -d <FEATURE_NAME>' to clean-up local branch
	- DONE: 'git push origin --delete <FEATURE_NAME>' to clean up origin
	- DONE: confirm origin is cleaned up
	- DONE: post-branch-delete run test
	- DONE: update cleesh engine version build


- DONE: fix VS Code error checking / pylance or whatever is wrong
	- DONE: tried un-installing and re-installing python extension & pylance (Sept 17)
	- DONE: moved vscode.exe from Downloads to Applications and was then able to upgrade => Pylance works!
		- LINK: https://github.com/microsoft/vscode/issues/7426#issuecomment-425093469


- DONE: Cases where I want a modular machine to run despite an error standard (build 0012 [])
	- IDEA: problem description
		- IDEA: e.g. 'go north' in antechamber triggers goblin
		- IDEA: i.e. should it ever be possible to override an error? If so, then how?
		- IDEA: the 'open portcullis' case is a special problem here - it will tell Burt it's locked...
			- IDEA: but the Goblin should attack before Burt can touch the Portcullis
	- IDEA: general thinking / philosophy
		- IDEA: narrative shoudld be able to trump simulation rules if desired (but it may take extra work)
		- IDEA: use fake_door for now and swap on goblin death ?
		- DEC: 'take axe' case is hard to fake out... I think I do need a systemic soluiton after-all
	- IDEA: basic approach
		- IDEA: what we really need to do is differentiate between "attemptable" failure vs. "impossible"
		- IDEA: attempting to open a locked door is the poster child for this
			- IDEA: it is reasonable for the player to attempt a new door they find
			- IDEA: in fact, they can only learn that it is locked by making the attempt
			- IDEA: further, if there is a guard in the room, it is reasonably that they take action
			- IDEA: against a player that is rattling the locked door they are guarding
		- IDEA: by contrast: 'eat horseshoe' (when there is no nearby horseshoe) is NOT attemptable
			- IDEA: and should not be dignified by a pre_action() response
	- IDEA: possible "attemptable" implementation
		- IDEA: perhaps re-org app_main()
			- IDEA: interp => val_err => auto_act => pre_act => val_att => cmd_exe => post_acct
		- IDEA: in Invisible, create separate <verb>_att method right after each <verb>_err method
			- IDEA: validated_att() checks for attemptable errors and returns if they are found
		- IDEA: alternatively, maybe new Errors class inherits from Invisible ?
			- IDEA: appears that only Writing inherits directly from Invisible?
		- IDEA: in errors, return is_attemptable
			- IDEA: if is_attemptable == True, time passes, and both pre_act() and auto_act() run
		- IDEA: all errors that return useful info (e.g. 'locked door') are attemptable
			- IDEA: is_attemptable = False for all cases where the obj is not in room
			- IDEA: in between is tricky... 
			- IDEA: go <direction w/ no exit> and take <obj held by creature> are good attemptable candidates
	- DONE: alternative work-arounds:
		- CANCEL: Maybe just 'x axe' case?
			- NA: update take_err() creature check - allow hostile reaction if burt attempts to take goblin axe?
		- CANCEL: possible solution 1
			- IDEA: creation of a pre-validate() module called interupt() that can over-ride errors
			- IDEA: modular machines should be designed so that it is easy to trigger & run them from interupt()
		- DEC: want a more consistent approach

	- DONE: sort out Error class idea
		- DONE: create fresh map of class inheritance
			- DONE: map class_std classes
			- DONE: map class_gs classes
			- DONE: map class_mach classes

		- DONE: create new <FEATURE_NAME>_feature git branch [attemptable_error]
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch <FEATURE_NAME>' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout <FEATURE_NAME>' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master

		- INPROC: sort out Invisible and Error classes
			- IDEA: all non-MixIn classes should inherit from Invisible
			- IDEA: Invisible itself should only hold the 'name' attrib and print footer
			- DONE: simplify Identity class
				- DONE: create identity_class_def.py in class_std pkg directory
				- DONE: copy all of Invisible class to identity_class_def.py
				- DONE: create Identity class which inherits from Invisible
				- DONE: update tipple quote doc line
				- DONE: comment out print
				- DONE: have Writing inherity from Identity; update base_class() import to Identity
				- DONE: comment out all in Invisible except name, print, and abstract identities
				- DONE: test
			- DONE: fix tactical issues
				- DONE: move where_is() debug method to ViewOnly
				- DONE: elim has_cond() identity in AutoMachMixIn / abastract identity section of Invisible
				- DONE: elim has_switch and has_trigger identities
				- DONE: elim is_warning()
				- DONE: de-dup Invisible vs. Identity identity methods
				- DONE: fix room.get_mach_lst() to not require invisible obj to have is_switch() or is_creature()
				- DONE: test
			- DONE: base condition and result classes inherit from Invisible
				- DONE: TrueCond in condition_class()
				- DONE: test
				- DONE: BaseResult in result_class()
				- DONE: test
			- DONE: clean up invisible(), identity(), up base(), room(), mach(), cond(), result()
			- DONE: post clean-up test
			- DONE: gs_class classes inherit from Invisible
				- DONE: update gs_class()
				- DONE: test
				- DONE: update core_class()
				- DONE: test
				- DONE: update map_class()
				- DONE: test
				- DONE: update io_class()
				- DONE: test
				- DONE: update score_class()
				- DONE: test
				- DONE: update end_class()
				- DONE: test
				- DONE: clean up gs_class classes
				- DONE: test
			- DONE: misc fixes
				- DONE: tripple quote descriptions for all mach classes
			- DONE: Error class
				- DONE: create error_class() module in class_std
				- DONE: import from Identity
				- DONE: create Error class in error() which inherits from Identity
				- DONE: update Writing to inherit from Error
				- DONE: copy all err methods to Error
				- DONE: tripple-quote elim all err from Identity
				- DONE: test
				- DONE: clean up identity(), base(), error()
		- DONE: update doc for classes
		- CANCEL: re-order auto_act to start of app-main loop
			- DONE: review web_main()
				- DONE: minor updates for web_main()
				- DONE: test
			- IDEA: interp => val_err => auto_act => pre_act => val_att => cmd_exe => post_acct
				- DONE: app_main() minor input refactor (if input = x or input = y ==> if input in [x, y])
				- DONE: is_stateful => is_wait
				- DONE: test
				- DONE: clean-up
				- DONE: copy / paste of existing command flow
				- CANCEL: comment out end of app_main auto_act()
				- CANCEL: move auto_act() to start of app_main on is_wait or is_interp_cmd
				- DONE: test & compare new command flow (should be the same)
			- FINDING: determined that best game flow was 1) input, 2) response, 3) end or auto_act
			- DONE: doc updated app_main() flow with findings
		- DONE: define NON-attemptable
			- IDEA: non-attemptable (i.e. <verb>_err() ) errors include:
			- IDEA: all interp() errors
				- IDEA: noun or direct obj not in scope or not in reach
				- IDEA: violates game phyiscis (e.g. obj not in hand, can't close locked door)
				- IDEA: there is no value in having attempt errors for debug commands
			- IDEA: challenges 
				- IDEA: the line behind what is attemptable and what viloates game physics is blurry!
				- IDEA: we want the designer to have confidence in what has happened
				- IDEA: need to think through what attempt would look like... what could it trigger?
			- IDEA: tricky case is where _att() error could work if a 2ndary condition were changed
				- EXAMPLE: if not obj.is_openable then there is no case in which obj *could* be openned
				- IDEA: so no complexity is created by moving this test to open_att()
				- IDEA: because we will *never* be testing for obj to be successfully openned
				- IDEA: compare this to the case where obj.is_openable and obj.is_locked
				- IDEA: here, obj *could* be openned if only it wasn't locked
				- IDEA: and if we wanted to create a cond for when obj *is* openned,
				- IDEA: we have now made that cond more complicated if we move the is_locked test to open_att()
				- IDEA: we are balancing the freedom to trigger vs. the cost of double checking in cond
				- IDEA: <verb>_att() cases like this include open (but locked) and go (but closed door)
			- IDEA: error order of operations also comes into play (e.g. "exit"); att always after err
				- IDEA: prep verbs - which have complex order of operations - get messy!!
				- IDEA: for now, all prep methods are unattemptable
			- IDEA: high-level principals
				- IDEA: think in terms of DBs... first normalize for consistency then de-normalize for perf/flex
				- IDEA: when in doubt, make an error unattemptable (<verb>_err() )
		- DONE: create attempt_err()
			- DONE: create attempt_err() module
			- DONE: create attmept_err() function
			- DONE: similar code to validate but call <verb>_att ; use try... except...
		- DONE: update app_main()
			- DONE: import attempt_err()
			- DONE: add attempt_err() to app_main loop after pre_action() and before cmd_exe()
		- DONE: fix hedgehog_guard_mach
			- DONE: create sword_not_on_flr_cond
			- DONE: add sword_not_on_flr_cond and pass_result to hedgehog_guard_mach
			- DONE: test
		- DONE: create attemptable error code in Error class
			- DONE: test existing (empty) calls to attempt_err()
			- DONE: create <verb>_att methods in Error and clean up redundant errors as I go
				- DONE: take <from creature>, <non-item>
				- DONE: drop <none>
				- DONE: stowe <none>
				- DONE: eat <not_food>
				- DONE: wear <not_garment>
				- DONE: open <not openable>, <*** locked ***>
				- DONE: close <not openable>
				- DONE: push <not buttonswitch>
				- DONE: pull <not springsliderswitch or leverswitch>
				- DONE: stand <none>
				- DONE: enter <not seat>
				- DONE: exit <not seat>, <creature not contained>
				- DONE: drink <none>
				- DONE: unlock <none>
				- DONE: lock <none>
				- DONE: put <none>
				- DONE: show <none>
				- DONE: give <none>
				- DONE: attack <none>
				- DONE: go <invalid direction>, <*** door closed ***>
			- DONE: clean up single comment <verb>_err
		- DONE: document Error updates and categories in doc
		- DONE: find way to signal special case of <open locked> and <direction door closed>
			- DONE: document special cases in game_update comments near mach
		- DONE: set time to clean up "##" comments in Error class
		- DONE: refactor attack_err() method
		- DONE: need early alert for when hero's load is getting heavy (i.e. approaching limit)
	- DONE: test

	- DONE: git branch merge with master
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d <FEATURE_NAME>' to clean-up local branch
		- DONE: 'git push origin --delete <FEATURE_NAME>' to clean up origin
		- DONE: confirm origin is cleaned up
		- DONE: post-branch-delete run test

	- DONE: update cleesh engine version build (build 0012 [11/17/2024])

- DONE: next gen error sub-system (build 0013 [12/11/2024])
	- POV: I really don't want to do this now... but machs and errors have a natural tension...
		- POV: and right now they are both in my head... 
		- POV: so there will never be a better time to fix this...
		- POV: major lesson learned: whenever reasonably possible, pass results to central orchestrator...
		- POV: provides much more flexibility down the road
	- IDEA: problems to solve
		- IDEA: need to eliminate order of operations dependency between error() and attempt()
		- IDEA: need to eliminate special cond desing for conditional att errors
		- IDEA: ideally, consolidate back to one set of error code per verb
	- IDEA: next generation error sub-system ideas (solving the attemptable error compromise) [IN-VER]
		A. One error command (<verb>_err) returns is_valid and is_attemptable to app_main()
		B. for is_valid == Flase and is_att == False:
			a. buffer error, no turn time passes (similar to validate() today) 
		C. for is_valid == False and is_att == True:
			a. cache error text
			a. app_main() increments turn and runs pre_act() and auto_act()
				1. app_main() passes is_valid to pre_act() which passes it to cond_chk (default == True)
				2. The base Condition class includes attrib and test for is_valid match
			c. if not cmd_override, buffer cached error
		- clean up "##" comments in Error class

	- DONE: create deployment plan
	- DONE: create new <FEATURE_NAME>_feature git branch [nxt_gen_err_branch]
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch <FEATURE_NAME>' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout <FEATURE_NAME>' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master

	- DONE: deployment plan steps
		- DONE: update app_main() and validate()
			- DONE: in app_main, is_interp_valid => is_valid
			- DONE: from validate() return cmd_err, is_att, and err_txt
			- DONE: default values of is_att = False and err_txt = ""
			- DONE: update app_main() to accept is_att & err_txt from validate()
			- DONE: in app_main() "if is_valid or is_wait:" => "if is_valid or is_att or is_wait:"
			- DONE: in app_main() "if is_valid:" => "if is_valid or is_att:"
			- DONE: in app_main(), after "err_on_attempt" line, 2nd "if" cmd = gs.io.buffer(err_txt)
			- DONE: in app_main(), add "not is_att" to if for cmd_exe()
			- DONE: test game (especially 3x attemptable errors)
			- DONE: clean up comments in app_main(), validate()
			- DONE: reconsider if auto_act() should run when is_att == True; => added is_att to 'if' 
		- DONE: pass is_valid all the way to cond_check()
			- IDEA: app_main() pass is_valid => pre_act() => run_mach() => cond_check()
			- DONE: update app_main() to pass is_valid to pre_action()
			- DONE: update pre_action() to recieve is_valid
			- DONE: pass is_valid to run_mach() in pre_action()
			- DONE: pass True to run_mach() in auto_action()
			- DONE: pass True to run_mach() in post_action()
			- DONE: update all variants of run_mach() to recieve is_valid
				- IDEA: for non-AutoMachMixIn, no use for is_valid
				- IDEA: for AutoMachMixIn, will pass to cond_check()
			- DONE: full game test
		- DONE: sort out Condition code
			- DONE: research attrib packing w/ **kwargs and defaulting to True
			- DONE: update TrueCond class to include **kwargs and is_valid_reqd attrib w/ default == True
			- DONE: in AutoMachMixIn run_mach() , pass is_valid to cond_check()
			- DONE: update all cond_check to recieve is_valid
			- DONE: test
			- DONE: update cond_check() in TrueCond to test is_valid vs. self.is_valid_reqd
			- DONE: test
		- DONE: update error methods (all errors to method, return is_att and err_txt for each "if"):
			- DONE: case = go
				- DONE: in validate()
					- DONE: for case = 'go', update getattr() to recieve is_att and err_txt
					- DONE: if (cmd_err and not is_att): buffer(err_txt)
				- DONE: in error()
					- DONE: move go_att => go_err 
					- DONE: set err_txt = (f"")
					- DONE: comment out buffer(f"")
					- DONE: return is_att (True for moved cases) and err_txt()
				- DONE: in app_main()
					- DONE: for case == 'go', elim attempt_err() call
					- DONE: test all go_err cases (antechamber 'n' should not run mach)
				- DONE: in game_update:
					- DONE: set cond attrib to is_valid_reqd = False
					- DONE: test antechamber 'n' again (mach should run now)
				- DONE: thurough testing of all go_err cases
				- DONE: clean up game_update(), error(), cond(), mach(), validate(), app_main()
			- DONE: case = 2word
				- DONE: in validate()
					- DONE: for (case = '2word' and word1 in [<verb_lst>]
					- DONE: update getattr() to recieve is_att and err_txt
					- DONE: if (cmd_err and not is_att): buffer(err_txt)
				- DONE: per <verb> updates
					- DONE: read
						- DONE: validate(): <update verb_lst>
						- DONE: app_main(): <update verb_lst>
						- DONE: error(): <verb_att> => <err>, return is_att, err_txt, buffer => err_txt
						- DONE: game_update(): set is_valid_reqd = True for an7 is_att cond objs
						- DONE: test
					- DONE: examine
					- DONE: take
					- DONE: drop
					- DONE: stowe
					- DONE: clean up comments in error()
					- DONE: eat
					- DONE: wear
					- DONE: open
					- DONE: close
					- DONE: clean up comments in error()
					- DONE: push
					- DONE: pull
					- DONE: stand
					- DONE: enter
					- DONE: exit
					- DONE: clean up comments in error()
					- DONE: get_weight
					- DONE: capacity
					- DONE: where_is
					- DONE: clean up comments in error()
					- DONE: elim individual verb test in validate()
			- DONE: case = prep
				- DONE: individual verb test in validate()
				- DONE: update app_main()
				- DONE: drink
				- DONE: lock
				- DONE: unlock
				- DONE: put
				- DONE: clean up comments in error()
				- DONE: show
				- DONE: give
				- DONE: attack
				- DONE: clean up comments in error()
				- DONE: remove test_chair from main_hall and box + rock from entrance
		- DONE: clean-up legacy code	
			- DONE: in app_main, eliminate refs to attempt_err() including import and <verb_lst>
			- DONE: in validate(), elim <verb_lst> ref
			- DONE: test
			- DONE: clean up comments in validate(), app_main(), game_update()
			- DONE: test
			- DONE: eliminate attempt_err()
			- DONE: final test (including cup_of_tea)
		- DONE: doc update (kwargs, pros == order of ops & default, base errors still buffer directly)

	- DONE: git branch merge with master
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d <FEATURE_NAME>' to clean-up local branch
		- DONE: 'git push origin --delete <FEATURE_NAME>' to clean up origin
		- DONE: confirm origin is cleaned up
		- DONE: post-branch-delete run test

	- DONE: update cleesh engine version build (build 0013 [12/11/2024])


# *** start unused code for combo conditions ***

*** Eliminated Code ***
	def run_mach(self, gs):
		cond_return_lst = []
		for cond in self.cond_lst:
			cond_return = cond.cond_check(gs, self.mach_state, self.cond_swicth_lst)
			cond_return_lst.append(cond_return)
		result_index = cond_return_lst.index(True)
		result = self.result_lst[result_index]
		temp_mach_state, cmd_override = result.result_exe(gs, self.mach_state)
		self.mach_state = temp_mach_state
		return cmd_override, result.name

# *** sample input = [['and', cond_1, cond_2]['or', cond_3, cond_4], cond_5] ***

#	def run_mach(self, gs):
##		print(f"mach running; mach_name = {self.name}") # for troubleshooting
#		for idx, cond in enumerate(self.cond_lst):
#			if isinstance(cond, list):
#				term_1 = cond[1].cond_check(gs, self.mach_state, self.cond_swicth_lst)
#				for condition in cond[2:]:
#					term_2 = condition.cond_check(gs, self.mach_state, self.cond_swicth_lst)
#					if cond[0] == 'and':
#						combo = term_1 and term_2
#					elif cond[0] == 'or':
#						combo = term_1 and term_2
#					term_1 = combo
#				if combo:
#					result = self.result_lst[idx]
#					self.mach_state, cmd_override = result.result_exe(gs, self.mach_state)
#					return cmd_override, result.name
#			else:
#				if cond.cond_check(gs, self.mach_state, self.cond_swicth_lst):
#					result = self.result_lst[idx]
#					self.mach_state, cmd_override = result.result_exe(gs, self.mach_state)
#					return cmd_override, result.name

# *** end unused code for combo conditions ***

*** already done ***
- DONE: would be nice to have an Error class that inherits from Invisible [FUTURE]
	- IDEA: but this would break in heritance?
	- IDEA: or maybe Writing just needs to inherit from Error ?

- DONE: How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away
	- DONE: eliminate universal_scope => just add these to Burt's invis_lst

- DONE: review mod-mach improvement ideas:
	- CANCEL: initial ideas
		- IDEA: goal is a single method for conditions and a single method for results (???)
		- IDEA: for conditions, attributes = modules + logic_str + descript_str
		- IDEA: use attribute packing / kwargs to pack conditions / results with variable # of attributes
	- CANCEL: naming
		- IDEA: Shorter cond & result names!!
		- IDEA: Compound Results and Conditions named after intent
		- IDEA: naming conventions: need to avoid confusion between match_state and mach_state
		- IDEA: naming conventions: cond & result name should be same except post-fix
		- IDEA: address long naming issue with describe() ability
	- DONE: general org ideas
		- DONE: BaseCond => always check state
		- DONE: BaseResult => always do a buff_try()
		- DONE: All results capable of Buffering (rename Result classes appropriately)
		- DONE: if no conditions == True then default_result = nothing happens (no need for pass_result)
		- CANCEL: in machines, should conditions and results just be key-value pairs in a dictionary?
			- IDEA: As opposed to needing 2 separate lists with identical indexes?
	- DONE: primative conditions & results modules
		- DONE: goal of primative & compound structure is to increase re-use of Cond & Result classes 
			- IDEA: currently too many class-per-var cases
		- DONE: Primative Conditions (named after condition) [always include single attribute & value] 
		- CANCEL: Compound Conditions (and / or) 
			- IDEA: named after intent; match mach, result, & trig 
			- IDEA: {trig_check() method links primatives}
		- DONE: Primative Results (named after result) [always include single attribute & value] 
		- DONE: Compound Results (named after intent
			- IDEA: match cond, trig, & mach) 
			- IDEA: {trig_check() method links primatives}
	- DONE: Composed Conditions & Results: comp_cond / comp_result == AND / OR of multiple primatives
		- CANCEL: like the idea of AND vs. OR option
		- DONE: NOT option for each cond module is vital (achieved via 'match')
			- EXMP: Generalize in-hand vs. not-in-hand Condition (single primative)
			- EXMP: Generalize creature-has-item vs. creature-does-not-have-item Cond (single primative)
		- IDEA: each 'primitive' cond tests for *one* thing (but state of thing is attrib to be matched)
	- DONE: Have simple, 1-test/ 1-action 'Primative' Conditions and Results: prim_cond and prim_result
		- IDEA: would we really want each primative cond & rslt linked?
		- IDEA: lean towards composing result_1 from r1_m1, r1_m2, & r1_m3 => linked to comp cond
	- DONE: Wildcard clean-ups
		- IDEA: Extend trig_check wildcards to 'post_act_cmd' & 'auto_act_cmd'
		- IDEA: Extend trig_check wildcards to work with Warnings (or de-dup Warning's trig_check)
		- IDEA: guard against multiple wildcaards per list
	- DONE: Results
		- IDEA: extend BufferOnlyResult result_exe method in BufferAndEndResult and BufferAndGiveResult
		- IDEA: extend child methods in results_class_def ?

- DONE: list of 'contained' internal_switches in MachMixIn attributes?
	- IDEA: (i.e. add to scope and remove levers & button from features?)
	- IDEA: [hold off until at least one more control_panel type machine gets created]

- DONE: sort out ability to push button / pull levers while goblin is guarding

- DONE: Establish clearer nomenclature for temp variables that will be fully assigned at end
	- EXMP: 'royal_hedgehog-*temp*'


############################
### CLEESH VERSION 3.8.1 / DARK CASTLE VERSION 3.2.0 START ###
############################

Start Date: Dec 11, 2024
End Date: 

*** getting started ***
- DONE: establish new versions and builds
- DONE: review project list and decide on scope
- DONE: organize scope by cleesh vs. dark castle work where possible
- DONE: fine-grained to-do review and ordering for DC tech issues

	- DONE: create new story_update_feature git branch
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch story_update_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout story_update_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master

*** known dark castle tech issues ***
- DONE: hedgehog description should change when distracted by food (ALREADY DONE)
- DONE: sort out hedgehog description post biscuits if Burt leaves rm
	- IDEA: burt leaves room before RH finishes eating => description update never triggered
	- PROB: hedgehog_done_eating_mach is in RH; never triggers if RH out of scope at timer end
	- IDEA: need a universal_invis_<holder?> that is added to room.get_mach_lst() scope
	- IDEA: tempted to make this a room... but want it to be universal across games...
	- IDEA: maybe a list in gs.core ? "universal_invis_lst" = invist obj always in scope ?
	- DONE: git branch story_update_feature
	- DONE: add univ_invis_lst attrib to gs.core
	- DONE: update univ_invis_lst attrib in game_update() (DC & cup_of_tea)
	- DONE: ref univ_invis_lst in room.get_mach_lst() (use copy() to create independent copy)
	- DONE: add hedgehog_done_eating_mach to uni_invis_lst in game_update()
	- DONE: test
	- DONE: clean-up room(), game_update()
	- DONE: check for any other auto-actions that should be in univ_invis_lst (could I have just added to burt?)
		- DONE: moved hedgehog_eats_timer to univ_invis_lst
		- DONE: test
	- DONE: update mach doc with univ_invis_lst
- DONE: fix Antechamber description still mentions goblin after death (ALREADY DONE)
- DONE: fix hedgehog description after sword is returned (before goblin killed)
	- FINDING: RH response is fins (thankfull and gives key); but need to enable key-for-sword swap
- DONE: fix eat_biscuits_warning 
	- DONE: so that it no longer lives in just entrance and main_hall 
	- DONE: and no longer triggers when biscuits not in hand
	- DONE:  making eat_biscuits_warning universal and enabling success feedback loop for cmd_exe
- DONE: fix case where sword is in Burt's inventory and tries to take in Entrance but royal_hedgehog stops him
- DONE: enable player to give silver_key to RH in return for shiny_sword
- DONE: update show silver_key for RH
- DONE: solve case where player drops sword in same room as hedgehog after using it; on get key, disable guard
	- IDEA: create a modular machine that disables hedgehog_guard after silver_key is given
	- DONE: create new Cond class to check creature inventory
	- DONE: import Cond class in game_updates
	- DONE: instantiate new Cond obj for RH has silver_key == False
	- DONE: create new Result class to disable mach
	- DONE: import Result class into game_updates
	- DONE: instantiate new Result obj
	- DONE: create auto_mach in DC game_update
	- DONE: pre-test to confirm as-is behavior
	- DONE: add auto_mach to game (in RH invis_lst)
	- DONE: test
	- DONE: set disable_rh_guard_result_2 to disable guard_disable_mach (don't need auto_action once run)
	- DONE: test
	- DONE: clean-up: cond(), DC game_update()
- DONE: stale_biscuits => biscuit
	- DONE: make stale_biscuits singluar (just one biscuits in a paper bag)
		- IDEA: change biscuit trademark to sword and key emblem
		- IDEA: make biscuit yummy; Nana's famous recipie
		- IDEA: backstory of Nana fondly feeding hedgehog biscuits back when she was at the castle?
		- IDEA: update 'eat biscuit' warning text... should ref baker job and Nana
		- IDEA: maybe Burt is the first Baker in his family; perhaps not a highly regarded profession
		- DONE: implement
			- DONE: re-read Nana broach text
			- DONE: create paper bag (openable but no lock)
			- DONE: add paper bag to Burt's inventory
			- DONE: decide on Burt's backstory / baking heritage... 
				- IDEA: is Burt a true baker following in the footsteps of Nana? (lean this way)
				- IDEA: or is baking something he's not really cut out for?
				- IDEA: maybe Willy's middle name was Herbert?
				- DONE: create story.md in doc folder to document the story of Dark Castle
				- DONE: formally document Burt's backstory
				- DONE: Update Nana borach text to match Burt's backstory
				- DONE: update family tree if needed
			- DONE: create baked_biscuit (class = food)
			- DONE: add biscuit to paper bag
			- DONE: create insignia (Writing)
			- DONE: add insignia to biscuit
			- DONE: update warning to reference biscuit
			- DONE: update warning text
			- DONE: test
			- DONE: remove stale_biscuits
- DONE: vary Burt description during inventory (inject some backstory here; include Nana and pub crush)
	- DONE: implement just for DC
	- DONE: generalize to work for all games (test w/ Tea) [hero_descript_count attrib in gs.core]
	- DONE: test for DC and Tea
- DONE: sort out Burt cary weight post biscuits swap
	- DONE: test (does not pass - not removing weight of portable container contents when item dropped)
	- DONE: sorted - needed to include weight of biscuit in starting weight of  bag
	- DONE: biscuit weight from 2.5 lb => 1 lb (subtract 1.5 lbs)
		- DONE: burt from 106.5 => 105 lb
		- DONE: bag from 3 lbs => 1.5 lbs
		- DONE: biscuit from 2.5 lbs => 1 lbs
		- DONE: test
- DONE: update winning condition to reading scroll while sitting on throne?
	- DONE: update Illuminated Letters text to ref throne
	- DONE: creaate CreatureContainedCond class in cond module
	- DONE: import CreatureContainedCond and instantiate not_in_throne_cond obj
	- DONE: instantiate scroll_not_in_throne_result obj based on BaseResult
	- DONE: write text for scroll_not_in_throne_result
	- DONE: add cond & result to kinging_scroll mach
	- DONE: test
	- DONE: clean up cond()
- DONE: add option to win condition to read back story 
	- DONE: return gs.end.game_ending as game_ending from app_main() to web_main()
	- IDEA: in web_main(), just before "THANKS" & "Press Enter", if game_ending = 'win!', offer backstory
	- DONE: create print_game() in file_io()
	- DONE: import print_game() into web_main()
	- DONE: in web_main(), if end == 'won!': print_game('read_bkstry_str')
	- DONE: call confirm_choice() function
	- DONE: if confirm: print_game('backstory')
	- DONE: test
	- DONE: clean up web_main(), gs.end(), to-do-list
	- DONE: add back-story to game_static() w/ /n/n breaks
	- DONE: test
- DONE: fix goblin attack on attempt to unlock portcullis
	- DONE: fix prep order in mach
	- DONE: test
	- DONE: clean up game_update, app_main
	- DONE: investigate wild-card option (works for portcullis or key? use if key)
		- DONE: in game_update(), replace 'rusty_key' with '*'
		- DONE: test => worked!
		- DONE: clean-up game_update()
	- DONE: document prep case trigger order somewhere I will see it (ref to interp / validate / trig_check)
	- DONE: create TBD in Interpreter section to sort out whole dir-obj prep-case word order / re-order issue
- DONE: Stone Coffer => no-lid box
	- DONE: convert stone_coffer to ContainerFixedSimple
	- DONE: test
	- DONE: clean up game_update()


*** known dark castle narrative issues ***
- DONE: misc specific description updates
	- DONE: on 'x goblin' descript, emphasize that Burt is peering from S side of room
	- DONE: 'officious' == offering unwanted advice => NOT hidebound or miro-managerial
		- IDEA: Perhaps update to implay new definition rather than classic: "assertive of authority in an annoyingly domineering way, especially with regard to petty or trivial matters." 
	- DONE: update hedgehog description while eating to "The RH is ravenously eating" (done?)
	- DONE: fix Goblin description to no longer mention Control Panel
	- CANCEL: "what would your mothter say" error to "What would your Nana say?"
		- FINDING: this error belongs to the clessh engine and should stay generic
	- DONE: fix post-goblin-slain Antechamber description
- DONE: more description updates:
	- DONE: RH
		- DONE: describe RH as "stalwart"
		- DONE: Have the hedgehog think burt is playing if he attacks with a non-weapon
			- DONE: starts making wax-on, wax-off motions with paws
	- DONE: link lantern, sword, and jug to Infocom history but unify with fantasy genre (no battery)
		- DONE: lantern description (but no battery)
		- DONE: Upate water_bottle to Enchanter jug description
		- DONE: Update shiny_sword to Zork I elven sword description (elven runes)
	- DONE: shiny sword glows near enemies?
		- DONE: research Zork options
			- FINDING: 1 rm away: "Your sword is glowing with a faint blue glow"
			- FINDING: 2 rm away: "Your sword is no longer glowing"
			- FINDING: same rm: "Your sword has begun to glow very brightly"
			- FINDING: enemy dead: "Your sword is no longer glowing"
		- DONE: create WeaponAutoMach
			- DONE: create mach class
			- DONE: import mach class to both game_updates
			- DONE: instantiate starting shiny_sword_new based on WeaponAutoMach
		- CANCEL: cond & results - first try
			- DONE: 0th cond = sword not in hand => nothing happens
			- DONE: 1st cond = goblin_dead => result = "no longer glow", disable mach
			- PAUSE: 2nd cond = room is Main Hall => buffer "faint glow", set state
				- TBD: still need to set state
			- CANCEL: 3rd cond = room is Antechamber => buffer "very bright glow"
			- CANCEL: 4th cond = state set (must be Entrance) => buff "no longer glowing"			
		- DONE: re-think cond & results
			- IDEA: sword state needs 3 values: 0 = off, 1 = glow, 2 = bright glow
			- IDEA: sword description only mentioned on state change (or 'x')
			- IDEA: state only changes on pick-up, drop, rm chg, death of enemy
			- DONE: need to create disp_cond() for shiny_swordnew and base cond on state for 'x'
			- DONE: disp_cond => buff(f'sword_disp_{sword_state}')
			- DONE: create descriptions linked to shiny_sword state
			- CANCEL: does sword state pass to room state?
			- DONE: update descriptions / disp_cond() to make sense for examine (skip on 0 or None)
			- DONE: need to update mach module to deal with compound cond
				- DONE: review 'full' compound cond code in 'unused code' in done()
				- DECISION: just implement simple 'and' case that mirrors result implementation
				- DONE: implement simple 'and' case for compound cond
				- DONE: test (existing single-cond code)
			- DONE: review & update cond & results plan
			- DONE: modify / create needed cond and result classes:
				- DONE: update MachStateCond to include tgt_state attrib
					- DONE: update MachStateCond
					- DONE: update existing MachStateCond conditions
					- DONE: test existing MachStateCond conditions
				- DONE: create sword_state_not_0_cond of class MachStateCond
				- CANCEL: create SetStateResult SetStateResult => can set mach_state in BaseResult
				- CANCEL: make sword_state_0_result class BaseResult => already exist: sword_stops_glowing_result
				- DONE: clean up old SetStateResult in result_class()
			- DONE: Update mach combo conditions and results to check for state change (states part 2)
				- DONE: (sword not in hand) && (s_s == !0) => (buff('stopped glowing'; sword_state => 0)
				- DONE: goblin dead => (buff('stopped glowing'); sword_state => 0) && (disable mach)
				- DONE: (rm = Entrance) && (sword_state != 0) => (buff('stopped glowing'); sword_state=> 0)
				- DONE: (rm = main_hall) && (sword_state != 1) => (buff('blue glow'); sword_sate => 1)
				- DONE: (rm = antechamber) & (sword_state != 2) => buff('bright glow) / sword_state => 2
		- DONE: test
			- DONE: place shiny_swordnew in main_hall
			- DONE: test shiny_swordnew behavior
				- DONE: fix stops glowing if in backpack (in_hand => in_inv)
				- DONE: fix glowing on enter main_hall (pass_result if not_in_inv and is_0)\
				- DONE: sort out 'x swordnew' => all good now
		- DONE: shiny_swordnew => shiny_sword
		- DONE: clean up game_update(), game_static()
	- DONE: one final full test
- DONE: have shiny sword be hanging on wall (like Zork I)?
	- IDEA: how does this work in Zork?
		- IDEA: In TADS, this is accomplished for obj and rooms by giving them two attribs:
		- IDEA: isInInitState attrib (bool) and initDesc (string) [or roomFirstDesc]
		- IDEA: by default, IsInInitState starts as True and becomes False as soon as obj is moved
		- IDEA: this would require updating base obj and also core methods like take()
		- IDEA: But, it would allow object to be easily given more placement description on initial contact
		- IDEA: in the room display method, obj w/ initDesc and isInInitState could be handled separately
	- IDEA: how do I want to accomplish it?
		- IDEA: how about associating init_desc with the room rather than the obj?
		- IDEA: there are fewer room obj to update - and init_desc is really about initial placement in rm
		- IDEA: add init_desc_lst attrib to room class
		- IDEA: create init_desc class with attribs for name, linked obj, and desc_key
		- IDEA: for obj w/ initial descriptions, instantiate init_desc and add to rm init_desc_lst
		- IDEA: in rm display, provide init_desc first and add associated obj to skip_lst
		- IDEA: later in dispaly, skip std obj desc if obj is on skip_lst
		- IDEA: in take() method chk to see if obj has init_desc and, if so, remove it from init_desc_lst
			- IDEA: how to link from obj back to init_desc ?
			- IDEA: propose strict naming convention for init_desc (e.g. '<obj_name>_init_desc')
			- IDEA: include init_desc obj in obj pickle so they can be reverse looked up via text
	- DONE: implement
		- DONE: create init_desc class
		- DONE: instantiate shiny_sword_init_desc obj
		- DONE: create desc value in static_gbl() 
		- DONE: add init_desc_lst attrib to room class
		- DONE: update room display code to handle init_desc first
		- DONE: sort out UI / spacing
		- DONE: update room display code to not display same obj in std descript vis skip_lst
		- DONE: don't display init_desc if obj taken and elim init_desc
			- DONE: update room.remove_item to remove init_desc from init_desc_lst
		- DONE: test - gen
	- DONE: fine tune room display
		- DONE: decide if init_desc() should truly only be for items on rm floor
			- IDEA: excluded obj include view-only and obj in / on containers
			- IDEA: a ViewOnly obj could be described in detail in the regular room description...
			- IDEA: unless it is somehow manipulated... but these cases are currently rare
			- IDEA: could be used for non-portable containers before open... but would I want to?
			- IDEA: an obj in a container could have it's state described in more detail
			- IDEA: e.g. "the teddy bear is sweetly tucked in under the covers"... but again, rare
			- DECISION: follow the "don't build it if you don't need it yet" rule
			- DONE: linked_obj => linked_item
			- DONE: test
		- CANCEL: update shiny_sword regular desc if appropriate
		- DONE: update rm disp: 1) title, 2) rm desc, 3) passages, 4) viewonly, 5) init, 6) item, 7) creat
			- DONE: for room display, separate creatures from ViewOnly and list creatures 2nd
		- DONE: test - multiple obj w/ init_desc
		- DONE doc rm display_contain order
		- DONE: clean up room_class()
		- DONE: room_itme_lst => rm_item_lst
- TBD: play & note obvious nouns with no description; provide description (e.g. 'keyhole')
	- DONE: room 1
		- IDEA: goals for room 1
			- IDEA: room 1 is mostly about learning the rules of the Dark Castle world
			- IDEA: lesson 1: pay attentinn - the world is dangerous (e or w off drawbridge)
			- IDEA: lesson 2: learn to open / close (postbox)
			- IDEA: lesson 3: learn to lock / unlock (front_gate)
			- IDEA: lesson 4: learn how weight works (big_rock)
			- IDEA: lesson 5: learn that we are in the Zork / Enchanter universe (zorkmid / certficate)
		- IDEA: should start out looking very foreboding but then get a bit silly as front_gate is examined
		- DONE: add viewonly drawbridge
		- DONE: read and update Moat & Dark Castle
		- DONE: update passages to include all info in description
		- DONE: update room description; eliminate duplication with passages; "entrance" desc=> "front gate"
		- DONE: review existing nouns:
			- DONE: drawbridge
			- DONE: moat
			- DONE: dark_castle
			- DONE: front_gate
			- DONE: rusty_lettering
			- DONE: add key_hole
			- CANCEL: add handle
			- DONE: rusty key
			- DONE: cheese wedge
			- DONE paper bag
			- DONE: baked biscuit
			- DONE: earthen jug
			- DONE: well water
		- DONE: UI decision - if all nouns will have a description, do I need to capitalize?
			- DECISION: Dark Castle stays in caps. Everything else in regular text becomes regular case.
		- DONE: test go south
		- DONE: test east & west (no weapon)
		- DONE: test 'eat biscuits'
		- DONE: there should be at least one item here (like the mailbox & leaflet)
			- IDEA: WR postbox / mail slot w/ ancient scroll certifying bright castle to be Grue-Free
			- IDEA: (not very convincing - cert largely tells dark and dangerous places not explored)
				- IDEA: lock has only just recently crumbled from rust and neglect
				- DONE: create royal_cypher
				- DONE: create postbox obj
				- DONE: update room description
				- DONE: add postbox to room
				- DONE: create ancient_certificate
				- DONE: create bold_script
				- CANCEL: investigate adding room.feature_lst to item scope (enable interaction w/ postbox)
					- IDEA: this code is pretty deep - not sure I want to mess with it right now
				- DONE: investigate enabling init_desc attrib for viewonly (e.g. postbox)
					- IDEA: in some cases, will want non-init_desc - for key / interactive obj (like throne)
					- DONE: update room.disp_contain to check for init_desc for non-items, non-creatures
					- DONE: test
					- DONE: create init_desc obj for postbox
					- DONE: test
					- DONE: clean up room_class()
					- DONE: comment room_class() / game_update with init_desc order implications
		- DONE: big_rock here (use init_desc) with a zorkmid (key to weight puzzle) under it
			- DONE: check burt's weight capacity; set big_rock weight so burt can only take it w no inv
			- DONE: add big_rock to Room 1
			- DONE: create desc for big rock
			- DONE: adjust creature.put_in_hand() to test for weight > max_weight (NOT >= )
			- DONE: test
			- DONE: create an init_desc for bog_rock
			- DONE: test
			- DONE: instantiate zorkmid as item
			- DONE: create machine to vend zorkmid (once) when rock is first taken
				- IDEA: make big_rock the zorkmid_dispenser? Turn off after one run
			- DONE: adjust item weights to make zorkmid the only half-pound weight
			- DONE: enable drop to work on backpack items (e.g. "you toss the X from your pack")
			- DONE: enable multiple commands to be input at once, separated by commas
				- DONE: check Zork behavior => multiple entry halts on error or enter dark rm
				- DONE: in app_main() create cmd_queue, populate it, and read commands from it
				- DONE: test std cases
				- DONE: clear cmd_queue on special word cases (e.g. 'quit')
				- DONE: test special cases
				- DONE: clear cmd_queue on not is_valid and on comd_override
				- DONE: test error cases
				- DONE: clean-up app_main()
			- DONE: enable 'drop all'
				- DECISION: 'drop all' will drop item in hand and all in bkp but not worn
				- DONE: construct drop all commands in cmd_queue
				- DONE: initial test
				- DONE: deep-dive test (use in multi-cmd string)
				- DONE: clean-up app_main()
			- DONE: enable multiples UI (e.g. 'Rusty Key: Dropped')
				- DONE: create multi_count attrib in gs.io
				- DONE: set multi_count = 0 in game_update()
				- DONE: in app_main() , if 'drop all', multi_count = len(drop_lst)
				- DONE: in app_main() , at end of while loop, if multi_count > 0 , decrement
				- DONE: in item_class() : drop() : if multi_count > 0 use multi_format
				- DONE: testing
			- DONE: enable 'except command
				- DONE: except testing - basic problem = how to evaluate except_element to item name ??
					- DONE: test rusty_key
					- DONE: if 2 words after 'except', try word1_word2 in inventory_list by name
					- DONE: elif 1 word after 'except', try word1 in inventory_list by name and
					- DONE: elif 1 word, try word1 inventory_ist by root_name
					- DONE: check for 2 of same root => err
					- DONE: test error cases
						- DONE: > 1 use of 'except'
						- DONE: > 1 except item
						- DONE: except item not in your inventory
						- DONE: no except item
					- DONE: tighten code - first pass
			- DONE: enable 'take all'
				- IDEA: in order of weight ?
				- DONE: test in Zork to see order / behavior of 'take all'
				- DECISION: don't re-order for now
				- DONE: expand app_main() 'drop all' case to include 'take all'
					- DONE: drop_lst => multiples_lst
					- DONE: add local vars: is_multiples_action and multiples_action_type ('drop', 'take')
					- DONE: define inventory_lst for multiples_action_type == 'take'
						- DONE: define what behaviors do I want for 'take all'?
							- IDEA: take all taks from room.floor_lst, NOT room.feature_lst
							- IDEA: don't try to take non-Item class obj
							- IDEA: don't try to take Liquid class obj
							- IDEA: If there's an open ViewOnly container holding an item, take the item
							- IDEA: if there's a portable container take it
							- IDEA: don't attempt to take from player's own inventory
							- DONE: if there's a portable container holding an item, don't take the item
							- DONE: if there's a creature, don't attempt to take from the creature
						- DONE: create get_take_all_lst() method in Room class
						- DONE: initial testing
				- DONE: expand Item.take() methoed to use multiples UI
				- DONE: full test of take_all behavior - especially containers (does take from port contain)
				- DONE: fix 'take all' / 'drop all' if there is nothing to take / drop
				- DONE: get "again" working with "drop all" / "take all" cases
					- DONE: get g working for 'drop all'
					- DONE: get g working for 'take all'
						- FINDING: finally figured out the problem... by default, I can take from bkpk
						- DONE: create from-scratch get_take_all_lst() method to exclude gs.core.her0
				- DONE: expand 'except' case to include take all
				- DONE: sort out last 2 take-all cases
				- DONE: get 'again' working with except cases
				- DONE: mini-in-place code clean-up for app_main()
				- DONE: err when ref obj excluded from inventory_lst ('take all except X' when X in inv)
					- DECISION: addressed this via updated error message
			- DONE: Full code clean-up - probably need a separate 'except' function
				- DONE: prep for except function creation
				- DONE: create except function and refactor
				- DONE: clean-up
				- DONE: additional except clean-up
				- DONE: initial clean-up multiples function
				- DONE: clarify / make consistent if-then-else outputs
				- DONE: clean up multiples code to prepare for external function
				- DONE: clean up comments
				- DONE: create multiples mini interp function
			- DONE: fix take_rock_mach for cases where rock can't be taken due to weight
				- DONE: need to pass is_valid to post_act()
				- DONE: keep investigating is_valid => post_act() => run_mach() => cond_chk() [not printing]
				- DONE: updated code in each condition class
				- DONE: full game test
				- CANCEL: create ValidCond that all cond (inc TrueCond) inherit from and use super() to call
					- FINDING: not needed. super().method() only returns to local scope. can use TrueCond
				- DONE: sort out super() call for TrueCond for MachStateCond
				- DONE: extend super() solution to rest of Cond classes (had to exclude non-TrueCond childs)
				- DONE: full game test
				- DONE: clean up app_main() and post_act(), cond_check(), run_mach()
			- DONE: update help menu to explain 'drop all / take all' (not from bkpk) & 'except'
			- DONE: update help menu to explain command queue
		- CANCEL: entrance => gatehouse
			- FINDING: entrance works fine - the real change is main_hall => gatehouse
		- DONE: make path south examineable
			- DONE: 'path' => 'untrodden_path' in game_update() gs.map
			- DONE: create untrodden_path ViewOnly obj
			- DONE: add untrodden_path to entrance.features
			- DONE: add untrodden_path to the object pickle
			- DONE: test
		- DONE: clean up game_update()
	- DONE: room 2
		- IDEA: this is a safe room for Burt to rest in - sort of a home base
		- DONE: main_hall => gatehouse
			- DONE: crete gatehouse room in game_update()
			- DONE: create gatehouse description in game_static_gbl()
			- DONE: update map in game_update()
			- DONE: initial test
			- DONE: replace all instances in game_update()
			- DONE: move main_hall & tapestries to test section of pickle load in game_update()
			- DONE: full test
			- DONE: re-org main_hall and faded_tapestries in game_static_gbl()
			- DONE: clean up game_update()
		- DONE: de-capitalize all nouns
		- DONE: de-dup passages descriptions vs. base description
		- DONE: review existing nouns
			- DONE: update bandana to remmove 80s ref
		- DONE: add all referenced nouns
			- DONE: old_furniture
			- DONE: cobwebs
			- DONE: musty_smell
			- DONE: arrow slits
		- DONE: use init_desc where appropriate
		- DONE: make paths examineable
			- DONE: make path names (provided via 'look') examinable nouns ('path' => Winding Path)
			- DONE: foreboding_archway
			- DONE: can passage obj live in map (rather than room feature?)
			- DONE: update gs.map.get_door_str() to enable f_archway n => s but lit_archway s => n
				- IDEA: door_var = room_pair['door'] ; if door_var is list, read dict in list => door_var
				- IDEA: existing clauses ref door_var (not room_pair['door'])
				- IDEA: contemplate need to make 'door' val work for get_door_lst() and get_door() too
				- DONE: update go_err() in error_class() to acount for non-door returns from get_door()
				- DONE: propose multi-value path in game_update()
				- DONE: update get_door_str() for multi-val path
				- DONE: update get_door for multi-val path
				- DONE: update get_door_lst for multi-val path
				- DONE: create obj and description for lit_archway
				- DONE: test
				- DONE: update to allow string paths in multi-val dict
				- DONE: test
				- DONE: clean-up game_update(), error_class(), map_class(), room_class()
				- DONE: doc dict option in comments and in doc file (also mention paths as obj)
				- DONE: doc that 'door' in map_dict really means 'any passage between rooms'
		- DONE: update dark_castle description to indicate that there are always dark clouds overhead?
		- DONE: elim need for unreachable rooms
			- DONE: update room_lst with special 'unreachable' value
			- DONE: update gs.map.chk_valid_dir() for 'unreachable'
			- DONE: update gs.map.get_room_lst() to check for 'unreachable'
			- DONE: test
			- DONE: comment out old unreachable rooms
			- DONE: 2nd full test
			- DONE: comment special value of 'unreachable'
			- DONE: clean up gs.map() and game_update()
			- CANCEL: eliminate hidden rooms [IN-VER]
				- EXAMPE: s, e, & w of Entrance 
				- CANCEL: Room class would need a custom_path_lst attrib
				- CANCEL: custom_path_lst called from room.disp_cond()	
		- DONE: test all machines
		- DONE: final tune up
			- DONE: extract paths from description
	- DONE: room 3
		- DONE: de-capitalize all nouns
		- DONE: de-dup passage descriptions vs. base description
		- DONE: review existing nouns
		- DONE: add all referenced nouns
		- DONE: make paths examineable
		- N/A: use init_desc where appropriate
		- DONE: test all machines
		- DONE: sort out unarmed strike obj (e.g. burt == fist); unlock gate empty handed => Fist
			- DONE: fix "can't unlock door w/ fist" error on unlock door w/ hand empty
				- DONE: start fix at line 167 in interp - separate 'lock', 'unlock' cases from 'attack'
			- DONE: clean-up interp()
		- DONE: figure out how to update creature.hand vs. inventory to reduce un-fun friction
			- IDEA: I want the outside world to see what's in creatures hand (e.g. goblin holding axe)
			- IDEA: but I don't want player to need to think about inventory mgmt
			- IDEA: if the player specifies the obj and it is in inventory but not in hand:
				- IDEA: auto move the obj to hand and then perform action
			- DONE: final decision on whenther 2-word ['drop', 'eat', 'wear'] case = one-off or swap hand
			- DONE: sort out 2-word case
				- DONE: review / refine drop()
				- DONE: one-off solution to 'eat' (similar to 'drop')
					- DONE: update eat() in item()
					- DONE: update eat_err() in error()
					- DONE: test
				- DONE: one-off solution to 'wear' (similar to 'drop')
					- DONE: update wear() in item()
					- DONE: update wear_err() in error()
					- DONE: test
			- DONE: core troubleshooting
				- DONE: sort out debug_poke53281,0
					- FINDING: ',' no longer usable due to cmd queue - switched to 'debug_xyzzy'
				- DONE: sort out 'unlock gate with key' from entrance w/ empty hand
					- FINDING: was just a remnant from the 'debug_poke53281,0' error
			- DONE: sort out prep case
				- CANCEL: in validate() check for item not in hand but in backpack; if so, put_in_hand()
					- FINDING: this won't work - 'with' assumptions in interp(); try interp()
				- DONE: step back and think how I want this to work for specified obj not in hand
				- DONE: in interp() (pre-return) chk for item not in hand but in bakp; if so, put_in_hand()
				- DONE: test lock, unlock, unlock, drink, attack
				- DONE: test put, show, give
				- DONE: sort out initial 'get key' score (elim and double open gate score?)
				- DONE: customize put_in_hand() for bkpk case to avoid weight check				
				- DONE: update chk_bkpk() to deal with obj in portable containers (e.g. biscuit in bag)
					- DONE: investigate obj.chk_contain_lst() used in room.chk_contain_item()
					- FINDING: obj.chk_contain_lst() does not appear to exist
					- FINDING: get_contain_lst() exists, and chk_contain_item() exists...
					- FINDING: but chk_contain_lst() appears to be a masked error
					- DONE: determine test for get_contain_lst()
						- FINDING: no good test - issue is addressed at remove level
					- CANCEL: clean-up room.chk_contain_item() that fails due to above error
					- DONE: fix room.chk_contain_item()
					- DONE: test to confirm fix
					- DONE: extend room solution to backpack for portable containers
						- DONE: overhaul chk_in_bkpk() and bkpk_lst_remove() to ref sub-containers
						- DONE: test drop(), eat(), wear()(
						- DONE: troubleshoot verbs w/ bag & biscuit
			- DONE: Additional fixes for moving to general inventory
				- DONE: end-to-end review of obj & lbs moving between rooms, containers, and creatures
					- DONE: dee dive into Identity
						- IDEA: do we really need get_contain_lst() ?
						- IDEA: better understand Interactive contain_lst_remove()
						- DONE: make worn_lst_remove() container aware
						- DONE: make hand_lst_remove() container aware
						- IDEA: enable concept of Creature item_inventory ?
					- DONE: deep dive into Room
						- IDEA: get_take_all_lst() & get_mach_lst() stay unique to room
						- IDEA: extend chk_is_vis() & chk_wrt_is_vis() to all receptacles
						- IDEA: elim is_obj_on_floor() ?
					- DONE: deep dive into Interactive
						- IDEA: sort out weight calc (=> burt wt == sum of inv wt) ??
						- IDEA: elim is_empty() ?
						- IDEA: make chk_wrt_is_vis() & chk_is_vis() universal / Identity methods?
							- IDEA: extend to Creature ?
					- DONE: deep dive into Creature
						- DONE: hand_lst_remove => 2 levels
						- DONE: chk_in_hand => extend to 2 levels
						- IDEA: put_in_hand => move weight error to error_class? Add worn to weight chk?
						- IDEA: hand_is_empty() and bkpk_is_empty() => unify w/ Interactive is_empty() ?
						- IDEA: shift 2_word hand approach to prep / interp method for drop, eat, wear ?
						- DONE: chk_is_worn() => increase to 2 lvls deep
						- DONE: chk_contain_name() => increase to 2 lvls deep ?
					- DONE: deep dive into Item
						- IDEA: move increment_weight & decrement_weight to portable container? (prob not)
						- IDEA: take()
							- CANCEL: move "worn remove" buff to sep worn_remove_disp method? (stowe, drop)
							- IDEA: move "heavy load" buff to put_in_hand() ?
						- IDEA drop()
							- IDEA: eliminate local bkpk_remove() call / enable auto-hand-trans
							- IDEA: enable for port_cont
						- IDEA: stowe()
							- IDEA: enable for port_cont
						- IDEA: eat()
							- IDEA: eliminate local bkpk_remove() call / enable auto-hand-trans
							- IDEA: enable for port_cont
						- IDEA: drink()
							- IDEA: enable auto-hand-trans
							- IDEA: no concern about port_cont
						- IDEA: wear()
							- IDEA: eliminate local bkpk_remove() call / enable auto-hand-trans
							- IDEA: enable for port_cont
					- DONE: where to start?
						- DONE: chk_in_hand & hand_lst_remove
							- DONE: test: hold bag in hand, put biscuit
							- DONE: update chk_in_hand() to be 2-levels deep (like chk_in_bkpk() )
							- DONE: update hand_lst_remove to be 2-lvls deep (like bkpk_lst_remove )
							- DONE: test: hold bag in hand, put biscuit
							- DONE: test weight change
							- DONE: update doc
						- DONE: misc fixes
							- DONE: fix 'help verbs' works but 'help travel' fails
							- DONE: fix game 1
						- DONE: standardize port_cont remove in bkpk_lst_remove to match hand
							- DONE: remove gs attrib
							- DONE: test put biscuit from bkpk
						- DONE: chk_is_worn() & worn_lst_remove()
							- NA: can't test because have no clothes with pockets
							- DONE: update chk_worn() to be 2-levels deep (like chk_in_bkpk() )
							- DONE: update worn_lst_remove to be 2-lvls deep (like bkpk_lst_remove )
						- DONE: expand prep case to include worn
							- DONE: add baseball_cap to entrance
							- DONE: pre-test
							- DONE: add full 'if' statements for chk / remove worn (both dirobj & noun)
							- DONE: test gen
							- DONE: test burt wt
							- DONE: test put to see if remove disp is triggered
							- DONE: address remove disp in 'if'; add "(removing the X first)"
							- DONE: test put to see if remove disp is triggered
						- DONE: convert relevant 2_word cases to prep strategy
							- DONE: drop
								- DONE: update interp 2_word case
								- DONE: update drop() method in item()
								- DONE: test verb, lvl2, & wt
							- DONE: stowe (from worn only)
								- DONE: update interp 2_word case for worn
								- NA: update stowe() method in item() [bkpk never in scope]
								- DONE: test verb and wt handling
							- DONE: wear 
								- DONE: update interp 2_word case (bkpk only)
								- DONE: update wear() method in item()
								- DONE: test verb, lvl2, & wt
							- DONE: eat
								- DONE: update interp 2_word case
								- DONE: update wear() method in item()
								- DONE: test verb, lvl2, & wt
							- DONE: re-test drink prep verb
							- DONE: remove baseball_cap from entrance
					- DONE: decide if sword glows in backpack?? (probably yes if 'hand' de-emphasized)
						- DECISION: yes
			- DONE: dangerous scenarios
				- IDEA: burt should attempt to auto-draw a weapon when threatened
					- IDEA: also the special nature of weapons in general needs to be highlighted
					- IDEA: provide disp text any time burt draws or sheaths a weapon
				- IDEA: do I want weapon-draw disp if sword just passes through burt's hand from bkpk?
					- IDEA: e.g. sword in bkpk and burt uses 'put' or 'drop' or 'give'
					- DECISION: No, causes confusion; sword disp only if turn ends w/ sword in hand
					- IDEA: also, I don't want weapon-sheath disp if sword just passes through hand
					- IDEA: ony want weapon-sheath disp if weapon was actually 'drawn'
				- DONE: update general weapon disp behavior
					- IDEA: "whenever player 'take's weapon => "You are armed and dangerous!"
					- IDEA: "whenever player drops / stowes a weapon => "You look a bit more approachable."
					- CANCEL: update 'take' weapon disp
					- IDEA: I have a weapon-sheath disp problem: how to know if weapon was drawn?
						- IDEA: maybe need a core value for last_turn hand contents???
					- IDEA: also, I have a weapon-sheath disp scalability issue
						- IDEA: there is only one way anything goes into burt's hand ('take')
						- IDEA: but many ways it could leave ('drop', 'stowe', 'put', 'gvie')
						- IDEA: and there could be more ways in the future - don't want disp code for all
						- IDEA: actually, it worse than this because there are now many way to draw weapon
						- IDEA: what if burt attempts to 'unlock' door with sword and now has it in hand
						- IDEA: need a way to compare hand contents at end of each turn?
						- IDEA: where to do this? must run if error or cmd_exe... validate is too soon...
						- IDEA: yes - I think I need a dedicated call in app_main() to enable
						- IDEA: weapon_disp() called between cmd_exe() and post_act()
					- CANCEL: solve weapon disp
					- CANCEL: update weapon disp for 'drop', 'stowe', 'put', 'give'
					- CANCEL: update weapon disp for put_in_hand()
				- DONE: solve draw-weapon to hand for "attack X with <weapon>" case
					- DONE: in app_main(), get start_in_hand at same time as incrementing move
					- DONE: create disp_weapon() function in app_main w/ gs & start_in_hand attribs
					- DONE: call disp_weapon() between cmd_exe() and post_act()
					- DONE: test 'take' case for draw
						- FINDING: score buffers in cmd_exe before draw text
					- DONE: test 'drop' & 'stowe' case for sheathe
					- DONE: test unlock, show, give from bkpk case for draw
						- FINDING: doesn't work because hand is updated in interp()
						- IDEA: move start_in_hand to before interp()
					- DONE: test 'take X' for sheathe
					- DONE: test put from bkpk for no buffer
				- DONE: solve auto-draw weapon for burt attacks goblin case
					- IDEA: "(Sensing imminent combat, you draw a weapon)"
					- IDEA: bake draw weapon into interp() (v.s. auto use what's in hand)
					- IDEA: useful existing methods: in_hand_is_weapon(), is_weapon()
					- DONE: add as first if statement if 'with' not specified for 'attack'
					- DONE: test attack hand empty, no sword
					- DONE: test attack hand full, no sword
					- DONE: test attack with cheese, key in hand
					- DONE: test attack with fist, key in hand => stowe key, attack with fist, hand empty
					- DONE: test attack sword in hand
					- DONE: test attack hand empty, sword in bkpk
					- DONE: test attack hand full, sword in bkpk					
					- DONE: test attack 'with cheese'
					- DONE: test attack 'with sword'
					- DONE: test attack 'with fist'
					- DONE: test attach hedgehog while both sword & axe in bkpk
			- DONE: clean-up item handling methods
				- DONE: capture weapon disp updates on diagram (especially 'give')
				- DONE: detailed review of inventory management notes / fix opportunities
					- DONE: Creature class
						- DONE: remove_item() calls hand_lst_remove, bkpk_lst_remove, & worn_lst_remove
							- DONE: all 3 now portable container aware
							- DONE: all 3 are hero_wt and port_c_wt aware
						- DONE: Creature first pass
						- DONE: interim game test
						- DONE: Creature deep-dive
							- DONE: updated creature.remove_item() to be container aware ()
							- DONE: decided no need creature.is_empty() [similar to container]
							- DONE: decided not to attempt to integrate hand_is_empty() and get_hand_item()
								- IDEA: None value for get_hand_item() is often not useful
								- IDEA: usually want to take an action / buffer only if hand item exists
							- CANCEL: in creature, consolidate if hand_empty() => None else get_hand_item()
						- DONE: more testing
						- DONE: Creature final clean-up
					- DONE: Interactive class
						- DONE: update Container.remove_item() to be level-2 aware
						- DONE: decide to keep Container.is_empty() as standard call (even though not used)
						- DONE: testing
						- DONE: clean-up Interactive
					- DONE: Room class
						- DONE: elim is_obj_on_floor() => chk_contain_item()
						- DONE: test
						- DONE: elim floor_lst_extend()
						- DONE: test
						- DONE: sort out room.remove_item()
							- IDEA: there is a need for a simple, visibility-independent chk_contain_item()
							- IDEA: but there are also cases where chk_contain_item() is mis-used:
								- IDEA: in these cases it is treated as deep inventory check:
									- FINDING: ObjInInvCond(), take_err(), take()
							- IDEA: also, should pre-fix obj.check_contain_item() w/ obj.is_container()
							- DONE: document chk_contain_item() as single level
							- DONE: create chk_item_in_inv() universal method that goes deeep
								- DONE: probably first need to create get_top_lvl_inv_lst()
								- DONE: Identity => False
								- DONE: Room
									- DONE: new mehtod
									- DONE: second is_container() is not contributing - remove
								- DONE: Creature
								- DONE: Interactive
							- DONE: update room.remove_item() based on use of chk_item_in_inv()
							- DONE: test
							- DONE: review chk_contain_item() & update w/ is_container / chk_item_in_inv()
								- DONE: Cond class
								- DONE: Creature class
								- DONE: Error class
								- DONE: Identity class
								- DONE: Interactive class
								- DONE: Item class
								- DONE: Room class
							- DONE: also check for mis-use of get_vis_contain_lst() => get_inv_lst()
								- DONE: interp() 
								- DONE: creature()
									- DONE: create get_inv_lst() for identity, creature, interactive, room
									- DONE: review / update chk_item_in_inv() based on get_inv_lst()
									- DONE: update creature.has_weapon() code w/ get_inv_lst()
									- DONE: update creature.get_weapon() code w/ get_inv_lst()
									- DONE: test
									- IDEA: get_vis_contain_lst() more appropriate than get_inv_lst()
									- IDEA: (for has_weapon / get_weapon)
									- IDEA: because shouldn't be able to draw weapon in closed container
									- DONE: revert has_weapon / get_weapon
								- IDEA: do get_inv_lst and chk_inv_lst enable access to locked containers?
								- IDEA: need to tune for visible (i.e. not in closed containers)
								- DONE: refactor inventory methods:
									- DONE: interactive.get_inv_lst()
									- DONE: interactive.chk_inv_lst()
									- DONE: creature.get_inv_lst()
									- DONE: creature.chk_inv_lst() [ => in get_inv_lst() ]
									- DONE: room.get_inv_lst()
									- DONE: room.chk_inv_lst() [ => in get_inv_lst() ]
							- DONE: re-do mis-use check on get_vis_contain_lst() => get_inv_lst()
								- DONE: interp()
								- DONE: creature() [has_weapon() / get_weapon() ]
								- DONE: error, identity, interactive, room
								- DONE: test
									- DONE: 'get all' with postbox closed => 'can't see cert'
									- DONE: biscuit in bag in postbox: take biscuit => 2x biscuits
										- DONE: print for room.remove() [prints]
										- DONE: print for interactive.remove() [does not print??]
										- DONE: print to prove that interactive.remove_item() is running
										- FINDING: appears biscuit is in postbox??
										- DONE: investigate results from put() => not put() fault ??
										- DONE: problem appears to be not using copy() in get_inv_lst return
										- DONE: now I'm getting an error on 'get biscuit' and get fails
										- DONE: comment out interactive.remove troubleshooting prints
										- DONE: search on all uses of list.extend()
									- DONE: 'drp all','get rck','stowe rck','drp rok','get all except rck'
									- DONE: get biscuit from bag in postbox
									- DONE: general test
										- DONE: fix can't read or examine scroll while seated in throne
									- DONE: one final full-game test
				- DONE: review Identity / Universal ideas
					- DONE: review value of elim get_contain_lst()
						- DONE: interactive()
							- DONE: update
							- DONE: test
						- CANCEL: map()
							- FINDING: get_contain_lst() has value of its own; see Identity comments
						- DONE: test
				- DONE: clean-up all classes and methods!
				- DONE: full test
				- DONE: document the definition of accessable inventory:
					- IDEA: with the elimination of 'hand', need to know what items a creature can access
					- IDEA: this is distinct from obj that are visible in 2 ways:
						- IDEA: 1) it only relates to items
						- IDEA: 2) it assumes access to all items (because it is the creature's inventory)
						- IDEA: an obj in a closed container is not acceessable
						- IDEA: inventory relates to creatures therefor is needed for Interactive & Creature
						- IDEA: room.inventory has also been created but may be superfluous???
				- DONE: update 'help hand' to explain inventory concepts
				- DONE: test cup of tea
				- DONE: update sword glow narrative for crocodile encouters
					- DONE: update condition to determine if shiny_sword is in hand
						- DONE: create sword_in_hand_cond and update temp attribs
						- DONE: comment out old cond & result
						- DONE: create new combo cond: [sword_in_hand, crown_not_dispensed]
						- DONE: create new result: moat_get_crown_result2 and update temp attribs
						- DONE: create text for get_crown_result2
						- DONE: run game_update
						- DONE: test => not running sword result when holding sword; print chk_cond()
							- DONE: try printing mach name and full cond & result lists
							- FINDING: wrong cond names caused the problem; I am surprised
		- CANCEL: general ideas
			- DONE: now prep case works with portable containers but 2-word does not - fix
			- DONE: extend hand => bkpk to worn items?			
			- CANCEL: address minor issues / redundancy / naming
			- CANCEL: restructure 2_word cases
			- CANCEL: generalize item handling across receptacles; use creature inventory approach
			- CANCEL: next steps to consider
			- CANCEL: tons of testing!!
	- INPROC: room 4
		- DONE: immediate fixes:
			- DONE: correct 'stowe' command to 'stow'
				- DONE: search on 'stowe' and replace with 'stow'
				- DONE: test
		- INPROC: in-depth walk-through of Throne Room
			- DONE: de-dup passage descriptions vs. base description
			- DONE: de-capitalize all nouns (except rooms)
				- DONE: throne_room
				- DONE: throne
				- DONE: crystal_box
				- DONE: calligraphy
				- DONE: family_tree
				- DONE: stone_coffer
				- DONE: kinging_scroll
				- DONE: silver_key
				- DONE: illuminated_letters
			- DONE: add all referenced nouns
				- DONE: pedestal (late romantic period)
				- DONE: windows
				- DONE: silver_keyhole => move silver sword hint here
				- DONE: stained_glass
				- DONE: make paths examineable
			- INPROC: additional review
				- DONE: test all machines
				- DONE: use init_desc where appropriate
					- DONE: pedestal to right
						- DONE: create init_desc obj
						- DONE: create init_desc description
						- DONE: add to room
					- DONE: coffers to left
						- DONE: create init_desc obj
						- DONE: create init_desc description
						- DONE: add to room
					- DONE: test (fix unable to get obj in coffer? )
					- DONE: try re-aranging examine order to show init obj before paths
						- DONE: move paths from room.cond_disp() to room.contain_disp()
						- IDEA: this is good prep for linking room.cond to lighting
						- DONE: testing to get spacing right
						- DONE: final testing (including cup_of_tea)
						- DONE: clean up room_class() and fully comment parts of disp_contain()
						- DONE: update antechamber_post_goblin descript w/ control panel in sep line
			- DONE: problem-solving
				- DONE: make pedestal into true surface (enables error on attempt to put obj on it)
				- DONE: enable "the box is firmly affixed to the pedestal" warning on attempt to take box
					- DONE: enable warning
					- FINDING: now, the crystal_box condition is no longer highlighted... how to fix?
					- CANCEL: maybe just put crystal_box in floor_lst & elegant_pedistal max_obj = 0
				- DONE: use warning to divert attempts to pick up stained_glass (mention melted)
				- DONE: create highlight attrib for init_desc
					- IDEA: if highlight == True, don't remove from view_only_lst
					- DONE: implement for elegant_pedestal in throne_room
				- CANCEL: use init_desc w/ control_panel in antechamber ?
					- DECISION: tempting out of "purity of design" but nt better than current approach
			- DONE: review / play-through existing noun descriptions
				- DONE: fix 'walk into wall' error
					- FINDING: problem appears to be in map.chk_valid_dir()
					- DONE: re-write as nested for loop and add print statements to troubleshoot
					- FINDING: walk-into-wall error is gone but now moat_mach doesn't run??
					- DONE: try reversing for loop order
					- FINDING: same exact behavior
					- DONE: revert to original for loop order
					- DONE: test orginal return code
					- FINDING: same failure as orignal => poor test; running for loops twice
					- DONE: confirm that return value is as expected
					- FINDING: go_err() appears to return is_att == True
					- DONE: chk app_main() for go special case?
					- FINDING: no go special case but cmd_override is evaluating to False (wrong)
						- NOTE: is_val == F, is_att = T
					- DONE: fix cmd_override
						- FINDING: cmd_override passed by InvisTrigMach.run_mach()
						- FINDING: die_in_moat_result.cmd_override == True
						- DONE: review AutoMachMixIn.run_mach => check EndResult.result_exe()
					- DONE: jump into the world of AI Troubleshooting!
						- FINDING: today was very different, aws q helped me troubleshoot
						- NARATIVE: the basic issue was that map.chk_valid_dir() was not really functioning correctly all this time. When I fixed it - suddenly the path not being valid broke the is_valid_req for the WeaponInHandCond class and I could no longer die by going off the drawbridge. After a week of manual troubleshooting, I called in q and they were amazing! They found and fixed the issue in on sitting. 
						- Q's Explanaation: 	
							"The code is now clean and the fix is in place:

							Root cause: The no_weap_in_hand_cond was failing because is_valid = False (invalid command) and is_valid_reqd = True (default), so TrueCond.cond_check() returned False before checking the weapon condition.

							Solution: Set is_valid_reqd=False for no_weap_in_hand_cond so it evaluates even when the command is invalid.

							Implementation: Added **kwargs support to WeaponInHandCond constructor to accept the is_valid_reqd parameter and pass it to the parent TrueCond class.

							Now when you go east from the Entrance without a weapon, cmd_override correctly evaluates to True, triggering the death result as intended."
					- DONE: new fixes
						- DONE: probably the q fix means I don't need pretend rooms anymore?
							- NOTE: i think I got rid of these already - double check this
							- FINDING: confirmmed... I got rid of the fake rooms a while ago
							- FINDING: this was the double error that got me:
							- FINDING: rooms removed while map.chk_valid_dir() wasn't working right
						- DONE: review existing is_valid_reqd state for iron_portcullis
							- F: true_cond_valid_not_reqd of class TrueCond has is_valid_reqd = False (me)
							- F: no_weap_in_hand_cond of class WeaponInHand has is_valid_reqd = False (q)
							- DONE: add **kwargs (2x) to all Condition classes
							- DONE: figure out how to pass is_valid_reqd = False for compound cond
								- FINDING: in AutoMachMixIn.run_mach() , both cond must just eval True
							- DONE: solve moat with weapon (first try) case
							- DONE: solve moat with weapon (repeat) case
							- DONE: test all moat cases
						- DONE: mach is_valid_reqd fix-it
							- FINDING: today, the is_valid_reqd bool lives in machine conditions
							- FINDING: bool refers to *triggers* which are hardwared to the mach
							- IDEA: need to move is_valid_reqd to machine level
							- IDEA: this will simplify conditions and condition evaluation
							- IDEA: make is_valid_reqd a bool attrib of ProtoMachMixIn
							- IDEA: in pre_act(), pass is_valid_reqd to trig_check() and test there
							- DONE: ask Q if she agrees with approach => Q agrees!
							- Q_REC: The implementation would be:
								- Add is_valid_reqd to ProtoMachMixIn
								- Update trig_check() to handle the validation logic
								- Modify pre_action() to pass is_valid to trig_check()
								- Clean up all the **kwargs from the condition classes
								- Update your machine definitions to use the new parameter
							- DONE: work w/ Q to move is_valid_reqd to machine trigger level
								- DONE: **kwargs / is_valid_reqd = True added to ProtoMachMixIn
								- DONE: update trig_check() and pre_act(), post_act(), auto_act()
								- DONE: add is_valid_reqd as attrib for moat_mach(), goblin_attack() 
								- DONE: elim is_valid from run_mach() and cond_check() ??
								- DONE: goblin_attack_mach() true_cond_no_valid_reqd => true_cond ??
								- DONE: testing
									- FINDING: invalid cmds (entrance go e, antichamb go n) failing
									- DONE: troubleshoot w/ Q => I had forgotten to run game_update()
									- DONE: test cup_of_tea()
					- DONE: clean-up app_main() and map_class() and others
				- DONE: update is_valid_reqd in doc.md
		- DONE: general
			- DONE: search on all room names to ensure consistently capitalized
			- DONE: review final title => king vs. baron
			- DECISION: should obj.full_name be de-captialized? => YES
			- DONE: clean up cleesh static_gbl, clean-up game_static_gbl
		- INPROC: additional fixes (ask q for help):
			- DONE: make inventory description text rare (20%?)
				- DONE: review 'score' and 'title' to see how to buff dict within dict
				- DONE: put descriptions in dict in game_static_gbl (key = #, value = txt)
				- DONE: use len(hero_descript_dict) to get hero_descript_count
				- DONE: rename core.hero_descript_count => core.hero_descript_pct
				- DONE: in base_class() rand_max = ((1/hero_descript_pct) * hero_descript_count)
				- DONE: get dict_val; e.g. title = gs.io.get_dict_val('titles_by_score', title_score)
				- DONE: in base_class() use 'try' with buff_f() to enable default response
				- DONE: test DC
				- DONE: Test Cup of Tea
				- DONE: check in with Q
				- DONE: clean up old hero descriptions in game_static_dict
				- DONE: clean up gs.core(), both game_updates(), base()
			- DONE: improve item listings for 'l' (with Q!):
				- DONE: ensure that portable container contents are listed with port container "()"
				- DONE: use and between 2nd to last and last item
				- DONE: use a and an for single items
			- DONE: improve rest of 'l' UI
				- DONE: fix articles for view_only listings
				- DONE: fix articles for passages
				- DONE: test
				- DONE: clean-up map
			- INPROC: improve 'contain' UI (e.g. bag and coffer)
				- DONE: articles
				- DONE: and pattern
				- DONE: port-contain contents in parenthesis (e.g. bag in coffer)
				- DONE: testing
					- DONE: intantiate larger lidded container and port container in Entrance
					- DONE: detailed testing w/ x and l
				- DONE: fix pre-list of port containers
				- DONE: add articles for port_containers in containers (use full for-loop)
				- DONE: generalize display list w/ view_only.get_disp_str()
				- DONE: fix look w/ cheese in shoebox in box
				- DONE: fix look w/ empty shoebox in box
				- DONE: clean-up ContainMixIn disp_contain()
				- DONE: re-use get_disp_str() in room for items
				- DONE: re-use get_disp_str() in room for view_only
				- DONE: test on special case of l / x while in seat
				- DONE: rename viewonly.get_disp_str() => get_disp_sub_str()
				- DONE: create viewonly.get_disp_str()
				- DONE: call get_disp_str() from Interactive.disp_contain() ?
				- DONE: call get_disp_str() from room.disp_contain() [view_only & items] ?
				- DONE: extend UI to i / creature.disp_contain
					- DONE: hand
					- DONE: backpack
					- DONE: worn
					- DONE: test
				- DONE: clean-up Interactive, view_only, room, creature
				- DONE: text cup_of_tea
				- TBD: full test of dc3
				- TBD: final playthrough room 4 to make sure it all works together
		- INPROC: minor features:
			- INPROC: implement 'jump' (jump on drawbridge in Entrance = go over side ?)
				- DONE: test play 'jump' cmd in Zork; test at chasim too
					- FND: non-dangerous responses
						- FND: "Wheeeeeeeeeee!!!"
						- FND: "Are you enjoying yourself?"
						- FND: "Do you expect me to applaud?"
						- FND: "Very good. Now you can go to the second grade."
					- FND: dangerous response
						- FND: "This was not a very safe place to try jumping. Geronimo..."
				- DONE: implement standard response for creature.jump() (hero & other)
					- DONE: create creature.jump()
					- DONE: in staic_gbl(), add 'jump' to 'one_word_convert_lst'
					- DONE: in staic_gbl(), add 'jump' to 'known_verbs_lst'
					- DONE: in interp() create routine for 'jump'
					- DONE: create jump_err() method in error_class()
					- DONE: test in game (including while seated)
					- DONE: test 'help one-word-commands'
				- DONE: implement modular machine to alter jump behavior on drawbridge
			- DONE: clean up test obj
- DONE: git merge
	- DONE: 'git checkout master' to switch focus to master
	- DONE: 'git branch: to confirm focus
	- DONE: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
	- DONE: 'git push' to push merge to origin (GitHub)
	- DONE: confirm that origin is updated
	- DONE: confirm that code is updated and still runs
	- DONE: 'git branch -d <FEATURE_NAME>' to clean-up local branch
	- DONE: 'git push origin --delete <FEATURE_NAME>' to clean up origin
	- DONE: confirm origin is cleaned up
	- DONE: post-branch-delete run test

############################
### CLEESH VERSION 3.8.1 / DARK CASTLE VERSION 3.2.0 END ###
############################


*** what's next? [INTERIM UPDATES ON MASTER - BUILD 14] ***
- DONE: move to-do to done
- DONE: update game version
- DONE: update cleesh version
- DONE: test version updates
- DONE: quick fix - correct double buffer on 'eat cheese'
- DONE: review backlog and choose next goal
- DONE: decide on next target => mvps / done / cancel
- DONE: creat branch
- DONE: more frequent merges!!

