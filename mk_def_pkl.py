# program: dark castle v3.74
# name: Tom Snellgrove
# date: Nov 5, 2022
# description: default object instantiation module (used as a tool)


# import statements
import pickle
from base_class_def import Invisible, Writing, ViewOnly
from room_class_def import Room
from item_class_def import Item, Food, Garment, Weapon
from door_class_def import Door, Container, PortableContainer, PortableLiquidContainer
from switch_class_def import ButtonSwitch, SpringSliderSwitch, LeverSwitch
from misc_class_def import Liquid
from cond_class_def import (PassThruCond, StateCond, WeaponInHandCond,
				SwitchStateCond, LeverArrayCond, CreatureItemCond, NotTimerAndItemCond,
				StateItemInRoomCond, TimerActiveCond, RoomCond, InWorldCond, WornCond, IsWeaponAndStateCond, InRoomCond)
from result_class_def import (BufferOnlyResult, BufferAndEndResult, BufferAndGiveResult,
				AddObjToRoomResult, DoorToggleResult, AttackBurtResult, StartTimerResult,
				TimerAndCreatureItemResult, ChgCreatureDescAndStateResult, PutItemInHandResult, TravelResult)
from mach_class_def import InvisMach, ViewOnlyMach, ItemMach, Warning, Timer
from creature_class_def import Creature
from gs_class_def import GameState
from map_class_def import Map

# object instantiation - starting state
rusty_lettering = Writing('rusty_lettering', 'Rusty Lettering', "lettering", 'rusty_lettering')
dwarven_runes = Writing('dwarven_runes', 'Dwarven Runes', "runes", 'dwarven_runes')
messy_handwriting = Writing('messy_handwriting', 'Messy Handwriting', 'handwriting', 'messy_handwriting')
small_printing = Writing('small_printing', 'Small Printing', 'printing', 'small_printing')
illuminated_letters = Writing('illuminated_letters', 'Illuminated Letters', 'letters', 'illuminated_letters')
calligraphy = Writing('calligraphy', 'Calligraphy', 'calligraphy', 'calligraphy')
trademark = Writing('trademark', 'Trademark', 'trademark', 'trademark')
gold_capitals = Writing('gold_capitals', 'Gold Capitals', 'capitals', 'gold_capitals')

dark_castle = ViewOnly('dark_castle', "Dark Castle", "castle", 'dark_castle', None)
moat = ViewOnly('moat', 'Moat', 'moat', 'moat', None)
backpack = ViewOnly('backpack', "Backpack", "backpack", 'backpack', None)
burt = ViewOnly('burt', 'Burt', "burt", 'burt', None)
fist = ViewOnly('fist', 'Fist', "fist", 'fist', None)
brass_lantern = ViewOnly('brass_lantern', 'Brass Lantern', "lantern", 'brass_lantern', None)
conscience = ViewOnly('conscience', 'Conscience', 'conscience', 'conscience', None)
faded_tapestries = ViewOnly('faded_tapestries', 'Faded Tapestries', 'tapestries', 'faded_tapestries', None)
alcove = ViewOnly('alcove', 'Alcove', 'alcove', 'alcove', None)
stone_coffer = ViewOnly('stone_coffer', 'Stone Coffer', 'coffer', 'stone_coffer', None)
family_tree = ViewOnly('family_tree', 'Family Tree', 'tree', 'family_tree', None)
dead_goblin = ViewOnly('dead_goblin', 'Dead Goblin', 'goblin', 'dead_goblin', None)
officiousness = ViewOnly('officiousness', 'Officiousness', 'officiousness', 'officiousness', None)
loyalty = ViewOnly('loyalty', 'Loyalty', 'loyalty', 'loyalty', None)

rusty_key = Item('rusty_key', 'Rusty Key', "key", 'rusty_key', None)
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None) # test object
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'bubbly_potion', None) # test object
torn_note = Item('torn_note', 'Torn Note', 'note', 'torn_note', messy_handwriting)
silver_key = Item('silver_key', 'Silver Key', 'key', 'silver_key', None)
random_mcguffin = Item('random_mcguffin', 'Random McGuffin', 'mcguffin', 'random_mcguffin', None)

cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None)
stale_biscuits = Food('stale_biscuits', 'Stale Biscuits', 'biscuits', 'stale_biscuits', trademark)

fresh_water = Liquid('fresh_water', 'Fresh Water', 'water', 'fresh_water', None)

royal_crown = Garment('royal_crown', 'Royal Crown', 'crown', 'royal_crown', None, 'hat')
baseball_cap = Garment('baseball_cap', 'Baseball Cap', 'cap', 'baseball_cap', None, 'hat')
hedgehog_broach = Garment('hedgehog_broach', 'Hedgehog Broach', 'broach', 'hedgehog_broach', None, 'pin')
red_bandana = Garment('red_bandana', 'Red Bandana', 'bandana', 'red_bandana', None, 'hat')
big_medal = Garment('big_medal', 'Big Medal', 'medal', 'big_medal', gold_capitals, 'pin')

grimy_axe = Weapon('grimy_axe', 'Grimy Axe', 'axe', 'grimy_axe', small_printing,
				[['arcs', 'lightening-fast stroke'],['cleaves', 'violent swing'],['hacks', 'deadly intent']])
shiny_sword = Weapon('shiny_sword', 'Shiny Sword', 'sword', 'shiny_sword', dwarven_runes,
				[['swings', 'blazing-fast assault'],['stabs', 'cunning unterhau']])

crystal_box = Container('crystal_box', 'Crystal Box', 'box', 'crystal_box', calligraphy,
				False, False, silver_key, ['kinging_scroll_temp'])

glass_bottle = PortableLiquidContainer('glass_bottle', 'Glass Bottle', 'bottle', 'glass_bottle', None, None, None, None, [fresh_water])

front_gate = Door('front_gate', 'Front Gate', "gate", 'front_gate', rusty_lettering, False, False, rusty_key)
iron_portcullis = Door('iron_portcullis', 'Iron Portcullis', 'portcullis', 'iron_portcullis', None, False, False, None)

throne = SpringSliderSwitch('throne', 'Throne', 'throne', 'throne', None, 'neutral', 'neutral', 'auto_switch_reset')
left_lever = LeverSwitch('left_lever', 'Left Lever', 'lever', 'left_lever', None, 'down', None, None)
middle_lever = LeverSwitch('middle_lever', 'Middle Lever', 'lever', 'middle_lever', None, 'down', None, None)
right_lever = LeverSwitch('right_lever', 'Right Lever', 'lever', 'right_lever', None, 'down', None, None)
red_button = ButtonSwitch('red_button', 'Red Button', 'button', 'red_button', None, 'neutral', 'neutral', 'auto_switch_reset')

hedgehog_eats_timer = Timer('hedgehog_eats_timer', 'auto_act', False, 0, 4, 'variable', False, 'royal_hedgehog')

hand_no_weap_cond = WeaponInHandCond('hand_no_weap_cond', False)
hand_weap_1st_cond = IsWeaponAndStateCond('hand_weap_1st_cond', True, False)
hand_weap_repeat_cond = IsWeaponAndStateCond('hand_weap_repeat_cond', True, True)
pass_thru_cond = PassThruCond('pass_thru_cond')
broach_dispensed_cond = StateCond('broach_dispensed_cond', True)
throne_push_cond = SwitchStateCond('throne_push_cond', ['pushed'])
throne_pull_cond = SwitchStateCond('throne_pull_cond', ['pulled'])
correct_lever_array_cond = LeverArrayCond('correct_lever_array_cond', [4,2,1])
wrong_lever_array_cond = PassThruCond('wrong_lever_array_cond')
hedgehog_has_biscuit_cond = CreatureItemCond('hedgehog_has_biscuit_cond', 'royal_hedgehog_temp', stale_biscuits, True)
hedgehog_guard_cond = NotTimerAndItemCond('hedgehog_guard_cond', hedgehog_eats_timer, shiny_sword)
hedgehog_keeps_sword_cond = StateItemInRoomCond('hedgehog_keeps_sword_cond', False, shiny_sword, True)
hedgehog_loses_sword_cond = StateItemInRoomCond('hedgehog_loses_sword_cond', False, shiny_sword, False)
hedgehog_distracted_cond = TimerActiveCond('hedgehog_timer_active_cond', hedgehog_eats_timer, True)
scroll_not_in_throne_room_cond = RoomCond('scroll_not_in_throne_room_cond', 'throne_room_temp', False)
hedgehog_not_exist_cond = InWorldCond('hedgehog_not_exist_cond', 'royal_hedgehog_temp', False)
crown_not_worn_cond = WornCond('crown_not_worn_cond', royal_crown, False)
read_scroll_win_cond = PassThruCond('read_scroll_win_cond')
axe_in_goblin_hand_cond = CreatureItemCond('axe_in_goblin_hand_cond', 'guard_goblin_temp', grimy_axe, False)

die_in_moat_result = BufferAndEndResult('die_in_moat_result', 'death', True)
moat_croc_scared_result = BufferOnlyResult('moat_croc_scared_result', True)
moat_get_crown_result = BufferAndGiveResult('moat_get_crown_result', royal_crown, True)
throne_push_result = BufferOnlyResult('throne_push_result', False)
nothing_happens_result = BufferOnlyResult('nothing_happens_result', False)
throne_pull_result = AddObjToRoomResult('throne_pull_result', hedgehog_broach, False)
toggle_portcullis_result = DoorToggleResult('toggle_portcullis_result', iron_portcullis, False)
portcullis_doesnt_open_result = BufferOnlyResult('portcullis_doesnt_open_result', False)
goblin_attacks_result = AttackBurtResult('goblin_attacks_result', 'guard_goblin_temp', True)
start_hedgehog_timer_results = TimerAndCreatureItemResult('start_hedgehog_timer_results', hedgehog_eats_timer, False, 'royal_hedgehog', stale_biscuits)
pass_result = BufferOnlyResult('pass_result', False)
hedgehog_guard_result = BufferOnlyResult('hedgehog_guard_result', True)
fed_hedgehog_keeps_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_keeps_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_smug')
fed_hedgehog_loses_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_loses_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_yearn')
hedgehog_distracted_result = BufferOnlyResult('hedgehog_distracted_result', True)
scroll_wrong_room_result = BufferOnlyResult('scroll_wrong_room_result', False)
scroll_no_hedgehog_result = BufferOnlyResult('scroll_no_hedgehog_result', False)
scroll_crown_not_worn_result = BufferOnlyResult('scroll_crown_not_worn_result', False)
scroll_win_game_result = BufferAndEndResult('scroll_win_game_result', 'won', False)
axe_in_goblin_hand_result = PutItemInHandResult('axe_in_goblin_hand_result', False, 'guard_goblin_temp', grimy_axe)

entrance_south_warn = Warning('entrance_south_warn', 'pre_act_cmd', [['go', 'south']], 0, 0)
attack_hedgehog_warning = Warning('attack_hedgehog_warning', 'pre_act_cmd', [['attack', 'royal_hedgehog']], 3, 0)
eat_biscuits_warning = Warning('eat_biscuits_warning', 'pre_act_cmd', [['eat','stale_biscuits']], 3, 0)

entrance_moat_mach = InvisMach('entrance_moat_mach', False, 'pre_act_cmd', None, [['go', 'east'], ['go', 'west']],
				None, [hand_no_weap_cond, hand_weap_1st_cond, hand_weap_repeat_cond],
				[die_in_moat_result, moat_get_crown_result, moat_croc_scared_result]) # machine_state == got_crown

broach_dispenser_mach = InvisMach('broach_dispenser_mach', False, 'post_act_switch', throne, ['pushed', 'pulled'],
				[throne], [broach_dispensed_cond, throne_push_cond, throne_pull_cond],
				[nothing_happens_result, throne_push_result, throne_pull_result]) # machine_state == broach_dispensed

control_panel = ViewOnlyMach('control_panel', 'Control Panel', 'panel', 'control_panel', None,
				0, 'post_act_switch', red_button, ['pushed'], [left_lever, middle_lever, right_lever],
				[correct_lever_array_cond, wrong_lever_array_cond], [toggle_portcullis_result, portcullis_doesnt_open_result])
				# machine_state == lever_array_value

hedgehog_eats_mach = InvisMach('hedgehog_eats_mach', None, 'post_act_cmd', None, [['give', 'stale_biscuits', 'royal_hedgehog']],
				None, [hedgehog_has_biscuit_cond, pass_thru_cond], [start_hedgehog_timer_results, pass_result])

hedgehog_guard_mach = InvisMach('hedgehog_guard_mach', None, 'pre_act_cmd', None, [['take', 'shiny_sword']],
				None, [hedgehog_guard_cond, pass_thru_cond], [hedgehog_guard_result, pass_result])

hedgehog_done_eating_mach = InvisMach('hedgehog_done_eating_mach', 0, 'pre_act_timer', hedgehog_eats_timer, [True], None,
				[hedgehog_keeps_sword_cond, hedgehog_loses_sword_cond, pass_thru_cond],
				[fed_hedgehog_keeps_sword_result, fed_hedgehog_loses_sword_result, pass_result]) # machine_state == post-eating description updated?

goblin_attack_mach = InvisMach('goblin_attack_mach', None, 'pre_act_cmd', None,
				[['examine', 'iron_portcullis'], ['examine', 'control_panel'], ['examine', 'grimy_axe'], ['take', 'grimy_axe'],
				['open', 'iron_portcullis'], ['go', 'north']],
				None, [pass_thru_cond], [goblin_attacks_result])

hedgehog_distracted_mach = InvisMach('hedgehog_distracted_mach', None, 'pre_act_cmd', None,
				[['give', '*', 'royal_hedgehog'], ['show', '*', 'royal_hedgehog']], None, 
				[hedgehog_distracted_cond, pass_thru_cond], [hedgehog_distracted_result, pass_result])

kinging_scroll = ItemMach('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', illuminated_letters,
				None, 'post_act_cmd', None, [['read', 'illuminated_letters']], None,
				[scroll_not_in_throne_room_cond, hedgehog_not_exist_cond, crown_not_worn_cond, read_scroll_win_cond],
				[scroll_wrong_room_result, scroll_no_hedgehog_result, scroll_crown_not_worn_result, scroll_win_game_result])

re_arm_goblin_mach = InvisMach('re_arm_goblin_mach', None, 'auto_act', None, None, None,
				[axe_in_goblin_hand_cond, pass_thru_cond], [axe_in_goblin_hand_result, pass_result])

guard_goblin = Creature('guard_goblin', 'Guard Goblin', 'goblin', 'guard_goblin', None,
				None, [grimy_axe], [torn_note, dead_goblin], [big_medal], [officiousness],
				[goblin_attack_mach, re_arm_goblin_mach],
				{
						shiny_sword : {'accept' : False, 'give' : None},
						stale_biscuits : {'accept' : False, 'give' : None},
						'def_give' : {'accept' : True, 'give' : None}
				},
				True,
				{
						shiny_sword : {'result_code' : 'creature_death', 'custom_key' : 'goblin_slain', 'resolution_key' : None},
						'def_attack' : {'result_code' : 'burt_death', 'custom_key' : 'burt_slain_by_goblin', 'resolution_key' : None},
						'shiny_sword_burt_*' : 'tgt_death',
						'weapon_*_*' : None, # parry
						'*_*_*' : 'src_death'
				},
				{
						shiny_sword : {'result_code' : None, 'custom_key' : None, 'resolution_key' : None}, # was 'custom_key' : 'parry_goblin'
						'def_attack' : {'result_code' : 'burt_death', 'custom_key' : None, 'resolution_key' : None} # was 'custom_key' : 'goblin_slays_burt'
				})
				
royal_hedgehog = Creature('royal_hedgehog', 'Royal Hedgehog', 'hedgehog', 'hungry_hedgehog', None,
				None, [], [silver_key], [red_bandana], [loyalty],
				[attack_hedgehog_warning, hedgehog_eats_mach, hedgehog_guard_mach, hedgehog_done_eating_mach, hedgehog_distracted_mach],
				{
						shiny_sword : {'accept' : True, 'give' : silver_key},
						stale_biscuits : {'accept' : True, 'give' : None}
				},
				True,
				{
						'def_attack' : {'result_code' : 'creature_flee', 'custom_key' : 'hedgehog_flees', 'resolution_key' : None},
						'weapon_burt_*' : 'tgt_flee_dc',
						'unarmed_burt_*' : None, # karate kid
						'*_*_*' : None # dodge
				},
				{})

burt = Creature('burt', 'Burt', 'burt', 'burt', None,
				None, [], [rusty_key, glass_bottle, cheese_wedge, stale_biscuits], [], [fist, backpack, conscience, brass_lantern],
				[hedgehog_eats_timer],
				{},
				True,
				{
						shiny_sword : {'result_code' : None, 'custom_key' : None, 'resolution_key' : None}, # was 'custom_key' : 'parry_goblin'
						'def_attack' : {'result_code' : 'burt_death', 'custom_key' : None, 'resolution_key' : None}, # was 'custom_key' : 'goblin_slays_burt'
						'grimy_axe_guard_goblin_weapon' : None, # parry
						'grimy_axe_guard_gobin_*' : 'tgt_death'
				},
				{}) # note: for non-burt-creature testing, frog_travel_mach was in burt.invis_lst

# *** Rooms ***
entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, [dark_castle, moat],
				[burt], [entrance_moat_mach, entrance_south_warn, eat_biscuits_warning])
				# note: for timer testing, big_bomb was in entrance.floor_lst and blue_button was in entrance.feature_lst

main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
				[shiny_sword, royal_hedgehog], [eat_biscuits_warning])
				# note: for non-burt-creature testing, test_frog was in main_hall.floor_lst

antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
				[alcove, left_lever, middle_lever, right_lever, red_button], [control_panel, guard_goblin], [])

throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
				[throne, crystal_box], [broach_dispenser_mach])

unreachable_1 = Room('unreachable_1', 'Unreachable', 'unreachable_1', 'unreachable_1', None, [], [], [])

unreachable_2 = Room('unreachable_2', 'Unreachable', 'unreachable_2', 'unreachable_2', None, [], [], [])

unreachable_3 = Room('unreachable_3', 'Unreachable', 'unreachable_3', 'unreachable_3', None, [], [], [])

# *** Map ***
map = Map([{'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall},
				{'room_x' : entrance, 'dir_x' : 'south', 'door' : 'path', 'dir_y' : None, 'room_y' : unreachable_1},
				{'room_x' : entrance, 'dir_x' : 'east', 'door' : 'leap down to the moat', 'dir_y' : None, 'room_y' : unreachable_2},
				{'room_x' : entrance, 'dir_x' : 'west', 'door' : 'leap down to the moat', 'dir_y' : None, 'room_y' : unreachable_3},
				{'room_x' : main_hall, 'dir_x' : 'north', 'door' : 'passage', 'dir_y' : 'south', 'room_y' : antechamber},
				{'room_x' : antechamber, 'dir_x' : 'north', 'door' : iron_portcullis, 'dir_y' : 'south', 'room_y' : throne_room}])

# *** Hierarchy-Based Object Re-assignment ***
goblin_attacks_result.creature_obj = guard_goblin
hedgehog_has_biscuit_cond.creature_obj = royal_hedgehog
hedgehog_eats_timer.alert_anchor = royal_hedgehog
start_hedgehog_timer_results.creature_obj = royal_hedgehog
fed_hedgehog_keeps_sword_result.creature_obj = royal_hedgehog
fed_hedgehog_loses_sword_result.creature_obj = royal_hedgehog
scroll_not_in_throne_room_cond.match_room = throne_room
hedgehog_not_exist_cond.exist_obj = royal_hedgehog
crystal_box.contain_lst = [kinging_scroll]
axe_in_goblin_hand_cond.creature_obj = guard_goblin
axe_in_goblin_hand_result.creature_obj = guard_goblin

### active_gs is the central store of game info ###
active_gs = GameState(
		'active_gs',
		{}, # dyn_descript_dict
		{
				'rusty_key' : False,
				'main_hall' : False,
				'shiny_sword' : False,
				'throne_room' : False,
				'silver_key' : False,
				'kinging_scroll' : False,
				'royal_crown' : False,
				'hedgehog_broach' : False,
				'hedgehog_attack' : False,
				'goblin_dead' : False
		},
		{
				'score' : 0,
				'move_counter' : 0,
				'end_of_game' : False,
				'game_ending' : "tbd",
##				'room' : entrance,
				'out_buff' : ""
		},
		map,
		burt
)

### instantiated objects added to list ###
### Used as an obj index in Interp() - must include all non-invisible obj ###
### invisible objects need not be listed ###
master_obj_lst = [active_gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, dead_goblin, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, random_mcguffin, cheese_wedge, stale_biscuits, fresh_water, royal_crown, baseball_cap, hedgehog_broach, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, left_lever, middle_lever, right_lever, red_button, royal_hedgehog, guard_goblin, entrance, main_hall, antechamber, throne_room, loyalty,
officiousness, gold_capitals, red_bandana, big_medal, burt, brass_lantern] # note: big_bomb & test_frog removed

# list written to pickle
with open('default_obj_pickle', 'wb') as f:
		pickle.dump(master_obj_lst, f)

# *** Test Objects ***

# --- Legacy Classes 
# kinging_scroll = Item('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', illuminated_letters) # old scroll
# glass_bottle = Jug('glass_bottle', 'Glass Bottle', 'bottle', 'glass_bottle', None, True, [fresh_water]) # legacy glass_bottle

# --- Never Used ---
## giftbox = Container('giftbox', 'A pretty gift box', None, False, True, 'none', True, [necklace])
## screen_door = Door('screen_door', "You should never be able to examine the screen_door", None, False, False, chrome_key)

# --- Small Tests ---
## wooden_chest = Container('wooden_chest', 'wooden chest', "chest", 'wooden_chest', None, False, False, brass_key, [bubbly_potion]) # test object
# black_suitcase = PortableContainer('black_suitcase', 'Black Suitcase', 'suitcase', 'black_suitcase', None, False, False, rusty_key, [cheese_wedge])

# --- Big Bomb Test ---
## blue_button = ButtonSwitch('blue_button', 'Blue Button', 'button', 'blue_button', None, 'neutral', 'neutral', 'pre_act_auto_switch_reset') # test obj
## test_timer = Timer('test_timer', 'auto_act', False, 0, 3, 'variable', False, blue_button) # test obj
## blue_button_result = StartTimerResult('blue_button_result', test_timer, False) # test obj
## big_bomb = ViewOnlyMach('big_bomb', 'Big Bomb', 'bomb', 'big_bomb', None, # test obj, 0, 'post_act_switch', blue_button, ['pushed'], [], [pass_thru_cond], [blue_button_result])

# --- Test Frog Go Test ---
# frog_in_main_hall_cond = InRoomCond('frog_in_main_hall_cond', 'test_frog_temp', 'main_hall_temp', True) # test creature
# frog_in_antechamber_cond = InRoomCond('frog_in_antechamber_cond', 'test_frog_temp', 'antechamber_temp', True) # test creature

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


