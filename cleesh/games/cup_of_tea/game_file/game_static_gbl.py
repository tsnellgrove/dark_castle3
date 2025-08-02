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

	### end info ###

	'read_bkstry_str' : "Would you like to know the game's backstory ", # default string
    
	'backstory' : "This space intentionally left blank.", # default string

	### universal constants ###
	'game_version' : '0.1.0', # was '0.15 (5/22/2024)' up untill 6/12/2024; no build # between releases

	### bodies of liquid the player cannot drink from ###
	'reservoir_lst' : [],

	### title and score dicts ###
    'title_factor' : 10,

	'max_score' : 10,

	'titles_by_score' : {
		-10: 'Cecily the Strained',
		0: 'Cecily the Stressed', 
		10: 'Cecily the Serene'
	},

	'score_dict' : {
        'drink' : {('tea', 'tea_cup') : 10}
	},

#	'give' : {('royal_hedgehog', 'shiny_sword') : 5},

	### one-word commands - non-objeects ###
	'introduction' : "Hello!\n\nYou are Cecily-the-Serene - or at least you would be - if only you could manage to get a quiet moment to yourself to have a cup of tea. But as the youngest daughter of the family that runs the only pub in the village, quiet moments can be hard to come by!\n\nType 'help' for help.",
	'credits' : "The A Cup of Tea game was written and programmed by Tom.",


	#### VISIBLE OBJ ####

	### writing objects ###
    'cursive' : "'A drink with jam and bread'",
    'block_text' : "McGiggin's Pub (close the door ya' fool!)",

	### ViewOnly objects ###
	
	### item objects ###
	'rusty_key' : "An old Rusty Key... the one they claim opens the front gate to Dark Castle. Just last night, wasn't Burt bragging that he would take it and storm the castle and use the gold to buy everyone drinks?",
	'brass_key' : "You try to keep this handy. You never know when you'll need it.",

	### food objects ###

	### liquid objects ###
	'tea' : "Look at that - a perfectly brewed cup of tea. If only you could get a quiet moment to enjoy it.",

	### clothes objects ###

	### container objects ###

	### surface objects ###
	'dingy_shelf' : "The Dingy Shelf is in urgent need of dusting - but it's a pretty high shelf so you haven't gotten to it lately.",

	### PortableLiquidContainer objects ###
	'tea_cup' : "Hand cast from river-side clay by your mother and perfectly proportioned, this is your favorite Tea Cup.", 
	
	### door objects ###
	'creaky_door' : "The front door to your familie's pub (and home, since you live on the second floor). It's always had a ferocious creak to it.",
    'comfy_chair' : "The Comfy Chair is a bit ragged around the edges but still cozy to curl up in. It's a small oasis of relaxation amidst a sea of ale-fuled raucousness.",

	### creatures ###
	
	# feature_lst #

	# creatures #
	'cecily_0': "You give yourself a self-concious once-over: at age 19 and the youngest daughter of Ethan Brewer, the prosperous owner of the town's busiest pub, you should be well on your way towards matrimony - but to your mother's dismay and your own deep gratitude, it appears to be nowhere on the horrizon. Of course you're also the more homely and introverted daughter - more fond of books than boys they say. Your older sister, Chrissy, the queen of the viallage, has always had a dozzen men at a time circling her in eratic orbits, moths to the flame - so who would ever notice you?",

	# creature feature_lst # 
	'hand' : "Yes, that's your Hand. Small, like the rest of you, with long dexterous fingers with a knack for sewing but a few calouses from serving and daily chores. Your favorit Tea Cup is just the right size for this hand...", 

	### room objects ###
    'pub' : "You are in your family's pub. Sunlight streams through the windows showing a room full of well-worn tables and chairs with a large bar standing across from the entrance. Any moment the regulars will arrive, clamoring for their favorite brews, arguing loudly over sports and poltics, and hurling darts in the general direction of the dart board - and the pub will ignite with sound and motion.",

	## attack result display ##

	#### MACH OBJ & DISP ####

	### warnings ###

	### timers ###

	### switch objects ###

	### machines & results ###
    'tea_drunk_win_result' : "Upon sipping your hot tea from your favorite Tea Cup, a deep sense serenity comes over you. This was the moment of peace you needed. You feel ready to face the day.",

	#### AUTO-DISP ####

	### updated room descriptions ###

	### enter descriptions ###
	'cecily_enter_comfy_chair' : "Your favorite comfy chair - the perfect place for a sip of tea!",

	### wear descriptions ###
			
	### remove descriptions ###

	### eat descriptions ###

	### drink descriptions ###
    'cecily_drink_tea' : "Ah tea, what a devine beverage it is!",

	### show descriptions ###

	### give descriptions ###

	### description resulting from give ###

	### attack descriptions ###

}		