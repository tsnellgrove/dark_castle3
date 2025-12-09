Coding Standards - Dark Castle v3

Feb 11, 2024

*** Need a new IDE ***
- iPad / offline: Pyto
- Mac Air / Offline: MS VSCode [CHOSEN]
- Cloud / Online: CodeAnyWhere, Cloud9 (AWS)
- Reference article: '5 ways to use Python on an iPad'


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl


*** List Comprehension vs. Generators ***
- List comprehension is used to act on a list but returns a list as long as the original
	- Relevant Link: https://stackoverflow.com/questions/16632124/how-to-emulate-sum-using-a-list-comprehension
- A generator can be used to reduce the values of a list to a single value
	- Example: sum(c.a for c in c_list)
	- Example Link: https://stackoverflow.com/questions/10879867/sum-average-an-attribute-of-a-list-of-objects


*** Inheritance & Method Extension ***
- This solution recommended at this stackoverflow link: https://stackoverflow.com/questions/51249310/attributeerror-super-object-has-no-attribute

## class Child(Parent):
##		def __init__(self): # <== THIS DIDN'T WORK FOR PortableLiquidContainer
##		super().__init__()   # no arguments is almost always best in Python 3 <== THIS DIDN'T WORK FOR PortableLiquidContainer either

##		def do_something(self, some_parameter, next_parameter):
##				super(Child, self).do_something(some_parameter, next_parameter) # name the current class <== BUT THIS WAS VITAL!!!
##				return some_parameter + next_parameter 


*** Recursion ***
- Good link on this topic: https://stackoverflow.com/questions/10544513/breaking-out-of-a-recursive-function
- pseudo code for recursion: https://stackoverflow.com/questions/65604019/how-to-return-true-or-false-using-recursive-function


Versioning:
	- IDEA: start using std versioning format: x.y.z (build #) => api.features.bug-fix (internal)
		- REF: https://softwareengineering.stackexchange.com/questions/368643/should-we-assign-version-numbers-for-internal-releases
	- IDEA: version cleesh engine separately from each game version


*** Var and Method Naming Conventions ***
- general:
	- use singular, not the pluaral form of words in variable names (e.g. use 'object_lst', not "objects_lst')
	- avoid the term 'scope' since there are different scopes for different actions... prefer terms like 'vis'
	- do NOT reference the class in the attribute - the attribute will always appear w/ the class: creature.state vs. creature.creature_state
	- do NOT attempt a rigorous and exhaustive naming convention - this way lies madness and very long vars. Embrace function context! 
	- be biased towards shorter vars; bend naming rules as needed to achieve shorter vars; shorter vars == more readable code!
	- use consistent attribute and method naming across classes whenever possible - especially classes that could be grouped together.
		- This approach allows for easy itteration across an amorphous list of objects.
- classes:
	- prefer generic naming for classes (e.g. Container and Surface vs. Chest and Shelf)
	- class attributes should be named after physical features of the class, NOT their expected data types: hand_lst, bkpk_lst, worn_lst
		- class data types can be grouped via methods whose naming denotes the data type: vis_lst, mach_lst
- attributes:
	- prefixes:
		- 'is' for bools
	- postfixes:
		- 'lst' for lists
		- 'dict' for dictionaries
		- 'str' for strings
		- do NOT use 'obj'; vars are assumed to be obj by default
			- If similar obj and non-obj vars appear in same function, diff the non-obj case: e.g. worn_lst vs. worn_str_lst
- methods
	- prefixes:
		- 'is'/'are'/'has'/'can' for no var is passed but a bool is returned; e.g. 'obj.is_item()'
		- 'chk' for a method where you will send an obj and get back a bool
		- 'get' for a method that will return a 'usuable' obj var
		- 'disp' if a method's main purpose is to buffer content
		- 'err' if method's main purpose is to test for an error, throw an error message, and return bool
	- postfixes:
		- 'err' if method's main purpose is to test for an error, throw an error message, and return bool


*** Standard Module Sections ***
Notes:
- Custom sections exist for some complex classes like Room, Creature, and Container
- Doulbe-spacing between module section; single-spacing between class sections

<header = program, name, date, description>
### import
### local functions
### classes
<within a class>
	# *** getters & setters ***
	# *** attrib methods ***
	# *** simple methods ***
	# *** class identity methods ***
	# *** scope methods ***
	# *** display methods ***
	# *** complex methods ***
	# *** general errors ###
	# *** verb error methods ***
	# *** verb methods ***
""" *** Module Documentation *** """


*** standard doc_string sections ***
""" *** Module Documentation ***
	* <ClassName> class:
	- <method_name>() method [<ClassName> class]:
		Overview:
		Implementation Detail:
		Program Architecture:
		Game Design:
		Historic Note:


*** Basic Refactor Steps ***
	- refactor pass - basics
		- shorten / standardize variable names
		- MOVE ASSIGNEMENTS CLOSER TO USAGE!
		- leverage if-then shield pattern 
		- provide 'None' options for variables and 'match' options for Conditions
		- Format strings with f-Strings. 'name = "Alex" ;; my_string = f"Hello {name}"
		- ensure graceful failure of missing key lookups
		- raise errors on 'impossible' outcomes
		- comment each new attribute
		- add tripple-quote doc_strings for classes, verbs, and in-depth doc
	- refactor pass-advanced
		- auto-gen keys
		- return the conditional comparison value itself (bool)
		- Concatenate strings with '.join' ; 'lst_of_str = ["Hi", "Tom"] ;; my_str = " ".join(lst_of_str)' => "Hi Tom"
		- merge / shorten if-then-else with use of 'and' & 'or'
		- consider removing 'inline variables' that are only used once... just return the assigned value...
		- use enumerate to get index & value! replace 'for i in range(len(lst)): lst_item = lst[i]' with 'for i, lst_item in enumerate(lst):'
		- use 'any' to return boolean rather than for-looping through lists
		- don't need to check for if len(lst) > 0: ;; just use if lst: (Also, bool(None) == False
		- use list comprehension: 'squares = [i*i for i in range(10)]'

Links:
- very useful 'how to copy files in python' link: https://stackoverflow.com/questions/123198/how-to-copy-files


*** 9/27/2025 - how to add a command ***
- DONE: implement standard response for creature.jump() (hero & other)
	- DONE: create creature.jump() [w/ hero and other creature option]
	- DONE: in staic_gbl(), add 'jump' to 'one_word_convert_lst'
	- DONE: in staic_gbl(), add 'jump' to 'known_verbs_lst'
	- DONE: in interp() create routine for 'jump'
	- DONE: create jump_err() method in error_class()
	- DONE: test in game (including while seated)
	- DONE: test 'help one-word-commands'


- DONE: create debug rand_mode cmd (include in help display)
	- DONE: in staic_gbl(), add 'rand_mode' to 'debug_verb_lst'
	- DONE: DO NOT in staic_gbl(), add 'rand_mode' to 'known_verbs_lst'
	- DONE: in static_gbl(), add 'rand_mode' to 'one_word_secret_lst'
	- FINDING: tru1word cmds do not currently get validated in validate()
	- CHOICE: create 1word validation or else validate debug in cmd_exe() ?
	- DECISION: debug validation in cmd_exe(); keep tru1word pass-thru on validate()
	- DONE: in cmd_exe() create routine for 'rand_mode'
		- DONE: rand_mode cmd will show current mode ('random' or 'locked')
		- DONE: should also explain rand_mode options and how to enter locked mode
	- DONE: test in game
	- DONE: test help debug
