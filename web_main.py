# program: dark castle v3.76
# name: Tom Snellgrove
# date: Mar 20, 2023
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#								integrate triggers, replicate full original, add more puzzles!

### import statements
from app_main import wrapper

### main routine
end_of_game = False
start_of_game = True
while end_of_game == False:
	if start_of_game:
			user_input = "xyzzy42"
			start_of_game = False
	else:
		user_input = input('Type your command: ')
	end_of_game, output = wrapper(user_input)
	print(output)
print("THANKS FOR PLAYING!!")


"""

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

- Moving the help() function to interpreter()
	- The macro organization of the program is for interpreter() to interpret the players intent and for cmd_exe() to execute it
	- However, at the module level, the idea is that the interpreter() module is uniquely focussed on language semantics
	- The help() function is also (mostly) focussed on language semantics - specificly exposing them to the player
	- Moving help() to interpreter() also enables us to make all the static lists and dictionaries local to interpreter()
	- The balance between module-level structure and macro-program flow seems best served by moving the help() function to interpreter()

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


"""
