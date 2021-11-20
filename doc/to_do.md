To Do List - Dark Castle v3
Nov 13, 2021


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl()
5) Run mk_def_pkl()
6) Add object description in static_gbl

	
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
	IDEA: instead of counter, implement as got_crown = False => True

CANCEL: entrance_east_weap_repeat (full get item case with counter after first count)

NOTE: ending v 3.50 early... I have a new modular idea for how to implement machines (with TravelEffect as an invisible machine)


##########################
### VERSION 3.51 START ###
##########################

IDEA: machines should be modular... a bit like rooms

- Machine attributes [entrance east / west example]
		machine_type => pre_action_trigger
		machine_vars => [got_crown = False] *** or should this be a GameState attribute?? ***
		cmd_triggers_lst => [['go', 'go', 'east'], ['go', 'go', 'west']] => return True or False
		cmd_cond_lst =>
				[hand_no_weap, => return result 'die_in_moat'
				hand_weap_1st, => return result 'moat_get_crown'
				hand_weap_repeat] => return result 'moat_crocs_scared'
		resutl_lst =>
			[die_in_moat, => buffer message, active_gs.game_ending = 'death', return override == True
			moat_get_crown, => buffer message, active_gs.hand_lst_append(crown), got_crown = True, return override == True
			moat_crocs_scared] => buffer message, return override == True

- Machine attributes [entrance south example]
	machine_type => pre_action_trigger
	machine_vars => None
	cmd_triggers => [['go', 'go', 'south']]
	cmd_cond_lst => None
	result_lst => [cant_leave] => buffer message, return override == True


NEXT:
1) Think through pre_action_cmd function
2) What do the generic condition and result objects / methods look like?




TBD: create crown object
	TBD: create Hat class
	TBD: create crown obj
	TBD: create wear method
	TBD: create remove method
	TBD: update score for crown in hand
	TBD: Update active_gs to include 'worn' attribute
	TBD: Update inventory() function in cmd_exe() module to show 'worn' in inventory

TBD: documentation:
	TBD: write up thinking and decisions on interactive obj
	TBD: update class diagram
	TBD: update module diagram


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

IDEA: create a fun scenario where TravelEffect take item gets used... maybe a giant brid comes along and takes whatever's in Burts hand and scares him off until he carries a lead weight (or a heavy rock?) - which tires the bird out so much Burt can go in the room and get back his stuff and enter the room? Maybe this could be a room between main hall and antechamber that the maze / mouse hole is off of? Maybe nest is in corder of room of class Box (not open / close or lock / unlock).

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
