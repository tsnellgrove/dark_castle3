# program: dark castle v3.81
# name: Tom Snellgrove
# date: Feb 11, 2024
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		integrate triggers, replicate full original, add more puzzles!

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
	is_end, user_output = app_main(user_input, is_start)
	is_start = False
	print(user_output)
	if user_output == "\nRestarting...\n":
		is_start = True
print("THANKS FOR PLAYING!!")



