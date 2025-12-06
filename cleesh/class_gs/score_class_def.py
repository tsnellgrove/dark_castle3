# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for score sub-class

### import ###
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class Score(Invisible):
    def __init__(self, name, score, pts_earned_lst):
        super().__init__(name)
        self._score = score # current player score
        self._pts_earned_lst = pts_earned_lst # which points has the player already earned?
        """ Score class inherits from Invisible. It contains the attribs to track the player's current
        score and which scoring events the player has already achieved. And the disp_score() method 
        which calculates and displays score updates.
		"""

	### setters & getters ###
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
    def print_score(self, gs):
        output1 = ("Your score is now " + str(self.score))
        output2 = (" out of " + str(gs.io.get_str_nr('max_score')))
        gs.io.buffer(output1 + output2)

    def disp_score(self, verb_str, noun_str, dirobj_str, gs, suppress_display=False):
        if verb_str not in gs.io.get_dict('score_dict'):
            return
        # determine whether dirobj_key is standard or wildcard
        dirobj_key = dirobj_str
        subj_key = (noun_str, dirobj_key)
        if subj_key not in gs.io.get_dict_val('score_dict', verb_str):
            dirobj_key = '*'
            subj_key = (noun_str, dirobj_key)
        if subj_key not in gs.io.get_dict_val('score_dict', verb_str):
            return
        # have the points for this score condition already been earned?
        if (verb_str, noun_str, dirobj_key) in gs.score.pts_earned_lst:
            return
        # variable outcome verb special cases
        if verb_str == 'attack' and gs.map.chk_obj_exist(gs.core.get_str_to_obj_dict(noun_str), gs):
            return
        if verb_str == 'give' and not gs.core.get_str_to_obj_dict(noun_str).chk_contain_item(gs.core.get_str_to_obj_dict(dirobj_str)):
            return
        # score condition is valid
        self.score += gs.io.get_ddict_val('score_dict', verb_str, subj_key)
        self.pts_earned_lst.append((verb_str, noun_str, dirobj_key))
        if not suppress_display:
            self.print_score(gs)
        return    