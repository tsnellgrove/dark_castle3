# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		integrate triggers, replicate full original, add more puzzles!

### import statements
import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')
from dc3.app_main.app_main import app_main

### main routine
end_of_game = False
start_of_game = True
while not end_of_game:
	if start_of_game:
		user_input = "xyzzy42"
		start_of_game = False
	else:
		user_input = input('Type your command: ')
	end_of_game, user_output = app_main(user_input)
	print(user_output)
	if user_output == "\nRestarting...\n":
		start_of_game = True
print("THANKS FOR PLAYING!!")



