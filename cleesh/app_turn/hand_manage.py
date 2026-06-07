# program: cleesh
# author: Tom Snellgrove
# module description: performs hand management functions prior to execution functions


### import statements ###


### main routines ###

def hand_mgmt(case, word_lst, gs):
    verb_str = word_lst[0]
    # 'eat' to be added
    if verb_str in ['wear', 'drop'] and not gs.core.hero.chk_in_hand(word_lst[1]) and gs.core.hero.chk_in_bkpk(word_lst[1]):
        do_noun_obj = word_lst[1]
        gs.core.hero.put_in_hand(do_noun_obj, gs)
        gs.core.hero.bkpk_lst_remove(do_noun_obj)
    # 'stow', and 'eat' to be added
    if verb_str in ['drop'] and not gs.core.hero.chk_in_hand(word_lst[1]) and gs.core.hero.chk_is_worn(word_lst[1]):
        do_noun_obj = word_lst[1]
        gs.core.hero.put_in_hand(do_noun_obj, gs)
        gs.core.hero.worn_lst_remove(do_noun_obj)
        gs.io.buffer(f"(Removing the {do_noun_obj.full_name} first)")
        gs.io.buff_s(f"{gs.core.hero.name}_remove_{do_noun_obj.descript_key}")
    return