# program: cleesh game engine
# version: 3.8.0 (build 0001)
# author: Tom Snellgrove
# date: Jun 12, 2024
# description: web main module for a zork-like text adventure game.
# goals vs. dc2: oop, modular, improved interpreter, working containers, 
#		modularized machines, and replicate full original.

### import statements
import sys
sys.path.append('/Users/tas/Documents/Python/dark_castle3')
from cleesh.app_main.app_main import app_main
from cleesh.app_main.start_up import start_me_up
from cleesh.app_main.game_menu import print_game_menu
from cleesh.app_main.file_io import save_game, restore_game

#local functions
def confirm_choice(user_input, warn_str):
	is_confirm = True
	user_output = ""
	confirm_input = input("\n" + warn_str + ' (Y / N): ')
	if confirm_input.lower() not in ['y', 'yes']:
		user_output = f"\n{user_input.capitalize()} aborted.\n"
		is_confirm = False
	return user_output, is_confirm

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
				user_output = start_me_up(game_name)
				is_start = False
				call_app_main = False
			else:
				user_input = input('Type your command: ')
				call_app_main = True
			if user_input.lower() in ['q', 'quit', 'restart']:
			# for 'q' / 'restart', after confirm_choice(), still need to pass to app_main to get score
				if user_input.lower() == 'q':
					user_input = 'quit'
				user_output, is_confirm = confirm_choice(user_input, 'Are you sure you want to leave?')
				if not is_confirm:
					call_app_main = False
			if user_input.lower() in ['save']:
				user_output, is_confirm = confirm_choice(user_input, 'Save overwrites old save. Confirm?')
				if is_confirm:
					user_output = save_game(game_name)
				call_app_main = False
			if user_input.lower() in ['restore']:
				user_output, is_confirm = confirm_choice(user_input, 'Restore overwrites current game. Confirm?')
				if is_confirm:
					user_output = restore_game(game_name)
				call_app_main = False
			if call_app_main:
				is_start, is_end, user_output = app_main(user_input, game_name)
			print(user_output)
			if user_input.lower() == 'restart'and is_confirm:
				any_key = input("Press Enter to continue: ")
		print("THANKS FOR PLAYING!!")
		print()
		any_key = input("Press Enter To Return To The Game Menu: ")
print("GOODBYE!")
