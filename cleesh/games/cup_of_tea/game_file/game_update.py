# program: cup_of_tea v0.10
# name: Tom Snellgrove
# date: May 9, 2024
# description: default object instantiation module (used as a tool)


# import statements
import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')

import pickle
from cleesh.class_std.invisible_class_def import Invisible
from cleesh.class_std.base_class_def import Writing, ViewOnly
from cleesh.class_std.room_class_def import Room
from cleesh.class_std.item_class_def import Item, Food, Liquid, Garment, Weapon
from cleesh.class_std.interactive_class_def import DoorSimple, DoorLockable
from cleesh.class_std.interactive_class_def import ContainerFixedSimple, ContainerFixedLidded, ContainerFixedLockable, Seat
from cleesh.class_std.interactive_class_def import ContainerPortableSimple, ContainerPortableLidded, ContainerPortableLockable
from cleesh.class_mach.switch_class_def import LeverSwitch, ViewOnlyButtonSwitch, SeatSpringSliderSwitch
from cleesh.class_mach.cond_class_def import (PassThruCond, StateCond, WeaponInHandCond,
		SwitchStateCond, LeverArrayCond, CreatureItemCond, NotTimerAndItemCond,
		StateItemInRoomCond, TimerActiveCond, RoomCond, InWorldCond, WornCond, IsWeaponAndStateCond, InRoomCond, InWorldStateCond)
from cleesh.class_mach.result_class_def import (BufferOnlyResult, BufferAndEndResult, BufferAndGiveResult,
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
calligraphy = Writing('calligraphy', 'Calligraphy', 'calligraphy', 'calligraphy')

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

# Food
# cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None, 1)


# Liquid
tea = Liquid('tea', 'Tea', 'tea', 'tea', None, 0.5)

# Garment
# royal_crown = Garment('royal_crown', 'Royal Crown', 'crown', 'royal_crown', None, 5, 'hat')
# hedgehog_broach = Garment('hedgehog_broach', 'Hedgehog Broach', 'broach', 'hedgehog_broach', None, 1, 'pin')

# Weapon
# shiny_sword = Weapon('shiny_sword', 'Shiny Sword', 'sword', 'shiny_sword', dwarven_runes, 10, 
#				[['swings', 'blazing-fast assault'],['stabs', 'cunning unterhau']])

# Container
wooden_shelf = ContainerFixedSimple('wooden_shelf', 'Wooden Shelf', 'shelf', 'wooden_shelf', None, [], 999, 20, 'on')
tea_cup = ContainerPortableSimple('tea_cup', 'Tea Cup', 'cup', 'tea_cup', calligraphy, 1.5, [tea], 0.5, 5, 'in')

# Door
front_gate = DoorLockable('front_gate', 'Front Gate', "gate", 'front_gate', calligraphy, False, False, rusty_key)

# Switches
# left_lever = LeverSwitch('left_lever', 'Left Lever', 'lever', 'left_lever', None, 'down', None, None)
# red_button = ViewOnlyButtonSwitch('red_button', 'Red Button', 'button', 'red_button', None, 'neutral', 'neutral', 'auto_switch_reset')
# throne = SeatSpringSliderSwitch('throne', 'Throne', 'throne', 'throne_pre_broach', None, [], 999, 2, 'on', [crystal_box], 'neutral', 'neutral', 'auto_switch_reset')

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
hedgehog_eats_timer = Timer('hedgehog_eats_timer', 'auto_act', False, 0, 4, 'variable', False, 'royal_hedgehog')

# conditions
hand_no_weap_cond = WeaponInHandCond('hand_no_weap_cond', False)
hand_weap_1st_cond = IsWeaponAndStateCond('hand_weap_1st_cond', True, False)
hand_weap_repeat_cond = IsWeaponAndStateCond('hand_weap_repeat_cond', True, True)
pass_thru_cond = PassThruCond('pass_thru_cond')
broach_dispensed_cond = StateCond('broach_dispensed_cond', True)
throne_push_cond = SwitchStateCond('throne_push_cond', ['pushed'])
throne_pull_cond = SwitchStateCond('throne_pull_cond', ['pulled'])
correct_lever_array_cond = LeverArrayCond('correct_lever_array_cond', [4,2,1])
wrong_lever_array_cond = PassThruCond('wrong_lever_array_cond')
# hedgehog_has_biscuit_cond = CreatureItemCond('hedgehog_has_biscuit_cond', 'royal_hedgehog_temp', stale_biscuits, True)
# hedgehog_guard_cond = NotTimerAndItemCond('hedgehog_guard_cond', hedgehog_eats_timer, shiny_sword)
# hedgehog_keeps_sword_cond = StateItemInRoomCond('hedgehog_keeps_sword_cond', False, shiny_sword, True)
# hedgehog_loses_sword_cond = StateItemInRoomCond('hedgehog_loses_sword_cond', False, shiny_sword, False)
hedgehog_distracted_cond = TimerActiveCond('hedgehog_timer_active_cond', hedgehog_eats_timer, True)
scroll_not_in_throne_room_cond = RoomCond('scroll_not_in_throne_room_cond', 'throne_room_temp', False)
hedgehog_not_exist_cond = InWorldCond('hedgehog_not_exist_cond', 'royal_hedgehog_temp', False)
# crown_not_worn_cond = WornCond('crown_not_worn_cond', royal_crown, False)
read_scroll_win_cond = PassThruCond('read_scroll_win_cond')
# axe_in_goblin_hand_cond = CreatureItemCond('axe_in_goblin_hand_cond', 'guard_goblin_temp', grimy_axe, False)
goblin_exist_state_cond = InWorldStateCond('goblin_dead_state_cond', 'guard_goblin_temp', False)

# results
die_in_moat_result = BufferAndEndResult('die_in_moat_result', 'died.', True)
moat_croc_scared_result = BufferOnlyResult('moat_croc_scared_result', True)
# moat_get_crown_result = BufferAndGiveResult('moat_get_crown_result', royal_crown, True)
throne_push_result = BufferOnlyResult('throne_push_result', False)
nothing_happens_result = BufferOnlyResult('nothing_happens_result', False)
# throne_pull_result = AddObjChgDescriptResult('throne_pull_result', hedgehog_broach, throne, 'throne_post_broach', False)
# toggle_portcullis_result = DoorToggleResult('toggle_portcullis_result', iron_portcullis, False)
portcullis_doesnt_open_result = BufferOnlyResult('portcullis_doesnt_open_result', False)
goblin_attacks_result = AttackBurtResult('goblin_attacks_result', 'guard_goblin_temp', True)
hedgehog_attacks_result = AttackBurtResult('hedgehog_attacks_result', 'royal_hedgehog_temp', True)
start_hedgehog_timer_results = TimerAndCreatureItemResult('start_hedgehog_timer_results', hedgehog_eats_timer, False, 'royal_hedgehog', stale_biscuits)
pass_result = BufferOnlyResult('pass_result', False)
fed_hedgehog_keeps_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_keeps_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_smug')
fed_hedgehog_loses_sword_result = ChgCreatureDescAndStateResult('fed_hedgehog_loses_sword_result', False, 'royal_hedgehog_temp', 'hedgehog_desc_yearn')
hedgehog_distracted_result = BufferOnlyResult('hedgehog_distracted_result', True)
scroll_wrong_room_result = BufferOnlyResult('scroll_wrong_room_result', False)
scroll_no_hedgehog_result = BufferOnlyResult('scroll_no_hedgehog_result', False)
scroll_crown_not_worn_result = BufferOnlyResult('scroll_crown_not_worn_result', False)
scroll_win_game_result = BufferAndEndResult('scroll_win_game_result', 'won!', False)
axe_in_goblin_hand_result = PutItemInHandResult('axe_in_goblin_hand_result', False, 'guard_goblin_temp', grimy_axe)
dispense_panel_result = AddObjToRoomAndDescriptResult('dispense_panel_result', 'temp_control_panel', False)



# warnings
entrance_south_warn = Warning('entrance_south_warn', 'pre_act_cmd', [['go', 'south']], 0, 0)
attack_hedgehog_warning = Warning('attack_hedgehog_warning', 'pre_act_cmd',
		[['attack', 'shiny_sword', 'royal_hedgehog'], ['attack', 'grimy_axe', 'royal_hedgehog']], 3, 0)
eat_biscuits_warning = Warning('eat_biscuits_warning', 'pre_act_cmd', [['eat','stale_biscuits']], 3, 0)

# machines
entrance_moat_mach = InvisMach('entrance_moat_mach', False, 'pre_act_cmd', None, [['go', 'east'], ['go', 'west']],
		None, [hand_no_weap_cond, hand_weap_1st_cond, hand_weap_repeat_cond],
		[die_in_moat_result, moat_get_crown_result, moat_croc_scared_result]) # machine_state == got_crown

broach_dispenser_mach = InvisMach('broach_dispenser_mach', False, 'post_act_switch', throne, ['pushed', 'pulled'],
		[throne], [broach_dispensed_cond, throne_push_cond, throne_pull_cond],
		[nothing_happens_result, throne_push_result, throne_pull_result]) # machine_state == broach_dispensed

control_panel = ContainerFixedSimpleMach('control_panel', 'Control Panel', 'panel', 'control_panel', None, [left_lever, middle_lever, right_lever, red_button], 999, 4, 'on',
		0, 'post_act_switch', red_button, ['pushed'], [left_lever, middle_lever, right_lever], [correct_lever_array_cond, wrong_lever_array_cond],
		[toggle_portcullis_result, portcullis_doesnt_open_result])
		# machine_state == lever_array_value

hedgehog_eats_mach = InvisMach('hedgehog_eats_mach', None, 'post_act_cmd', None, [['give', 'stale_biscuits', 'royal_hedgehog']],
		None, [hedgehog_has_biscuit_cond, pass_thru_cond], [start_hedgehog_timer_results, pass_result])

hedgehog_guard_mach = InvisMach('hedgehog_guard_mach', None, 'pre_act_cmd', None, [['take', 'shiny_sword']],
		None, [hedgehog_guard_cond, pass_thru_cond], [hedgehog_attacks_result, pass_result])

hedgehog_done_eating_mach = InvisMach('hedgehog_done_eating_mach', 0, 'pre_act_timer', hedgehog_eats_timer, [True], None,
		[hedgehog_keeps_sword_cond, hedgehog_loses_sword_cond, pass_thru_cond],
		[fed_hedgehog_keeps_sword_result, fed_hedgehog_loses_sword_result, pass_result]) # machine_state == post-eating description updated?

goblin_attack_mach = InvisMach('goblin_attack_mach', None, 'pre_act_cmd', None,
		[['examine', 'iron_portcullis'], ['examine', 'alcove'], ['examine', 'grimy_axe'], ['take', 'grimy_axe'],
		['open', 'iron_portcullis'], ['go', 'north']],
		None, [pass_thru_cond], [goblin_attacks_result])

hedgehog_distracted_mach = InvisMach('hedgehog_distracted_mach', None, 'pre_act_cmd', None,
		[['give', '*', 'royal_hedgehog'], ['show', '*', 'royal_hedgehog']], None, 
		[hedgehog_distracted_cond, pass_thru_cond], [hedgehog_distracted_result, pass_result])

kinging_scroll = ItemMach('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', illuminated_letters, 1, 
		None, 'post_act_cmd', None, 
		[['read', 'illuminated_letters'],['read', 'kinging_scroll'], ['examine', 'illuminated_letters']], None,
		[scroll_not_in_throne_room_cond, hedgehog_not_exist_cond, crown_not_worn_cond, read_scroll_win_cond],
		[scroll_wrong_room_result, scroll_no_hedgehog_result, scroll_crown_not_worn_result, scroll_win_game_result])

re_arm_goblin_mach = InvisMach('re_arm_goblin_mach', None, 'auto_act', None, None, None,
		[axe_in_goblin_hand_cond, pass_thru_cond], [axe_in_goblin_hand_result, pass_result])

dispense_panel_mach = InvisMach('dispense_panel_mach', False, 'auto_act', None, None, None, [goblin_exist_state_cond, pass_thru_cond], [dispense_panel_result, pass_result])

cecily = Creature('cecily', 'Cecily', 'cecily', 'cecily', None,
		None, [], [rusty_key, cheese_wedge, stale_biscuits, earthen_jug], [], [fist, backpack, conscience, brass_lantern],
		[hedgehog_eats_timer],
		{},
		True,
		{
			'grimy_axe_guard_goblin_weapon' : 'hard_parry', # parry
			'grimy_axe_guard_goblin_*' : 'tgt_death',
			'fierce_teeth_royal_hedgehog_*' : 'jump_back'
		}, 90, 90)

# *** Rooms ***
pub = Room('pub', 'Pub', "pub", 'pub', None, [dark_castle, moat],
		[cecily], [entrance_moat_mach, entrance_south_warn, eat_biscuits_warning])
		# note: for timer testing, big_bomb was in entrance.floor_lst and blue_button was in entrance.feature_lst

unreachable_1 = Room('unreachable_1', 'Unreachable', 'unreachable_1', 'unreachable_1', None, [], [], [])


# *** gs class modules ***
core = Core(
		'core', # name
		cecily, # hero
        0, # move_count
        False # is_debug
#		dark_castle # game_name
		)

map = Map(
		'map', # name
		pub, # hero_rm
		[
			{'room_x' : pub, 'dir_x' : 'south', 'door' : front_gate, 'dir_y' : None, 'room_y' : unreachable_1},
		] # map_lst
		)

io = IO(
		'io', # name
		{}, # dyn_dict
		"", # buff_str
		"", # last_input_str
		'cup_of_tea' # game_name
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


### instantiated objects added to list ###
### Used as an obj index in Interp() - must include all non-invisible obj ###
### invisible objects need not be listed ###
master_obj_lst = [gs, calligraphy, dark_castle, moat, backpack, fist, conscience, faded_tapestries, alcove, stone_coffer, family_tree, dead_goblin, rusty_key, brass_key, bubbly_potion, kinging_scroll, random_mcguffin, baseball_cap, front_gate, control_panel, pub, loyalty,
officiousness, cecily, brass_lantern, fierce_teeth, chewed_fingernails, wooden_shelf, test_chair, screen_door, cardboard_box, small_barrel, red_shoebox, black_suitcase, heavy_rock] # note: big_bomb & test_frog removed; glass_bottle removed

# list written to pickle
with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/cup_of_tea/game_file/game_pkl', 'wb') as f:
	pickle.dump(master_obj_lst, f)




