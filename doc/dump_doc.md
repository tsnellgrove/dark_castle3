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


*** Refactoring Advice ***

- Function Design:
1) provide 'None' option for class attributes
2) provide 'match_value' for Conditions & Results

- Variable Assignment:
9) MOVE ASSIGNEMENTS CLOSER TO USAGE!! I need this one!!
15) return the conditional comparison itself! I do this now but my old code needs updating!! Note - can force boolean value with bool() function

- Strings
26) Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}" '. Can also do math in string: 'print(f"{i} squared is {i*i}")'. I NEED TO MAKE THIS SWITCH!!!
27) Concatenate strings with '.join': 'lst_of_str = ["Hi", "Tom"] ;; my_str = " ".join(lst_of_str)' => "Hi Tom"

- If Statements:
3) Merge nested if statements with 'and'
7) can use an 'if expression' with 'condition' statement: 'x = 1 if condition else 2'
8) use 'if guard statements' to return false cases immediately at the top of the if-then chain; reduces indentation
16) if 'if-else' blocks contain duplicate execution, use an 'or' to combine them
17) replace multiple value comparisons with 'in list' - or better yet, 'in set' ... since sets have unique values... I need to learn more about sets...
29) Simplify if-statements with 'if x in [a, b, c]'. I think I already do this. (same as 17)

- For Loops:
4) use 'any' to return boolean rather than for-looping through lists
5) pull variable assignments out of loops unless the variable will change within the loop
6) consider removing 'inline variables' that are only used once... just return the assigned value... I am guilty of this one a lot... I like how it looks but should reconsider
13) replace 'for i in range(len(lst)): lst_item = lst[i]' with 'for i, lst_item in enumerate(lst):' ; enumerate gives you both index and value as 
a tupple... need to see if I can use this?
19) iterate with enumerate to get index & value (same as 13)
14) replace manual loop counters of lists with enumerate... provides index and value... I think I am guilty of this in my Conditions / Results match-up

- Lists:
10) SIMPLIFY SEQUENCE CHECKS! don't need to check for if len(lst) > 0: ;; just use if lst:
11) When possible, declare a list with intended values... don't declare an empty list and then populate with append
20) use list comprehension: 'squares = [i*i for i in range(10)]'
21) sort complex iterables with sorted() functions: 'sorted_data = sorted(data)'
22) sort unique value with set();  sets are unordered and have unique values; can convert list to set: my_set = set(my_list)
25) Count 'hashable obj' w/ collectinos.Counter(). Need to import collections: 'counter = Counter(my_list)' => dict of unique list items as keys with number of occurences in list as values. 'print(counter(x))' returns number of occurences (0 if not in list). Can also: 'most_common = counter.most_common(1)' where argument tells how many most common values are desired => list of tupples. can call repeatedly to just get the number of occurences of the most common item.

- Dicts:
12) For cases where you need to reference both a dictionary's keys and their values: don't call values by keys manually... instead, use format 'for key, value in dict.items():' - I need to watch for this in my code - espeically older code
24) define default values in dicts with .get() and .setdefault(): 'count = my_dict.get("count", 0)' will return the default of '0' if there is no "count" key in my_dict; if there is no default it returns 'None';; Also, count = my_dict.setdefault("count", 0) will add "count" to my_dict with a value of 0
28) Merge dicts with {**d1, **d2}. if you have dict1 & dict 2, 'merged_dect = {**dict1, **dict2}' merges and eliminates duplicataes.

- Other:
18) learn more about 'yield' and 'yield from' for generators (only for very large data sets - I don't need this)
23) save memory with generators (for very large lists)

	
Learning Links:
- 1 & 2 = me
- 3 to 10 = https://youtu.be/rp1QR3eGI1k
- 11 to 18 = https://youtu.be/wd1JqBWm3lQ
- 19 - 29 = https://youtu.be/8OKTAedgFYg
- TBD: https://youtu.be/C-gEQdGVXbk
- TBD: https://youtu.be/KTIl1MugsSY (refactor starts about 7 min in)


