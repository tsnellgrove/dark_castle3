# program: dark castle v3.56
# name: Tom Snellgrove
# date: Dec 31, 2021
# description: default object instantiation module (used as a tool)


# import statements
import pickle
from noun_class_def import Invisible, Writing, ViewOnly, Item, Food, Beverage, Clothes, Container, Jug, Door, Room
from noun_class_def import ButtonSwitch, SpringSliderSwitch, LeverSwitch
from cond_class_def import PassThruCond, NotInHandCond, StateCond, InHandAndStateCond, SwitchStateCond
from results_class_def import PassThruResult, BufferOnlyResult, BufferAndEndResult, BufferAndGiveResult, AddObjToRoomResult
from mach_class_def import InvisMach
from gs_class_def import GameState


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
random_mcguffin = Item('random_mcguffin', 'Random McGuffin', 'mcguffin', 'random_mcguffin', None)

cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None, 'cheese_eat')
stale_biscuits = Food('stale_biscuits', 'Stale Biscuits', 'biscuits', 'stale_biscuits', trademark, 'biscuit_eat')

fresh_water = Beverage('fresh_water', 'Fresh Water', 'water', 'fresh_water', None, 'water_drink')

royal_crown = Clothes('royal_crown', 'Royal Crown', 'crown', 'royal_crown', None, 'wear_royal_crown', 'remove_royal_crown', 'hat')
baseball_cap = Clothes('baseball_cap', 'Baseball Cap', 'cap', 'baseball_cap', None, None, None, 'hat')
hedgehog_broach = Clothes('hedgehog_broach', 'Hedgehog Broach', 'broach', 'hedgehog_broach', None,
				'wear_hedgehog_broach', 'remove_hedgehog_broach', 'pin')

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
throne = SpringSliderSwitch('throne', 'Throne', 'throne', 'throne', None, 'neutral', 'pre_act_switch_reset')
left_lever = LeverSwitch('left_lever', 'Left Lever', 'lever', 'left_lever', None, 'down', None)
middle_lever = LeverSwitch('middle_lever', 'Middle Lever', 'lever', 'middle_lever', None, 'down', None)
right_lever = LeverSwitch('right_lever', 'Right Lever', 'lever', 'right_lever', None, 'down', None)

hand_no_weap_cond = NotInHandCond('hand_no_weap_cond', [shiny_sword, grimy_axe])
hand_weap_1st_cond = InHandAndStateCond('hand_weap_1st_cond', [shiny_sword, grimy_axe], False)
hand_weap_repeat_cond = InHandAndStateCond('hand_weap_1st_cond', [shiny_sword, grimy_axe], True)
pass_thru_cond = PassThruCond('pass_thru_cond')
broach_dispensed_cond = StateCond('broach_dispensed_cond', True)
throne_push_cond = SwitchStateCond('throne_push_cond', ['pushed'])
throne_pull_cond = SwitchStateCond('throne_pull_cond', ['pulled'])

die_in_moat_result = BufferAndEndResult('die_in_moat_result', 'die_in_moat_result', 'death', True)
moat_croc_scared_result = BufferOnlyResult('moat_croc_scared_result', 'moat_croc_scared_result', True)
moat_get_crown_result = BufferAndGiveResult('moat_get_crown_result', 'moat_get_crown_result', royal_crown, True)
cant_turn_back_result = BufferOnlyResult('cant_turn_back_result', 'cant_turn_back_result', True)
throne_push_result = BufferOnlyResult('throne_push_result', 'throne_push_result', False)
nothing_happens_result = BufferOnlyResult('nothing_happens_result', 'nothing_happens_result', False)
throne_pull_result = AddObjToRoomResult('throne_pull_result', 'throne_pull_result', hedgehog_broach, False)

entrance_moat_mach = InvisMach('entrance_moat_mach', 'pre_act_cmd', False, None, [['go', 'east'], ['go', 'west']],
				None, [hand_no_weap_cond, hand_weap_1st_cond, hand_weap_repeat_cond],
				[die_in_moat_result, moat_get_crown_result, moat_croc_scared_result]) #machine_state = got_crown

entrance_south_mach = InvisMach('entrance_south_mach', 'pre_act_cmd', None, None, [['go', 'south']],
				None, [pass_thru_cond], [cant_turn_back_result])

broach_dispenser_mach = InvisMach('broach_dispenser_mach', 'post_act_switch', False, throne, ['pushed', 'pulled'],
				[throne], [broach_dispensed_cond, throne_push_cond, throne_pull_cond],
				[nothing_happens_result, throne_push_result, throne_pull_result])

entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, [dark_castle, moat],
				[front_gate], {'north' : front_gate}, [entrance_moat_mach, entrance_south_mach])
main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
				[shiny_sword, front_gate], {'south' : front_gate}, [])
antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None, [alcove, control_panel],
				[torn_note, grimy_axe, iron_portcullis, left_lever, middle_lever, right_lever], {'north' : iron_portcullis}, [])
throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
				[throne, silver_key, crystal_box, iron_portcullis], {'south' : iron_portcullis}, [broach_dispenser_mach])


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
				'kinging_scroll' : False,
				'royal_crown' : False,
				'hedgehog_broach' : False
		},
		{'universal' : [backpack, burt, fist, conscience]},
		{
				'score' : 0,
				'move_counter' : 0,
				'end_of_game' : False,
				'game_ending' : "tbd",
				'backpack' : [rusty_key, cheese_wedge, stale_biscuits, glass_bottle],
				'hand' : [],
				'worn' : [],
				'room' : entrance,
				'out_buff' : ""
		}
)

### instantiated objects added to list ###
### Used as an obj index in Interp() - must include all non-invisible obj ###
### invisible obj referenced in room.invis_obj_lst need not be listed ###
master_obj_lst = [active_gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, random_mcguffin, cheese_wedge, stale_biscuits, fresh_water, royal_crown, baseball_cap, hedgehog_broach, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, left_lever, middle_lever, right_lever, entrance, main_hall, antechamber, throne_room]

# list written to pickle
with open('default_obj_pickle', 'wb') as f:
		pickle.dump(master_obj_lst, f)

