# program: dark castle
# author: Tom Snellgrove
# module description: assign game session variables

### import statements
import random

### main routine
def game_session_vars(gs):
	portcullis_code = random.randint(0, 7)
	port_code_txt = f"'..ode is {str(portcullis_code)}. Don't tell anyo..'"
	gs.io.set_dyn_dict('messy_handwriting', port_code_txt)
	gs.core.get_str_to_obj_dict('control_panel').mach_state = portcullis_code
	return

