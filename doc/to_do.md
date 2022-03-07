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
IN-PROC: create attack() method
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
	TBD: full final test
TBD: create goblin machines
	TBD: attack burt machine
TBD: create help function for creatures
TBD: update creature doc

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


*** CREATURE IDEAS ***

Creature Class Ideas:

- Class:
	- inherits from ViewOnly
	- inherited attributes: name, full_name, root_name, descript_key, writing

- Unique Attributes v2:
	- creature_state
		for Goblin = None
	- mach_obj_lst
		for Goblin: 
			1) attack if player interacts with room obj
			2) watch player with malicious glare each turn in room
		For Hedgehog: 
			1) attack_warning?
	- show_item_dict # {{item : 'response_key'}}
		- for Goblin: scared of sword
	- give_item_dict
		{{item : {'response_key' : response_key, 'accept_item' : accept_item, 'give_item' : give_item, 'new_descript_key' : new_descript_key}}
		- for Goblin: scared of sword
	- attack_creature_dict
		{burt_weapon : result_code, result_text_key}
		(will need to implement default weapon code)
	- creature_items_lst
		for Goblin: Note and Axe for Goblin
		Key for Hedgehog
	- dead_creature_obj
	
- Unique Attributes v1 (Legacy):
	- creature_state
		(Goblin = None)
	- mach_obj_lst
		(for Goblin: attack if player interacts with room obj, watch player with malicious glare each turn in room; For Hedgehog: attack_warning)
	- show_item_lst
	- show_response_lst
		(Goblin is scared of sword; critical of all else)
	- give_items_lst
	- give_response_lst 
		[should be list of lists of text response and barter item]
		(CANCEL: Goblin "confiscates" all given items in a suspicious fashion)
	- attack_win_lst (weapon_lst, result code, resutl text)
	- attack_tie_lst (weapon_lst, result code, result text)
	- attack_lose_lst (weapon_lst, result code, result text)
		- weapon_lst : Fist, Sword, Axe, Other_Item
		- result_code : 'creature_flee', 'creature_death', 'burt_death', None
		- result_text : description of result
	- creature_items_lst (e.g. Note and Axe for Goblin, Key for Hedgehog)

	
- Methods:
	- Show (default response = "the <creature> is not interested in the <item>")
	- Give (default response = "the <creature> is not interested in the <item>")
	- Attack (default response = 'flee')

- Creature Machines
	- how does goblin attack Burt??
		- attack_src_dict
			{burt_weapon, result_code, result_text_key}
			(will need to implement default weapon code)
		- NEW IDEA: maybe an attack_burt method???



*** Open Thoughts ***
should item lists be changed once an item is given? Maybe doesn't matter since there are no duplicates... and even if there were 2x Biscuits... the point would be for the hedgehog to want to eat them again? So maybe creature_state doesn't really matter for show()? And maybe give() only needs to update creature_descript?


*** Creature Method Philosopy ***

* Over-Arching Approach *
I'm thinking through two different approaches to creatures. In one approach - I'll call it the "primatives" approach - I declare that each creature has wants and fears (e.g. the hedgehog wants the biscuits, the goblin fears the shiny sword). Under the primatives approach the creatures have innate personalities and the role of creature methods like show, give, and attack are just to expose those personalities. This is attractive in that it makes the creatures more real and gives general guidance for their future behaviors. However, I'm not sure it's realistic. Dark Castle is not a life simulator... there is no ecosystem or food chain (I mean really, the castle has been abandoned for generations - what have they all been eating??). And the creature's wants and fears are quite idiosyncratic... the goblin is an autocrat who wants to prevent passage to the throne room or any rejuvination of the castle... the hedgehog, along with loving biscuits, is the keeper of bright castle's spirit and wants to see it restored. These are not easy desires to model in a simple python object!

The other approach I'm considering - I'll call it theh "mechanical" approach - is that a creature is wholy defined by its methods. There is no attempt to track and expose a creature's inner desires - their actions are their all - like early impressionism, their surface is their whole. I find this a little unsatisfying - but I also think it's much more implementable. So at least for version 3.x this is the approach I'll take. Perhaps in version 4.x I'll find away to capture the hedgehog's inner yearnings in code ;-D

So, based on the mechanical approach:

- Show is meant to be informational in nature. The Player will learn something about the Creature - what it desires and fears - based on its response to the item shown. Therefore the show() method provides only a text response. It is possible that showing an item to a Creature could provoke an action response (e.g. running away) but this is outside the standard use case and should be implemented via Modular Machine. Ideally, show() would take creature_state into account.

- Give it meant to enable barter and trade. If the Player gives an item to a Creature - particularly if that creature has shown interest in the item via show() - then the player can reasonably hope for some other useful item in return. Therefore the give() method provides a text response, removes an itme from Burt's hand, and places a new item in Burt's hand - but that's it. Again, it's possible that give() could trigger a more advanced sequence of actions from a Creature but this is outside the scope of the method and should be implemented via Modular Machine. Because give() can provide a creature with a vital need it also has the power to change the creature's mood and therefore update their description. 

- The Attack method is a bit more complex and is intended to enable decisive combat between Burt and creatures. Burt can attack a creature and a creature can pro-actively attack Burt. The intent in Dark Castle is for combat to be a purely logical exercise... so if you attack a Creature with the correct weapon you will always win. Burt's "weapon" is whatever he is holding in his hand. If Burt's hand is empty he attacks with his Fist. attack() must first determine (based on Burt's weapon) whether Burt wins, ties, or loses in combat. Based on this outcome there are several possible outcomes: 'flee', 'creature_death', 'burt_death', or None and text descriptions to go with them. As, with the other Creature methods, it's easy to imagine attack() provoking a more complex response than these outcomes - but those are outside the scope of the method and should be implemented via modular machine.



*** Methods Psuedo Code ***

- Show: 
	if obj in creature.show_item_list: 
		buffer creature.show_response_lst[item_index]
	else:
		buffer("the <creature> is not interested in the <item>")


- Goblin Pseudo Code:
	- On examine of Goblin - maybe some mention of Nana talking about Goblin Guard

- flow chart Goblin interaction

- introduce pre-built "warning" machine?
	- use for 'go south', 'attack hedgehog', 'lift heavy rock', etc
	- or maybe bake warning into 'attack method'

- for attack warning
	- attack_warning (boolean)
	- attack_warning_index
	- attack_warning_lst

- creatures = pre-action trigger, post-action trigger, pre-action auto, post-action auto

- a Creature is a collection of VewOnlyMach objs that enable it to respond to show, give, attack, and other stimuli
- Creatures should be no more complex than necessary
	- so when a specific creature need is met but a new creature behanvior will arrise =>
		- it may make sense to 'swap' in a 'new' creature of the same name
		- (e.g. hedgehog1 == hungry_guard, hedgehog2 == trader
		- presumably creature swap also happens via machine?

### Creature Class ###
### Switch Classes (button & lever) ###

More ideas on Creatures:
- Treat creatures like roving conditional events
- Wrapper checks for presence of creature in room and checks for conditionals against creature too

Key Creature Verbs (methods):
- show, give, attack


More obj Ideas:
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
- Burt as an object??
- How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away
- possibly rename modules to indicate usage first? i.e. creature_class_def.py => class_def_creature.py ???
- in machines, should conditions and results just be key-value pairs in a dictionary?
	- As opposed to needing 2 separate lists with identical indexes?
- Can I just set descript_key for Note in mk_def_pkl() with setter rather than whole dynamic_dict?
TBD: what should happen if Burt tries to take the axe from a living goblin? (general case)
TBD: auto_static_behavior for goblin? (e.g. "the goblin is eyeing you coldly") each turn - maybe should be a standard function??


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
