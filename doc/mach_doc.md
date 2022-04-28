Machine Documentation - Dark Castle v3
Apr 28, 2022

****************************
*** Formal Documentation ***
****************************

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

def_switch_state: the default state of the switch. For stateful switches like levers, def_switch_state == None. For non-stateful switches like buttons, def_switch_state typically == 'neutral'.

trigger_type: This attribute enables switch_state resets. Some switches, like levers, are innately 'stateful' - their switch_state remains constant until they are acted on again. By contrast, stateless switches like buttons and spring-slider-switches must be reset to neutral each turn. When trigger_type = 'pre_act_auto_switch_reset' switch_state is reset to def_switch_state at the start of each turn.

The Switch class is implemented as a MixIn that is combined with ViewOnly to include Switch-specific attributes. Each specific type of switch (ButtonSwitch, SpringSliderSwitch, LeverSwitch) contains the methods needed to act on it (e.g. push or pull).


Conditions:
Triggers are what start Machines but Conditions determine what happens when they run. For example, if in the Entrance, Burt goes East off of the drawbridge, then there are three possible conditions: 1) Burt doesn't have a weapon in his hand, 2) Burt does have a weapon and not gotten the Royal Crown yet, 3) Burt has a weapon and has already gotten the Royal Crown. Each of these conditions will then be associated with a different Result. A Machine's Conditions are limited to examination of Game State, Switches that are associated with the Machine, and the Machine's State.

The Machine class has two Switch-related attributes: cond_switch_lst and cond_lst. cond_switch_lst is a list of switches whose state impacts condidtions. cond_lst is an ordered list of conditions that are possible when the machine is triggered. The conditions within cond_lst should cover all possible cases... e.g. if cond_1 is the case where item_x in hand_lst then cond_2 woudld typically be the case where item_x not in hand_lst.

Each Condition class includes a name attribute and whatever other attributes are needed to check the condition and a method, named cond_check(), that returns True or False. cond_check is called from the Machine class run_mach() method so cond_check() is limited to evaluating conditions beased on the values of active_gs, cond_switch_lst, and mach_state. 


Results:
There is a Result associated with each Condition. The Result updates the game environment with the outcome of running the Machine under these specific conditions and also buffers the outcome description to the Player.

Each Result class includes the attributes it needs to function. For example, the BufferAndGiveResult class includes the give_item attribute which specifies the Item to be placed into Burt's hand when the Result executes.

Each Result class also has a result_exe() method associated with it. result_exe() is passed active_gs and mach_state and returns mach_state (the Machine's own state variable) and cmd_override (which determines whether the Result overrides the Player's own command).

Results are associated with a given machine via the result_lst Machine attribute.


The Machine class itself:
This then brings us to the Machine class itself, which orchestrates all of these components. There is only one Machine class - most of the variability between Machines is introduced via different Switches, Conditions, and Results. From a class definition perspective, Machines are actually implemented as dual-inheritance mix-ins: MachMixIn. This allows for Machine traits to be associated with Invisible, ViewOnly, or Item class traits => InvisMach, ViewOnlyMach, and ItemMach.

The one Machine attribute that we haven't already covered in detail is mach_state. Machines can be stateless (e.g. entrance_south_mach which simply tells Burt that he can't turn back now) but most have some kind of persistent state condition (e.g. has the Crocodile dispensed the Royal Crown?, has the Throne dispensed the Hedgehog Broach?, what is the number that the Iron Portcullis lever array must match?). mach_state holds this state value. It is most often boolean but can be an integer, string, or whatever is needed. A Machine's state is typically inspected by Conditions and updated by Results.

The MahineMixIn class has two methods: trig_check() and run_mach()

Based on the trigger type, trig_check() composes trig_key_lst and compares it to the Machine's trig_val_lst and returns True or False.

run_mach() loops through cond_lst, checks whether each Condition is met (using the condition's check_cond() method), identifies the first True Condition in the ordered cond_lst and its index, and then runs result_exe for the Result in result_lst with the same index. The run_mach() method then updates the Machine's mach_state and returns cmd_override. A structural requirement for run_mach() to run successfully is that there must be one Result for every Condidtion and the associated Conditions and Results must be listed in the same order in cond_lst and result_lst.


An Example: 
Let's take a look at the control_panel Machine located in the antechamber:

control_panel = ViewOnlyMach('control_panel', 'Control Panel', 'panel', 'control_panel', None,
				'post_act_switch', 0, red_button, ['pushed'], [left_lever, middle_lever, right_lever],
				[correct_lever_array_cond, wrong_lever_array_cond], [toggle_portcullis_result, portcullis_doesnt_open_result]) # mach_state == lever_array_value

And before we dive into the machine itself, let's take a glance at the room it's in:

antechamber = Room('antechamber', 'Antechamber', 'antechamber', 'antechamber', None,
				[alcove, left_lever, middle_lever, right_lever, red_button], [torn_note, grimy_axe, iron_portcullis, control_panel],
				{'north' : iron_portcullis}, [])

Here we see that the control_panel is in room_obj_lst (so it is listed in the room description) and the machine's switches (left_lever, middle_lever, right_lever, red_button) are in features (where they can be examined but are not automaticaly listed in the room description). 

Suppose Burt is in the Antechamber and types "push button".

web_main passes this user_input to app_main which opens the save pickle of objects, increments movement, resets the buffer, and calls interp().

Since red_button is in scope for Player interaction, the command is valid and interp() converts this too a two-word command (case = '2word', word_lst = ['button', 'push']).

app_main() calls pre_action() next. It sees that control_panel is a machine but, as its trigger_type is NOT pre_act_cmd, takes no action. red_button does have trigger_type == pre_act_auto_switch_reset so it is reset to 'neutral'. The control_panel run_mach() method has not been run so cmd_override remains False and is returned.

Since cmd_override == False, cmd_exe executes the Player's command. The ButtonSwitch push() method is called and red_button.switch_state = 'pushed' and the response "Pushed." is buffered to the user output.

Control is passed back to app_main() which now calls post_action(). post_action() gets mach_obj_lst (the list of Machine objects in scope) from active_gs and itterates through it searching for any Machines that have trigger_type == 'post_act_switch'. control_panel meets these conditions so trig_case = 'switch' and trig_switch_state_lst = the state of the Machine's trigger switch = the state of control_panel's trigger switch = the state of red_button = 'pushed'. 

Under the same if clause, the value of control_panel.trig_check() is checked and, since 'pushed' is in 'trig_val_lst' (trig_val_lst == ['pushed']), trig_check returns True and control_panel.run_mach() is run.

Let's say for the sake of arguement that the lever array is NOT set correctly.

First control_panel.run_mach() loops through cond_lst and runs cond_check() for each listed Condition. for control_panel, cond_lst == [correct_lever_array_cond, wrong_lever_array_cond]. correct_lever_array_cond is of class LeverArrayCond which is fairly complex. It has a cond_check() method that calculates the binary value of the of the lever array and then returns the compare of this sum to mach_state. Since the lever array is not set correctly, correct_lever_array_cond.cond_check() returns False.

wrong_lever_array_cond does none of the calculations descirbed above. It is of class PassThruCond which has a cond_check() method that checks nothing and simply returns a value of True. This works because wrong_lever_array_cond is the *last* condition in cond_lst and we execute the Result for the first Condition to be True.

So we end up with cond_return_lst == [False, True] => result_index == 1 (the index of the first True Condition) => we rune results_exe on result_lst[result_index]. result_lst == [toggle_portcullis_result, portcullis_doesnt_open_result] so we run portcullis_doesnt_open_result.result_exe(). This is of class BufferOnlyResult so, sure enough, all it does is buffer some text (a mild clue to the Player) and return the existing cmd_override (False) and mach_state.

control_panel.run_mach() is nearly done. It updates it's mach_state based on the return from portcullis_doesnt_open_result.result_exe() (which is the same as the existing mach_state) and then returns cmd_override (which by definition will always be False for tirgger_type == 'post_act_switch').

The Machine has done its job! sore() and end() will be called next by app_main() as needed but the machine coding itself is fini!

Naming Convention:
All machines of class InvisMach have names ending in "_mach". For machines of class ViewOnlyMach or ItemMach this convention colides with the interpreter-based convention of object name = 'noun_verb'. The interpreter-based convention wins here and the '_mach' postfix is dropped for these machines (e.g. control_panel).

Closing Thoughts:
I'm conflicted about Machines. On the plus side, they work and they meet all my goals - they are in-game, transparent, scalable, and reusable. But they are also *vastly* more work and code and, in many ways, complexity than a simple series if-then-elses. Is this good coding or am I making mountains out of molehills by clinging over-tightly to idealogical purity? I'm really not sure... but I've learned a lot and that's the ultimate goal - so I'm going to keep using them. I also suspect that the "goodness" of the Machine structure has everything to do with the scale of Dark Castle. For a four-room dungeon Machines are vastly over-engineered. But for a larger dungeon - or a construction set - perhaps Machines (as I've dsigned them) make sense. Time will tell.

The other reason to stay the course on Machines is that I intend for them to be the basis for Creatures. Creatures were arguably the least fleshed out aspect of Dark Castle v1 & v2. They worked mostly because I allowed very few ways of interacting with them. Hopefully, with the use of Machines, I can imporove on this in v3.



* WARNINGS & TIMERS - GENERAL *

In the wise (roughly paraphrased) words of PERL's creator, "Good tools make easy things easy and hard things possible." The MachineMixIn class addresses the 'hard things' case... it's extremenly flexible - but frankly, it's a convoluted PitA. It's great at enabling the unexpected and expanding the complexity of the Dark Castle world - but whenever possible, it's preferable to create and use simpler, fixed purpose machines (i.e. to make "easy things easy"). Warnings and Timers are both examples of this approach and are also necessary infrastructure for the Hedgehog creature. Warnings are innately self-contained. Timers are a bit more involved. While solving one problem, timers introduce a few new ones... the need to be more rigorous about game time, ensuring that 'auto' game messages are delivered at the right time relative to other game responses, and tracking which events in the game world Burt is able to witness.

* WARNINGS *

Warnings have a rich history in Interactive Fiction. If you cursed in Zork you'd be warned that cursing wasn't allowed. If you issued the same curse again the game would quit on you! Warnings are also a good way to redirect the player from a non-useful pursuit and possibly give them a nudge in the right direction. For example, when Burt attempts to go south from the Entrance and leave Dark Castle we tell him that he can't turn back and then give the player a hint about the Rusty Key. And similar to the Zork cursing use case, if Burt attempts to attack the Hedgehog we warn him not to once or twice but if he keeps at it we let him... with game-impacting results.

The Warning class inherits from Invisible (including the attribute 'name') and, in common with MachMixIn has attributes 'trigger_type' and 'trig_vals_lst'. Warnings need to happen before player command execution and are always triggered by player commands - so 'trigger_type' is always 'pre_act_cmd'. 'trig_vals_lst' uses the same [case, word_lst] format as MachMixIn, and the trig_check() method code is the same as well.

After these similarities, Warnings are much simpler than the MachMixIn class with only two more attributes: 'warn_max' and 'warn_count'. warn_count gets incremented each time pre_action() calls the Warning mach_run() method. If 'warn_max' == 0 then the use case is 'always give the same warning' and always return cmd_override = True. If 0 < 'warn_count' < 'warn_max'then give a specific error and cmd_override still = True. If  'warn_count' == 'warn_max' give a final "Don't say I didn't warn you Burt..." and cmd_override = False. Once warn_count > warn_max there are no future warnings and cmd_override always = False.

The actual warning description key is based on "name" + "_" + str(warn_count). This is implemented with 'try: ... except:' with "I'm not sure that's a good idea Burt..." as the 'except' default.

Fundamentally, Warnings are simple - they inhibit a player command either always or for a finite number of tries and return a variable text message. Warnings do not actually generate any actions - but a MachMixIn condition could take the difference between warn_count and warn_max into account.


* TIMERS *

Like Warnings, Timers inherit from Invisible and have a trigger_type attribute. But in this case trigger_type is set to 'auto_act' and is not triggered by either pre_action() or post_action() (more on this later).

The intent is that timers are "dumb". They are not triggered by player commands or switches - instead they are started or reset via the timer.start() and timer.reset() methods - typically by complex machines. Once started the counter's only job is to count up until it reaches it's maximum. To enable this the counter has attributes of 'active' (boolean), 'timer_count', 'timer_max', and 'timer_done' (also boolean). The mach_run() method is called when the timer is active. Its primary job is to increment timer_count and set timer_done = True once timer_count = timer_max.

Although Timers never directly trigger actions (this is left to machines which can use Timer attributes in their Conditions), one typically does want to let the player know that a timer is running. To this end, Timers have the innate ability to send messages to the player on each Timer interval. To support this, Timer has the attribute 'message_type' which can be 'constant' (same message each turn), 'variable' (different message each turn), or 'silent' (no message). Description key creation is managed in the same way as Warnings with a built-in default alert of "Beep."

Beyond their core functionality, Timers are interesting because they are our first 'auto' machines - that is, they take an action regardless of Burt's choices. This has several implications.

*Valid Turns*

The first is that we need to get more rigorous about what does and does not constitute a valid turn. In the past I called active_gs.move_inc() at the start of app_main() and then selectively called active_gs.move_dec() from within interp() when any error seemed more like the interpreter's fault than the player's. But now, with auto commands in play, we need a clear and consistent measure of which turns are valid so that the timer doesn't tick on a non-valid turn. To enable this I eliminated the move_dec() calls in interp() and set a move_valid variable (boolean) within app_main(). For all 'case' == 'error' and also the 'quit' command, move_valid = False. In this case, no pre, post, or auto actions are called. Whereas, for move_valid == True, move_inc() gets called and pre, post, and auto actions are executed.

*Auto Message Timing*

The next problem to solve is *when* should auto commands be displayed? Let's build up turn order logic from first principles:
	1) We get the player's input via web_main() and call app_main. Within app_main() we first call interp() to understand the player's command.
	2) The player's command is then executed in cmd_exe() (unless overridden)
	3) In some cases, the player's command is inhibited or overriden by the game's response. For example, the case of Burt walking east or west from the Entrance off of the drawbridge. This is carried out by pre_action(), which should clearly run before cmd_exe()
	4) In other cases, the player's command causes a game response. For example, Burt pushing a button. This is performed by post_action(), which clearly needs to run after cmd_exe().

So when should auto commands happen? If they execute in post_action() then they feel like a response to the player's command... which they're not. If it happens in pre_action() then it also comes across as a response to a player's choices (because other pre_actions reference Burt's attempted action). Instead, auto would ideally run *before* getting user input, so that the player can make choices based on it... but if you look at the events in 1) above, you'll see that web_main() has already gotten user input before app_main is ever called... so it appears to be impossible to call auto first without messing around with web_main() (which we want to keep simple). However, if we consider that the first move of the game will never have an auto command... then there's really no difference between going "first" and going "last". So we create an auto_action() routine and have it called at the very end of app_main() so that the auto results appeare *before* the player's next input option.

*Timer Scope*

Finally, we get to the topic of Timer Scope. As our first auto machine, Timers present a unique problem. Before now, all machines operated based on immediate command or switch stimulous from the player. If Burt was in the same room as the machine then he could trigger it. And if he had just triggered then he could surely experience its effects. But auto machines operate independently of player stimulous. This makes scope more complicated.

Let's take our test_timer example - which placed a bomb with a button on it in the Entrance room. The bomb was a fairly simple machine. If Burt pushed the button the timer was started and counted up, turn by turn, to a timer_max of 3. On turn 1 it messaged "Tick 1". On turn 2: "Tick 2". And on turn 3: "Boom!". If Burt pushes the button and spends the next 3 turns in the Entrance than he sees all 3 messages and everything works as expected. 

But what if, instead, Burt pushes the button and then walks north into the Main Hall? Our first question here should always be: "What *should* happen?". This in turn raises the question of how separate are Dark Castle rooms? Should Burt hear what is happening in the next room? My design choice here is that standard rooms are hermetically sealed. There can be custom exceptions of course - but as a standard response, Burt knows nothing about the events of a room he is not in. This standard behavior clarifies what *should* happen in the above example: Burt should hear "Tick 1", then, after going north, he should see the description of the Main Hall. In the mean time the bomb should "Tick 2" and "Boom!" in the Entrance without Burt getting any notification of it (unless he immediately turns around and runs back to the Entrance).

Now that we know our goal, what *does* happen if Burt pushes the bomb button and then walks north? The default coding only runs a machine that is in the scope of the room Burt is in. So if test_timer is in entrance.invis_obj_lst then Burt hears "Tick 1" and then heads north to the Main Hall. He can now spend an infinite number of turns in the rest of Dark Castle and the timer will wait until he returns to the Entrance to perform "Tick 2". This is not what we want - we want test_timer to operate independently of Burt's proximity to the bomb. So we create a new attribute in the GameState class: universal_mach_lst. We remove test_timer from entrance.invis_obj_lst add it to universal_mach_lst and, in GameState methods, extend mach_obj_lst with universal_mach_lst. Now auto_in_alert_scope will find test_timer to be in scope no matter where Burt happens to be (though Burt still needs to push the button on the bomb to *start* the timer).

However, now we have the problem that no matter where Burt goes, since test_timer is still in scope, Burt still gets notified of "Tick 2" and "Boom!" - even though he's not in the same room as the bomb! We solve this by giving the Timer class one more attribute: alert_anchor. Now, in the run_mach() method of Timer, we can check for scope_check(alert_anchor) as a requirement for buffering the test_timer messages. If this condition fails, the timer still runs, but Burt never sees the "Tick 2" or "Boom!" messages.

At long last, test_timer is working as we would expect! This was a lot of work just to enable the Hedgehog to eat some stale_biscuits - but hopefully we have also laid some good groundwork for future timers and other auto machines ;-D



********************************
*** Rough Notes and Ideation ***
********************************

* machine / interactive object ideas *

IDEA: perhaps part of control_panel purpose is to isolate description of switch elements from main room inventory?

IDEA: keep all the smarts in machine; lever only knows if it's up or down

DECISION: prefer shallow class inheritance tree over deep


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

