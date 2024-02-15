# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: class deffinition module for end sub-class

### import


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

