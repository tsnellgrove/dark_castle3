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
    def get_max_score(self, gs):
        max_score = 0
        for verb in gs.io.get_dict('score_dict'):
            for nouns_key in gs.io.get_dict('score_dict')[verb]:
                if gs.io.get_dict('score_dict')[verb][nouns_key] > 0:
                    max_score += gs.io.get_dict('score_dict')[verb][nouns_key] # fix with io getter
        return max_score

    def print_score(self, gs):
        output1 = ("Your score is now " + str(self.score))
        output2 = (" out of " + str(self.get_max_score(gs)))
        gs.io.buffer(output1 + output2)

    def disp_score(self, verb_str, noun_str, driobj_str, gs):
        if (verb_str,noun_str,driobj_str) in gs.score.pts_earned_lst:
            return
        if verb_str not in gs.io.get_dict('score_dict'):
            return
        if driobj_str == None:
            subj_key = noun_str
        else:
            subj_key = (noun_str, driobj_str)
        if subj_key in gs.io.get_dict_val('score_dict', verb_str):
                self.score += gs.io.get_dict('score_dict')[verb_str][subj_key] # fix w/ getter!
                self.pts_earned_lst.append((verb_str,noun_str,driobj_str))
                self.print_score(gs)
        return    