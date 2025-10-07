# program: Cleesh game engine
# name: Tom Snellgrove
# description: static dictionary initialization module


### this module declares static variables ###
### these variable values never change ###
### also, these variable values cannot be objects ###
### (because static_init => class_def) ###


### static dict ###
engine_static_dict = {

	### universal constants ###
    'engine_name' : "Cleesh",

	'engine_version' : '3.8.1 build 0013 [9/28/2025])', # api.features.bug-fix (internal); was '3.8.0 build 0013 [12/11/2024])'

	### Menu Constants ###
	'game_lst' : ['cup_of_tea', 'dark_castle'],

	### interp lists ###

	'articles_lst' : ['a', 'an', 'the'],

	'pre_interp_word_lst' : ['quit', 'wait', 'again', 'restart', 'save', 'restore'],
    
	'one_word_secret_lst' : ['debug_xyzzy'], # was 'debug_poke53281,0' before the cmd queue was implemented

    'one_word_only_lst' : ['credits', 'score', 'version'],

	'one_word_convert_lst' : ['inventory', 'look', 'stand', 'jump'],

	'one_word_travel_lst' : ['north', 'south', 'east', 'west'],

	'assumed_noun_2word_lst' : ['exit', 'drop', 'stow', 'eat', 'wear'],

	'one_or_two_word_lst' : ['help'], 

	'known_verb_lst' : ['attack', 'close', 'drink', 'drop', 'eat', 'examine', 'open',
		'give', 'go', 'help', 'lock', 'pull','push', 'put', 'read', 'show', 'take',
		'unlock', 'wear', 'enter', 'exit', 'stand', 'stow', 'jump'
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


	#### ONE WORD & ERRORS ####

	### one-word commands - non-objeects ###
	'credits' : "The Cleesh game engine was written and programmed by Tom.",

	### error messages ###
	'misc_err_0' : ", I have no idea what you're talking about!",
	'misc_err_1' : ", are you babbling again?",
	'misc_err_2' : ", I'm just going to pretend I didn't hear that.",
	'misc_err_3' : ", you've said some strange things over the years but that was a doosey!",
	'misc_err_4' : "! What would your Mother say if she heard you speaking like that!?",

	### direction errors ###
	'dir_err_0' : "Ouch! Stop walking into walls!",
	'dir_err_1' : "Ouch! You have walked into a wall.",
	'dir_err_2' : "There's no exit that way.",
	'dir_err_3' : "You can't go that way.",
	'dir_err_4' : "And exactly how do you propose to do that?",

	### help commands ###
	'help' : "Help syntax = 'help <option>'. Help options = 'basics', 'abbreviations', 'adjectives', 'articles', 'attack', 'creatures', 'command-queue', debug', 'inventory', 'multiples', 'one-word-commands', prepositions', 'read', 'save', 'travel', or 'verbs'.",
	'help_basics' : "You can 'take' an object that you can see. Use 'read' to read text you find written on objects. To travel, use the 'go' command: 'go <cardinal direction>'. Travel can be further abbreviated to just: '<cardinal direction>'.  You can view what you're carying using 'inventory'. Use 'look' to get a description of the room you're in. Start all multi-word commands with a verb. Type 'quit' to quit.",
	'help_creatures' : "Despite its age and state of disrepair, Dark Castle contains a number of creatures. Some are helpful, some are not. There are three main commands for interacting with creatures: 'show', 'give', and 'attack'. Showing an item to a creature may give you information about its opinion of that item. Giving an item to a creature may generate a useful response - particularly if it's an object that the creature has an opinion about. Alas, not all encounters can be resolved amicably - and for these cases there is the 'attack' command. Not surprisingly, this can generate a very hostile response (see 'help attack' for more info). Lastly, be aware that each creature has its own priorities and point of view and will respond to your actions accordingly.",
	'help_adjectives' : "Most nouns have an adjective (e.g. 'rusty key'). The interpreter recognizes adjectives but only requires them if other similar nouns are in the room. So 'take rusty key' and 'take key' are equivalent unless there is another key in the room.",
	'help_prepositions' : "There are several available prepositions including: 'in', 'on', 'with', 'to' and 'from'. 'in' and 'on' are used with the verb 'put'. This allows you to put items in containers or 'on' surfaces. Example: 'put the rusty key in the wooden chest' or 'put the cheese wedge on the shelf'. 'with' is used to indicate an object to use when performing an action. Example: 'unlock the crystal door with the platinum key'. If you use a verb that is typically performmed with an object (e.g. 'lock', 'unlock', or 'attack') - but omit the the 'with' clause - Dark Castle will assume that you want to perform the command with the object in your hand. 'to' is used with the verbs 'show' and 'give'. This allows you to specify which creature you want to show or give items to. Examples: 'show the rusty key to the goblin' or 'give the rusty key to the hedgehog'. 'from' is used with the verb 'drink'. Examples: 'drink water from cup'.",
    'help_read' :  "If you find an object with text written on it, you can 'read <text>'. Alternatively, 'examine <text>' and 'read <object with text on it>' prodcue similar results.",
	'help_attack' : "There are various creatures that reside in Dark Castle. Some are friendly but some may not be. You can 'attack' a creature using whatever weapon he is holding in his hand. If the creature is hostile and you are wielding the correct weapon you may be able to slay it. However there are risks to attacking as well. If the creature is friendly, an 'attack' may scare it away and you may lose a valuble ally. And if the creature is hostile but you are wielding the wrong weapon, you yourself may perish. As in real life, combat in Dark Castle is frought!",
	'help_debug_error' : "The first rule of debug mode is that we don't talk about debug mode.",
	'help_debug' : "There are currently 3 main features to debug mode: 1) Python errors are shown rather than muted, 2) A module prefix is provided for game errors, and 3) The following debug verbs are usable: ",
    'help_save' : "Type 'save' to save your game. Type 'restore' to restore from save. There is only one save slot. New saves over-write old saves. Restoring over-writes current game state.",
    'help_travel' : "In general, the following cardinal directions are available for travel: ",
    'help_multiples' : "The 'take' or 'drop' commands can be used with multiple items by specifying 'all'. For example: 'take all' or 'drop all'. You can also exclude one item by using the 'except' clause. For example: 'take all except rusty key'.",
    'help_command-queue' : "In cases where you already know your next several commands, you can enter them on one line, separated by commas. For example: 'go north, open door, take sword'. The game will process each command in order.",
    'help_inventory' : "Your inventory includes what is in your hand, what you are wearing, and what is in your backpack. Other creatures can see what is in your hand and what your are wearing but not what is in your backpack. If you issue a command that requires an item to be in your hand (e.g. 'drop sock') but the item is currently worn or in your backpack, the Cleesh interpreter will implicitly move the item to your hand and any item already in your hand will be simultaneously moved to your backpack.",
}

