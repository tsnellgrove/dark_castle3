# program: dark castle v3.68
# name: Tom Snellgrove
# date: July 7, 2022
# description: static dictionary initialization function module


### this module declares static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => class_def) ###


### static dictionary ###
static_dict = {
		'version' : '3.68',
		'max_score' : 75,
}

### description dict ###
descript_dict = {
		### one-word commands - non-objeects ###
		'introduction' : "Greetings brave adventurer!\n\nYou are Burt-the-Baker, the only adventurer brave - or foolish - enough to enter the Dark Castle in search of treasure.\n\nType 'help' for help.\n\n",
		'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'creatures', 'one-word-commands', 'verbs', 'abbreviations', 'adjectives', prepositions', 'articles', 'read', or 'attack'.",
		'credits' : "Written and programmed by Tom. Thanks to Toby, Joshua, JoyEllen, Milo, Gideon, Franco, Karl, Andy, Ken and Alec for advice and playtesting!!",
		
		### help subsystem - non-objects ###
		'help_basics' : "Objects you can examine and interact with are capitalized. Use 'read' (not 'examine') to read text you find written on objects. You can 'take' one object that you can see into your hand at a time from the room, a container, your backpack, or from being worn. Your other hand is holding your light source. In many cases you must be holding an object in your hand in order to act uppon it (e.g. 'unlock', drop', 'eat', 'put', 'wear'). If you are already holding an item when you take something else, the original item you were holding is automatically transferred into your backpack. You can view what you're carying using 'inventory'. Use 'look' to get a description of the room you're in. Type 'quit' to quit.  Start all multi-word commands with a verb.",
		'help_creatures' : "Despite its age and state of disrepair, Dark Castle contains a number of creatures. Some are helpful, some are not. There are three main commands for interacting with creatures: 'show', 'give', and 'attack'. 'show'ing an item to a creature may give you information about its opinion of that item. 'give'ing an item to a creature may generate a useful response - particularly if it's an object that the creature has an opinion about. Alas, not all encounters can be resolved amicably - and for these cases there is the 'attack' command. Not surprisingly, this can generate a very hostile response (see 'help attack' for more info). Lastly, be aware that each creature has its own priorities and point of view and will respond to Burt's actions accordingly.",
		'help_adjectives' : "Most nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
		'help_prepositions' : "There are two available prepositions: 'in' and 'to'. 'in' is used with the verb 'put'. This allows you to put items in containers. Example: 'put the rusty key in the wooden chest'. 'to' is used with the verbs 'show' and 'give'. This allows you to show or give items to creatures. Examples: 'show the rusty key to the goblin' or 'give the rusty key to the hedgehog'.",
		'help_read' :  "If you can't 'read' something (e.g. a note or a scroll) try 'examine' instead. The item may have some readable text written on it that you'll learn more about via 'examine'.",
		'help_attack' : "There are various creatures that reside in Dark Castle. Some are friendly but some may not be. Burt can 'attack' a creature using whatever weapon he is holding in his hand. If the creature is hostile and Burt is wielding the correct weapon he may be able to slay it. However there are risks to attacking as well. If the creature is friendly, an 'attack' may scare it away and Burt may lose a valuble ally. And if the creature is hostile but Burt is wielding the wrong weapon, Burt himself may perish. As in real life, combat in Dark Castle is frought!",
		
		### universal objects ###
		'backpack' : "Your trusty, well-worn leather backpack",
		'burt' : "Yep, that's you Burt. A fine specimen of a man. If not for the drooling and the farting I don't know how you'd fend off the ladies.",
		'fist' : "Yep, that's your fist. Still bruised from the last time you swung and missed and hit a wall...", 
		'conscience' : "Burt, Dark Castle is quite murky enough without pondering your prodigal and Hal-esque misspent youth!",

		### wrong way errors ###
		'wrong_way_0' : "Ouch! Burt, stop walking into walls!",
		'wrong_way_1' : "Ouch! You have walked into a wall.",
		'wrong_way_2' : "There's no exit that way.",
		'wrong_way_3' : "You can't go that way.",
		'wrong_way_4' : "And exactly how do you propose to do that?",

		### interpreter errors ###
		'interp_error_0' : "Burt, I have no idea what you're talking about!",
		'interp_error_1' : "Burt, are you babbling again?",
		'interp_error_2' : "Burt, I'm just going to pretend I didn't hear that.",
		'interp_error_3' : "Burt, you've said some strange things over the years but that was a doosey!",
		'interp_error_4' : "Burt! What would your mother say if she heard you speaking like that!?",

		### writing objects ###
		'rusty_lettering' : "'ABANDON HOPE ALL YE WHO EVEN THINK ABOUT IT'",
		'dwarven_runes' : "'Goblin Wallopper'",
		'messy_handwriting' : "...ode is X. Don't tell anyo..",
		'small_printing' : "'ACME AXE: Effective at dispatching small dragons, large crocodiles, and even the most agressive of trees.'",
		'illuminated_letters' : "First with great effort and then, surprisingly, with surety and confidence, you read out loud the text on the scroll. Your voice booms forth of its own accord - as if some part of your brain has been getting ready to say these words all your life. The rest of brain is struggling just to make sense of what you're saying with such confidence... it seems to be something along the lines of a recipe with ingredients... so if the 'heir to the true king' (whoever that might be)... reads 'this precious parchment'(you're pretty sure that means the scroll you're holding)... in the Throne Room (you've been there!)... while 'adorned with the gleaming headpiece of state' (whatever that means)... and also requiring that 'so long as the castle remains invested with a representative of our most noble heraldic charge seen ever upon our crest, seal, and glorious coat of arms' (even Ms. Lusk would have no clue what this means but she would notice that an awful lot of the Illuminated Letters in this sentence include a hedgehog with a sword and a key)... and then it finishes on a rather dramatic high note with the words 'upon the hour these conditions be met, a new King of Bright Castle shall shine forth and be proclaimed!'",
		'calligraphy' : "'The Kinging Scroll'",
		'trademark' : "'McVities'",
		
		### ViewOnly objects ###
		'dark_castle' : "Dark Castle looms over you. Its facade of blackened turrets and cracked walls is dour and singlularly univiting. It's hard to imagine but your great grandma Nana used to tell wonderous stories of the old days when the castle gleamed brightly on its hill and was a beacon of order and goodness for the land. Maybe it's because of the stories, but you've always had a bit of an itch to venture inside. The place has somehow called to you - almost daring you to enter - and now that a round of beer and your alehouse repuation as a fearless ruffian are on the line, you intend to answer the call!",		
		'moat' : "You know Burt, you've never heard anyone say 'It's a hot out - I think I'll go for a swim in the Dark Castle Moat'... and now you know why. The dark and muddy water is repellent and it swirls in a way that makes you suspect there's something down there you'd rather not meet.",
		'alcove' : "A small indentation in the west wall near the Iron Portcullis. It is just deep enough to hold one Control Panel and one Goblin.",
		'faded_tapestries' : "The Main Hall Faded Tapestries are vast and elaborate, covering both the east and the west walls. They appear to depict an unkempt figure breaking into a solitary white house and from there pillaging a Great Underground Empire. Strangely, there is a looming figure near the top of the west tapestry who appears to be tapping with his fingers on a many-buttoned plank and staring intently into a window filled with text. For some reason the figure disconcerts you.. his presence in the Faded Tapestries fills you with existential dread and forces you to question your agency and the very nature of your being... BURT!! Get hold of yourself man! You're a mangey, pub-crawling adventurer who lives in his mom's basement. You don't even know what half those words mean. Stop staring at tapestries and get out there and find the treasure you fool!!",
		'stone_coffer' : "This is the sort of coffer that, in better days, was no doubt filled to the brim will brightly shining gold pieces. Unfortunately, as you'd begun to fear, those days are long past and now the coffer is filled only with a deep layer of dust.",
		'family_tree' : "It appears to show the family tree of the Flathead dynasty. Though generally agreed to have peaked (nadired?) during the reign of Dimwit Flathead and petered out shortly there-after during the inglorious rulership of Wurb Flathead, this Family Tree tells a different story. It claims that a remote uncle of Wurb continued the line for seven more generations and eventually ended with William 'The Wanderer' Flathead only a little over 100 years ago. The area below William is indistinct and feels incomplete.. as if there are details still waiting to be filled in.\n\nAt the very top of the Family Tree you see a royal crest. Oddly enough, it appears to be a Hedgehog bearing a Shiny Sword and a Silver Key.",
		'dead_goblin' : "Even in its demise, the Dead Goblin looks fierce and resolute. Whoever dispatched this enemy must be an adventurer of some renown!",
		
		### item objects ###
		'rusty_key' : "An old Rusty Key... the one they gave you at the pub when you swore to pillage the Dark Castle. What could you possibly do with it?",
		'shiny_sword' : "The Shiny Sword glitters even in the dim light. Despite its age, the edge is keen and looks ready for action. There are Dwarven Runes engraved upon the blade.",
		'torn_note' : "This must have dropped from the Goblin's hand when you slew it. The Torn Note is ragged and only barely readable.", 
		'grimy_axe' : "A nasty looking weapon - and poorly maintained too. If you ever get out of this castle you should set aside some time to polish it. You notice uppon inspection that there is some Small Printing on the handle.",
		'silver_key' : "The small silver_key glitters in the dim light. It certainly stands out in the otherwise dreary Dark Castle. If you find a glittering silver keyhole somewhere this is definitely the key for it!",
		'kinging_scroll' : "Wow this thing is fancy! Huge letters with little pictures inside them and all sorts of curvy flourish at the end of each and every letter. Burt, your humble biscuit-baking, pub-crawling brain doesn't even know what to call this thing but if it did you would call it an illuminated manuscript composed (of course) of Illuminated Letters. Thanks to the hard and thankless work of your first grade teacher, Ms. Lusk, you could probably just manage to read the Illuminated Letters.",
		'random_mcguffin' : "It's a radom test McGuffin - just what you've always wanted!!",

		### food objects ###
		'cheese_wedge' : "A small wedge of cheese you absconded with from the larder. It's very small - so small that a lone mouse could probably make off with the whole thing - but your mother was saving it for company so you suspect it's quite delicious.",
		'stale_biscuits' : "The Stale Biscuits are rather unappetizing. There is a Trademark baked into the biscuits.",

		### beverage objects ###
		'fresh_water' : "After your trudge up the hill to Dark Castle the Fresh Water looks invitingly refreshing.",

		### clothes objects ###
		'royal_crown' : "Giant rubies: check. Dozens of glittering jewels: check. Gleaming gold and precious metals: check. Yep, this is a *seriously royal* crown you've got here Burt!",
		'baseball_cap' : "Burt, it's a code-testing Baseball Cap! Your favorite kind!!",
		'hedgehog_broach' : "The silver Hedgehog Broach is about an inch in diameter and is carved with the crest of a hedgehog bearing a sword and a key. It's strangely familiar... you've seen one just like it... long ago... examining the Hedgehog Broach up close triggers a long forgotten memory...\n\nyou were only five or six years old... you and all your family were at the bedside of your great grandmother, Nana Baker. She was old - very, very old - so old no even was sure how old - not even Nana. She'd been unable to eat or get out of bed for the past week and the village healer had given his solemn verdict that at long last her time had come. The whole village had come round to pay their last respects but now it was just family left. She looked very tired and her eyes were closed.\n\n'Thomas', said Nana, meaning your father, 'I'm weary... be a good lad and go heat me some tea... Nice and hot please.'. Next she sent your mother off for a special pillow she'd loaned to a friend. Soon every member of the family was off on an errand and it was just you and Nana.\n\nQuite suddenly, Nana's eyes opened, bright blue and wide awake. 'Well, Burty, finally we can have a little chat. I wish you were a bit older but now will have to do. Tell me Burty, how do ya feel about baking biscuits?'\n\n'It's na so bad' you'd stammered back.\n\nNana laughed and gave you a warm smile. 'Don't feel bad Burty, I wasn't much of a Baker myself - had a bit of a wild romantic streak in me - just like you. You remind me so much of my Willy... and that's not entirely an accident mind you. Thought I might see a resemblance in your grandfather or father but they were mindful lads and happy enough to be Bakers. I guess it's waited for you to show itself. Probably just as well.'\n\n'Ah Willy... now don't get me wrong, Papa Baker was a good man - hard working and with a kind heart - took me hand when many others wouldn't have and always treated me good. But you're from different stock Burty, very different. And that comes with some responsibilities... you've got a destiny 'afore you and that can be hard on young man with no expecting of it. That's why I'm telling you this now.'\n\n'Your real great grandpa was Willy... William Herbert... last of the line of Flatheads... or so everyone's been told. He was a handsome man... like you Burty. And unlike the rest of his family - full of romance and laughter and travel and adventure. Could be a bit reckless at times but he had a good heart. He proposed to me right proper he did... didn't really have to... he was so high up in society... and so much older too... but the moment I told him he dropped right to one knee and popped the question. Didn't care the least what people said! Swore we'd elope if the high priest wouldn't marry us... and he would have too!'\n\n'Alas, that crazy man... four months before the big day he was wandering about the castle entrance, wearing his bathrobe and Royal Crown, smoking his pipe and reading a book as he walked, as usual, and boom, he trips on the drawbridge and falls right into the Moat! Eaten right up in one big bite by one of those mean old crocodiles that have swum in it forever. Oh the day I heard the news...' And with these words she touched the Hedgehog Broach she always wore over her heart. 'It was a dark day Burty, a dark day for me an' for the castle and all the lands around.'\n\n'Someday Burty William Baker, someday you'll be King. And when you is, you be a good King... a kind and courageous and bold king... and when you is King don't ya be going walking off the edge of the drawbridge with no weapon in your hands and breaking young girl's hearts - you hear me?'\n\nStunned by this strange tale you began to stammer an answer but just then your Father returned with the hot tea. With a wink just for you, Nana's eyes closed again and she sank back into the bed. Minutes later she was gone.\n\nFor years and years you wondered what she was talking about and eventually you began to doubt the conversation had ever even happened. Over time it had faded completely... but here in Dark Castle, with the Hedgehog Broach before you, the memory is clear and real. Nana was buried with her beloved broach - she had insisted on it. This must have been a matching mate - presumably worn by Willy himself.",

		### wear descriptions ###
		'wear_royal_crown' : "You now feel more regal.",
		'wear_hedgehog_broach' : "There's no sign of magical properties but you're confident that Nana would be glad to see the Hedgehog Broach being worn in the castle again after all these years. You pause and wonder for a moment and wonder if there are any lessons you can still learn from Nana's last words to you...",
		
		### remove descriptions ###
		'remove_royal_crown' : "You suddenly feel a bit less kingly.",
		'remove_hedgehog_broach' : "You look down fondly at the broach in your hand and wonder if there are any lessons you can still learn from Nana's last words to you...",

		### eat descriptions ###
		'cheese_eat' : "tastes delicious!",
		'biscuit_eat' : "taste like damp cardboard that's been run over by a cart. You already regret eating them.",
#		".. especially as to some poor creature out there they might be a rare and wonderous delicacy.",

		### drink descriptions ###
		'water_drink' : "was refreshing!",

		### test objects ###
		'brass_key' : "The key is brass.",
		'bubbly_potion' : "The cork-stopperd glass vial contains a bubbly green potion.",
		'wooden_chest' : "An old wooden chest.",
				
		### container objects ###
		'crystal_box' : "Atop an ornate pedestal to the left of the throne sits an intricate Crystal Box. The crystal panels are heavily leaded and skillfully carved such that you're unable to tell what may lie within. There is a silver keyhole on the front of the crystal_box that glitters brilliantly - much like the shiny_sword in fact - in the otherwise dark and brooding room. The top of the Crystal Box is engraved with Calligraphy.",
		
		### jug objects ###
		'glass_bottle' : "A clear glass bottle suitable for carrying a liquid. Alas, if only it was filled with ale...",
		
		### door objects ###
		'front_gate' : "The Front Gate is just north of the Dark Castle's drawbridge. It is 10 feet tall and reenforced with steel bands. Imposing indeed! There is Rusty Lettering across the top of the gate and a rusty keyhole next to a handle.",
		'iron_portcullis' : "Beyond the iron portcullis you can dimly make out the next room.",

		### switch objects ###
		'left_lever' : "The Left Lever is old and rusty.",
		'middle_lever' : "The Middle Lever is old and rusty.",
		'right_lever' : "The Right Lever is old and rusty.",

		### warnings ###
		'entrance_south_warn_1' : "Don't be ridiculous Burt. You just swore to the whole pub that you'd march into the Dark Castle, grab the gold, and buy everyone drinks with it. That's why they gave you the Rusty Key. You can't turn back now!",

		'eat_biscuits_warning_1' : "You'd really rather not. You've been rooming in your Mom's basement and living off the Stale Biscuits in her pantry ever since you finished school - mostly so that you could spend whatever money you had at the pub. You don't mind sleeping in the basement but the Stale Biscuits are really getting to you.. you'll need to be a lot hungrier than you are now before you'll be able to keep another of those down!",
		'eat_biscuits_warning_2' : "Don't do it Burt. You know they'll only give you indigestion... and to some poor creature out there they might be a rare and wonderous delicacy.",
		

		### timers ###
		'test_timer_1' : "Tick 1",
		'test_timer_2' : "Tick 2",
		'test_timer_3' : "Boom!",
		'big_bomb' : "The Big Bomb has a Blue Button on it.",
		'blue_button' : "The Blue Button seems to dare you to push it.",
		'blue_button_result' : "Uh-oh Burt... not sure you should have pushed that...",

		'hedgehog_eats_timer_1' : "The Royal Hedgehog is ravenously devouring the Stale Biscuits and is taking no notice of you at all.",
		'hedgehog_eats_timer_2' : "The Royal Hedgehog has eaten through half the Stale Biscuits but is still giving them all of its attention.",
		'hedgehog_eats_timer_3' : "The Royal Hedgehog is nearly done eating all of the Stale Biscuits and is beginning to look around a bit.",
		'hedgehog_eats_timer_4' : "The Royal Hedgehog has finished the Stale Biscuits and is vigilantly looking around.",

		### machine objects ###
		'control_panel' : "The Control Panel contains three levers: a Left Lever, a Middle Lever, and a Right Lever. The control panel also contains a Red Button. There are no directions posted as to what the controls are for or how to use them (a clear ISO lapse if ever you've seen one Burt).",

		'throne' : "High-backed and intricately carved, the Throne is secured to the floor and wedged against the castle wall behind it. It does not look entirely comfortable but it must have once been very grand indeed. Alas, like the rest of Dark Castle, it is now dingy and ominous with only faint hints of its past glory. The Throne must have heard many secrets in its time... perhaps it still holds some?",

		'die_in_moat_result' : "With confidence and vigor you pitch off the side of the drawbridge and into the Moat. Who knew it would be full of crocodiles?",

		'moat_croc_scared_result' : "With courage and boldness to spare you leap from the drawbridge into the murky waters of the Moat. Apparently the last time you did this you terrified the local wildlife so much that they are still in hiding. After treading water for a few minutes you clamber back onto the drawbridge.",

		'moat_get_crown_result' : "With courage and boldness to spare you leap from the drawbridge into the murky waters of the Moat. A less resolute adventurer might have turned tail at the sight of the oncoming giant crocodile but not you Burt. Treading water with your feet you take a two-handed grip on your weapon and get ready to face your destiny. Just before reaching you the primitive reptile realizes that you are armed and ready to fight (crocs are famously near-sighted). In surprise and fear it belches up the contents of it's stomach - including the Royal Crown - and flees in fear. With a deft athleticism unlike anything you've ever displayed before today you sheath your weapon, snag the Royal Crown before it sinkes, and in one smooth motion adroitly hoist yourself back onto the drawbridge one handed. The lads at the pub would fall over at the sight of your skill and courage! (though mind you, they fall over on a regular basis as it is)",

		'cant_turn_back_result' : "Don't be ridiculous Burt. You just swore to the whole pub that you'd march into the Dark Castle, grab the gold, and buy everyone drinks with it. That's why they gave you the Rusty Key. You can't turn back now!",

		'throne_push_result' : "You push hard on the Throne. Nothing happens but one side of the throne feels a bit askew - as if something was wedged behind it. Strange...",
		
		'throne_pull_result' : "Hoping to find some sort of secret compartment filled with gold - or at least a good souvenir to show to the lads back at the pub - you pull and prod the Throne. As you are pulling the throne forward you hear a metallic 'clank' and something rolls out from beneath the Throne.. it appears to be a Hedgehog Broach. It must have been wedged between the Throne and the castle wall all these years... since the days of the last King! The sight of it brings back old memories... \n\nYou have a strong urge to examine the Hedgehog Broach more closely.",
		
		'nothing_happens_result' : "Nothing happens.",

		'toggle_portcullis_result' : "You hear a loud clank, a whirring of gears, and the Iron Portcullis suddenly ",
		
		'portcullis_doesnt_open_result' : "You press the button and hear a whirring of gears but nothing happens.",



		### creatures ###
		'guard_goblin' : "The Guard Goblin stands in the Alcove guarding the Control Panel and is armed and dangerous. It wields a Grimy Axe and looks at you with watchful malice. This goblin clearly takes its guard duties very seriously. It would not be wise to approach the Iron Portcullis or the Control Panel (or the Guard Goblin!) un-armed.",


		### attack defaults ###
		'not_attackable_default' : "You consider attacking but then realize that the act is futile. This foe cannot be vanquished by force of arms. You must find another path to victory.",
		'creature_flee_default_res_key' : "The creature flees in terror from your unprovoked attack.",
		'creature_death_default_res_key' : "You dispatch your enemy with one blazing fast strike of your weapon!",
		'burt_death_default_res_key' : "You are helpless against its onslaught. You will need a better weapon if you are to survive this foe.",
		'no_result_default_res_key' : "You only barely manage to parry with your own weapon!",


		### creature responses ###
		
		# guard_goblin #
		'show_goblin_shiny_sword' : "The Guard Goblin's face turns ashen at the sight of the Shiny Sword. It trembles and takes a step back.",
		'show_goblin_default' : "The Guard Goblin glares at you with a hauty expression of disdain and then imperiously motions for you to hand the item over for further inspection.",
		'show_goblin_stale_bisuits' : "The Guard Goblin scowels at the Stale Biscuits, wrinkles its nose, and then mutters something about 'gauche and impertinent' under its breath. You get the distinct impression that the Guard Goblin doesn't think much of biscuits - or biscuit bakers for that matter.",
		'give_goblin_default' : "The Guard Goblin pockets the item and mutters something about the need to confiscate articles of dubious provenance from ill-favored vagrants.",
		'give_goblin_stale_biscuits' : "The Guard Goblin waves its hand dismissively at the suggestion that it take reciept of the Stale Biscuits and makes an expression indicating that it would be best if we all just pretended that this had never happened.",
		'give_goblin_shiny_sword' : "The Guard Goblin blanches and backs away, terrified at the very thought of even touching the Shiny Sword.",
		'burt_slain_by_goblin' : "With an echoing war cry you charge the Guard Goblin, flailing your arms wildly in all directions as you come. This technique has served you well during drunken altercations at the pub but it proves less effective against a trained mercenary. The last thing you ever see is the Guard Goblin calmly stepping into fighting stance and drawing back its weapon.",
##		previously, 'burt_slain_by_goblin' finsiehd with "'s Grimy Axe swinging towards your head.",
		'goblin_slain' : "The Shiny Sword surges with power and lethal heft in your hand. A preternatural calm comes over you. You were born for this moment. Your raucous pub crawling days were a mere temporary distraction. you know in your bones that this primal showdown was meant to be and that, with the Shiny Sword at your command, you were meant to win it. Resolute, and with a confidence you have never even imagined having up until this very moment, you stride forward to meet your foe in battle.",
##	 previously, 'goblin_slain' finished with " and dispatch him with one blazing fast strike of your sword.",
##		'goblin_slays_burt' : "The Guard Goblin swings the Grimy Axe with a lightening-fast stroke and you are helpless against its onslaught. You will need a better weapon if you are to survive this foe.",
##		'goblin_slays_burt' : "You are helpless against its onslaught. You will need a better weapon if you are to survive this foe.",
##		'parry_goblin' : "You only barely manage to parry with your own weapon.",
		'goblin_attacks_result' : "The Guard Goblin does not take kindly to your presence in the north side of the room.",

		# royal_hedgehog #
		'hungry_hedgehog' : "This poor little Royal Hedgehog has seen better days. It looks gaunt and like it skipped breakfast - and maybe lunch and dinner too. But despite looking in need of a good meal the Royal Hedgehog's eyes have a bright, territorial gleam in them and it appears to have quite a preference for shiny things. You don't know why but you feel an innate fondness for this small but valiant creature.",
		'show_hedgehog_stale_biscuits' : "The Royal Hedgehog's eyes light up with excitement! Apparently, Stale Biscuits are a favorite hedgehog delacacy. The Royal Hedgehog gives you a look half way between hopeful and pleading.",
		'show_hedgehog_shiny_sword' : "The Royal Hedgehog gives a small squeek of excitement. It gives you a yearning look, clearly hoping that you will return its long-time favorite object.",
		'give_hedgehog_biscuits' : "With a yelp of grateful delight the starving hedgehog leaps upon the Stale Biscuits and begins to devour them.",
		'hedgehog_eating' : "The hedgehog is eating ravenously.",
		'give_hedgehog_sword' : "The hedgehog beams at you with gratitude for returning the Shiny Sword. From a hidden fold of its fur it takes out a Silver Key and, bowing, places it in your hand.",
		'hedgehog_sword_returned' : "This hedgehog is on top of the world! It has recently devoured a meal of Stale Biscuits (a rare delicacy among hedgehogs) and now has it's favorite shiny object back. It looks upon you with gratitude and devotion. It sees within you a nobility, compassion, and destiny beyond anything you've hitherto imagined possessing.",
		'hedgehog_flees' : "You strike at the Royal Hedgehog and, with a terrified squeek, it flees from your unprovoked attack. You know in your heart that you will come to regret this unkingly deed.",
		'attack_hedgehog_warning_1' : "BURT! What has gotten into you?? We have an evil castle to conquer. Stop trying to slay defenseless woodland creatures!", # old text: "You take a wild swipe at the Royal Hedgehog but it nimbly leaps aside."
		'attack_hedgehog_warning_2' : "Burt, I mean it - leave the poor little Hedgehog alone!",
		'hedgehog_guard_result' : "The moment you approach the Shiny Sword the territorial Royal Hedgehog springs forward, blocks your path, and bares it's teeth.",
		'fed_hedgehog_keeps_sword_result' : "The Royal Hedgehog now looks considerably more bright-eyed and bushy-tailed.",
		'fed_hedgehog_loses_sword_result' : "The Royal Hedgehog now looks considerably more bright-eyed and bushy-tailed.",
		'hedgehog_desc_smug' : "The Royal Hedgehog is looking svelte and chipper. It has the swagger of a hedgehog that has just scored a meal of Stale Biscuits and still has it's favorite shiny possession.",
		'hedgehog_desc_yearn' : "The Royal Hedgehog is looking svelte and chipper but not entirely content. It's clearly grateful for its recent meal but keeps looking at you hopefully.",
		'hedgehog_distracted_result' : "The Royal Hedgehog is too busy eating its favorite meal of Stale Biscuits to notice what you are doing.",

		### kinging_scroll ###
		'scroll_wrong_room_result' : "Upon reading the Kinging Scroll aloud you hear a distant rumble as if great powers are at work... but then it fades... perhaps you need to read it somewhere else to complete the recipe?",
		'scroll_no_hedgehog_result' : "Upon reading the Kinging Scroll aloud, there is a rumble and a bright flash of light in the sky.. but then it dims and the sound fades. Alas, some vital ingredient has gone missing in the castle... this is grim Burt... you may need to start your adventures over from the start and play through with a more benevolent spirit.",
		'scroll_crown_not_worn_result' : "Upon reading the Kinging Scroll aloud, the clouds outside part, the sun shines, there is a booming sound... but then it fades away abruptly. There's one missing ingredient that's keeping the Kinging Scroll from performing its magic... if only there was some token of royal lineage... perhaps some form of headpiece you could wear.. that would proclaim your birthright...",
		'scroll_win_game_result' : "Upon reading the Kinging Scroll aloud the clouds outside part, the sun shines, there is a booming sound like a great and thunderous gong that echoes and rebounds across the land! By the scroll's power the castle is scourgafied and all that was once dark is now glimmering with color and ligtht. Where Dark Castle once lurked, now gleams Bright Castle! The Stone Coffer magically fills with gold (and also a conveniently provided and legally complete deed to Bright Castle). And suddenly Burt, you find your own somewhat threadbare Baker's clothing replaced by garments of rich velvet and silk. Moments later, the Royal Hedgehog scampers into the Throne Room, places the Silver Sword at your feet, and kneels in fealty. Well done Burt! To the amazement of your family and friends - and the eternal pride of your great grandmother, Nana - you are now the King of Bright Castle!!",


		### room objects ###
		'entrance' : "*** Entrance ***\n\nYou are standing atop the drawbridge before the daunting entrance of Dark Castle. To the north is the Front Gate. To the south the way back home. To the east and west of your precarious perch on the drawbridge - and about three feet below you - is the Moat.",
		'main_hall' : "*** Main Hall ***\n\nYou are standing in what was once the sumptuous main hall of the castle. Faded Tapestries hang on the east and west walls. The Front Gate is to the south. And a foreboding archway leads to the north.",

		'antechamber' :"*** Antechamber ***\n\nYou are standing in a what feels more like a wide, tall-ceilinged corridor than a room. Apparently this is the room-before-the-room, the pre-room before the really, really grand room that comes after it. If so, the next room must be quite something because back in it's day this spot was clearly impressive. Alas, like all of the castle it has fallen on dark times and now feels more sinister than grand. The east and west walls are bare stone. To the south is an open passageway leading to the Main Hall and to the north there is an Iron Portcullis that guards the path to the grand chamber beyond. Near the Iron Portcullis on the west wall there is a small Alcove. It appears to have a Control Panel with some levers and a button on it but you can't see it very well due to the dim light. The whole north end of the room is cloaked in shadows that make you uneasy.",
		
		'throne_room' : "*** Throne Room ***\n\nThe room you're currently in is vast - almost cavernous. At the far end sits what must have once been a grand and glorious Throne. To the right of the Throne is a giant Stone Coffer and to the left an elegant pedestal that holds what appears to be a delicate Crystal Box. On either wall there are tall windows - now shattered and ruined - but you you remember hearing stories from your great grandmother, Nana, of the beautiful, glowing stained glass that once filled them. And above the room's entrance hangs a vast (though quite dusty) Family Tree."
}
