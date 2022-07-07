# program: dark castle v3.68
# name: Tom Snellgrove
# date: July 7, 2021
# description: presents end of game text 


### imports ###
import math
from static_gbl import descript_dict

titles_dict = {
		-10: 'Burt the Best Forgotten',
		0: 'Burt the Boneheaded',
		10: 'Burt the Beginner',
		20: 'Burt the Better Than Average',
		30: 'Burt the Brawny',
		40: 'Burt the Brainy',
		50: 'Burt the Benevolent',
		60: 'Burt the Breathtaking',
		70: 'Burt the Bodacious',
		80: 'Burt the Bold, King of Bright Castle'
}

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
		title = titles_dict[title_score]

		if game_ending == 'death':
				active_gs.buffer("You have died.")
		elif game_ending == 'quit':
				active_gs.buffer("You have quit.")
		elif game_ending == 'won':
				active_gs.buffer("You have won!")

		active_gs.buffer("Your adventure ended after " + str(moves) + " moves.")
		active_gs.print_score()
		active_gs.buffer("Your title is: " + title)
		if game_ending == 'won':
				active_gs.buffer(descript_dict['credits'])
		active_gs.set_end_of_game(True)

		return
