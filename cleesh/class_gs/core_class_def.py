# program: dark castle
# author: Tom Snellgrove
# module description: class deffinition module for core sub-class

### import ###
from cleesh.class_std.invisible_class_def import Invisible


### classes ###
class Core(Invisible):
#    def __init__(self, name, hero, hero_descript_count, move_count, is_debug, str_to_obj_dict, has_session_vars, univ_invis_lst):
    def __init__(self, name, hero, hero_descript_pct, move_count, is_debug, str_to_obj_dict, has_session_vars, univ_invis_lst):
        super().__init__(name)
        self._hero = hero # the Creature class object that is the hero of the game
#        self._hero_descript_count = hero_descript_count # tracks the number of descriptions available for the hero
        self._hero_descript_pct = hero_descript_pct # the percent of occassions a description is showin on inventory and examine
        self._move_count = move_count # tracks the number of valid moves made by the player
        self._is_debug = is_debug # a boolean that defines whether the game is in debug mode (default = False)
        self._str_to_obj_dict = str_to_obj_dict # dict that enables look-up of game obj via name str keys
        self._has_session_vars = has_session_vars # bool indicating whether session vars needed at start_up
        self._univ_invis_lst = univ_invis_lst # list of invisible obj always in scope; used for machines
        """ Core class inherits from Invisible. It holds a small number of essential attributes. 
        """

	### setters & getters ###
    @property
    def hero(self):
        return self._hero

#    @property
#    def hero_descript_count(self):
#        return self._hero_descript_count

    @property
    def hero_descript_pct(self):
        return self._hero_descript_pct

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

    @property
    def univ_invis_lst(self):
        return self._univ_invis_lst

	### methods ###
    def move_inc(self):
        self.move_count += 1

    def is_key_in_sto_dict(self, key):
        return key in self._str_to_obj_dict
