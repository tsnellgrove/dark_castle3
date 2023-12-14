# program: dark castle v3.79
# name: Tom Snellgrove
# date: Oct 31, 2023
# description: presents end of game text 


### imports ###
import math
from dc3.data.static_gbl import static_dict


### end routine ###
def end(active_gs):
	moves = active_gs._state_dict['move_counter']
	game_ending = active_gs.get_game_ending()
	score = active_gs.get_score()

	if score < 0:
		title_score = -10
	elif score == 0:
		title_score = 0
	else:
		title_score = math.ceil(score / 10) * 10
	title = active_gs.io.get_dict_val('titles_by_score', title_score)

	if game_ending == 'death':
		active_gs.io.buffer("You have died.")
	elif game_ending == 'quit':
		active_gs.io.buffer("You have quit.")
	elif game_ending == 'won':
		active_gs.io.buffer("You have won!")

	active_gs.io.buffer("Your adventure ended after " + str(moves) + " moves.")
	active_gs.print_score()
	active_gs.io.buffer("Your title is: " + title)
	if game_ending == 'won':
		active_gs.io.buff_e('credits')
	active_gs.set_end_of_game(True)

	return
