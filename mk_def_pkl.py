# program: dark castle v3.49
# name: Tom Snellgrove
# date: Nov 13, 2021
# description: default object instantiation module (used as a tool)


# import statements
import pickle
from class_def import Invisible, TravelEffect, Writing, ViewOnly, Item, Food, Beverage, Container, Jug, Door, Room, GameState

# object instantiation - starting state
rusty_lettering = Writing('rusty_lettering', 'Rusty Lettering', "lettering", 'rusty_lettering')
dwarven_runes = Writing('dwarven_runes', 'Dwarven Runes', "runes", 'dwarven_runes')
messy_handwriting = Writing('messy_handwriting', 'Messy Handwriting', 'handwriting', 'messy_handwriting')
small_printing = Writing('small_printing', 'Small Printing', 'printing', 'small_printing')
illuminated_letters = Writing('illuminated_letters', 'Illuminated Letters', 'letters', 'illuminated_letters')
calligraphy = Writing('calligraphy', 'Calligraphy', 'calligraphy', 'calligraphy')
trademark = Writing('trademark', 'Trademark', 'trademark', 'trademark')

dark_castle = ViewOnly('dark_castle', "Dark Castle", "castle", 'dark_castle', None)
moat = ViewOnly('moat', 'Moat', 'moat', 'moat', None)
backpack = ViewOnly('backpack', "Backpack", "backpack", 'backpack', None)
burt = ViewOnly('burt', 'Burt', "burt", 'burt', None)
fist = ViewOnly('fist', 'Fist', "fist", 'fist', None)
conscience = ViewOnly('conscience', 'Conscience', "conscience", 'conscience', None)
faded_tapestries = ViewOnly('faded_tapestries', 'Faded Tapestries', 'tapestries', 'faded_tapestries', None)
alcove = ViewOnly('alcove', 'Alcove', 'alcove', 'alcove', None)
stone_coffer = ViewOnly('stone_coffer', 'Stone Coffer', 'coffer', 'stone_coffer', None)
family_tree = ViewOnly('family_tree', 'Family Tree', 'tree', 'family_tree', None)

rusty_key = Item('rusty_key', 'Rusty Key', "key", 'rusty_key', None)
shiny_sword = Item('shiny_sword', 'Shiny Sword', "sword", 'shiny_sword', dwarven_runes)
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None) # test object
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'bubbly_potion', None) # test object
torn_note = Item('torn_note', 'Torn Note', 'note', 'torn_note', messy_handwriting)
grimy_axe = Item('grimy_axe', 'Grimy Axe', 'axe', 'grimy_axe', small_printing)
silver_key = Item('silver_key', 'Silver Key', 'key', 'silver_key', None)
kinging_scroll = Item('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', illuminated_letters)

cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None, 'cheese_eat')
stale_biscuits = Food('stale_biscuits', 'Stale Biscuits', 'biscuits', 'stale_biscuits', trademark, 'biscuit_eat')

fresh_water = Beverage('fresh_water', 'Fresh Water', 'water', 'fresh_water', None, 'water_drink')

wooden_chest = Container('wooden_chest', 'wooden chest', "chest", 'wooden_chest', None,
				False, False, brass_key, [bubbly_potion]) # test object
crystal_box = Container('crystal_box', 'Crystal Box', 'box', 'crystal_box', calligraphy,
				False, False, silver_key, [kinging_scroll])
## giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])

glass_bottle = Jug('glass_bottle', 'Glass Bottle', 'bottle', 'glass_bottle', None, True, [fresh_water])

front_gate = Door('front_gate', 'Front Gate', "gate", 'front_gate', rusty_lettering, False, False, rusty_key)
## screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)
iron_portcullis = Door('iron_portcullis', 'Iron Portcullis', 'portcullis', 'iron_portcullis', None, True, False, None)

control_panel = ViewOnly('control_panel', 'Control Panel', 'panel', 'control_panel', None)
throne = ViewOnly('throne', 'Throne', 'throne', 'throne', None)

entrance_south = TravelEffect('entrance_south', ["go", "go", "south"], 'entrance_south', True, 'pre-action_trig', None, None, [])
entrance_east_no_weap = TravelEffect('entrance_east_no_weap', ["go", "go", "east"], 'entrance_east_no_weap',
				True, 'pre-action_trig', 'death', False, [shiny_sword, grimy_axe])
entrance_west_no_weap = TravelEffect('entrance_west_no_weap', ["go", "go", "west"], 'entrance_west_no_weap',
				True, 'pre-action_trig', 'death', False, [shiny_sword, grimy_axe])

entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, [dark_castle, moat],
				[front_gate], {'north' : front_gate}, [entrance_south, entrance_east_no_weap, entrance_west_no_weap])
main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
				[shiny_sword, front_gate], {'south' : front_gate}, [])
antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None, [alcove, control_panel],
				[torn_note, grimy_axe, iron_portcullis], {'north' : iron_portcullis}, [])
throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
				[throne, silver_key, crystal_box, iron_portcullis], {'south' : iron_portcullis}, [])


### active_gs is the central store of game info ###
active_gs = GameState(
		'active_gs',
		{'messy_handwriting' : ""},
		{
				'entrance' : {'north' : main_hall},
				'main_hall' : {'south' : entrance, 'north' : antechamber},
				'antechamber' : {'south' : main_hall, 'north' : throne_room},
				'throne_room' : {'south' : antechamber}
		},
		{
				'rusty_key' : False,
				'main_hall' : False,
				'shiny_sword' : False,
				'throne_room' : False,
				'silver_key' : False,
				'kinging_scroll' : False
		},
		{'universal' : [backpack, burt, fist, conscience]},
		{
				'score' : 0,
				'move_counter' : 0,
				'end_of_game' : False,
				'game_ending' : "tbd",
				'backpack' : [rusty_key, cheese_wedge, stale_biscuits, glass_bottle],
				'hand' : [],
				'room' : entrance,
				'out_buff' : ""
		}
)

# instantiated objects added to list
master_obj_lst = [active_gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, cheese_wedge, stale_biscuits, fresh_water, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, entrance_south, entrance_east_no_weap, entrance_west_no_weap, entrance, main_hall, antechamber, throne_room]


# list written to pickle
with open('default_obj_pickle', 'wb') as f:
		pickle.dump(master_obj_lst, f)

