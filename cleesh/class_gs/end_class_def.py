# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for end sub-class

### import ###
import math
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class End(Invisible):
    def __init__(self, name, is_end, game_ending):
        super().__init__(name)
        self._is_end = is_end # bool indicating whether or not the game has ended
        self._game_ending = game_ending # type of ending; includes punct ('won!', 'quit.', 'died', or 'restarted.')
        """ The End class inherits from Invisible. It holds the is_end and game_ending attribs to determine
        if and how the game has ended. And the disp_end() method to display the end state to the player.
		"""

	### setters & getters ###
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
    def disp_end(self, gs):
        title_factor = gs.io.get_str_nr('title_factor')
        if gs.score.score < 0:
            title_score = -title_factor
        elif gs.score.score == 0:
            title_score = 0
        else:
            title_score = math.ceil(gs.score.score / title_factor) * title_factor
        title = gs.io.get_dict_val('titles_by_score', title_score)

        gs.io.buffer(f"You have {self.game_ending}")
        gs.io.buffer("Your adventure ended after " + str(gs.core.move_count) + " moves.")
        gs.score.print_score(gs)
        gs.io.buffer("Your title is: " + title)
        if self.game_ending == 'won!':
            gs.io.buff_e('credits')

        return