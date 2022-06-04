To Do List - Dark Castle v3
May 8, 2022


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl

	
*** NOTES ***

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
- INPROC: create hedgehog_distracted_mach (if timer active, inhibits show & give)
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
	- INPROC: Machine
		- DONE: instantiate hedgehog_distracted_mach
		- DONE: add hedgehog_distracted_mach to royal_hedgehog
		- DONE: run mk_def_pkl()
		- TBD: testing! [appears that list_of_lists loop is not working as expected => use enumerate() for indexes!!]
	- TBD: Update Warning class trig_check() to work with wildcards

##########################
### VERSION 3.66 START ###
##########################
Version 3.66 Goals
- Create conditions, results, and read_scroll machine

- TBD: should the shiny_sword vanish after being given to the royal_hedgehog?
	- IDEA: sure - but maybe in the end scene, the hedgehog places it before Burt's feet and kneels?


##########################
### VERSION 3.68 START ###
##########################

Version 3.68 Goals
- Clean up creature, machine, warning, and timer coding
- Create / update program documentation

- TBD: Machine coding clean-up
	- TBD: Machine 2.0 improvement ideas:
		- Have simple, single-test / single-action 'Primative' Conditions and Results: prim_cond and prim_result
		- Composed Conditions & Results: comp_cond / comp_result == AND / OR of multiple primatives
		- All results capable of Buffering (rename Result classes appropriately)
		- if no conditions == True then default Result = nothing happens (no need for pass_result)
		- Establish switch triggers such that timer as trigger is more natural
		- Generalize in-hand vs. not-in-hand Condition (single primative)
		- Generalize creature-has-item vs. creature-does-not-have-item Conditions (single primative)
		- Establish clearer nomenclature for temp variables that will be fully assigned at end (e.g. 'royal_hedgehog-*temp*')
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

##########################
### VERSION 3.7x START ###
##########################

Version 3.7x Goals
- Refactor code
- Unit Testing (link: https://youtu.be/6tNS--WetLI )
- Introduce non-functional requirement code (e.g. saves and obj clean-up)
- Migrate to web


##########################
### VERSION 3.7x START ###
##########################
Version 3.8x Goals
- New rooms and puzzles!!



*** Timer Decisions ***
- timers are set by machines rather than triggered by player commands
- other than providing description text, timers are dumb - they just count -  a machine takes all actions

*** Future obj Ideas ***
- timers as obj
- 'warnings' as obj


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
TBD: learn about Super()
TBD: read this article: https://sangeeta.io/posts/a-super-post-on-python-inheritance/
TBD: extend child methods in results_class_def ?
TBD: Jenkins integration to automatically update "v3 alpha" tab with latest commits?
TBD: list of 'contained' internal_switches in MachMixIn attributes?
	NOTE: (i.e. add to scope and remove levers & button from features?)
	NOTE: [this is a good idea but hold off until at least one more control_panel type machine gets created]
TBD: re-name 'wrapper' to 'app_main'
TBD: update pickle names
TBD: out_buff => output (or possibly user_output)
- Burt as an object?? (allows elimination of attack_burt() method of Creature class)
- How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away
- possibly rename modules to indicate usage first? i.e. creature_class_def.py => class_def_creature.py ???
- in machines, should conditions and results just be key-value pairs in a dictionary?
	- As opposed to needing 2 separate lists with identical indexes?
- Can I just set descript_key for Note in mk_def_pkl() with setter rather than whole dynamic_dict?
TBD: what should happen if Burt tries to take the axe from a living goblin? (general case)
	i.e. should creatures have a visible_inventory_lst that is part of examine scope?
TBD: auto_static_behavior for goblin? (e.g. "the goblin is eyeing you coldly") each turn - maybe should be a standard function??
TBD: no swearing in Dark Castle (with warning or else end of game)
TBD: sort out more elegant assignment process for self referenced obj (e.g. re-assigning goblin to goblin_mach after goblin Creature instantiation)
TBD: elim hasattrib() in active_gs scope checks => is_cont(), is_mach(), is_creature() methods within classes
- DONE: introduce pre-built "warning" machine? use for 'go south', 'attack hedgehog', 'lift heavy rock', etc
- does creature_state really have any value? Maybe build hedgehog before pulling the plug on this one
- change hand from list to string
- cursing => end of game (requires warning_mach and usniversal scope)
- lantern (requires darkness travel tracker, timer, item_mach, univeral scope, death by grue)
- game saves (requires file clean up?)
- encumberance (post Burt as object?)
- implement carying capacity / container cappacity; Also carry restriction passages, etc..
- move doc to modules?
- org modules in directories?
- create vehical puzzle?
- eliminate active_gs.move_dec() ?
- why do I need active_gs.dynamic_descript_dict again?
- investigate setters & getters for GameState class
- move switch_reset to auto_action() ???
- is there really any need for GameState room_mach_lst() ??
- 'trigger_type' => 'trig_type' ??
- 'try... except' standard descriptions for examine() method (similar to Warnings)
- review how creatures vs. items appear in DCv2 - mimic?
- 'g' as abbreviation for 'again' ?
- for command-driven machines - especially pre-action - would like to have a systemic way to know if player command runs successfully
- Do a refactoring code review (look into the 'any' command in place of for loops)


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
