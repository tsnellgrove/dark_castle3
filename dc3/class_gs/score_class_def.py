# program: dark castle v3.80
# name: Tom Snellgrove
# date: Jan 7, 2024
# description: class deffinition module for score sub-class

### import


### classes
class Score(object):
    def __init__(self, name, points_earned_dict):
        self._name = name # name of obj
        self._points_earned_dict = points_earned_dict # which points has the player already earned?

	### setters & getters ###
    @property
    def name(self):
        return self._name

    def get_points_earned_state(self, score_key):
        if score_key not in self._points_earned_dict:
            raise KeyError("key does not exist in dict")
        else:
            return self._points_earned_dict[score_key]

    def set_points_earned_state(self, score_key, value):
        if score_key not in self._points_earned_dict:
            raise KeyError("key does not exist in dict")
        else:
            self._points_earned_dict[score_key] = value

    ### score methods ###
    def print_points(self, gs, score_key):
        points = gs.io.get_dict_val('score_val', score_key)
        gs.update_score(points)
        self.set_points_earned_state(score_key, True)
        gs.print_score()

    def get_score(self, gs):
        room_obj = gs.map.get_hero_rm(gs)
        creature = gs.hero

        # increment item scores
        for score_key in gs.io.get_lst('item_score_lst'):
            if (not creature.hand_is_empty() and creature.get_hand_item().name == score_key
                    and self.get_points_earned_state(score_key) == False):
                self.print_points(gs, score_key)

        # increment worn scores
        for score_key in gs.io.get_lst('worn_score_lst'):
            worn_lst = creature.worn_lst
            if len(worn_lst) > 0:
                for garment in worn_lst:
                    if (garment.name == score_key and self.get_points_earned_state(score_key) == False):
                        self.print_points(gs, score_key)

        # increment room scores
        for score_key in gs.io.get_lst('room_score_lst'):
            if (room_obj.name == score_key and self.get_points_earned_state(score_key) == False):
                self.print_points(gs, score_key)

        # obj not in game scores
        for score_key in gs.io.get_lst('obj_in_game_lst'):
            if (not gs.map.chk_name_exist(score_key) and self.get_points_earned_state(score_key) == False):
                self.print_points(gs, score_key)

        score_key = 'game_won'
        game_ending = gs.get_game_ending()
        if game_ending == 'won':
            points = gs.io.get_dict_val('score_val', score_key)
            gs.update_score(points)

        return
    