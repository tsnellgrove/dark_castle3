# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: presents end of game text 


### imports ###
import math


### end routine ###
def end(gs):
	moves = gs._state_dict['move_counter']
	game_ending = gs.get_game_ending()
	score = gs.get_score()

	if score < 0:
		title_score = -10
	elif score == 0:
		title_score = 0
	else:
		title_score = math.ceil(score / 10) * 10
	title = gs.io.get_dict_val('titles_by_score', title_score)

	if game_ending == 'death':
		gs.io.buffer("You have died.")
	elif game_ending == 'quit':
		gs.io.buffer("You have quit.")
	elif game_ending == 'won':
		gs.io.buffer("You have won!")

	gs.io.buffer("Your adventure ended after " + str(moves) + " moves.")
	gs.print_score()
	gs.io.buffer("Your title is: " + title)
	if game_ending == 'won':
		gs.io.buff_e('credits')
	gs.set_end_of_game(True)

	return
