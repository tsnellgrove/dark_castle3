# program: dark castle v3.80
# name: Tom Snellgrove
# date: Jan 7, 2024
# description: class deffinition module for score sub-class

### import


### classes
class Score(object):
	def __init__(self, name):
		self._name = name # name of obj

	### setters & getters ###
	@property
	def name(self):
		return self._name

    ### score methods ###
def get_score(self, gs):
        room_obj = gs.map.get_hero_rm(gs)
        creature = gs.hero

        # increment item scores
        for score_key in gs.io.get_lst('item_score_lst'):
            if (not creature.hand_is_empty() and creature.get_hand_item().name == score_key
                    and gs.get_points_earned_state(score_key) == False):
                points = gs.io.get_dict_val('score_val', score_key)
                gs.update_score(points)
                gs.set_points_earned_state(score_key, True)
                gs.print_score()

        # increment worn scores
        for score_key in gs.io.get_lst('worn_score_lst'):
            worn_lst = creature.worn_lst
            if len(worn_lst) > 0:
                for garment in worn_lst:
                    if (garment.name == score_key and gs.get_points_earned_state(score_key) == False):
                        points = gs.io.get_dict_val('score_val', score_key)
                        gs.update_score(points)
                        gs.set_points_earned_state(score_key, True)
                        gs.print_score()

        # increment room scores
        for score_key in gs.io.get_lst('room_score_lst'):
            if (room_obj.name == score_key and gs.get_points_earned_state(score_key) == False):
                points = gs.io.get_dict_val('score_val', score_key)
                gs.update_score(points)
                gs.set_points_earned_state(score_key, True)
                gs.print_score()

        # custom scoring
        score_key = 'hedgehog_attack'
        if (not gs.map.chk_name_exist('royal_hedgehog') and gs.get_points_earned_state(score_key) == False):
            points = gs.io.get_dict_val('score_val', score_key)
            gs.update_score(points)
            gs.set_points_earned_state(score_key, True)
            gs.print_score()

        score_key = 'goblin_dead'
        if (gs.map.chk_name_exist('dead_goblin') and gs.get_points_earned_state(score_key) == False):
            points = gs.io.get_dict_val('score_val', score_key)
            gs.update_score(points)
            gs.set_points_earned_state(score_key, True)
            gs.print_score()

        score_key = 'game_won'
        game_ending = gs.get_game_ending()
        if game_ending == 'won':
            points = gs.io.get_dict_val('score_val', score_key)
            gs.update_score(points)

        return