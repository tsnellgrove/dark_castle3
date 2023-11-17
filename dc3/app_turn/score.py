# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: updates score based on post-command execution game state


### import statements
from dc3.data.static_gbl import descript_dict

### score dictionaries and lists ###

worn_score_lst = [
	'royal_crown'
]

room_score_lst = [
	'main_hall',
	'throne_room'
]

def score(active_gs):
	room_obj = active_gs.get_room()
	creature = active_gs.hero

	# increment item scores
	for score_key in descript_dict['item_score_lst']:
		if (not creature.hand_is_empty() and creature.get_hand_item().name == score_key
				and active_gs.get_points_earned_state(score_key) == False):
			points = descript_dict['score_val'][score_key]
			active_gs.update_score(points)
			active_gs.set_points_earned_state(score_key, True)
			active_gs.print_score()

	# increment worn scores
	for score_key in worn_score_lst:
		worn_lst = creature.worn_lst
		if len(worn_lst) > 0:
			for garment in worn_lst:
				if (garment.name == score_key and active_gs.get_points_earned_state(score_key) == False):
					points = descript_dict['score_val'][score_key]
					active_gs.update_score(points)
					active_gs.set_points_earned_state(score_key, True)
					active_gs.print_score()

	# increment room scores
	for score_key in room_score_lst:
		if (room_obj.name == score_key and active_gs.get_points_earned_state(score_key) == False):
			points = descript_dict['score_val'][score_key]
			active_gs.update_score(points)
			active_gs.set_points_earned_state(score_key, True)
			active_gs.print_score()

	# custom scoring
	score_key = 'hedgehog_attack'
	if (not active_gs.map.chk_name_exist('royal_hedgehog') and active_gs.get_points_earned_state(score_key) == False):
		points = descript_dict['score_val'][score_key]
		active_gs.update_score(points)
		active_gs.set_points_earned_state(score_key, True)
		active_gs.print_score()

	score_key = 'goblin_dead'
	if (active_gs.map.chk_name_exist('dead_goblin') and active_gs.get_points_earned_state(score_key) == False):
		points = descript_dict['score_val'][score_key]
		active_gs.update_score(points)
		active_gs.set_points_earned_state(score_key, True)
		active_gs.print_score()

	score_key = 'game_won'
	game_ending = active_gs.get_game_ending()
	if game_ending == 'won':
		points = descript_dict['score_val'][score_key]
		active_gs.update_score(points)

	return
