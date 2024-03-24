# program: dark castle
# version: 3.83
# author: Tom Snellgrove
# date: Mar 13, 2024
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		modularized machines, and replicate full original.

### import statements
import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')
from dc3.app_main.start_up import start_me_up
from dc3.app_main.app_main import app_main

### main routine
is_end = False
is_start = True
user_input = ""
while not is_end:
	if is_start:
		user_output = start_me_up()
		is_start = False
	else:
		user_input = input('Type your command: ')
		is_start, is_end, user_output = app_main(user_input, is_start)
#	if not is_start:
#		user_input = input('Type your command: ')
#	is_start, is_end, user_output = app_main(user_input, is_start)
	print(user_output)
print("THANKS FOR PLAYING!!")


#	if is_start == True:
#		user_output = start_me_up()
#		return False, False, user_output


