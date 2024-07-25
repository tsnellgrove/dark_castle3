# program: dark castle
# name: Tom Snellgrove
# date: Feb 28, 2024
# description: default object instantiation module (used as a tool)


# import statements
import sys, os
root_path_str = os.path.realpath(__file__).replace('/cleesh/games/dark_castle/game_file/game_update.py','')
sys.path.append(root_path_str)

import pickle
from cleesh.class_std.invisible_class_def import Invisible
from cleesh.class_std.base_class_def import Writing, ViewOnly
from cleesh.class_std.room_class_def import Room
from cleesh.class_std.item_class_def import Item, Food, Liquid, Garment, Weapon
from cleesh.class_std.interactive_class_def import DoorSimple, DoorLockable
from cleesh.class_std.interactive_class_def import ContainerFixedSimple, ContainerFixedLidded, ContainerFixedLockable, Seat
from cleesh.class_std.interactive_class_def import ContainerPortableSimple, ContainerPortableLidded, ContainerPortableLockable
from cleesh.class_mach.switch_class_def import ViewOnlyLeverSwitch, ViewOnlyButtonSwitch, SeatSpringSliderSwitch
from cleesh.class_mach.cond_class_def import (TrueCond, WornCond, ObjOnRmFlrCond, ObjInRmCond, ObjInWorldCond, 
		ItemInHandCond, WeaponInHandCond, MachStateCond, TimerActiveCond, SwitchStateCond, LeverArrayCond)
from cleesh.class_mach.result_class_def import (BaseResult, 
		BufferOnlyResult, BufferAndEndResult, BufferAndGiveResult,
		AddObjToRoomResult, DoorToggleResult, AttackBurtResult, StartTimerResult, AddObjChgDescriptResult,
		TimerAndCreatureItemResult, ChgCreatureDescAndStateResult, PutItemInHandResult, TravelResult, AddObjToRoomAndDescriptResult)
from cleesh.class_mach.mach_class_def import InvisMach, ViewOnlyMach, ItemMach, Warning, Timer, ContainerFixedSimpleMach
from cleesh.class_std.creature_class_def import Creature
from cleesh.class_gs.gs_class_def import GameState
from cleesh.class_gs.map_class_def import Map
from cleesh.class_gs.io_class_def import IO
from cleesh.class_gs.score_class_def import Score
from cleesh.class_gs.end_class_def import End
from cleesh.class_gs.core_class_def import Core

# *** object instantiation - starting state ***

# Writing obj
rusty_lettering = Writing('rusty_lettering', 'Rusty Lettering', "lettering", 'rusty_lettering')
dwarven_runes = Writing('dwarven_runes', 'Dwarven Runes', "runes", 'dwarven_runes')
messy_handwriting = Writing('messy_handwriting', 'Messy Handwriting', 'handwriting', 'messy_handwriting')
small_printing = Writing('small_printing', 'Small Printing', 'printing', 'small_printing')
illuminated_letters = Writing('illuminated_letters', 'Illuminated Letters', 'letters', 'illuminated_letters')
calligraphy = Writing('calligraphy', 'Calligraphy', 'calligraphy', 'calligraphy')
trademark = Writing('trademark', 'Trademark', 'trademark', 'trademark')
gold_capitals = Writing('gold_capitals', 'Gold Capitals', 'capitals', 'gold_capitals')

# ViewOnly
dark_castle = ViewOnly('dark_castle', "Dark Castle", "castle", 'dark_castle', None)
moat = ViewOnly('moat', 'Moat', 'moat', 'moat', None)
backpack = ViewOnly('backpack', "Backpack", "backpack", 'backpack', None)
# burt = ViewOnly('burt', 'Burt', "burt", 'burt', None)
fist = ViewOnly('fist', 'Fist', "fist", 'fist', None)
fierce_teeth = ViewOnly('fierce_teeth', 'Fierce Teeth', 'teeth', 'fierce_teeth', None)
chewed_fingernails = ViewOnly('chewed_fingernails', 'Chewed Fingernails', 'fingernails', 'chewed_fingernails', None)
brass_lantern = ViewOnly('brass_lantern', 'Brass Lantern', "lantern", 'brass_lantern', None)
conscience = ViewOnly('conscience', 'Conscience', 'conscience', 'conscience', None)
faded_tapestries = ViewOnly('faded_tapestries', 'Faded Tapestries', 'tapestries', 'faded_tapestries', None)
alcove = ViewOnly('alcove', 'Alcove', 'alcove', 'alcove', None)
stone_coffer = ViewOnly('stone_coffer', 'Stone Coffer', 'coffer', 'stone_coffer', None)
family_tree = ViewOnly('family_tree', 'Family Tree', 'tree', 'family_tree', None)
dead_goblin = ViewOnly('dead_goblin', 'Dead Goblin', 'goblin', 'dead_goblin', None)
officiousness = ViewOnly('officiousness', 'Officiousness', 'officiousness', 'officiousness', None)
loyalty = ViewOnly('loyalty', 'Loyalty', 'loyalty', 'loyalty', None)

# Item
rusty_key = Item('rusty_key', 'Rusty Key', "key", 'rusty_key', None, 1)
torn_note = Item('torn_note', 'Torn Note', 'note', 'torn_note', messy_handwriting, 1)
silver_key = Item('silver_key', 'Silver Key', 'key', 'silver_key', None, 1)

# Food
cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None, 1)
stale_biscuits = Food('stale_biscuits', 'Stale Biscuits', 'biscuits', 'stale_biscuits', trademark, 3)

# Liquid
well_water = Liquid('well_water', 'Well Water', 'water', 'well_water', None, 0.5)

# Garment
royal_crown = Garment('royal_crown', 'Royal Crown', 'crown', 'royal_crown', None, 5, 'hat')
hedgehog_broach = Garment('hedgehog_broach', 'Hedgehog Broach', 'broach', 'hedgehog_broach', None, 1, 'pin')
red_bandana = Garment('red_bandana', 'Red Bandana', 'bandana', 'red_bandana', None, 1, 'hat')
big_medal = Garment('big_medal', 'Big Medal', 'medal', 'big_medal', gold_capitals, 2, 'pin')

# Weapon
grimy_axe = Weapon('grimy_axe', 'Grimy Axe', 'axe', 'grimy_axe', small_printing, 10, 
				[['arcs', 'lightening-fast stroke'],['cleaves', 'violent swing'],['hacks', 'deadly intent']])
shiny_sword = Weapon('shiny_sword', 'Shiny Sword', 'sword', 'shiny_sword', dwarven_runes, 10, 
				[['swings', 'blazing-fast assault'],['stabs', 'cunning unterhau']])

# Container
wooden_shelf = ContainerFixedSimple('wooden_shelf', 'Wooden Shelf', 'shelf', 'wooden_shelf', None, [], 999, 20, 'on')
crystal_box = ContainerFixedLockable('crystal_box', 'Crystal Box', 'box', 'crystal_box', calligraphy, ['kinging_scroll_temp'], 1, 999, 'in', False, False, silver_key)
earthen_jug = ContainerPortableSimple('earthen_jug', 'Earthen Jug', 'jug', 'earthen_jug', None, 1.5, [well_water], 0.5, 5, 'in')

# Door
front_gate = DoorLockable('front_gate', 'Front Gate', "gate", 'front_gate', rusty_lettering, False, False, rusty_key)
iron_portcullis = DoorLockable('iron_portcullis', 'Iron Portcullis', 'portcullis', 'iron_portcullis', None, False, False, None)

# Switches
left_lever = ViewOnlyLeverSwitch('left_lever', 'Left Lever', 'lever', 'left_lever', None, 'down', None, None)
middle_lever = ViewOnlyLeverSwitch('middle_lever', 'Middle Lever', 'lever', 'middle_lever', None, 'down', None, None)
right_lever = ViewOnlyLeverSwitch('right_lever', 'Right Lever', 'lever', 'right_lever', None, 'down', None, None)
red_button = ViewOnlyButtonSwitch('red_button', 'Red Button', 'button', 'red_button', None, 'neutral', 'neutral', 'auto_switch_reset')
throne = SeatSpringSliderSwitch('throne', 'Throne', 'throne', 'throne_pre_broach', None, [], 999, 2, 'on', [crystal_box], 'neutral', 'neutral', 'auto_switch_reset')

# test obj - not currently in use
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None, 1) # test object
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'bubbly_potion', None, 2) # test object
random_mcguffin = Item('random_mcguffin', 'Random McGuffin', 'mcguffin', 'random_mcguffin', None, 5) # test object
heavy_rock = Item('heavy_rock', 'Heavy Rock', 'rock', 'heavy_rock', None, 40)
baseball_cap = Garment('baseball_cap', 'Baseball Cap', 'cap', 'baseball_cap', None, 1, 'hat')
cardboard_box = ContainerFixedLidded('cardboard_box', 'Cardboard Box', 'box', 'cardboard_box', None, [], 999, 2, 'in', False)
small_barrel = ContainerPortableSimple('small_barrel', 'Small Barrel', 'barrel', 'small_barrel', None, 2, [], 5, 999, 'in')
red_shoebox = ContainerPortableLidded('red_shoebox', 'Red Shoebox', 'shoebox', 'red_shoebox', None, 1, [], 3, 999, 'in', False)
black_suitcase = ContainerPortableLockable('black_suitcase', 'Black Suitcase', 'suitcase', 'black_suitcase', None, 3, [], 7, 999, 'in', False, False, rusty_key)
screen_door = DoorSimple('screen_door', 'Screen Door', 'door', 'screen_door', None, False)
test_chair = Seat('test_chair', 'Test Chair', 'chair', 'test_chair', None, [], 999, 2, 'on', [wooden_shelf])

# test obj - currently in use
# TBD

# timers
hedgehog_eats_timer = Timer('hedgehog_eats_timer', 'auto_act', False, 0, 4, 'variable', False, 'temp_royal_hedgehog', True)

# conditions
true_cond = TrueCond('true_cond')
crown_not_worn_cond = WornCond('crown_not_worn_cond', royal_crown, 'burt_temp', False)
biscuits_in_hedgehog_hand_cond = ItemInHandCond('biscuits_in_hedgehog_hand_cond', stale_biscuits, 'royal_hedgehog_temp', True)
axe_not_in_goblin_hand_cond = ItemInHandCond('axe_in_goblin_hand_cond', grimy_axe, 'guard_goblin_temp', False)
no_weap_in_hand_cond = WeaponInHandCond('hand_no_weap_cond', 'burt_temp', False)
sword_on_floor = ObjOnRmFlrCond('sword_on_floor', 'main_haal_temp', shiny_sword, True)
sword_not_on_floor = ObjOnRmFlrCond('sword_not_on_floor', 'main_haal_temp', shiny_sword, False)
not_in_throne_room_cond = ObjInRmCond('not_in_throne_room_cond', 'throne_room_temp', 'burt_temp', False)
hedgehog_not_in_world_cond = ObjInWorldCond('hedgehog_not_in_world_cond', 'royal_hedgehog_temp', False)
goblin_in_world_cond = ObjInWorldCond('goblin_in_world_cond', 'guard_goblin_temp', True)
broach_dispensed_cond = MachStateCond('broach_dispensed_cond', True)
crown_not_dispensed_cond = MachStateCond('crown_not_dispensed_cond', False)
crown_dispensed_cond = MachStateCond('crown_dispensed_cond', True)
panel_not_dispensed_cond = MachStateCond('panel_not_dispensed_cond', False)
hedgehog_descript_updated_cond = MachStateCond('hedgehog_descript_updated_cond', True)
hedgehog_eats_timer_active_cond = TimerActiveCond('hedgehog_eats_timer_active_cond', hedgehog_eats_timer, True) # hedgehog is distracted
hedgehog_eats_timer_not_active_cond = TimerActiveCond('hedgehog_eats_timer_not_active_cond', hedgehog_eats_timer, False) # hedgehog is not eating
throne_push_cond = SwitchStateCond('throne_push_cond', ['pushed'])
throne_pull_cond = SwitchStateCond('throne_pull_cond', ['pulled'])
lever_array_matches_mach_state_cond = LeverArrayCond('lever_array_matches_mach_state_cond', [4,2,1])

# results
# pass_result = BufferOnlyResult('pass_result', False)
# moat_croc_scared_result = BufferOnlyResult('moat_croc_scared_result', True)
# nothing_happens_result = BufferOnlyResult('nothing_happens_result', False)
# throne_push_result = BufferOnlyResult('throne_push_result', False)
# portcullis_doesnt_open_result = BufferOnlyResult('portcullis_doesnt_open_result', False)
# hedgehog_distracted_result = BufferOnlyResult('hedgehog_distracted_result', True)
# scroll_wrong_room_result = BufferOnlyResult('scroll_wrong_room_result', False)
# scroll_no_hedgehog_result = BufferOnlyResult('scroll_no_hedgehog_result', False)
# scroll_crown_not_worn_result = BufferOnlyResult('scroll_crown_not_worn_result', False)

pass_result = BaseResult('pass_result', False, None, False)
moat_croc_scared_result = BaseResult('moat_croc_scared_result', False, None, True)
nothing_happens_result = BaseResult('nothing_happens_result', False, None, False)
throne_push_result = BaseResult('throne_push_result', False, None, False)
portcullis_doesnt_open_result = BaseResult('portcullis_doesnt_open_result', False, None, False)
hedgehog_distracted_result = BaseResult('hedgehog_distracted_result', False, None, True)
scroll_wrong_room_result = BaseResult('scroll_wrong_room_result', False, None, False)
scroll_no_hedgehog_result = BaseResult('scroll_no_hedgehog_result', False, None, False)
scroll_crown_not_worn_result = BaseResult('scroll_crown_not_worn_result', False, None, False)

# die_in_moat_result = BufferAndEndResult('die_in_moat_result', 'died.', True)
die_in_moat_result = BufferAndEndResult('die_in_moat_result', False, None, True, 'died.')

# scroll_win_game_result = BufferAndEndResult('scroll_win_game_result', 'won!', False)
scroll_win_game_result = BufferAndEndResult('scroll_win_game_result', False, None, False, 'won!')

# name, is_mach_state_set, mach_state_val, cmd_override, ending


moat_get_crown_result = BufferAndGiveResult('moat_get_crown_result', royal_crown, True)
axe_in_goblin_hand_result = PutItemInHandResult('axe_in_goblin_hand_result', False, 'guard_goblin_temp', grimy_axe)
throne_pull_result = AddObjChgDescriptResult('throne_pull_result', hedgehog_broach, throne, 'throne_post_broach', False)
dispense_panel_result = AddObjToRoomAndDescriptResult('dispense_panel_result', 'temp_control_panel', False)
toggle_portcullis_result = DoorToggleResult('toggle_portcullis_result', iron_portcullis, False)
goblin_attacks_result = AttackBurtResult('goblin_attacks_result', 'guard_goblin_temp', True)
hedgehog_attacks_result = AttackBurtResult('hedgehog_attacks_result', 'royal_hedgehog_temp', True)
start_hedgehog_timer_results = TimerAndCreatureItemResult('start_hedgehog_timer_results', hedgehog_eats_timer, False, 'royal_hedgehog', stale_biscuits)
fed_hedgehog_keeps_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_keeps_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_smug')
fed_hedgehog_loses_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_loses_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_yearn')


# warnings
entrance_south_warn = Warning('entrance_south_warn', 'pre_act_cmd', [['go', 'south']], 0, 0, True)
attack_hedgehog_warning = Warning('attack_hedgehog_warning', 'pre_act_cmd',
		[['attack', 'shiny_sword', 'royal_hedgehog'], ['attack', 'grimy_axe', 'royal_hedgehog']], 3, 0, True)
eat_biscuits_warning = Warning('eat_biscuits_warning', 'pre_act_cmd', [['eat','stale_biscuits']], 3, 0, True)

# machines
entrance_moat_mach = InvisMach('entrance_moat_mach', False, 'pre_act_cmd', None, [['go', 'east'], ['go', 'west']],
		None, [no_weap_in_hand_cond, crown_not_dispensed_cond, crown_dispensed_cond],
		[die_in_moat_result, moat_get_crown_result, moat_croc_scared_result],
		'entrance_temp', True) # mach_state == got_crown

broach_dispenser_mach = InvisMach('broach_dispenser_mach', False, 'post_act_switch', throne, ['pushed', 'pulled'],
		[throne], [broach_dispensed_cond, throne_push_cond, throne_pull_cond],
		[nothing_happens_result, throne_push_result, throne_pull_result],
		'throne_room_temp', True) # mach_state == broach_dispensed

dispense_panel_mach = InvisMach('dispense_panel_mach', False, 'auto_act', None, None, None, 
		[goblin_in_world_cond, panel_not_dispensed_cond], 
		[pass_result, dispense_panel_result],
		'antechamber_temp', True) # mach_state = has panel been dispensed

control_panel = ContainerFixedSimpleMach('control_panel', 'Control Panel', 'panel', 'control_panel', None, 
		[left_lever, middle_lever, right_lever, red_button], 999, 4, 'on',
		0, 'post_act_switch', red_button, ['pushed'], [left_lever, middle_lever, right_lever], 
		[lever_array_matches_mach_state_cond, true_cond], 
		[toggle_portcullis_result, portcullis_doesnt_open_result],
		'antechamber_temp', True) # mach_state == lever_array_value

hedgehog_eats_mach = InvisMach('hedgehog_eats_mach', None, 'post_act_cmd', None, 
		[['give', 'stale_biscuits', 'royal_hedgehog']], None, 
		[biscuits_in_hedgehog_hand_cond], [start_hedgehog_timer_results],
		'royal_hedgehog_temp', True)

hedgehog_guard_mach = InvisMach('hedgehog_guard_mach', None, 'pre_act_cmd', None, [['take', 'shiny_sword']], None, 
		[hedgehog_eats_timer_not_active_cond], [hedgehog_attacks_result],
		'royal_hedgehog_temp', True)

hedgehog_done_eating_mach = InvisMach('hedgehog_done_eating_mach', False, 
		'pre_act_timer', hedgehog_eats_timer, [True], None,									  
		[hedgehog_descript_updated_cond, sword_on_floor, sword_not_on_floor],
		[pass_result, fed_hedgehog_keeps_sword_result, fed_hedgehog_loses_sword_result],
		'royal_hedgehog_temp', True) # mach_state == has the machine  run? (ie. has the hedgehog's description been updated already?)

hedgehog_distracted_mach = InvisMach('hedgehog_distracted_mach', None, 'pre_act_cmd', None,
		[['give', '*', 'royal_hedgehog'], ['show', '*', 'royal_hedgehog']], None, 
		[hedgehog_eats_timer_active_cond], [hedgehog_distracted_result],
		'royal_hedgehog_temp', True)

goblin_attack_mach = InvisMach('goblin_attack_mach', None, 'pre_act_cmd', None, 
		[['examine', 'iron_portcullis'], ['examine', 'alcove'], ['examine', 'grimy_axe'], 
   		['take', 'grimy_axe'], ['open', 'iron_portcullis'], ['go', 'north']], None, 
		[true_cond], [goblin_attacks_result],
		'guard_goblin_temp', True)

re_arm_goblin_mach = InvisMach('re_arm_goblin_mach', None, 'auto_act', None, None, None,
		[axe_not_in_goblin_hand_cond], [axe_in_goblin_hand_result],
		'guard_goblin_temp', True)

kinging_scroll = ItemMach('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', 
		illuminated_letters, 1, None, 'post_act_cmd', None, 
		[['read', 'illuminated_letters'],['read', 'kinging_scroll'], ['examine', 'illuminated_letters']], None,
		[not_in_throne_room_cond, hedgehog_not_in_world_cond, crown_not_worn_cond, true_cond],
		[scroll_wrong_room_result, scroll_no_hedgehog_result, scroll_crown_not_worn_result, scroll_win_game_result],
		'kinging_scroll_temp', True)

# *** creatures	***

guard_goblin = Creature('guard_goblin', 'Guard Goblin', 'goblin', 'guard_goblin', None,
		None, [grimy_axe], [torn_note, dead_goblin], [big_medal], [chewed_fingernails, officiousness],
		[goblin_attack_mach, re_arm_goblin_mach],
		{
			shiny_sword : {'accept' : False, 'give' : None},
			stale_biscuits : {'accept' : False, 'give' : None},
			'def_give' : {'accept' : True, 'give' : None}
		},
		True,
		{
			'shiny_sword_burt_*' : 'tgt_death',
			'weapon_*_*' : 'easy_parry', # parry
			'*_*_*' : 'src_death'
		}, 93, 999)

royal_hedgehog = Creature('royal_hedgehog', 'Royal Hedgehog', 'hedgehog', 'hungry_hedgehog', None,
		None, [], [silver_key], [red_bandana], [fierce_teeth, loyalty],
		[attack_hedgehog_warning, hedgehog_eats_mach, hedgehog_guard_mach, hedgehog_done_eating_mach, hedgehog_distracted_mach],
		{
			shiny_sword : {'accept' : True, 'give' : silver_key},
			stale_biscuits : {'accept' : True, 'give' : None}
		},
		True,
		{
			'weapon_burt_*' : 'tgt_flee_dc',
			'unarmed_burt_*' : 'easy_dodge', # karate kid
			'*_*_*' : 'easy_dodge' # dodge
		}, 22, 999)

burt = Creature('burt', 'Burt', 'burt', 'burt', None,
		None, [], [rusty_key, cheese_wedge, stale_biscuits, earthen_jug], [], [fist, backpack, conscience, brass_lantern],
		[hedgehog_eats_timer],
		{},
		True,
		{
			'grimy_axe_guard_goblin_weapon' : 'hard_parry', # parry
			'grimy_axe_guard_goblin_*' : 'tgt_death',
			'fierce_teeth_royal_hedgehog_*' : 'jump_back'
		}, 106.5, 150) # note: for non-burt-creature testing frog_travel_mach was in burt.invis_lstj

# *** Rooms ***
entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, [dark_castle, moat],
		[burt], [entrance_moat_mach, entrance_south_warn, eat_biscuits_warning])
		# note: for timer testing, big_bomb was in entrance.floor_lst and blue_button was in entrance.feature_lst

main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
		[shiny_sword, royal_hedgehog, wooden_shelf], [eat_biscuits_warning])
		# note: for non-burt-creature testing, test_frog was in main_hall.floor_lst

antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
#		[alcove, left_lever, middle_lever, right_lever, red_button], [control_panel, guard_goblin], [])
		[alcove], [guard_goblin], [dispense_panel_mach])

throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
		[throne, crystal_box], [broach_dispenser_mach])

unreachable_1 = Room('unreachable_1', 'Unreachable', 'unreachable_1', 'unreachable_1', None, [], [], [])

unreachable_2 = Room('unreachable_2', 'Unreachable', 'unreachable_2', 'unreachable_2', None, [], [], [])

unreachable_3 = Room('unreachable_3', 'Unreachable', 'unreachable_3', 'unreachable_3', None, [], [], [])


# *** gs class modules ***

core = Core(
		'core', # name
		burt, # hero
        0, # move_count
        False, # is_debug
		{}, # str_to_obj_dict
		True # has_session_vars
		)

map = Map(
		'map', # name
		entrance, # hero_rm
		[{'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall},
		{'room_x' : entrance, 'dir_x' : 'south', 'door' : 'path', 'dir_y' : None, 'room_y' : unreachable_1},
		{'room_x' : entrance, 'dir_x' : 'east', 'door' : 'leap down to the moat', 'dir_y' : None, 'room_y' : unreachable_2},
		{'room_x' : entrance, 'dir_x' : 'west', 'door' : 'leap down to the moat', 'dir_y' : None, 'room_y' : unreachable_3},
		{'room_x' : main_hall, 'dir_x' : 'north', 'door' : 'passage', 'dir_y' : 'south', 'room_y' : antechamber},
#		{'room_x' : main_hall, 'dir_x' : 'north', 'door' : screen_door, 'dir_y' : 'south', 'room_y' : antechamber},
		{'room_x' : antechamber, 'dir_x' : 'north', 'door' : iron_portcullis, 'dir_y' : 'south', 'room_y' : throne_room}] # map_lst
		)

io = IO(
		'io', # name
		{}, # dyn_dict
		"", # buff_str
		"", # last_input_str
		'dark_castle' # game_name
		)

score = Score(
		'score', # name
		0, # score
		[] # pts_earned_lst
		)

end = End(
		'end', # name
		False, # is_end
		None # game_ending
		)

### gs is the central store of game info ###
gs = GameState(
		'gs', # name
		core, # Core class; fundamental attributes of game state
		map, # Map class; dungeon navigation capabilities
		io, # IO class; all buffering and static dictionary lookup for game
		score, # Score class; all score-related functions of game
		end # End class; end-of-game title and dispaly
		)

# *** Hierarchy-Based Object Re-assignment ***
crown_not_worn_cond.creature_obj = burt
not_in_throne_room_cond.match_room = throne_room
not_in_throne_room_cond.obj = burt
hedgehog_not_in_world_cond.obj = royal_hedgehog
biscuits_in_hedgehog_hand_cond.creature_obj = royal_hedgehog
axe_not_in_goblin_hand_cond.creature_obj = guard_goblin
no_weap_in_hand_cond.creature_obj = burt
goblin_in_world_cond.obj = guard_goblin
sword_not_on_floor.match_room = main_hall
sword_on_floor.match_room = main_hall

entrance_moat_mach.alert_anchor = entrance
broach_dispenser_mach.alert_anchor = throne_room
control_panel.alert_anchor = antechamber
dispense_panel_mach.alert_anchor = antechamber
hedgehog_eats_mach.alert_anchor = royal_hedgehog
hedgehog_guard_mach.alert_anchor = royal_hedgehog
hedgehog_done_eating_mach.alert_anchor = royal_hedgehog
hedgehog_distracted_mach.alert_anchor = royal_hedgehog
goblin_attack_mach.alert_anchor = guard_goblin
re_arm_goblin_mach.alert_anchor = guard_goblin
kinging_scroll.alert_anchor = kinging_scroll

goblin_attacks_result.creature_obj = guard_goblin
hedgehog_attacks_result.creature_obj = royal_hedgehog
start_hedgehog_timer_results.creature_obj = royal_hedgehog
fed_hedgehog_keeps_sword_result.creature_obj = royal_hedgehog
fed_hedgehog_loses_sword_result.creature_obj = royal_hedgehog
axe_in_goblin_hand_result.creature_obj = guard_goblin
dispense_panel_result.room_item = control_panel

hedgehog_eats_timer.alert_anchor = royal_hedgehog
crystal_box.contain_lst = [kinging_scroll]

## test_chair.in_reach_lst = [main_hall, front_gate, wooden_shelf]


### instantiated objects added to list ###
### Used as an obj index in Interp() - must include all non-invisible obj ###
### invisible objects need not be listed ###
master_obj_lst = [gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, dead_goblin, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, random_mcguffin, cheese_wedge, stale_biscuits, well_water, royal_crown, baseball_cap, hedgehog_broach, crystal_box, front_gate, iron_portcullis, control_panel, throne, left_lever, middle_lever, right_lever, red_button, royal_hedgehog, guard_goblin, entrance, main_hall, antechamber, throne_room, loyalty,
officiousness, gold_capitals, red_bandana, big_medal, burt, brass_lantern, fierce_teeth, chewed_fingernails, wooden_shelf, test_chair, screen_door, cardboard_box, small_barrel, red_shoebox, black_suitcase, earthen_jug, heavy_rock] # note: big_bomb & test_frog removed; glass_bottle removed

# list written to pickle
with open(f"{root_path_str}/cleesh/games/dark_castle/game_file/game_pkl", 'wb') as f:
	pickle.dump(master_obj_lst, f)




# *** Test Objects ***

# --- Big Bomb Test ---
## blue_button = ButtonSwitch('blue_button', 'Blue Button', 'button', 'blue_button', None, 'neutral', 'neutral', 'pre_act_auto_switch_reset') # test obj
## test_timer = Timer('test_timer', 'auto_act', False, 0, 3, 'variable', False, blue_button) # test obj
## blue_button_result = StartTimerResult('blue_button_result', test_timer, False) # test obj
## big_bomb = ViewOnlyMach('big_bomb', 'Big Bomb', 'bomb', 'big_bomb', None, # test obj, 0, 'post_act_switch', blue_button, ['pushed'], [], [pass_thru_cond], [blue_button_result])

# --- Test Frog Go Test ---
# frog_in_main_hall_cond = ObjInRmCond('frog_in_main_hall_cond', 'main_hall_temp', 'test_frog_temp', True) # test creature
# frog_in_antechamber_cond = ObjInRmCond('frog_in_antechamber_cond', 'antechamber_temp', 'test_frog_temp', True) # test creature

# frog_goes_north_result = TravelResult('frog_goes_north_result', False, 'test_frog_temp', 'north')
# frog_goes_south_result = TravelResult('frog_goes_north_result', False, 'test_frog_temp', 'south')

# frog_travel_mach = InvisMach('frog_travel_mach', None, 'auto_act', None, None, None,
#				[frog_in_main_hall_cond, frog_in_antechamber_cond], [frog_goes_north_result, frog_goes_south_result])

#test_frog = Creature('test_frog', 'Test Frog', 'frog', 'test_frog', None,
#				None, [], [], [], [],
#				[],
#				{},
#				True,
#				{},
#				{}) # test creature

# frog_in_main_hall_cond.creature = test_frog
# frog_in_main_hall_cond.match_room = main_hall
# frog_in_antechamber_cond.creature = test_frog
# frog_in_antechamber_cond.match_room = antechamber
# frog_goes_north_result.creature = test_frog
# frog_goes_south_result.creature = test_frog


