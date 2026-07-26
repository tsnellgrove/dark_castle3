# program: dark castle
# author: Tom Snellgrove
# module description: executes meta commands


### import statements ###
import traceback

### execute commands based on case ###
def meta_cmd_exe(word_lst, gs):
    meta_cmd, arg, *_ = word_lst
    try:
        if meta_cmd == 'score':
            gs.score.print_score(gs)
        elif meta_cmd == 'version':
            gs.io.disp_version(gs)
        elif meta_cmd == 'credits':
            gs.io.buff_e('credits')
        elif meta_cmd == 'verbose':
            gs.io.set_verbosity_mode('verbose', gs)
        elif meta_cmd == 'brief':
            gs.io.set_verbosity_mode('brief', gs)
        elif meta_cmd == 'superbrief':
            gs.io.set_verbosity_mode('superbrief', gs)
        elif meta_cmd == 'rand_mode':
            gs.core.disp_rand_mode(gs)
        elif meta_cmd == 'debug':
            gs.core.set_debug_mode(arg, gs)
        gs.core.move_decr()
        return
    except Exception:
        gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)