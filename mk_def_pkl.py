# program: dark castle v3.64
# name: Tom Snellgrove
# date: June 7, 2022
# description: default object instantiation module (used as a tool)


# import statements
import pickle
from noun_class_def import Invisible, Writing, ViewOnly, Item, Food, Beverage, Clothes, Container, Jug, Door, Room
from switch_class_def import ButtonSwitch, SpringSliderSwitch, LeverSwitch
from cond_class_def import (PassThruCond, NotInHandCond, StateCond, InHandAndStateCond,
				SwitchStateCond, LeverArrayCond, RoomCond, CreatureItemCond, NotTimerAndItemCond,
				StateItemInRoomCond, TimerActiveCond, InHandAndRoomCond, InHandAndExistInWorldCond,
				InHandAndGarmentWornCond)
from result_class_def import (BufferOnlyResult, BufferAndEndResult, BufferAndGiveResult,
				AddObjToRoomResult, DoorToggleResult, AttackBurtResult, StartTimerResult,
				TimerAndCreatureItemResult, ChgCreatureDescAndStateResult)
from mach_class_def import InvisMach, ViewOnlyMach, Warning, Timer
from creature_class_def import Creature
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
dead_goblin = ViewOnly('dead_goblin', 'Dead Goblin', 'goblin', 'dead_goblin', None)

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
iron_portcullis = Door('iron_portcullis', 'Iron Portcullis', 'portcullis', 'iron_portcullis', None, False, False, None)

throne = SpringSliderSwitch('throne', 'Throne', 'throne', 'throne', None, 'neutral', 'neutral', 'pre_act_auto_switch_reset')
left_lever = LeverSwitch('left_lever', 'Left Lever', 'lever', 'left_lever', None, 'down', None, None)
middle_lever = LeverSwitch('middle_lever', 'Middle Lever', 'lever', 'middle_lever', None, 'down', None, None)
right_lever = LeverSwitch('right_lever', 'Right Lever', 'lever', 'right_lever', None, 'down', None, None)
red_button = ButtonSwitch('red_button', 'Red Button', 'button', 'red_button', None, 'neutral', 'neutral', 'pre_act_auto_switch_reset')

blue_button = ButtonSwitch('blue_button', 'Blue Button', 'button', 'blue_button', None, 'neutral', 'neutral', 'pre_act_auto_switch_reset') # test obj

test_timer = Timer('test_timer', 'auto_act', False, 0, 3, 'variable', False, blue_button) # test obj
hedgehog_eats_timer = Timer('hedgehog_eats_timer', 'auto_act', False, 0, 4, 'variable', False, 'royal_hedgehog')


hand_no_weap_cond = NotInHandCond('hand_no_weap_cond', [shiny_sword, grimy_axe])
hand_weap_1st_cond = InHandAndStateCond('hand_weap_1st_cond', [shiny_sword, grimy_axe], False)
hand_weap_repeat_cond = InHandAndStateCond('hand_weap_1st_cond', [shiny_sword, grimy_axe], True)
pass_thru_cond = PassThruCond('pass_thru_cond')
broach_dispensed_cond = StateCond('broach_dispensed_cond', True)
throne_push_cond = SwitchStateCond('throne_push_cond', ['pushed'])
throne_pull_cond = SwitchStateCond('throne_pull_cond', ['pulled'])
correct_lever_array_cond = LeverArrayCond('correct_lever_array_cond', [4,2,1])
wrong_lever_array_cond = PassThruCond('wrong_lever_array_cond')
goblin_in_antechamber_cond = RoomCond('goblin_in_antechamber', 'antechamber')
hedgehog_has_biscuit_cond = CreatureItemCond('hedgehog_has_biscuit_cond', 'royal_hedgehog', stale_biscuits)
hedgehog_guard_cond = NotTimerAndItemCond('hedgehog_guard_cond', hedgehog_eats_timer, shiny_sword)
hedgehog_keeps_sword_cond = StateItemInRoomCond('hedgehog_keeps_sword_cond', False, shiny_sword, True)
hedgehog_loses_sword_cond = StateItemInRoomCond('hedgehog_loses_sword_cond', False, shiny_sword, False)
hedgehog_distracted_cond = TimerActiveCond('hedgehog_timer_active_cond', hedgehog_eats_timer, True)
read_scroll_in_throne_room_cond = InHandAndRoomCond('read_scroll_in_throne_room_cond', ['kinging_scroll_temp'], 'throne_room_temp')
read_scroll_hedgehog_exist_cond = InHandAndExistInWorldCond('read_scroll_hedgehog_exist_cond', ['kinging_scroll_temp'], 'royal_hedgehog_temp')
read_scroll_crown_worn_cond = InHandAndGarmentWornCond('read_scroll_crown_worn_cond', ['kinging_scroll_temp'], royal_crown)
read_scroll_win_cond = PassThruCond('read_scroll_win_cond')

die_in_moat_result = BufferAndEndResult('die_in_moat_result', 'death', True)
moat_croc_scared_result = BufferOnlyResult('moat_croc_scared_result', True)
moat_get_crown_result = BufferAndGiveResult('moat_get_crown_result', royal_crown, True)
throne_push_result = BufferOnlyResult('throne_push_result', False)
nothing_happens_result = BufferOnlyResult('nothing_happens_result', False)
throne_pull_result = AddObjToRoomResult('throne_pull_result', hedgehog_broach, False)
toggle_portcullis_result = DoorToggleResult('toggle_portcullis_result', iron_portcullis, False)
portcullis_doesnt_open_result = BufferOnlyResult('portcullis_doesnt_open_result', False)
antechamber_goblin_attacks_result = AttackBurtResult('antechamber_goblin_attacks_result', 'goblin_placeholder', True)
blue_button_result = StartTimerResult('blue_button_result', test_timer, False) # test obj
start_hedgehog_timer_results = TimerAndCreatureItemResult('start_hedgehog_timer_results', hedgehog_eats_timer, False, 'royal_hedgehog', stale_biscuits)
pass_result = BufferOnlyResult('pass_result', False)
hedgehog_guard_result = BufferOnlyResult('hedgehog_guard_result', True)
fed_hedgehog_keeps_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_keeps_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_smug')
fed_hedgehog_loses_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_loses_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_yearn')
hedgehog_distracted_result = BufferOnlyResult('hedgehog_distracted_result', True)
scroll_wrong_room_result = BufferOnlyResult('scroll_wrong_room_result', False)
scroll_no_hedgehog_result = BufferOnlyResult('scroll_no_hedgehog_result', False)
scroll_crown_not_worn_result = BufferOnlyResult('scroll_crown_not_worn_result', False)
scroll_win_game_result = BufferAndEndResult('scroll_win_game_result', 'win', False)


# name, timer_obj, cmd_override, creature_obj, ceature_item_obj

entrance_south_warn = Warning('entrance_south_warn', 'pre_act_cmd', [['go', 'south']], 0, 0)

attack_hedgehog_warning = Warning('attack_hedgehog_warning', 'pre_act_cmd', [['attack', 'royal_hedgehog']], 3, 0)


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

# name, mach_state, trigger_type, trig_switch, trig_vals_lst, cond_swicth_lst, cond_lst, result_lst

big_bomb = ViewOnlyMach('big_bomb', 'Big Bomb', 'bomb', 'big_bomb', None, # test obj
				0, 'post_act_switch', blue_button, ['pushed'], [],
				[pass_thru_cond], [blue_button_result])

hedgehog_done_eating_mach = InvisMach('hedgehog_done_eating_mach', 0, 'pre_act_timer', hedgehog_eats_timer, [True], None,
				[hedgehog_keeps_sword_cond, hedgehog_loses_sword_cond, pass_thru_cond],
				[fed_hedgehog_keeps_sword_result, fed_hedgehog_loses_sword_result, pass_result]) # machine_state == post-eating description updated?

goblin_attack_mach = InvisMach('goblin_attack_mach', None, 'pre_act_cmd', None,
				[['examine', 'iron_portcullis'], ['examine', 'control_panel'], ['examine', 'grimy_axe'], ['open', 'iron_portcullis'], ['go', 'north']],
				None, [goblin_in_antechamber_cond, pass_thru_cond], [antechamber_goblin_attacks_result, nothing_happens_result])

hedgehog_distracted_mach = InvisMach('hedgehog_distracted_mach', None, 'pre_act_cmd', None,
				[['give', '*', 'royal_hedgehog'], ['show', '*', 'royal_hedgehog']], None, 
				[hedgehog_distracted_cond, pass_thru_cond], [hedgehog_distracted_result, pass_result])

goblin_guard = Creature('guard_goblin', 'Guard Goblin', 'goblin', 'guard_goblin', None, None, [goblin_attack_mach],
				{
						shiny_sword : 'show_goblin_shiny_sword',
						stale_biscuits : 'show_goblin_stale_bisuits',
						'def_show' : 'show_goblin_default'
				}, 
				{
						shiny_sword : {'response_key' : 'give_goblin_shiny_sword', 'accept_item' : False, 'give_item' : None, 'new_descript_key' : None},
						stale_biscuits : {'response_key' : 'give_goblin_stale_biscuits', 'accept_item' : False, 'give_item' : None, 'new_descript_key' : None},
						'def_give' : {'response_key' : 'give_goblin_default', 'accept_item' : True, 'give_item' : None, 'new_descript_key' : None}
				},
				{
						shiny_sword : {'result_code' : 'creature_death', 'response_key' : 'goblin_slain'},
						'def_attack' : {'result_code' : 'burt_death', 'response_key' : 'burt_slain_by_goblin'}
				},
				{
						shiny_sword : {'result_code' : None, 'response_key' : 'parry_goblin'},
						'def_attack' : {'result_code' : 'burt_death', 'response_key' : 'goblin_slays_burt'}
				},
				[grimy_axe, torn_note], dead_goblin)

# name, full_name, root_name, descript_key, writing, creature_state, mach_obj_lst, show_item_dict, give_item_dict,
#		attack_creature_dict, attack_burt_dict, creature_items_lst, dead_creature_obj

royal_hedgehog = Creature('royal_hedgehog', 'Royal Hedgehog', 'hedgehog', 'hungry_hedgehog', None, None,
				[attack_hedgehog_warning, hedgehog_eats_mach, hedgehog_guard_mach, hedgehog_done_eating_mach, hedgehog_distracted_mach],
				{
						shiny_sword : 'show_hedgehog_shiny_sword',
						stale_biscuits : 'show_hedgehog_stale_biscuits'
				},
				{
						shiny_sword : {'response_key' : 'give_hedgehog_sword', 'accept_item' : True, 'give_item' : silver_key, 'new_descript_key' : 'hedgehog_sword_returned'},
						stale_biscuits : {'response_key' : 'give_hedgehog_biscuits', 'accept_item' : True, 'give_item' : None, 'new_descript_key' : 'hedgehog_eating'}
				},
				{
#						shiny_sword : {'result_code' : 'creature_flee', 'response_key' : 'hedgehog_flees'},
#						'def_attack' : {'result_code' : None, 'response_key' : 'hedgehog_dodges'}
						'def_attack' : {'result_code' : 'creature_flee', 'response_key' : 'hedgehog_flees'}
				},
				{},
				[silver_key], None)


entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, [dark_castle, moat, blue_button],
				[front_gate, big_bomb], {'north' : front_gate}, [entrance_moat_mach, entrance_south_warn])
main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
				[shiny_sword, front_gate, royal_hedgehog], {'south' : front_gate}, [])
antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
				[alcove, left_lever, middle_lever, right_lever, red_button], [iron_portcullis, control_panel, goblin_guard],
				{'north' : iron_portcullis}, [])
throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
				[throne, crystal_box, iron_portcullis], {'south' : iron_portcullis}, [broach_dispenser_mach])

# hedgehog_eats_timer = Timer('hedgehog_eats_timer', 'auto_act', False, 0, 4, 'variable', False, royal_hedgehog)


# *** 'object not defined' re-assignment ***
antechamber_goblin_attacks_result.creature_obj = goblin_guard
hedgehog_has_biscuit_cond.creature_obj = royal_hedgehog
hedgehog_eats_timer.alert_anchor = royal_hedgehog
start_hedgehog_timer_results.creature_obj = royal_hedgehog
fed_hedgehog_keeps_sword_result.creature_obj = royal_hedgehog
fed_hedgehog_loses_sword_result.creature_obj = royal_hedgehog
read_scroll_in_throne_room_cond.in_hand_lst = [kinging_scroll]
read_scroll_in_throne_room_cond.match_room_name = throne_room
read_scroll_hedgehog_exist_cond.in_hand_lst = [kinging_scroll]
read_scroll_hedgehog_exist_cond.exist_obj = royal_hedgehog
read_scroll_crown_worn_cond.in_hand_lst = [kinging_scroll]

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
				'hedgehog_broach' : False,
				'hedgehog_attack' : False
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
		},
		[test_timer, hedgehog_eats_timer],
		[entrance, main_hall, antechamber, throne_room]
)

### instantiated objects added to list ###
### Used as an obj index in Interp() - must include all non-invisible obj ###
### invisible obj referenced in room.invis_obj_lst need not be listed ###
master_obj_lst = [active_gs, rusty_lettering, dwarven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, trademark, dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, dead_goblin, rusty_key, shiny_sword, brass_key, bubbly_potion, torn_note, grimy_axe, silver_key, kinging_scroll, random_mcguffin, cheese_wedge, stale_biscuits, fresh_water, royal_crown, baseball_cap, hedgehog_broach, wooden_chest, crystal_box, glass_bottle, front_gate, iron_portcullis, control_panel, throne, left_lever, middle_lever, right_lever, red_button, blue_button, big_bomb, royal_hedgehog, goblin_guard, entrance, main_hall, antechamber, throne_room]

# list written to pickle
with open('default_obj_pickle', 'wb') as f:
		pickle.dump(master_obj_lst, f)

