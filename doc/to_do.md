To Do List - Dark Castle v3
Feb 9, 2022


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl


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
		- DONE: override run_mach with warn-specific code (buffer descript_dict[warn_key], return override value)
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
		- IDEA: obj_name+str(count); if exist descript_dict[key]: active_gs.buffer(descript_dict[key]); else: buffer default
		- IDEA: or maybe the pythonic approach here is "try" ?
		- IDEA: initial Warning attributes = name, trigger_type, trig_vals_lst, warn_max, warn_count, warn_key_1, warn_key_2
		- IDEA: should be able to eliminate warn_key_1, warn_key_2
		- IDEA: if warn_max = 0: key = name_1 ; else try key = name + "_" + warn_count except name_1 (i.e. name_1 is the default)
	- DONE: code warning improvements
		- DONE: add increment for warn_count (how did I forget this??)
		- DONE: eliminate warn_key_1 and warn_key_2 attributes
		- DONE: update obj instantiation
		- DONE: update descript_dict key
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
		- IDEA: if silent_timer == False: active_gs.buffer(timer_descript_key) where timer_descript_key = name + str(timer_count)
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
- INPROC: write up notes for warnings, timers, and auto_scope
	- DONE: warnings
	- TBD: timers
	- TBD: auto_in_alert_scope()
	
*** NOTES ***

* GENERAL *

In the wise (paraphrased) words of PERL's creator, "Good tools make easy things easy and hard things possible." The MachineMixIn class is extremenly flexible - but frankly, it's a convoluted PitA. It's great a enabling the unexpected and expanding the complexity of the Dark Castle world - but whenever possible, it's preferable to create and use simpler, fixed purpose machines. Warnings and Timers are both opportunities for this approach. While solving one problem, timers introduce a few new ones... the need to be more rigorous about game time, tracking which events in the game world Burt is able to witness, and ensuring that 'auto' game turns happen at the right time relative to other game responses.

* WARNINGS *

Warnings have a rich history in Interactive Fiction. If you cursed in Zork you'd be warned that cursing wasn't allowed. If you issued the same curse again the game would quit. Warnings are also a good way to redirect the player from a non-useful pursuit and possibly give them a nudge in the right direction. So when Burt attempts to go south from the Entrance and leave Dark Castle we tell him that he can't turn back and give the player a hint about the Rusty Key. And similar to the Zork cursing use case, if Burt attempts to attack the Hedgehog we warn him not to once or twice but if he keeps at it we let him... with game-impacting results.

The Warning class inherits from Invisible (including the attribute 'name') and, in common with MachMixIn has attributes 'trigger_type' and 'trig_vals_lst'. Warnings need to happen before player command execution and are always triggered by player commands - so 'trigger_type' is always 'pre_act_cmd'. 'trig_vals_lst' uses the same [case, word_lst] format as MachMixIn and the trig_check() method code is the same as well.

After these similarities, Warnings are much simpler than the MachMixIn class with only two more attributes: 'warn_max' and 'warn_count'. warn_count gets incremented each time pre_action() calls the Warning mach_run() methoed. If 'warn_max' == 0 then the use case is 'always give the same warning' and always return cmd_override = True. If 0 < 'warn_count' < 'warn_max'then give a specific error and cmd_override still = True. If  'warn_count' == 'warn_max' give a final "Don't say I didn't warn you Burt..." and cmd_override = False. Once warn_count > warn_max there are no future warnings and cmd_override always = False.

The actual warning description key is based on "name" + "_" + str(warn_count). This is implemented with 'try: ... except:' with "I'm not sure that's a good idea Burt..." as the 'except' default.

Fundamentally, Warnings are simple - they inhibit a player command either always or for a finite number of tries and return a variable text message. Warnings do not actually generate any actions - but a MachMixIn condition could take the difference between warn_count and warn_max into account.

* TIMERS *

* ALERT SCOPE *

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
- Create class, methods, and obj for read_scroll machine


##########################
### VERSION 3.68 START ###
##########################

Version 3.68 Goals
- Create / update program documentation

TBD: documentation:
	TBD: updeate creature doc
	TBD: update class diagram
	TBD: update module diagram
	TBD: create machine diagram
	TBD: create creature diagram


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
- introduce pre-built "warning" machine? use for 'go south', 'attack hedgehog', 'lift heavy rock', etc
- does creature_state really have any value? Maybe build hedgehog before pulling the plug on this one
- change hand from list to string
- cursing => end of game (requires warning_mach and usniversal scope)
- lantern (requires darkness travel tracker, timer, item_mach, univeral scope, death by grue)
- game saves (requires file clean up?)
- encumberance (post Burt as object?)
	- DONE: de-dup warning and timer classes
		- IDEA: after cleaning up some typos it appears that "selective inheritance" just isn't a thing. What now?
		- IDEA: this makes sense... in all other cases I inherit from simple parents to more complex children
		- IDEA: WarnClass is simpler... so it should be the parent
		- IDEA: Actually - how about a TrigDetectMixIn that is inherited by both WarnClass and MachineMixIn and only has trig_check method?
		- IDEA: A MixIn of a MixIn seems over-complicated... 
		- IDEA: perhaps right now I'll just make an independent class with duplicate trig_check code base
		- IDEA: as a future activity, I can look to de-dup in a more elegant fashion
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
