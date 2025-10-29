To Do List - Dark Castle v3


# *** GIT BRANCH TEMPLATE *** #

	- TBD: <TEMPLATE>
		- TBD: create new <FEATURE_NAME>_feature git branch
			- TBD: 'git branch' to confirm *master
			- TBD: 'git branch <FEATURE_NAME>' to create new branch
			- TBD: 'git branch' to confirm new branch exists but that master is still checked out
			- TBD: 'git checkout <FEATURE_NAME>' to switch focus to branching_test branch
			- TBD: 'git branch' to confirm new branch is now in focus
			- TBD: Publish Branch via VS Code button
			- TBD: confirm new branch on GitHub
			- TBD: update doc TBDs to DONEs
			- TBD: <CMD><OPT>S (to save all files)
			- TBD: 'git add .' to add files to be committed
			- TBD: 'git commit -m "doc updates"
			- TBD: 'git push" to push updates to origin (GitHub)
			- TBD: confirm new branch on GitHub is now ahead of master
		- TBD: refactor <CODE CHANGES>
			- TBD: result class updates
				- TBD: copy existing class; change parent to BaseResult and update class name
				- TBD: update attribs and setters and getters
				- TBD: update result_exe() attribs
				- TBD: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- TBD: specific class changes: <list here>
			- TBD: update game files
				- TBD: add new result class to game_update imports
				- TBD: update Result obj name if appropriate
				- TBD: update game_update result obj classes, attribs, and post-assignment updates
				- TBD: set mach_state appropriately
				- TBD: update post-attrib assignment if needed
				- TBD: add result name to mach_run() exception list
				- TBD: comment out old result class and remove from import (in new name)
			- TBD: test & clean-up
				- TBD: test
				- TBD: clean-up game_update(), result_class(), mach_class() [??]
		- TBD: git branch merge with master
			- TBD: 'git checkout master' to switch focus to master
			- TBD: 'git branch: to confirm focus
			- TBD: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
			- TBD: 'git push' to push merge to origin (GitHub)
			- TBD: confirm that origin is updated
			- TBD: confirm that code is updated and still runs
			- TBD: 'git branch -d <FEATURE_NAME>' to clean-up local branch
			- TBD: 'git push origin --delete <FEATURE_NAME>' to clean up origin
			- TBD: confirm origin is cleaned up
			- TBD: post-branch-delete run test


# *** BIG PICTURE ***
- DONE: machincs / classes / error subsystem
- DONE: story updates
- TBD: interpreter updates
- TBD: test harness
- TBD: db back end (sqlalchemy)
- TBD: web site
- TBD: ECS (UI & App tasks w/ DynamoDB back end)
- TBD: CI/CD
- TBD: remaining foundation features: light, food, drink, sleep, etc
- TBD: get test player feedback
- TBD: expand adventure!

*** major updates in separate git merges ***
- DONE: mvps
- INPROC: implement full set of cardinal directions + u & d
- TBD: automated / unit testing
- TBD: major interpreter update!
	- TBD: introduce verbose and brief commands
	- TBD: address 'Do What I Mean' in interp() now?
- TBD: food
- TBD: webify
- TBD: drink
- TBD: live updates with git
- TBD: sleep
- TBD: db back end
- TBD: day / night
- TBD: liquids
- TBD: transparnecy
- TBD: fire / heat
- TBD: turn lantern into actual light (?)
	- IDEA: once an item, perhaps Landtern should be found on shelf (it's from Willy after all)
	- IDEA: lean in on TADS approach
- TBD: extend castle

*** major updates in separate git merges ***


############################
### CLEESH VERSION 3.8.3 / DARK CASTLE VERSION 3.4.0 START ###
############################

- DONE: choose branch name => card_dir
- DONE: create new <FEATURE_NAME>_feature git branch
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

- INPROC: implemenet full set of cardinal directions
	- DONE: implement ne, nw, se, sw, u, & d:
		- DONE: expand 'one_word_travel_lst' in engine_static_dict in static_gbl()
		- DONE: expand 'abbreviations_dict' in engine_static_dict in static_gbl()
		- DONE: set untrodden path to sw in dark_castle game_update()
		- DONE: test 'help travel' => good
		- DONE: update go_err() in error_class() to use 'one_word_travel_lst'
		- DONE: update interp() to use 'one_word_travel_lst'
		- DONE: update entrance_south warning => sw
		- DONE: test sw warning
		- DONE: temp test ne gate	
	- INPROC: for up, down only
		- DONE: zork: test u/d in front of house
			- FINDING: "You can't go that way."
		- DONE: test jump from in_tree
			- FINDING: land on ground, "In a feat of unaccustomed daring, you manage to land on your feet without killing yourself."
			- IDEA: maybe notion of survivable jump from one 'level' up
		- DONE: update u / d errors
			- DONE: u;;date err_go() to provide consistent u / d errors
			- DONE: restart mac to solve integrated terminal error (mac terminal working; not VSC)
				- FINDING: can run from mac terminal
				- FINDING: run "python3 web_main.py" and git from cleesh
			- DONE: test
		- DONE: still working through terminal errors :-(
			- FINDING: appears to be a PTY resource limit
			- DONE: closed all but 1 VS Code tab
			- DONE: temp raised max from 511 using: sudo sysctl -w kern.tty.ptmx_max=768
			- FINDING: can now run integrated console from VS Code
			- FINDING: per Tobi, terminal session persist across VS Code restarts - delete many
			- IDEA: i expect this will solve the issue
		- DONE: decide: multi-room types or just one???
			DECISION: floorless = FloorlessRoom sub-class, outdoor = attrib of Room
		- DONE: consider implementing room, outdoor_room, and floorless_room (like tads)
			- CANCLE: implement at 'type' attrib in room() ; type == 'std', 'floorless', 'outdoor'
			- IDEA: implement as 1 room() attribs: is_outdoor and FloorlessRoom sub-class
		- DONE: implement is_outdoor attrib
			- DONE: is_outdoor => Room attribs
			- DONE: add setter in room_class()
			- DONE: update in cup_of_tea game_update() file
			- DONE: test
			- DONE: update in dark_castle game_update() file
			- DONE: test
		- DONE: update wrong-way errors based on is_outdoors
			- DONE: is_outdoors => wrong-way error = "You can't go that way."
			- DONE: u / d errors for is_outdoor == False => try to climb wall / bonk head on floor
			- DONE: test
		- DONE: drop_rm, is_jump_fatal (None) > FloorlessRoom attribs
			- DONE: create subclass FloorlessRoom
			- DONE: add drop_rm and is_drop_fatal attribs
			- DONE: create setters and getters for drop_rm and is_drop_fatal
			- DONE: create is_floorless identity method
			- DONE: add is_floorless_room() => False identity method to identity_class
		- DONE: re-tune errors / effects based on new attribs
			- DONE: is_floorless => wrong-way = "You can't go that way."
			- DONE: in error class, update gs.map.get_obj_room(gs.core.hero, gs) to gs.map.hero_rm
		- DONE: update drop
			- DONE: update drop method: if is_floorless() , obj => to drop_rm 
		- INPROC: test up / down
			- DONE: update init_desc for postbox to include tree
			- DONE: create  up_tree room
			- DONE: add up_tree to map
			- DONE: create room description for up_tree
			- DONE: add dark_castle, moat, and drawbridge to up_tree.feature_lst
			- DONE: convert up_tree from Room to FloorlessRoom
			- DONE: test u / d
			- DONE: test wrong directions 
			- DONE: test drop (reg, mulit, floorless)
			- DONE: create tree ViewOnly obj => feature_lst in entrance and up_tree
				- DONE: entrance_tree and uptree_tree obj w/ different descriptions
				- DONE: move Cecily reference to in_tree description: "Being up here..."
				- DONE: add tree descirptions to feature_lst of each room 
			- DONE: create uptree_ moat and drawbridge descriptions to match up_tree view??
				- DONE: presence of active crocs clearer from up high (bite marks and water motion)
			- DONE: sort out direction UI; for u/d use "leading" or "leads" rather than "to the"
			- DONE: sort out lack of passage str in FloorlessRoom (update has_contain() method)
			- INPROC: enable description of "on the ground below you" (see Frotz)			
				- DECISION: yes, let's do this
				- TBD: create FloorlessRoom method get_below_lst()
				- TBD: create FloorlessRoom method get_below_str()
				- TBD: update disp_contain() in room(): "On the ground below you can see"
				- TBD: test
				- IDEA: I want to be able to move a trampoline under the drop spot
					- IDEA: to enable this, make init_desc obj not below by default
					- IDEA: but enable them to be added to get_below_lst()
				- TBD: update get_below_lst() to exclude items with init_desc by default
				- TBD: create custom_below_lst as attrib of floorlessroom()
				- TBD: create getters and setters for custom_below_lst
				- TBD: update get_below_lst() to incorporate custom_below_lst
				- TBD: for in_tree.custom_below_lst add [postbox]
				- TBD: test (shoudl see floor_lst + postbox but NOT big_rock)
			- TBD: create hollow as ViewOnly container
			- TBD: populate hollow with rubby
		- TBD: update jump method: if is_floorless(), move hero to drop_rm => is_drop_fatal
			- IDEA: land on feet vs. this was not a safe place to jump
			- TBD: test jump
		- TBD: how to enable 'climb tree' => ClimbableMixIn ???
		- TBD: review full entrance / tree UI and tune for best flow
	- TBD: clean up static_gbl(), game_update(), error_class(), interp(), room(), game_static, map()

- TBD: git branch merge with master
	- TBD: 'git checkout master' to switch focus to master
	- TBD: 'git branch: to confirm focus
	- TBD: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
	- TBD: 'git push' to push merge to origin (GitHub)
	- TBD: confirm that origin is updated
	- TBD: confirm that code is updated and still runs
	- TBD: 'git branch -d <FEATURE_NAME>' to clean-up local branch
	- TBD: 'git push origin --delete <FEATURE_NAME>' to clean up origin
	- TBD: confirm origin is cleaned up
	- TBD: post-branch-delete run test


############################
### CLEESH VERSION 3.8.3 / DARK CASTLE VERSION 3.4.0 END ###
############################


*********************
*** SOMEDAY MAYBE ***
*********************


*** structural ***
- TBD: maybe call disp_weapon from within cmd_exe() instead of in app_main() due to score??
	- EXAMPLE: 1) get sword from hedgehog, 2) attack goblin 'with sword' from bkpk
- TBD: should burt auto-draw weapon when attacked (e.g. 'go n' near goblin)?
	- IDEA: add 'draw_weapon' call into attack()
- TBD: should burt auto-draw weapon when for moat case?
- TBD: create a wearabel portable container and test lvl 2 with prep & 2_word
	- IDEA: simple wearable portable container would be a "fanny pack"
	- TBD: create class for wearable portable container
	- TBD: instantiate "fanny pack"
	- TBD: test basic functionality
	- TBD: test functionality with all in-scope 2_word & prep verbs
	- TBD: test whether game can distinguish between 'pack' and 'pack'
- TBD: leverage app_main() cmd_queue for 'again' command ?
- TBD: enable use of 'and' with action multiples ?
- TBD: enable use of 'from' with action multiples ??
- TBD: consider other possible uses for **kwargs; google "when to use kwargs in python"
- TBD: find a good use for TravelResult !!
- TBD: at end of story-driven updates, elim "##" error messages in error()
- TBD: sort out local buffering in standard errors?
- TBD: update validate() to move debug error indicators to pre rather than post			

*** decision about UI ***
- TBD: search on obj nouns and ensure always capitalized (???)
- TBD: how to handle obj.full_name capital cases?
- TBD: Add handle as an attrib of door? Could pull handle to open? door would have open direction
- TBD: investigate enabling init_desc attrib for items in containers (e.g. certificate)
- TBD: instantiate obj in hero inventory

*** known cleesh tech issues ***
- TBD: improve drink verb resevoir_lst error via undrinkable_dict error
	- IDEA: custom error for each non-liquid

*** new content / story ideas ***
- IDEA: Royal Hedgehog valor:
	- IDEA: caprecious and messy sort of valor
	- IDEA: sort that shows up two hours late and three sheets to the wind 
	- IDEA: (but is ready and willing to save the day)
- TBD: tune goblin text
	- TBD: maybe add a faded poster of ancient and unreasonable regulations to the antechamber wall?
- IDEA: maybe the hedgehog should act differently once you get & wear the crown?
- IDEA: at some point, perhaps Burt must knight the loyal hedgehog ?
- IDEA: meet the wizard from Enchanter who is searching for a scroll
- IDEA: puzzle based on 4 weights to weigh 40 lbs math puzzle
- IDEA: After winning game Burt can wander around the castle and see everone turned back to human?
- IDEA: In the Library there is a locked magical book ('The Future and Once King')
	- IDEA: is "still being writtin" according to the dragon librarian
	- IDEA: After winning the game, Burt can come back, find it unlocked, and read it
	- IDEA: (it's the back story for DC I; replaces magic scroll concept)

*** extend adventure / puzzle ideas ***
- muster room / main_hall antechamber is north of Gatehouse
	- puzzle TBD
- east of muster room = storage closet (TBD)
	- maybe secret passage from here to kitchens to north?
- west of muster room = passage way to gate and stone bridge over moat w/ path beyond
	- but bridge is shattered and cannot be crossed
	- can see lightening-struck tree leaning against tower to north
- North of muster room = main_hall
	- as soon as player enters main hall, baby roc swoops down and steals random obj and burt flees south
	- player must cary big_rock - roc tries to take - collapses - and flees west to nest
	- player is now free to investigate main hall and se/sw passages (roc no longer steals from burt)
	- CANCEL: baby roc flies from tower to tower west-east-west continuously
- cleared main_hall
	- baby roc now hiding in nest
	- main_hall has caved in so can only explore south half of room
	- 5 more passages (2 east, 2 west, 1 north) from main hall (kitchens mid-east door)
		- kitechens have garlic (for vampire)
		- workshop is maybe mid-west; has hammer (for vampire); sword sharpened here by badger?
	- NOTE: for this to work I'll need to embrace the other 4 cardinal dir
	- CANCLE: north is separately obstructed - player can slip through debris w/ no items?
- south-east of main_hall goes to wizard's tower / astronomy
	- Probably weight / pulley problem to solve here (zorkmid is key item)
	- Wizard himself has been converted into a kindly owl
	- was in love with gardener (now Otter) but can't get to her because window is closed
	- Maybe has key to garden shed, love letters, and something else useful (potion ?)
	- Access to room has useful astronomy-themed tool (telescope ??)
	- can see layout of castle from here including weather vane on top of round room
	- see village as well - cecily maybe? Or pub window at least
	- possibly even see weather vane well enough to see that it locks and how to get there?
- south-west of main_hall goes to catapult_tower
	- stairs to tower have collapsed
	- can get to top and catapult via tree (see tree climbing)
	- baby roc has made it's nest here atop some kind of platform / scafolding
	- if player tries to climb platform, roc appears and thwarts
	- all stolen items go to roc nest
	- roc really just wants to escape - looks towards west window freq; calls for mama
	- can't escape because lightening-struck tree is leaning against west window
- player can climb tree
	- tree = room with no floor
	- if jump => moat and die
	- if drop item => moat and vanish
	- hollow with some mcguffin half way up
	- higher up gives access to 2nd floor of tower, roof
	- from roof can view castle, weather vane, and fire items past cinch pts w/ help of telescope
	- telescope can give angle. Might need potion of parabolic motion knowledge to solve angle and force?
	- possibly even see weather vane well enough to see that it locks and how to get there?
	- player can also go further west on big_branch (hollow height)
	- if player goes west far enough tree will tip over away from tower
	- if player just holds on, they landly softly on the shore across moat and tree crushes them
	- they need to jump from tree when it is half way over, then run south to dodge
	- the tree now acts as a bridge across the moat
	- also, the roc immediately flies out and player can recover items from nest and get new item (?)
	- (what if player chops tree with axe ??? easter egg? )
- game_trail leads south along west bank of moat from tree crash and arrives at far end of stone bridge
	- west from here leads gazebo and sun dial (?)
- north of gazebo = garden
	- otter lives here and pines for owl
	- if palyer frees owl (maybe otter needs to help with this) otter will help player
	- owl flies to garden and otter embraces him => otter helps player / allows to enter shed
	- garden_shed is also here
- in garden_shed 
	- shed key in wizard tower with love letters
	- player finds stakes (for vampire)
- south of gazebo = grave_yard
	- has time-based puzzles
	- Mausoleum with writing that only opens at specific time shown by sundial (?)
	- potion must be made here under full moon
	- tombstone with useful writing of some sort (again, should be time-based puzzle)
- North of main_hall is round_room which spins like Zork II
	- actually, this is where Willy got the idea (since he is the adventurer)
	- he got sick of people constantly bugging him for answers to problems so he installed the round rm
	- spin can only be disabled by getting to round room roof (how?) and locking weather vane
- Beyond round room is whole rest of castle
	- antechamber holds goblin
		- entrance to antechamber (or nearby) should be a cinch point
		- makes it impossible to bring sword
		- Burt will need to balista sword and other neeeded goods to courtyard
	- library with book_dragon
	- courtyard
		- great tree of bright castle (in decay)
		- ducklings in courtyard imprint on burt; turn out to be bathing nymphs?
	- cathedral / oratory holds vampiire

TBD: Introduce multi-room puzzle
- IDEA: trigger in one room, switch in 2nd room, effect in 3rd room

TBD: New Room Update
- IDEA: convert Moat to actual rooms?
	- IDEA: Create on_the_moat room that e, w, d lead to 
	- IDEA: unarmed players get one turn before croc attacks
	- IDEA: no floor to room (items drop down several rooms)

*** new story ideas ***

*** Awesome Words to Use ***
- stalwart (hedgehog)
- griffonage (illegible handwriting)
- recreancy (shameful cowardice; perfidy)
- aubade
- defenistrate
- consigliere
- consternation
- phyisogamy (from 3 Muskateers)
- Gallivanter
- Solipsistic
- Bamboozled
- Flabbergasted
- Discombobulated
- Cattywampus
- Lollygag
- Makarkey
- Kerfluffle
- Brouhaha
- Nincompoop
- Skedaddle
- Pumpernickel
- rolly-polly (hedgehog)
- Coddiwomple
- Sockdolager (forceful blow)
- sagaciate (get along)
- sockdolager

*-- possible new rooms --*
- upon_drawbridge
- entrance_hall (home base with well & safe shelf & hedgehog?)
- chapel (another possible home base?)
- courtyard
- library
- narrow / collapsed passage
- kitchen
- smithy
- maze
- wizards_tower
- dungeons

*-- RESEARCH --*
- read The Craft of Adventure
- Play at least 5 games
- Read the Digital Antiquiarian reviews

- PUZZLE: perhaps at some point Burt needs to bake biscuits??
	- would involve finding and mixing ingredients, right order, starting fire, baking right time / temp

- PUZZLE: Under Water Puzzle:
	- treasure at bottom of old well - but need a magical way to hold your breath?
	- old_well as water source in entrance_hall and also passage to... where?
	- can hold breath for 4 turns, locked grate is 2 moves down, get warning on half air and last turn
		- TBD: create LiquidContainer class
			- TBD: create new LiquidContainer class
			- TBD: instantiate old_well in the main_hall which contains fresh water
			- TBD: update drink() to allow / error for drinking from the old_well
	- lantern is water proof
	- should be like rope puzzle for Zork I... 
		- you have everything you need in the remote room but can't get out without solving puzzle

*-- DC1 PUZZLE IDEAS --*
Misc:
- Randomization feature like the spinning room in Zork 2 ? With way to turn it off
- Physics puzzles - see-saws, pulleys, and ceterfugal force
- Dragon is bored because it has read every book in the library - need to find a new book to interest it
- Ferret is named Bartleby
- landscape / path changes
- create vehical puzzle?

Alter Terrain:
- Use Map room_pair updates to alter a room dramatically after a major change
	- e.g. Zork I resevoir post-dam opening
	- could use this after a cave in or rock collapse in the dungeons / mines?

Vehical:
- Bucket pulley / weight puzzle in wizard's tower
- need to adjust weight correctly going up and down
- need to grab staute (?) on way up / down?
- or else maybe mine cart / parachute??

Zork Thief = Ferret:
- dextrous, loves colorful objects, likes to fidtet / fiddle with things, clever
- will steal an object from burt (or that burt has touched) each time it randomly runs into him (some items off limits?)
- Some item on a high shelf or complexly locked (like the Zork egg) can only be opened by the ferret
- burt can indefinitely / eternally distract the ferret (*after* it has solved its puzzle) by giving it a rubks cube (described not named)
- the ferrets treasures can be found in a hole that burt needs to reach his arm into (scary warnings - could be a grue)
- maybe the shelf in the main hall is the one place safe from the ferret
- or else the object is in the courtyard and ferret gets it after burt sees it through window?? (seems like less agency?)
- hedgehog chases ferret away from Entrance Hall any time it randomely attempts to enter (entrance hall has well & shelf too)

hedghog:
- perhaps the hedgehog greets you every time you walk into the main_hall once you return the sword?

Special Glasses / Dream form:
- let burt see a room using descriptions from another dict

Carry Cappacity Constraints:
- item 'size' limits (invent point values) for Containers and Narrow Passages
- instead of big_rock could have sea_chest in main_hall tht burt can barely lug
	- maybe it's locked but has no key
	- can be the solution to the Wumpus_bat puzzle
	- Also, when the bat drops the chest, it smashes open... maybe revealing the rubiks cube (too soon??)
- Could have a narrow_passage - perhaps a collapsed passage that connects the north and south halves of the castle?
	- burt can only squeeze through with a few items (no sword)... perhaps the ruby for the smithy mouse is in the north side?

Writing / engraving:
- would be nice to have a way to write / engrave on something
- maybe make a weapon useful against a particular foe by engraving it??
- or put the dragon to work clearing a passage by making a sign that says 'cheese cake'

Vanishing cabinets:
- enable limited travel to another part of the dungeon?
- maybe only work one way (because broken?)
- or maybe can only bring very little gear?

Window:
- would be need to have a Window class that allows burt to see what he can't take
- could allow burt to peer into a courtyard with a tree and fountain
- maybe 2 guard dogs - one with red hat, one with blue hat - that are constantly paroling a passage
- if burt observest the window for a few turns he can see when to zip past the patrol
- (when the blue-hat dog looks up expectantly)
- perhaps window is in the collapsed_passage ??

Game Ending:
- Kinging Scroll glows faintly... and can only read when sitting on the Royal Lecturn... which also glows slightly
	- lecturn found in the Library (Willy's favorite room in the castle)
	- But only one thing can be _on_ the lecturn at a time... and there is currently a stuborn_snail there
	- snaill can only be encouraged to move by showing it the salt from the Kitchen
	- Depends on class Shelf (example obj = table, counter, lecturn - anything with a surface); needs a max_items attribute?

Glum Dragon
- how about a glum / bored / enui-ladden dragon that is blocking the libary entrance with its bulk
	- the dragon is too tough to be harmed by - or even to notice - being attacked
	- instead it just bemoans its misery - misquoting hamlet, and camus ("The underworld is other people")
	- If given cheesecake (baked in the royal bakery) it can be cheered up - and will go work on its to-do list and read a book and such
	- note: all other creatures like cheesecake too?

- map
	- maybe room beyond the Main Hall is the round room with many collapsed / ruined exits
	- can go east through mouse hole to bakery or smithy
	- or west to libary - which will then connect player back to cooridor that leads to anti-chamber


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
	- IDEA: grafitti on Room wall = disp_writing()
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
	- or maybe you shrink for 3 turns or as long as you're in a confined space - whichever comes later??
		- (don't want to code every room for being mouse sized)
- maybe 2nd mouse, every once in a while, gets up from his nap at the table near the blacksmith and sneaks off to the bakery
	- bakery very hard to find... go to a corner of the maze and then go 'up'!!
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


*** future big structural improvements ***
- TBD: state machine for hedgehog [FUTURE]
	- IDEA: need to implement hedgehog state machine based on creature state
		- IDEA: Both hedgehog and throne_broach_dispenser would be better implemented as state machines
		- TBD: state machines and other general purpose mod-machs
	- TBD: update cleesh engine version build

- TBD: consider introducing an event bus [FUTURE]
	- IDEA: if cmd passes validate => event bus
	- IDEA: invisible triggers / switches: in hedgehog_eats_mach, give() command should set trigger (not cmd)
		- FINDING: Invis Trigger Idea = Event Bus Idea => 'burt-give-stale_biscuits-royal_hedgehog'
	- IDEA: does Event Bus work well cmd_exe() ?
		- CONCERN: need to process commands... is it easy to process commands from events???
	- IDEA: need to learn more about event busses, topics, message formats
	- IDEA: message field => type (e.g. 'cmd'), event_key, cmd_terms ('case' and word_lst)
	- IDEA: event bus idea
		- IDEA: would hold all commands, timer 'ticks', and state changes (e.g. switches)
		- IDEA: for event bus, consider moving auto_action() to front of app_main() run order

- IDEA: module triggers [FUTURE]
	- IDEA: Modular Triggers? (named after intent; match cond, result, & mach)
	- IDEA: Establish switch triggers such that timer as trigger is more natural
	- TBD: update cleesh engine version build

- TBD: mod-mach bug ideas [FUTURE]
	- TBD: auto_static_behavior for goblin? each turn - maybe should be a standard function??
		EXAMPLE: "the goblin is eyeing you coldly"
	- TBD: Do we really need to test for goblin in antechamber??? (will the goblin ever move)
	- TBD: should hedgehog_distracted_mach just be replaced by a Creature class attribute?
	- IDEA: Can we create a general purpose Dispenser machine - for use with Crown and Broach?
		- IDEA: would also be useful for control_panel
	- TBD: broaden hedgehog response to interacting with sword (e.g. "pull sword" should trigger)
- TBD: update cleesh engine version build

- TBD: debug ideas: [FUTURE]
	- IDEA: room should have show_machs() method that lists all local mod-machs
	- TBD: mach visible command (include switchs, warnings, and timers too)
	- TBD: machine purpose and state command (include warnings and timers too)
	- IDEA: machine mix-in should have a dbg_describe() method that describes the machine (like K8s)
	- IDEA: dbg_describe and debug_show_mach commands
		- IDEA: to keep obj names short, just use abreviations <mach_name>_r1_m1
		- IDEA: to understant what mod-mach does, have attribute that explains each module
		- IDEA: also explains each result and condition
		- IDEA: then have debug-only command that describes mod-mach based on that attribute
		- IDEA: would also presumably need debug_show_mach command
	- TBD: update cleesh engine version build

- TBD: in mk_def_pkl(), sort out more elegant assignment process for self referenced obj [FUTURE]
	- EXAMPLE: re-assigning goblin to goblin_mach after goblin Creature instantiation
	- ANALYSIS: basic problem pattern = obj => obj_mach => obj_cond / obj_result => obj
	- IDEA: pass/link obj to obj_con/obj_result innately (not explicitly) as part of call/assignment?
	- TBD: update cleesh engine version build

- TBD: enable general case of player interaction in-game, from web_main() [e.g. "what is your name?"]
	- IDEA: need to reconsider how to present backstory...
	- IDEA: web_main is framework for all games - "floating scroll" won't work (think of space game)
		- IDEA: ARGH!!!! I just realized I CAN'T do this in gs.end ....
	- IDEA: except for in web_main(), there is no interactive option
		- IDEA: everything is bulk beffered, then presented to player for input back in web_main()
		- IDEA: input is ONLY collected in web_main() which is *HUGE* pain for backstory interaction
		- IDEA: I need to move backsotry interaction back to web_main() and pass is_bkstry with it
		- IDEA: then pull 'read_bkstry_str' and 'backstory' from static_gbl() using game_name & path
		- IDEA: need a function in file_io() to pull descriptions from static_gbl(); re-usable
	- TBD: create player_interact() in /app_main
		- TBD: player_interact() = 3 func: get_player_confirm(), [get_player_int(), get_player_str()]
		- TBD: create is_interact attrib in gs.core (default = False)
		- TBD: in gs.end() set core.is_interact=True, retrn interact_str, interact_type to app_main()

TBD: Refactor app_main() modules
- TBD: refactor remaining app_main chain: pre_action, cmd_exe, post_action, auto_action
- TBD: use __getattr__ and __setattr__ methods to make dict accessible as obj
- TBD: refactor GameState & dicts in static_gbl() with dunder methods ( __getattr__ and __setattr__ )
	- LINK: see: https://stackoverflow.com/questions/10761779/when-to-use-getattr
	- TBD: create dict_class_def.py w/ StaticDict and __getattr___ (and s__setattr__ for future tools)

TBD: Enable Verb Methods for Machines
- IDEA: enable silent run mode for verb methods so that I can use them in result_exe()
- IDEA: start with Item.take() => TakeResult



*** TO REVIEW ***


*** Unit Testing ***
- IDEA: build a framework based on mock GameState class
- IDEA: get serious about creating a "test harness" that can run automated test cases
- TBD: enable mode to write all input and last 80 char of output to CSV file
- TBD: enable passing file of commands and comparing with file of outputs ("get key")
- TBD: Stack Overflow: "how to implement command line switches to my script"
- TBD: in test mode, manually set random switch to value = 7
- TBD: eventually need to be able to run a suite of tests built up over time


*** modular machine updates ***
- TBD: make 'disable post run' a standard feature / attrib of modular machines
	- IDEA: attrib => is_run_once

*** refactor Creature ***
- TBD: sort out whole 'fist' / 'sharp_teeth' un-armed attack issue in Creature class
	- Sort out the wierd thing where unarmed attack is represented by first item in feature_lst
- TBD: consider how to surface 'not_attackable' txt in game_static_gbl
	- UPDATE: is_attackable checked in error() - maybe good enough?
- TBD: does creature_state really have any value? Maybe build hedgehog state machine before pulling the plug on this one
- TBD: Could simplify 'give', remove description updates from give, and instead implement them as part of state machine?

- TBD: should it be possible to show() an obj of class Writing or ViewOnly ??
	- TBD: enable 'show writing to creature' is writing is on an item Burt is holding

- TBD: make creature obj data more atomic
	- TBD: create weapon() method to provide adj & adv (vs reading weapon_dict via attack() )
		- IDEA: obj should be a black-box
	- TBD: same idea for 'can't attack error' for attack() in invisible(); should be creature() meth

- IDEA: Distracted state & description as creature attribute; inhibits 'show', 'give', attack 'commands'
	- "The creature too distracted to notice what you are showing them"
	- "You think better of attacking the distracted creature"
- IDEA: Creature state is linked to descript; e.g. hedgehog_descript_1
- IDEA: machine result changes Creature State; State machine itself changes creature attributes based on state
	- e.g. start timer, description, machine active, distracted attribute, etc


*** refactor Interactive ***
- TBD: clean up and make more efficient
- TBD: should "put key in moat" do more? what about "enter moat"
- TBD: Sort out prepositional spaces (e.g. Under, Nook, Hole, Bed) ***
- TBD: maybe a Bed in the Main Hall?
- TBD: maybe a fireplace in the Main Hall (class = Nook)? Or better yet, Alcove as class Nook?

- TBD: the future list - future interactive obj updates / features to be implemented
	- framework for complex obj to contain sub-elements (e.g. drawer + surface + under == desk)
	- Could also have UnderMixIn and BehindMixIn
	- TBD: for UnderMixIn - need to include bulk capacity for negative space
	- would need to deal with the wording 'look under' and 'look behind'
	- 'look under' adds contents to room.feature_lst
	- additional 'under' commands = 'put under' and 'reach under'
	- for MixInHole have commands 'look in' and 'reach in'
		- can a 'hole' be dark if the room is light?
	- TBD: enable the 'behind' preposition (with multiple varients of obfustication)
		- IDEA: minor_behind = you can see but not reach
		- IDEA: moderate_behind = can see some
		- IDEA" major_behind = can't see
		- Presumably, all 3 flavors of behind impact availability of obj in room list
		- TBD: put the control_panel behind the goblin (check TADS implementation)
	- IDEA: 'hole' = contain, opaque from room, no light
		- 'nook' = 'hole' that can contain Creatures
		- 'under' = opaque from room but no lighting issues
		- use 'take from under' for 'under'
		- use 'reach in' for 'hol'
		- need to enter() 'nook' to get contents

- TBD: figure out 'behind' prep for case of control panel in alcove behind goblin

- non-humanoid monster could be a special weapon description case (fun new puzzle idea)???
- DONE: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
	- encumberance (post Burt as object?)
	- implement carying capacity / container cappacity; Also carry restriction passages, etc..
- DONE: make goblin hand contents examinable (e.g. Grimy Axe)


*** Roll up sleaves and fix Interpreter ***

word_lst assignment:
- prep case word_lst => trig_vals_lst is erratic. see interp() ln 201, validate() ln 32, & mach_class() ln 72

*** Commands List ***
- if you meet a person:
	- Talk to <name>
	- Tell <name> about <X>
	- Give <thing> to <name>
	- Show <thing> to <name>

- If you find a thing:
	- Turn <X>
	- Feel <X>
	- Fill <X>
	- Smell <X>
	- Listen to <X>
	- Break <X>
	- Burn <X>
	- Look under <X>
	- Climb <X>
	- Wave <X>
	- Take <X> off
	- Turn <X> on
	- Dig in <X>
	- Enter <X>
	- Search <X>

- Also
	- Listen
	- Sleep
	- Wake up
	- Undo
	- Jump
	- Pray
	- Curse
	- Sing

- TBD: special case of guessing what player means if they don't specify
	- TBD: how shoudld this work? Should they need to be aware of what's in their hand?
	- TBD: default to key-like obj for lock / unlock activity?
	- TBD: review inform flags used for (Get What I Mean)
	- TBD: how to implement?
	- TBD: should be based on class => create Key class, is_key() method
- TBD: updates on this theme
	- TBD: now that hand is de-emphasized, need a better system for guessing what obj player means
	- TBD: should be mostly based on class
- TBD: solve articles for innate plurals (e.g Water, Tea => "qty of water" ???)
	- TBD: requires noun-adj strings longer than 2

- TBD: need to enable a rich set of game-specific synonyms!
	- TBD: make 'apparatus' a synonym for control_panel
	- TBD: add '* apparatus' as trigger to goblin_attack_mach

- TBD: need a better way to error on 'x'_'y' != obj.name ; maybe if '_' in noun, buff: "I don't see that"

- TBD: gracefully deal with unneeded preposition usage (e.g. "push on button")

- TBD: implement curse warning / ending at Interpreter() level

- TBD: read for DCv3 parser ideas: https://medium.com/swlh/zork-the-great-inner-workings-b68012952bdc

- TBD: fix interp() prep_verb noun vs. dirobj nomenclature once and for all!
	IDEA: swap to meth_noun_str and attrib_noun_str ??

- TBD: consider introducing str_to_obj_dict in Core (enable ease of entrance.examine(gs) in startup() )
- TBD: interpreter idea => permitted verbs & synonymbs by class (e.g. 'doff' for Garment)

- IDEA: in interp(), what about making prep check similar to put() for all prep verbs
	- IDEA: could have a prep attribute for each prep verb
	- IDEA: in interp(), have a list of all possible preps and use list to break sentence

- IDEA: next interp() goals:
	- IDEA: noun synonyms (different than abreviations)
	- IDEA: global verb synonyms
	- IDEA: simple prep verbs ('sit_in')
	- IDEA: basic interp features: 'take all', 'again', 'wait'
	- IDEA: address 'I can't see a x_y' error
- IDEA: introduce a vs. an

- TBD: text UI updates:
	- TBD: sort out 'can't drop fist or brass_lantern issue
	- TBD: change backpack and worn lists to include 'a' and 'an'
		- IDEA: convert plurals to singulars for this???
		- IDEA: (given that there is water in the game maybe all singlulars is impossible?)
		- IDEA: maybe a txt_handling() module with a disp_lst() func that takes care of 1) "x", "x & y", "x, y, & z"; 2) 'a' or 'an'; 3) plurals
	- TBD: sort out approach to plurals
		- 1) perhaps this becomes a ViewOnly attribute??? (don't like this - way too many un-used cases of attribute)
		- 2) possibly ItemPlural class inherits from Item and has method is_plural() which returns True ??
		- 3) could just have a plural_tuning_lst in the txt_handling() module that checks for known plurals as a one-off?
			- `Note: the problem with defining plurals in classes is, what if I want to establish plurals for a non-obj (e.g. a path)
		- Maybe apply 'xxy' prefix on text list if plural??
	- TBD: drop node 3 (portable_containers in containers) disp?
		- TBD: can burt know about node 3 items he hasn't 'seen' in this game?
		- TBD: play through Zork kitchen to test out

- TBD: exit() should apply to chairs and doors => move to Perch / Nook class
- TBD: should have 'go in gate' and 'enter gate' as synonyms for 'go north' from entrance? (doors & rooms ??)

- Do I need a gs.Gramarian class to deal with recurring display issues around pronouns and plurals?
	- e.g. pronoun_tobe(creature) => 'You are' or 'The <creature.full_name> is'
	- e.g. article_plural(obj) => 'a Grimy Axe' or 'Water' or 'an Apple'
	- maybe plural_dict is a local dict in the Gramarian class?
	- Or maybe a better class name is just Display (???)
	- Division of labor: player text => commands == Interp; obj => player response == Output
	- could put some recurring dispaly routines here (obj_lst => str_lst and such) ??
	- Display could also hold buffer commands???
	- Another possible class name == Output ???
	- Leaning towards Output... this helps distinguish from all the verb-linked Disp methods

- TBD: create a version just for interp() updates and gather all interp updates there!!
- IDEA: verb synonyms per obj with 'move' as a broadly used and variable synonym??
	- verb synonuyms linked to class / class method?
	- perhaps additional, optional cusotm verb synonyms as an obj attribute?
- TBD: implement global verb synonyms for 'sit in' or 'sit on' == enter()
	- TBD: also want to enable 'go in' and 'go out' of chair

- TBD: interpreter - should all nouns be singular? Can 'a' vs. 'an' be fixed?

- Interp deep dive including better solution to prep checking ('put in' vs. 'put on')

interpreter ideas:
- can I store variables in static_dict strings? (in f-string format)
- can I return method errors based on verb method (e.g. "Burt, what kind of person would try to attack a Throne?")
- should synonyms be an obj attribute??
- more abreviations: 'g' = 'again', 'z' = 'wait'
- fix progromatic usage of "a" vs "an" (e.g. "There is a Iron Portcullis to the north")

- DONE: unlock => 'unlock with' prep  command
- DONE: default prep behavior = try command with obj in hand
- New interp() Ideas:
	- interp() refacto shoud be based on objects (contents of rooom)
	- each obj should have noun syns (in place of root_word)
	- if user input has multiple obj, determine noun vs. dir_obj from prep usage (i.e. to vs with)
	- have global verb syns and class-based verb syns (start with global; much easier!)
		- e.g. 'get' is gbl verb syn for take() but 'sit on' is a Seat class verb syn for enter()
	- based on verb, validate prep usage
	- Order of Op: 1) obj noun syns, 2) gbl verb syns

*-- INTERPRETER ENHANCEMENT --*
- TBD: sort out synonyms like 'stand' and 'sit' and 'lie'
- Interpreter enhancements:
	- noun synonyms (list in place of base_name)
	- verb synonyms (attribute of Class? Should verbs associated with obj???)
	- enable "take all", "drop all"
	- randomize frequent responses (e.g. "in your spell book you see...")
- re-institue remove() verb for Garment; 'take' as synonym
	- worn obj take() => "You're already wearing it"
	- obj on floor remove() => "Taken" (i.e. is synonym)
- assume that item in hand will be used for activity (e.g. attack)
- move() command ?
- enable 'take all'
- create 'jump' command with same response as Zork ('Whee!' I think?)
- randomize description of Burt shown during 'inventory'
- convert words like 'look' to 2word in interp(), rather than cmd(), if possible

*-- ARCHITECTURE --*
- What would a decoupled, micro=services based DC look like? What are the consumers / providers?


*** get on the web and start working in the open! ***
- TBD: figure out multi-user
- TBD: get flask on Amazon Linux 2023 on EC2 working!
- TBD: Have 'prod' game tab, 'legacy' tab, and 'dev' tab
- TBD: link mac updates to dev tab via pipelines
- TBD: link dev tab to prod during manual updates
- TBD: pull in DB migration to get ready for web


*** cup_of_tea enhancements ***
- IDEA: need to provide default engine mechanisms with option to replace with custom game versions
	- IDEA: assume a 'lazy game designer' who doesn't create custom values; should work anyhow
	- TBD: need a default set of titles title_factor that can be over-ridden with game-specific
- TBD: future updates for cup_of_tea (this will eventually be the setup for why Burt went to DC)
	- TBD: need to fix door (have pub folks charge in)
	- IDEA: to drink tea, Cecily must lock front door, sit in comfy chair, read book, eat biscuit
	- IDEA: also, she must get rid of Burt who wants her attention (give rusty_key to burt)
	- IDEA: Cecily sort of likes Burt - he's better than that Gaston fellow - but overgrown puppy
	- IDEA: night before, Burt was bragging to whole pub about how he would storm Dark Castle, get treasure
	- IDEA: Winning condition = drink Tea; Time up when pub opens (belching contest begins); 9 bells
	- IDEA: Gaston keeps flirting with her sister; big-headed and constantly singing...
	- IDEA: book is riff on LotR; 
		- IDEA: office workers on death march project; must bring TTL report to shredder
		- IDEA: led by bearded application developer, heart-string-pulling retirement party at end
		- IDEA: always saved by IT person at critical moment


*** Get light working ***
- IDEA: what to do on container (or other) loss of light?
	- e.g. put lantern in box, close box (no stuck)
	- had thought about lighting up box from interiour - but wouldn't work for switch
	- is safe to actually turn off lantern - because anything in your hand can still be accessed...
	- so alternate idea is that hedgehog has to come rescue you
	- but at least one inventory item gets scattered (hedgehog shrug)

*-- AMBIENT SIM --*
- for light sources:
	- "(providing light)" in inventory; also is a condition (on)
	- can move into a dark room, but can't open a container in the dark
- for FlamableItem: light & burn (e.g. matches)
- PaperItem: burns; also, if writing, ink runs and becomes unreadable

- darkness & light source system?
	- lantern (requires darkness travel tracker, timer, item_mach, univeral scope, death by grue)
	- honestly, Grues don't make sense in DC... I intend for there to be a fair number of creatures around the place... why haven't they been eaten by Grues? (one could ask the same about the Troll and the Thief of Zork - but presumably these are dangerous creatures that can fend off Grues?). Instead, I think I'll use the same mechanic (2 dark rooms in a row == death) but the textual explanation will be Nana's warning to young burt "Burty, you mind gallavanting around in the darkness - you'll trip and break your neck!"


*** Get liquids working ***
- Liquid handling
	- INPROC: Research IF liquids
		- DONE: Infocom
			- Zork: Glass Bottle 
				- has one 'quantity of water'
				- bottle must be held to be drunk
				- bottle must be openned to be drunk
			- Enchanter: Jug
				- has multiple quantities of water
				- jug has no 'cap': "The jug has no cover. It can't be openned or closed."
				- must be at least a little 'thirsty' to drink water
			- Other uses (in Zork):
				- Water can be poured on flame to put it out
				- Water can be poured on the heated bell to cool it
		- TBD: how does TADS do it??
	- INPROC: Long-term Liquid plans
		- Liquid class
			- The primary liquid in the game will be water
			- An important point of awareness is that 'water' (unlike all other nouns) cannot be guaranteed to be unique
			- Main liquid verbs = drink(), pour(), fill()
				- where 'Y' is a Liquid and 'X' and 'Z' are containers / bodies of water
				- drink() : 'drink Y from X'
					- Liquid method
				- pour() : 'pour X from Y in / on Z'
					- ContainerPortableSimple method
				- fill() : 'fill X with Y from Z'
					- ContainsMixIn method
			- - IDEA: Advanced verbs: mix(), stir(), shake()	
		- Non Liquid class properties related to liquids
			- If water is poured in or on an object it has an effect:
				- no special results (if the obj is a Container then it holds the water)
				- Obj unimpacted but water 'evaporates'
				- Obj is ruined / disolved / rendered illegible (e.g. paper note); water "evaporates"
				- Heated obj is cooled (Zork example; future)
				- Flame is extinquished (Zork example; future)
				- note that these effects are properties of the objects - NOT the liquid class
			- Implementation:
				- for ViewOnly class and below, need an attribute: liquid_result
					- defines what happens to the obj when it contacts liquid
					- also defines what happens to the liquid when it contacts the obj
		- Special case of bodies of water
			- does an object sink or flat?
			- this can get complicated 
				- maybe keep the Entrance 'well' to a shallow rainwater-fed pool
				- test with Enchanter spring
		- Special case of immersion
			- You should be able to swim in water and diver under water
			- Breathing limits will apply
			- This will mostly be independent of Liquids... 
				- but anything with a 'ruin' liquid_result == 'ruin' should be destroyed by swimming


*** Get food / hunger and beverages / thirst working ***
- IDEA: interesting updates for food & bulk
	- require eating
	- enable Water to be drunk in small amounts (multiple servers per filled bottle)
	- enable same partial consumption for bread loaf (calls back to Enchanter)
	- Make sips of water / bites of bread the one frational bulk amount in game
	- Enables interesting weight puzzle (4 gallons from 3 & 5 gallon buckets)
	- Maybe stale_biscuits => 3 biscuits in paper package (Nana sword & key logo; better than McV ref?)
	- Perhaps for bulk puzzle, have a Pywrong beaker - extremely fragile - breaks if put in pack or dropped

- TBD: hunger & thirst become Creature conditions to examine??

- IDEA: for food, maybe have the biscuits take 3 turns to eat... but if burt eats some he gets less time to grab the sword... 
- IDEA: maybe don't need warning so much... just keep describing them as tasting worse and worse? Food consistent within creatures?

- food & drink system?
- hunger & thirst to be indepedent boolean settings in gs.core
- hunger & thirst durations settable in gs.core

Food:
- bread for Burt (save piecs of cheese for the mice)
- maybe need to keep feeding biscuits to the hedgehog?
- perhaps loaf of bread and bottle of water can each provide multiple servers (similar to enchanter)
- additional bread verbs needed: bake ???

*** Get tiredness and sleep working ***
- sleep to be a setable boolean in gs.core; also setable duration

- maybe sleep in bed (after min # of moves) to dream to get hints? But light must be on so you loose turns of light and wake up hungry and thirsty? Hint is provided randomly based on points not yet accrued?
- need to check Enchanter to find length of days, when sleep needed, food & drink, etc
- For dream hint: Burt has dream / memory of Nana teaching him the binary code she would use with Willy while secretly courting (she was a lunch lady?) to set a time to sneak off with him. Would involve 2 types of biscuits on counter... Nana's Own and McVittles (which were awful)... she only had room for 3 biscuits but had to show times from 0 to 7... 


*** Introduce fire & heat ***
- TBD: a thermal attribute for obj that cools over time (hot_tea => warm_tea => cold_tea)


*** Introduce transparency ***
- e.g. Crystal Box should show kinging_scroll / empty / contents
- TBD: an hour glass machine (changes time as turns pass; has flip() verb) 
- Window: would be need to have a Window class that allows burt to see what he can't take


*** conversational verbs ***
- IDEA: 'talk to creature' format:
	- IDEA: 'Ask X about Y'
	- IDEA: 'Tell X about Y'
	- IDEA: Say 'Z'


*** Implement Symetric Verbs ***
- TBD: as part of symetric functions reveiw...
	- re-examine current use of creature = gs.core.hero
	- if non-hero creatures never hit errors... do we need this in the Invisible class ??

- enable all verb methods for non-burt creatures
- TBD: doc_string about future 'silent_exe' for symetric creature commandsv
- TBD: test with test_frog holding test_box (PortableContainer) holding red_mcguffin Item
- TBD: tune pronouns
- IDEA: errors are only for burt
- IDEA: auto-gen descriptions (e.g. drink, eat, wear, sit) are only for burt
- TBD: doc_string on 'semi-symetric' methods
- TBD: enable non-burt creature use of all verb methods 
- TBD: how should creature be passed to Conditions & Results?
- TBD: how to deal with error messages for non-burt creatures (e.g. test_frog walks into door)
- IDEA: alternatives for how to to auto-move non-burt creatures: dir_lst, room_lst, room_dir_dict

- In some cases creatures will use methods to take actions and burt will *obeserve* their actions
	- this should be enabled by mode = 'exe_creature'
	- DECISION: part of making verb methods 'symetric', 'creature' should be checked for in each method


*** Long-term Pondering ***

- TBD: reveiw / update / finalize doc file

- TBD: possibly rename modules to indicate usage first? i.e. creature_class_def.py => class_def_creature.py ???

- Long Term Pondering:
	- the whole 'hand' concept is looking increasingly dodgy... too much inventory mgmt...
	- maybe time to bite the recursive bullet and just allow portable containers in portable containers?

- decide if interactive() class objects should eventually have noun identities (e.g. is_door() )

- TBD: static_gbl => tupple

- INPROC: Given that creatures will be contained:
	- INPROC: need to embrace a node-based awareness of creature location
	- DONE: need to embrace the use of recursion on methods like remove()
	- INPROC: Apply this to concepts like drop() and stand() / exit()
	- OLD DECISION: alternatively, just treat creature-containers as special exceptions
	- NEW DECISION: started using recursion when applying weight to obj & creatures
- TBD: Alternatively, maybe time to consider letting obj know what container they're in??

- INPROC: review TADS3 terms for Description and preposition

- IDEA: consider converting Writing to Decorations (examine() vs. read() )

- TBD: make backpack a true container???
- TBD: learn how to use VS Code word wrap and other features for Python
- IDEA: maybe I should call validate() again between pre_action() and cmd_exe() and then again between cmd_exe() and post_action() ?

- TBD: refactor gs. scope / mach_scope
		- Use list comprehension to eliminate for-loop? (link: https://medium.com/self-training-data-science-enthusiast/python-list-comprehensions-use-list-comprehension-to-replace-your-stupid-for-loop-and-if-else-9405acfa4404 )

- CANCEL: considers re-distributing not-in hand & read errors back into verb methods ???

- DONE: for doors and containers, use None option for no lock or no lid?
- CANCEL: Can I just set descript_key for Note in mk_def_pkl() with setter rather than whole dynamic_dict?
	- CANCEL: why do I need gs.dynamic_static_dict again?

python techniques:
- Do a refactoring code review (look into the 'any' command in place of for loops)
- TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )
- TBD: Try tupples for static_dict
	- NOTE: Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
- TBD: learn about Super()
- TBD: read this article: https://sangeeta.io/posts/a-super-post-on-python-inheritance/

pipeline & testing:
- create 'win' test routine with checksum
- TBD: Jenkins integration to automatically update "v3 alpha" tab with latest commits


*** make database-driven! ***


*** doc_strings ***

- TBD: doc_string about why errors and actions must be clearly delineated (e.g. and error cannot change gamestate)

- Clean up documentation and incorporate into doc_strings

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
	- TBD: Timer Decisions
		- timers are set by machines rather than triggered by player commands
		- other than providing description text, timers are dumb - they just count -  a machine takes all actions


*** Out of Game Quality of Life Code ***
- Introduce non-functional requirement code (e.g. saves and pkl clean-up)
- Integrate with web template
- webify

file handling:
- game saves (requires file clean up?)
- move doc to modules?
- org modules in directories?

web features:
- TBD: Figure out a way in web browser to show all adventure text in scrolling window (???)

- create a hint sub-system
- TBD: no swearing in Dark Castle (with warning or else end of game)
	- cursing => end of game (requires warning_mach and usniversal scope)

- TBD: Debug mode:
	- TBD: Need a debug mode that eliminates 'try' from 2word and prep commands
	- TBD: need a secret code to prevent regular player from falling into debug: 'debug poke53281,0'
	- TBD: maybe debug opens a menu where you can choose start room & choose to disable method and / or description guards
- TBD: verbose / brief

- Unit Testing (link: https://youtu.be/6tNS--WetLI ) ???

* DEBUG TOOLS *
- work room for testing similar to tcrf.net Hollywood Hijinx

- "dungeon builder" web interface (?)

- runs on AWS with API GW, Lambda, and DynamoDB!

*** DB Driven ***
Version X.x Goals:
	- DB back end
	- "dungeon builder" web interface (?)
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


*** Expansion of Dark Castle ***
- Research existing IF languages (TADS & INFORM)
- Plan out expanded adventure
- Establish new base code needed for new adventure
- Write new code!

first: scan puzzle ideas and decide on next puzzles; plan for required features

- New rooms and puzzles!!
- New ideas - ideally should leverage existing coding with minimal addiional feature requirements
-implement new ideas
- publish new version and get feedback


*** DC2 PUZZLE IDEAS ***
- maybe, in DC2, before the ball, the princess is missing (hiding from evil prince) and is diguised as a black cat that burt needs to befriend?
- it would be cool to have an invisibility cloak / spell (probably need to keep it short term / contained)
- Note: gs.core.hero enables player to take on different characters in the game (e.g. Burt could become a mouse)
- princess 'poise' & 'moxie'
- fun idea - small creature - like a mouse - as an item
- more directions
- Princess takes 3 forms:
	1) Cat => Burt must get her collar
	2) Raven => ring
	3) Cockney goth waif (castle servant) => boots
	- Then princess arrives at ball wearing collar, ring, and boots
- Burt must also foil evil Prince plan to murder princess (perhaps swap fake dagger for real one?)
- Burt himself is taken for a lowly Baker (in past time)
- Basically, Burt and the Princess (in various forms) wander around the castle doing chores learning info
- Also, Burt has a chance to demonstrate himself as kind and helpful - or not - to disguised princess
- Meanwhile, the whole castle is in an uproar getting ready for big ball and princess arrival
- some scattered rumors that princess has "mysterious magical powers"
- Meeting Nana
	- Also, somewhere in the mix, Burt must prove who he is to a (much younger) Nana
	- he needs to get (Willy's) broach, and put it behind the throne
- Burt is given most of his hot/cold direction via a portrait of himself & princess
	- As Burt makes right decisions the portrait gets clearer; fades with wrong decisions
	- Portrait is taken of Burt and waif-princess by great artist who needs stand ins for Prince & Princess wedding portrait
	- Burt originally (in modeern times) finds the portrait on the pedistal next to the throne and *MUST* put it back there during time travel just before arriving back or else the closed time loop fails (gets multiple hints that there's "something he must do")
- Dungeon key
	- in modern times, the one room Burst still can't get into is the dungeon
	- main key was lost years ago during the "great ball fiasco" and spare has never been found
	- not viewed as very important since the dungeon side-wall parially collapsed and was flooded by moat
	- Dungeon is now the lair of the evil croc in the moat 
	- Burt needs to get the dungeon key in past times
	- he must somehow get it back to modern times so he can rescue princess in flooded dungeon from croc
		- why can't she just turn into a fast fish?? need to think through her magic limits
	- impossible to keep it so must hide it behind a brick (where he will retrieve it in the future)

- Princess Time-Travel Quest:
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

DCII Time Travel Ideas:
- In past, burt must convince young_nana to give him Willy's broach in order to drop it behind throne or else timeline is doomed!
- Perhaps burt first travels fwd in time a week and can pick up an unfinished portrait of burt & princess that gives future status (similar to Back to the Future)

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


##### RANDOM NOTES #####


##########################
### VERSION 3.7x START ###
##########################

Version 3.7x Goals



##########################
### VERSION 3.7y START ###
##########################

Version 3.7y Goals


##########################
### VERSION 3.7z START ###
##########################

Version 3.7z Goals


##########################
### VERSION 3.8q START ###
##########################

Version 3.8q Goals


##########################
### VERSION 3.8u START ###
##########################

Version 3.8u Goals


##########################
### VERSION 3.8r START ###
##########################

Version 3.8r Goals


##########################
### VERSION 4.x START ###
##########################

Version 4.x Goals


##########################
### VERSION 5.x START ###
##########################

Version 5.x Goals


##########################
### VERSION 6.x START ###
##########################

Version 6.x Goals


##########################
### VERSION X.x START ###
##########################


##########################
### VERSION Y.y START ###
##########################

vY.y IDEAS






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
