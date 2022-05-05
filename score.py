# program: dark castle v3.54
# name: Tom Snellgrove
# date: Dec 19, 2021
# description: updates score based on post-command execution game state


### import statements

### score dictionaries and lists ###
score_val_dict = {
		'rusty_key' : 5,
		'main_hall' : 10,
		'shiny_sword' : 10,
		'throne_room' : 10,
		'silver_key' : 5,
		'kinging_scroll' : 5,
		'royal_crown' : 10,
		'hedgehog_broach' : 5,
		'hedgehog_attack' : -20
}

item_score_lst = [
		'rusty_key',
		'shiny_sword',
		'silver_key',
		'kinging_scroll',
		'hedgehog_broach'
]

worn_score_lst = [
		'royal_crown'
]

room_score_lst = [
		'main_hall',
		'throne_room'
]

def score(active_gs):
		room_obj = active_gs.get_room()
		hand_lst = active_gs.get_hand_lst()

		# increment item scores
		for score_key in item_score_lst:
				if (not active_gs.hand_empty() and hand_lst[0].name == score_key
								and active_gs.get_points_earned_state(score_key) == False):
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						active_gs.print_score()

		# increment worn scores
		for score_key in worn_score_lst:
				worn_lst = active_gs.get_worn_lst()
				if len(worn_lst) > 0:
						for garment in worn_lst:
								if (garment.name == score_key
												and active_gs.get_points_earned_state(score_key) == False):
										points = score_val_dict[score_key]
										active_gs.update_score(points)
										active_gs.set_points_earned_state(score_key, True)
										active_gs.print_score()

		# increment room scores
		for score_key in room_score_lst:
				if (room_obj.name == score_key
								and active_gs.get_points_earned_state(score_key) == False):
						points = score_val_dict[score_key]
						active_gs.update_score(points)
						active_gs.set_points_earned_state(score_key, True)
						active_gs.print_score()

		# custom scoring
		score_key = 'hedgehog_attack'
		if (royal_hedgehog not in main_hall.room_obj_lst 
						and active_gs.get_points_earned_state(score_key) == False):
				points = score_val_dict[score_key]
				active_gs.update_score(points)
				active_gs.set_points_earned_state(score_key, True)
				active_gs.print_score()

		return
