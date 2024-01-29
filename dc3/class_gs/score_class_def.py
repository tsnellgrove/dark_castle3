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
    def chk_pts_earned(self, score_key):
        if score_key in self.pts_earned_lst:
            return True
        return False

    def set_pts_earned(self, score_key):
        self.pts_earned_lst.append(score_key)
        return

    def get_max_score(self, gs):
        max_score = 0
        for verb in gs.io.get_dict('score_dict'):
            for nouns_key in gs.io.get_dict('score_dict')[verb]:
                if gs.io.get_dict('score_dict')[verb][nouns_key] > 0:
                    max_score += gs.io.get_dict('score_dict')[verb][nouns_key] # fix with io getter
        max_score += 25 # temp correction for 'attack', 'give', and win_mach
        return max_score

    def print_score(self, gs):
        output1 = ("Your score is now " + str(self.score))
##        output2 = (" out of " + str(gs.io.get_str_nr('max_score')))
        output2 = (" out of " + str(self.get_max_score(gs)))
        gs.io.buffer(output1 + output2)

    def print_points(self, gs, score_key):
        self.score += gs.io.get_dict_val('score_val', score_key)
        self.set_pts_earned(score_key)
        self.print_score(gs)


    def disp_score(self, verb_str, noun_str, driobj_str, gs):
##        print(noun_str)
        if noun_str in gs.score.pts_earned_lst:
            return
        if verb_str not in gs.io.get_dict('score_dict'):
            return
        if driobj_str == None:
            nouns_key = noun_str
        else:
            nouns_key = (noun_str, driobj_str)
        if nouns_key in gs.io.get_dict_val('score_dict', verb_str):
                self.score += gs.io.get_dict('score_dict')[verb_str][nouns_key] # fix w/ getter!
                self.set_pts_earned(noun_str)
                self.print_score(gs)
##            print(verb_str)
##            print(noun_str)
##            print(driobj_str)
        return


    def check_score(self, gs):
        room_obj = gs.map.get_hero_rm(gs)
        creature = gs.hero

        # increment item scores

        # obj not in game scores
        for score_key in gs.io.get_lst('obj_in_game_lst'):
            if (not gs.map.chk_name_exist(score_key) and not self.chk_pts_earned(score_key)):
                self.print_points(gs, score_key)

        score_key = 'game_won'
        game_ending = gs.get_game_ending()
        if game_ending == 'won':
            self.score += gs.io.get_dict_val('score_val', score_key)

        return
    