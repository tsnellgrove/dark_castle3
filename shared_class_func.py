# program: dark castle v3.56
# name: Tom Snellgrove
# date: Dec 31, 2021
# description: class deffinition module for GameState


### imports


### shared class functions
def obj_lst_to_str(obj_lst):
		if not isinstance(obj_lst, list):
				raise ValueError("is not a list")
		elif len(obj_lst) == 0:
				lst_str = "nothing"
		else:
				lst_str = ""
				for obj in obj_lst:
						lst_str = lst_str + obj.full_name + ", "
				lst_str = lst_str[:-2]
		return lst_str
