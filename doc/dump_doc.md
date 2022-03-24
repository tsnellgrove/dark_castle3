Dark Castle v3
Dump Doc
Mar 24, 2022

This file holds documentation ideas that were overruled but are being retained in case they later prove useful. This file mostly exists because I hate deleting data of any kind ;-D


****************
*** 20220324 ***
****************

*** Methods Psuedo Code ***

- Unique Attributes v1 (Legacy):
	- creature_state
		(Goblin = None)
	- mach_obj_lst
		(for Goblin: attack if player interacts with room obj, watch player with malicious glare each turn in room; For Hedgehog: attack_warning)
	- show_item_lst
	- show_response_lst
		(Goblin is scared of sword; critical of all else)
	- give_items_lst
	- give_response_lst 
		[should be list of lists of text response and barter item]
		(CANCEL: Goblin "confiscates" all given items in a suspicious fashion)
	- attack_win_lst (weapon_lst, result code, resutl text)
	- attack_tie_lst (weapon_lst, result code, result text)
	- attack_lose_lst (weapon_lst, result code, result text)
		- weapon_lst : Fist, Sword, Axe, Other_Item
		- result_code : 'creature_flee', 'creature_death', 'burt_death', None
		- result_text : description of result
	- creature_items_lst (e.g. Note and Axe for Goblin, Key for Hedgehog)

- Show: 
	if obj in creature.show_item_list: 
		buffer creature.show_response_lst[item_index]
	else:
		buffer("the <creature> is not interested in the <item>")


- Goblin Pseudo Code:
	- On examine of Goblin - maybe some mention of Nana talking about Goblin Guard

- flow chart Goblin interaction

- introduce pre-built "warning" machine? use for 'go south', 'attack hedgehog', 'lift heavy rock', etc
	- or maybe bake warning into 'attack method'

- for attack warning
	- attack_warning (boolean)
	- attack_warning_index
	- attack_warning_lst

- creatures = pre-action trigger, post-action trigger, pre-action auto, post-action auto

- a Creature is a collection of VewOnlyMach objs that enable it to respond to show, give, attack, and other stimuli
- Creatures should be no more complex than necessary
	- so when a specific creature need is met but a new creature behanvior will arrise =>
		- it may make sense to 'swap' in a 'new' creature of the same name
		- (e.g. hedgehog1 == hungry_guard, hedgehog2 == trader
		- presumably creature swap also happens via machine?

### Creature Class ###
### Switch Classes (button & lever) ###

More ideas on Creatures:
- Treat creatures like roving conditional events
- Wrapper checks for presence of creature in room and checks for conditionals against creature too

Key Creature Verbs (methods):
- show, give, attack

- Creature Machines
	- how does goblin attack Burt??
		- attack_src_dict
			{burt_weapon, result_code, result_text_key}
			(will need to implement default weapon code)
		- NEW IDEA: maybe an attack_burt method???

*** Open Thoughts ***
should item lists be changed once an item is given? Maybe doesn't matter since there are no duplicates... and even if there were 2x Biscuits... the point would be for the hedgehog to want to eat them again? So maybe creature_state doesn't really matter for show()? And maybe give() only needs to update creature_descript?
