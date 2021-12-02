To Do List - Dark Castle v3
Nov 30, 2021


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl()
5) Run mk_def_pkl()
6) Add object description in static_gbl


##########################
### VERSION 3.54 START ###
##########################
Version 3.54 Goals
- Create class, methods, and obj for throne room throne machine

***** NEEDED UPDATES TO PLAN *****
= need to link switch to machine
- incorporate switch_state into trigger
- HOW DO I PASS SWITCH STATE TO CONDITIONS?


IN-PROC: update classes and types of pre and post actions
	DONE: pre_action_com.py module => pre_action.py
	TBD: pre_action_trig => pre_action_cmd_trig
	TBD: cmd_cond_lst => cond_lst
TBD create class ButtonSwitch  (child of ViewOnly)
	TBD: attributes = switch_state (values = 'pushed', 'pulled', 'neutral') and machine_type (values = 'pre_action_auto_reset')
	TBD: create method push (updates switch_state to 'pushed')
TBD: create class SliderSwitch (child of ButtonSwitch)
	TBD: create SpringLoadedSlider method pull (updates switch_state to 'pulled')
	TBD: update throne obj => SliderSwitch class with dark_castle2 description
TBD: update pre_action() to check for machine_type 'pre_action_auto_reset' and reset value
TBD: test throne slider
TBD: broach_dispensesr
	TBD: create broach_dispenser obj of class InvisMach
	TBD: machine_type = post_action_switch_trig
	TBD: machine_state = False (# broach_dispensed)
	TBD: cmd_triggers_lst = None
	TBD: cond_lst:
		machine_state = True => create MachStateCond class => create obj broach_dispensed
		switch_state = pushed => ???
		switch_state = pulled => ???
	TBD: result_lst = <BufferOnly, BufferOnly, ObjDispensedToRoom>
TBD: create post_action() module [very similar to pre_action()]
TBD: create broach obj of class Clothes and clothing type 'pin'
	TBD: Allow broach to be worn but hint in wear_descript and remove_descript that it's only of sentimental value
	TBD: update score dicts to grant 5 pts on broach in hand


IDEA: we could have more types of pre and post actions...
	- pre_action_trig => pre_action_cmd_trig
	- this allows for pre_action_state_trig
	- could also have a simple pre_action_state_reset which just resets a button or spring_loaded_slider to given default value (None)
IDEA: throne is the trigger. Is the machine invisible?
IDEA: throne obj is of class SpringLoadedSlider (child of ViewOnly)
	IDEA: has mehods push() and pull() and state
	IDEA: last_action_state can == 'pushed', 'pulled', 'neutral'
	IDEA: auto_pre_action resets state to 'neutral'


##########################
### VERSION 3.56 START ###
##########################
Version 3.56 Goals
- Create class, methods, and obj antechamber control_panel machine


##########################
### VERSION 3.58 START ###
##########################
Version 3.58 Goals
- Create class, methods, and obj for read_scroll machine

IDEA: Should GameState be in a separate module? 
	IDEA: gs_def.py ? class_def.py would import gs_def (?) - then mk_def_pkl.py would import from both?


##########################
### VERSION 3.59 START ###
##########################

Version 3.59 Goals
- Create / update program documentation

TBD: documentation:
	TBD: write up thinking and decisions on machines
	TBD: update class diagram
	TBD: update module diagram
	TBD: Create machine diagram


##########################
### VERSION 3.60 START ###
##########################
Version 3.60 Goals
- Create class, methods, and obj for goblin creature


##########################
### VERSION 3.62 START ###
##########################
Version 3.62 Goals
- Create class, methods, and obj for hedgehog1 (hungry_guard) creature


##########################
### VERSION 3.64 START ###
##########################
Version 3.64 Goals
- Create class, methods, and obj for hedgehog2 (key_trader) creature


##########################
### VERSION 3.66 START ###
##########################

Version 3.66 Goals
- Create / update program documentation

TBD: documentation:
	TBD: write up thinking and decisions on creatures
	TBD: update class diagram
	TBD: update module diagram
	TBD: update machine diagram
	TBD: create creature diagram



*** interactive object ideas ***

Ideas:
- 4 cases:
	- pre-action trigger
	- post-action trigger
	- pre-action auto
	- post-action auto

- simplest approach is long if-then-else list
	- pros: very flexible
	- cons: opaque, non-scalable
- next idea might be trigger obj associated with rooms or obj that have eval-uable conditions an results
	- pros: less opaque - you know something will happen
	- cons: more coding, essentially a distributed if-then-else
- alt approach: specific machines with specific conditions and actions
	- pros: much less opaque and predictable, create interactive world, standard re-usable object types, provides some creative constraints
	- cons: more coding, less flexible

IDEA: Still thinking through - do I want one TravelEffect obj per possible outcome? Or one per direction??
	- DEC: multiple conditions per TravelEffect but as few outcomes as possible

- interactive object types (class == IntObj ???)
	- travel_effects = pre-action trigger
		- results = buffer, ending, take obj from hand_lst, give obj to hand_lst
		- conditinos = hand_lst contains, event counter
	- machines = post-action trigger
	- creatures = pre-action trigger, post-action trigger, pre-action auto, post-action auto

- Perhaps rooms have an attribute of invis_obj_lst (list contains travel_effects) ?
- Perhaps invisible objects are of a class that wriiting inherits from??
- For inter_obj auto case, need scope_list in active_gs so that inter_obj always gets a turn - even when not in room


IDEA: taking another run at how machines should work
IDEA: machines should be modular... a bit like rooms
IDEA: instead of counter, implement as got_crown = False => True

Principles:
- if the cmd_triggers_lst matches the player command, a result should always be triggered (i.e. a condition should be true)
- conditions should be mutually exclusive => one and only one condition should be true at any one time
- machines should be attomic - they should keep track of their own state (e.g. got_crown)
- each machine will have trig_check() and trigger() methods called byt the pre_action_cmd method
- a triggered machine should always have a True condition that leads to a defined result
	- so the link between conditions & results should live attomicaly within the machine
- so pre_action_cmd will initially be very simple... but it may eventually become the home for pre_action_auto too
- a Creature is a collection of VewOnlyMach objs that enable it to respond to show, give, attack, and other stimuli
- Creatures should be no more complex than necessary
	- so when a specific creature need is met but a new creature behanvior will arrise =>
		- it may make sense to 'swap' in a 'new' creature of the same name
		- (e.g. hedgehog1 == hungry_guard, hedgehog2 == trader
		- presumably creature swap also happens via machine?

- Machine attributes [entrance east / west example]
		machine_type => pre_action_trigger
		machine_state => got_crown = False (Only 1 state per machine? Ppass to every condition?)
		cmd_triggers_lst => [['go', 'go', 'east'], ['go', 'go', 'west']] => return True or False
		cmd_cond_lst =>
				[hand_no_weap, => return result 'die_in_moat'
				hand_weap_1st, => return result 'moat_get_crown'
				hand_weap_repeat] => return result 'moat_crocs_scared'
		result_lst =>
			[die_in_moat, => buffer message, active_gs.game_ending = 'death', return override == True
			moat_get_crown, => buffer message, active_gs.hand_lst_append(crown), got_crown = True, return override == True
			moat_crocs_scared] => buffer message, return override == True

- Machine attributes [entrance south example]
	machine_type => pre_action_trigger
	machine_vars => None
	cmd_triggers => [['go', 'go', 'south']]
	cmd_cond_lst => None
	result_lst => [cant_turn_back] => buffer message, return override == True

Conditions and Results thinking:
- What do the generic condition and result objects / methods look like?
	- condition objects
		- not_in_hand_cond attributes = not_in_hand_lst; Returns True or False => hand_no_weap
		- in_hand_and_bool attributes = in_hand_lst, bool; Returns True or False => hand_weap_1st, hand_weap_repeat
- cond_return_lst = [] , for cond in cmd_cond_lst: cond_return_lst.append(cond_check(cond))
- result_num = return_list.index(True)
- trigger(result_lst[result_num])
	- result obj
		- buffer_and_ending attributes = result_descript, ending < can be None>, cmd_override <T/F> => die_in_moat, moat_crocs_scared
		- buffer_and_give = result_descript, give_item, cmd_override <T/F> => moat_get_crown
- machine variable updates => if result_num == 2: got_crown = True

Class Considerations:
- What class should machines inherit from?
- Some machines will be invisible, some will be features, and some will be items... so where to inherit from?
- Maybe a more important question is what class will MachCond and MachRslt inherit from?
- These should be usable by all Machine varieties... and should never be seen by the player...
- So MachCond and MachRslt should be children of class Invisible
- Then machines can inherit from the correct class: InvisMach, ViewOnlyMach, ItemMach

pre_action_cmd() Function Pseudo-Code:
- get inter_obj_lst and for each pre_action_trig: trig_check = trig_check() <return = T/F>
- if trig_check: cmd_override = trigger() <return = T/F>


### Cutscene ###

- Room Events (pre-action trigger) - maybe using exec()

### Timer Events ###
- have a lantern that dimms over time
- references to Zork Brass Lantern
- Provides a timer based trigger that can be inspected each turn (not directly based on Burt actions)


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



*** SOMEDAY MAYBE IDEAS ***

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
TBD: for doors and containers, use None option for no lock or no lid?
- extend BufferOnlyResult result_exe method in BufferAndEndResult and BufferAndGiveResult



*** NEW PUZZLE IDEAS ***

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

IDEA: create a jaunty_cap that makes Burt move twice as fast as everything else in the world - maybe essential for escaping the time travel ball?

IDEA: create a fun scenario where TravelEffect take item gets used... maybe a giant brid comes along and takes whatever's in Burts hand and scares him off until he carries a lead weight (or a heavy rock?) - which tires the bird out so much Burt can go in the room and get back his stuff and enter the room? Maybe this could be a room between main hall and antechamber that the maze / mouse hole is off of? Maybe nest is in corner of room of class Box (not open / close or lock / unlock).
- Make it a Wumpus Bat - a reference to Hunth the Wumpus and Adventure!!
- Takes an item from Burt's hand and sends him back the way he came to take cover; item is randomly placed in another (reachable) room
- Solution is to enter room carrying a heavy rock - Bat will take but leaves rock by its nest with a note "Tired out from lugging big rocks - leaving Dark Castle for a while to visit the Wumpus"
- Heavy Rock allows introduction of carrying capacity... playing can't carry *anything* else while carrying Heavy Rock
- some useful treasure found in the nest 
- Nest could be a container with open_state = None and lock_state = None

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
