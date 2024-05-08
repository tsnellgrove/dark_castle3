# program: dark castle
# version: 3.84
# author: Tom Snellgrove
# date: Mar 31, 2024
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		modularized machines, and replicate full original.

### import statements
import sys
from importlib import import_module
sys.path.append('/Users/tas/Documents/Python/dark_castle3')
# from cleesh.games.dark_castle.game_file.start_up import start_me_up
from cleesh.app_main.app_main import app_main
from cleesh.app_main.game_menu import print_game_menu

# initialize menu variables
user_choice = ""
user_num = 0

# game print game menu and get user choice
while True:
	max_num, game_lst = print_game_menu()
	user_choice = input("Type the number of the game you want to play or type 'Q' to quit: ")
	if user_choice.strip() == 'q' or user_choice.strip() == 'Q':
		break
	try:
		user_num = int(user_choice)
	except:
		user_num = 0
	if user_num > 0 and user_num <= max_num:
		
		# initialize game variables
		game_name = game_lst[user_num - 1]
		is_end = False
		is_start = True
		call_app_main = True

		# game routine
		while not is_end:
			if is_start:
				user_input = ""
				import_str = f"cleesh.games.{game_name}.game_file.start_up"
				user_output = import_module(import_str).start_me_up()
#				user_output = start_me_up()
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
