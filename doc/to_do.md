To Do List - Dark Castle v3
Jan 9, 2022


*** How to Add Objects ***
1) If needed, create Class and methods in class_def
2) Instantiate object in mk_def_pkl()
3) Add object to room in mk_def_pkl()
4) Add object to master_obj_lst in mk_def_pkl() [exception: invisible obj like conditions & results that player will never ref]
5) Run mk_def_pkl()
6) Add object description in static_gbl


##########################
### VERSION 3.59 START ###
##########################

Version 3.59 Goals
- Create / update program documentation

IN-PROC: documentation:
	DONE: write up thinking and decisions on machines and switches
	IN-PROC: Machine Code Updates
		DONE: move machine_state to first Machine attribute
			DONE: comment old code
			DONE: write new code
			DONE: full test
			DONE: delete comments
		DONE: standardize 'result' vs. 'results'
			DONE: results_exe => resulte_exe
			DONE: full test
			DONE: delete comments
		DONE: change results_class_def => result_class_deff
			DONE: change file name
			DONE: change import from mk_def_pkl()
			DONE: run mk_def_pkl()
			DONE: full test
		DONE: trigger() => run_mach()
			DONE: rename trigger() in mach_class_def
			DONE: rename trigger() call in pre_action() and post_action()
			DONE: full test
			DONE: delete comments
		DONE: result_num => result_index
			DONE: in the mach_class_def module, run_mach() function, change result_num => result_index
			DONE: run mk_def_pkl()
			DONE: test
			DONE: clean up comments
		DONE: clean up post_action trig_switch_state_lst assignment
			DONE: multi-value code retained in case of future changes
		DONE: machine_state => mach_state
			DONE: in the mach_class_def module, update machine_state => mach_state
			DONE: run mk_def_pkl()
			DONE: full test
			DONE: clean up comments
			DONE: in cond_class_def and result_class_def modules, update machine_state => mach_state
			DONE: test
		DONE: full test (portcullis button failing)
			DONE: backed out trigger_type value changes... button still misbehaving... need to examine "mach_state" change
			DONE: Review mach_state => updated in cond_class_def and result_class_def but still doesn't work right
			INFO: now door only works on zero value lever array... ???
			INFO: throne switch appears to work correctly
			DONE: deep dive on LeverArrayCond
				DONE: Don't forget to run mk_def_pkl after updates!!!
			NOTE: solved it! had forgotten to updat machine_state => mach_state assignment in start_up()
			DONE: full test
		DONE: using trigger_type is *very* efficient... maybe just change attribute value to 'pre_act_auto_switch_reset' ???
			DONE: change value in pre_action()
			DONE: change value in mk_def_pkl()
			DONE: run mk_def_pkl()
			DONE: full test
		CANCEL: re-name Switch trigger_type to switch_reset
			CANCEL: update mach_obj_lst() in gs_class_def() to include switch_reset attribute
			CANCEL: update pre_action module
				CANCEL: add switch_reset check
			CANCEL: updates SwitchMixIn in switch_class_def() to replace trigger_type with switch_reset
				CANCEL: attribute
				CANCEL: declaration
				CANCEL: @properties
			CANCEL: full test
			CANCEL: delete comments
		DONE: Machine naming convention... no '_mach' after control_panel ??
			DONE: documented in Machine Decisions
		IN-PROCES: Run switch re-sets w/ regular pass-thru machines (?)
			CANCEL: add pre_act_auto code to pre-action
			CANCEL: create SwitchResetResult
			CANCEL: create switch_neutral_reset_result obj
			IDEA: thinking through this further... I don't want to have to create a separate reset trigger for every "standard" switch
			IDEA: standard switches should be pretty painless... I can make a complex switch later if I need special behaviors
			IDEA: as a compromise, how about if I add a def_switch_state attribute to SwitchMixIn (standard value == 'neutral')
			IDEA: then, in the pre_action() test, if obj.switch_state != obj.def_swicth_state: obj.switch_state = obj.def_switch_state
			IDEA: this allows for non-'neutral' default switch states
			TBD: add def_switch_state attribute to SwitchMixIn and ViewOnlySwitch
			TBD: update switch obj values in mk_def_pkl
			TBD: run mk_def_pkl
			TBD: update reset code in pre_action 
	TBD: Update Machine Notes based on Code Updates
	TBD: Separate document for Machine Notes
	TBD: Sort out rough Machine ideas


*** Machine Decisions ***

The Purpose of Machines:

If Machines are simply objects taht respond to user commands then one could argue that the world of Dark Castle is already filled with machines. After all, doors are machines. Containers are machines. On some level, even rooms and items are machines. Each responds in a standard, simple, and reactive fashion to player actions.

But many of the puzzles in Dark Castle - or any other text adventure - hinge on exception cases to these norms: the Player tries to walk south from the entrnace but they're turned back with a clue, the Player wants to take the Shiny Sword but the Hedgehog intercedes, the Player tries to examine the control panel but the Goblin attacks before they can. 

Likewise, many puzzles depend on more complex machines: the Iron Portcullis can only be opened by matching the Lever Array to the Messy Handwriting on the Note and then pushing the Red Button, the Hedgehog Broach will only be dispensed once after the first time Burt pulls the Throne. 

These custom, complex, and pro-active Player interactions require a more intricate coding solution than a simple door - and the general name I give for many of them is "Machines". What follows is an explanation of my approach to implementing "Machines" in Dark Castle.

The Journey to Modular Machines:

The journey to establishing the current structure for Machines was a long and winding one that's hopefully arrived at a reasonable solution. Here were the major milestones:

1) In both Dark Castle ev1 and v2 I realized the need to interject pre and post actions into the game based on player behavior. A pre-action is one that occurred before the player's intended result (e.g. the Hedgehog blocking Burt from getting the shiny Sword). A post-action is one that occurs after Burt's action (e.g. after Burt pushes the Red Button the Control Panel machine should whirr and possibly open the Iron Portcullis). In the early versions of the game the player's commands were sent to an enormous If-Then-Else construct that checked to see if the conditions were right to invoke a pre or post action. This approach had the advantages of being simple and extremly flexible - but it always disturbed me for several reasons:
	A) It was extremely opaque to anyone reading the code. You could easily read through the coding for the Entrance and have no idea that going East or West off the drawbridge was deadly.
	B) It took you out of the game... it was like a whole second set of game logic independent from the main program.
	C) The If-Then-Else routine was neither scalable nor reusable
For all these reasons I wanted a different solution in v3.

2) My first idea was to populate rooms with 'conditional-command-lists'. These would be objects with lists-of-lists attributes that acted as AND and OR grouping of conditions and results. This approach had the natural advantage of signalling that something was going on in the room... but it was basically a large, distributed If-Then-Else list so it still had problems B) and C) from above. After tinkering with some psedo code I abandoned this idea.

3) Next I considered specific machines with specific conditions and actions. For example, a 'travel_effect' machine that would reside in each room and produce effects like the "You can't turn back now..." message when going South from the Entrance as well as the hazzards and benefits of going East or West off of the Entrance drawbridge. I prototype this solution and made several discoveries:
- Machines can be invisible
- Monolithic machines have way too many attributes to keep track of
- The Entrance 'Go South' vs. 'Go East / West' use cases are very different ('Go East / West' is much more complex)... attempting to use the same Monolithic Machine for both leads to *many* attributes with Null value in the 'Go South' case.

4) The problematic 'travel_effect' implementation led me to the solution of Modular Machines. The fundamental idea is that the Machine class definition is the same for all Machines but that the Conditions and Results are separate objects that are attributes of each Machine. This modular approach allows for much greater re-use. Having a single Machine class definition does impose some constraints - but that's not an all bad thing - constraints create structure. We'll take a look at how the Modular Machine and it's components in detail in the next section.

High Level Appliction Flow:
To understand Machines it helps to first understand the high-level module call flow of the Dark Castle app.

It all starts with web_main, a very simple web-tier function who's only job is to get user input and present the app's response text to that input. 

To get the response text, web_main calls app_main. app_main is the heart of the app. It recieves user_input from web_app and converts it into output (the app's response text). In the special case of the game's first turn, app_main calls start_me_up which prints a welcome and sets some one-time game variables. But for all subsequent calls to app_main the following flow occurs:
	1) load the object variables from the game's save pickle and increment the move count
	2) calls the interpreter function to convert the user's input into a game command. interpreter returns a 'case' and a 'word_lst'
	3) before executing the game command, app_main now calls the pre_action function. pre_action scans the available machine scope (simplisticaly, the room Burt is in) for machines that have pre_act triggers. If any exist, checks to see if any pre_action Machines are triggered and, if so,  runs those Machines. The pre_action function returns the boolean variable cmd_override to app_main. cmd_override == True is for cases where the pre_action negates the player's command.
	4) If cmd_override is False, app_main now calls cmd_exe to execute the player's command (e.g. "take key" => "Taken")
	5) app_main now calls the post_action function which determines if the player's command (for example, pulling a lever) triggers a post_action Machine. If so, the Machine is run.
	6) app_main calls score to check if any gamestate changes (e.g. Burt entering a new room or Burt holding an object in his hand for the first time) merrit a score increase. If so, score is increased and an update to the player is buffered.
	7) if game_ending != 'tbd' then app_main calls the 'end' function to buffer the end of game text
	8) app_main saves the updated objects to the save pickle and resturns 'output' and 'end_of_game' to web_main

The key take-away from the app_main flow is that, both before and after the player's command execution call, the game "gets a turn". These ad-hoc pro-active or responsive game actions are what the Machine construct enables.


The Modular Machine Components:
Michines are composed of Triggers, Switches, Conditions, Results, and the framework of the Machine itself which orchestrates all of these. I'll detail each of these below.

Triggers:
Triggers are the Player Commands or Switches that can start Machines. The information about a Trigger lives in the Machine class itself - a given Switch has know "knowledge" that it's the trigger for a machine and multiple Machines could have the exact same Trigger (this makes sense when you think about Player Commands being triggers).

The Machine class has the following Trigger attributes: trigger_type, trig_switch, trig_vals_lst

trigger_type: a string that identifies when the Trigger takes effect and what type of Trigger it is. Examples: 'pre_act_cmd', 'post_act_switch', 'pre_act_auto'

trig_switch: for Switch-based Triggers this is the Switch object that Triggers the Machine. For Player Command-based Triggers the value is None. At present, all Machines have at most one Switch Trigger. I may make trig_switch a list in the future if I end up making Machines with multiple triggers.

trig_vals_lst: The Switch States or Player Commands (case & word_lst) that will activate the Trigger.


Switches:
Switches are buttons, levers, sliders, and the like. They can be operated on ("pushed", "pulled", etc) to change their state. In theory, one could bake intelligence into switches but I have chosen to make my Switches simple and dumb. They know their own state and that's it. Their only unique attributes are swtich_state and trigger_type:

switch_state: The possible values of switch_state depend on the switch in question. For ButtonSwitch it's 'pushed' or 'neutral'. For SpringSliderSwitch, 'pulled' is added as a possible value. For LeverSwitch, 'up' or 'down' are possible. 

trigger_type: This attribute enables switch_state resets. Some switches, like levers, are innately 'stateful' - their switch_state remains constant until they are acted on again. By contrast, stateless switches like buttons and spring-slider-switches must be reset to neutral each turn. When trigger_type = 'pre_act_switch_reset' switch_state is reset to 'neutral' at the start of each turn. I should probably rename this attribute to switch_reset to avoid confusion.

The Switch class is implemented as a MixIn that is combined with ViewOnly to include Switch-specific attributes. Each specific type of switch (ButtonSwitch, SpringSliderSwitch, LeverSwitch) contains the methods needed to act on it (e.g. push or pull).


Conditions:
Triggers are what start Machines but Conditions determine what happens when they run. For example, if in the Entrance, Burt goes East off of the drawbridge, then there are three possible conditions: 1) Burt doesn't have a weapon in his hand, 2) Burt does have a weapon and not gotten the Royal Crown yet, 3) Burt has a weapon and has already gotten the Royal Crown. Each of these conditions will then be associated with a different Result. A Machine's Conditions are limited to examination of Game State, Switches that are associated with the Machine, and the Machine's State.

The Machine class has two Switch-related attributes: cond_switch_lst and cond_lst. cond_switch_lst is a list of switches whose state impacts condidtions. cond_lst is an ordered list of conditions that are possible when the machine is triggered. The conditions within cond_lst should cover all possible cases... e.g. if cond_1 is the case where item_x in hand_lst then cond_2 woudld typically be the case where item_x not in hand_lst.

Each Condition class includes a name attribute and whatever other attributes are needed to check the condition and a method, named cond_check(), that returns True or False. cond_check is called from the Machine class trigger() method so cond_check() is limited to evaluating conditions beased on the values of active_gs, cond_switch_lst, and machine_state. 


Results:
There is a Result associated with each Condition. The Result updates the game environment with the outcome of running the Machine under these specific conditions and also buffers the outcome description to the Player.

Each Result class includes the attributes it needs to function. For example, the BufferAndGiveResult class includes the give_item attribute which specifies the Item to be placed into Burt's hand when the Result executes.

Each Result class also has a results_exe() method associated with it. results_exe() is passed active_gs and machine_state and returns machine_state (the Machine's own state variable) and cmd_override (which determines whether the Result overrides the Player's own command).

Results are associated with a given machine via the result_lst Machine attribute.


The Machine class itself:
This then brings us to the Machine class itself, which orchestrates all of these components. There is only one Machine class - most of the variability between Machines is introduced via different Switches, Conditions, and Results. From a class definition perspective, Machines are actually implemented as dual-inheritance mix-ins: MachMixIn. This allows for Machine traits to be associated with Invisible, ViewOnly, or Item class traits => InvisMach, ViewOnlyMach, and ItemMach.

The one Machine attribute that we haven't already covered in detail is machine_state. Machines can be stateless (e.g. entrance_south_mach which simply tells Burt that he can't turn back now) but most have some kind of persistent state condition (e.g. has the Crocodile dispensed the Royal Crown?, has the Throne dispensed the Hedgehog Broach?, what is the number that the Iron Portcullis lever array must match?). machine_state holds this state value. It is most often boolean but can be an integer, string, or whatever is needed. A Machine's state is typically inspected by Conditions and updated by Results.

The MahineMixIn class has two methods: trig_check() and trigger()

Based on the trigger type, trig_check() composes trig_key_lst and compares it to the Machine's trig_val_lst and returns True or False.

trigger() loops through cond_lst, checks whether each Condition is met (using the condition's check_cond() method), identifies the first True Condition in the ordered cond_lst and its index, and then runs results_exe for the Result in result_lst with the same index. The trigger() method then updates the Machine's machine_state and returns cmd_override. A structural requirement for trigger() to run successfully is that there must be one Result for every Condidtion and the associated Conditions and Results must be listed in the same order in cond_lst and result_lst.


An Example: 
Let's take a look at the control_panel Machine located in the antechamber:

control_panel = ViewOnlyMach('control_panel', 'Control Panel', 'panel', 'control_panel', None,
				'post_act_switch', 0, red_button, ['pushed'], [left_lever, middle_lever, right_lever],
				[correct_lever_array_cond, wrong_lever_array_cond], [toggle_portcullis_result, portcullis_doesnt_open_result]) # machine_state == lever_array_value

And before we dive into the machine itself, let's take a glance at the room it's in:

antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
				[alcove, left_lever, middle_lever, right_lever, red_button], [torn_note, grimy_axe, iron_portcullis, control_panel],
				{'north' : iron_portcullis}, [])

Here we see that the control_panel is in room_obj_lst (so it is listed in the room description) and the machine's switches (left_lever, middle_lever, right_lever, red_button) are in features (where they can be examined but are not automaticaly listed in the room description). 

Suppose Burt is in the Antechamber and types "push button".

web_main passes this user_input to app_main which opens the save pickle of objects, increments movement, resets the buffer, and calls interp().

Since red_button is in scope for Player interaction, the command is valid and interp() converts this too a two-word command (case = '2word', word_lst = ['button', 'push']).

app_main() calls pre_action() next. It sees that control_panel is a machine but, as its trigger_type is NOT pre_act_cmd, takes no action. red_button does have trigger_type == pre_act_switch_reset so it is reset to 'neutral'. The control_panel trigger() method has not been run so cmd_override remains False and is returned.

Since cmd_override == False, cmd_exe executes the Player's command. The ButtonSwitch push() method is called and red_button.switch_state = 'pushed' and the response "Pushed." is buffered to the user output.

Control is passed back to app_main() which now calls post_action(). post_action() gets mach_obj_lst (the list of Machine objects in scope) from active_gs and itterates through it searching for any Machines that have trigger_type == 'post_act_switch'. control_panel meets these conditions so trig_case = 'switch' and trig_switch_state_lst = the state of the Machine's trigger switch = the state of control_panel's trigger switch = the state of red_button = 'pushed'. 

Under the same if clause, the value of control_panel.trig_check() is checked and, since 'pushed' is in 'trig_val_lst' (trig_val_lst == ['pushed']), trig_check returns True and control_panel.trigger() is run.

Let's say for the sake of arguement that the lever array is NOT set correctly.

First control_panel.trigger() loops through cond_lst and runs cond_check() for each listed Condition. for control_panel, cond_lst == [correct_lever_array_cond, wrong_lever_array_cond]. correct_lever_array_cond is of class LeverArrayCond which is fairly complex. It has a cond_check() method that calculates the binary value of the of the lever array and then returns the compare of this sum to machine_state. Since the lever array is not set correctly, correct_lever_array_cond.cond_check() returns False.

wrong_lever_array_cond does none of the calculations descirbed above. It is of class PassThruCond which has a cond_check() method that checks nothing and simply returns a value of True. This works because wrong_lever_array_cond is the *last* condition in cond_lst and we execute the Result for the first Condition to be True.

So we end up with cond_return_lst == [False, True] => result_num == 1 (the index of the first True Condition) => we rune results_exe on result_lst[result_num]. result_lst == [toggle_portcullis_result, portcullis_doesnt_open_result] so we run portcullis_doesnt_open_result.result_exe(). This is of class BufferOnlyResult so, sure enough, all it does is buffer some text (a mild clue to the Player) and return the existing cmd_override (False) and machine_state.

control_panel.trigger() is nearly done. It updates it's machine_state based on the return from portcullis_doesnt_open_result.result_exe() (which is the same as the existing machine_state) and then returns cmd_override (which by definition will always be False for tirgger_type == 'post_act_switch').

The Machine has done its job! sore() and end() will be called next by app_main() as needed but the machine coding itself is fini!

Naming Convention:
All machines of class InvisMach have names ending in "_mach". For machines of class ViewOnlyMach or ItemMach this convention colides with the interpreter-based convention of object name = 'noun_verb'. The interpreter-based convention wins here and the '_mach' postfix is dropped for these machines (e.g. control_panel).

Closing Thoughts:
I'm conflicted about Machines. On the plus side, they work and they meet all my goals - they are in-game, transparent, scalable, and reusable. But they are also *vastly* more work and code and, in many ways, complexity than a simple series if-then-elses. Is this good coding or am I making mountains out of molehills by clinging over-tightly to idealogical purity? I'm really not sure... but I've learned a lot and that's the ultimate goal - so I'm going to keep using them. I also suspect that the "goodness" of the Machine structure has everything to do with the scale of Dark Castle. For a four-room dungeon Machines are vastly over-engineered. But for a larger dungeon - or a construction set - perhaps Machines (as I've dsigned them) make sense. Time will tell.

The other reason to stay the course on Machines is that I intend for them to be the basis for Creatures. Creatures were arguably the least fleshed out aspect of Dark Castle v1 & v2. They worked mostly because I allowed very few ways of interacting with them. Hopefully, with the use of Machines, I can imporove on this in v3.


##########################
### VERSION 3.60 START ###
##########################
Version 3.60 Goals
- Create class, methods, and obj for goblin creature

TBD: consolidate rough Creature ideas


##########################
### VERSION 3.62 START ###
##########################
Version 3.62 Goals
- Create class, methods, and obj for hedgehog1 (hungry_guard) creature


##########################
### VERSION 3.64 START ###
##########################
Version 3.64 Goals
- Create class, methods, and obj for hedgehog2 (key_trader) creature


##########################
### VERSION 3.66 START ###
##########################
Version 3.66 Goals
- Create class, methods, and obj for read_scroll machine


##########################
### VERSION 3.68 START ###
##########################

Version 3.68 Goals
- Create / update program documentation

TBD: documentation:
	TBD: write up thinking and decisions on creatures
	TBD: update class diagram
	TBD: update module diagram
	TBD: create machine diagram
	TBD: create creature diagram


*** interactive object ideas ***

IDEA: perhaps part of control_panel purpose is to isolate description of switch elements from main room inventory?

IDEA: keep all the smarts in machine; lever only knows if it's up or down

DECISION: prefer shallow inheritance tree over deep

- Burt as an object??
- How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away

***** NEEDED UPDATES TO PLAN *****
- need to link switch to machine
- need to embed the switch in the machine?
- HOW DO I PASS SWITCH STATE TO CONDITIONS?


IDEA: we could have more types of pre and post actions...
	- pre_action_trig => pre_action_cmd_trig
	- this allows for pre_action_state_trig
	- could also have a simple pre_action_state_reset which just resets a button or spring_loaded_slider to given default value (None)
IDEA: throne is the trigger and state switch. Is the machine invisible?
IDEA: throne obj is of class SpringLoadedSlider (child of ViewOnly)
	IDEA: has mehods push() and pull() and state
	IDEA: last_action_state can == 'pushed', 'pulled', 'neutral'
	IDEA: auto_pre_action resets state to 'neutral'
IDEA: I want the trigger and condition switches to be clearly embeded in the machine
IDEA:
	- triggers = player commands or switch values
	- conditions = switch values or active_gs values
	- results = active_gs values, machine_state, and cmd_override value
	
DECISION: for now, only one trigger switch per machine... might want to add a 2nd at some point for a special puzzle


Ideas:
- 4 cases:
	- pre-action trigger
	- post-action trigger
	- pre-action auto
	- post-action auto

- simplest approach is long if-then-else list
	- pros: very flexible
	- cons: opaque, non-scalable
- next idea might be trigger obj associated with rooms or obj that have eval-uable conditions an results
	- pros: less opaque - you know something will happen
	- cons: more coding, essentially a distributed if-then-else
- alt approach: specific machines with specific conditions and actions
	- pros: much less opaque and predictable, create interactive world, standard re-usable object types, provides some creative constraints
	- cons: more coding, less flexible

IDEA: Still thinking through - do I want one TravelEffect obj per possible outcome? Or one per direction??
	- DEC: multiple conditions per TravelEffect but as few outcomes as possible

- interactive object types (class == IntObj ???)
	- travel_effects = pre-action trigger
		- results = buffer, ending, take obj from hand_lst, give obj to hand_lst
		- conditinos = hand_lst contains, event counter
	- machines = post-action trigger
	- creatures = pre-action trigger, post-action trigger, pre-action auto, post-action auto

- Perhaps rooms have an attribute of invis_obj_lst (list contains travel_effects) ?
- Perhaps invisible objects are of a class that wriiting inherits from??
- For inter_obj auto case, need scope_list in active_gs so that inter_obj always gets a turn - even when not in room


IDEA: taking another run at how machines should work
IDEA: machines should be modular... a bit like rooms
IDEA: instead of counter, implement as got_crown = False => True

Principles:
- if the cmd_triggers_lst matches the player command, a result should always be triggered (i.e. a condition should be true)
- conditions should be mutually exclusive => one and only one condition should be true at any one time
- machines should be attomic - they should keep track of their own state (e.g. got_crown)
- each machine will have trig_check() and trigger() methods called byt the pre_action_cmd method
- a triggered machine should always have a True condition that leads to a defined result
	- so the link between conditions & results should live attomicaly within the machine
- so pre_action_cmd will initially be very simple... but it may eventually become the home for pre_action_auto too
- a Creature is a collection of VewOnlyMach objs that enable it to respond to show, give, attack, and other stimuli
- Creatures should be no more complex than necessary
	- so when a specific creature need is met but a new creature behanvior will arrise =>
		- it may make sense to 'swap' in a 'new' creature of the same name
		- (e.g. hedgehog1 == hungry_guard, hedgehog2 == trader
		- presumably creature swap also happens via machine?

- Machine attributes [entrance east / west example]
		machine_type => pre_action_trigger
		machine_state => got_crown = False (Only 1 state per machine? Ppass to every condition?)
		cmd_triggers_lst => [['go', 'go', 'east'], ['go', 'go', 'west']] => return True or False
		cmd_cond_lst =>
				[hand_no_weap, => return result 'die_in_moat'
				hand_weap_1st, => return result 'moat_get_crown'
				hand_weap_repeat] => return result 'moat_crocs_scared'
		result_lst =>
			[die_in_moat, => buffer message, active_gs.game_ending = 'death', return override == True
			moat_get_crown, => buffer message, active_gs.hand_lst_append(crown), got_crown = True, return override == True
			moat_crocs_scared] => buffer message, return override == True

- Machine attributes [entrance south example]
	machine_type => pre_action_trigger
	machine_vars => None
	cmd_triggers => [['go', 'go', 'south']]
	cmd_cond_lst => None
	result_lst => [cant_turn_back] => buffer message, return override == True

Conditions and Results thinking:
- What do the generic condition and result objects / methods look like?
	- condition objects
		- not_in_hand_cond attributes = not_in_hand_lst; Returns True or False => hand_no_weap
		- in_hand_and_bool attributes = in_hand_lst, bool; Returns True or False => hand_weap_1st, hand_weap_repeat
- cond_return_lst = [] , for cond in cmd_cond_lst: cond_return_lst.append(cond_check(cond))
- result_num = return_list.index(True)
- trigger(result_lst[result_num])
	- result obj
		- buffer_and_ending attributes = result_descript, ending < can be None>, cmd_override <T/F> => die_in_moat, moat_crocs_scared
		- buffer_and_give = result_descript, give_item, cmd_override <T/F> => moat_get_crown
- machine variable updates => if result_num == 2: got_crown = True

Class Considerations:
- What class should machines inherit from?
- Some machines will be invisible, some will be features, and some will be items... so where to inherit from?
- Maybe a more important question is what class will MachCond and MachRslt inherit from?
- These should be usable by all Machine varieties... and should never be seen by the player...
- So MachCond and MachRslt should be children of class Invisible
- Then machines can inherit from the correct class: InvisMach, ViewOnlyMach, ItemMach

pre_action_cmd() Function Pseudo-Code:
- get inter_obj_lst and for each pre_action_trig: trig_check = trig_check() <return = T/F>
- if trig_check: cmd_override = trigger() <return = T/F>


### Cutscene ###

- Room Events (pre-action trigger) - maybe using exec()

### Timer Events ###
- have a lantern that dimms over time
- references to Zork Brass Lantern
- Provides a timer based trigger that can be inspected each turn (not directly based on Burt actions)


-  events: conditional-command-list, conditions (list of lists; outer = AND; inner = OR), event-text, events (list); check for end of game in wrapper
IDEA: Conditional Cutscene Class
IDEA: Conditional_events (a class similar to dcv2 triggers??) => implement for moat ????
	- default, default description, default method
	- special event first time, seft_description, seft_method, count
	- special event additional times, seat_description, seat_method, count
	- track numbrer of times CE is run?
	- Or maybe just binary cond_event_exists in each obj?
	- also need to distinguish pre=action vs. post-action (e.g. 'take sword' vs. 'read lettering' or 'push button')
	- also need to distinguish 1-time events (e.g. croc) vs. every-time events ('take sword') vs. warnings (e.g. 'eat biscuits')

### Creature Class ###
### Switch Classes (button & lever) ###

More obj Ideas:
- timers as obj
- 'warnings' as obj

More ideas on Creatures:
- Treat creatures like roving conditional events
- Wrapper checks for presence of creature in room and checks for conditionals against creature too

Key Creature Verbs (methods):
- show, give, attack


HOW MACHINES SHOULD WORK:

levers, and button => and machines!
	Lever and Button objects
	Working portcullis puzzle

IDEA: Create Machine class
		- Complex machines have at least 2 inputs (vs. doors)
		- Control Panel is a machine (also throne, radio, and baking machine)
		- Have 'help machines'
		- Logic, outcomes, & descriptions live in machine - button just starts, levels just set values
		- Machine obj also includes list of 'controls' (3x levers and button)
		- (For fun, baking machine should have lever to start and buttons to set values)
		- Buttons & Levers are dumb
			- Levers only know if they are up and down and how many times pulled
			- Buttons only know if phushed this turn and how many times
		- Machine state is checked each turn in wrapper (similar to conditional events & creatures)
			- Machine checked based on room
		- Should logic be in machine or in attached conditional events??
	TBD: Create class LeverSetVal and objects left_lever, middle_lever, right_lever
		TBD: Create method pull()
			TBD: set lever value based on up or down (start down; down = 0)
	TBD: Create class ButtonToggleIfVal and object red_button
		TBD: Create method push()
			TBD: on push check value; if value then toggle state else nothing; descript text for success and fail
TBD: random responses to wrong direction commands ;-D
TBD: implement scoring



*** SOMEDAY MAYBE IDEAS ***

TBD: Figure out a way in web browser to show all adventure text in scrolling window
TBD: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )
TBD: Try tupples for descript_dict
	NOTE: Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
- fun idea - small creature - like a mouse - as an item
- more directions
- landscape / path changes
- create 'win' test routine with checksum
- create a hint sub-system
TBD: for doors and containers, use None option for no lock or no lid?
- extend BufferOnlyResult result_exe method in BufferAndEndResult and BufferAndGiveResult
TBD: learn about Super()
TBD: read this article: https://sangeeta.io/posts/a-super-post-on-python-inheritance/
TBD: extend child methods in results_class_def ?
TBD: Jenkins integration to automatically update "v3 alpha" tab with latest commits?
TBD: list of 'contained' internal_switches in MachMixIn attributes?
	NOTE: (i.e. add to scope and remove levers & button from features?)
	NOTE: [this is a good idea but hold off until at least one more control_panel type machine gets created]
TBD: re-name 'wrapper' to 'app_main'
TBD: update pickle names
TBD: out_buff => output (or possibly user_output)

*** NEW PUZZLE IDEAS ***

Princess Time-Travel Quest:
- Princess asks Burt if he's an assassin, spy, or suitor => answer = 'baker'
- Back in time, need to hide key behind brick (otherwise princess arrives but time travels back behind locked door)
- Get key from chief guard via cheesecake?
- Both Burt and the Princess need to eat food before time travel (nod to hitchhikers guide)
- Juanty hat to escape guards at just the right time

IDEA: have a 'jaunty hat' that enables you to move 'twice per time click' (i.e. no pre or post actions or move increments for one turn)
	- would necesitate default responses to attacks and things like that
	- could solve nearly any puzzle so need to deliver late in the game
	- maybe especially useful for solving a '2 button' puzzle

- Back to the Future - time machine chariot idea
	- chariot is in stable hooked up to old_mare
	- feed old_mare 1.7 boxes of jigga-whats special speed feed and chariot charges forward... at 8.9 mph blue light and time change
	- dial in chariot picks year
	- chariot is shiny metal and has a label on is saying "from the grande dutchy of Lorean" (remember, only chariots from the Grande Dutchy can truly call themselves 'De Lorean' - all others are merely fast, shiny chariots)
	- Special easter eggs... there are 2 full boxes of jigga-what's special feed and 2 70% full boxes on an old dusty shelf (current time). They appear ancient and you've heard that for some reason or other this brand was outlawed 100 years ago - you didn't think any was left in the world... if Burt goes back in time he can feed the 1.7 jw to the old mare to get back in time - at this point, all 4 boxes are consumed (Burt will, in fact remember there as only having been 2 in current time)... but, if Burt attempts to bring a box with him back to the future he will fragment the space-time-continum and find himself sitting at a computer, playing a text adventure... with all of his memories fading and end with the statement "it must have been just a game all along..." with no score = "N/A" and title = time traveller

- Peter Pan puzzle where you catch and make use of your shadow / mirror image?

IDEA: Junk mail puzzle (multi-element solution); all for "chariot warranties"

IDEA: Thief puzzle (can take from backpack)

IDEA: create a jaunty_cap that makes Burt move twice as fast as everything else in the world - maybe essential for escaping the time travel ball?

IDEA: create a fun scenario where TravelEffect take item gets used... maybe a giant brid comes along and takes whatever's in Burts hand and scares him off until he carries a lead weight (or a heavy rock?) - which tires the bird out so much Burt can go in the room and get back his stuff and enter the room? Maybe this could be a room between main hall and antechamber that the maze / mouse hole is off of? Maybe nest is in corner of room of class Box (not open / close or lock / unlock).
- Make it a Wumpus Bat - a reference to Hunth the Wumpus and Adventure!!
- Takes an item from Burt's hand and sends him back the way he came to take cover; item is randomly placed in another (reachable) room
- Solution is to enter room carrying a heavy rock - Bat will take but leaves rock by its nest with a note "Tired out from lugging big rocks - leaving Dark Castle for a while to visit the Wumpus"
- Heavy Rock allows introduction of carrying capacity... playing can't carry *anything* else while carrying Heavy Rock
- some useful treasure found in the nest 
- Nest could be a container with open_state = None and lock_state = None

- Can sharpen and clean sword in mouse hole - maybe only way to get past goblin
- need a non-shrunken ruby to pay for sword sharpening (turns up nose at cheese - says he never touches it because it gives him indigestion)
- mini Zork maze to get to blacksmith mouse
- maybe random mouse keeps appearing and if you give it cheese it runs off and can be followed to the blacksmith
- maybe mouse in maze is from Who Moved my Cheese
- references to grafitti in maze?? (e.g. "what would you do if you weren't afraid?")
- Potion cabinet => maze => sharpen payment; cabinet: Royal Potions Maker: Danni Igotyour , potion: 867-5 => combo
	- Give clues - mention that you hear a boppy tune in your head on description; give some lyrics after 5th attempt
- Sign on mousehole mentions royal blacksmith and royal baker
- Can only find royal baker by NOT taking the signed "exit" route from the blacksmith (easy east)
- Machine in bakery makes cheese (for mouse) or biscuits (for hedgehog) by adding ingredients and pushing correct button
	- Need to have "hatch" closed in order to run machine
	- Takes 3 turns to create food
	- if start biscuits turn after starting cheese then 5 turns later produces cheesecake! (only once - machine brakes after)
	- Everyone wants cheesecake! Can be used to solve any creature puzzle (even goblin) and takes 5 turns to eat
- potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
	- 3 turns of shrink in Main Hall; 30 turns in mouse hole
	- maybe 2 potions in cabinet
	- Need to keep the magic shrink potion from traveling... maybe have it in a basin with a chain-attached cup?
		- (don't want to code every room for being mouse sized)
- Maybe a magic radio (a machine entity like the baking machine) in the Maine Hall that plays "Danni I've got your numbrer" when tuned correctly? Gives clue for potion chest. Also maybe acts as distraction during time travel puzzel - plays over gentle lilting of harp, violins, and triange - which enables Burt to cut in and dance with princess (evil prince is off gyrating hips wildly)? Perhaps the magic radio used to live in the throne room but got moved to the main hall after the 'incident' (note could indicate this) ;-D
- Radio damaged during move from throne room (speaker out; etc)
	- Radio volume goes to 11 (crossed out?)
	- On time travel need right station & full volume to distract prince (learn songs during future time investigation; maybe "moany moany" or "old time rock and roll"?)
	- Perhaps wearing Hedgehog brooch (and smiling) are key to winning princess' trust durning time travel?

5.x Additional rooms
	Have portait of Willie revealed in throne room and give player mouse hole and time travel quest
	5th room
		mouse hole - to exercise existing capabilities (e.g. "food" that can be eaten)
		copper key opens cabinet which holds potion
		find a use for 'close' verb; maybe potion refill
		possibly create 'return' verb to put things back (or maybe 'swap')
		potion shrinks for set turn count (can only drink twice); toes tingle just before you expand
		enter mouse hole
		maybe fight mouse?
		silver key in mouse trap; need to swap with copper key
		find a use for close command?
		would be fun to use every verb ;-D
		maybe a guard mouse that only lets you past if you're wearing the hedgehog_broach
		Indiana Jones reference for mouse trap and ball chasing you out ;-D
		make hedgehog_broach wearable
		link puzzle to total number of moves? Or to score?
		repeat option like 'again' / 'g' in Zork (JE request)
	Possibly add a room 6 with time travel??
		find a use for the word "griffonage" (illegible handwriting)
		Opportunity to include princess in game - perhaps have Willie give her the hedgehog_broach to time travel
		Depict future (opportunity but challenges) by painting to portrait
		Also get key from time travel - put in container and then refind 100 years later
		loose brick in dark_alcove - "appears not to have been disturbed for 100 years"
		guard with key_detector in main hall
		trade keys with princess? give her the hedgehog broach? maybe during dance in throne room
		dungeon down stairs from throne room
		use the world "balter" (dance poorly but having fun)
		save hedgehog from evil prince?
		final question from princess "you look like you woke up an a stable" - final choice of response from Burt to princess - down to earth or prim
		in throne room 3 paintings of past and 1 blank space for future
		key to open dungeon?
		keys same colors as ready player 1



##########################
### VERSION 4.xx START ###
##########################

Version 4.xx Goals:
	- DB back end
	- "dungeon bulder" web interface (?)

DONE: Watch YouTube vid on SQLAlchemy: https://youtu.be/51RpDZKShiw
	DONE: Create practice file
	DONE: Watch video

DONE: instantiate sqlalchemy DB
	DONE: Queue huge sdk issues due to ancient version of sqlalchemy...
	DONE: Have upgraded to version 1.1.2 using Stash but still getting issues in sqlite compiler
	DONE: Think I might have to upgrade to 1.4.x to get JSON support for sqlalchemy.dialect.sqlite (installed 1.4.18)
	DONE: now requires install of importlib_metadata (installed via 'pip install')
	DONE: now I need to 'pip install typing_extensions'
	NOTE: APPEARS TO WORK!!!

TBD: now start working with sqlalchemy again in place of txt files
	TBD: How do I setup a DB that continues to persist independent of an app running??
	TBD: Before returning values, Interpreter must save stateful_dict to DB
	TBD: Before running code, must load the value of stateful_dict from DB
	IDEA: default object values should start as a DB entry (or txt files) and be loaded on new game



##########################
### VERSION 5.xx START ###
##########################

v5.x IDEAS
- runs on AWS with API GW, Lambda, and DynamoDB!



*** Demo Object Commands ***

# entrance.examine()
# print(entrance.valid_paths)
# entrance.go('south')
# entrance.go('north')

# entrance.examine()
# dark_castle.examine()
# gate.examine()
# gate.read_writing()
# sword.examine()
# sword.take()
# print(hand)
# sword.take()
# sword.drop()
# gate.open()
# gate.unlock()
# rusty_key.examine()
# rusty_key.take()
# print(hand)
# gate.unlock()
# gate.open()
# gate.open()
# print(eval(room).room_stuff)

# sword = Item('sword','The sword is shiny.', True, 5)
# sword.examine()
# sword.change_desc('The sword is rusty.')
# sword.examine()
# print(sword.takeable)
# print(sword.weight)
# sword.add_writing('dwarven runes', 'Goblin Wallaper')
# sword.examine()
# sword.read_writing()
# gate = Door('front gate', 'The front gate is daunting', False, False)
# gate.examine()
# gate.change_desc('The front gate is HUGE!')
# gate.examine()
# gate.read_writing()
# gate.add_writing('rusty letters', "Abandon Hope All Ye Who Even Thank About It")
# gate.read_writing()


### test ###
# rusty_letters.read(stateful_dict)
# print("TEST: " + stateful_dict['room'].desc)
# rusty_key.take(stateful_dict)
