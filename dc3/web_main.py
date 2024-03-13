# program: dark castle v3.83
# name: Tom Snellgrove
# date: Mar 13, 2024
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		modularized machines, and replicate full original.

### import statements
import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')
from dc3.app_main.app_main import app_main

### main routine
is_end = False
is_start = True
user_input = ""
while not is_end:
	if not is_start:
		user_input = input('Type your command: ')
	is_start, is_end, user_output = app_main(user_input, is_start)
	print(user_output)
print("THANKS FOR PLAYING!!")



