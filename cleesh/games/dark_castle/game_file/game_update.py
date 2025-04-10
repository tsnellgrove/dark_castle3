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
from cleesh.class_std.room_class_def import Room, InitDesc
from cleesh.class_std.item_class_def import Item, Food, Liquid, Garment, Weapon
from cleesh.class_std.interactive_class_def import DoorSimple, DoorLockable
from cleesh.class_std.interactive_class_def import ContainerFixedSimple, ContainerFixedLidded, ContainerFixedLockable, Seat
from cleesh.class_std.interactive_class_def import ContainerPortableSimple, ContainerPortableLidded, ContainerPortableLockable
from cleesh.class_mach.switch_class_def import ViewOnlyLeverSwitch, ViewOnlyButtonSwitch, SeatSpringSliderSwitch
from cleesh.class_mach.cond_class_def import (TrueCond, 
		WornCond, CreatureContainedCond, ObjOnRmFlrCond, ObjInRmCond, ObjInWorldCond, 
		ItemInHandCond, ObjInInvCond, WeaponInHandCond, 
		MachStateCond, TimerActiveCond, SwitchStateCond, LeverArrayCond)
from cleesh.class_mach.result_class_def import (BaseResult, DisableMach, EndResult, ChgDescriptResult, 
		GiveItemResult, TakeItemResult, DispenseObjResult, StartTimerResult, RemoveObjResult, AttackHeroResult, 
		OpenableToggleResult, CreatureTravelResult)
from cleesh.class_mach.mach_class_def import (Timer, Warning, InvisAutoMach, WeaponAutoMach, InvisTrigMach, ItemTrigMach,
		InvisSwitchMach, ContainerFixedSimpleSwitchMach
		)
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
elven_runes = Writing('elven_runes', 'Elven Runes', "runes", 'elven_runes')
messy_handwriting = Writing('messy_handwriting', 'Messy Handwriting', 'handwriting', 'messy_handwriting')
small_printing = Writing('small_printing', 'Small Printing', 'printing', 'small_printing')
illuminated_letters = Writing('illuminated_letters', 'Illuminated Letters', 'letters', 'illuminated_letters')
calligraphy = Writing('calligraphy', 'Calligraphy', 'calligraphy', 'calligraphy')
insignia = Writing('insignia', 'Insignia', 'insignia', 'insignia')
gold_capitals = Writing('gold_capitals', 'Gold Capitals', 'capitals', 'gold_capitals')
royal_cypher = Writing('royal_cypher', 'Royal Cypher', 'cypher', 'royal_cypher')
bold_script = Writing('bold_script', 'Bold Script', 'script', 'bold_script')

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
family_tree = ViewOnly('family_tree', 'Family Tree', 'tree', 'family_tree', None)
dead_goblin = ViewOnly('dead_goblin', 'Dead Goblin', 'goblin', 'dead_goblin', None)
officiousness = ViewOnly('officiousness', 'Officiousness', 'officiousness', 'officiousness', None)
loyalty = ViewOnly('loyalty', 'Loyalty', 'loyalty', 'loyalty', None)
drawbridge = ViewOnly('drawbridge', 'Drawbridge', 'drawbridge', 'drawbridge', None)
rusty_keyhole = ViewOnly('rusty_keyhole', 'Rusty Keyhole', 'keyhole', 'rusty_keyhole', None)

# Item
rusty_key = Item('rusty_key', 'Rusty Key', "key", 'rusty_key', None, 1)
torn_note = Item('torn_note', 'Torn Note', 'note', 'torn_note', messy_handwriting, 1)
silver_key = Item('silver_key', 'Silver Key', 'key', 'silver_key', None, 1)
ancient_certificate = Item('ancient_certificate', 'Ancient Certificate', 'certificate', 'ancient_certificate', bold_script, 1)
# big_rock = Item('big_rock', 'Big Rock', 'rock', 'big_rock', None, 50)
zorkmid = Item('zorkmid', 'Zorkmid', 'coin', 'zorkmid', None, 0.5)

# Food
cheese_wedge = Food('cheese_wedge', 'Cheese Wedge', 'cheese', 'cheese_wedge', None, 1)
baked_biscuit = Food('baked_biscuit', 'Baked Biscuit', 'biscuit', 'baked_biscuit', insignia, 1)

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

# Containers (NOTE for PORTABLE containers, weight of starting contents MUST be included in container weight!!!)
wooden_shelf = ContainerFixedSimple('wooden_shelf', 'Wooden Shelf', 'shelf', 'wooden_shelf', None, [], 999, 20, 'on')
crystal_box = ContainerFixedLockable('crystal_box', 'Crystal Box', 'box', 'crystal_box', calligraphy, ['kinging_scroll_temp'], 1, 999, 'in', False, False, silver_key)
earthen_jug = ContainerPortableSimple('earthen_jug', 'Earthen Jug', 'jug', 'earthen_jug', None, 1.5, [well_water], 0.5, 5, 'in')
paper_bag = ContainerPortableLidded('paper_bag', 'Paper Bag', 'bag', 'paper_bag', None, 1.5, [baked_biscuit], 1.5, 3, 'in', False)
stone_coffer = ContainerFixedSimple('stone_coffer', 'Stone Coffer', 'coffer', 'stone_coffer', None, [], 100, 999, 'in')
postbox = ContainerFixedLidded('postbox', 'Postbox', 'postbox', 'postbox', royal_cypher, [ancient_certificate], 999, 5, 'in', False)

# Door
front_gate = DoorLockable('front_gate', 'Front Gate', "gate", 'front_gate', rusty_lettering, False, False, rusty_key)
iron_portcullis = DoorLockable('iron_portcullis', 'Iron Portcullis', 'portcullis', 'iron_portcullis', None, False, False, None)

# Switches
left_lever = ViewOnlyLeverSwitch('left_lever', 'Left Lever', 'lever', 'left_lever', None, 'down', None, None)
middle_lever = ViewOnlyLeverSwitch('middle_lever', 'Middle Lever', 'lever', 'middle_lever', None, 'down', None, None)
right_lever = ViewOnlyLeverSwitch('right_lever', 'Right Lever', 'lever', 'right_lever', None, 'down', None, None)
red_button = ViewOnlyButtonSwitch('red_button', 'Red Button', 'button', 'red_button', None, 'neutral', 'neutral', 'auto_switch_reset')
throne = SeatSpringSliderSwitch('throne', 'Throne', 'throne', 'throne_pre_broach', None, [], 999, 2, 'on', [crystal_box], 'neutral', 'neutral', 'auto_switch_reset')

# test / legacy obj - not currently in use
dwarven_runes = Writing('dwarven_runes', 'Dwarven Runes', "runes", 'dwarven_runes')
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None, 1) # test object
bubbly_potion = Item('bubbly_potion', 'bubbly potion', "potion", 'bubbly_potion', None, 2) # test object
random_mcguffin = Item('random_mcguffin', 'Random McGuffin', 'mcguffin', 'random_mcguffin', None, 5) # test object
baseball_cap = Garment('baseball_cap', 'Baseball Cap', 'cap', 'baseball_cap', None, 1, 'hat')
cardboard_box = ContainerFixedLidded('cardboard_box', 'Cardboard Box', 'box', 'cardboard_box', None, [], 999, 2, 'in', False)
small_barrel = ContainerPortableSimple('small_barrel', 'Small Barrel', 'barrel', 'small_barrel', None, 2, [], 5, 999, 'in')
red_shoebox = ContainerPortableLidded('red_shoebox', 'Red Shoebox', 'shoebox', 'red_shoebox', None, 1, [], 3, 999, 'in', False)
black_suitcase = ContainerPortableLockable('black_suitcase', 'Black Suitcase', 'suitcase', 'black_suitcase', None, 3, [], 7, 999, 'in', False, False, rusty_key)
screen_door = DoorSimple('screen_door', 'Screen Door', 'door', 'screen_door', None, False)
test_chair = Seat('test_chair', 'Test Chair', 'chair', 'test_chair', None, [], 999, 2, 'on', [wooden_shelf])
trademark = Writing('trademark', 'Trademark', 'trademark', 'trademark')
stale_biscuits = Food('stale_biscuits', 'Stale Biscuits', 'biscuits', 'stale_biscuits', trademark, 3)
eat_biscuits_warning = Warning('eat_biscuits_warning',
		'pre_act_cmd', 0, stale_biscuits, True, 
		[['eat','stale_biscuits']], 3)
random_mcguffin_init_desc = InitDesc('random_mcguffin_init_desc', random_mcguffin, 'random_mcguffin_init_desc')


# test obj - currently in use
# TBD

# *** timers ***
hedgehog_eats_timer = Timer('hedgehog_eats_timer', 
		'auto_act', 0, 'temp_royal_hedgehog', True, False, 4)


# *** warnings ***
entrance_south_warn = Warning('entrance_south_warn', 
		'pre_act_cmd', 0, 'entrance_temp', True, 
		[['go', 'south']], 0)

attack_hedgehog_warning = Warning('attack_hedgehog_warning', 
		'pre_act_cmd', 0, 'royal_hedgehog_temp', True, 
		[['attack', 'shiny_sword', 'royal_hedgehog'], ['attack', 'grimy_axe', 'royal_hedgehog']], 3)

eat_biscuits_warning = Warning('eat_biscuits_warning',
		'pre_act_cmd', 0, baked_biscuit, True, 
		[['eat','baked_biscuit']], 3)


# *** conditions ***
# *** note: obj.open (if locked) and room.go (w/ closed door in way) must be tested for success ***
true_cond = TrueCond('true_cond')
true_cond_valid_not_reqd = TrueCond('true_cond', is_valid_reqd = False)
crown_not_worn_cond = WornCond('crown_not_worn_cond', royal_crown, 'burt_temp', False)
biscuits_in_hedgehog_hand_cond = ItemInHandCond('biscuits_in_hedgehog_hand_cond', baked_biscuit, 'royal_hedgehog_temp', True)
axe_not_in_goblin_hand_cond = ItemInHandCond('axe_not_in_goblin_hand_cond', grimy_axe, 'guard_goblin_temp', False)
silver_key_given_cond = ObjInInvCond('silver_key_given_cond', silver_key, 'royal_hedgehog_temp', False)
no_weap_in_hand_cond = WeaponInHandCond('silver_key_given', 'burt_temp', False)
sword_on_floor = ObjOnRmFlrCond('sword_on_floor', 'main_hall_temp', 'shiny_sword_temp', True)# sword_not_on_floor = ObjOnRmFlrCond('sword_not_on_floor', 'main_hall_temp', shiny_sword, False)
sword_not_on_floor = ObjOnRmFlrCond('sword_not_on_floor', 'main_hall_temp', 'shiny_sword_temp', False)
not_in_throne_room_cond = ObjInRmCond('not_in_throne_room_cond', 'throne_room_temp', 'burt_temp', False)
hedgehog_not_in_world_cond = ObjInWorldCond('hedgehog_not_in_world_cond', 'royal_hedgehog_temp', False)
goblin_in_world_cond = ObjInWorldCond('goblin_in_world_cond', 'guard_goblin_temp', True)
goblin_not_in_world_cond = ObjInWorldCond('goblin_not_in_world_cond', 'guard_goblin_temp', False)
broach_dispensed_cond = MachStateCond('broach_dispensed_cond', True, True)
crown_not_dispensed_cond = MachStateCond('crown_not_dispensed_cond', False, True)
crown_dispensed_cond = MachStateCond('crown_dispensed_cond', True, True)
panel_not_dispensed_cond = MachStateCond('panel_not_dispensed_cond', False, True)
hedgehog_descript_updated_cond = MachStateCond('hedgehog_descript_updated_cond', True, True)
hedgehog_eats_timer_active_cond = TimerActiveCond('hedgehog_eats_timer_active_cond', hedgehog_eats_timer, True) # hedgehog is distracted
hedgehog_eats_timer_not_active_cond = TimerActiveCond('hedgehog_eats_timer_not_active_cond', hedgehog_eats_timer, False) # hedgehog is not eating
throne_push_cond = SwitchStateCond('throne_push_cond', [throne], ['pushed'])
throne_pull_cond = SwitchStateCond('throne_pull_cond', [throne], ['pulled'])
lever_array_matches_mach_state_cond = LeverArrayCond('lever_array_matches_mach_state_cond', [left_lever, middle_lever, right_lever], [4,2,1])
not_in_throne_cond = CreatureContainedCond('not_in_throne_cond', throne, 'burt_temp', False)
sword_not_in_burt_inv_cond = ObjInInvCond('sword_not_in_burt_inv_cond', 'shiny_sword_temp', 'burt_temp', False)
burt_in_hall_cond = ObjInRmCond('burt_in_hall_cond', 'main_hall_temp', 'burt_temp', True)
burt_in_entrance_cond = ObjInRmCond('burt_in_entrance_cond', 'entrance_temp', 'burt_temp', True)
burt_in_antechamber_cond = ObjInRmCond('burt_in_antechamber_cond', 'antechamber_temp', 'burt_temp', True)
sword_state_is_0_cond = MachStateCond('sword_state_not_0_cond', 0, True)
sword_state_not_0_cond = MachStateCond('sword_state_not_0_cond', 0, False)
sword_state_not_1_cond = MachStateCond('sword_state_not_1_cond', 1, False)
sword_state_not_2_cond = MachStateCond('sword_state_not_2_cond', 2, False)
mach_state_false = MachStateCond('mach_state_false', False, True)
mach_state_true = MachStateCond('mach_state_true', True, True)

# *** results ***
pass_result = BaseResult('pass_result', False, None, False)
moat_croc_scared_result = BaseResult('moat_croc_scared_result', False, None, True)
nothing_happens_result = BaseResult('nothing_happens_result', False, None, False)
throne_push_result = BaseResult('throne_push_result', False, None, False)
portcullis_doesnt_open_result = BaseResult('portcullis_doesnt_open_result', False, None, False)
hedgehog_distracted_result = BaseResult('hedgehog_distracted_result', False, None, True)
scroll_wrong_room_result = BaseResult('scroll_wrong_room_result', False, None, False)
scroll_no_hedgehog_result = BaseResult('scroll_no_hedgehog_result', False, None, False)
scroll_crown_not_worn_result = BaseResult('scroll_crown_not_worn_result', False, None, False)
scroll_not_in_throne_result = BaseResult('scroll_not_in_throne_result', False, None, False)
die_in_moat_result = EndResult('die_in_moat_result', False, None, True, 'died.')
scroll_win_game_result = EndResult('scroll_win_game_result', False, None, False, 'won!')
fed_hedgehog_keeps_sword_result = ChgDescriptResult('fed_hedgehog_keeps_sword_result', True, True, False, 'royal_hedgehog_temp', 'hedgehog_desc_smug')
fed_hedgehog_loses_sword_result = ChgDescriptResult('fed_hedgehog_loses_sword_result', True, True, False, 'royal_hedgehog_temp', 'hedgehog_desc_yearn')
moat_get_crown_result = GiveItemResult('moat_get_crown_result', True, True, True, royal_crown, 'temp_burt')
goblin_take_axe_result = TakeItemResult('goblin_take_axe_result', False, None, False, 'guard_goblin_temp', grimy_axe)
throne_pull_result1 = ChgDescriptResult('throne_pull_result1', False, None, False, throne, 'throne_post_broach')
throne_pull_result2 = DispenseObjResult('throne_pull_result2', True, True, False, hedgehog_broach, 'throne_room_temp')
dispense_panel_result1 = ChgDescriptResult('dispense_panel_result1', False, None, False, 'antechamber_temp', 'antechamber_with_panel')
dispense_panel_result2 = DispenseObjResult('dispense_panel_result2', True, True, False, 'control_panel_temp', 'antechamber_temp')
hedgehog_eats_result1 = StartTimerResult('hedgehog_eats_result1', False, None, False, hedgehog_eats_timer)
hedgehog_eats_result2 = RemoveObjResult('hedgehog_eats_result2', False, None, False, baked_biscuit)
goblin_attacks_result = AttackHeroResult('goblin_attacks_result', False, None, True, 'guard_goblin_temp', grimy_axe)
hedgehog_attacks_result = AttackHeroResult('hedgehog_attacks_result', False, None, True, 'royal_hedgehog_temp', fierce_teeth)
toggle_portcullis_result = OpenableToggleResult('toggle_portcullis_result', False, None, False, iron_portcullis)
disable_rh_guard_result1 = DisableMach('disable_rh_guard_result1', False, None, False, 'hedgehog_guard_mach_temp')
disable_rh_guard_result2 = DisableMach('disable_rh_guard_result2', False, None, False, 'disable_rh_guard_mach_temp')
sword_stops_glowing_result = BaseResult('sword_stops_glowing_result', True, 0, False)
disable_shiny_sword_result = DisableMach('disable_shiny_sword_result', False, None, False, 'shiny_sword_temp')
sword_starts_glowing_result = BaseResult('sword_starts_glowing_result', True, 1, False)
sword_glows_bright_result = BaseResult('sword_glows_bright_result', True, 2, False)
big_rock_take_result1 = DispenseObjResult('big_rock_take_result1', True, True, False, zorkmid, 'entrance_temp')
big_rock_take_result2 = DisableMach('big_rock_take_result2', False, None, False, 'big_rock_temp')

# *** machines ***

## AutoMach ##
## auto_act runs every move if mach is in scope - there is no trigger

dispense_panel_mach = InvisAutoMach('dispense_panel_mach', False,
		'auto_act', 'antechamber_temp', True,
		[goblin_in_world_cond, panel_not_dispensed_cond],
		[pass_result, [dispense_panel_result1, dispense_panel_result2]])
		# mach_state == has panel been dispensed

re_arm_goblin_mach = InvisAutoMach('re_arm_goblin_mach', None, 
		'auto_act', 'guard_goblin_temp', True, 
		[axe_not_in_goblin_hand_cond], 
		[goblin_take_axe_result])
		# mach_state == None

disable_rh_guard_mach = InvisAutoMach('disable_rh_guard_mach', None, 
		'auto_act', 'royal_hedgehog_temp', True, 
		[silver_key_given_cond], 
		[[disable_rh_guard_result1, disable_rh_guard_result2]])
		# mach_state == None

# shiny_swordnew = WeaponAutoMach('shiny_swordnew', 'Shiny SwordNew', 'swordnew', 'shiny_sword', elven_runes, 10,
shiny_sword = WeaponAutoMach('shiny_sword', 'Shiny Sword', 'sword', 'shiny_sword', elven_runes, 10,
		[['swings', 'blazing-fast assault'],['stabs', 'cunning unterhau']], 0, 
		'auto_act', 'shiny_sword_temp', True,
		[
			[sword_not_in_burt_inv_cond, sword_state_is_0_cond],
			[sword_not_in_burt_inv_cond, sword_state_not_0_cond], 
			goblin_not_in_world_cond, 
			[burt_in_entrance_cond, sword_state_not_0_cond],
			[burt_in_hall_cond, sword_state_not_1_cond],
			[burt_in_antechamber_cond, sword_state_not_2_cond]
		],
		[
			pass_result,
			sword_stops_glowing_result,
			[sword_stops_glowing_result, disable_shiny_sword_result], 
			sword_stops_glowing_result,
			sword_starts_glowing_result,
			sword_glows_bright_result
		]
		) # mach_state == sword brightness; 0 = not glowing, 1 = glowing, 2 = glowing brightly


## TrigMach ##
## for pre_act_cmd or post_act_cmd: trig_vals_lst = list-of-list of word_lst values that will trigger mach
## prep case word_lst => trig_vals_lst is erratic. see interp() ln 201, validate() ln 32, & mach_class() ln 72

hedgehog_guard_mach = InvisTrigMach('hedgehog_guard_mach', None, 
		'pre_act_cmd', 'royal_hedgehog_temp', True, 
		[['take', 'shiny_sword']],
		[sword_not_on_floor, hedgehog_eats_timer_not_active_cond], 
		[pass_result, hedgehog_attacks_result]
		) # mach_state == None

hedgehog_distracted_mach = InvisTrigMach('hedgehog_distracted_mach', None, 
		'pre_act_cmd', 'royal_hedgehog_temp', True,
		[['give', '*', 'royal_hedgehog'], ['show', '*', 'royal_hedgehog']], 
		[hedgehog_eats_timer_active_cond], 
		[hedgehog_distracted_result]
		) # mach_state == None

goblin_attack_mach = InvisTrigMach('goblin_attack_mach', None, 
		'pre_act_cmd', 'guard_goblin_temp', True,
		[['examine', 'iron_portcullis'], ['examine', 'alcove'], ['examine', 'grimy_axe'], 
   		['take', 'grimy_axe'], ['open', 'iron_portcullis'], ['go', 'north'],
		['unlock', '*', 'iron_portcullis']], 
		[true_cond_valid_not_reqd], 
		[goblin_attacks_result]
		) # mach_state == None

entrance_moat_mach = InvisTrigMach('entrance_moat_mach', False, 
		'pre_act_cmd', 'entrance_temp', True,
		[['go', 'east'], ['go', 'west']],
		[no_weap_in_hand_cond, crown_not_dispensed_cond, crown_dispensed_cond],
		[die_in_moat_result, moat_get_crown_result, moat_croc_scared_result]
		) # mach_state == got_crown

hedgehog_eats_mach = InvisTrigMach('hedgehog_eats_mach', None, 
		'post_act_cmd', 'royal_hedgehog_temp', True,
		[['give', 'baked_biscuit', 'royal_hedgehog']], 
		[biscuits_in_hedgehog_hand_cond],
		[[hedgehog_eats_result1, hedgehog_eats_result2]]
		) # mach_state == None

kinging_scroll = ItemTrigMach('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll', 
		illuminated_letters, 1, None, 
		'post_act_cmd', 'kinging_scroll_temp', True,
		[['read', 'illuminated_letters'],['read', 'kinging_scroll'], ['examine', 'illuminated_letters']], 
		[not_in_throne_room_cond, hedgehog_not_in_world_cond, crown_not_worn_cond, not_in_throne_cond, 
   				true_cond],
		[scroll_wrong_room_result, scroll_no_hedgehog_result, scroll_crown_not_worn_result, scroll_not_in_throne_result, 
				scroll_win_game_result]
		) # mach_state == None

big_rock = ItemTrigMach('big_rock', 'Big Rock', 'rock', 'big_rock',
		None, 50, False,
		'post_act_cmd', 'entrance_temp', True,
		[['take', 'big_rock']],
		[mach_state_true, mach_state_false],
		[pass_result, [big_rock_take_result1, big_rock_take_result2]]
		) # mach_state == has zorkmid been dispensed

## SwitchMach ##
## for auto_act_timer: trig_vals_lst = list of trigger values for timer.is_dinging()
## for post_act_switch: trig_vals_lst = list of trigger values for cond_switch

hedgehog_done_eating_mach = InvisSwitchMach('hedgehog_done_eating_mach', False, 
		'auto_act_timer', 'royal_hedgehog_temp', True, 
		hedgehog_eats_timer, [True], 
		[hedgehog_descript_updated_cond, sword_on_floor, sword_not_on_floor],
		[pass_result, fed_hedgehog_keeps_sword_result, fed_hedgehog_loses_sword_result]
		) # mach_state == mach has run once

control_panel = ContainerFixedSimpleSwitchMach('control_panel', 'Control Panel', 'panel', 'control_panel', None, 
		[left_lever, middle_lever, right_lever, red_button], 999, 4, 'on', 0, 
		'post_act_switch', 'antechamber_temp', True, 
		red_button, ['pushed'],
		[lever_array_matches_mach_state_cond, true_cond], 
		[toggle_portcullis_result, portcullis_doesnt_open_result]
		) # mach_state == lever_array_value

broach_dispenser_mach = InvisSwitchMach('broach_dispenser_mach', False, 
		'post_act_switch', 'throne_room_temp', True, 
		throne, ['pushed', 'pulled'],
		[broach_dispensed_cond, throne_push_cond, throne_pull_cond],
		[nothing_happens_result, throne_push_result, [throne_pull_result1, throne_pull_result2]],
		) # mach_state == broach_dispensed


# *** creatures	***

guard_goblin = Creature('guard_goblin', 'Guard Goblin', 'goblin', 'guard_goblin', None,
		None, [grimy_axe], [torn_note, dead_goblin], [big_medal], [chewed_fingernails, officiousness],
		[goblin_attack_mach, re_arm_goblin_mach],
		{
			shiny_sword : {'accept' : False, 'give' : None},
			baked_biscuit : {'accept' : False, 'give' : None},
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
		[
			attack_hedgehog_warning, hedgehog_eats_mach, hedgehog_guard_mach, hedgehog_distracted_mach, 
   			disable_rh_guard_mach
		],
		{
			shiny_sword : {'accept' : True, 'give' : silver_key},
			silver_key : {'accept' : True, 'give' : shiny_sword},
			baked_biscuit : {'accept' : True, 'give' : None}
		},
		True,
		{
			'weapon_burt_*' : 'tgt_flee_dc',
			'unarmed_burt_*' : 'easy_dodge', # karate kid
			'*_*_*' : 'easy_dodge' # dodge
		}, 22, 999)

burt = Creature('burt', 'Burt', 'burt', 'burt', None,
		None, [], [rusty_key, cheese_wedge, paper_bag, earthen_jug], [], [fist, backpack, conscience, brass_lantern],
		[],
		{},
		True,
		{
			'grimy_axe_guard_goblin_weapon' : 'hard_parry', # parry
			'grimy_axe_guard_goblin_*' : 'tgt_death',
			'fierce_teeth_royal_hedgehog_*' : 'jump_back'
		}, 105, 150) # note: for non-burt-creature testing frog_travel_mach was in burt.invis_lstj

# *** Initial Descriptions ***
postbox_init_desc = InitDesc('postbox_init_desc', postbox, 'postbox_init_desc')
shiny_sword_init_desc = InitDesc('shiny_sword_init_desc', shiny_sword, 'shiny_sword_init_desc')
big_rock_init_desc = InitDesc('big_rock_init_desc', big_rock, 'big_rock_init_desc')


# *** Rooms ***
gatehouse = Room('gatehouse', 'Gatehouse', 'gatehouse', 'gatehouse', None, 
		[dark_castle, moat, drawbridge, rusty_keyhole],
		[burt, postbox, big_rock], [entrance_moat_mach, entrance_south_warn], [postbox_init_desc, big_rock_init_desc])
		# note: for timer testing, big_bomb was in entrance.floor_lst and blue_button was in entrance.feature_lst

entrance = Room('entrance', 'Entrance', "entrance", 'entrance', None, 
		[dark_castle, moat, drawbridge, rusty_keyhole],
		[burt, postbox, big_rock], [entrance_moat_mach, entrance_south_warn], [postbox_init_desc, big_rock_init_desc])
		# note: for timer testing, big_bomb was in entrance.floor_lst and blue_button was in entrance.feature_lst

main_hall = Room('main_hall', 'Main Hall', "hall", 'main_hall', None, [faded_tapestries],
		[shiny_sword, royal_hedgehog, wooden_shelf], [], [shiny_sword_init_desc])
		# note: for non-burt-creature testing, test_frog was in main_hall.floor_lst

antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
		[alcove], [guard_goblin], [dispense_panel_mach], [])

throne_room = Room('throne_room', 'Throne Room', 'throne_room', 'throne_room', None, [stone_coffer, family_tree],
		[throne, crystal_box], [broach_dispenser_mach], [])

unreachable_1 = Room('unreachable_1', 'Unreachable', 'unreachable_1', 'unreachable_1', None, [], [], [], [])

unreachable_2 = Room('unreachable_2', 'Unreachable', 'unreachable_2', 'unreachable_2', None, [], [], [], [])

unreachable_3 = Room('unreachable_3', 'Unreachable', 'unreachable_3', 'unreachable_3', None, [], [], [], [])


# *** gs class modules ***

core = Core(
		'core', # name
		burt, # hero
		5, # hero_descript_count
        0, # move_count
        False, # is_debug
		{}, # str_to_obj_dict
		True, # has_session_vars
		[eat_biscuits_warning, hedgehog_eats_timer, hedgehog_done_eating_mach] # univ_invis_lst
		)

map = Map(
		'map', # name
		entrance, # hero_rm
		[{'room_x' : entrance, 'dir_x' : 'north', 'door' : front_gate, 'dir_y' : 'south', 'room_y' : main_hall},
		{'room_x' : entrance, 'dir_x' : 'south', 'door' : 'path leading back home', 'dir_y' : None, 'room_y' : unreachable_1},
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
		None, # game_ending
		True # is_bkstry
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
silver_key_given_cond.creature_obj = royal_hedgehog
no_weap_in_hand_cond.creature_obj = burt
goblin_in_world_cond.obj = guard_goblin
sword_not_on_floor.match_room = main_hall
sword_on_floor.match_room = main_hall
not_in_throne_cond.creature_obj = burt
sword_not_in_burt_inv_cond.creature_obj = burt
sword_not_in_burt_inv_cond.item_obj = shiny_sword
goblin_not_in_world_cond.obj = guard_goblin
burt_in_hall_cond.obj = burt
burt_in_hall_cond.match_room = main_hall
burt_in_entrance_cond.obj = burt
burt_in_entrance_cond.match_room = entrance
burt_in_antechamber_cond.obj = burt
burt_in_antechamber_cond.match_room = antechamber
sword_on_floor.obj = shiny_sword
sword_not_on_floor.obj = shiny_sword
big_rock_take_result1.room_obj = entrance

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
entrance_south_warn.alert_anchor = entrance
attack_hedgehog_warning.alert_anchor = royal_hedgehog
disable_rh_guard_mach.alert_anchor = royal_hedgehog
shiny_sword.alert_anchor = shiny_sword
big_rock.alert_anchor = entrance

fed_hedgehog_keeps_sword_result.obj = royal_hedgehog
fed_hedgehog_loses_sword_result.obj = royal_hedgehog
moat_get_crown_result.tgt_creature = burt
goblin_take_axe_result.creature_obj = guard_goblin
throne_pull_result2.room_obj = throne_room
dispense_panel_result1.obj = antechamber
dispense_panel_result2.dispense_obj = control_panel
dispense_panel_result2.room_obj = antechamber
disable_rh_guard_result1.mach = hedgehog_guard_mach
disable_rh_guard_result2.mach = disable_rh_guard_mach
disable_shiny_sword_result.mach = shiny_sword
big_rock_take_result2.mach = big_rock

goblin_attacks_result.creature_obj = guard_goblin
hedgehog_attacks_result.creature_obj = royal_hedgehog

hedgehog_eats_timer.alert_anchor = royal_hedgehog
crystal_box.contain_lst = [kinging_scroll]

## test_chair.in_reach_lst = [main_hall, front_gate, wooden_shelf]


### instantiated objects added to list ###
### Used as an obj index in Interp() - must include all non-invisible obj ###
### invisible objects need not be listed ###
master_obj_lst = [
		gs, rusty_lettering, elven_runes, messy_handwriting, small_printing, illuminated_letters, calligraphy, 
		dark_castle, moat, backpack, burt, fist, conscience, faded_tapestries, alcove, stone_coffer, 
		family_tree, dead_goblin, rusty_key, shiny_sword, torn_note, grimy_axe, silver_key, kinging_scroll, 
		cheese_wedge, well_water, royal_crown, hedgehog_broach, crystal_box, front_gate, iron_portcullis, 
		control_panel, throne, left_lever, middle_lever, right_lever, red_button, royal_hedgehog, guard_goblin, 
		entrance, main_hall, antechamber, throne_room, loyalty, officiousness, gold_capitals, red_bandana, 
		big_medal, burt, brass_lantern, fierce_teeth, chewed_fingernails, wooden_shelf, earthen_jug, paper_bag, 
		insignia, baked_biscuit, drawbridge, rusty_keyhole, royal_cypher, postbox, ancient_certificate, 
		bold_script, big_rock, zorkmid,

		# test objects
		dwarven_runes, trademark, brass_key, bubbly_potion, random_mcguffin, stale_biscuits, baseball_cap, 
		test_chair, screen_door, cardboard_box, small_barrel, red_shoebox, black_suitcase, 
	] # note: big_bomb & test_frog removed; glass_bottle removed

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


