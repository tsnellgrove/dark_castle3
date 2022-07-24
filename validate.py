# program: dark castle v3.70
# name: Tom Snellgrove
# date: July 24, 2022
# description: module to validate user_input


### import statements ###
import random
from static_gbl import descript_dict, static_dict

def rand_error():
		num = random.randint(0, 4)
		interp_error_key = 'interp_error_' + str(num)
		return descript_dict[interp_error_key]

### *** make error dict local?? ***

def validate(active_gs, case, word_lst):
		input_valid = True
		if case == 'error':
				input_valid = False
				if word_lst[0] == "random error":
						output = rand_error()
				else:
						output = word_lst[0]
				active_gs.buffer(output)

		return input_valid
