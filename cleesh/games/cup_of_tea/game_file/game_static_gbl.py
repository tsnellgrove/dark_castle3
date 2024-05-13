# game: A Cup of Tea
# name: Tom Snellgrove
# description: holds the static game dictionary


### this module declares static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => class_def) ###


### static dict ###
game_static_dict = {


	#### STANDARD DICT ELEMENTS ####

	### menu info ###
 
	'game_name' : 'cup_of_tea',
    
	'game_full_name' : 'A Cup of Tea',
    
	'game_descript' : "A very simple game that proves out the multi-game ability of the Cleesh engine.",

	### universal constants ###
	'game_version' : '0.10 (5/12/2024)',

	### title and score dicts ###
    'title_factor' : 10,

	'titles_by_score' : {
		-10: 'Cecily the Strained',
		0: 'Cecily the Stressed', 
		10: 'Burt the Serene'
	},

	'score_dict' : {
        'drink' : {('tea', None) : 10}
	},

# cecily, comfy_chair, pub,

	### one-word commands - non-objeects ###
	'introduction' : "Hello!\n\nYou are Cecily-the-Serene - or at least you would be - if only you could manage to get a quiet moment to yourself to have a cup of tea. But as the youngest daughter of the family that runs the only pub in the village, quiet moments can be hard to come by!\n\nType 'help' for help.",
	'credits' : "The A Cup of Tea game was written and programmed by Tom.",


	#### VISIBLE OBJ ####

	### writing objects ###
    'cursive' : "'A drink with jam and bread'",
    'block_text' : "McGiggin's Pub (close the door you fool!)",

	### ViewOnly objects ###
	
	### item objects ###
	'rusty_key' : "An old Rusty Key... the one they claim opens the front gate to Dark Castle. Just last night, wasn't Burt bragging that he would take it and storm the castle and use the gold to buy everyone drinks?",
	'brass_key' : "You try to keep this handy. You never know when you'll need it.",

	### food objects ###

	### liquid objects ###
	'tea' : "Look at that - a perfectly brewed cup of tea. If only you could get a quiet moment to enjo it.",

	### clothes objects ###

	### container objects ###

	### surface objects ###
	'dingy_shelf' : "The Dingy Shelf is in urgent need of dusting - but it's a pretty high shelf so you haven't gotten to it lately.",

	### PortableLiquidContainer objects ###
	'tea_cup' : "Hand cast from river-side clay by your mother and perfectly proportioned, this is your favorit Tea Cup.", 
	
	### door objects ###
	'creaky_door' : "The front door to your familie's pub (and home, since you live on the second floor). It's always had a ferocious creak to it.",

	### creatures ###
	
	# feature_lst #

	# burt #
	'burt' : "You cast an apraising inner eye and take stock: Manly rough-and-tumble good looks - check, Affable demeanor paired with self-depreciating humor - check!, A lifetime of finely-honed baking skills - check!! Yep - that's you Burt - A fine specimen of a man. If not for the belching and the farting I don't know how you'd fend off the ladies!",
	
	# feature_lst # 
	'hand' : "Yes, that's your Hand. Small, like the rest of you, with long dexterous fingers with a knack for sewing but a few calouses from serving and daily chores. Your favorit Tea Cup is just the right size for this hand...", 

	## attack result display ##
	'attack_method_default_result' : "nimbly dodges the attack.",
	'tgt_flee_dc' : "terrirfied and flees from the unprovoked attack.",
	'tgt_death' : "slain by the blazing-fast strike!",
	'src_death' : "helpless against the onslaught. A better weapon will be needed to survive this foe.",
	'no_result' : "only barely able to dodge the assult!",
	'easy_dodge' : "easily able to duck and dodge the blow.",
	'hard_dodge' : "only barely able to dodge the assult!",
	'easy_parry' : "easily able to parry and thwart the blow.",
	'hard_parry' : "only barely able to parry the assult!",
	'jump_back' : "startled and compelled to leap back in surprise.",

	### room objects ###
	'entrance' : "You are atop the drawbridge before the daunting entrance of Dark Castle. To the north is the Front Gate. To the south, the way back home. To the east and west of your precarious perch on the drawbridge - and about three feet below you - is the Moat.",
	
	'main_hall' : "You are in what was once the sumptuous main hall of the castle. Faded Tapestries hang on the east and west walls. The Front Gate is to the south. And a foreboding archway leads to the north.",

	'antechamber' :"You are in a what feels more like a wide, tall-ceilinged corridor than a room. Apparently this is the room-before-the-room, the pre-room before the really, really grand room that comes after it. If so, the next room must be quite something because, back in it's day, this spot was clearly impressive. Alas, like all of the castle, it has fallen on dark times and now feels more sinister than grand. The east and west walls are bare stone. To the south is an open passageway leading to the Main Hall and to the north there is an Iron Portcullis that guards the path to the grand chamber beyond. Near the Iron Portcullis on the west wall there is a small Alcove. It appears to have some kind of apperatus in it but you can't see it very well due to the dim light and the Guard Goblin standing in front of it and glowering at you. The whole north end of the room is cloaked in shadows that make you uneasy.",

	'throne_room' : "The room you're currently in is vast - almost cavernous. At the far end sits what must have once been a grand and glorious Throne. To the right of the Throne is a giant Stone Coffer and to the left an elegant pedestal that holds what appears to be a delicate Crystal Box. On either wall there are tall windows - now shattered, ruined, and completely choked with thorned vines - but you you remember hearing stories from your great grandmother, Nana, of the beautiful, glowing stained glass that once filled them. And above the room's entrance hangs a vast (though quite dusty) Family Tree.",


	#### MACH OBJ & DISP ####

	### warnings ###
	'entrance_south_warn_1' : "Don't be ridiculous Burt. You just swore to the whole pub that you'd march into the Dark Castle, grab the gold, and buy everyone drinks with it. That's why they gave you the Rusty Key. You can't turn back now!",
	'eat_biscuits_warning_1' : "You'd really rather not. You've been rooming in your Mom's basement and living off the Stale Biscuits in her pantry ever since you finished school - mostly so that you could spend whatever money you had at the pub. You don't mind sleeping in the basement but the Stale Biscuits are really getting to you.. you'll need to be a lot hungrier than you are now before you'll be able to keep another of those down!",
	'eat_biscuits_warning_2' : "Don't do it Burt. You know they'll only give you indigestion... and to some poor creature out there they might be a rare and wonderous delicacy.",
	'attack_hedgehog_warning_1' : "BURT! What has gotten into you?? We have an evil castle to conquer. Stop trying to slay defenseless woodland creatures!", # old text: "You take a wild swipe at the Royal Hedgehog but it nimbly leaps aside."
	'attack_hedgehog_warning_2' : "Burt, I mean it - leave the poor little Hedgehog alone!",

	### timers ###
	'hedgehog_eats_timer_1' : "The Royal Hedgehog is ravenously devouring the Stale Biscuits and is taking no notice of you at all.",
	'hedgehog_eats_timer_2' : "The Royal Hedgehog has eaten through half the Stale Biscuits but is still giving them all of its attention.",
	'hedgehog_eats_timer_3' : "The Royal Hedgehog is nearly done eating all of the Stale Biscuits and is beginning to look around a bit.",
	'hedgehog_eats_timer_4' : "The Royal Hedgehog has finished the Stale Biscuits and is vigilantly looking around.",

	### switch objects ###
	'left_lever' : "The Left Lever is old and rusty.",
	'middle_lever' : "The Middle Lever is old and rusty.",
	'right_lever' : "The Right Lever is old and rusty.",
	'red_button' : "The Red Button is to the right of the three levers. You have no idea what it does but it's very big... and red... and shiny. Without concious intent, your hands begins to reach out to push the Big. Red. Shiny. Candy-Like. Button...",
	'throne_pre_broach' : "High-backed and intricately carved, the Throne is secured to the floor and wedged against the castle wall behind it. It does not look entirely comfortable but it must have once been very grand indeed. Alas, like the rest of Dark Castle, it is now dingy and ominous with only faint hints of its past glory. The Throne must have heard many secrets in its time... perhaps it still holds some?",
	'throne_post_broach' : "High-backed and intricately carved, the Throne is secured to the floor and wedged against the castle wall behind it. It does not look entirely comfortable but it must have once been very grand indeed. Alas, like the rest of Dark Castle, it is now dingy and ominous with only faint hints of its past glory.",

	### machines & results ###
	'control_panel' : "The Control Panel contains multiple levers and a button. There are no directions posted as to what the controls are for or how to use them (a clear ISO lapse if ever you've seen one!).",

	'die_in_moat_result' : "With confidence and vigor you pitch off the side of the drawbridge and into the Moat. Who knew it would be full of crocodiles?",
	'moat_croc_scared_result' : "With courage and boldness to spare you leap from the drawbridge into the murky waters of the Moat. Apparently the last time you did this you terrified the local wildlife so much that they are still in hiding. After treading water for a few minutes you clamber back onto the drawbridge.",
	'moat_get_crown_result' : "With courage and boldness to spare you leap from the drawbridge into the murky waters of the Moat. A less resolute adventurer might have turned tail at the sight of the oncoming giant crocodile but not you Burt. Treading water with your feet you take a two-handed grip on your weapon and get ready to face your destiny. Just before reaching you the primitive reptile realizes that you are armed and ready to fight (crocs are famously near-sighted). In surprise and fear it belches up the contents of it's stomach - including the Royal Crown - and flees in fear. With a deft athleticism unlike anything you've ever displayed before today you stow your weapon, snag the Royal Crown before it sinkes, and in one smooth motion adroitly hoist yourself back onto the drawbridge one handed. The lads at the pub would fall over at the sight of your skill and courage! (though mind you, they fall over on a regular basis as it is)",

	'cant_turn_back_result' : "Don't be ridiculous Burt. You just swore to the whole pub that you'd march into the Dark Castle, grab the gold, and buy everyone drinks with it. That's why they gave you the Rusty Key. You can't turn back now!",

	'throne_push_result' : "You push hard on the Throne. Nothing happens but one side of the throne feels a bit askew - as if something was wedged behind it. Strange...",		
	'throne_pull_result' : "Hoping to find some sort of secret compartment filled with gold - or at least a good souvenir to show to the lads back at the pub - you pull and prod the Throne. As you are pulling the throne forward you hear a metallic 'clank' and something rolls out from beneath the Throne.. it appears to be a Hedgehog Broach. It must have been wedged between the Throne and the castle wall all these years... since the days of the last King! The sight of it brings back old memories... \n\nYou have a strong urge to examine the Hedgehog Broach more closely.",
	
	'nothing_happens_result' : "Nothing happens.",
	'toggle_portcullis_result' : "You hear a loud clank, a whirring of gears, and the Iron Portcullis suddenly ",		
	'portcullis_doesnt_open_result' : "You press the button and hear a whirring of gears but nothing happens.",

#		'hedgehog_guard_result' : "The moment you approach the Shiny Sword the territorial Royal Hedgehog springs forward, blocks your path, and bares it's Fierce Teeth.",
	'fed_hedgehog_keeps_sword_result' : "The Royal Hedgehog now looks considerably more bright-eyed and bushy-tailed.",
	'fed_hedgehog_loses_sword_result' : "The Royal Hedgehog now looks considerably more bright-eyed and bushy-tailed.",
	'hedgehog_desc_smug' : "The Royal Hedgehog is looking svelte and chipper. It has the swagger of a hedgehog that has just scored a meal of Stale Biscuits and still has it's favorite shiny possession.",
	'hedgehog_desc_yearn' : "The Royal Hedgehog is looking svelte and chipper but not entirely content. It's clearly grateful for its recent meal but keeps looking at you hopefully.",
	'hedgehog_distracted_result' : "The Royal Hedgehog is too busy eating its favorite meal of Stale Biscuits to notice what you are doing.",

	'scroll_wrong_room_result' : "Upon reading the Kinging Scroll aloud you hear a distant rumble as if great powers are at work... but then it fades... perhaps you need to read it somewhere else to complete the recipe?",
	'scroll_no_hedgehog_result' : "Upon reading the Kinging Scroll aloud, there is a rumble and a bright flash of light in the sky.. but then it dims and the sound fades. Alas, some vital ingredient has gone missing in the castle... this is grim Burt... you may need to start your adventures over from the start and play through with a more benevolent spirit.",
	'scroll_crown_not_worn_result' : "Upon reading the Kinging Scroll aloud, the clouds outside part, the sun shines, there is a booming sound... but then it fades away abruptly. There's one missing ingredient that's keeping the Kinging Scroll from performing its magic... if only there was some token of royal lineage... perhaps some form of headpiece you could wear.. that would proclaim your birthright...",
	'scroll_win_game_result' : "Upon reading the Kinging Scroll aloud the clouds outside part, the sun shines, there is a booming sound like a great and thunderous gong that echoes and rebounds across the land! By the scroll's power the castle is scourgafied and all that was once dark is now glimmering with color and ligtht. Where Dark Castle once lurked, now gleams Bright Castle! The Stone Coffer magically fills with gold (and also a conveniently provided and legally complete deed to Bright Castle). And suddenly Burt, you find your own somewhat threadbare Baker's clothing replaced by garments of rich velvet and silk. Moments later, the Royal Hedgehog scampers into the Throne Room, places the Silver Sword at your feet, and kneels in fealty. Well done Burt! To the amazement of your family and friends - and the eternal pride of your great grandmother, Nana - you are now the Baron of Bright Castle!!",



	#### AUTO-DISP ####

	### updated room descriptions ###
	'antechamber_dispense_panel_result' :"You are standing in a what feels more like a wide, tall-ceilinged corridor than a room. Apparently this is the room-before-the-room, the pre-room before the really, really grand room that comes after it. If so, the next room must be quite something because back in it's day this spot was clearly impressive. Alas, like all of the castle it has fallen on dark times and now feels more sinister than grand. The east and west walls are bare stone. To the south is an open passageway leading to the Main Hall and to the north there is an Iron Portcullis that guards the path to the grand chamber beyond. Near the Iron Portcullis on the west wall there is a small Alcove. It appears to have a Control Panel with some levers and a button on it.",

	### enter descriptions ###
	'burt_enter_throne_pre_broach' : "Sitting in the throne, it feels slightly out of kilter - as if it's been pushed or pulled out of alignment by something...",

	### wear descriptions ###
	'burt_wear_royal_crown' : "You now feel more regal.",
	'burt_wear_hedgehog_broach' : "There's no sign of magical properties but you're confident that Nana would be glad to see the Hedgehog Broach being worn in the castle again after all these years. You pause and wonder if there are any lessons you can still learn from Nana's last words to you...",
			
	### remove descriptions ###
	'burt_remove_royal_crown' : "You suddenly feel a bit less kingly.",
	'burt_remove_hedgehog_broach' : "You look down fondly at the broach in your hand and wonder if there are any lessons you can still learn from Nana's last words to you...",		

	### eat descriptions ###
	'burt_eat_cheese_wedge' : "The Cheese Wedge tastes delicious!",
	'burt_eat_stale_biscuits' : "The Stale Biscuits taste like damp cardboard that's been run over by a cart. You already regret eating them.",

	### drink descriptions ###
	'burt_drink_well_water' : "That was refreshing!",

	### show descriptions ###
	'burt_show_guard_goblin_shiny_sword' : "The Guard Goblin's face turns ashen at the sight of the Shiny Sword. It trembles and takes a step back.",
	'burt_show_guard_goblin_default' : "The Guard Goblin glares at you with an officious expression of disdain and then imperiously motions for you to hand the item over for further inspection.",
	'burt_show_guard_goblin_stale_biscuits' : "The Guard Goblin scowels at the Stale Biscuits, wrinkles its nose, and then mutters something about 'gauche and impertinent' under its breath. You get the distinct impression that the officious Guard Goblin doesn't think much of biscuits - or of biscuit bakers either for that matter.",
	'burt_show_royal_hedgehog_stale_biscuits' : "The Royal Hedgehog's eyes light up with excitement! Apparently, Stale Biscuits are a favorite hedgehog delacacy. The Royal Hedgehog gives you a look half way between hopeful and pleading.",
	'burt_show_royal_hedgehog_shiny_sword' : "The Royal Hedgehog gives a small squeek of excitement and a yearning look - clearly hoping that you will return its long-time favorite object.",

	### give descriptions ###
	'burt_give_guard_goblin_default' : "The Guard Goblin pockets the item and mutters something about castle regulations that require the confiscation articles of dubious provenance from ill-favored vagrants.",
	'burt_give_guard_goblin_stale_biscuits' : "The Guard Goblin waves its hand dismissively at the suggestion that it take reciept of the Stale Biscuits and makes an expression indicating that it would be best if we all just pretended that this had never happened.",
	'burt_give_guard_goblin_shiny_sword' : "The Guard Goblin blanches and backs away, terrified at the thought of even touching the Shiny Sword.",
	'burt_give_royal_hedgehog_stale_biscuits' : "With a yelp of grateful delight the starving hedgehog leaps upon the Stale Biscuits and begins to devour them.",
	'burt_give_royal_hedgehog_shiny_sword' : "The hedgehog beams at you with gratitude and Loyalty for returning the Shiny Sword. From a hidden fold of its fur it takes out a Silver Key and, bowing, places it in your hand.",

	### description resulting from give ###
	'burt_give_royal_hedgehog_stale_biscuits_descript' : "The hedgehog is eating ravenously.",
	'burt_give_royal_hedgehog_shiny_sword_descript' : "This hedgehog is on top of the world! It has recently devoured a meal of Stale Biscuits (a rare delicacy among hedgehogs) and now has it's favorite shiny object back. It looks upon you with gratitude and loyal devotion. It sees within you a nobility, compassion, and destiny beyond anything you've hitherto imagined possessing.",

	### attack descriptions ###
	'royal_hedgehog_weapon_burt_*' : "The Royal Hedgehog squeeks in dismay as it dodges your malevolent agression. It's loyal gaze changes to one of bewilderment and hearbreak. 'Et tu Burtus?' Even as the loyal little creature gives way, you know in your heart that you will come to regret this unkingly deed.",
	'royal_hedgehog_unarmed_burt_*' : "The Royal Hedgehog seems to view your unarmed swipe as a playful challenge. It drops into a martial arts pose and begins making wax-on, wax-off motions with its paws.",
	'royal_hedgehog_*_*_*' : "The Royal Hedgehog is more nimble than you would have guessed! It adroitly balances on the balls of its feet and gets ready to bob and weave.",

	'guard_goblin_*_*_*' : "With an echoing war cry you charge the Guard Goblin, flailing your arms wildly in all directions as you come. This technique has served you well during drunken altercations at the pub but it proves less effective against a trained mercenary. The last thing you ever see is the Guard Goblin calmly stepping into fighting stance and drawing back its weapon.",
	'guard_goblin_shiny_sword_burt_*' : "The Shiny Sword surges with power and lethal heft in your hand. A preternatural calm comes over you. You were born for this moment. Your raucous pub crawling days were a mere temporary distraction. You know in your bones that this primal showdown was meant to be and that, with the Shiny Sword at your command, you were meant to win it. Resolute, and with a confidence you have never even imagined having up until this very moment, you stride forward to meet your foe in battle.",

	'burt_fierce_teeth_royal_hedgehog_*' : "The moment you approach the Shiny Sword the territorial Royal Hedgehog springs forward, blocks your path, and bares it's Fierce Teeth.",


	#### TEST OBJ ####

	### test descriptions ###
	'burt_enter_test_chair' : "The chair feels cozy and nice.",

	# items #
	'brass_key' : "The key is brass.",
	'random_mcguffin' : "It's a radom test McGuffin - just what you've always wanted!!",

	# containers #
	'bubbly_potion' : "The cork-stopperd glass vial contains a bubbly green potion.",
	'wooden_chest' : "An old wooden chest.",

	# garments #
	'baseball_cap' : "Burt, it's a code-testing Baseball Cap! Your favorite kind!!",

	# big_bomb machine, blue_button, & test_timer #
	'test_timer_1' : "Tick 1",
	'test_timer_2' : "Tick 2",
	'test_timer_3' : "Boom!",
	'big_bomb' : "The Big Bomb has a Blue Button on it.",
	'blue_button' : "The Blue Button seems to dare you to push it.",
	'blue_button_result' : "Uh-oh Burt... not sure you should have pushed that...",

	# creatures #
	'test_frog' : "The Test Frog looks testy.",

}		


# *** Not in Use ***
##		previously, 'burt_slain_by_goblin' finsiehd with "'s Grimy Axe swinging towards your head.",
##	 previously, 'goblin_slain' finished with " and dispatch him with one blazing fast strike of your sword.",
##		'goblin_slays_burt' : "The Guard Goblin swings the Grimy Axe with a lightening-fast stroke and you are helpless against its onslaught. You will need a better weapon if you are to survive this foe.",
##		'goblin_slays_burt' : "You are helpless against its onslaught. You will need a better weapon if you are to survive this foe.",
##		'parry_goblin' : "You only barely manage to parry with your own weapon.",
##		'hedgehog_flees' : "You strike at the Royal Hedgehog and, with a terrified squeek, it flees from your unprovoked attack. You know in your heart that you will come to regret this unkingly deed.",
#		'tgt_flee_dc' : "flees in terror from the unprovoked attack.",
#		'tgt_death' : "dispatch the enemy with one blazing fast strike!",

#		'creature_flee_default_res_key' : "The creature flees in terror from your unprovoked attack.",
#		'creature_death_default_res_key' : "You dispatch your enemy with one blazing fast strike of your weapon!",
#		'burt_death_default_res_key' : "You are helpless against its onslaught. You will need a better weapon if you are to survive this foe.",
#		'no_result_default_res_key' : "You only barely manage to parry with your own weapon!",
#		'not_attackable_default' : "You consider attacking but then realize that the act is futile. This foe cannot be vanquished by force of arms. You must find another path to victory.",

#		'burt_slain_by_goblin' : "With an echoing war cry you charge the Guard Goblin, flailing your arms wildly in all directions as you come. This technique has served you well during drunken altercations at the pub but it proves less effective against a trained mercenary. The last thing you ever see is the Guard Goblin calmly stepping into fighting stance and drawing back its weapon.",
#		'goblin_slain' : "The Shiny Sword surges with power and lethal heft in your hand. A preternatural calm comes over you. You were born for this moment. Your raucous pub crawling days were a mere temporary distraction. you know in your bones that this primal showdown was meant to be and that, with the Shiny Sword at your command, you were meant to win it. Resolute, and with a confidence you have never even imagined having up until this very moment, you stride forward to meet your foe in battle.",
#		'goblin_attacks_result' : "It seems that by entering the north side of the room you have violated a minor castle ordinance. The Guard Goblin is incensed and will not tolerate this flagrant defiance of orthodoxy!",
#		'hedgehog_flees' : "The Royal Hedgehog squeeks in dismay as it dodges your malevolent agression. Even as the loyal little creature gives way, you know in your heart that you will come to regret this unkingly deed.", # consternation alternatives: fright, dismay, alarm


# *** Not Game ***

"""
	### interp lists ###

	'articles_lst' : ['a', 'an', 'the'],

	'pre_interp_word_lst' : ['quit', 'wait', 'again', 'restart'],
    
	'one_word_secret_lst' : ['debug_poke53281,0'],

    'one_word_only_lst' : ['credits', 'score', 'version'],

	'one_word_convert_lst' : [
        'north', 'south', 'east', 'west',
        'inventory', 'look', 'stand'
    ],

	'assumed_noun_2word_lst' : ['drop', 'stowe', 'eat', 'wear'],

	'one_or_two_word_lst' : ['help'], 

	'known_verb_lst' : ['attack', 'close', 'drink', 'drop', 'eat', 'examine', 'open',
		'give', 'go', 'help', 'lock', 'pull','push', 'put', 'read', 'show', 'take',
		'unlock', 'wear', 'enter', 'exit', 'stand', 'stowe'
	],

	'prep_verb_lst' : ['put', 'show', 'give', 'attack', 'lock', 'unlock', 'drink'],
    
	'var_outcome_verb_lst' : ['give', 'attack'], # for reference; not actually used in score.disp_score()

	'debug_verb_lst' : ['get_weight', 'capacity', 'where_is'],

	'abbreviations_dict' : {
		'n' : 'north',
		's' : 'south',
		'e' : 'east',
		'w' : 'west',
		'i' : 'inventory',
		'l' : 'look',
		'get' : 'take',
		'x' : 'examine',
		'h' : 'help',
		'g' : 'again',
		'z' : 'wait',
        'q' : 'quit'
	},

    
	### error messages ###
	'misc_err_0' : "Burt, I have no idea what you're talking about!",
	'misc_err_1' : "Burt, are you babbling again?",
	'misc_err_2' : "Burt, I'm just going to pretend I didn't hear that.",
	'misc_err_3' : "Burt, you've said some strange things over the years but that was a doosey!",
	'misc_err_4' : "Burt! What would your Nana say if she heard you speaking like that!?",

	### direction errors ###
	'dir_err_0' : "Ouch! Burt, stop walking into walls!",
	'dir_err_1' : "Ouch! You have walked into a wall.",
	'dir_err_2' : "There's no exit that way.",
	'dir_err_3' : "You can't go that way.",
	'dir_err_4' : "And exactly how do you propose to do that?",

	### help commands ###
	'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'abbreviations', 'adjectives', 'articles', 'attack', 'creatures', 'debug', 'one-word-commands', prepositions', 'read', or 'verbs'.",
	'help_basics' : "Objects you can examine and interact with are capitalized. To travel, use the 'go' command: 'go <cardinal direction'. Travel can be further abbreviated to just: '<cardinal direction>'. Use 'read' to read text you find written on objects. You can 'take' one object that you can see into your hand at a time from the room, a container, your backpack, or from being worn. Your other hand is holding your light source. In many cases you must be holding an object in your hand in order to act uppon it (e.g. 'unlock', drop', 'eat', 'put', 'wear', 'drink'). If you are already holding an item when you take something else, the original item you were holding is automatically transferred into your backpack. You can view what you're carying using 'inventory'. Use 'look' to get a description of the room you're in. Start all multi-word commands with a verb. Type 'quit' to quit.",
	'help_creatures' : "Despite its age and state of disrepair, Dark Castle contains a number of creatures. Some are helpful, some are not. There are three main commands for interacting with creatures: 'show', 'give', and 'attack'. Showing an item to a creature may give you information about its opinion of that item. Giving an item to a creature may generate a useful response - particularly if it's an object that the creature has an opinion about. Alas, not all encounters can be resolved amicably - and for these cases there is the 'attack' command. Not surprisingly, this can generate a very hostile response (see 'help attack' for more info). Lastly, be aware that each creature has its own priorities and point of view and will respond to Burt's actions accordingly.",
	'help_adjectives' : "Most nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
	'help_prepositions' : "There are several available prepositions including: 'in', 'on', 'with', 'to' and 'from'. 'in' and 'on' are used with the verb 'put'. This allows you to put items in containers or 'on' surfaces. Example: 'put the rusty key in the wooden chest' or 'put the cheese wedge on the shelf'. 'with' is used to indicate an object to use when performing an action. Example: 'unlock the crystal door with the platinum key'. If you use a verb that is typically performmed with an object (e.g. 'lock', 'unlock', or 'attack') - but omit the the 'with' clause - Dark Castle will assume that you want to perform the command with the object in your hand. 'to' is used with the verbs 'show' and 'give'. This allows you to specify which creature you want to show or give items to. Examples: 'show the rusty key to the goblin' or 'give the rusty key to the hedgehog'. 'from' is used with the verb 'drink'. Examples: 'drink water from cup'.",
##	'help_read' :  "If you can't 'read' something (e.g. a note or a scroll) try 'examine' instead. The item may have some readable text written on it that you'll learn more about via 'examine'.",
    'help_read' :  "If you find an object with text written on it, you can 'read <text>'. Alternatively, 'examine <text>' and 'read <object with text on it>' prodcue similar results.",
	'help_attack' : "There are various creatures that reside in Dark Castle. Some are friendly but some may not be. Burt can 'attack' a creature using whatever weapon he is holding in his hand. If the creature is hostile and Burt is wielding the correct weapon he may be able to slay it. However there are risks to attacking as well. If the creature is friendly, an 'attack' may scare it away and Burt may lose a valuble ally. And if the creature is hostile but Burt is wielding the wrong weapon, Burt himself may perish. As in real life, combat in Dark Castle is frought!",
	'help_debug_error' : "The first rule of debug mode is that we don't talk about debug mode.",
	'help_debug' : "There are currently 3 main features to debug mode: 1) Python errors are shown rather than muted, 2) A module prefix is provided for game errors, and 3) The following debug verbs are usable: ",
    
    
"""