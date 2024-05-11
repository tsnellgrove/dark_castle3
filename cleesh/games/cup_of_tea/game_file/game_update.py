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
cursive = Writing('cursive', 'Cursive', 'cursive', 'cursive')
block_text = Writing('block_text', 'Block Text', 'text', 'block_text')

# ViewOnly
hand = ViewOnly('hand', 'Hand', "hand", 'hand', None)

# Item
rusty_key = Item('rusty_key', 'Rusty Key', "key", 'rusty_key', None, 1)
brass_key = Item('brass_key', 'brass key', "key", 'brass_key', None, 1)

# Food

# Liquid
tea = Liquid('tea', 'Tea', 'tea', 'tea', None, 0.5)

# Garment

# Weapon

# Container
dingy_shelf = ContainerFixedSimple('dingy_shelf', 'Dingy Shelf', 'shelf', 'dingy_shelf', None, [], 999, 20, 'on')
tea_cup = ContainerPortableSimple('tea_cup', 'Tea Cup', 'cup', 'tea_cup', cursive, 1.5, [tea], 0.5, 5, 'in')
comfy_chair = Seat('comfy_chair', 'Comfy Chair', 'chair', 'comfy_chair', None, [], 999, 2, 'on', [])

# Door
creaky_door = DoorLockable('creaky_door', 'Creaky Door', "door", 'creaky_door', block_text, False, False, rusty_key)

# Switches

# test obj - not currently in use

# test obj - in use

# timers

# conditions

# results

# warnings

# machines

# Creatures
cecily = Creature('cecily', 'Cecily', 'cecily', 'cecily', None,
		None, [], [brass_key], [], [hand],
		[],
		{},
		True,
		{}, 90, 90)

# *** Rooms ***
pub = Room('pub', 'Pub', "pub", 'pub', None, [],
		[cecily], [])

unreachable_1 = Room('unreachable_1', 'Unreachable', 'unreachable_1', 'unreachable_1', None, [], 
		[], [])


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
			{'room_x' : pub, 'dir_x' : 'south', 'door' : creaky_door, 'dir_y' : None, 'room_y' : unreachable_1},
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
master_obj_lst = [gs, rusty_key, brass_key, cecily, cursive, block_text, hand, dingy_shelf, tea, comfy_chair, creaky_door, pub, unreachable_1] # note: big_bomb & test_frog removed; glass_bottle removed

# list written to pickle
with open('/Users/tas/Documents/Python/dark_castle3/cleesh/games/cup_of_tea/game_file/game_pkl', 'wb') as f:
	pickle.dump(master_obj_lst, f)




