To Do List - Dark Castle v3
Oct 22, 2021


*** How to Add Objects ***
1) If needed, create Class and methods in dc3_classes
2) Instantiate object in mk_default_pkl()
3) Add object to room in mk_default_pkl()
4) Add object to master_obj_lst in mk_default_pkl()
5) Run mk_default_pkl()
6) Add object description in dc3_static_init


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
TBD: map object attributes, verb methods, and inheritance visually
TBD: re-map modules
TBD: map import dependencies

	
##########################
### VERSION 3.50 START ###
##########################

Version 3.50 Goals
- Room Events (pre-action trigger) - maybe using exec()
- implement scoring


### Timer Events ###
- have a lantern that dimms over time
- references to Zork Brass Lantern
- Provides a timer based trigger that can be inspected each turn (not directly based on Burt actions)



CLASS IDEAS:

### Cutscene ###
-  events: conditional-command-list, conditions (list of lists; outer = AND; inner = OR), event-text, events (list); check for end of game in wrapper
IDEA: Conditional Cutscene Class
IDEA: Conditional_events (a class similar to dcv2 triggers??) => implement for moat ????
	- default, default description, default method
	- special event first time, seft_description, seft_method, count
	- special event additional times, seat_description, seat_method, count
	- track numbrer of times CE is run?
	- Or maybe just binary cond_event_exists in each obj?
	- also need to distinguish pre=action vs. post-action (e.g. 'take sword' vs. 'read lettering' or 'push button')
	- also need to distinguish 1-time events (e.g. croc) vs. every-time events ('take sword') vs. warnings (e.g. 'eat biscuits')

### Creature Class ###
### Switch Classes (button & lever) ###

More obj Ideas:
- timers as obj
- 'warnings' as obj

More ideas on Creatures:
- Treat creatures like roving conditional events
- Wrapper checks for presence of creature in room and checks for conditionals against creature too

Key Creature Verbs (methods):
- show, give, attack



HOW MACHINES SHOULD WORK:

levers, and button => and machines!
	Lever and Button objects
	Working portcullis puzzle

IDEA: Create Machine class
		- Complex machines have at least 2 inputs (vs. doors)
		- Control Panel is a machine (also throne, radio, and baking machine)
		- Have 'help machines'
		- Logic, outcomes, & descriptions live in machine - button just starts, levels just set values
		- Machine obj also includes list of 'controls' (3x levers and button)
		- (For fun, baking machine should have lever to start and buttons to set values)
		- Buttons & Levers are dumb
			- Levers only know if they are up and down and how many times pulled
			- Buttons only know if phushed this turn and how many times
		- Machine state is checked each turn in wrapper (similar to conditional events & creatures)
			- Machine checked based on room
		- Should logic be in machine or in attached conditional events??
	TBD: Create class LeverSetVal and objects left_lever, middle_lever, right_lever
		TBD: Create method pull()
			TBD: set lever value based on up or down (start down; down = 0)
	TBD: Create class ButtonToggleIfVal and object red_button
		TBD: Create method push()
			TBD: on push check value; if value then toggle state else nothing; descript text for success and fail
TBD: random responses to wrong direction commands ;-D
TBD: implement scoring



SOMEDAY MAYBE IDEAS:
TBD: Figure out a way in web browser to show all adventure text in scrolling window
TBD: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )
TBD: Try tupples for descript_dict
	NOTE: Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
- fun idea - small creature - like a mouse - as an item
- more directions
- landscape / path changes
- create 'win' test routine with checksum
- create a hint sub-system



NEW PUZZLE IDEAS:

### New Puzzle Ideas ###
- Can sharpen and clean sword in mouse hole - maybe only way to get past goblin
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
		find a use for the word "griffonage" (illegible handwriting)
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
