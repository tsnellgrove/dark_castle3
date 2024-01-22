# program: dark castle v3.80
# name: Tom Snellgrove
# date: Jan 7, 2024
# description: class deffinition module for score sub-class

### import


### classes
class Score(object):
    def __init__(self, name, score, pts_earned_lst):
        self._name = name # name of obj
        self._score = score # current player score
        self._pts_earned_lst = pts_earned_lst # which points has the player already earned?

	### setters & getters ###
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score

    @property
    def pts_earned_lst(self):
        return self._pts_earned_lst
    
    @pts_earned_lst.setter
    def pts_earned_lst(self, new_lst):
        self._pts_earned_lst = new_lst

    ### score methods ###
#    def update_score(self, points):
#        self.score += points

    def chk_pts_earned(self, score_key):
        if score_key in self.pts_earned_lst:
            return True
        return False

    def set_pts_earned(self, score_key):
        self.pts_earned_lst.append(score_key)
        return

    def print_score(self, gs):
        output1 = ("Your score is now " + str(self.score))
        output2 = (" out of " + str(gs.io.get_str_nr('max_score')))
        gs.io.buffer(output1 + output2)

    def print_points(self, gs, score_key):
        points = gs.io.get_dict_val('score_val', score_key)
#        self.update_score(points)
        self.score += points
        self.set_pts_earned(score_key)
        self.print_score(gs)

    def check_score(self, gs):
        room_obj = gs.map.get_hero_rm(gs)
        creature = gs.hero

        # increment item scores
        for score_key in gs.io.get_lst('item_score_lst'):
            if (not creature.hand_is_empty() and creature.get_hand_item().name == score_key
                    and not self.chk_pts_earned(score_key)):
                self.print_points(gs, score_key)

        # increment worn scores
        for score_key in gs.io.get_lst('worn_score_lst'):
            worn_lst = creature.worn_lst
            if len(worn_lst) > 0:
                for garment in worn_lst:
                    if (garment.name == score_key and not self.chk_pts_earned(score_key)):
                        self.print_points(gs, score_key)

        # increment room scores
        for score_key in gs.io.get_lst('room_score_lst'):
            if (room_obj.name == score_key and not self.chk_pts_earned(score_key)):
                self.print_points(gs, score_key)

        # obj not in game scores
        for score_key in gs.io.get_lst('obj_in_game_lst'):
            if (not gs.map.chk_name_exist(score_key) and not self.chk_pts_earned(score_key)):
                self.print_points(gs, score_key)

        score_key = 'game_won'
        game_ending = gs.get_game_ending()
        if game_ending == 'won':
            points = gs.io.get_dict_val('score_val', score_key)
#            self.update_score(points)
            self.score += points

        return
    