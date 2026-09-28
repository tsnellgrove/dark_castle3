# program: cleesh
# author: Tom Snellgrove
# module description: performs hand management functions prior to execution functions


### import statements ###


### main routines ###

def hand_mgmt(case, word_lst, gs):
    verb_str = word_lst[0]
    if verb_str in ['wear', 'stow','drop', 'eat', 'put', 'show', 'give'] and not gs.core.hero.chk_in_hand(word_lst[1]):
        do_noun_obj = word_lst[1]
        if gs.core.hero.chk_in_bkpk(do_noun_obj) and verb_str not in ['stow']:
            gs.core.hero.put_in_hand(do_noun_obj, gs)
            gs.core.hero.bkpk_lst_remove(do_noun_obj)
        elif gs.core.hero.chk_is_worn(do_noun_obj) and verb_str not in ['wear']:
            gs.core.hero.put_in_hand(do_noun_obj, gs)
            gs.core.hero.worn_lst_remove(do_noun_obj)
            gs.io.buffer(f"(Removing the {do_noun_obj.full_name} first)")
            gs.io.buff_s(f"{gs.core.hero.name}_remove_{do_noun_obj.descript_key}")

    elif verb_str in ['attack', 'lock', 'unlock', 'drink'] and not gs.core.hero.chk_in_hand(word_lst[3]):
        id_noun_obj = word_lst[3]
        if gs.core.hero.chk_in_bkpk(id_noun_obj):
            gs.core.hero.put_in_hand(id_noun_obj, gs)
            gs.core.hero.bkpk_lst_remove(id_noun_obj)
        elif gs.core.hero.chk_is_worn(id_noun_obj):
            gs.core.hero.put_in_hand(id_noun_obj, gs)
            gs.core.hero.worn_lst_remove(id_noun_obj)
            gs.io.buffer(f"(Removing the {id_noun_obj.full_name} first)")
            gs.io.buff_s(f"{gs.core.hero.name}_remove_{id_noun_obj.descript_key}")

# CONSOLIDATE INTO SINGLE FUNCTION - W/ hand_mgmt_verb_lst and noun_obj based on word_lst[-1]


##    if verb_str in ['wear', 'drop', 'eat'] and not gs.core.hero.chk_in_hand(word_lst[1]) and gs.core.hero.chk_in_bkpk(word_lst[1]):
#    if verb_str in ['wear', 'drop', 'eat', 'put', 'show', 'give'] and not gs.core.hero.chk_in_hand(word_lst[1]) and gs.core.hero.chk_in_bkpk(word_lst[1]):
#        do_noun_obj = word_lst[1]
#        gs.core.hero.put_in_hand(do_noun_obj, gs)
#        gs.core.hero.bkpk_lst_remove(do_noun_obj)
##    if verb_str in ['drop', 'eat', 'stow'] and not gs.core.hero.chk_in_hand(word_lst[1]) and gs.core.hero.chk_is_worn(word_lst[1]):
#    elif verb_str in ['drop', 'eat', 'stow', 'put', 'show', 'give'] and not gs.core.hero.chk_in_hand(word_lst[1]) and gs.core.hero.chk_is_worn(word_lst[1]):
#        do_noun_obj = word_lst[1]
#        gs.core.hero.put_in_hand(do_noun_obj, gs)
#        gs.core.hero.worn_lst_remove(do_noun_obj)
#        gs.io.buffer(f"(Removing the {do_noun_obj.full_name} first)")
#        gs.io.buff_s(f"{gs.core.hero.name}_remove_{do_noun_obj.descript_key}")





    return