# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: class deffinition module for end sub-class

### import
import math

### classes
class End(object):
    def __init__(self, name, is_end, game_ending):
        self._name = name # name of obj
        self._is_end = is_end # bool indicating whether or not the game has ended
        self._game_ending = game_ending # string that indicates type of ending (e.g. 'won', 'quit', etc.)

	### setters & getters ###
    @property
    def name(self):
        return self._name

    @property
    def is_end(self):
        return self._is_end

    @is_end.setter
    def is_end(self, new_val):
        self._is_end = new_val

    @property
    def game_ending(self):
        return self._game_ending
    
    @game_ending.setter
    def game_ending(self, new_val):
        self._game_ending = new_val

    ### end methods ###
#    def end(self, gs):
    def disp_end(self, gs):
        self.is_end = True

        if gs.score.score < 0:
            title_score = -10
        elif gs.score.score == 0:
            title_score = 0
        else:
            title_score = math.ceil(gs.score.score / 10) * 10
        title = gs.io.get_dict_val('titles_by_score', title_score)

        if self.game_ending == 'death':
            gs.io.buffer("You have died.")
        elif self.game_ending == 'quit':
            gs.io.buffer("You have quit.")
        elif self.game_ending == 'won':
            gs.io.buffer("You have won!")

        gs.io.buffer("Your adventure ended after " + str(gs._state_dict['move_counter']) + " moves.")
        gs.score.print_score(gs)
        gs.io.buffer("Your title is: " + title)
        if self.game_ending == 'won':
            gs.io.buff_e('credits')

        return