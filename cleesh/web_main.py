# program: dark castle
# version: 3.84
# author: Tom Snellgrove
# date: Mar 31, 2024
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		modularized machines, and replicate full original.

### import statements
import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')
from cleesh.app_main.start_up import start_me_up
from cleesh.app_main.app_main import app_main
from cleesh.data.static_gbl import engine_static_dict

### initialize local variables
user_choice = ""
user_num = 0

is_end = False
is_start = True
call_app_main = True

# game choice routine
while str(user_choice).lower != 'q':
	print("Game List:")
	game_lst = engine_static_dict['game_lst']
	print(game_lst)
	user_choice = input("Type the number of the game you want to play or type 'Q' to quit:")
	max_num = len(game_lst)
	user_num = int(user_choice)
#	if str(user_choice).lower != 'q' and user_choice > 0 and user_choice <= max_num and isinstance(user_choice, int):
	if user_num > 0 and user_num <= max_num and isinstance(user_num, int):
		
		# in-game routine
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

print("GOODBYE!")

