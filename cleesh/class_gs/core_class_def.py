# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for core sub-class

### import ###
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class Core(Invisible):
    def __init__(self, name, hero, move_count, is_debug, str_to_obj_dict, has_session_vars):
        super().__init__(name)
        self._hero = hero # the Creature class object that is the hero of the game
        self._move_count = move_count # tracks the number of valid moves made by the player
        self._is_debug = is_debug # a boolean that defines whether the game is in debug mode (default = False)
        self._str_to_obj_dict = str_to_obj_dict # dict that enables look-up of game obj via name str keys
        self._has_session_vars = has_session_vars # bool indicating whether session vars needed at start_up
        """ Core class inherits from Invisible. It holds a small number of essential attributes. 
        """

	### setters & getters ###
    @property
    def hero(self):
        return self._hero

    @property
    def move_count(self):
        return self._move_count

    @move_count.setter
    def move_count(self, new_val):
        self._move_count = new_val

    @property
    def is_debug(self):
        return self._is_debug

    @is_debug.setter
    def is_debug(self, new_val):
        self._is_debug = new_val

    def get_str_to_obj_dict(self, key):
        return self._str_to_obj_dict[key]
    
    def set_str_to_obj_dict(self, key, value):
        self._str_to_obj_dict[key] = value

    @property
    def has_session_vars(self):
        return self._has_session_vars

	### methods ###
    def move_inc(self):
        self.move_count += 1

    def is_key_in_sto_dict(self, key):
        return key in self._str_to_obj_dict
