Dark Castle v3.83
Tom Snellgrove
Mar 13, 2024



###############
# web_main.py #
###############

*** READ ME FROM DCv1 ***

"Dark Castle" is a very simple Zork-like text adventure game. I have written it in order to teach myself Python. The program is written using Pythonista and Working Copy on an iPad.

The program's language skills are very basic. All commands are either one word (a simple command verb like "north") or two words (simple verb-noun combinations like "attack goblin"). Adjectives are directly attached to the noun they are associated with via an underscore (e.g. "take rusty_key"). There are no articles or pronouns.

There are only four rooms and the puzzle difficulty progresses from trivial to moderate through the course of the game. The content is appropriate for kids.

I'm very much a beginner at both Python and text adventure writing so I welcome your feedback and suggestions! Also, feel free to clone and extend my code with new or different rooms, features, and verbs. Let me know if you do - I would love to play whatever game you create! I do ask that you credit my initial work and that you clearly state in the intro if the game is no longer appropriate for kids.

My next goal is to "flaskify" the app and put it on the web so that I can get feedback on it from others. I'm new to flask so this may take a bit. After the "flaskification" I plan to create an object-oriented version that supports better linguistics so any advice on object oriented techniques is much appreciated!

- Tom


*** WHAT IS ***

(Preamble)

- What Exactly is a Text Adventure / Interactive Fiction Game:

	- Wikipedia: "Interactive fiction, often abbreviated IF, is software simulating environments in which players use text commands to control characters and influence the environment."

	- I grew up calling IF "Text Adventures". I was 12 when Infocom released Zork I for the Commodore 64 and it blew my mind. At the time computer graphics were very primative. Fine if you wanted an arcade "twitch" experience like Pac Man or Galaga... but not something that could pull you into a story. Zork changed all that... suddenly there was a detailed fantasy setting where I could be the main character. It was the computer version of reading a "Choose Your Own Adventure" book - but with infinitely more freedome. Like being set down in Middle Earth or Narnia and asked simply "Where do you want to go next?". I was overjoyed.

	- I came to IF for the stories but I stayed for the puzzles. Games like Zork did not rely primarily on roling dice, collecting gear, and gaining levels in the fashion of my other favorite childhood hobby, D&D (though Zork combat does have a minor element of chance to it). Instead, IF was all about solving a series of interlinked logic puzzles. And man could those puzzles be madening! This was back before Google. Back before the World Wide Web. If you got stuck you either had to mail order the Invisclues hint book - which cost about a third the price of the game and took weeks to arrive - or find someone who had solved it already and beg for answers. In my case I had one friend who had solved nearly every Infocom Text Adventure released - but at the time I only saw him at school during lunch period. So I might get stuck on a puzzle over the weekend and not see him till Monday... and then my friend (yes, Im talking about you Geoff!) might well say "That's a really easy puzzle - you don't need a hint - you just need to think about it a bit more". Argh!!

	- The positive side to frustration was engagement and satisfaction. I would wander around the real with the puzzles in my head - replaying the steps I'd tried already again and again and thinking about new things to try in order to make progress. And when I did finally have a breakthrough it was a genuine triumph. I can still vividly recall the thrill of getting the Platinum Bar for the first time in Zork.

	- When I first started learning Python (as part of an AI Coursera course) I marvelled at how well it managed text and lists. So, not unsurprisingly, when I decided to start a Python project to really learn the language, a Text Adventure seemed like a natural fit. That said, it's important to be aware, while writing IF is a great way to *learn* Pyhton, it's certainly not the best way to *write* IF. That would be TADS - which is a purpose built language specifically created for IF and supported by a rich community of amerature IF game writers: https://www.tads.org

	- I also heartily recommend that you try out "real" IF if you haven't already.
		- Here is a link to play Zork I on the web: https://playclassic.games/games/adventure-dos-games-online/play-zork-great-underground-empire-online/
		- Here's a link to IFDB - one of the most widest and most active repositories of IF content: https://ifdb.tads.org
		- Lastly, if you're an Apple iOS user, I recommend the "Frotz" app. It's an older compiler but it still has a rich collection of works for free.


*** GAME STORY HISTORY FROM DCv2 ***

*** Story ***

- Like everything elese in the game the story just sort of happened as I went along. Burt did not start off as a Henry Vth wastrel with a destiny, a career as a baker, and a great-grandmother with little-known connections to royalty -  but here is the tale of how he eventually got there. I rewrote very little of the description text during final editing (the main exception being an update to the hedgehog description to discourage players from attacking it) so you can track the story evolution from room to room.

- Room 1: In the tradition of Zork I introduce Burt as a rough and ready sort not known for his feats of intelect or his sophistication. At this point I had a vague idea of Burt's pub bragging motivations but that was about all. Although the story had little refinement even at this point I was planning for the game to have four rooms with the winning condition being in Room 4.

 - Room 2: This was still early days story-wise. Why a hedgehog? Why not!? That's the unique beauty of the puzzle-centric easthetic of IF - one day you're whomping draggons - the next day you're held at bay by hungry hedgehogs. The stale_biscuits were inspired by my wife's love of British McVitties biscuits. At this point Burt was still a random bloke living in his Mom's basement without any kind of baking career and the game victory vaguely involved him finding a big chest of gold in Room 4.

- Room 3: Making the switches work and fixing some timer bugs took me a while so this is when a lot of the story thinking happened. Also around this time I had a conversation with my young friend Gideon who told me to end the game with a magic scroll that you read to win. Having no better plan I agreed heartily so now the end plan was in sight. The goblin was planned from Room 2 and is still entirely arbitrary but I was starting to think more about the writing and you can begin to see small signs of the eventual narrative. The description of the Antechamber is longer than that of past rooms and hints at a cursed condition. And the description of Burt's shiny_sword attack on the goblin hints at a hitherto unanticipated destiny. It was somewhere around this time that the castle went from just being a random spooky place to "Dark Castle".

- Room 4: The puzzles here are a lot more intricate so I had a lot more time to ponder the story. Also, endings tend to make one think of beginnings. And lastly I didn't have good puzzle ideas / props. My original idea was just that Burt would just get to Room 4 and find a pile of gold. But now that I'd committed to the scroll ending I had to have Burt return to earlier rooms to find the necessary puzzle mcguffins - which led me to want to explain elements which had previously been arbitrary. Why exactly was Burt destined to be king / barron of the castle. What was the castle called before it was Dark Castle? How come Burt is carying biscuits in his backpack? And what on earth is the deal with the hedgehog in the Main Hall? All of these ideas came together in Room 4. Which perhaps explains why nearly all the story elements get pulled together in the description of one item - which I proudly believe the be the most exposition-heavy broach in IF history. 

- Room 5: [future] We'll see if this ever happens but story-wise I do have some loose ends to tie together. Why is there a guard golin in Room 3? I usually picture him as a sour old servent who went dark with the castle but time will tell. And what about Burt's love life. In fantasy tales, (un)promsing lads like Burt usually have some sweetheart they are pining for. In Burt's case I picture it being a no nonsense laday of superior intelect and competence who's attention Burt is desperately trying to gain. Her story has been wholy absent from the tale so far and would be fun to weave in.



*** v3 Game Decisions ***

Coding Decisions File - Dark Castle v3
Feb 9, 2022


TRIGGER PRINCIPLES:
- In theory could have order of operations considerations:
	- (e.g. what if a monster causes darkness but you have a sword that glows around monsters?)
	- I don't think these will be a common problem that I need to code for - but worth thinking about

- For machines, the 'trigger' just sets the value... the machine holds the logic and takes the action

- Can (should) I make the program work without external triggers... can the obj just interact on their own?
	Perhaps the key is to make creatures behave as state machines... 
	each has conditions under which they will guard, attack, gift, etc..
	Also room 'events' with conditionals?
	IDEA: avoid external triggers - create classes / state-machines
		Examples: conditional_cutscenes (moat, ending), antagonistic_guard (goblin), hungry_guard (hedgehog1), trader (hedgehog2)[introduce "give" verb, dispenser (throne), lever, button


VARIABLE DECLARATION:
- Std solution for declaring obj variables with reciprocal properties (e.g. writing)
	IDEA: Objects only aware of what is "inside" of them. Examples:
		1) A room knows about the door on its north wall but not the room beyond the door.
		2) An item knows what is written on it but the "writing" knows nothing about the object it is written on
		3) A container knows its contents but items know nothing about the container they are in


CODING SPECIFICS:

- The value of the Item class:
	- Now that I have eliminated the 'takable' attribute from Item there is no attribute difference between Item and ViewOnly
	- the key functional difference is that Item has the take() and drop() methods
	- this is occasionally inconvenient because it makes it hard for me to give clear errors to reasonable requests (e.g. 'take water')
	- however, most of the time this is handy because it eliminates the need to handle all sorts of crazy requests (e.g. 'take castle')
	- Further, someday, I may want to add attributes to Items (e.g. some measure of carrying capacity)
	- So, in summary, I think it makes snese to keep Item and ViewOnly as separate classes - at least for now (10/23/2021)

- Standardizing obj-not-in-hand error (with error message) as a method of GameState:
	- Tried this and ended up going back to original "custom" approach with a simple boolean method
	- Was very conflicted re balance between less repitition vs. less readible & less customizable; Pondering
	- The code was more readable & customizable before; maybe implement a simple boolean function instead

- Moving the help() routine to cmd_exe():
	- During the creation of the IO sub-class (v3.80), I decided to centralize static data - including the word lists and dictionaries in interpreter() - to static_gbl.py and access it via get_str(), get_lst(), and get_dict() in IO. 
		- In the future, this will make it much easier to update the word lists / dicts via developer tooling
		- It also makes it easy to move the help() routine to cmd_exe() where it really belongs.
	- Historic info on the previous location of the help() routine:
		- Moving the help() function to interpreter():
			- The macro organization of the program is for interpreter() to interpret the players intent and for cmd_exe() to execute it
			- However, at the module level, the idea is that the interpreter() module is uniquely focussed on language semantics
			- The help() function is also (mostly) focussed on language semantics - specificly exposing them to the player
			- Moving help() to interpreter() also enables us to make all the static lists and dictionaries local to interpreter()
			- The balance between module-level structure and macro-program flow seems best served by moving the help() function to interpreter()

- Elimination of the 'magic word' ('xyzzy') trigger for startup()
	- Before v3.80 (where the IO su b-class was implemented), I only passed user_input from web_main() to app_main(). In web_main(), I checked to see if start_of_game was True and, if so, set user_input to a secret command ('xyzzy42') which then triggered calling startup() from app_main(). This had felt fun and clever and easter-egg-y... but ultimately it was sloppy code.
	- During v3.80 I tightend things up and just passed start_of_game to app_main().
	- I'm currently (v3.80) still processing the 'restart' command in web_main based on the user_output string and intend to fix this soon when I create the Ending as a subclass.
	- The moral of the story here is, where possible, trigger on variables, not strings.

DECISION: keep all the smarts in machine; lever only knows if it's up or down
DECISION: prefer shallow class inheritance tree over deep
DECISION: for now, only one trigger switch per machine... might want to add a 2nd at some point for a special puzzle

Burt as an object
- why?
	- allows elimination of attack_burt() method of Creature class
	- suddenly inventory becomes much more elegant
	- this is the way
- when?
	- Maybe make Burt an object before making all the machine changes??
	- this is a big refactor => do this first
- how?
	- Burt to be obj type Creature

- Old thinking => validate()
	- today: interp() =(if no interp_error)=> pre_action() => cmd_exe() => post_action()
		- this works if there is an interp() error or if the command is successful... but what if there is a cmd_error ???
		- as a work-around, I end up re-testing command validity in pre_action() / post_action() - or accepting buggy code (eat_biscuits_warning)
	- to-be: interp() =(if no interp_error)=> cmd_error_check =(if no cmd_error)=> pre_action() => cmd_exe() => post_action()
		- so in noun_class, every verb method needs to return cmd_error (boolean) and be able to run in 2 'modes': 'ec_mode' or 'exe_mode'
		- cmd_error_check() runs the method in ec_mode and returns cmd_error
		- if not cmd_error: cmd_exe() runs method in exe_mode
		- can likely shortcut for non '2word' and 'prep' cases
		- one side effect: every method needs to either throw text on error or do something on success... we cannot take an action on failure (?) 

###############
# static_gbl.py #
###############

static_gbl.py holds static_dict which, as the name implies, holds nearly all the static values of the game. These are mostly text descriptions for various objects but also include constants, like the game 'version', and dictionaries like 'score_dict'.

There are several advantages to having a centralized static dictionary:
1) Eliminates the overhead of managing a database for values that will never change.
2) Eventually, when I create a web interface for creating objects and descriptions, this makes it much easier to edit those static values.
3) Isolates static from dynamic data.

Historically, static_dict was once multiple dictionaries: descript_dict for object descriptions and static_dict for constants. There were also numerous local dictionaries in modules like score.py and ending.py (both of which themselves were eventually merged into subclasses of GameState). I eventually merged all of these into one dictionary named static_dict.

It is worth noting that there are 2 main areas of static descriptions / constants that have NOT been migrated to static_dict:
1) Error messages: for now, these remain embeded in code. This means that while it is easy to update object descriptions is is hard to update error messages... so in general error text should be as simple and broadly applicable as possible.
2) The lists and dictionaries from interp.py. interp.py needs a major over-haul and I expect this to be easier if I can reference these locally. Once I have fully updated interp.py, I intend to centralize these elements to static_dict.

Description Perspective:
- With burt being a creature and all methods being rewritten to work symetrically with Creature class, we have a choice. in theory, any creature could be used to play the game - and each might have its own description_dict. So each Creature could have it's own set of descriptions for every object in the game. This would be fun for a short session in a single room but is not practical for extended play. Realistically, nearly all descriptions will be from burt's perspective. 


###############
# validate.py #
###############

Brief history of validate():
    Originally, most errors were generated in cmd_exe(). This worked acceptably well right through v3.68 (precedural parity version). However, as coding progressed a couple issues made it clear this was non-ideal:
    
    1) Once timers were introduced, time tracking became important. Previously, errors and time were sort of intended to have a karmic relationship. The turn-counter was incremented for all input and then decremented when it appeared likely that an error was the interpreter's fault. This was inconsistent at best - but, once timers were introduced, it ceased to work at all. We couldn't have the hedgehog eating biscuits on an error turn. The short-term approach was to make Interpreter Errors untimed but Command Errors timed... but a better soluiton was desireable.
    
    2) The bigger problem was the more advanced use of pre_action machines. Machine code is usually triggered by a player command... but what if the command isn't valid? What if user_input == 'get sword' but Burt already has the sword? The upshot was having to put a 2nd set of error checking into Condition methods... which was crazy since error checking was already carefully coded into the verb error methods. Clearly a mechanism was needed to validate whether or not a command would be viable *before* it was executed.
    
    For both these reasons, validate() was inserted between interp() and pre_action() during refactoring. The idea is that every command is inspected in validate() and, if invalid, an error message is presented, validate() returns False, time is not incremented, and we ask the player for new input. We only ever reach cmd_exe() if validate() returns True.


###############
# gs_class_def.py #
###############

*** Module Documentation ***
Overview: 
gs_class_def.py defines the GameState class.

Implementation Detail:
GameState holds all of the non-object-specific attributes of the game (e.g. move_count). GameState is instantiated as gs in mk_def_pkl(). GameState itself holds no direct data and has no methods. Instead, its attributes are a series of modular classes (e.g. Core, End, IO, Map, Score) that hold relevant attributes and methods. GameState is an esential resource for nearly every function and method in the game and is heavily passed.

Historic Note:
The modular nature of GameState is relatively new and was not fully implemented until v3.83. Initially, GameState held a dictionary of values (state_dict) and all the methods for maintaining general game state. As the game grew in complexity, so did the GameState class. Eventually, it became unmanageable and existing elements started to be refactored into separate classes. This began with the Map class but didn't complete until v3.83 with Core class.

####################
# map_class_def.py #
####################

*** Module Documentation ***

Overview:
Stores the over-arching map of Dark Castle and provides methods for accessing and updating map info. Contains room_pairs and doors.

Implementation Detail:
map_lst is stored in GameState (rather than being a constant declared in the class) to allow for major terrain changes. For example, after a major cave-in the room description might change dramatically and three new passages might open up. One could make all these updates to the original room - but it would be far easier just to redirect to a new room. The most famous example of this behavior is the magic pencil used at the end of The Lurking Horror / Enchanter.

map_class_def() is also the home for any method that requires searching the entire map for an object. This is similar to the situation of searching for objects that don't know what container they're in - but the search for the hero object (via get_hero_rm() ) within Map was by far the most common case. My thinking had been to start of with a data normalization approach... and then de-normalizer (i.e. cache) for performance purposes down the road. So eventually, hero_rm became an attribute of Map. This was a case where the value was needed incredibly often - and was only updated in one place (the go() methed) - so the processing savings were likely vast. Before becomeing gs.map.get_hero_rm() this method was previously gs.get_room(). It's only purpose was to search the map for hero (i.e. Burt) and return the room that he resided in.

Historic Note:
Before refactoring, map_dict was an attribute of GameState and was a dictionary-of-dictionaries that was keyed off room and direction and returned next_room ast a value. Room.floor_lst contained doors and Room had an attribute, door_dict, that was keyed off direction and returned a door as its value. 

This worked fine but had a few logistical and philosphical flaws. Logistically, GameState was an ugly monolith. It had *way* too many methods. It was hard to keep track of them all. So it was high time to apply OOP to the operational aspects of the game and organize game state information into classes with methods that would then become attributes of GameState. Map became the first such operational object, in advance of migrating Burt to a Creature. The intention is to do the same for the rest of the operational capabilities in Game State.

The other issue was more about data design philosophy... There was a GameState map_dict entry for room_x that pointed to room_y, and a map_dict entry for room_y that pointed to room_x... but they were independent entries that seemed to imply that the connection was arbitrary. There were also separate door_dict entries for both room_x and room_y that each pointed to the same door that was between them - but again were in theory entirely independent. Lastly, the same door was in floor_lst of both rooms. As my theory of node hierarchy matured, it seemed "right" that there should be one and only one instance of every object... so why was there two of every door?

I considered making doors 'smart' and allowing them know about the rooms on either side of them. This was simple but it broke my rule that 'objects only know what they contain'. Also, it obviated the need for a central map, and I was convinced that a human-readible master map would be a valuable design aid. I even contemplated breaking doors in half... each side of the door would be contained in a given room and link back to a 'master door' that would maintain open and locked state for both. This had the attrictive capability of showing different features on each side of a door... but it seemed over-engineered and, again, eliminated the central map.

The eventual solution was the concept of 'room pairs' - the idea that the whole map is essentially comprised of pairs of rooms that are connected. And that in all but a few exceptional cases, if room_x leads to room_y, then room_y will lead to room_x - and that the door or passage between them will be contained uniquely and consistently within that pair. Based on this thinking I created a custom data structure: a list of room_pair dictionaries (I used a dictionary rather than a list for the sake of making the structure self-documenting). The structure requires a lot of custom methods to access - but this turned out to be a bit of a fun master class in list comprehension. Doors now appear once and only once in map_lst. Of course, now rooms appear multiple times, but for some reason this doesn't bother me. YMMV.


####################
# score_class_def.py #
####################

*** Module Documentation ***

Overview:
Score is a instance of score_def_class(). Score is an attribute of the GameState class. It stores the player's current score and a list of tupples that represent score points the player has already earned. Score also holds all of the methods that relate to determining and printing the player's score. Chief among these is disp_score().

Historic Notes & Implementation Detail:
The focus version the 3.81 was to refactor score() from a stand-alone module / funtion that was called via app_main() to a class that lived as an attribute of GameState (similar to the refactoring of Map and IO). During the refactoring, all dynamic values related to scoring (e.g. score and pts_earned_lst) became attributes of Score and all score-related methods were migrated from GameState and the old score() method into Score(). However, during the same refactoring, and in keeping with the current data centralization strategy, all of the static dictionaries and lists that kept track of which events were score-worthy were migrated to the central static_dict in static_gbl().

Prior to version 3.81, there were multiple static score lists and dictionaries to track different types of points that could be scored (e.g. a dictionary of objects that would score points when first found in Burt's inventory, a dictionary of rooms that would score points the first time Burt entered them, etc.). Also, there was a sepaarate dictionary that defined the value of the points earned when a score event occurred. During the refactoring, all of these data structures were consolidated into a single double dictionary. Perhaps more importantly, the keys / elements for both score_dict and pts_earned_lst were updated from single nouns to tupples that represented the verb, noun, and direct object of the scoring event (where dir_obj = None for non-prep verbs). These changes dramatically simplified score lookups and also enabled scoring distinction between events involving the same noun (e.g you could now assign points for both unlocking the front_gate and oepening the front_gate).

These data structure changes were partly drien by universal goals of simplicity and consistency. But they were also caused by a fundamental change in *what* was scored. Prior to version 3.81, the player's score was based on game state. Points were scored the first time that the rusty_key was found in Burt's inventory. As part of the v3.81 refactor, score events now became player commands and post-action results. In theory, game-state-based scoring seemed elegant and 'ground truth'. The problem was that this meant inpecting every scorable aspect of game state every turn - which seemed ineficient. Further, state could only be inspected via code - and this would mean creating more scoring code for every new type of object - which ultimately seemed unscalable. The solution was to base scoring events on player commands. These could be inspected easily in cmd_exe() via tupples holding ('verb_str', 'noun_str', 'dirobj_str') which solved the scaling issue. It also significantly reduced the score inspection required each turn. 

Philosphically, we are switching from scoring based on state to scoring based on player action. With this thinking in mind, there's no need to check for scoring in pre_act() or auto_act() (neither of which are directly caused by player action) - but we should check for score as a result of post_act(). For example, when Burt reads the kinging_scroll, the winning condition machine is triggered and, if all the conditions are met, the winning result is triggered and game_end becomes 'won'. We want this result to trigger the 'winning the game' points. To enable this, run_mach() is updated to pass result.name back to post_act(). In score_dict, the score condition tupple is represented as ('mach_name','result_name').

Since validate() ensures that we only reach cmd_exe() if the command is successful, we can, for most verbs, confidently assign score points once we get to cmd_exe(). But some verbs, even when successful, have variable outcomes (e.g. 'gvie', 'attack'). So, in disp_score(), we need to check each of these special verb cases for successful outcome (here we assume here that "success" means that that given object ends up in the target creature inventory and the attack target is removed from the game). In theory, this is, perhaps, not necessary. The game designer should, presumably, know whether a given attack or give command will result in the intended outcome... but this gets complicated - and could even change over the course of the game - so inspecting state for these special cases seems like the best case. An additional benefit of testing state for these complex cases is that we can now implement a wildcard option ('*') for dirobj_str. This is handy for cases like the 'attack hedgehog with x' - where any 'x' = weapon will lead to the hedgehog fleeing. In theory there could be 10 weapons in the game. We could code a -20 score for all 10 cases, but it is convenient to be able to code ('attack', 'hedgehog', '*') - which will equate to any dirobj_str that removes the hedgehog from the game is a scoring event.

One last minor tweak from v3.81 was that max_score went from being a static value in static_dict to dynamically generated on every usage. This has scalability advantages - max_score will automatically be updated as the game designer adds scoring events - seems a bit ineficient. In the future it would be nice to update max_score on every run of mk_def_pkl(), rather than every run of the game. This is in the backlog. Lastly, there is an underlying assumption here that all non-negative scoring events are available in a single game. This may not be the intent of every game designer but for now it seems like a reasonable premise.


####################
# end_class_def.py #
####################

*** Module Documentation ***

Overview:
The End class holds a couple essential attributes for the game ending: 'is_end' and 'game_ending' and the disp_end() method. End is instantiated in the game as 'end' in mk_def_pkl() which is, itself, an attribute of gs (the instantiation of GameState).

is_end is a boolean that tracks whether the game will end after the current turn. This value is ultimately passed back to web_main() and governs the while loop that propels that game forward each turn.

game_ending is a string that does double duty. It can have the values of 'quit.', 'died.', 'restarted.', or 'won!'. and is used both as a declarative statement regarding how the game ended f"You have {game_ending}" and also to trigger the game credits in the case of game_ending == 'won!' .

The purpose of disp_end() is to buffer the appropriate end-of-game text. This includes calculating and buffering the player's title which is based on their score.

Implementation Detail / Historic Note:
Like Score, IO, and Map, a large portion of the End class was once embeded directly in GameState prior to version 3.81. As part of the GameState modularization effort, it became it's own class. end_of_game became is_end (following my official naming convention for booleans) and both it and game_ending were pulled out fo gs.state_dict and made attributes of gs.end(). disp_end had previously been named end() and had lived in its own module named ending(). ending() had at one time held the titles_by_score dictionary but this was centralized into static_dict in static_global() before 3.81.

In prior variations, end() had a number of purposes and was not consistently called. During refactoring I realized that its only job was display-oriented and renamed it as such. At the same time I incorporated restart into the cases that could trigger disp_end (this is not actually an is_end case but it is the ending of the current game).

Under the current implementation, when an end-of-game condition is met (presently only 'quit' and 'restart' in app_main(), attack() in Creature, and one case of result_exe() ) is_ending is set (except for the restart case), game_ending is set, and disp_end() is called.

I also took the refactor opportunity to put a conditional in front of auto_act in app_main() so that there was no chance an auto-action would run after the player ending text.


##########################
# invisible_class_def.py #
##########################

*** Module Documentation ***

* Invisible class:
	
	Overview:
		'name' is a text string that represents the canonical name of an object. It should be identical to the declared object label, unique, and immutable. For object rusty_key, rusty_key.name = 'rusty_key'. For reasons that remain a little murky to my beginner brain, objects in Python have no way of actually knowing their own names. As I understand it, object names are merely labels that are pointers to the actual object... and the object itself has no idea what labels are pointing to it at any given time. In any case, the perceived wisdom is that if you want to be able to reference an object by its name, you'd better give it a name attribute - hence 'name'.
		
		The object tree of Dark Castle forks from Invisible. One trunk leads to Writing, then ViewOnly, and then all the other visible objects in the game that Burt can interct with. The other trunk leads to a collection of invisible objects that manage the automated behavior of the game. It might surprise a player of Dark Castle to learn that there are about as many invisible objects in the game as there are visible ones. However if you inspect the take() method you'll see that there's no code there that could trigger the royal_hedgehog to guard the shiny_sword. Likewise, there's no code in go() that could tell Burt about the Rusty Key when he tries to head south from the Entrance. These behaviors and many more are all enabled by invisible objects. See mach_class_def() for more information on these objects.

	Program Architecture:
		Becase Invisible is the root of the class inheritance tree and is also a class from which no objects are directly instantiated, it is the ideal place for methods that should always be available. There are 2 main classes of these:
			
			1) Class Identity Methods: these are the simple class identifyer methods (e.g. is_item() ) that returns True or False and which Dark Castle uses to verrify whether an object belongs to a given class. Within each class in the inheritance tree, the appropriate Class Identity Method is over-ridden with True but in Invisible, all of them are (except is_invisible() ) are set to False.

			2) The Error Sub-System. This is where Method Mis-Match errors are handled for all verb methods. The Error Sub-System spans the whole of Dark Castle but the foundation is laid in Invisible so this is a good place to discuss how it works. It's covered in more detail than anyone but myself could possibly desire in a section of its own.

* Error Sub-System
	- Overview:
		Handling incorrect commands is an innate requirement of any text adventure. The error subsystem performs this duty.

	- Game Design:
		The Purpose of Errors:
			There are vastly more wrong command strings that can be given than right ones. When the valid command set is small enough, it works to simply accept the correct commands and throw a generic error on everything else. But as the vocabulary grows, the opportunity for genuine mis-wordings increses exponentially (e.g. if Burt can 'enter Throne', why can't he 'enter Moat' ??). At this point, the error sub-system becomes responsible for providing verb usage guidance. Lastly, anyone who plays the full game will recieve quite a few errors - so, in addition to being instructive, errors should also be varried, fun, and amusing.

		Error Hierarchy:
			Along with providing guidance and humor, the error sub-system should present the player with the intuitively most obvious issue concerning their proposed action. For example, suppose the players issues the command "unlock gate with silver key". There could be several reasons why this command doesn't succeed: Maybe you aren't holding the key. Maybe the door is already open (in Dark Castle you can't lock or unlock an open door). Maybe the Silver Key is the wrong key for the Gate. In fact, all three of these could be true at once. But we only want to throw one error - and we want that error to reflect the "most obvious" problem (in this case, the fact that you aren't holding the Silver Key that you intended to unlock the Gate with).

			The error hierarchy for a given class can be intricate and even debatable (in the above example, one could argue that the door being open is a more obvious issue than not having the Silver Key in hand). But for most verbs there are some broad initial errors (these are the Generic Command Errors described under Implementation Details) to check that have a standard hierarchy:
				1. A referenced object is not visible in the room
				2. A referenced object is of class Writing (and the command is not read() )
				3. A referenced object is not in reach (for example, because Burt is in a Seat)
				4. A referenced object is not a member of the verb method class but merrits a custom error (e.g. take(obj) where obj is of class Liquid)
				5. A referenced object is not a member of the verb method class (generic case). (e.g. take(obj) where obj is not of class Item)

		Errors Are for User Input:
			One of the issues with traditional text adventures like Zork is that they are often set in vest empty terrains. The Great Underground Empire is fascinating... but nearly devoid of life. I suspect the reason for this is simple: programming creatures is hard. One of my goals is for Dark Castle to feel more "lived in" than Zork... so I intend to make all verb methods "symetric" - meaning that they can optionally take 'creature' as an arguemnt and can be used for any creature in the game - not just Burt. Hopefully, this makes programming creatures easier and encourages a more populous dungeon. 
			
			However, there are limits. Errors are tricky. Creatures are tricky. For now at least, throwing gramatically accurate errors for non-Burt creatures is simply out of scope. For non-Burt creatures, errors should be silencable (future feature) - but if not silenced, they will appear to be directed at the user - and at Burt in particular - in second person tense. It is up to the Implementor to avoid programming other creatures to perform error generating tasks!

	- Implementation Detail:
		There are 3 Error Types:

			1) Interpreter Errors: The interpreter is unclear what command the player is trying to issue. These are usually caused by the limitations of the interpreter. The user needs feedback on what command format or vocabulary the interpreter can handle.
			
			2) Validation Errors: The command is understood but cannot be carried out. Often caused by 'silly' (e.g. 'take moat') commands but sometimes simply by interpreter limiations (e.g. 'unlock castle with key'). The user needs feedback on how each command can be used and what actions are possible in the game world. Validation error response comprises the vast majority of the error sub-system.

			3) Command Errors: The command is understood and not erronious - but cannot be performmed. Almost always a programming error.
		
		There are 4 flavors of Validaation Error:
			1) Generic Validation Errors: Command failure cases that occur across multiple methods. e.g. very few commands will run if the noun of the command is not in the room's scope. Catching these errors in err_std() avoids needing to re-write the same error-checking code repeatedly in multiple methods.
			
			2) Custom Validation Errors: Command failure cases specific to a given method. e.g. Burt tries to unlock a container with the wrong key. This is a specific type of error that is best addressed in the specific unlock_err() method in invisible(). The error text is buffered and the fail condition is returned to validate() - which then returns False to app_main() - so that no command is actually run.
			
			3) Generic Method Mis-Match Errors: The player attempts to use a method on an incompatible object. These are usually acts of experimentation or silliness on the player's part. e.g. when Burt tries to 'take castle' no one really expects the command to work. So we throw an appropriately snide error.
			
			4) Custom Method Mis-Match Errors: In a few specific cases, player confusion over which methods can be used with which objects is quite justified. e.g. it's not unreasonable for the player to attempt to take the 'water'. In these cases we give an explanitory error in take_err() in invisible() for the specific error case of taking a liquid.

		No actions should be performed via errors:
			As a general rule, no actions should be taken - and no in-game information should be provided - via errors. The error sub-system is intended as a 'pre-check' for user commands, which then aborts from command execution if the command is not valid. Time does not pass on error-generating turns and there are no pre-actions, post-actions, or auto-actions. 

			While it is technically possible to update object state within error code, this is not intended and should be avoided. If a state change will be triggered, it should be handeled within the class verb method - or possibly by a modular machine. Ideally, the same would be true for providing in-game information (e.g. examine() or read() ). An exception to this rule can be made for game meta-information where the player appears to need a usage hint (e.g. "use read() rather than examine() on objects of class Writing"). 

		Debug functionality:
			At long last - which is to say, long after I should have - I've introduced a debug feature to the Dark Castle code base. In early versions of the game, miscelaneous Validation Errors that didn't match common pattern types were caught via a 'try... except...' clause in cmd_exe() (and later in validate() ) and a random "what are yout talking about?!" type error would be presented to the user. This had the advantage of ensuring that there was a response to any user command no matter how absurd... but it also masked real errors that came up during coding. As a result, I was constantly having to disable the 'try... except...' clause manually - which was a pain. Under the new error subsystem, very few actual user command-based errors should ever make it through to the 'except' statement... but it is foolhardy to underderestimate the ability of end users to find novel ways of generating abends - so the 'try... except...' and random errors still remaain. But now there is a debug mode that the developer can drop into using 'debug_<secret code>'. In debug mode, the developer will see that actual error code - rather than a random snarky response. Also, each error is pre-fixed with the name of the module ([INTERP], [VAL], or [CMD]) that generated it. 

		The potential perils of pre_action() with c'md_override == False':
			pre_action() enables the game to take an action after the player has submitted their intended action but *before* the action takes place. Example: in the Entrance Hall, the user types 'get sword' but, before that action can take place, the Hedgehog charges forward to defend the Shiny Sword. pre_action() returns the cmd_override boolean. 'cmd_override == True' indicates that the player's intended command is negated (overriden) by the game's pre_action. This holds in the case above - where because of the Hedgehog's actions, the 'take sword' command is no longer taken. However, if 'cmd_override == False', the game's pre_action behavior takes place and then the user's command is also executed. 
			
			There are times when this can make perfect sense - perhaps a pre-action just generates and amusing sound effect - but it can also be hazardous! This is because, once we get past the validate() routine, there is no additional error checking performmed within the game. So if the game's pre_action command somehow interfere's with the player's command the two will collide with unpredictable results. Example: Suppose the player says 'take McGuffin', but this triggers a pre_action() with 'cmd_override == False' that takes the same McGuffin. When those events coincide, there will be no check in cmd_exe() to ensure that the McGuffin is still there. The command was valid when validate() inspected it so cmd_exe() will blithly attempt to take the (now absent) McGuffin - likely with game-crashing results.

			The safest course is to *ALWAYS* use 'cmd_override == True'. You have been warned!

	- Program Architecture:
		We need to deal with two main variants of Validate Errors: 1) Custom Validate Errors that are are specific to the verb method and its class and 2) Those errors that are based on Method Mis-Match or are Generic in nature. 
		
		Invisible is the top of the class inheritance tree. So this is an obvious place to catch both types of error. This allows us to address method mis-matches. As a result, every verb method has an error block (<verb>_err) in invisible() that deals with Method Mis-Match Errors, Generic Command Errors, and Custom Validate Errors. The Invisible error code block returns True to validate() if there is an error and Falso on no errors. 

		This structure is perhaps a bit heavy-handed but it has the following advantages:
		
			1) All Validate Errors are generated in only one code block

			2) Re-use of the Generic Validation Error / Method Mis-Match Error code block when checking for Custom Validate Errors

			3) Because all Validate Errors are called within invisible(), Custom Method Mis-Match errors can easily be generated based on referenced object class.

	- A Not-so-Brief History of Error Handling:
		From the start, the verb methods themselves were the home for all Generic and Custom Command Errors. I addressed Method Mis-Match cases in cmd_exe() where I simply wrapped the verb method call in a try... except... routine that called a random, non-specific, humorous error. 
		
		However, as time passed, and I created more verb methods - and periodically went back to refactor them - the repetition of Generic Command Errors began to bother me. Also, the unfairness of the Custom Method Mis-Match cases (especially examine() for Writing) became clearer. So I began to look for a central pre-verb-method "home" for these error checks.

		Originally, cmd_exe() fit this purpose. I simply checked for the Generic Command Error cases and the Custom Method Mis-Match cases in advance of the try... except... verb method call.
		
		This worked acceptably well right through v3.68 (precedural parity version). However, as coding progressed a couple issues made it clear this was non-ideal:

			1) Once timers were introduced, time tracking became important.	

			2) The bigger problem was the more advanced use of pre_action machines. (see validte() for more info)

		For both these reasons, validate() was inserted between interp() and pre_action() during refactoring and became the new home for Generic Command Errors, Generic Method Mis-Match Errors, and Custom Method Mis-Match Errors.

		Over time, it began to click for me that a better solutino for Custom Method Mis-Match Errors was to instantiate them in the problem class. So in created a separate take() method in class Liquid that did nothing but throw an error explaining the the use that they were not able to 'take' a liquid and recommending that they try 'drink' instead. Of course, for this to work, I needed to exclude these special cases from any general Method Mis-Match cases that were handled in validate().

		Also, around this time, I began repalying Hollywood Hijinx with my youngest son, Joshua. I'd never played it all the way through before and we had a lot of fun solving it (though I did need hints on both the penguin and the buzz saw - both of which felt like iffy puzzles to me). In playing it I was reminded that Infocom did a nice job of throwing verb-specific errors... where-as Dark Castle still threw generic "Burt, I have no idea what you're talking about" errors for the vast majority of Method Mis-Matches.

		So, this was the state of DC errors when I started coding the Seat class... which required a whole slew of new Generic Command errors. Here, the complexity sins of my past caught up with me. I had error messages being triggered from interp(), validate(), verb classes, and non-verb classes. I struggled repeatedly to troubleshoot bugs because I couldn't easily figure out which bit of code (false) errors were getting triggered from. I eventually got class Seat working but I was so frustrated with the error situation that I pushed off the othe work I had been planning to do and immediately started working on the (hoefully) comprehensive and systemic error solution. I initially put the foundation of the Error Sub-System in Writing (the highest visible class in the inheritance tree), but quickly realized that Invisible wouild be a better home. Also, I initially kept verb-specific errors in the same block as the commands and called the generic error block in invisble() from there - but it soon became clear that a single error block in invisilbe for all code made more sense.


#####################
# base_class_def.ph #
#####################

*** Module Documentation ***

* Writing class:

	Overview:
		It may seem counter-intuitive that the first visible object class in the hierarchy is Writing - but when one remembers that all other visible objects can have Writing as an attribute the order makes sense. As the first class that Burt can interactive, Writing introduces three critical attributes:
				
			full_name is a text string that represents the object name the player will see. the full_name for object rusty_key is 'Rusty Key'. All object full_names are capitalized as a convention intended to help players recognize which entities in the room descriptions they can interact with.
			
			root_name is a text string that represents the one-word "short name" for an object. The root_name for object rusty_key is 'key'. The player can refer to the object by its root_name so long as there are no other visible objects with the same root_name. root_name is used within the interpreter().
			
			descript_key is a text string that is used to lookup the description of an object (or in the case of the Writing class, the text of an object) in static_dict. By default, descript_key == name (i.e. the descript_key for object rusty_key is 'rusty_key'). However, by making descript_key and independent attribute from name, we enable the descriptions (or text) associated with an object to change over time. 

	Implementation Detail:
		It is worth noting that writing is treated a bit differently than other 'noun' objects. Writing is not treated as being 'contained' in the object it is written on. Instead it is treated as an object 'Condition' (similar to a Door being open or closed) and as such it can only be observed via the examine() method. This is partly to avoid over-cluttering the room descriptions and partly to provide a sense of discovery when an object is examined. Also, I picture Burt needing to peer closely at writing to make it out in the dim lantern light. See the ViewOnly examine() doc_string for details on Active vs. Passive Observation.
		
	Game Design:
		The introduction of descript_key is a good time to say a word about descriptions in general: they are the heart of Interactive Fiction. If you've ever read an IF walk-through it is dull as dust - because the interpreter's vocabulary is tiny and the commands to play the game are simple and repetative. It's the descriptions and the writing that create the illusion of a complex world. 
		
		Zork itself was often accused of 'purple prose' - which some claimed was all the more egrigious a sin given that the Zork interpreter could only understand a minute fraction of the words in its descriptions. I disagre with - yay verilly, gainsay! - this trait being claimed a fault. Now more than ever, anyone who's playing a text adventure game must have a deep and abiding love of words. Let us lean in and double-down on the 'purple-prose' and paint our digital landscapes with intense and vivid language - hopefully to the delight of logophiles and philologists the world over!

	Historic Note:
		The tradition of copous writing samples in text adventures dates right back to Zork itself. In Zork the first interactive object you come across is a mailbox. And within the mailbox is a leaflet you can read and which welcomes you to the game. Dark Castle cleaved tightly to this tradition. From the earliest implementation, the front_gaate had rusty_lettering... which is both a reference to the similar gates of hades in Zork I and of course a nod to good ol' Dante.


- get_str() method [IO class]:

	Overview:
		One might reasonably think that getting the description of an object would be a simple matter of looking up obj.descript_key in static_dict. This does indeed work the vast majority of the time. And because an object's descript_key is independent of its canonical 'name', we can can change the value of descript_key (and therefore the description value) any time we want to. However, it should be noted that static_dict lives in a module name static_gbl() - so named because all of its contents are indeed static. This is extremely useful logisticaly. It means that we never need to worry about saving any of the text in static_dict - because it never changes. Instead we just change obj.descript_key and point to a different ready-made static_dict value. Alternatively, if we need to dynamically generate a description, we can do that within a method based on current GameState (e.g. the description provided by inventory() ).
		
		But what if we want to dynamically generate a description *once* and then be able to reference it again in the future? An example of this is the 'secret code' on the guard_goblin's torn_note. We generate a random value between 0 and 7 for the iron_portcullis at the beginning of the game in start_up() and save that value to control_panel state... but how do we store the description for messy_handwriting? There are only 8 possible values so we could have 8 static dictionary entries in static_dict - but a general solution to the problem seems desireable. My approach is to keep a small dyn_dict in GameState where it is saved every turn. Then whenever we examine() or read() we try looking up obj.descript_key in dyn_dict first. If this fails, then we check the static static_dict. Hence the need for get_str() in IO.

		In the initial implementation of get_str(), only read() and examine() called get_str(). Many other methods simply accessed static_dict[] directly. During the creation of the IO subclass (v3.80) get_str() was moved from the Writing class to the IO class and all static_dict[] refs were reidirected to io.get_str(). The goal here was to abstract the static data layer so that it can be changed to multiple dictionaries or a database as needed in the future. My current, long-term, persistance strategy is to eventually store all dynamic data (i.e. object attribute values and the contents of dyn_dict) in a NoSQL DB and keep the static content in a single large dictionary - but this plan could evolve.


- read() method [Writing class]:

	Overview:
		Read is the first player-accessible method. For the reasons mentioned above in Writing, writing objects are treated a bit differently than other 'nouns' and therefore the error checking in read() is a bit different as well (writing has it's own unique scope check method, chk_wrt_is_vis). 


* ViewOnly class:

	Overview:
		ViewOnly is the most basic class that represents actual entities in the Dark Castle world. It introduces the all-important examine() method. However, the take() method is not yet defined so there's no hazard that Burt will make off with a ViewOnly object. This is actually quite handy. Adventures are inveterate pillagers but with ViewOnly you can be sure that an object will stay where you put it.
		
		Because the writing attribute is introduced in the ViewOnly class, any object that Burt can see is capable of holding text. I originally debated this approach. Of all attributes, writing is probably the one most often set to None. This seemed like a good case for a MixIn class... but then it became clear that I would have at least one member of nearly every class that had writing on it. Two versions of every class - one with writing and one without - certainly didn't seem desirable. Also, I often found myself adding text to objects later on as I realized that a puzzle was too obscure (e.g. the small_printing on the grimy_axe). As of v3.70 there's no conversation in the game - and none likly in the near future - so often it's left to writing to make the Dark Castle world feel explicable and lived in. Ultimately, in a game based on words, enabling lots of in-game text turns out to be pretty important.


- examine() method [ViewOnly class]:

	Overview:
		examine() is the most fundamental command for gameplay and is the second method available for visible objects after read(). ViewOnly is the ancestor of all visible classes except Writing so the examine() method operates across quite a few different classes.

	Program Architecture:
		"Saparation of content and presentation" is an age-old programming saw - and rightly so. I embrace this mantra in Dark Castle by having a standard set of 'display' methods (disp_cond(), disp_writing(), and disp_contain() ) who's purpose is to buffer game-world information when an object is examined. This allows me to vary the 'condition' text based on the class (e.e. for a Door, condition = "open" or "closed"; for a LeverSwitch, condition = "up" or "down"). It also allows me to customize descriptions related to the burt Creature object (e.g. since burt is the observer, he is never included in the "look" / "examine <room>" 'contain' list. Also, "inventory" / "i" / "examine burt" does provide a 'contain' list of burt's bkpk_lst - since burt is able to look in his own backpack). Down the road, isolated display methods called from examine should also make it easier to enable or disable part of the examine() output based on settings like 'brief' and 'verbose'. The down side to this formal approach is that the descriptions have a bulleted feel and are hard to unify into paragraphs.

		However, isolated display methods also create their own set of problems. The aesthetic goal of Dark Castle is to feel book-like and present information in traditional paragraph format. But the default presentation that results from isolated dispaly methods is a series of one-line sentences (e.g. "There is a goblin here.", "The goblin is holding: Grimy Axe.", "The goblin is wearing: Big Medal.") each separated by a line of space. It ends up feeling more like a Twitter feed than a book. To solve this I needed to start checking each object to determine which examine() elements it included (has_cond(), has_writing(), has_contain() ). I also needed to enlarge the buffer options from just buffer() (which is equivalent to <cr><text><cr>) to also including buff_no_cr() and buff_cr(). As always, the UI was more work than expected, but the results are now a bit more paragraph like.
	
	Game Design:
		The examine() method is probably as good a place as anywhere to discuss the game design intentions of what Burt sees and how he sees it. In the Room method we will delve into the notion of node hierarchy - which is also related to what Burt sees - but for now we'll ignore nodes and speak in generalities.
		
		Let's start with *what* burt can see. There are many Python classes of visible objects. But from a description perspective there are basically only two *types* of visible object:
				
			Interactive Objects: These are objects that Burt can somehow interact with. This includes all Items, Doors, Containers, Switches, Creatures, and, every once in a while, a ViewOnly object. Solving puzzles and winning the game requires Burt to manipulate Interactive Objects.
			
			Descriptive Objects: These are always ViewOnly. In fact, most ViewOnly objects are Descriptive Objects. Burt can never manipulate Descriptive Objects and the whole game could be played through without ever paying any attention to them. They exist only to provide a bit of narrative color, to offer some in-game hints, and to provide some geeky humor. In Rooms and Creatures, ViewOnly Descriptive Objects are stored in the feature_lst attribute. Examples of Descriptive Objects include: dark_castle, moat, faded_tapestries, alcove, stone_coffer, and family_tree.
				
		Now lets talk about the two types of observation that Burt can engage in:
		
			Passive Observaation: This is what happens when Burt uses 'look' to examine a room or 'inventory' to examine himself. The game design goal of Passive Observaation is to provide the player with a broad awareness of what they can currently do in the game. To this end, 'look' + 'inventory' provide a listing of all Interactive Objects currently visible to Burt. However we don't want to drown the player in details every time they 'look' and we do want to encourage them to explore the Dark Castle world closely. So object Descriptions, Writing, and Conditions are not provided via Passive Observation. Also, Passive Observation does not provide a listing of Descriptive Objects - they are only mentioned in object Descriptions and must then be explicitly examined.
			
			Active Observation:  This is when Burt is examining a specific object. e.g. 'examine the front gate'. Burt can only examine one object at a time. The idea is that he is inspecting the object closely. Active Observaation will provide the following:
				- The object Title (rooms only)
				- The object Description
				- The object Condition (i.e. open, closed, up, down, empty, etc)
				- Writing on the object
				- A List of any Interactive Objects 'contained' within the examined object (including objects held / worn by Creatures)
				The intent of this ordering is that first we learn everything we can from inspecting a given object - and then we learn more about any objects it may contain.

			The hope is that, for the player, all of this theory results in intuitive game play. When you want a list of the 'stuff' in a room you 'look'... when you want to know everything about a specific object you 'examine' it... descriptions should be read carefully because, occasionally, they include references to things you can look at that aren't mentioned otherwise... But if you're actually reading through the code and wondering "Why aren't Writing objects, the state of Doors, or most ViewOnly objects listed via 'look' or 'inventory'?" - well, now you know.

	Historic Note:
		Originally, examine() was extended by most classes and there was no clear definition of what Burt saw when he examined an object. Codifying what was presented by examine() seemed valuable so I broke it into parts (Title, Description, Condition, Writing, Contained) and defined functions for those in each class. 


##################
# item_class_def #
##################

*** Module Documentation ***

* Item class:
	Attributes:
		- weight: The Item class has the 'weight' attribute. Containers and Creatures can be limited in the weight (max_weight) or number (max_count) of items they can hold. In modern IF, inventory constraints are considered "old school" but I am, after all, largely modeling after two old-school Infocom games, Zork and Enchanter, both of which make heavy use of Inventory limitationss. The weight attribute also enables physics-based puzzes, crawl-space travel restrictions (which enhance the feel of peril), and the sense of realism provided by finite capacity.

	Implementation Detail:
		All objects of class Item are takable - there's no 'is_takable' attribute to prevent this. To temporarily prevent an Item from being taken you could:
			1) Initially provide a ViewOnly object and then, when appropriate, swap in an Item object with the same full_name
			2) Prevent the take() method via a Warning
			3) Prevent the take() method via a Modular Machine
	
	Game Design:
		Adventurers love Items. This tradition dates back to Zork I itself, where the sole mission of the game was to collect 20 (or 19, depending on how you count) treasures and safely store them in a trophy case. Although Dark Castle theoretically follows the Enchanter tradition of saving the land, truthfully, Burt showed up at Dark Castle to score some loot and that desire is never far from his heart. Good game design leverages this love of Items. 
		
		Want to intrigue and excite an Adventurer? Show them an out-of-reach Item. Want to infuriate an Adventurer? Pilfer their hard won Items! Want to make a puzzle hard? Require that the Adventurer surrender an Item to solve it. Dark Castle leans in heavily on each of these standard Adventurer manipulation techniques.
	
- take() method [Item class]:

	Implementation Detail:
		take() used to be a more complex method. Adding the object into Burt's hand is trivial but finding where to remove it from takes some serching. I initially did all that searching in take(). During refactoring it became clear that it made sense to do this in Room instead since the Room class is already responsible for providing visible object scope and therefore is already required to know all the places an object could be.
		
		I initially thought that the 'Can't take another creature's stuff' error would be a great use case for the any(if x == y for x in z) pattern. This proved to be incorrect. For one thing, the any() pattern is a one-liner - so 'x' does not exist outside that line - but I need it for the error message on the next line. Also, curiously, it turns out that Python's magic ability to have an 'if x and y' statement where 'y' can be undefined so long as 'x' is False does not work within any(). Code and learn!
		
		It may initially be surprising how few tests we need to conduct before performing the method. The logic works as follows:
			1) We confirm that 'obj' is visible to Burt in validate()
			2) 'obj' must either be of class Item or inherit from class Item or else the method could not run
			3) Local error checking ensures that 'obj' is not already in Burt's hand or held / worn by another creature
			4) Therefore, 'obj' must be a takable Item!


# Food class:

	Overview: 
		Food currently has no purpose in the game other than to distract the hedgehog and provide some color. But I eventually envision creating an old-school game like Enchanter where Burt needs to keep eating and hydrating as he plays the game. This will eventually require that food have a quantity attribute (i.e. it takes 3 bites to finish the stale_biscuits) which can be percieved via examine() as a condition.


# Liquid class:
	Overview: Liquids and drinking them currently have no purpose in the game but in future versions I intend to implement food and drink requirements similar to those in Enchanter. I also plan to eventually implement a pour() verb method that allows Burt to do more with water than just drink() it.

	
# Garment class:

	Overview:
		The Garment class was initially named Clothing and, originally, was only used to enable the royal_crown to be worn. But as the Creature class came more into focus, I made the decision that I wanted Dark Castle to be more vibrantly inhabited than Zork or Enchanter. Since  conversation in IF is extremely challenging, this meant providing more clues to the player about the personality and needs of creatures that Burt meets. Clothing became a key mechanism to display these traits.

	Implementation Detail:
		For magic garments, like the royal_crown, we want to provide a clue to the player that the garment has special powers. When using the wear() command this is easy. But, for reasons explained under Program Architecture, I decided that there should be no remove() command. Instead, to remove a garment, Burt would just take it. I still wanted to alert that player that the magic effects of the royal_crown had ceased when the garment was removed - but this meant distinguishing between 'take royal_crown' (from the floor_lst) and 'take royal_crown' (from burt's worn_lst).
		
		This made linking the magic power alerts to the Creature worn_list_append() and worn_lst_remove() methods very tempting. But, here too, we run into an issue: the long-term goal for Dark Castle as a toolset is to enable every verb method to be executable for any creature. In some cases, the creature may not even be in the same room as Burt... so we need to be able to silence user feedback from a verb method when appropriate.
		
		The upshot of all this pondering is taht I ended up incorporating the alert-on-removing-garment into the take() method using the chk_is_worn() method. The key take-away from this thought process is:

		"All user output from verb actions MUST be centralized in the verb method!"

	Program Architecture:
		We usually focus on the reasons for the solutions we have implemented. But sometimes, the most important decisions are about what we choose NOT to do - and why. After creating the wear() method it seemed very natural to create a remove() method. Not only did it make alerting players to the royal_crown's magic powers easy, it also felt like natural language... when we take off an article of clothing we 'remove' it. And lastly, it increased the verb-count of Dark Castle... which feels like an innately good metric to increase in an interpreter-driven game.
		
		But there's a catch... how should remove() work for non-Garment objects? Can you remove() an object from a room's floor? If so, then remove() is actually just an oddly-chosen synonym for take (just like 'get') and does nothing to solve our alert-on-removing-garment problem. Alternatively, maybe remove() only works for class Garment... and it seems fair to throw an error on 'removing' an object from the floor... but what about 'remove kinging_scroll from crystal_box'? That absolutely sounds like valid usage. And while we're at it, what about 'removing' something from Burt's hand? Language usage gets frought fast! 
		
		Ultimately, the alternative to having remove() be a synonym for take() is to make it only work for class Garment. But this latter option is far from ideal. The underlying driver behind increasing Dark Castle's verb count is a less artificial language interaction... but the only thing more artificial than a small verb-count is a bunch of general-purpose verbs that can only ever be used in very narrowly defined contexts.

		The result of this thinking is that remove() was eliminated as a verb - if burt wants to take off a garment he just uses the take() command. The broader mantra that accompanies this decision is:

		"When in doubt, expand the applicability of existing verbs rather than co-opting new general-purpose verbs for narrow purposes."


# Weapon class:

	Overview:
		Unlike Zork, which embraced a D&D-style dice-rolling approach to combat, in Dark Castle, fights are decided by pure logic. If Burt attacks a particular creature with a particular object, he will prefail. However, it seems fitting that some objects (shiny_sword, grimy_axe) are innately more likely to be effective than others (stale_biscuits, cheese_wedge, rusty_key). You can attack with the latter but the results are more likely to be comical than deadly.

		The Weapon class also includes the attribute desc_lst, which provides elaborate verbs and adjectives for your attack.


############################
# interactive_class_def.py #
############################

*** Module Documentation ***

* Module Overview *
	
'interactive' is a vauge term. Hopefully I'll think of a better module name down the road. But the intent is along the vein of 'standardized and prepositionally / combinatorally, interactive'. Hence, not foundational classes like ViewOnly or Item. Not custom objects like Machines. Not classes like Food and Liquid for which there are highly specific, non-combinatorial verb methods (eat() and drink() respectively). Rather, the goal here is to address objects like doors, surfaces, and containers... which all operate in a standard fashion but potentially have some functionality overlap (e.g. doors and containers both open, surfaces and containers both hold Items, etc).

In early DCv3 versions I treated this as an inheritance chain of monolithic classes: Surface inherited from Container which inherited from Door (in fact, all of these classes lived in a module named door_class_def() ). This approach worked but wasn't very elegant - by the time you got to Surface, all of the attributes related to openning and locking had to be set to None. Ditto for doors and containers without locks. And portable containers were sketchy at best. The final straw was my attempt to add a 'weight' attribute to the Item class. The already sketchy implementation of portable containers completely broke down. It was time for a fresh start.

Durring refactoring I took a new approach: I created MixIn classes for 'openable', 'lockable', and 'contains'. Then noun classes were built by combining ViewOnly or Item with one or more MixIn.

* Current MixIn Classes:
	- OpenableMixIn
		attributes = is_open
		methods = 
			- open()
			- close()
	- LockableMixIn
		attributes = 
			- is_unlocked
			- key
		methods =
			- lock()
			- unlock()
	- ContainsMixIn
		attributes = 
			- contain_lst
			- max_weight
			- max_obj
			- prep
		methods = put()

* Current Generic Noun Classes:
	- DoorSimple = ViewOnly + OpenableMixIn
		examples = screen_door
	- DoorLockable = DoorSimple + LockableMixIn
		examples = front_gate
	- ContainerFixedSimple = ViewOnly + ContainsMixIn
		examples = wooden_shelf or stone_coffer
	- ContainerFixedLidded = ContainerFixedSimple + OpenableMixIn
		examples = cardbaord_box
	- ContainerFixedLockable = ContainerFixedLidded + LockableMixIn
		examples = crystal_box
	- ContainerPortableSimple = Item + ContainsMixIn
		examples = small_barrel or silver_tray
		methods =
			- put() extension to address weight
			- remove_item() extension to address weight
			- chk_content_prohibited() extension to prohibit portable containers
	- ContainerPortableLidded = ContainerPortableSimple + OpenableMixIn 
		examples = red_shoebox
	- ContainerPortableLockable = ContainerPortableLidded + LockableMixIn
		examples = black_suitcase
	
* Current Custom Noun Classes:
	- Seat (I know, the naming goes a bit sideways here) = ContainerFixedSimple for Creatures
		examples = test_chair
		attributes = in_reach_lst
		methods = 
			- chk_content_prohibited() over-ride to allow creatures
			- enter()
			- exit()

			
*** MixIn Classes
* OpenableMixIn class:
	- Overview:
		An openable object can be opened and closed. In doing so, the player may reveal either a new passage or one or more new objects to investigate. The most fundamental openable object is the Door. Finding a way to open a door is one of the most basic puzzle elements in interactive fiction.

		Most containers can also be openned and closed. By implementing the open and close functionality as a MixIn, the same code can be applied to many different base objects - from imposing locked-and-barred front gates to champagne bottles.

	- Class Attributes:
		OpenableMixIn has a single attribute: 'is_open'. 'is_open' is a boolean which can be either True or False (None, was a valid value in the Door class but is no longer supported or used).
		
	- open() and close() methods [OpenaableMixIn class]:
		Overview:
			open() and close() are quite simple. When called, they set the state of the is_open attribute to True or False respectively and provide confirmational output. Most of the heavy lifting gets done in open_err() and close_err() which check for obj which are not opennable / closeable, or are already openned or closed, or are locked.
	
		Implementation Detail:
			For the purposes of examine(), an Openable object has a 'condition' (i.e. obj.has_cond() = True) and examine() => disp_cond() will indicate whether the object is openned or closed.
	
		Program Architecture:
			On the topic of OpenableMixIn, let's take a moment to meniton where Doors 'live'. Unlike most other large objects (e.g. Creatures), doors do not reside in room.floor_lst. This is because doors don't really exist in just one room. Instead, they are contained within "room pairs" - which in turn reside in the map_lst attribute of the GameState map object. See map_class_def.py for details.

		Game Design:
			Regarding open() in particular, let's consider UI. A core goal in IF is to anticipate and meet player expectations. In the case of open(), if a player opens a chest, they are keen to know what is in it. To this end, in the open() method, we check for obj.is_container() and, if True, display the contents.
			
		Historic Note:
			In v1 and v2 of Dark Castle, doors could be unlocked and opened but not closed or locked. The problem wasn't actually room doors - it would have been easy to code them to close and lock - the real problem was containers, which were based on the same code base as doors (as is still the case in v3). Containers were the last and most complicated thing I coded in v1 (v2 just being the web version of v1). I was running into the limits of writing the program in procedural code and by this time I knew I was going to do a full re-write in OOP. So faced with the prospect of writing a 'put' verb and more complicated room inventory management, I totally dialed it in. Containers in v1 / v2 simply dumped their contents into the room inventory the moment you managed to open them. But of course that meant you couldn't close the container - because the the objects 'in' the container would still be in the room... hence the lack of 'close' and 'lock'. From a gameplay and puzzle point of view, this was never a problem. But the asymetry always annoyed me - I pictured Nana calling out to Burt across the years "For goodness sake Burtie, close the door behind you!" Properly working Containers and Doors were one of my first goals for v3.

			
* OpenableMixIn class:
	- Overview:
		When applied to an existing object, makes it lockable or unlockable. The typical intent is that the existing object also be Openable. However, this is not mandated. In theory, you could have have a car ignition Machine that was Lockable and is_unlocked == True could be the Machine trigger to start the car. 

	- Class Attributes:
		- is_unlocked: The boolean state of the lock. True => unlocked; False => locked; None is not a valid value (unlike in the previous case of the Door class). 
		- key: The object that can lock() or unlock() the target Door or Container. If key == None, there is no keyhole and the Door or Container must be openned by some other means (e.g. the iron_portcullis). 

	- lock() and unlock() methods [OpenableMixIn class]:
		Overview:
			Prepositional verb methods that expect a command in the form of: 'unlock front_gate with rusty_key'. If a key is not specified and Burt is holding something in his hand, that hand object will be assumed to be the key.

		Implementation Detail:
			The is_unlocked atribut is stated as a negative (i.e. is_*un*locked) so that the player's typically desired state == True.

		Program Architecture:
			Initially, all doors and containers were lockable. Since, in practace, not many doors or containers in IF are *not* lockable (even though it's a common occurence in real life) this seemed like a reasonable compromise. But once it became clear that the Surface class would be commonly used, it became clear that the Lockable state should be a MixIn class rather than directly baked into a Noun class.
		
		Game Design:
			There are no fewer than 11 custom errors for lock_err() and unlock_err(). This is partly because, as a prepositional verb method, there are twice as many objects that could be non-sensical (e.g. 'lock moat with cheese') and partly to give the player a helpful nudge when possible (e.g. when they use the *wrong* key). A concerted effort is made to visualize someone walking up to a door to unlock it and to give errors in the order of "least user astonishment" (e.g. the player is warned that an opened door can't be locked before they are warned that they are holding the wrong key).
		
		Historic Note:
			See historic note for OpenableMixIn().


* ContainsMixIn class:
	- Overview:
		Like doors, containers are fundamental puzzle elements. Doors are obstacles to entering rooms. Containers are obstacles to getting items.

		In Dark Castle v1/2, containers were just a coding slight of hand. So when I finally coded them for real, I needed to decide in what way a container and its contents were aware of each other. Presumably the crystal_box knew it contained the kinging_scroll... but did the kinging_scroll 'know' it was in the crystal_box? 
		
		Ultimately, I decided on two axioms:
			1) Within the constraints of acceptable performance, data should always live in one and only one location
			2) An object should know about the objects contained directly within it.
		
		From these axioms it becomes clear that containers should know what they contain but items are location 'ignorant': the kinging_scroll has no idea that it's in the crystal_box... or if it gets moved to Burt's hand or to the floor of the throne_room. Along with meeting our 'data in only one place' constraint, this approach also has the benefit of keeping most objeccts simple. There's no need to assign and update an extra 'location' attribute for every object. The down side is that recepatacle entities (i.e. Containers, Creatures, Rooms) become more complicated - and we end up frequently searching them for their contents. This hierarchal approach to containers is fundamental and has been applied to all aspects of the game (e.g. rooms know about the objects within them but know nothing about other rooms outside of them).
		
	- Class Attributes:
		- contain_lst: A list of obj in / on the container

		- max_weight: The maximum combined weight of obj that the container can hold. Notice that here, weight is being used as a proxy for volume. At some point, it may become necessary to add an additional 'bulk' attribute to the Item class but for now this seems like a reasonable generalization.

		- max_obj: The maximum count of obj the container can hold. The maximum is independent of max_weight and either limit can make it impossible to place an obj in / on a container. For the sake of simplicity, I typically make only one limit the constraining value and set the other to 999. My default is to constrain "enclosed contaiers" via obj weight and "surfaces" via obj count.

		- prep: The preposition that should be used when putting and object 'in' or 'on' a container - so generally either "in" or "on". The need for 'prep' arrises from the fact that, from an IF topology standpoint, the only difference between an unlidded but "enclosed" container like cardboard_box and a "surface" like wooden_shelf is the preposition used when adding an object to them. Previously, Surface was a class of its own that inherited from Container. Under the MixIn approach, they are both containers - only differentiated by attribute 'prep'.

	- put() method [ContainsMixIn class]:
		Overview:
			Used to add obj to containers.
		
		Implementation Detail:
			Container.chk_content_prohibited() is used to limit what can be put in a container and is extended for 'ContainerPortableSimple'. For details on why Containers can't hold Creatures and why 'ContainerPortableSimple' can't hold 'ContainerPortableSimple' obj, please see the explanation on node hierarchy under the Room class.

		Program Architecture:
			It might appear that put() could just as well be a method of Item as it is of Container. Code-wise this would certainly work. But what becomes clear when developing verb methods is that the code for testing error cases and buffering error messages is often longer than the code for actually executing the command. A corollary to this realization is that we always want to associate a method with its most restrictive noun - which in the case of put() is Container. This means that we don't need to test to see if the target location for put() is a Container - the method simply can't run if it isn't. This same logic applies to other preposition type verb methods like show() and give() - which in theory could be methods of Item but which are more efficiently coded when naturally limited in use by being methods of Creature.
			
			With Burt now being of class Creature, this principle can be generalized. Nearly every command actually involves Burt as the subject (e.g. "Burt, put the Rusty Key in the Crystal Box"). So while it's tempting to ask "who or what is performing the action?" - this line of reasoning would lead to every verb method being of class Creature. Instead, we generally want to ask "who or what is being acted on?" We can formalize this logic as follows:
				
				The 3 rules of method association:
				1) It's (almost) never the actor - because the actor is (almost) always Burt
				2) Ask, who or what is being acted on
				3) Choose the noun that is most restrictive
					
			When we apply this razor to "Burt, put the Rusty Key in the Crystal Box", Burt is immediately excluded and, between Rusty Key (class Item) and Crystal Box (class Container) we see that container is more restrictive. So put() is implemented as a verb method of Container.

		Game Design:
			ContainsMixIn has a number of scope and display "helper methods" that control what the player sees when they examine() a container, how obj are removed from a container, and how container capacity behaves.
		
			The ContainsMixIn class also sees the very first debug-only verb method: capacity(). capacity() gives the remaining weight and obj count capacity of any Container but can only be run in debug mode.
		
		Historic Note:
			put() was the very first preposition-based command in DCv3. After ages of two-word commands it very exciting to be able to type 'put the rusty key in the crystal box' and have a working result!

			Since the Surface class has been subsumed into the ContainsMixIn class, I will give its history here as well. My initial reason for creating the Surface class was that control_panel was previously an annoying hack. control_panel itself was of ViewOnlyMach class. This was fine but what to do with left_lever, middle_lever, right_lever, and red_button? The work-around was to mention them explicitly in the control_panel description but then stuff them in antechamber.feature_lst. This always irked me... and the more consistently behaved the Container class became the more unacceptable this work-around felt. One day I started thinking that control_panel should just be a container... but with no lid - and voila - the insight that a Surface class was needed arrived!		


* Generic Noun class:
	- Overview:
		There are eight Generic Noun classes: DoorSimple, DoorLockable, ContainerFixedSimple, ContainerFixedLidded, ContainerFixedLockable, ContainerPortableSimple, ContainerPortableLidded, ContainerPortableLockable. With the exception of ContainerPortableSimple, each works as expected based on MixIns and their base class (ViewOnly or Item) with no additional attributes or methods.

	- Methods:	
		ContainerPortableSimple is an excpetion because it needs to establish how a portable container's weight changes as a result of having Items added or removed. This was initially accomplished via extensions to put() and remove_item(). chk_content_prohibited() was initially also extended to prohibit portable containers from holding other portable containers - which sets an upper bound on receptacle nesting. During refactoring, the main code was updated to check for Portable Containers which enabled these extensions to be eliminated.

	- Implementation Detail:
		Some special mention should be made here regarding Liquids. As part of refactoring Doors and Containers, teh PortableLiquidContainr class was eliminated and Liquid itself was converted from inheriting from ViewOnly (as the only member of the misc_class_def.py module) to inheriting from Item in item_class_def.py. This enables Liquid to have the newly created 'weight' attribute. Players still can't take() Liquids - but this limit is now enforced by take_err() rather than ViewOnly class membership. At present, the earthen_jug is the only portable container that with a weight limit < 1 and well_water is the only Item with a weight low enough to fit into it - so earthen_jug's unique role as a liquid container remains (albeit via kludgy work-around). I have outlined the (many) features needed to fully implement Liquids in the game and plan to deploy them in a future version.


* Seat class:
	- Overview:
		The Seat class inherits from ContainerFixedSimple but overrides chk_content_prohibited() to allow the receptacle to hold Creatures. Creatures use the class verb methods enter() and exit() to sit in / on a Seat obj. 

	- Implementation Detail:
		Conceptually, Seat is a new topology for Dark Castle. Before Seat, the player was either in a room  or they weren't and rooms were treated as hermetically sealed from each other. So if you were in the Entrance you could attempt any action on any obj that was present. And if you weren't in the Entrance, any reference to an obj that was there would only generate a "I can't see a <obj X> here" response.

		By contrast, Seat introduces a level of transluscence to the environment. When you are seated in a chiar, you can reasonably expect to see all the objects in the (modest-sized) room you are sitting in - but unless they are nearby and in-reach, you can't necessarily examine them closely, read text on them, or pick them up.

		The Seat class seeks to replicate the expected transluscent behavior - but much of the heavy lifting actually gets done in the Creature class and, of course, Invisible. Creature contains scope methods is_contained() and get_contained_by() to determine if a creature is seated and, if so, in / on what Seat obj. Creature also contains the chk_obj_in_reach() and chk_wrt_in_reach() methods to determine if a given object is in-reach of the seated creature. In Invisible, the standard error checking applied to nearly every err method includes an in_reach check and an admonition that "You'll have to exit the <Seat obj> to attempt that." if the object or writing is not in reach. 

	- Program Architecture:
		In addition to the introduction of 'translucence', there are a few other architectural consioderations around Seat. One is light. As of this writing, I haven't yet introduced a lighting system to Dark Castle but I do intend to. The idea is that, as part of being 'translucent', Seat will inherit light from the room. But traditional IF also includes small enclosed non-room spaces that are opaque (e.g. the Closet and Fireplace in Hollywood Hijinks). These can be useful for some puzzles and  I'm planning to introduce them down the road. My current proposed class name is Nook.

		Speaking of class names, I debated heavily between Seat and Perch (naming is hard). Perch seems more generic. Seat comes with more expectations that something will be chair-like. But I had already started using Seat by the time I thought of Perch so Seat it is.

		Other MixIns are possible - for example BehindMixIn and UnderMixIn - and I am considering eventually building complex and specific furniture by combining these with Seat. IF also traditionally contains Bed objects. In fact Enchanter has a sleep() mechanic that requires a Bed and I am intending to implement something similar in DC. The intention is that Bed will inherit from Seat and include the sleep() method. I like the idea that the games hint system can be embeded in sleep() generated dreams.

		A final architectural decision I had to make regarding Seat was whether it would be a one-off special case or whether I would finally sucumb to an infinite-depth of recursive receptacles. Someday I will probably need to do the latter but for now I am going with the special-case approach. So no chairs on diases on stages floating in pools for Dark Castle... at least not yet! For now, Seat is a Creature Container - not a universal deeper level of room node.

	- Game Design:
		Chairs are present in traditional IF but are not typically a vital feature. The Seat class has been a lot of work so one might reasonably ask "why bother?" The answer is that Seat is really the precursor of Vehicle. In fact, a Vehicle is just a Seat that moves from room to room - with all of the same 'translucency' challenges as Seat. And the archtypal Vehicle puzzle is for the player to need to grab an object that can only be reached from thw moving Vehicle (e.g. the inflatable boat in Zork).

		I'm not planning to add vehicle in the immediate future, but reading Tim Anderson's wonderful 'The History of Zork' (https://gunkies.org/wiki/History_of_Zork) brought home for me how complicated vehicles could be if I didn't plan for them from the start. So, since I was refactoring Doors, Containers, and Surfaces already, this seemed like the right time to sort out Seats.

	- Class Attributes:
		in_reach_lst: in_reach_lst provides a list of Containers or ViewOnly objects that are in-reach to the Seat obj. If the room name is given then all Items in Room.floor_lst are treated as in-reach. Interestingly, unlesses explicitly added to in_reach, the Seat itself is not in_reach (if you wanted to examine a chair closely you would probably stand up first).

	- enter() and exit() methods [Seat class]:
		Overview: 
			put() can only place an obj in / on a Container if the object is an Item held in the putting creature's hand. take() has similar requirements. Since Creatures are not Items... how do they get in and out of a Seat? The answer is enter() and exit() - which work pretty much as you'd expect put() and take() commands for creatures to function.

		Implementation Detail:
			One interesting highlight to exit() is that exit_err() cannot use the std_err() call. This is because exit() is a method of Seat and, unless explicitly added to in_reach_lst, the Seat obj itself is not accessible when sitting. As a result, a special exception to this scope exclusion needs to be baked into exit_err().

			It's worth noting that in addition to the Seat.exit() verb method - which is specific to the Seat that the command-issueing creature is in / on - there is also a universal Creature.stand() method which will place a contained Creature in the Room.floor_lst independent of the Seat in question. This seemed a bit duplicative but 'stand' is a standard one-word 'get up from whereever' IF command so I replicated it in Dark Castle to follow convention.

		Program Architecture:	
			Perhaps what is highlighted most by enter() and exit() is the intereter blank space they expose. A player walking up to Dark Castle for the first time and wanting to sit in chair - even a player well versed in IF - would not initially use 'enter' or 'exit' commands. They would type 'sit on chair' or something similar.

			So why not use sit() rather than enter()? The challenge is that there will likely be other Creature-containing obj that inherit from Seat (e.g. Bed) where sit() would be the wrong command. So my intention with enter() and exit() is to create generic commands that can then be pointed to via object or class-specific synonyms (i.e. 'sit').

			This seems like a reasonable plan but it should be noted that, as of this writing, no such obj or class-specific synonym system exists and I don't really have a clear idea in my mind as to how to implement one. Thus begins the voyage ;-D


#####################
# room_class_def.py #
#####################

*** Module Documentation ***

* Room class:

	Overview:
		Every space Burt can occupy is a 'room' - even if he is outside. All of the game's  visible objects (except Doors) are contained within Rooms. Rooms themselves (along with Doors) reside within the room-pairs of Map.
		
		Since everything Burt can interact with on a given turn (except Doors) is in the room that he's occupying, Room is the perfect place to determine object scope. All scope methods for both visible and invisble objects are in Room. Available exits are considered to be conditions of the Room and are presented when the Room is examined. The commands 'look' and 'examine room' have identical results.

	Program Architecture:
		Rooms are a good time to pause and discuss Receptacles and Nodes. 
		
		Any visible object that can hold an Item is a Receptacle (i.e. Containers, Creatures, and Surfaces). As discussed in the Container method, Receptacles are 'smart' (i.e. they know what they contain) and Items are 'dumb' (i.e. they know nothing about the container that holds them). This means that to generate a list of all visible objects in a room (e.g. via get_vis_contain_lst() ) we need to first compile a list of immediately available objects and then, if any of them are open Receptacles, we need to list all of the ojbects inside *them*. But what if one of the objects inside a Receptacle is, itself, a Receptacle? 
		
		In theory, this could get deeply recursive. One obvious way to avoid this is "Just don't create very many PortableContainers in the game." But, hypoetheically, the goal is here is to create a tool set that could be used by others to build their own text adventure games... so we would like to put in place some prescriptive guard rails.
		
		Before we solve the problem, we need some nomenclature to describe it. The terminology I've chosen is "Node", from the study of binary trees (though in this case we have a non-binary tree). Imagine an inverted "tree" with one "node" at the top. This is the Room object, node_0. One level below Room we have nodes for all the visible objects in the Room. These are the node_1 objects. Some of the node_1 objects may be Receptacles and their contents are represented by Nodes one level further down: the node_2 objects. By default when we reference a node_1 object we are discussing 'absolute' node level where the current Room is node_0. But it is also possible to talk about 'relative' node level - for example, if Burt is in the Main Hall and holding the shiny_sword, then the shiny_sword has an absolute node level of node_2 (Room => Creature => Item) but a node level of node_1 relative to Burt (Burt => Item). You will occasionally see node_1 or node_2 variables referenced in methods. In this case, absolute node level is being used.
		
		So now that we have have some terminology, the key question is: "How do we want the game to work?" Whe could use recursion to allow recepticales to be indefinitely nested... but tracking items like this is cumbersome and hard to represent to the user. At the other end of the spectrum, we could disallow any Receptacle nesting - but this seems heavy-handed. I've taken the capabilities and limitations of Zork are a source of guidance. Early in the game, when the player enters the Kitchen, they find a sack containing food and a bottle of water on a table. So PortableContainers nested on a Surface seems like a reasonable expectation. PortableContainers nested in Creatures and Containers also happens within the game. But there are no takable Creatures, few, if any, takable Surfaces, and few if any instances of PortableContainers nested in other PortableContainers. Adopting these limits allows us a fun simulation - but limits node level to 3 (Room => Receptacle => PortableContainer => Item) - which is a reasonable depth to manage and represent.


#########################
# creature_class_def.py #
#########################

*** Module Documentation ***

* Creature class:

	Overview: 
		I thought through two different approaches to creatures. 
		
		In one approach - I'll call it the "primatives" approach - I declare that each creature has wants and fears (e.g. the hedgehog wants the biscuits, the goblin fears the shiny sword). Under the primatives approach the creatures have innate personalities and the role of creature methods like 'show', 'give', and 'attack' are just to expose those personalities. This is attractive in that it makes the creatures more real and gives general guidance for their future behaviors. However, I don't think it's realistic. Dark Castle is not a life simulator... there is no ecosystem or food chain (I mean really, the castle has been abandoned for generations - what have they all been eating??). And the creature's wants and fears are quite idiosyncratic... the goblin is an autocrat who wants to prevent passage to the throne room or any rejuvination of the castle... the hedgehog, along with loving biscuits, is the keeper of Bright Castle's spirit and wants to see it restored. These are not easy desires to model in a simple python object!
		
		The other approach I considered - I'll call it the "mechanical" approach - is that a creature is wholy defined by its methods. There is no attempt to track and expose a creature's inner desires - their actions are their all - like early impressionism, their surface is their whole. I find this a little unsatisfying - but I also think it's much more implementable. So at least for version 3.x this is the approach I'll take. Perhaps in version 4.x I'll find away to capture the hedgehog's inner yearnings in code ;-D
		
		Based on the "mechanical" approach, creatures have three standard interaction methods: show(), give(), and attack()

	Class Attributes:
		max_weight is the maximum weight a creature can carry and acts as an inventory limit for Burt. In modern IF, inventory limits are frowned upon as boring constraints that nag but add no value. This can be the case but I still love the old-school nature of needing to carefully decide what you'll carry with you on a particular mission. 

		In Zork, the inventory limit is the number of items a creature can carry - with a random number generator thrown in just to be a bit more caprecious. My hope is that max_weight is a bit less arbitrary but still creates game limitations that require creative problem-solving.

		Ref Link: https://blog.zarfhome.com/2017/08/your-load-is-too-heavy-zork-deep-reading.html


- take() method [Creature class]:

	Overview:
		take() in Creature class over-rides the Item method and provides guardrails to ensure that Creature class receptacles cannot be 'taken' even if a CreatureItem class is someday created.

- show() method [Creature class]:

	Overview: 
		'Show' is meant to be informational in nature. The Player will learn something about the creature - what it desires and fears - based on its response to the item shown. Therefore the show() method provides only a text response. Provoking an action response (e.g. running away) is outside the standard use case and should be implemented via a Modular Machine.

	Implementation Detail:
		1) When creating a new creature, remember to create the show() response descriptions in static_dict() using the auto-genertated key format. Auto-gen key format == "<player_creature>_show_<target_creature>_item"
		2) Creaatures are not allowed to have Creatures or Surfaces in their inventory
		
	Historic Note:
		show() is new to v3 (as are all commands requiring a preposition - since v1 / v2 only supported 2-word commands). Previously, the player's only insight into creature sentiment was the creature's description. Some test players of v2 felt that the act of giving the hedgehog the sword to get the silver key was pretty arbitrary - and they had a point - the clues (i.e. color of the keyhole on the craystal_box and the crest over the family_tree) were subtle.  show() enables richer creature interactions and a Dark Castle world of greater object variety - while still maintaining a feel of determinism.


- give() method [Creature class]:

	Overview: 
		'Give' is meant to enable barter and trade. If the Player gives an item to a creature - particularly if that creature has shown interest in the item via show() - then the player can reasonably hope for some other useful item or information in return. Therefore the give() method enables a text response, determines whether the creature will accept the gift, and what, if anything, it will give Burt in return. Because give() can fulfill a creature's needs it also has the power to change the creature's mood and therefore update their description.

	Implementation specifics:
		1) When creating a new creature, remember to create the response descriptions and (if appropriate) the creature description updates in static_dict() using the auto-genertated key format.
		2) It is assumed that if the creature 'shows no interest' in Burt's gift then they will not accept it, will not provide a gift in response, and will not change their demeanor as a result of the offer.
		3) It is assumed that if a creature won't accept an item from Burt, then they also won't have a gift to give in return and that their demeanor will not change.
		4) Creaatures are not allowed to have Creatures or Surfaces in their inventory
	
	Historic Note:
		Like show(), give() is new to v3. In v1 / v2 , Burt just dropped the 'stale_biscuits' on the floor of the 'main_hall' and the 'royal_hedgehog' charged forward and gobbled them up. With a new interpreter in v3 that enabled prepositions, give() seemed like a more intentional way to enable barter. It also provides more information about creature sentiment regarding objects.
	

- attack() method [Creature class]:

	Overview: 
		The attack() method is a bit more complex and is intended to enable combat between creatures. In Dark Castle, combat is a purely logical exercise. If you attack a Creature with the correct weapon at the correct time in the correct place, you will always win. Attack is a prepositional command in the form of 'Attack <creature> with <object>'. The attack object must match whatever the attacker is holding in their hand. If the attacker's hand is empty, then unarmed strikes are supported (but often not very effective). The results of an attack include the attacked creature dodging or fleeing and extend all the way up to or or the other creatures being slain. it's easy to imagine attack() provoking a more complex response than these outcomes - but those are outside the scope of the method and should be implemented via a Modular Machine.
	
	Implementation Detail:
		As verb methods go, attack() is fairly complex and perhaps it is over-engineered. The complexity comes from several sources.
		
		For one, it is a symetric method that can be used by any creature - not just by Burt. This means that Burt could attack a creature. Or a creature could attack Burt. Or possibly one creature could attack another without Burt even being in the room (Burt attacking Burt is not allowed and is handedled as a command error). This variety of possible combatants drives the need for a lot of case checking and pronoun tuning. It also forces the method to be rigorous about output... all game state changes must be performed first, then we check to see if Burt is even in the room, and if not we return without displaying any text (silent mode).

		Another complexity driver is the variety of object types that Burt can attack with. Attack objects are categorized as 'weapon' (i.e. they are of class Weapon), 'unarmed' (i.e. they reside in a creature's feature_lst), or 'item' (everything else). Attack results can then varry based on the attacking creature, and the exact object or object category that each combatant is holding. It's a felixble system... but again, arguably over engineered. 

		A final driver for complexity is the wealth of description that an attack() generates. Assuming that Burt is in the room to witness (or participate in) the proceedings, there are a total of four separately generated display strings for a given attack():
			1) The attack initiation string - which states who is attacking with what and what the attacked creature attempts to do (i.e. parry or dodge).
			2) Custom attack response - this is an auto-gen string which may or may not exist and is displayed if it does.
			3) Attack Resolution First Clause - this describes the attack stroke of the winner of the combat round. For weapons, randomly chosen custom text is used that's specific to the weapon object.
			4) Attack Resolution Second Clause - describes the results for the combat looser (which can varry from "easily dodges" to "is slain").
		Again, quite possibly over-engineered - but hopefully enjoyable to read when combat does breat out!
		
		In the context of historic text adventure combat, I'm guess that DCv3 is simpler than Zork's D&D-based attack scheme but more complex than other Infocom games that came after it.


	Program Architecture:
		The attack() method has the following sections:
		1) Command Errors. This section detects command errors, displays error text, and then exits. This is the one part of the method that is *not* fully symetric. All errors are written with the premise that Burt is attacking - the assumption here is that if a designer is using attack() for a creature then it is there job to use it correctly.
		2) Results. A list of possible result_keys is generated. This list is compared to the keys in the tgt_creature's attacked_dict (e.g. 'shiny_sword_burt_*') and the first hit is used to lookup the result_code value (e.g. 'tgt_death') with a default value used if no key hit occurs. Based on the result code, the attack results are carried out (e.g. in the case of 'tgt_death', the creature is removed from the game and the creature's inventory is droped on the floor of the room).
		3) Silent mode check. We check to see if Burt is in the room; if not, we exit.
		4) Display attack strings. Determine the win_obj and lose_creature and set pronouns appropriately (see Implementation Detail for more info).

	Game Design:
		It is said that one flouts convention at one's peril. If so, I am indeed courting doom with my approach to hand inventory. Inventory management in general is deemed to be a necessary evil of the Text Adventures genre... and to the best of my knowledge Dark Castle is unique in making the player manage an entire separate hand inventory on top of their inventory of carried items and worn garments.

		My rational is that I am trying to make Dark Castle more populated than your typical Infocom adventure - and also more interactive. Being able to see what a creature is carying in their hand gives the player more information about them. And creatures in the game can react to Burt based on what *he* is carrying in his hand. Perhaps a store keeper will close up their shop if they see Burt approaching with a weapon. But on the other hand, if Burt is attcked and not carrying a weapon, he is much more likely to perish. The intent here is to create a tesnsion between being prepared in a perilous environment and adhering to the social contract of a community.

		Time will tell whether any of these good intentions warrant yet more inventory management... but this is what I was aiming for.

	Historic Note:
		In the first functional version of DCv3, Burt was not an object - just a collection of dictionary entries in the GameState object. From a developement standpoint this makes sense... the Creature class was the last and most complex non-machine class I created. The initial player state information needed to be as simple as possible as I learned how on earth OOP worked.

		My first hint that Burt should be a variable came from reading Tim Anderson's wonderful History of Zork (https://gunkies.org/wiki/History_of_Zork). Among other things, this mentioned that from early on in Zork, there was a player entitiy that could move from room to room. I didn't have one of these and began to wonder if I should - but clearly it would be a big effort so I pushed it off for a later update.

		The real revelation came as I was wrapping up the very last, most complex, Modular Machine for DCv3, goblin_attack_mach. It seemed straight-forward - if the conditions were met, the Goblin would simply use the attack() command (which back then was 2_word, not prep) to attack the Burt object - and I'd be all set. But of course, once I got to coding it, I was reminded that there *was* no Burt object. The short term hack was to create a secret_verb method called attack_burt() - which was very similar to attack() but with different pronouns, the ability to access the burt GameState dictionary keys, and no target creature argument... since, of course, it was only ever used to attack_burt...

		That got the game to 'done' - but it was such an egregious hacke that I knew I'd have to come back and fix it. At the time I wrote: 

			"'attack_burt' is an awkward 'hidden' verb that enables a creature to proactively attack Burt. Among other things, this work-around highlights that Burt should really be an object himself - rather than an amorphous set of attributes distributed across game state. But this will not be a minor undertaking - so for now, we have the attack_burt() method - which enables 'attack' to remain a 2word command without requiring a 'burt' object to exist."
		
		The obvious solution was to make Burt an object of class Creature - but this was a significant undertaking given how primative the original Creature class was (at the time, Creature objects did not have hand or worn attributes - among others). More challenging yet, every single method that impacted Burt's inventory and location (e.g. take, drop, wear, go, etc..) had to be heavily re-written. It was daunting, but it was also very clearly the 'the way' - so making burt a Creature object became one of the tentpole objectives of the DCv3 refactoring.

		go() was actually the very first verb method re-written to be 'symetric' (i.e. a verb method that could be called by either the burt object or another Creature object). attack() is now the second. The goal is to eventually make all verb methods (except perhaps examine() and read()) symetric so that Creature interaction can be as organic and uniform as possible.


#######################
# swtich_class_def.py #
#######################

*** Module Documentation ***

* Item class:

	Overview: 
		Switches are the first and simplest component of Complex Machines. Switches can trigger Machines (e.g. red_button, throne). Switches can also act as Conditions that control the behavior of Machines (e.g. left_lever, middle_lever, right_lever). Some switches also exhibit  simple Machine behaviors themselves (e.g. ButtonSwitch and SpringSliderSwitch classes are typically reset to 'neutral' state in the auto_action module). For this reason, is_mach() is set to True for the SwitchMixIn class.
		
	Program Architecture:
		Switches are the first class we see being implemented via the MixIn pattern. The SwitchMixIn class is not intended to be used directly for object instantiation. Instead, it can be combined (via dual inheritance) with other classes - most often ViewOnly - to give objects of those classes switch-like capabilities. Objects that dual-inherit from SwitchMixIn can appear as traditional levers and buttons that are clearly meant to invoke or control an action - or they can have the appearance of regular objects (e.g. the throne) - leaving it to the player to intuit that they can be manipulated.
		
		Switches, by design, are 'dumb' - meaning that they know nothing about the actions they can trigger or the Complex Machine that they are connected to. Switches only know their current switch_state. Complex Machines use switch_state as either a trigger or a condition. This approach is intuitive (at least to older minds like mine that grew up before you could fit a computer inside a button) and helps to centralize the 'smarts' of  the Complex Machine into the MachineMixIn object itself.
		
		From a program architecture point of view, Switches are innately varried - so the goal is for all (or at least most) attributes to live in the SwitchMixIn class but for verb methods to live in the 'noun' classes (e.g. ButtonSwitch, SpringSliderSwitch, and LeverSwitch). Likewaise, the 'noun' switch classes should be independent (except in cases of clear functinality inheritance, e.g. SpringSliderSwitch in heriting from ButtonSwitch) and the scalable - meaning that SwitchMixIn should not need to maintain awareness of all possible Switch 'nouns'. Given that many switches are interacted with via the same small numbrer of verbs (i.e. 'push', 'pull', 'turn', etc...) this implies that we will get method overrides - as we do in the case of SpringSliderSwitch and LeverSwitch each having independent, over-riding pull() methods. Bearing in mind the constraints and the potential for many more Switch 'noun' types, I think method independece is probably the best appraoch and I have not attempted to somehow centralize / synergize Switch methods (i.e. I am avoiding 'one pull() method to rule them all!').

		A final topic worth covering is: where do switches reside? Starting in Dark Castle version 3.76, control_panel was re-created as class SurfaceMach and the levers and buttons associated with it simply sat upon it. Since the switches all inherited from ViewOnly, they could not be taken from the Surface. And control_panel.max_obj was set to 4 so no additional items could be placed on the surface. To ensure that the control_panel was not examined closely while the Goblin was guarding, it was only instantiated upon the goblin's death.
		
	Historic Note:
		In older versions of Dark Castle (up to v3.75) the implementation was a bit kludgy. The control_panel switches (red_button, left_lever, middle_levrer, and right_lever) were mentioned in the control_panel description but were actually residing in antechamber.feature_lst. This kepts them out of sight and mind when Burt first entereds the room but made them available once he can examine() the control_panel and is aware of them. From a player perspective this worked pretty well but it was definitely a hack and I was glad to progress to the Surface approach used today.


#####################
# mach_class_def.py #
#####################

Machine Documentation - Dark Castle v3
Apr 28, 2022

****************************
*** Formal Documentation ***
****************************

The Purpose of Machines:

If Machines are simply objects that respond to user commands then one could argue that the world of Dark Castle is already filled with machines. After all, doors are machines. Containers are machines. On some level, even rooms and items are machines. Each responds in a standard, simple, and reactive fashion to player actions.

But many of the puzzles in Dark Castle - or any other text adventure - hinge on exception cases to these norms: the Player tries to walk south from the entrnace but they're turned back with a clue, the Player wants to take the Shiny Sword but the Hedgehog intercedes, the Player tries to examine the control panel but the Goblin attacks before they can. 

Likewise, many puzzles depend on more complex machines: the Iron Portcullis can only be opened by matching the Lever Array to the Messy Handwriting on the Note and then pushing the Red Button, the Hedgehog Broach will only be dispensed once after the first time Burt pulls the Throne. 

These custom, complex, and pro-active Player interactions require a more intricate coding solution than a simple door - and the general name I give for many of them is "Machines". What follows is an explanation of my approach to implementing "Machines" in Dark Castle.

The Journey to Modular Machines:

The journey to establishing the current structure for Machines was a long and winding one that's hopefully arrived at a reasonable solution. Here were the major milestones:

1) In both Dark Castle ev1 and v2 I realized the need to interject pre and post actions into the game based on player behavior. A pre-action is one that occurred before the player's intended result (e.g. the Hedgehog blocking Burt from getting the shiny Sword). A post-action is one that occurs after Burt's action (e.g. after Burt pushes the Red Button the Control Panel machine should whirr and possibly open the Iron Portcullis). In the early versions of the game the player's commands were sent to an enormous If-Then-Else construct that checked to see if the conditions were right to invoke a pre or post action. This approach had the advantages of being simple and extremly flexible - but it always disturbed me for several reasons:
	A) It was extremely opaque to anyone reading the code. You could easily read through the coding for the Entrance and have no idea that going East or West off the drawbridge was deadly.
	B) It took you out of the game... it was like a whole second set of game logic independent from the main program.
	C) The If-Then-Else routine was neither scalable nor reusable
For all these reasons I wanted a different solution in v3.

2) My first idea was to populate rooms with 'conditional-command-lists'. These would be objects with lists-of-lists attributes that acted as AND and OR grouping of conditions and results. This approach had the natural advantage of signalling that something was going on in the room... but it was basically a large, distributed If-Then-Else list so it still had problems B) and C) from above. After tinkering with some psedo code I abandoned this idea.

3) Next I considered specific machines with specific conditions and actions. For example, a 'travel_effect' machine that would reside in each room and produce effects like the "You can't turn back now..." message when going South from the Entrance as well as the hazzards and benefits of going East or West off of the Entrance drawbridge. I prototype this solution and made several discoveries:
- Machines can be invisible
- Monolithic machines have way too many attributes to keep track of
- The Entrance 'Go South' vs. 'Go East / West' use cases are very different ('Go East / West' is much more complex)... attempting to use the same Monolithic Machine for both leads to *many* attributes with Null value in the 'Go South' case.

4) The problematic 'travel_effect' implementation led me to the solution of Modular Machines. The fundamental idea is that the Machine class definition is the same for all Machines but that the Conditions and Results are separate objects that are attributes of each Machine. This modular approach allows for much greater re-use. Having a single Machine class definition does impose some constraints - but that's not an all bad thing - constraints create structure. We'll take a look at how the Modular Machine and it's components in detail in the next section.

High Level Appliction Flow:
To understand Machines it helps to first understand the high-level module call flow of the Dark Castle app.

It all starts with web_main, a very simple web-tier function who's only job is to get user input and present the app's response text to that input. 

To get the response text, web_main calls app_main. app_main is the heart of the app. It recieves user_input from web_app and converts it into output (the app's response text). In the special case of the game's first turn, app_main calls start_me_up which prints a welcome and sets some one-time game variables. But for all subsequent calls to app_main the following flow occurs:
	1) load the object variables from the game's save pickle and reset the output buffer
	2) calls the interpreter function to convert the user's input into a game command. interpreter returns a 'case' and a 'word_lst'
	2.5) The interpreted command is checked by validate(). If it is not valid, an error message will be buffered by validate() and no stateful changes to the game will take place. If valid, move count gets incremented and we move on to executing the player's command. 
	3) before executing the game command, app_main now calls the pre_action function. pre_action scans the available machine scope (simplisticaly, the room Burt is in) for machines that have pre_act triggers. If any exist, checks to see if any pre_action Machines are triggered and, if so,  runs those Machines. The pre_action function returns the boolean variable cmd_override to app_main. cmd_override == True is for cases where the pre_action negates the player's command.
	4) If cmd_override is False, app_main now calls cmd_exe to execute the player's command (e.g. "take key" => "Taken"). From the three cases of cmd_exe(), calls disp_score() from the Score subclass.
	5) disp_score() checks whether the player's current command matches any of the score conditions in score_dict. If so, score is increased and an update to the player is buffered.
	6) app_main now calls the post_action function which determines if the player's command (for example, pulling a lever) triggers a post_action Machine. If so, the Machine is run. post_act() also calls disp_score() to see if Machine results have impacted the player's score.
	7) if gs.end.is_end == True then app_main calls gs.end.disp_end() method to buffer the end of game text
	8) app_main saves the updated objects to the save pickle and resturns 'output' and 'end_of_game' to web_main

The key take-away from the app_main flow is that, both before and after the player's command execution call, the game "gets a turn". These ad-hoc pro-active or responsive game actions are what the Machine construct enables.

Note: in version 3.83, app_main() was significantly refactored. By this time, new special cases had been added ('restart', 'again', and 'wait') and the code had become opaque. I had taken the if-then-shild approach and had new fewer than eight return statements in the function and it was far from clear - even to me - how the over-arching code flow was supposed to work. In refactoring, I kept the early return for is_start == True (after calling start_me_up() ) but created a consistent flow, goverened by some core primative booleans (is_stateful, is_interp_cmd, is_interp_valid) for all remaining cases. For me the result is much more readable - and should make adding additional special cases much easier. Despite these changes, the description above (written before refactoring) is still a good overview of app_main()'s core functionality.

The Modular Machine Components:
Michines are composed of Triggers, Switches, Conditions, Results, and the framework of the Machine itself which orchestrates all of these. I'll detail each of these below.

Triggers:
Triggers are the Player Commands or Switches that can start Machines. The information about a Trigger lives in the Machine class itself - a given Switch has know "knowledge" that it's the trigger for a machine and multiple Machines could have the exact same Trigger (this makes sense when you think about Player Commands being triggers).

The Machine class has the following Trigger attributes: trigger_type, trig_switch, trig_vals_lst

trigger_type: a string that identifies when the Trigger takes effect and what type of Trigger it is. Examples: 'pre_act_cmd', 'post_act_switch', 'pre_act_auto'

trig_switch: for Switch-based Triggers this is the Switch object that Triggers the Machine. For Player Command-based Triggers the value is None. At present, all Machines have at most one Switch Trigger. I may make trig_switch a list in the future if I end up making Machines with multiple triggers.

trig_vals_lst: The Switch States or Player Commands (case & word_lst) that will activate the Trigger.


Switches:
Switches are buttons, levers, sliders, and the like. They can be operated on ("pushed", "pulled", etc) to change their state. In theory, one could bake intelligence into switches but I have chosen to make my Switches simple and dumb. They know their own state and that's it. Their only unique attributes are swtich_state and trigger_type:

switch_state: The possible values of switch_state depend on the switch in question. For ButtonSwitch it's 'pushed' or 'neutral'. For SpringSliderSwitch, 'pulled' is added as a possible value. For LeverSwitch, 'up' or 'down' are possible. 

def_switch_state: the default state of the switch. For stateful switches like levers, def_switch_state == None. For non-stateful switches like buttons, def_switch_state typically == 'neutral'.

trigger_type: This attribute enables switch_state resets. Some switches, like levers, are innately 'stateful' - their switch_state remains constant until they are acted on again. By contrast, stateless switches like buttons and spring-slider-switches must be reset to neutral each turn. When trigger_type = 'pre_act_auto_switch_reset' switch_state is reset to def_switch_state at the start of each turn.

The Switch class is implemented as a MixIn that is combined with ViewOnly to include Switch-specific attributes. Each specific type of switch (ButtonSwitch, SpringSliderSwitch, LeverSwitch) contains the methods needed to act on it (e.g. push or pull).


Conditions:
Triggers are what start Machines but Conditions determine what happens when they run. For example, if in the Entrance, Burt goes East off of the drawbridge, then there are three possible conditions: 1) Burt doesn't have a weapon in his hand, 2) Burt does have a weapon and not gotten the Royal Crown yet, 3) Burt has a weapon and has already gotten the Royal Crown. Each of these conditions will then be associated with a different Result. A Machine's Conditions are limited to examination of Game State, Switches that are associated with the Machine, and the Machine's State.

The Machine class has two Switch-related attributes: cond_switch_lst and cond_lst. cond_switch_lst is a list of switches whose state impacts condidtions. cond_lst is an ordered list of conditions that are possible when the machine is triggered. The conditions within cond_lst should cover all possible cases... e.g. if cond_1 is the case where item_x in hand_lst then cond_2 woudld typically be the case where item_x not in hand_lst.

Each Condition class includes a name attribute and whatever other attributes are needed to check the condition and a method, named cond_check(), that returns True or False. cond_check is called from the Machine class run_mach() method so cond_check() is limited to evaluating conditions beased on the values of gs, cond_switch_lst, and mach_state. 


Results:
There is a Result associated with each Condition. The Result updates the game environment with the outcome of running the Machine under these specific conditions and also buffers the outcome description to the Player.

Each Result class includes the attributes it needs to function. For example, the BufferAndGiveResult class includes the give_item attribute which specifies the Item to be placed into Burt's hand when the Result executes.

Each Result class also has a result_exe() method associated with it. result_exe() is passed gs and mach_state and returns mach_state (the Machine's own state variable) and cmd_override (which determines whether the Result overrides the Player's own command).

Results are associated with a given machine via the result_lst Machine attribute.


The Machine class itself:
This then brings us to the Machine class itself, which orchestrates all of these components. There is only one Machine class - most of the variability between Machines is introduced via different Switches, Conditions, and Results. From a class definition perspective, Machines are actually implemented as dual-inheritance mix-ins: MachMixIn. This allows for Machine traits to be associated with Invisible, ViewOnly, or Item class traits => InvisMach, ViewOnlyMach, and ItemMach.

The one Machine attribute that we haven't already covered in detail is mach_state. Machines can be stateless (e.g. entrance_south_mach which simply tells Burt that he can't turn back now) but most have some kind of persistent state condition (e.g. has the Crocodile dispensed the Royal Crown?, has the Throne dispensed the Hedgehog Broach?, what is the number that the Iron Portcullis lever array must match?). mach_state holds this state value. It is most often boolean but can be an integer, string, or whatever is needed. A Machine's state is typically inspected by Conditions and updated by Results.

The MahineMixIn class has two methods: trig_check() and run_mach()

Based on the trigger type, trig_check() composes trig_key_lst and compares it to the Machine's trig_val_lst and returns True or False.

run_mach() loops through cond_lst, checks whether each Condition is met (using the condition's check_cond() method), identifies the first True Condition in the ordered cond_lst and its index, and then runs result_exe for the Result in result_lst with the same index. The run_mach() method then updates the Machine's mach_state and returns cmd_override. A structural requirement for run_mach() to run successfully is that there must be one Result for every Condidtion and the associated Conditions and Results must be listed in the same order in cond_lst and result_lst. run_mach() returns result_name which in turn is used by post_act() to check for scoring events.


An Example: 
Let's take a look at the control_panel Machine located in the antechamber:

control_panel = ViewOnlyMach('control_panel', 'Control Panel', 'panel', 'control_panel', None,
				'post_act_switch', 0, red_button, ['pushed'], [left_lever, middle_lever, right_lever],
				[correct_lever_array_cond, wrong_lever_array_cond], [toggle_portcullis_result, portcullis_doesnt_open_result]) # mach_state == lever_array_value

And before we dive into the machine itself, let's take a glance at the room it's in:

antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
				[alcove, left_lever, middle_lever, right_lever, red_button], [torn_note, grimy_axe, iron_portcullis, control_panel],
				{'north' : iron_portcullis}, [])

Here we see that the control_panel is in room_obj_lst (so it is listed in the room description) and the machine's switches (left_lever, middle_lever, right_lever, red_button) are in features (where they can be examined but are not automaticaly listed in the room description). 

Suppose Burt is in the Antechamber and types "push button".

web_main passes this user_input to app_main which opens the save pickle of objects, increments movement, resets the buffer, and calls interp().

Since red_button is in scope for Player interaction, the command is valid and interp() converts this too a two-word command (case = '2word', word_lst = ['button', 'push']).

app_main() calls pre_action() next. It sees that control_panel is a machine but, as its trigger_type is NOT pre_act_cmd, takes no action. red_button does have trigger_type == pre_act_auto_switch_reset so it is reset to 'neutral'. The control_panel run_mach() method has not been run so cmd_override remains False and is returned.

Since cmd_override == False, cmd_exe executes the Player's command. The ButtonSwitch push() method is called and red_button.switch_state = 'pushed' and the response "Pushed." is buffered to the user output.

Control is passed back to app_main() which now calls post_action(). post_action() gets mach_obj_lst (the list of Machine objects in scope) from gs and itterates through it searching for any Machines that have trigger_type == 'post_act_switch'. control_panel meets these conditions so trig_case = 'switch' and trig_switch_state_lst = the state of the Machine's trigger switch = the state of control_panel's trigger switch = the state of red_button = 'pushed'. 

Under the same if clause, the value of control_panel.trig_check() is checked and, since 'pushed' is in 'trig_val_lst' (trig_val_lst == ['pushed']), trig_check returns True and control_panel.run_mach() is run.

Let's say for the sake of arguement that the lever array is NOT set correctly.

First control_panel.run_mach() loops through cond_lst and runs cond_check() for each listed Condition. for control_panel, cond_lst == [correct_lever_array_cond, wrong_lever_array_cond]. correct_lever_array_cond is of class LeverArrayCond which is fairly complex. It has a cond_check() method that calculates the binary value of the of the lever array and then returns the compare of this sum to mach_state. Since the lever array is not set correctly, correct_lever_array_cond.cond_check() returns False.

wrong_lever_array_cond does none of the calculations descirbed above. It is of class PassThruCond which has a cond_check() method that checks nothing and simply returns a value of True. This works because wrong_lever_array_cond is the *last* condition in cond_lst and we execute the Result for the first Condition to be True.

So we end up with cond_return_lst == [False, True] => result_index == 1 (the index of the first True Condition) => we rune results_exe on result_lst[result_index]. result_lst == [toggle_portcullis_result, portcullis_doesnt_open_result] so we run portcullis_doesnt_open_result.result_exe(). This is of class BufferOnlyResult so, sure enough, all it does is buffer some text (a mild clue to the Player) and return the existing cmd_override (False) and mach_state.

control_panel.run_mach() is nearly done. It updates it's mach_state based on the return from portcullis_doesnt_open_result.result_exe() (which is the same as the existing mach_state) and then returns cmd_override (which by definition will always be False for tirgger_type == 'post_act_switch').

The Machine has done its job! sore() and end() will be called next by app_main() as needed but the machine coding itself is fini!

Naming Convention:
All machines of class InvisMach have names ending in "_mach". For machines of class ViewOnlyMach or ItemMach this convention colides with the interpreter-based convention of object name = 'noun_verb'. The interpreter-based convention wins here and the '_mach' postfix is dropped for these machines (e.g. control_panel).

Closing Thoughts:
I'm conflicted about Machines. On the plus side, they work and they meet all my goals - they are in-game, transparent, scalable, and reusable. But they are also *vastly* more work and code and, in many ways, complexity than a simple series if-then-elses. Is this good coding or am I making mountains out of molehills by clinging over-tightly to idealogical purity? I'm really not sure... but I've learned a lot and that's the ultimate goal - so I'm going to keep using them. I also suspect that the "goodness" of the Machine structure has everything to do with the scale of Dark Castle. For a four-room dungeon Machines are vastly over-engineered. But for a larger dungeon - or a construction set - perhaps Machines (as I've dsigned them) make sense. Time will tell.

The other reason to stay the course on Machines is that I intend for them to be the basis for Creatures. Creatures were arguably the least fleshed out aspect of Dark Castle v1 & v2. They worked mostly because I allowed very few ways of interacting with them. Hopefully, with the use of Machines, I can imporove on this in v3.


* WARNINGS & TIMERS - GENERAL *

In the wise (roughly paraphrased) words of PERL's creator, "Good tools make easy things easy and hard things possible." The MachineMixIn class addresses the 'hard things' case... it's extremenly flexible - but frankly, it's a convoluted PitA. It's great at enabling the unexpected and expanding the complexity of the Dark Castle world - but whenever possible, it's preferable to create and use simpler, fixed purpose machines (i.e. to make "easy things easy"). Warnings and Timers are both examples of this approach and are also necessary infrastructure for the Hedgehog creature. Warnings are innately self-contained. Timers are a bit more involved. While solving one problem, timers introduce a few new ones... the need to be more rigorous about game time, ensuring that 'auto' game messages are delivered at the right time relative to other game responses, and tracking which events in the game world Burt is able to witness.

* WARNINGS *

Warnings have a rich history in Interactive Fiction. If you cursed in Zork you'd be warned that cursing wasn't allowed. If you issued the same curse again the game would quit on you! Warnings are also a good way to redirect the player from a non-useful pursuit and possibly give them a nudge in the right direction. For example, when Burt attempts to go south from the Entrance and leave Dark Castle we tell him that he can't turn back and then give the player a hint about the Rusty Key. And similar to the Zork cursing use case, if Burt attempts to attack the Hedgehog we warn him not to once or twice but if he keeps at it we let him... with game-impacting results.

The Warning class inherits from Invisible (including the attribute 'name') and, in common with MachMixIn has attributes 'trigger_type' and 'trig_vals_lst'. Warnings need to happen before player command execution and are always triggered by player commands - so 'trigger_type' is always 'pre_act_cmd'. 'trig_vals_lst' uses the same [case, word_lst] format as MachMixIn, and the trig_check() method code is the same as well.

After these similarities, Warnings are much simpler than the MachMixIn class with only two more attributes: 'warn_max' and 'warn_count'. warn_count gets incremented each time pre_action() calls the Warning mach_run() method. If 'warn_max' == 0 then the use case is 'always give the same warning' and always return cmd_override = True. If 0 < 'warn_count' < 'warn_max'then give a specific error and cmd_override still = True. If  'warn_count' == 'warn_max' give a final "Don't say I didn't warn you Burt..." and cmd_override = False. Once warn_count > warn_max there are no future warnings and cmd_override always = False.

The actual warning description key is based on "name" + "_" + str(warn_count). This is implemented with 'try: ... except:' with "I'm not sure that's a good idea Burt..." as the 'except' default.

Fundamentally, Warnings are simple - they inhibit a player command either always or for a finite number of tries and return a variable text message. Warnings do not actually generate any actions - but a MachMixIn condition could take the difference between warn_count and warn_max into account.


* TIMERS *

Like Warnings, Timers inherit from Invisible and have a trigger_type attribute. But in this case trigger_type is set to 'auto_act' and is not triggered by either pre_action() or post_action() (more on this later).

The intent is that timers are "dumb". They are not triggered by player commands or switches - instead they are started or reset via the timer.start() and timer.reset() methods - typically by complex machines. Once started the counter's only job is to count up until it reaches it's maximum. To enable this the counter has attributes of 'active' (boolean), 'timer_count', 'timer_max', and 'timer_done' (also boolean). The mach_run() method is called when the timer is active. Its primary job is to increment timer_count and set timer_done = True once timer_count = timer_max.

Although Timers never directly trigger actions (this is left to machines which can use Timer attributes in their Conditions), one typically does want to let the player know that a timer is running. To this end, Timers have the innate ability to send messages to the player on each Timer interval. To support this, Timer has the attribute 'message_type' which can be 'constant' (same message each turn), 'variable' (different message each turn), or 'silent' (no message). Description key creation is managed in the same way as Warnings with a built-in default alert of "Beep."

Beyond their core functionality, Timers are interesting because they are our first 'auto' machines - that is, they take an action regardless of Burt's choices. This has several implications.

*Valid Turns*

The first is that we need to get more rigorous about what does and does not constitute a valid turn. In the past I called gs.move_inc() at the start of app_main() and then selectively called gs.move_dec() from within interp() when any error seemed more like the interpreter's fault than the player's. But now, with auto commands in play, we need a clear and consistent measure of which turns are valid so that the timer doesn't tick on a non-valid turn. To enable this I eliminated the move_dec() calls in interp() and set a move_valid variable (boolean) within app_main(). For all 'case' == 'error' and also the 'quit' command, move_valid = False. In this case, no pre, post, or auto actions are called. Whereas, for move_valid == True, move_inc() gets called and pre, post, and auto actions are executed.

*Auto Message Timing*

The next problem to solve is *when* should auto commands be displayed? Let's build up turn order logic from first principles:
	1) We get the player's input via web_main() and call app_main. Within app_main() we first call interp() to understand the player's command.
	2) The player's command is then executed in cmd_exe() (unless overridden)
	3) In some cases, the player's command is inhibited or overriden by the game's response. For example, the case of Burt walking east or west from the Entrance off of the drawbridge. This is carried out by pre_action(), which should clearly run before cmd_exe()
	4) In other cases, the player's command causes a game response. For example, Burt pushing a button. This is performed by post_action(), which clearly needs to run after cmd_exe().

So when should auto commands happen? If they execute in post_action() then they feel like a response to the player's command... which they're not. If it happens in pre_action() then it also comes across as a response to a player's choices (because other pre_actions reference Burt's attempted action). Instead, auto would ideally run *before* getting user input, so that the player can make choices based on it... but if you look at the events in 1) above, you'll see that web_main() has already gotten user input before app_main is ever called... so it appears to be impossible to call auto first without messing around with web_main() (which we want to keep simple). However, if we consider that the first move of the game will never have an auto command... then there's really no difference between going "first" and going "last". So we create an auto_action() routine and have it called at the very end of app_main() so that the auto results appeare *before* the player's next input option.

*Timer Scope*

Finally, we get to the topic of Timer Scope. As our first auto machine, Timers present a unique problem. Before now, all machines operated based on immediate command or switch stimulous from the player. If Burt was in the same room as the machine then he could trigger it. And if he had just triggered then he could surely experience its effects. But auto machines operate independently of player stimulous. This makes scope more complicated.

Let's take our test_timer example - which placed a bomb with a button on it in the Entrance room. The bomb was a fairly simple machine. If Burt pushed the button the timer was started and counted up, turn by turn, to a timer_max of 3. On turn 1 it messaged "Tick 1". On turn 2: "Tick 2". And on turn 3: "Boom!". If Burt pushes the button and spends the next 3 turns in the Entrance than he sees all 3 messages and everything works as expected. 

But what if, instead, Burt pushes the button and then walks north into the Main Hall? Our first question here should always be: "What *should* happen?". This in turn raises the question of how separate are Dark Castle rooms? Should Burt hear what is happening in the next room? My design choice here is that standard rooms are hermetically sealed. There can be custom exceptions of course - but as a standard response, Burt knows nothing about the events of a room he is not in. This standard behavior clarifies what *should* happen in the above example: Burt should hear "Tick 1", then, after going north, he should see the description of the Main Hall. In the mean time the bomb should "Tick 2" and "Boom!" in the Entrance without Burt getting any notification of it (unless he immediately turns around and runs back to the Entrance).

Now that we know our goal, what *does* happen if Burt pushes the bomb button and then walks north? The default coding only runs a machine that is in the scope of the room Burt is in. So if test_timer is in entrance.invis_obj_lst then Burt hears "Tick 1" and then heads north to the Main Hall. He can now spend an infinite number of turns in the rest of Dark Castle and the timer will wait until he returns to the Entrance to perform "Tick 2". This is not what we want - we want test_timer to operate independently of Burt's proximity to the bomb. So we create a new attribute in the GameState class: universal_mach_lst. We remove test_timer from entrance.invis_obj_lst add it to universal_mach_lst and, in GameState methods, extend mach_obj_lst with universal_mach_lst. Now auto_in_alert_scope will find test_timer to be in scope no matter where Burt happens to be (though Burt still needs to push the button on the bomb to *start* the timer).

However, now we have the problem that no matter where Burt goes, since test_timer is still in scope, Burt still gets notified of "Tick 2" and "Boom!" - even though he's not in the same room as the bomb! We solve this by giving the Timer class one more attribute: alert_anchor. Now, in the run_mach() method of Timer, we can check for scope_check(alert_anchor) as a requirement for buffering the test_timer messages. If this condition fails, the timer still runs, but Burt never sees the "Tick 2" or "Boom!" messages.

At long last, test_timer is working as we would expect! This was a lot of work just to enable the Hedgehog to eat some stale_biscuits - but hopefully we have also laid some good groundwork for future timers and other auto machines ;-D
