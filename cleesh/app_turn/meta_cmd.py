# program: dark castle
# author: Tom Snellgrove
# module description: executes meta commands


### import statements ###
import traceback

### execute commands based on case ###
def meta_cmd_exe(word_lst, gs):
    meta_cmd, *_ = word_lst
    try:
        if meta_cmd == 'score':
            gs.score.print_score(gs)
            return
        if meta_cmd == 'version':
            gs.io.disp_version(gs)
            return
        if meta_cmd == 'credits':
            gs.io.buff_e('credits')
            return
        if meta_cmd == 'verbose':
            gs.io.set_verbosity_mode('verbose', gs)
            return
        if meta_cmd == 'brief':
            gs.io.set_verbosity_mode('brief', gs)
            return
        if meta_cmd == 'superbrief':
            gs.io.set_verbosity_mode('superbrief', gs)
            return
    except Exception:
        gs.io.buff_dbg("[CMD] " + traceback.format_exc(), gs)