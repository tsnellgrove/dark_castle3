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

### initialize local variables
is_end = False
is_start = True
call_app_main = True

### main routine
while not is_end:
	if is_start:
		user_input = ""
		user_output = start_me_up()
		is_start = False
		call_app_main = False
	else:
		user_input = input('Type your command: ')
		call_app_main = True

	if user_input.lower() in ['q', 'quit', 'restart']:
		cmd_conf_input = input('Are you sure you want to leave? (Y / N): ')
		if cmd_conf_input.lower() not in ['y', 'yes']:
			user_output = "Thank goodness you reconsidered!"
			call_app_main = False

	if call_app_main:
		is_start, is_end, user_output = app_main(user_input)

	print(user_output)
print("THANKS FOR PLAYING!!")


