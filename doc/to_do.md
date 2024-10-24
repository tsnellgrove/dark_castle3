To Do List - Dark Castle v3

############################
### VERSION 3.87.0 START ###
############################

Start Date: Jun 10, 2024
End Date: 

Version 3.87.0 Goals:
- review all mod-mach ideas / TBD to data
- introduce standard versioning nomenclature
- review current mod-mach functioning
- review of Switch class
- improve machine modularization
- incorporate Warnings and Timers into mod-mach code
- address response limitations due to std machines
- mod-mach bug fixes
- update mod-mach doc

*** to do org ***
- DONE: std version nomenclature 
	- IDEA: start using std versioning format: x.y.z (build #) => api.features.bug-fix (internal)
		- REF: https://softwareengineering.stackexchange.com/questions/368643/should-we-assign-version-numbers-for-internal-releases
	- IDEA: Reversion cleesh and games with new starting numbers
	- DONE: cleesh reversion 
		- DONE: from '3.86 (6/9/2024)' to '3.8.0 (build 0001)'
	- DONE: dark_castle reversion 
		DONE: from '3.86 (6/9/2024)' to '3.1.0 (build 0001)'
	- DONE: cup_of_tea reversion 
		- DONE: from '0.15 (5/22/2024)' to '0.1.0 (build 0001)'
	- IDEA: since the game code has not changed since last release, there should be no build #
		- DONE: updated

- DONE: setup new MacBook Air for coding
	- DONE: install VS Code
	- DONE: install homebrew
	- DONE: install git
	- DONE: git clone dark_castle3 repo
	- DONE: git stage / commit / push

- DONE: read existing mod-mach doc
	- DONE: read and update 'Road to' section
	- DONE: read 'Components' section
	- DONE: read 'Example' section
	- DONE: read 'Warnings' section
	- DONE: read 'Timers' section

- DONE: new mac updates (build 0001)
	- DONE: fix root_path_str issue
		- DONE: define new root_path_str
		- DONE: update all path calls
		- DONE: test
		- DONE: install pretty table: "pip3 install prettytable"
		- DONE: re-test
		- DONE: clean-up web_main(), app_main(), file_io(), start_up(), both game_updates()
		- DONE: elim engine static_global entry for root_path_str - this never gets used
- DONE: game install routine
	- DONE: pass root_path_str from web_main() to all other modules:
		- DONE: web_main(), app_main(), file_io(), start_up()
		- DONE: test
		- DONE: clean-up web_main(), app_main(), file_io(), start_up()
		- CANCEL: incorporate game_name into obj save in game_update() modules (no need; file is game-specific)
	- DONE: auto-localization
		- LINK: https://stackoverflow.com/questions/21259070/struggling-to-append-a-relative-path-to-my-sys-path
		- DONE: got web_main() working with import os ability
		- DONE: game_update() for cup_of_tea
		- DONE: game_update() for dark_castle
		- DONE: clean up comments in web_main(), & both game_update()
	- DONE: document install dependencies somewhere: set root_path_str & install prettytable

- DONE: switch class (build 0002)
	- DONE: review existing switch class
	- DONE: make LeverSwitch a true MixIn
		- DONE: remove ViewOnly from LeverSwitch
		- DONE: create ViewOnlyLeverSwitch
		- DONE: update import and assignment in dark_castle
		- DONE: text & fix errors
		- DONE: update version build #

- DONE: refactor app_turn modules (mach code only) (build 0003) [Jun 25, 2024]
	- DONE: refactor pre_action()
	- DONE: refactor post_action()
		- DONE: initial clean-up
		- DONE: reverse result_name (verb) and obj_name (noun) in score_disp() call
		- DONE: test
		- DONE: clean-up comments
	- DONE: refactor auto_action()
	- DONE: update version build #

- INPROC: review existing mach class (build 0004) [Jun 28, 2024]
	- DONE: trig_check()
	- DONE: refactor run_mach()
		- DONE: update code to eliminate dual index creation
		- DONE: test
		- DONE: exit and re-test
		- NOTE: was worried that returning a method arguement would cause a circular ref but apparently not
		- DONE: comment clean-up
	- DONE: need a deep dive on trig_check() wildcard routine
		- DONE: test existing wildcard routine via hedgehog_distracted_mach => does not appear to work
		- DONE: troubleshoot hedgehog_distracted_mach
			- DONE: confirm '*' issue by replacing w/ shiny_sword => works; '*' is the issue
			- DONE: fix / refactor hedgehog_distracted_mach / trig_check() wildcard routine
			- DECISION: wildcards will only be valid for nouns
			- DONE: clean up comments
	- DONE: update version build #

- DONE: cond review (build 0005) [Jul 17, 2024]
	- DONE: review and categorize existing conditions
	- DONE: refactor / rename simple conditions
		- DONE: PassThruCond => TrueCond
			- DONE: cup_of_tea
			- DONE: dark_castle
		- DONE: WornCond
			- DONE: refactor cond
			- DONE: update dark_castle
				- DONE: troubleshoot error on read scroll with no crown (indent error? try w/out creature)
				- FINDING: I think the issue was lack of a setter to over-write the 'temp_burt' placeholder
				- DONE: clean up comments
		- DONE: RoomCond & InRoomCond
			- DONE: cond usage eval - do we really need both?
				- FINDING: no - InRoomCond is better written but was only used for test_frog
				- FINDING: RoomCond and InRoomCond duplicate functionality
				- DECISION: re-purpose InRoomCond to inherit from TrueCond and match std WornCond format
			- DONE: refactor cond
			- DONE: update dark_castle
			- DONE: clean up comments
			- DONE: creature_obj => obj (InRoomCond could be used for any obj)
			- DONE: InRoomCond => ObjInRmCond ??
			- DONE: test
		- DONE: CreatureItemCond => ItemInHandCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
		- DONE: WeaponInHandCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
		- DONE: InWorldCond => ObjInWorldCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
			- DONE: sort out InWorldCond dependencies of InWorldStateCond
			- DONE: clean up comments
		- DONE: StateCond => MachStateCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
			- DONE: sort out dependant Cond classes
			- DONE: test & clean up comments
		- DONE: TimerActiveCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
		- DONE: SwitchStateCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
			- DONE: sort out dependant Cond classes
			- DONE: test & clean up comments
		- DONE: LeverArrayCond
			- DONE: update cond
			- DONE: update dark_castle
			- DONE: test
			- DONE: clean up comments
	- DONE: sort out combo cond
		- IDEA: perhaps cond_lst is a list-of-lists; 
			- IDEA: i.e. each cond is in a list; if len(cond) > 0 then 'and' them?
			- IDEA: so this happens at the Machine class / run_mach level
			- IDEA: this way, there is no class of combo_and_cond... which would just add complexity
			- IDEA: cond_combo_lst = [cond_1, 'and', cond_2] or [cond_1, 'or', cond_2] (etc, left to right)
		- DONE: update combo cond 1-by-1
			- DONE: IsWeaponAndStateCond
				- DONE: update run_mach() for element is_list case
				- DONE: loop through list
				- DONE: evaluate combo based on list[0] logic operator
				- CANCEL: create individual conditions for IsWeaponAndStateCond
				- CANCEL: create combo list obj for IsWeaponAndStateCond
				- CANCEL: implement IsWeaponAndStateCond case in dark_castle
				- FINDING: embarassing but it turns out I don't even need IsWeaponAndStateCond
				- DONE: update moat_mach with use of MachStateCond
				- DONE: elim IsWeaponAndStateCond
			- DONE: redo SwitchStateCond w/ enumerate and false check on each switch in list
			- DONE: elim InWorldStateCond
				- DONE: rewrite panel dispenser cond to no longer need combo condition
				- DONE: elimn combo condition
				- DONE: clean up comments
			- DONE: investigte need for StateItemInRoomCond
				- DONE: refeacto pre_action() with update for 'pre_act_timer' case
				- DONE: test
				- DONE: clean-up comments
				- DONE: do I really need to check mach_state in hedgehog_done_eating_mach ??
					- IDEA: is this just to avoid running every move?? [need a state machine!]
					- IDEA: if so, should check mach_state first, followed by 2x obj_in_rm cases
					- DONE: update hh_descript_update_mach mach_state to False
					- DONE: create new ObjOnRmFlrCond class
					- DONE: create new obj_is_on_floor() method in Room class
					- DONE: create new simple conditions based on MachStateCond and ObjOnRmFlrCond classes
					- DONE: test
					- DONE: clean up comments
					- DONE: troubleshooting of new hh_descript_mach()
					- DONE: fix attribute methods in Room class (why ref self._floor_lst ?)
			- DONE: sort out dispense_panel_mach (broach conds => panel conds)
			- DONE: investigate need for NotTimerAndItemCond
				- DONE: eliminate NotTimerAndItemCond
	- DONE: if no current need for complex cond, archive code at bottom of method via comments plug-in
	- DONE: update cond & mach to assume "pass" result if cond not listed
		- EXAMPLE: in dispense_panel_mach , should not need broach_dispensed_cond
		- NOTE: need to address this in run_mach() cond_check() => False if no cond == True
		- NOTE: proceed with caution - game currently errors if not all conditions provided
		- DONE: update machs so that true_cond => pass_cond is always last
	- DONE: clean up Cond class module
	- DONE: summary of deleted condition classes:
# PassThruCond : 		parent class :	 	True ==> DONE (legacy parent class)
# RoomCond :			PassThruCond :		match hero_rm
# CreatureItemCond : 	PassThruCond :	 	match on creature holding item
# StateCond : 			PassThruCond :  	match mach_state
# IsWeaponAndStateCond : MachStateCond :	(match mach_state) && (match weapon in hero hand) > [combo]
# InWorldStateCond :	ObjInWorldCond :	(not mach_state) and (match chk_obj_exist) [combo]
# StateItemInRoomCond :	PassThruCond :		(match item_obj in hero_rm.floor_lst) && (match mach_state) > [combo]
# NotTimerAndItemCond :	PassThruCond :	 	(item_obj in hero_rm.floor_lst) && (not timer_obj.active) > [combo]
	- DONE: update version build #


- DONE: update Mach class (build 0006) [Jul 23, 2024]
	- DONE: add alert_anchor and is_active attribs to MachMixIn
	- DONE: setters & getters
	- DONE: add attribs to all 4 resultant classes (e.g. InvisMach)
	- DONE: update Room.get_mach_lst() to ref 'active'
	- DONE: update cup_of_tea game machs
	- DONE: test
	- DONE: update dark_castle3 game machs
	- DONE: test
		- DONE: troubleshooting issue #1
			- FINDING: timers and warnings are effectively of class Mach (even though inedependent for now)
			- FINDING: this means that they will also be tested for is_active by Room.get_mach_lst()
			- FINDING: but Mach.is_active and Timer.active mean two very different things:
			- FINDING: Mach.is_active refers to whether or not the game should consider the mach to exist
			- FINDING: Timer.active refers to whether or not the timer is currently running
			- FINDING: this nomenclature is innately confusing
			- CANCEL: choose better nomenclature (e.g. perhaps Timer.active => Timer.is_running)
				- DECISION: too many timer.active references
			- DONE: mach.is_active => mach.is_enabled
				- DONE: mach_class
				- DONE: room_class
			- DONE: add is_enabled attribute to Warning
				- DONE: add to attributes
				- DONE: add setters & getters
				- DONE: add in game_update
			- DONE: add is_enabled attribute to Timer
				- DONE: add to attributes
				- DONE: add setters & getters
				- DONE: add in game_update
		- DONE: troubleshooting issues #2
			- FINDING: now I am running into issues with Switches - since they have identity is_mach
			- FINDING: this is true to enable auto-switch restes in auto_action()
			- FINDING: however, since (today) all switches are physical, is_enabled attrib seems wrong
			- FINDING: attempted to use get_mach_lst() logic for enabled machs or switches in Room
			- FINDING: but this is throwing errors (appears that Room is being added to mach_lst)
			- DONE: figure out why Room is being added to mach_lst; fix or create separate get_switch_lst()
				- FINDING: was calling obj.is_switch [i.e. and attrib] instead of ob.is_switch() [a method]
				- FINDING: also, needed to put switch option first in 'or' logic - to avoid is_enabled() eval
	- DONE: clean up comments in mach_class(), room_class(), post_action()

- DONE: result review + simple cases (build 0007) [Aug 7, 2024]
	- DONE: review and categorize existing results
	- DONE: initial result decision-making
		- DONE: decide if I should attempt to use super() on inherited results
			- DECISION: yes, attempt to use super()
		- DONE: decide if results should be symetric... can they be operated by non-players?
			- DECISION: no, don't attempt symetric - non-hero creatures receiving results is rare and tricky
		- DONE: even if machs only opperated by hero, what if opp from another rm? If so, buff only if in rm?
			- DECISION: yes, need to be room aware for result buffering
		- DONE: should BufferResult have a is_mach_state_set attrib?
			- DECISION: yes, BaseResult should do room-aware buffer + option to set mach_state
	- DONE: test git branching for new feature developemnt
		- LINK: https://www.split.io/blog/understanding-the-feature-branching-strategy-in-git/
		- LINK: https://www.linkedin.com/pulse/using-git-implement-new-featurechange-without-affecting-michel-noel/
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch branching_test' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout branching_test' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm that focus in on branching_test
		- DONE: Commit via VS Code to commit changes locally
		- DONE: Push via VS Code to push branch changes to origin (GitHub)
		- DONE: 2nd commit & push test
		- DONE: 3rd commit & push test
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "5th update"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge branching_test -m "branch test merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: 'git branch -d branching_test' to clean-up local branch
		- DONE: 'git push origin --delete branching_test' to clean up origin
	- DONE: BufferOnlyResult => BaseResult (buffer w/ alert_anchor) + set mach_state option (set vs. reset)
		- DONE: create new BaseResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch BaseResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout BaseResult_feature' to switch focus to branching_test branch
			- CANCEL: 'git push' to push new branch to origin
				- FINDING: failed: "fatal: The current branch BaseResult_feature has no upstream branch."
				- FINDING: but Push via VS Code button worked fine
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "5th update"
			- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: create BaseResult in results_class()
			- DONE: create BaseResult based on BufferOnlyResult
			- DONE: add alert_anchor to result_exe() call
			- DONE: test for hero in same room as event before buffering
			- DECISION: no descript_key attrib - keep simple - just buffer based on resutl_name as key
			- DONE: add attribs for mach_state
				- IDEA: bool attrib => is_mach_state_set
				- IDEA: val attrib => mach_state_val
				- DONE: add attribs
				- DONE: create setters & getters
			- FINDING: result_exe() never uses mach_state() [why whould it?]
				- CANCEL: elim mach_state attrib in result_exe() call
				- FINDING: actually, do need it - to pass back mach_state when not set
		- DONE: convert BufferOnlyResult to BaseResult
			- DONE: add BaseResult to import in game_update() for both games
			- DONE: dark_castle/game_files/game_update()
				- DONE: updated all BufferOnlyResult obj => BaseResult
			- DONE: test
		- DONE: git branch merge with master
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge BaseResult_feature -m "branch BaseResult_feature merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d BaseResult_feature' to clean-up local branch
		- DONE: 'git push origin --delete BaseResult_feature' to clean up origin
		- DONE: post-branch-delete run test
	- DONE: BufferAndEndResult => inherit from BaseResult & use super()
		- DONE: create new BufferAndEndResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch BufferAndEndResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout BufferAndEndResult_feature' to switch focus to branching_test branch
			- DONE: but Push via VS Code button
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DON: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc update"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub
		- DONE: add BufferAndEndResult result names to run_mach call for result_exe()
			- DONE: update BufferAndEndResult to inherit from BaseResult
			- DONE: update BufferAndEndResult attrib list and order
			- DONE: update cup_of_tea game_update() to use new BufferAndEndResult
				- DONE: update result obj attribs
				- DONE: add cup_of_tea BufferAndEndResult result to run_mach result_exe list
				- DONE: resolve error (need to explicityl return after super() )
			- DONE: update dark_castle game_update to use new BufferAndEndResult
				- DONE: update result obj attribs
				- DONE: add dark_castle BufferAndEndResult result to run_mach result_exe list
				- DONE: test
			- DONE: result class update: BufferAndEndResult => EndResult
				- DONE: update in result_class()
				- DONE: update in cup_of_tea
				- DONE: update in dark_castl
			- DUNE: comment clean-up: result_class, cup_of_tea//game_update, dark_castle//game_update
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge BufferAndEndResult_feature -m "branch BufferAndEndResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d BufferAndEndResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete BufferAndEndResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: ChgCreatureDescAndStateResult => ChgDescriptResult
		- DONE: create new ChgDescriptResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch ChgDescriptResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout ChgDescriptResult_feature' to switch focus to branching_test branch
			- DONE: Push via VS Code button
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc update"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub
		- DONE: refactor ChgCreatureDescAndStateResult => ChgDescriptResult
			- DONE: result class updates
				- DONE: copy ChgCreatureDescAndStateResult; change parent to BaseResult
				- DONE: change creature_obj => obj (class should change descript_key for any obj)
				- DONE: use super() call BaseResult buffer and mach_state change
				- DONE: update result_exe() attribs
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- DONE: add result obj to mach_run() exception list
				- DONE: update post-attrib assignment if needed
				- DONE: comment out old result class
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class()
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge ChgDescriptResult_feature -m "branch ChgDescriptResult merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d ChgDescriptResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete ChgDescriptResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: BufferAndGiveResult => GiveItemResult
		- DONE: create new BufferAndGiveResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch BufferAndGiveResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout BufferAndGiveResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc update"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub
		- DONE: refactor BufferAndGiveResult => GiveItemResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update setters and getters
				- DONE: <specific changes>: introduce tgt_creature attrib
				- DONE: use super() call BaseResult buffer and mach_state change
				- DONE: update result_exe() attribs
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- DONE: set mach_state appropriately
				- DONE: add result obj to mach_run() exception list
				- DONE: update post-attrib assignment if needed
				- DONE: comment out old result class and remove from import (in nnew name)
			- DONE: test & clean-up
				- DONE: test
					- FINDING: appears that mach_state is not getting set in BaseResult (suspected this)
					- FINDING: mach_state is getting set in BaseResult - but set is not sticking => mach_class
					- FINDING: solved it! Neet to return super().result_exe() !!!
				- DONE: extend lesson-learned to other chile classes of BaseResult
					- DONE: ChgDescriptResult
					- DONE: EndResult
				- DONE: clean-up game_update(), result_class(), mach_class()
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge BufferAndGiveResult_feature -m "branch BufferAndGiveResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d BufferAndGiveResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete BufferAndGiveResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: PutItemInHandResult => TakeItemResult
		- DONE: create new PutItemInHandResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch PutItemInHandResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout PutItemInHandResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is  now ahead of master
		- DONE: refactor PutItemInHandResult => TakeItemResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update attribs and setters and getters
				- DONE: update result_exe() attribs
				- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- DONE: specific class changes - code from take() method:
					- DONE: gs.map.hero_rm.remove_item(self, gs) => get_obj_room(creature_obj)
					- DONE: creature_obj.put_in_hand(self, gs)				
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- DONE: update Result obj name if appropriate => goblin_takes_axe_result
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- DONE: set mach_state appropriately
				- DONE: update post-attrib assignment if needed
				- DONE: add result name to mach_run() exception list
				- DONE: comment out old result class and remove from import (in new name)
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class(), mach_class() [??]
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge PutItemInHandResult_feature -m "branch PutItemInHandResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d PutItemInHandResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete PutItemInHandResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: AddObjToRoomResult => DispenseObjResult Update
		- DONE: create new AddObjToRoomResult_feature git branch
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch AddObjToRoomResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout AddObjToRoomResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master
		- DONE: refactor AddObjToRoomResult => DispenseObjResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update attribs and setters and getters
				- DONE: update result_exe() attribs
				- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- DONE: specific class changes: room_item => dispense_obj; include room_obj as class attrib
			- DONE: update game files
				- DONE: add new result class to game_update imports
				- N/A: update Result obj name if appropriate
				- N/A: update game_update result obj classes, attribs, and post-assignment updates
				- N/A: set mach_state appropriately
				- N/A: update post-attrib assignment if needed
				- N/A: add result name to mach_run() exception list
				- DONE: comment out old result class and remove from import (in new name)
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class(), mach_class() [??]
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge AddObjToRoomResult_feature -m "branch AddObjToRoomResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d AddObjToRoomResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete AddObjToRoomResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test


- DONE: combo Result cases (build 0008) [8/14/2024]
	- DONE: update Mach class to accept a list of results and run all results in the list
	- DONE: sort out AddObjChgDescriptResult and AddObjToRoomAndDescriptResult combos
		- DONE: create new git branch for AddObjChgDescriptResult_feature
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch AddObjChgDescriptResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout AddObjChgDescriptResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master
		- DONE: AddObjChgDescriptResult => ChgDescriptResult + DispenseObjResult
			- DONE: create ChgDescriptResult obj game_update
			- DONE: create DispenseObjResult obj game_update
			- DONE: comment out old AddObjChgDescriptResult obj in game_update
			- DONE: set mach_state appropriately
			- DONE: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: test
			- DONE: comment out old result class and remove from import (in new name)
			- DONE: clean up  comments in result_class, game_update
		- DONE: AddObjToRoomAndDescriptResult => ChgDescriptResult + DispenseObjResult
			- DONE: create ChgDescriptResult obj game_update
			- DONE: create DispenseObjResult obj game_update
			- DONE: comment out old AddObjToRoomAndDescriptResult obj in game_update
			- DONE: set mach_state appropriately
			- DONE: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: test
			- DONE: comment out old result class and remove from import (in new name)
			- DONE: clean up  comments in result_class(), game_update(), game_static_gbl()
		- DONE: git branch merge with master
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge AddObjChgDescriptResult_feature -m "branch AddObjChgDescriptResult_feature merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d AddObjChgDescriptResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete AddObjChgDescriptResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: sort out TimerAndCreatureItemResult combo result
		- DONE: git branch for TimerAndCreatureItemResult_feature
			- DONE: 'git branch' to confirm *master
			- DONE: 'git branch TimerAndCreatureItemResult_feature' to create new branch
			- DONE: 'git branch' to confirm new branch exists but that master is still checked out
			- DONE: 'git checkout TimerAndCreatureItemResult_feature' to switch focus to branching_test branch
			- DONE: 'git branch' to confirm new branch is now in focus
			- DONE: Publish Branch via VS Code button
			- DONE: confirm new branch on GitHub
			- DONE: update doc TBDs to DONEs
			- DONE: <CMD><OPT>S (to save all files)
			- DONE: 'git add .' to add files to be committed
			- DONE: 'git commit -m "doc updates"
			- DONE: 'git push" to push updates to origin (GitHub)
			- DONE: confirm new branch on GitHub is now ahead of master
		- DONE: refactor StartTimerResult
			- DONE: result class updates
				- DONE: copy existing class; change parent to BaseResult and update class name
				- DONE: update attribs and setters and getters
				- DONE: update result_exe() attribs
				- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- N/A: specific class changes: <list here>
			- DONE: update game files
				- N/A: add new result class to game_update imports (same name)
				- DONE: update Result obj name if appropriate
				- DONE: update game_update result obj classes, attribs, and post-assignment updates
				- N/A: set mach_state appropriately
				- N/A: update post-attrib assignment if needed
				- DONE: add result name to mach_run() exception list			
			- DONE: test & clean-up
				- DONE: test
				- DONE: clean-up game_update(), result_class(), mach_class() [??]
		- DONE: create RemoveObjResult
			- DONE: base off of StartTimerResult
			- DONE: key attribute is obj
			- DONE: include setter in case obj is mach or creature
			- DONE: find obj room using Map method and then remove obj using Room remove method
		- DONE: TimerAndCreatureItemResult => StartTimerResult + RemoveObjResult
			- DONE: add new RemoveObjResult class to game_update imports
			- DONE: create result obj based on RemoveObjResult class
			- DONE: add names of new result objs to run_mach()
			- DONE: comment out old result class
			- DONE: comment out old combo result class and remove from import
			- DONE: replace old combo result obj with list of primitive result obj
			- DONE: test [first try!]
			- DONE: clean up clean-up game_update(), result_class(), mach_class() [??]
		- DONE: merge git branch for TimerAndCreatureItemResult
			- DONE: 'git checkout master' to switch focus to master
			- DONE: 'git branch: to confirm focus
			- DONE: 'git merge TimerAndCreatureItemResult_feature -m "branch <FEATURE_NAME> merge"'
			- DONE: 'git push' to push merge to origin (GitHub)
			- DONE: confirm that origin is updated
			- DONE: confirm that code is updated and still runs
			- DONE: 'git branch -d TimerAndCreatureItemResult_feature' to clean-up local branch
			- DONE: 'git push origin --delete TimerAndCreatureItemResult_feature' to clean up origin
			- DONE: confirm origin is cleaned up
			- DONE: post-branch-delete run test
	- DONE: update version and complete build

- DONE: final result class build for refactor cases including travel (build 0009 [8/22/2024])
	- DONE: create new git branch for result_refactor_feature
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch result_refactor_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout result_refactor_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master
	- DONE: refactor AttackBurtResult => AttackHeroResult
		- DONE: result class updates
			- DONE: copy existing class; change parent to BaseResult and update class name <AttackHeroResult>
			- DONE: update attribs and setters and getters
			- DONE: update result_exe() attribs
			- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
			- DONE: specific class changes: <make hand_obj an explicit attrib>
		- DONE: update game files
			- DONE: add new result class to game_update imports
			- N/A: update Result obj name if appropriate
			- DONE: update game_update result obj classes, attribs, and post-assignment updates
			- N/A: set mach_state appropriately
			- N/A: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: comment out old result class and remove from import (in new name)
		- DONE: test & clean-up
			- DONE: test
			- DONE: clean-up game_update(), result_class(), mach_class() [??]
	- DONE: refactor DoorToggleResult => OpenableToggleResult
		- DONE: result class updates
			- DONE: copy existing class; change parent to BaseResult and update class name
			- DONE: update attribs and setters and getters
			- DONE: update result_exe() attribs
			- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
			- DONE: specific class changes: <move toggle() method into door class?; return display str?>
				- DONE: create door.toggle() method that returns is_open [True or False]
				- DONE: DoorToggleResult sets and buffs display str based on door.toggle() return
		- DONE: update game files
			- DONE: add new result class to game_update imports
			- DONE: update Result obj name if appropriate
			- DONE: update game_update result obj classes, attribs, and post-assignment updates
			- N/A: set mach_state appropriately
			- N/A: update post-attrib assignment if needed
			- DONE: add result name to mach_run() exception list
			- DONE: comment out old result class and remove from import (in new name)
		- DONE: test & clean-up
			- DONE: test
			- DONE: clean-up game_update(), result_class(), mach_class() [??]
	- DONE: refactor TravelResult => CreatureTravelResult
		- DONE: result class updates
			- DONE: copy existing class; change parent to BaseResult and update class name
			- DONE: update attribs and setters and getters
			- DONE: update result_exe() attribs
			- DONE: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
			- N/A: specific class changes: <list here>
		- DONE: update game files
			- DONE: add new result class to game_update imports
			- N/A: update Result obj name if appropriate
			- N/A: update game_update result obj classes, attribs, and post-assignment updates
			- N/A: set mach_state appropriately
			- N/A: update post-attrib assignment if needed
			- N/A: add result name to mach_run() exception list
			- DONE: comment out old result class and remove from import (in new name)
		- DONE: test & clean-up
			- N/A: test
			- DONE: clean-up game_update(), result_class(), mach_class() [??]
	- DONE: merge result_refactor_feature git branch
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge result_refactor_feature -m "branch result_refator_feature merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d result_refactor_feature' to clean-up local branch
		- DONE: 'git push origin --delete result_refactor_feature' to clean up origin
		- DONE: confirm origin is cleaned up
		- DONE: post-branch-delete run test
	- DONE: update cleesh engine version build
		- DONE: web_main.py
		- DONE: static_gbl.py

- DONE: final result class updates (build 0010 [8/25/2024])
	- DONE: create new result_class_feature git branch
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch result_class_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout result_class_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master
	- DONE: refactor result class
		- DONE: update call from run_mach(); self.mach_state => self.alert_anchor
			- DONE: comment out elif
			- DONE: test
			- DONE: clean-up comments
		- DONE: solve buffer issues:
			- DONE: need to sort out variable buff (e.g. DoorToggleResult)
				- DONE: pass buff_key as attrib to result_exe() in BaseResult
				- DONE: update BaseResult buff_s(buff_key)
				- DONE: update result_exe() return call in all child classes
				- DONE: update result_exe() call in mach_class() to pass result.name as buff_key
				- DONE: test
				- DONE: update OpenableToggleResult to modify buff_key
				- DONE: update game_static_gbl to provide two different buff_key entries
				- DONE: test
				- DONE: clean up comments in result_class(), mach_class(), game_static_gbl()
			- DONE: How to buffer first rather than last? (e.g. AttackHeroResult)
				- DONE: gs.io.buff_s(self.name + "_pre-buff")
		- DONE: clean-up all the result_class() module comments
	- DONE: git branch merge with master
		- DONE: 'git checkout master' to switch focus to master
		- DONE: 'git branch: to confirm focus
		- DONE: 'git merge result_class_feature -m "branch result_class_feature merge"'
		- DONE: 'git push' to push merge to origin (GitHub)
		- DONE: confirm that origin is updated
		- DONE: confirm that code is updated and still runs
		- DONE: 'git branch -d result_class_feature' to clean-up local branch
		- DONE: 'git push origin --delete result_class_feature' to clean up origin
		- DONE: confirm origin is cleaned up
		- DONE: post-branch-delete run test
	- DONE: update cleesh engine version build
		- DONE: web_main.py
		- DONE: static_gbl.py

- DONE: mach inheritance refactor (build 0011 [])
	- DONE: for Mach class, create an 'is_enabled' attribute
	- DONE: general Mach class review
		- DONE: analyze dark_castle machs
			- FINDING: auto could be parent of cmd which could be parent of switch
		- DONE: analyze dark_castle warnings 
			- FINDING: Warning could be 'proto' class for Mach
			- FINDING: Warning run_mach() needs re-factor
			- FINDING: warning_count has some similarities to mach_state
			- FINDING: warn_max is similar to timer_max
		- DONE: analyze timers
			- CANCEL: Timer needs a reset_timer() method
				- FINDING: exists
			- FINDING: existing Timer run_mach() auto-resets at count == max_count... is this desired?
			- FINDING: Timer is harder to incorporate into parent-child relationship with Mach and Warning
			- FINDING: timer_count has some similarities to mach_state
			- FINDING: active could likely be a method (not an attribute)
			- FINDING: timer_max is similar to warn_max
			- FINDING: timer_done could be replaced by run_count ... which might be useful elsewhere too...
				- IDEA: but this is only useful if we pass run_count to cond_check()
				- IDEA: if timer_count == mach_state, there is no way to pass info about multiple timer runs
				- IDEA: but how far ahead of real use-case do I want to get? Can add as a new feature when needed
			- FINDING: feels like message type (constant vs. variable) could be inferred?
				- IDEA: if message_0 exists => constant message
		- IDEA: inheritance big picture
			IDEA: MachProtoMixIn => (Timer, Warning, MachCmdMixIn), MachCmdMixIn => MachSwitchMixIn
		- DONE: summarize attribs and methods for each type; propose unifying Proto class
			- IDEA: MachProtoMixIn:
				- STD: mach_state, trigger_type, trig_vals_lst, alert_anchor, is_enabled
				- METH: run_mach(), trigger_check()
			- IDEA: Timer(MachProtoMixIn)
				- From Proto:
					- ATTRIB: name, mach_state, trigger_type, alert_anchor, is_enabled
					- MAP: timer_count => mach_state
					- METH: run_mach()
				- Proto Unused:
					- ATTRIB: trig_vals_lst
					- METH: trigger_check()
				- Timer Unique: 
					- ATTRIB: name, active, timer_max, message_type, timer_done
					- METH: over-load run_mach()
			- IDEA: Warning(MachProtoMixIn)
				- From Proto:
					- ATTRIB: name, mach_state, trigger_type, trig_vals_lst, is_enabled
					- MAP: warn_count => mach_state
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: alert_anchor
				- Warning Unique: 
					- ATTRIB: name, warn_max
					- METH: over-load run_mach()
			- IDEA: Mach_auto(MachProtoMixIn)
				- From Proto:
					- ATTRIB: mach_state, trigger_type, alert_anchor, is_enabled
					- MAP: None
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: trig_vals_lst
				- Mach_auto Unique: 
					- ATTRIB: cond_lst, result_lst
					- METH: over-load run_mach()
			- IDEA: Mach_cmd(MachProtoMixIn)
				- From Proto:
					- ATTRIB: mach_state, trigger_type, trig_vals_lst, alert_anchor, is_enabled
					- MAP: None
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: None
				- Mach_cmd Unique: 
					- ATTRIB: cond_lst, result_lst
					- METH: over-load run_mach()
			- IDEA: Mach_switch(MachCmdMixIn)
				- From Proto:
					- ATTRIB: mach_state, trigger_type, trig_vals_lst, cond_lst, result_lst, 
						alert_anchor, is_enabled
					- MAP: None
					- METH: run_mach(), trigger_check()
				- Proto Unused: 
					- ATTRIB: None
				- Mach_cmd Unique: 
					- ATTRIB: trig_switch, cond_switch_lst
					- METH: None

- DONE: plan out which mach ideas to act on and which order to perform them in (inheritance first)
	- DONE: re-read all remaining mach ideas and incorporate as appropriate
		- IDEA: org mach to-dos
		- IDEA: Sort out parrent-child inheritance
		- IDEA: triggers
		- IDEA: Cases where I want a modular machine to run despite an error standard
		- IDEA: state machine for hedgehog
		- IDEA: event bus for goblin dies => dispense panel	
		- IDEA: mod-mach bug fixes
		- IDEA: debug ideas:
		- IDEA: in mk_def_pkl(), sort out more elegant assignment process for self referenced obj
		- IDEA: update modular machine doc!

- DONE: Sort out parrent-child inheritance
	- DONE: create new mach_inherit_feature git branch
		- DONE: 'git branch' to confirm *master
		- DONE: 'git branch mach_inherit_feature' to create new branch
		- DONE: 'git branch' to confirm new branch exists but that master is still checked out
		- DONE: 'git checkout mach_inherit_feature' to switch focus to branching_test branch
		- DONE: 'git branch' to confirm new branch is now in focus
		- DONE: Publish Branch via VS Code button
		- DONE: confirm new branch on GitHub
		- DONE: update doc TBDs to DONEs
		- DONE: <CMD><OPT>S (to save all files)
		- DONE: 'git add .' to add files to be committed
		- DONE: 'git commit -m "doc updates"
		- DONE: 'git push" to push updates to origin (GitHub)
		- DONE: confirm new branch on GitHub is now ahead of master
	- DONE: create ProtoMachMixIn class
		- DONE: attribs = mach_state, trig_type, alert_anchor, is_enabled
			- IDEA: 'trigger_type' => 'trig_type' ??
			- IDEA: hold off on trig_vals_lst for now
		- DONE: methods = run_mach()
			- IDEA hold off on trigger_check() => trig_chk() for now
	- DONE: create TimerX class (inherits from ProtoMachMixIn + Invisible)
		- IDEAS: TimerX class
			- IDEA: existing Timer run_mach() auto-resets at count == max_count... is this desired?
			- IDEA: Timer is harder to incorporate into parent-child relationship with Mach and Warning
			- FINDING: timer_count => mach_state
			- FINDING: active could likely be a method (not an attribute)
				- IDEA: Do I want timers to be stoppable? [w/ stop() method]. If so, need 'active' attirb
			- FINDING: timer_max is similar to warn_max
			- FINDING: timer_done could be replaced by run_count ... which might be useful elsewhere too...
				- IDEA: but this is only useful if we pass run_count to cond_check()
				- IDEA: if timer_count == mach_state, there is no way to pass info about multiple timer runs
				- IDEA: but how far ahead of real use-case do I want to get? Can add as a new feature when needed
			- FINDING: feels like message type (constant vs. variable) could be inferred?
				- IDEA: if message_0 exists => constant message
		- DONE: create TimerX class
			- DONE: class + setters & getters
			- DONE: update chk_str_exist() in IO class to check game_static_gbl
			- DONE: refactor mach_run() method
				- DONE: elim "Beep!" default
				- DONE: elim message_type attrib
				- DONE: base refactor
				- DONE: create set_timer(num) method
				- DONE: create stop() method
			- IDEA: timer 'ding'
				- IDEA: basically, in auto_act() , when the timer is done counting to timer_max, it should 'ding'
				- IDEA: it should stay in 'ding' state for 1 turn so that any mach listening for ding can hear it
				- IDEA: then, in auto_act, at top of timer mach_run, if 'ding' == True; reset and turn 'ding' off
				- IDEA: tricky part is that would be nice to start timer and react to ding both in auto_act
				- IDEA: maybe new 'auto_act_timer_trig' mach trigger that always goes after auto_act ???
			- DONE: sort out 'ding' idea
				- DONE: create is_dinging()
				- DONE: at start of run_mach(), if self.is_dinging(), self.reset and then return
				- DONE: refactor auto_action() and update to enable is_enabled()
				- DONE: enable trig_type = 'pre_act_timer' in auto_action()
				- DONE: create timer.is_active() method (to be used by TimerActiveCond)
			- DONE: update dark_castle timers
				- DONE: first test / doc exact timing of existing Timer obj
				- DONE: update class and attribs and pre_act_timer mach
				- DONE: update TimerActiveCond: active => is_active
				- DONE: test
					- FINDING: Description updates are foobarred
					- FINDING: game starting with hedgehog_eats_timer evaluating to is_active == True
					- DONE: duplicate name for is_active attrib and method causing issues; elim method
				- DONE: try moving pre_act_timer to auto_act_timer
		- DONE: clean-up
			- DONE: comment out old Timer class
			- DONE: update TimerX => Timer
			- DONE: clean up auto_act(), game_update(), pre_act(), cond_class(), mach_class() 
		- DONE: update timer doc
	- DONE: TrigMixIn
		- IDEA: TrigMixIn idea
			- IDEA: inherited by both Warning and CmdMachMixIn
			- IDEA: contains just trig_vals_lst attrib and trigger_check() method
			- IDEA: multiple MixIn sources seems complicated but appears to be best approach
		- DONE: create TrigMixIn class with setters & getters and methods
		- DONE: eliminate 'timer' option from trig_check()
	- DONE: create WarningX class 
		- DONE: create WarningX class (inherits from ProtoMachMixIn + TrigMixIn + Invisible
		- DONE: setters & getters
		- DONE: update mach_run() to use mach-state
		- DONE: refactor mach_run()
			- DONE: custom hero name (vs. "Burt")
			- DONE: elim str-creation variables
			- DONE: cmd_override as default
			- DONE: try / except w/ default for all 3 cases (0, < max, == max) => freedom on last command
			- CANCEL: consider warning reset options
				- DECISION: if resets end up being needed I can add them
				- FINDING: the main goal of Warnings is just to *avoid* a consequence on the first few incidents
		- DONE: update each existing warning
			- DONE: import WarningX
			- DONE: entrance_south_warn 
				- DONE: update attribs
				- DONE: post-assign alert_anchor
				- DONE: test
			- DONE: attack_hedgehog_warning
				- DONE: update attribs
				- DONE: post-assign alert_anchor
				- DONE: test
			- DONE: eat_biscuits_warning
				- DONE: update attribs
				- N/A: post-assign alert_anchor
				- DONE: test
		- DONE: final Warning class updates
			- DONE: comment out old Warning class and swap WarningX => Warning
			- DONE: in mach_class() , WarningX => Warning
			- DONE: in game_update() , WarningX => Warning , elim WarningX import
			- DONE: final test
		- DONE: clean up mach_class(), game_static_gbl(), game_update()
		- DONE: for trigger_type == 'pre_act_cmd' , check for warning.is_enabled in pre_action()
		- DONE: in run_mach(), set is_enabled = False after mach_state == warn_max
		- DONE: update warning doc
	- DONE: create AutoMachMixIn (inherits from ProtoMachMixIn but adds cond_lst & result_lst)
		- DONE: create AutoMachMixIn class w/ setters & getters
		- DONE: update run_mach()
		- DONE: refactor run_mach ()
		- DONE: creaate InvisAutoMach
		- DONE: migrate existing AutoMachs
			- DONE: import new class
			- DONE: dispense_panel_mach
				- DONE: migrate mach obj / attribs
				- DONE: test
			- DONE: re_arm_goblin_mach
				- DONE: migrate mach obj / attribs
				- DONE: test
		- CANCEL: comment out old class and remove from imports
		- DONE: clean up mach_class(), game_update()
	- DONE: can I combine CmdMachMixIn and SwitchMachMixIn into TrigMachMixIn ?
		- DONE: investigate elim of switch_cond_lst as attrib ( vs. regular conditions )
			- FINDING: possible
		- DONE: can trig_switch + trig_vals_lst be combined for case = 'switch' ?
			- FINDING: will complicated trig_vals_switch usage in check_cond() but is possible
	- DONE: ceate TrigMachMixIn (inherits from AutoMachMixIn + TrigMixIn
		- DONE: create MixIn class
		- DONE: create InvisTrigMach class
		- DONE: import InvisTrigMach
		- DONE: migrate existing InvisMach cmd obj
			- DONE: hedgehog_guard_mach
				- DONE: test (trig_vals_lst == [timer_cond]... due to attrib order???)
				- FINDING: I think maybe I just forgot to run the game_update after swapping attrib order
			- DONE: hedgehog_distracted_mach
				- DONE: test
			- DONE: goblin_attack_mach
				- DONE: test
			- DONE: entrance_moat_mach
				- DONE: test
			- DONE: hedgehog_eats_mach
				- DONE: update post_action()
				- DONE: test
		- DONE: migrate existing "ItemMach" obj to ItemTrigMach
			- DONE: create ItemTrigMach class
			- DONE: import ItemTrigMach class
			- DONE: migrate existing ItemMach obj
		- DONE: migrate "timer" mach obj
			- DECISION: InvisTrigMach => InvisSwitchMach
				- IDEA: timer_obj.is_dinging() is really a trigger and should be treated as such
				- IDEA: also, we want the freedom to match on NOT is_dinging()
				- DECISION: do need a 'switch' variant of MachMixIn after all => un-natural to pack trig_vals_lst
			- DONE: update auto_action:
				- DONE: for trigger_type == 'auto_act_timer' and mach_obj.is_enabled == True:
					- DONE: from mach_obj.trig_vals_lst, unpack timer_obj (trig_vals_lst[0])
					- DONE: call timer_obj.trig_check() w/ case = 'timer' ; word_lst = [timer_obj]
			- DONE: update trig_check()
				- DONE: for case = 'timer', trig_key_lst = [timer_obj.is_dinging()]
			- DONE: create SwitchMachMixIn class (inherit from TrigMachMixIn = trig_switch attrib)
			- DONE: create InvisSwitchMach class (inherit from SwitchMachMixIn + Invisible)
			- DONE: import InvisSwitchMach
			- DONE: update auto_action() : word_lst = [switch.is_dinging()]
			- DONE: update trig_check() : elim loc_trig_vals_lst ; trig_vals_lst => [True] or [False]
			- DONE: migrate existing auto_act_timer => InvisTrigMach
				- CANCEL: trig_vals_lst = [timer_obj, <is_dinging_bool>]
				- DONE: solve attrib count error
			- DONE: test
			- DONE: document format for trig_vals_lst in comments ( auto_action() )
	- DONE: migrate existing "switch" mach obj
		- DONE: investigate existing 'switch' case
			- DONE: update post_action()
			- DONE: Test
			- DONE*: invstigate 'switch' case in trig_check()
				- DECISION: make trig_vals_lst a list-of-lists
				- DONE*: update game_update
				- DONE*: update trig_check()
			- DONE: create ContainerFixedSimpleTrigMach
			- DONE: update control_panel mach obj
			- DONE: update mach_run to elim cond_switch_lst attrib passed to cond_check()
			- DONE: in cond_check(), update LeverArrayCond to pass it's own cond_switch_list attrib
			- DONE: in cond_class, elim cond_check() cond_switch_lst attrib
			- DONE: update game_update LeverArrayCond call with local cond_switch_list
			- DONE: add setters & getters to LeverArrayCond
			- DONE: test => fix lever_array cond
			- DONE: in cond_check(), update SwitchStateCond to pass it's own cond_switch_list attrib
			- DONE: add setters & getters to SwitchStateCond
			- DONE: update game_update SwitchStateCond call with local cond_switch_list
			- CANCEL: rework SwitchStateCond cond_check() to allow for all False values => default (if on True)
				- FINDING: I was right the first time ;-D
			- DONE: test (never getting to cond_check() - need to look at trig_check() )
		- DONE: clean up and optimize
			- DONE: sort out cup_of_tea game_update
			- DONE: comment out old Mach code
			- DONE: comment out old imports in game_updates
			- DONE: test dark castle
			- DONE: test cup_of_tea
			- DONE: elim cond_switch_lst from AutoMachMixIn cond_check() call			
			- DONE: clean up web_main, game_update (both)
			- DONE: clean up mach_class, pre_act, post_act, auto_act, cond_class
			- N/A: update post_action() trig_check() call as needed
			- DONE: update TrigMixIn trig_check() as needed
			- DONE: check to see if 'Warning' is reserved word in python => it's not
			- DONE: review and standardize pre_action(), post_action() and auto_action()
			- DONE: in cond_class(), update LeverArrayCond to inherit from SwitchStateCond
			- DONE: test
			- DONE: decide whether to harmonize 'timer' & 'switch' cases in trig_check() ?
				- DEC: no change
			- DONE: rethink keeping individual lists in trig_vals_lst
				- IDEA: it is tempting to have a list of lists for SwitchMachMixIn trig_vals_list...
				- IDEA: because we have this for cmd cases (i.e. a list per commands, multiple triggering cmds)
				- IDEA: but, there is only one switch (trig_switch) passed to SwitchMachMixIn... 
				- IDEA: it can have diff vals but only 1 at time
				- IDEA: therefore, there is no value to having a list of list... it only serves to confuse
				- DEC: eliminate nested list-of-lists for SwitchMachMixIn trig_vals_lst
				- DONE: update game_update, auto_act(), post_act()
			- DONE: test
			- DONE: comment clean-up mach_class(), pre_act(), cond_class(), game_update, post_act(), auto_act()
			- DONE: document format for trig_vals_lst in comments ( auto_action() and game_update() )
			- DONE: update mach doc for AutoMachMixIn, TrigMachMixIn, and SwitchMachMixIn

- DONE: review other inheritance ideas
	- DONE: review existing Warning class - refactor / integrate with Mach class
		- DONE: refactor app_turn modules (warning & timer code)
		- DONE: review existing Timer class - refactor / integrate with Mach class
		- N/A: update version build #
	- DONE: reconsider parent / child mach classes / MixIns
		- IDEA: can Warning be a parent of Mach?
		- IDEA: is Timer truly an independent class?
		- IDEA: do I want different types of Mach based on trigger_type = proto vs. auto vs. cmd vs. switch
		- IDEA: but if so, then how many MixIn varients do I end up with? Too many?	
		- DONE: de-dup warning and timer classes
	- DONE: it appears that "selective inheritance" just isn't a thing. What now?
		- IDEA: makes sense... in all other cases I inherit from simple parents to more complex children
		- IDEA: WarnClass is simpler... so it should be the parent
		- IDEA: perhaps right now I'll just make an independent class with duplicate trig_check code base
		- IDEA: as a future activity, I can look to de-dup in a more elegant fashion
- DONE: full test play
- DONE: git branch merge with master
	- DONE: 'git checkout master' to switch focus to master
	- DONE: 'git branch: to confirm focus
	- DONE: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
	- DONE: 'git push' to push merge to origin (GitHub)
	- DONE: confirm that origin is updated
	- DONE: confirm that code is updated and still runs
	- DONE: 'git branch -d <FEATURE_NAME>' to clean-up local branch
	- DONE: 'git push origin --delete <FEATURE_NAME>' to clean up origin
	- DONE: confirm origin is cleaned up
	- DONE: post-branch-delete run test
	- DONE: update cleesh engine version build


- DONE: fix VS Code error checking / pylance or whatever is wrong
	- DONE: tried un-installing and re-installing python extension & pylance (Sept 17)
	- DONE: moved vscode.exe from Downloads to Applications and was then able to upgrade => Pylance works!
		- LINK: https://github.com/microsoft/vscode/issues/7426#issuecomment-425093469


- TBD: Cases where I want a modular machine to run despite an error standard (build 0011 [])
	- IDEA: problem description
		- IDEA: e.g. 'go north' in antechamber triggers goblin
		- IDEA: i.e. should it ever be possible to override an error? If so, then how?
		- IDEA: the 'open portcullis' case is a special problem here - it will tell Burt it's locked...
			- IDEA: but the Goblin should attack before Burt can touch the Portcullis
	- IDEA: general thinking / philosophy
		- IDEA: narrative shoudld be able to trump simulation rules if desired (but it may take extra work)
		- IDEA: use fake_door for now and swap on goblin death ?
		- DEC: 'take axe' case is hard to fake out... I think I do need a systemic soluiton after-all
	- IDEA: basic approach
		- IDEA: what we really need to do is differentiate between "attemptable" failure vs. "impossible"
		- IDEA: attempting to open a locked door is the poster child for this
			- IDEA: it is reasonable for the player to attempt a new door they find
			- IDEA: in fact, they can only learn that it is locked by making the attempt
			- IDEA: further, if there is a guard in the room, it is reasonably that they take action
			- IDEA: against a player that is rattling the locked door they are guarding
		- IDEA: by contrast: 'eat horseshoe' (when there is no nearby horseshoe) is NOT attemptable
			- IDEA: and should not be dignified by a pre_action() response
	- IDEA: possible "attemptable" implementation
		- IDEA: perhaps re-org app_main()
			- IDEA: interp => val_err => auto_act => pre_act => val_att => cmd_exe => post_acct
		- IDEA: in Invisible, create separate <verb>_att method right after each <verb>_err method
			- IDEA: validated_att() checks for attemptable errors and returns if they are found
		- IDEA: alternatively, maybe new Errors class inherits from Invisible ?
			- IDEA: appears that only Writing inherits directly from Invisible?
		- IDEA: in errors, return is_attemptable
			- IDEA: if is_attemptable == True, time passes, and both pre_act() and auto_act() run
		- IDEA: all errors that return useful info (e.g. 'locked door') are attemptable
			- IDEA: is_attemptable = False for all cases where the obj is not in room
			- IDEA: in between is tricky... 
			- IDEA: go <direction w/ no exit> and take <obj held by creature> are good attemptable candidates
	- DONE: alternative work-arounds:
		- CANCEL: Maybe just 'x axe' case?
			- NA: update take_err() creature check - allow hostile reaction if burt attempts to take goblin axe?
		- CANCEL: possible solution 1
			- IDEA: creation of a pre-validate() module called interupt() that can over-ride errors
			- IDEA: modular machines should be designed so that it is easy to trigger & run them from interupt()
		- DEC: want a more consistent approach
	- INPROC: sort out Error class idea
		- DONE: create fresh map of class inheritance
			- DONE: map class_std classes
			- DONE: map class_gs classes
			- DONE: map class_mach classes

		- TBD: create new <FEATURE_NAME>_feature git branch [attemptable_error]
			- TBD: 'git branch' to confirm *master
			- TBD: 'git branch <FEATURE_NAME>' to create new branch
			- TBD: 'git branch' to confirm new branch exists but that master is still checked out
			- TBD: 'git checkout <FEATURE_NAME>' to switch focus to branching_test branch
			- TBD: 'git branch' to confirm new branch is now in focus
			- TBD: Publish Branch via VS Code button
			- TBD: confirm new branch on GitHub
			- TBD: update doc TBDs to DONEs
			- TBD: <CMD><OPT>S (to save all files)
			- TBD: 'git add .' to add files to be committed
			- TBD: 'git commit -m "doc updates"
			- TBD: 'git push" to push updates to origin (GitHub)
			- TBD: confirm new branch on GitHub is now ahead of master

		- TBD: sort out Invisible and Error classes
			- IDEA: all non-MixIn classes should inherit from Invisible
			- IDEA: Invisible itself should only hold the 'name' attrib and print footer
			- TBD: gs_class classes inherit from Invisible
				- TBD: test
			- TBD: base condition and result classes inherit from Invisible
				- TBD: test
			- TBD: TangibleIdentity class
				- TBD: fix / elim has_cond() identity in AutoMachMixIn [=> has_cond_result() ??]
				- TBD: elim has_switch and has_trigger identities ??
				- TBD: create Identity (inherits from Invisible) in identity_class module in class_std pkg
				- TBD: Writing inherits from Identity
				- TBD: migrate all tangible identity func to Identity but keep abstract identity in Invisible
					- EXAMPLE: abstract == is_timer, is_mach, is_warning, and maybe is_switch (???)
				- TBD: test
			- TBD: move where_is() debug method to ViewOnly
			- TBD: Error class
				- TBD: create error_class() module in class_std
				- TBD: create Error class in error() which inherits from Identity
				- TBD: updated Writing to inherit from Error
				- TBD: copy all err methods to Error (and global debug methods too)
				- TBD: tripple-quote elim all err from Invisible
				- TBD: test
		- TBD: clean up invisible_class() and Writing in base_class()
	- TBD: re-order auto_act to start of app-main loop
		- IDEA: interp => val_err => auto_act => pre_act => val_att => cmd_exe => post_acct
		- TBD:
	- TBD: create attempt_err()
		- TBD: create attempt_err() module
		- TBD: create attmept_err() function
		- TBD: similar code to validate but call <verb>_att
		- TBD: add attempt_err() to app_main loop after pre_action() and before cmd_exe()
	- TBD: create <verb>_att methods in Error
	- TBD: document Error updates and categories in doc
	- TBD: consider whether hidden rooms s, e, & w of Entrance can be eliminated (needed for paths?)

	- TBD: git branch merge with master
		- TBD: 'git checkout master' to switch focus to master
		- TBD: 'git branch: to confirm focus
		- TBD: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
		- TBD: 'git push' to push merge to origin (GitHub)
		- TBD: confirm that origin is updated
		- TBD: confirm that code is updated and still runs
		- TBD: 'git branch -d <FEATURE_NAME>' to clean-up local branch
		- TBD: 'git push origin --delete <FEATURE_NAME>' to clean up origin
		- TBD: confirm origin is cleaned up
		- TBD: post-branch-delete run test

	- TBD: update cleesh engine version build


- TBD: would be nice to have an Error class that inherits from Invisible [FUTURE]
	- IDEA: but this would break in heritance?
	- IDEA: or maybe Writing just needs to inherit from Error ?

- TBD: state machine for hedgehog [FUTURE]
	- IDEA: need to implement hedgehog state machine based on creature state
		- IDEA: Both hedgehog and throne_broach_dispenser would be better implemented as state machines
		- TBD: state machines and other general purpose mod-machs
	- TBD: update cleesh engine version build

- TBD: consider introducing an event bus [FUTURE]
	- IDEA: if cmd passes validate => event bus
	- IDEA: invisible triggers / switches: in hedgehog_eats_mach, give() command should set trigger (not cmd)
		- FINDING: Invis Trigger Idea = Event Bus Idea => 'burt-give-stale_biscuits-royal_hedgehog'
	- IDEA: does Event Bus work well cmd_exe() ?
		- CONCERN: need to process commands... is it easy to process commands from events???
	- IDEA: need to learn more about event busses, topics, message formats
	- IDEA: message field => type (e.g. 'cmd'), event_key, cmd_terms ('case' and word_lst)
	- IDEA: event bus idea
		- IDEA: would hold all commands, timer 'ticks', and state changes (e.g. switches)
		- IDEA: for event bus, consider moving auto_action() to front of app_main() run order

- IDEA: triggers [FUTURE]
	- IDEA: Modular Triggers? (named after intent; match cond, result, & mach)
	- IDEA: Establish switch triggers such that timer as trigger is more natural
	- TBD: update cleesh engine version build


- TBD: mod-mach bug fixes
	- TBD: fix hedgehog description after sword is returned (before goblin killed)
	- TBD: auto_static_behavior for goblin? each turn - maybe should be a standard function??
		EXAMPLE: "the goblin is eyeing you coldly"
	- TBD: fix eat_biscuits_warning 
		- TBD so that it no longer lives in just entrance and main_hall 
		- TBD: and no longer triggers when biscuits not in hand
		- IDEA:  making eat_biscuits_warning universal and enabling success feedback loop for cmd_exe
	- TBD: Do we really need to test for goblin in antechamber??? (will the goblin ever move)
	- TBD: should hedgehog_distracted_mach just be replaced by a Creature class attribute?
	- IDEA: Can we create a general purpose Dispenser machine - for use with Crown and Broach?
		- IDEA: would also be useful for control_panel
	- TBD: broaden hedgehog response to interacting with sword (e.g. "pull sword" should trigger)
- TBD: update cleesh engine version build

- TBD: debug ideas:
	- IDEA: room should have show_machs() method that lists all local mod-machs
	- TBD: mach visible command (include switchs, warnings, and timers too)
	- TBD: machine purpose and state command (include warnings and timers too)
	- IDEA: machine mix-in should have a dbg_describe() method that describes the machine (like K8s)
	- IDEA: dbg_describe and debug_show_mach commands
		- IDEA: to keep obj names short, just use abreviations <mach_name>_r1_m1
		- IDEA: to understant what mod-mach does, have attribute that explains each module
		- IDEA: also explains each result and condition
		- IDEA: then have debug-only command that describes mod-mach based on that attribute
		- IDEA: would also presumably need debug_show_mach command
	- TBD: update cleesh engine version build

- TBD: in mk_def_pkl(), sort out more elegant assignment process for self referenced obj
	- EXAMPLE: re-assigning goblin to goblin_mach after goblin Creature instantiation
	- ANALYSIS: basic problem pattern = obj => obj_mach => obj_cond / obj_result => obj
	- IDEA: pass/link obj to obj_con/obj_result innately (not explicitly) as part of call/assignment?
	- TBD: update cleesh engine version build

- TBD: update modular machine doc!

	- TBD: <TEMPLATE>
		- TBD: create new <FEATURE_NAME>_feature git branch
			- TBD: 'git branch' to confirm *master
			- TBD: 'git branch <FEATURE_NAME>' to create new branch
			- TBD: 'git branch' to confirm new branch exists but that master is still checked out
			- TBD: 'git checkout <FEATURE_NAME>' to switch focus to branching_test branch
			- TBD: 'git branch' to confirm new branch is now in focus
			- TBD: Publish Branch via VS Code button
			- TBD: confirm new branch on GitHub
			- TBD: update doc TBDs to DONEs
			- TBD: <CMD><OPT>S (to save all files)
			- TBD: 'git add .' to add files to be committed
			- TBD: 'git commit -m "doc updates"
			- TBD: 'git push" to push updates to origin (GitHub)
			- TBD: confirm new branch on GitHub is now ahead of master
		- TBD: refactor <CODE CHANGES>
			- TBD: result class updates
				- TBD: copy existing class; change parent to BaseResult and update class name
				- TBD: update attribs and setters and getters
				- TBD: update result_exe() attribs
				- TBD: use return super().result_exe() to return BaseResult buffer and mach_state (update class)
				- TBD: specific class changes: <list here>
			- TBD: update game files
				- TBD: add new result class to game_update imports
				- TBD: update Result obj name if appropriate
				- TBD: update game_update result obj classes, attribs, and post-assignment updates
				- TBD: set mach_state appropriately
				- TBD: update post-attrib assignment if needed
				- TBD: add result name to mach_run() exception list
				- TBD: comment out old result class and remove from import (in new name)
			- TBD: test & clean-up
				- TBD: test
				- TBD: clean-up game_update(), result_class(), mach_class() [??]
		- TBD: git branch merge with master
			- TBD: 'git checkout master' to switch focus to master
			- TBD: 'git branch: to confirm focus
			- TBD: 'git merge <FEATURE_NAME> -m "branch <FEATURE_NAME> merge"'
			- TBD: 'git push' to push merge to origin (GitHub)
			- TBD: confirm that origin is updated
			- TBD: confirm that code is updated and still runs
			- TBD: 'git branch -d <FEATURE_NAME>' to clean-up local branch
			- TBD: 'git push origin --delete <FEATURE_NAME>' to clean up origin
			- TBD: confirm origin is cleaned up
			- TBD: post-branch-delete run test


*** Eliminated Code ***
	def run_mach(self, gs):
		cond_return_lst = []
		for cond in self.cond_lst:
			cond_return = cond.cond_check(gs, self.mach_state, self.cond_swicth_lst)
			cond_return_lst.append(cond_return)
		result_index = cond_return_lst.index(True)
		result = self.result_lst[result_index]
		temp_mach_state, cmd_override = result.result_exe(gs, self.mach_state)
		self.mach_state = temp_mach_state
		return cmd_override, result.name

# *** start unused code for combo conditions ***

# *** sample input = [['and', cond_1, cond_2]['or', cond_3, cond_4], cond_5] ***

#	def run_mach(self, gs):
##		print(f"mach running; mach_name = {self.name}") # for troubleshooting
#		for idx, cond in enumerate(self.cond_lst):
#			if isinstance(cond, list):
#				term_1 = cond[1].cond_check(gs, self.mach_state, self.cond_swicth_lst)
#				for condition in cond[2:]:
#					term_2 = condition.cond_check(gs, self.mach_state, self.cond_swicth_lst)
#					if cond[0] == 'and':
#						combo = term_1 and term_2
#					elif cond[0] == 'or':
#						combo = term_1 and term_2
#					term_1 = combo
#				if combo:
#					result = self.result_lst[idx]
#					self.mach_state, cmd_override = result.result_exe(gs, self.mach_state)
#					return cmd_override, result.name
#			else:
#				if cond.cond_check(gs, self.mach_state, self.cond_swicth_lst):
#					result = self.result_lst[idx]
#					self.mach_state, cmd_override = result.result_exe(gs, self.mach_state)
#					return cmd_override, result.name

# *** end unused code for combo conditions ***


*** already done ***
- DONE: How to enable switches and machines to self register for universal scope
	- EXAMPE: battery powered lamp must track usage even if Burt has dropped it and walked away
	- DONE: eliminate universal_scope => just add these to Burt's invis_lst

- DONE: review mod-mach improvement ideas:
	- CANCEL: initial ideas
		- IDEA: goal is a single method for conditions and a single method for results (???)
		- IDEA: for conditions, attributes = modules + logic_str + descript_str
		- IDEA: use attribute packing / kwargs to pack conditions / results with variable # of attributes
	- CANCEL: naming
		- IDEA: Shorter cond & result names!!
		- IDEA: Compound Results and Conditions named after intent
		- IDEA: naming conventions: need to avoid confusion between match_state and mach_state
		- IDEA: naming conventions: cond & result name should be same except post-fix
		- IDEA: address long naming issue with describe() ability
	- DONE: general org ideas
		- DONE: BaseCond => always check state
		- DONE: BaseResult => always do a buff_try()
		- DONE: All results capable of Buffering (rename Result classes appropriately)
		- DONE: if no conditions == True then default_result = nothing happens (no need for pass_result)
		- CANCEL: in machines, should conditions and results just be key-value pairs in a dictionary?
			- IDEA: As opposed to needing 2 separate lists with identical indexes?
	- DONE: primative conditions & results modules
		- DONE: goal of primative & compound structure is to increase re-use of Cond & Result classes 
			- IDEA: currently too many class-per-var cases
		- DONE: Primative Conditions (named after condition) [always include single attribute & value] 
		- CANCEL: Compound Conditions (and / or) 
			- IDEA: named after intent; match mach, result, & trig 
			- IDEA: {trig_check() method links primatives}
		- DONE: Primative Results (named after result) [always include single attribute & value] 
		- DONE: Compound Results (named after intent
			- IDEA: match cond, trig, & mach) 
			- IDEA: {trig_check() method links primatives}
	- DONE: Composed Conditions & Results: comp_cond / comp_result == AND / OR of multiple primatives
		- CANCEL: like the idea of AND vs. OR option
		- DONE: NOT option for each cond module is vital (achieved via 'match')
			- EXMP: Generalize in-hand vs. not-in-hand Condition (single primative)
			- EXMP: Generalize creature-has-item vs. creature-does-not-have-item Cond (single primative)
		- IDEA: each 'primitive' cond tests for *one* thing (but state of thing is attrib to be matched)
	- DONE: Have simple, 1-test/ 1-action 'Primative' Conditions and Results: prim_cond and prim_result
		- IDEA: would we really want each primative cond & rslt linked?
		- IDEA: lean towards composing result_1 from r1_m1, r1_m2, & r1_m3 => linked to comp cond
	- DONE: Wildcard clean-ups
		- IDEA: Extend trig_check wildcards to 'post_act_cmd' & 'auto_act_cmd'
		- IDEA: Extend trig_check wildcards to work with Warnings (or de-dup Warning's trig_check)
		- IDEA: guard against multiple wildcaards per list
	- DONE: Results
		- IDEA: extend BufferOnlyResult result_exe method in BufferAndEndResult and BufferAndGiveResult
		- IDEA: extend child methods in results_class_def ?

- DONE: list of 'contained' internal_switches in MachMixIn attributes?
	- IDEA: (i.e. add to scope and remove levers & button from features?)
	- IDEA: [hold off until at least one more control_panel type machine gets created]

- DONE: sort out ability to push button / pull levers while goblin is guarding

- DONE: Establish clearer nomenclature for temp variables that will be fully assigned at end
	- EXMP: 'royal_hedgehog-*temp*'




# *** FUTURE TO DO *** #

*** debug ideas ***
- TBD: instantiate obj in hero inventory

*** story-driven updates ***

- IDEA: maybe the hedgehog should act differently once you get & wear the crown?

- TBD: sort out hedgehog description post biscuits if Burt leaves rm

- TBD: hedgehog will trade sword for silver_key (update show() and give() )

- TBD: find a good use for TravelResult !!

- TBD: fix case where sword is in Burt's inventory and tries to take in Entrance but royal_hedgehog stops him

- TBD: sort out double print of score after win

- TBD: case where player drops sword in same room as hedgehog after using it... 
	- TBD: need to update description / situation; perhaps should give key and change to adoring description?

- TBD: hedgehog description should change when distracted by food
- Fix Antechamber description sill mentions goblin after death
- search for 'Nana'-based errors
- Fix: 'officious' == offering unwanted advice => NOT hidebound or miro-managerial

- maybe replace the current debug code (C64 poke) with magic word ('xyzzy') ?
- update 'eat biscuit' warning text... should ref baker job and Nana
- update hedgehog description while eating to "The RH is ravenously eating"

- TBD: fix Goblin description to no longer mention Control Panel
- TBD: "what would your mothter say" error to "What would your Nana say?"
- TBD: update winning condition to reading scroll while sitting on throne?
- TBD: Stone Coffer => no-lid box ?

- TBD: play & note obvious nouns with no description; provide description (e.g. 'keyhole')
- TBD: search on obj nouns and ensure always capitalized
- TBD: make path names (provided via 'l') examinable nouns ('path' => Winding Path)
- TBD: fix post-goblin-slain Antechamber description
- TBD: update win condition to must be sitting on throne

- TBD: Description updates:
	- TBD: hedgehog updates
		- describe as "stallwart"
		- Have the hedgehog think burt is playing if he attacks with a non-weapon; starts making wax-on, wax-off motions with paws
		- Upate water_bottle to Enchanter jug
		- Update shiny_sword to Zork I elven sword
	- TBD: Updatate the trademark on the stale_biscuits... 
		- perhaps the biscuits say "Nana's" - or better yet, have a sword-and-key emblam on them?
		- backstory of Nana fondly feeding hedgehog biscuits back when she was at the castle?

- TBD: tune goblin and hedgehog text; maybe add a faded poster of ancient and unreasonale regulations to the antechamber wall?

*-- STORY IDEAS --*
- link lantern, sword, and jug to Infocom history but unify with fantasy genre (no battery)
- valor; caprecious and messy sort of valor - sort of show up three sheets to the wind but ready to save the day
- shiny sword glows near enemies?
- meet the wizard from Enchanter who is searching for a scroll


*** Refactor app_main() modules ***
- TBD: refactor remaining app_main chain: pre_action, cmd_exe, post_action, auto_action
- TBD: use __getattr__ and __setattr__ methods to make dict accessible as obj
- TBD: refactor GameState & dicts in static_gbl() with dunder methods ( __getattr__ and __setattr__ )
	- LINK: see: https://stackoverflow.com/questions/10761779/when-to-use-getattr
	- TBD: create dict_class_def.py w/ StaticDict and __getattr___ (and s__setattr__ for future tools)


*** refactor Creature ***
- Sort out the wierd thing where unarmed attack is represented by first item in feature_lst

- TBD: does creature_state really have any value? Maybe build hedgehog state machine before pulling the plug on this one
- TBD: Could simplify 'give', remove description updates from give, and instead implement them as part of state machine?

- TBD: should it be possible to show() an obj of class Writing or ViewOnly ??
	- TBD: enable 'show writing to creature' is writing is on an item Burt is holding

- TBD: make creature obj data more atomic
	- TBD: create weapon() method to provide adj & adv (vs reading weapon_dict via attack() )
		- IDEA: obj should be a black-box
	- TBD: same idea for 'can't attack error' for attack() in invisible(); should be creature() meth

- IDEA: Distracted state & description as creature attribute; inhibits 'show', 'give', attack 'commands'
	- "The create to distracted to notice what you are showing them"
	- "You think better of attacking the distracted creature"
- IDEA: Creature state is linked to descript; e.g. hedgehog_descript_1
- IDEAD: machine result changes Creature State; State machine itself changes creature attributes based on state
	- e.g. start timer, description, machine active, distracted attribute, etc

*** refactor Interactive ***
- TBD: clean up and make more efficient
- TBD: should "put key in moat" do more? what about "enter moat"
- TBD: Sort out prepositional spaces (e.g. Under, Nook, Hole, Bed) ***
- TBD: maybe a Bed in the Main Hall?
- TBD: maybe a fireplace in the Main Hall (class = Nook)? Or better yet, Alcove as class Nook?

- TBD: the future list - future interactive obj updates / features to be implemented
	- framework for complex obj to contain sub-elements (e.g. drawer + surface + under == desk)
	- Could also have UnderMixIn and BehindMixIn
	- TBD: for UnderMixIn - need to include bulk capacity for negative space
	- would need to deal with the wording 'look under' and 'look behind'
	- 'look under' adds contents to room.feature_lst
	- additional 'under' commands = 'put under' and 'reach under'
	- for MixInHole have commands 'look in' and 'reach in'
		- can a 'hole' be dark if the room is light?
	- TBD: enable the 'behind' preposition (with multiple varients of obfustication)
		- IDEA: minor_behind = you can see but not reach
		- IDEA: moderate_behind = can see some
		- IDEA" major_behind = can't see
		- Presumably, all 3 flavors of behind impact availability of obj in room list
		- TBD: put the control_panel behind the goblin (check TADS implementation)
	- IDEA: 'hole' = contain, opaque from room, no light
		- 'nook' = 'hole' that can contain Creatures
		- 'under' = opaque from room but no lighting issues
		- use 'take from under' for 'under'
		- use 'reach in' for 'hol'
		- need to enter() 'nook' to get contents

- TBD: figure out 'behind' prep for case of control panel in alove behind goblin

- non-humanoid monster could be a special weapon description case (fun new puzzle idea)???
- DONE: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
	- encumberance (post Burt as object?)
	- implement carying capacity / container cappacity; Also carry restriction passages, etc..
- DONE: make goblin hand contents examinable (e.g. Grimy Axe)


*** Roll up sleaves and fix Interpreter ***

*** Commands List ***
- if you meet a person:
	- Talk to <name>
	- Tell <name> about <X>
	- Give <thing> to <name>
	- Show <thing> to <name>

- If you find a thing:
	- Turn <X>
	- Feel <X>
	- Fill <X>
	- Smell <X>
	- Listen to <X>
	- Break <X>
	- Burn <X>
	- Look under <X>
	- Climb <X>
	- Wave <X>
	- Take <X> off
	- Turn <X> on
	- Dig in <X>
	- Enter <X>
	- Search <X>

- Also
	- Listen
	- Sleep
	- Wake up
	- Undo
	- Jump
	- Pray
	- Curse
	- Sing

- TBD: implement curse warning / ending at Interpreter() level

- TBD: read for DCv3 parser ideas: https://medium.com/swlh/zork-the-great-inner-workings-b68012952bdc

- TBD: fix interp() prep_verb noun vs. dirobj nomenclature once and for all!
	IDEA: swap to meth_noun_str and attrib_noun_str ??

- TBD: consider introducing str_to_obj_dict in Core (enable ease of entrance.examine(gs) in startup() )
- TBD: interpreter idea => permitted verbs & synonymbs by class (e.g. 'doff' for Garment)

- IDEA: in interp(), what about making prep check similar to put() for all prep verbs
	- IDEA: could have a prep attribute for each prep verb
	- IDEA: in interp(), have a list of all possible preps and use list to break sentence

- IDEA: next interp() goals:
	- IDEA: noun synonyms (different than abreviations)
	- IDEA: global verb synonyms
	- IDEA: simple prep verbs ('sit_in')
	- IDEA: basic interp features: 'take all', 'again', 'wait'
	- IDEA: address 'I can't see a x_y' error
- IDEA: introduce a vs. an

- TBD: text UI updates:
	- TBD: sort out 'can't drop fist or brass_lantern issue
	- TBD: change backpack and worn lists to include 'a' and 'an'
		- IDEA: convert plurals to singulars for this???
		- IDEA: (given that there is water in the game maybe all singlulars is impossible?)
		- IDEA: maybe a txt_handling() module with a disp_lst() func that takes care of 1) "x", "x & y", "x, y, & z"; 2) 'a' or 'an'; 3) plurals
	- TBD: sort out approach to plurals
		- 1) perhaps this becomes a ViewOnly attribute??? (don't like this - way too many un-used cases of attribute)
		- 2) possibly ItemPlural class inherits from Item and has method is_plural() which returns True ??
		- 3) could just have a plural_tuning_lst in the txt_handling() module that checks for known plurals as a one-off?
			- `Note: the problem with defining plurals in classes is, what if I want to establish plurals for a non-obj (e.g. a path)
		- Maybe apply 'xxy' prefix on text list if plural??
	- TBD: drop node 3 (portable_containers in containers) disp?
		- TBD: can burt know about node 3 items he hasn't 'seen' in this game?
		- TBD: play through Zork kitchen to test out

- TBD: exit() should apply to chairs and doors => move to Perch / Nook class
- TBD: should have 'go in gate' and 'enter gate' as synonyms for 'go north' from entrance? (doors & rooms ??)

- Do I need a gs.Gramarian class to deal with recurring display issues around pronouns and plurals?
	- e.g. pronoun_tobe(creature) => 'You are' or 'The <creature.full_name> is'
	- e.g. article_plural(obj) => 'a Grimy Axe' or 'Water' or 'an Apple'
	- maybe plural_dict is a local dict in the Gramarian class?
	- Or maybe a better class name is just Display (???)
	- Division of labor: player text => commands == Interp; obj => player response == Output
	- could put some recurring dispaly routines here (obj_lst => str_lst and such) ??
	- Display could also hold buffer commands???
	- Another possible class name == Output ???
	- Leaning towards Output... this helps distinguish from all the verb-linked Disp methods

- TBD: create a version just for interp() updates and gather all interp updates there!!
- IDEA: verb synonyms per obj with 'move' as a broadly used and variable synonym??
	- verb synonuyms linked to class / class method?
	- perhaps additional, optional cusotm verb synonyms as an obj attribute?
- TBD: implement global verb synonyms for 'sit in' or 'sit on' == enter()
	- TBD: also want to enable 'go in' and 'go out' of chair

- TBD: interpreter - should all nouns be singular? Can 'a' vs. 'an' be fixed?

- Interp deep dive including better solution to prep checking ('put in' vs. 'put on')

interpreter ideas:
- can I store variables in static_dict strings? (in f-string format)
- can I return method errors based on verb method (e.g. "Burt, what kind of person would try to attack a Throne?")
- should synonyms be an obj attribute??
- more abreviations: 'g' = 'again', 'z' = 'wait'
- fix progromatic usage of "a" vs "an" (e.g. "There is a Iron Portcullis to the north")

- DONE: unlock => 'unlock with' prep  command
- DONE: default prep behavior = try command with obj in hand
- New interp() Ideas:
	- interp() refacto shoud be based on objects (contents of rooom)
	- each obj should have noun syns (in place of root_word)
	- if user input has multiple obj, determine noun vs. dir_obj from prep usage (i.e. to vs with)
	- have global verb syns and class-based verb syns (start with global; much easier!)
		- e.g. 'get' is gbl verb syn for take() but 'sit on' is a Seat class verb syn for enter()
	- based on verb, validate prep usage
	- Order of Op: 1) obj noun syns, 2) gbl verb syns

*-- INTERPRETER ENHANCEMENT --*
- TBD: sort out synonyms like 'stand' and 'sit' and 'lie'
- Interpreter enhancements:
	- noun synonyms (list in place of base_name)
	- verb synonyms (attribute of Class? Should verbs associated with obj???)
	- enable "take all", "drop all"
	- randomize frequent responses (e.g. "in your spell book you see...")
- re-institue remove() verb for Garment; 'take' as synonym
	- worn obj take() => "You're already wearing it"
	- obj on floor remove() => "Taken" (i.e. is synonym)
- assume that item in hand will be used for activity (e.g. attack)
- move() command ?
- enable 'take all'
- create 'jump' command with same response as Zork ('Whee!' I think?)
- randomize description of Burt shown during 'inventory'
- convert words like 'look' to 2word in interp(), rather than cmd(), if possible

*-- ARCHITECTURE --*
- What would a decoupled, micro=services based DC look like? What are the consumers / providers?


*** get on the web and start working in the open! ***
- TBD: figure out multi-user
- TBD: get flask on Amazon Linux 2023 on EC2 working!
- TBD: Have 'prod' game tab, 'legacy' tab, and 'dev' tab
- TBD: link mac updates to dev tab via pipelines
- TBD: link dev tab to prod during manual updates
- TBD: pull in DB migration to get ready for web

*** cup_of_tea enhancements ***
- IDEA: need to provide default engine mechanisms with option to replace with custom game versions
	- IDEA: assume a 'lazy game designer' who doesn't create custom values; should work anyhow
	- TBD: need a default set of titles title_factor that can be over-ridden with game-specific
- TBD: future updates for cup_of_tea (this will eventually be the setup for why Burt went to DC)
	- TBD: need to fix door (have pub folks charge in)
	- IDEA: to drink tea, Cecily must lock front door, sit in comfy chair, read book, eat biscuit
	- IDEA: also, she must get rid of Burt who wants her attention (give rusty_key to burt)
	- IDEA: Cecily sort of likes Burt - he's better than that Gaston fellow - but overgrown puppy
	- IDEA: night before, Burt was bragging to whole pub about how he would storm Dark Castle, get treasure
	- IDEA: Winning condition = drink Tea; Time up when pub opens (belching contest begins); 9 bells
	- IDEA: Gaston keeps flirting with her sister; big-headed and constantly singing...
	- IDEA: book is riff on LotR; 
		- IDEA: office workers on death march project; must bring TTL report to shredder
		- IDEA: led by bearded application developer, heart-string-pulling retirement party at end
		- IDEA: always saved by IT person at critical moment

*** Enable Verbe Methods for Machines ***
- IDEA: enable silent run mode for verb methods so that I can use them in result_exe()
- IDEA: start with Item.take() => TakeResult

*** Introduce multi-room puzzle ***
- IDEA: trigger in one room, switch in 2nd room, effect in 3rd room

*** New Room Update ***
- IDEA: convert Moat to actual rooms?
	- IDEA: Create on_the_moat room that e, w, d lead to 
	- IDEA: unarmed players get one turn before croc attacks
	- IDEA: no floor to room (items drop down several rooms)

*** Get light working ***
- IDEA: what to do on container (or other) loss of light?
	- e.g. put lantern in box, close box (no stuck)
	- had thought about lighting up box from interiour - but wouldn't work for switch
	- is safe to actually turn off lantern - because anything in your hand can still be accessed...
	- so alternate idea is that hedgehog has to come rescue you
	- but at least one inventory item gets scattered (hedgehog shrug)

*-- AMBIENT SIM --*
- for light sources:
	- "(providing light)" in inventory; also is a condition (on)
	- can move into a dark room, but can't open a container in the dark
- for FlamableItem: light & burn (e.g. matches)
- PaperItem: burns; also, if writing, ink runs and becomes unreadable

- darkness & light source system?
	- lantern (requires darkness travel tracker, timer, item_mach, univeral scope, death by grue)
	- honestly, Grues don't make sense in DC... I intend for there to be a fair number of creatures around the place... why haven't they been eaten by Grues? (one could ask the same about the Troll and the Thief of Zork - but presumably these are dangerous creatures that can fend off Grues?). Instead, I think I'll use the same mechanic (2 dark rooms in a row == death) but the textual explanation will be Nana's warning to young burt "Burty, you mind gallavanting around in the darkness - you'll trip and break your neck!"


*** Get liquids working ***
- Liquid handling
	- INPROC: Research IF liquids
		- DONE: Infocom
			- Zork: Glass Bottle 
				- has one 'quantity of water'
				- bottle must be held to be drunk
				- bottle must be openned to be drunk
			- Enchanter: Jug
				- has multiple quantities of water
				- jug has no 'cap': "The jug has no cover. It can't be openned or closed."
				- must be at least a little 'thirsty' to drink water
			- Other uses (in Zork):
				- Water can be poured on flame to put it out
				- Water can be poured on the heated bell to cool it
		- TBD: how does TADS do it??
	- INPROC: Long-term Liquid plans
		- Liquid class
			- The primary liquid in the game will be water
			- An important point of awareness is that 'water' (unlike all other nouns) cannot be guaranteed to be unique
			- Main liquid verbs = drink(), pour(), fill()
				- where 'Y' is a Liquid and 'X' and 'Z' are containers / bodies of water
				- drink() : 'drink Y from X'
					- Liquid method
				- pour() : 'pour X from Y in / on Z'
					- ContainerPortableSimple method
				- fill() : 'fill X with Y from Z'
					- ContainsMixIn method
			- - IDEA: Advanced verbs: mix(), stir(), shake()	
		- Non Liquid class properties related to liquids
			- If water is poured in or on an object it has an effect:
				- no special results (if the obj is a Container then it holds the water)
				- Obj unimpacted but water 'evaporates'
				- Obj is ruined / disolved / rendered illegible (e.g. paper note); water "evaporates"
				- Heated obj is cooled (Zork example; future)
				- Flame is extinquished (Zork example; future)
				- note that these effects are properties of the objects - NOT the liquid class
			- Implementation:
				- for ViewOnly class and below, need an attribute: liquid_result
					- defines what happens to the obj when it contacts liquid
					- also defines what happens to the liquid when it contacts the obj
		- Special case of bodies of water
			- does an object sink or flat?
			- this can get complicated 
				- maybe keep the Entrance 'well' to a shallow rainwater-fed pool
				- test with Enchanter spring
		- Special case of immersion
			- You should be able to swim in water and diver under water
			- Breathing limits will apply
			- This will mostly be independent of Liquids... 
				- but anything with a 'ruin' liquid_result == 'ruin' should be destroyed by swimming


*** Get food / hunger and beverages / thirst working ***
- IDEA: interesting updates for food & bulk
	- require eating
	- enable Water to be drunk in small amounts (multiple servers per filled bottle)
	- enable same partial consumption for bread loaf (calls back to Enchanter)
	- Make sips of water / bites of bread the one frational bulk amount in game
	- Enables interesting weight puzzle (4 gallons from 3 & 5 gallon buckets)
	- Maybe stale_biscuits => 3 biscuits in paper package (Nana sword & key logo; better than McV ref?)
	- Perhaps for bulk puzzle, have a Pywrong beaker - extremely fragile - breaks if put in pack or dropped

- TBD: hunger & thirst become Creature conditions to examine??

- IDEA: for food, maybe have the biscuits take 3 turns to eat... but if burt eats some he gets less time to grab the sword... 
- IDEA: maybe don't need warning so much... just keep describing them as tasting worse and worse? Food consistent within creatures?

- food & drink system?
- hunger & thirst to be indepedent boolean settings in gs.core
- hunger & thirst durations settable in gs.core

Food:
- bread for Burt (save piecs of cheese for the mice)
- maybe need to keep feeding biscuits to the hedgehog?
- perhaps loaf of bread and bottle of water can each provide multiple servers (similar to enchanter)
- additional bread verbs needed: bake ???

*** Get tiredness and sleep working ***
- sleep to be a setable boolean in gs.core; also setable duration

- maybe sleep in bed (after min # of moves) to dream to get hints? But light must be on so you loose turns of light and wake up hungry and thirsty? Hint is provided randomly based on points not yet accrued?
- need to check Enchanter to find length of days, when sleep needed, food & drink, etc
- For dream hint: Burt has dream / memory of Nana teaching him the binary code she would use with Willy while secretly courting (she was a lunch lady?) to set a time to sneak off with him. Would involve 2 types of biscuits on counter... Nana's Own and McVittles (which were awful)... she only had room for 3 biscuits but had to show times from 0 to 7... 


*** Introduce fire & heat ***
- TBD: a thermal attribute for obj that cools over time (hot_tea => warm_tea => cold_tea)


*** Introduce transparency ***
- e.g. Crystal Box should show kinging_scroll / empty / contents
- TBD: an hour glass machine (changes time as turns pass; has flip() verb) 
- Window: would be need to have a Window class that allows burt to see what he can't take


*** Implement Symetric Verbs ***
- TBD: as part of symetric functions reveiw...
	- re-examine current use of creature = gs.core.hero
	- if non-hero creatures never hit errors... do we need this in the Invisible class ??

- enable all verb methods for non-burt creatures
- TBD: doc_string about future 'silent_exe' for symetric creature commandsv
- TBD: test with test_frog holding test_box (PortableContainer) holding red_mcguffin Item
- TBD: tune pronouns
- IDEA: errors are only for burt
- IDEA: auto-gen descriptions (e.g. drink, eat, wear, sit) are only for burt
- TBD: doc_string on 'semi-symetric' methods
- TBD: enable non-burt creature use of all verb methods 
- TBD: how should creature be passed to Conditions & Results?
- TBD: how to deal with error messages for non-burt creatures (e.g. test_frog walks into door)
- IDEA: alternatives for how to to auto-move non-burt creatures: dir_lst, room_lst, room_dir_dict

- In some cases creatures will use methods to take actions and burt will *obeserve* their actions
	- this should be enabled by mode = 'exe_creature'
	- DECISION: part of making verb methods 'symetric', 'creature' should be checked for in each method


*** Long-term Pondering ***

- TBD: reveiw / update / finalize doc file

- TBD: possibly rename modules to indicate usage first? i.e. creature_class_def.py => class_def_creature.py ???

- Long Term Pondering:
	- the whole 'hand' concept is looking increasingly dodgy... too much inventory mgmt...
	- maybe time to bite the recursive bullet and just allow portable containers in portable containers?

- decide if interactive() class objects should eventually have noun identities (e.g. is_door() )

- TBD: static_gbl => tupple

- INPROC: Given that creatures will be contained:
	- INPROC: need to embrace a node-based awareness of creature location
	- DONE: need to embrace the use of recursion on methods like remove()
	- INPROC: Apply this to concepts like drop() and stand() / exit()
	- OLD DECISION: alternatively, just treat creature-containers as special exceptions
	- NEW DECISION: started using recursion when applying weight to obj & creatures
- TBD: Alternatively, maybe time to consider letting obj know what container they're in??

- INPROC: review TADS3 terms for Description and preposition

- IDEA: consider converting Writing to Decorations (examine() vs. read() )

- TBD: make backpack a true container???
- TBD: learn how to use VS Code word wrap and other features for Python
- IDEA: maybe I should call validate() again between pre_action() and cmd_exe() and then again between cmd_exe() and post_action() ?

- TBD: refactor gs. scope / mach_scope
		- Use list comprehension to eliminate for-loop? (link: https://medium.com/self-training-data-science-enthusiast/python-list-comprehensions-use-list-comprehension-to-replace-your-stupid-for-loop-and-if-else-9405acfa4404 )

- CANCEL: considers re-distributing not-in hand & read errors back into verb methods ???

- DONE: for doors and containers, use None option for no lock or no lid?
- CANCEL: Can I just set descript_key for Note in mk_def_pkl() with setter rather than whole dynamic_dict?
	- CANCEL: why do I need gs.dynamic_static_dict again?

python techniques:
- Do a refactoring code review (look into the 'any' command in place of for loops)
- TBD: Try argument unpacking ( https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/ )
- TBD: Try tupples for static_dict
	- NOTE: Franco on Tupples: A tuple is most suitable for immutable data with a well-defined order.  The static data that you pass to class constructors is often a good example.Another useful time for tuples is when you want dictionary keys with more than one field.  You cannot use something mutable there.
- TBD: learn about Super()
- TBD: read this article: https://sangeeta.io/posts/a-super-post-on-python-inheritance/

pipeline & testing:
- create 'win' test routine with checksum
- TBD: Jenkins integration to automatically update "v3 alpha" tab with latest commits


*** make database-driven! ***

*** New verbs ***

- IDEA: 'talk to creature' format:
	- IDEA: 'Ask X about Y'
	- IDEA: 'Tell X about Y'
	- IDEA: Say 'Z'


*** doc_strings ***

- TBD: doc_string about why errors and actions must be clearly delineated (e.g. and error cannot change gamestate)

- Clean up documentation and incorporate into doc_strings

- TBD: documentation:
	- TBD: updeate creature doc
		- discuss creature state
	- TBD: update timer doc with trigger changes from 3.64
	- TBD: update mach doc with wildcaard cahnges from 3.64
	- TBD: update class diagram
	- TBD: update module diagram
	- TBD: create machine diagram
		- hedgehog => state machine idea
	- TBD: create creature diagram
	- TBD: Timer Decisions
		- timers are set by machines rather than triggered by player commands
		- other than providing description text, timers are dumb - they just count -  a machine takes all actions

*** Out of Game Quality of Life Code ***

- Introduce non-functional requirement code (e.g. saves and pkl clean-up)
- Integrate with web template
- webify

file handling:
- game saves (requires file clean up?)
- move doc to modules?
- org modules in directories?

web features:
- TBD: Figure out a way in web browser to show all adventure text in scrolling window (???)

- create a hint sub-system
- TBD: no swearing in Dark Castle (with warning or else end of game)
	- cursing => end of game (requires warning_mach and usniversal scope)

- TBD: Debug mode:
	- TBD: Need a debug mode that eliminates 'try' from 2word and prep commands
	- TBD: need a secret code to prevent regular player from falling into debug: 'debug poke53281,0'
	- TBD: maybe debug opens a menu where you can choose start room & choose to disable method and / or description guards
- TBD: verbose / brief

- Unit Testing (link: https://youtu.be/6tNS--WetLI ) ???

* DEBUG TOOLS *
- work room for testing similar to tcrf.net Hollywood Hijinx

- "dungeon builder" web interface (?)

- runs on AWS with API GW, Lambda, and DynamoDB!

*** DB Driven ***

Version X.x Goals:
	- DB back end
	- "dungeon builder" web interface (?)
	- Run on AWS EC2

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


*** Expansion of Dark Castle ***

- Research existing IF languages (TADS & INFORM)
- Plan out expanded adventure
- Establish new base code needed for new adventure
- Write new code!

first: scan puzzle ideas and decide on next puzzles; plan for required features

- New rooms and puzzles!!
- New ideas - ideally should leverage existing coding with minimal addiional feature requirements
-implement new ideas
- publish new version and get feedback

*-- Awesome Words to Use --*
- stalwart (hedgehog)
- griffonage (illegible handwriting)
- recreancy (shameful cowardice; perfidy)
- aubade
- defenistrate
- consigliere
- consternation
- phyisogamy (from 3 Muskateers)
- Gallivanter
- Solipsistic
- Bamboozled
- Flabbergasted
- Discombobulated
- Cattywampus
- Lollygag
- Makarkey
- Kerfluffle
- Brouhaha
- Nincompoop
- Skedaddle
- Pumpernickel
- rolly-polly (hedgehog)
- Coddiwomple
- Sockdolager (forceful blow)
- sagaciate (get along)
- sockdolager

*-- possible new rooms --*
- upon_drawbridge
- entrance_hall (home base with well & safe shelf & hedgehog?)
- chapel (another possible home base?)
- courtyard
- library
- narrow / collapsed passage
- kitchen
- smithy
- maze
- wizards_tower
- dungeons

*-- RESEARCH --*
- read The Craft of Adventure
- Play at least 5 games
- Read the Digital Antiquiarian reviews

- PUZZLE: perhaps at some point Burt needs to bake biscuits??
	- would involve finding and mixing ingredients, right order, starting fire, baking right time / temp

- PUZZLE: Under Water Puzzle:
	- treasure at bottom of old well - but need a magical way to hold your breath?
	- old_well as water source in entrance_hall and also passage to... where?
	- can hold breath for 4 turns, locked grate is 2 moves down, get warning on half air and last turn
		- TBD: create LiquidContainer class
			- TBD: create new LiquidContainer class
			- TBD: instantiate old_well in the main_hall which contains fresh water
			- TBD: update drink() to allow / error for drinking from the old_well
	- lantern is water proof
	- should be like rope puzzle for Zork I... 
		- you have everything you need in the remote room but can't get out without solving puzzle

*-- DC1 PUZZLE IDEAS --*
Misc:
- Randomization feature like the spinning room in Zork 2 ? With way to turn it off
- Physics puzzles - see-saws, pulleys, and ceterfugal force
- Dragon is bored because it has read every book in the library - need to find a new book to interest it
- Ferret is named Bartleby
- landscape / path changes
- create vehical puzzle?

*-- DC2 PUZZLE IDEAS --*
- maybe, in DC2, before the ball, the princess is missing (hiding from evil prince) and is diguised as a black cat that burt needs to befriend?
- it would be cool to have an invisibility cloak / spell (probably need to keep it short term / contained)
- Note: gs.core.hero enables player to take on different characters in the game (e.g. Burt could become a mouse)
- princess 'poise' & 'moxie'
- fun idea - small creature - like a mouse - as an item
- more directions
- Princess takes 3 forms:
	1) Cat => Burt must get her collar
	2) Raven => ring
	3) Cockney goth waif (castle servant) => boots
	- Then princess arrives at ball wearing collar, ring, and boots
- Burt must also foil evil Prince plan to murder princess (perhaps swap fake dagger for real one?)
- Burt himself is taken for a lowly Baker (in past time)
- Basically, Burt and the Princess (in various forms) wander around the castle doing chores learning info
- Also, Burt has a chance to demonstrate himself as kind and helpful - or not - to disguised princess
- Meanwhile, the whole castle is in an uproar getting ready for big ball and princess arrival
- some scattered rumors that princess has "mysterious magical powers"
- Meeting Nana
	- Also, somewhere in the mix, Burt must prove who he is to a (much younger) Nana
	- he needs to get (Willy's) broach, and put it behind the throne
- Burt is given most of his hot/cold direction via a portrait of himself & princess
	- As Burt makes right decisions the portrait gets clearer; fades with wrong decisions
	- Portrait is taken of Burt and waif-princess by great artist who needs stand ins for Prince & Princess wedding portrait
	- Burt originally (in modeern times) finds the portrait on the pedistal next to the throne and *MUST* put it back there during time travel just before arriving back or else the closed time loop fails (gets multiple hints that there's "something he must do")
- Dungeon key
	- in modern times, the one room Burst still can't get into is the dungeon
	- main key was lost years ago during the "great ball fiasco" and spare has never been found
	- not viewed as very important since the dungeon side-wall parially collapsed and was flooded by moat
	- Dungeon is now the lair of the evil croc in the moat 
	- Burt needs to get the dungeon key in past times
	- he must somehow get it back to modern times so he can rescue princess in flooded dungeon from croc
		- why can't she just turn into a fast fish?? need to think through her magic limits
	- impossible to keep it so must hide it behind a brick (where he will retrieve it in the future)

- Princess Time-Travel Quest:
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

DCII Time Travel Ideas:
- In past, burt must convince young_nana to give him Willy's broach in order to drop it behind throne or else timeline is doomed!
- Perhaps burt first travels fwd in time a week and can pick up an unfinished portrait of burt & princess that gives future status (similar to Back to the Future)


Alter Terrain:
- Use Map room_pair updates to alter a room dramatically after a major change
	- e.g. Zork I resevoir post-dam opening
	- could use this after a cave in or rock collapse in the dungeons / mines?

Vehical:
- Bucket pulley / weight puzzle in wizard's tower
- need to adjust weight correctly going up and down
- need to grab staute (?) on way up / down?
- or else maybe mine cart / parachute??

Zork Thief = Ferret:
- dextrous, loves colorful objects, likes to fidtet / fiddle with things, clever
- will steal an object from burt (or that burt has touched) each time it randomly runs into him (some items off limits?)
- Some item on a high shelf or complexly locked (like the Zork egg) can only be opened by the ferret
- burt can indefinitely / eternally distract the ferret (*after* it has solved its puzzle) by giving it a rubks cube (described not named)
- the ferrets treasures can be found in a hole that burt needs to reach his arm into (scary warnings - could be a grue)
- maybe the shelf in the main hall is the one place safe from the ferret
- or else the object is in the courtyard and ferret gets it after burt sees it through window?? (seems like less agency?)
- hedgehog chases ferret away from Entrance Hall any time it randomely attempts to enter (entrance hall has well & shelf too)

hedghog:
- perhaps the hedgehog greets you every time you walk into the main_hall once you return the sword?

Special Glasses / Dream form:
- let burt see a room using descriptions from another dict

Carry Cappacity Constraints:
- item 'size' limits (invent point values) for Containers and Narrow Passages
- instead of big_rock could have sea_chest in main_hall tht burt can barely lug
	- maybe it's locked but has no key
	- can be the solution to the Wumpus_bat puzzle
	- Also, when the bat drops the chest, it smashes open... maybe revealing the rubiks cube (too soon??)
- Could have a narrow_passage - perhaps a collapsed passage that connects the north and south halves of the castle?
	- burt can only squeeze through with a few items (no sword)... perhaps the ruby for the smithy mouse is in the north side?

Writing / engraving:
- would be nice to have a way to write / engrave on something
- maybe make a weapon useful against a particular foe by engraving it??
- or put the dragon to work clearing a passage by making a sign that says 'cheese cake'

Vanishing cabinets:
- enable limited travel to another part of the dungeon?
- maybe only work one way (because broken?)
- or maybe can only bring very little gear?

Window:
- would be need to have a Window class that allows burt to see what he can't take
- could allow burt to peer into a courtyard with a tree and fountain
- maybe 2 guard dogs - one with red hat, one with blue hat - that are constantly paroling a passage
- if burt observest the window for a few turns he can see when to zip past the patrol
- (when the blue-hat dog looks up expectantly)
- perhaps window is in the collapsed_passage ??

Game Ending:
- Kinging Scroll glows faintly... and can only read when sitting on the Royal Lecturn... which also glows slightly
	- lecturn found in the Library (Willy's favorite room in the castle)
	- But only one thing can be _on_ the lecturn at a time... and there is currently a stuborn_snail there
	- snaill can only be encouraged to move by showing it the salt from the Kitchen
	- Depends on class Shelf (example obj = table, counter, lecturn - anything with a surface); needs a max_items attribute?

Glum Dragon
- how about a glum / bored / enui-ladden dragon that is blocking the libary entrance with its bulk
	- the dragon is too tough to be harmed by - or even to notice - being attacked
	- instead it just bemoans its misery - misquoting hamlet, and camus ("The underworld is other people")
	- If given cheesecake (baked in the royal bakery) it can be cheered up - and will go work on its to-do list and read a book and such
	- note: all other creatures like cheesecake too?

- map
	- maybe room beyond the Main Hall is the round room with many collapsed / ruined exits
	- can go east through mouse hole to bakery or smithy
	- or west to libary - which will then connect player back to cooridor that leads to anti-chamber


- Peter Pan puzzle where you catch and make use of your shadow / mirror image?

IDEA: Junk mail puzzle (multi-element solution); all for "chariot warranties"

IDEA: Thief puzzle (can take from backpack)

IDEA: chess puzzle - player first has to figure out that room is chess board ("statuary on a parquet floor" and then mate (probably smoother mate) to get through door. Replay button is broken (so only play once). other side has mate next turn so loose if you make wrong move. Possibly a small, wizzened gnome shows up to scold the player if they make an illegal move?

IDEA: create a jaunty_cap that makes Burt move twice as fast as everything else in the world - maybe essential for escaping the time travel ball?

IDEA: create a fun scenario where TravelEffect take item gets used... maybe a giant brid comes along and takes whatever's in Burts hand and scares him off until he carries a lead weight (or a heavy rock?) - which tires the bird out so much Burt can go in the room and get back his stuff and enter the room? Maybe this could be a room between main hall and antechamber that the maze / mouse hole is off of? Maybe nest is in corner of room of class Box (not open / close or lock / unlock).
- Make it a Wumpus Bat - a reference to Hunth the Wumpus and Adventure!!
- Takes an item from Burt's hand and sends him back the way he came to take cover; item is randomly placed in another (reachable) room
- Solution is to enter room carrying a heavy rock - Bat will take but leaves rock by its nest with a note "Tired out from lugging big rocks - leaving Dark Castle for a while to visit the Wumpus"
- Heavy Rock allows introduction of carrying capacity... playing can't carry *anything* else while carrying Heavy Rock
- some useful treasure found in the nest 
- Nest could be a container with open_state = None and lock_state = None

- Can sharpen and clean sword in mouse hole - maybe only way to get past goblin
- Until sharpened, sword can only parry goblin?
- need a non-shrunken ruby to pay for sword sharpening (turns up nose at cheese - says he never touches it because it gives him indigestion)
- mini Zork maze to get to blacksmith mouse
- maybe random mouse keeps appearing and if you give it cheese it runs off and can be followed to the blacksmith
- maybe mouse in maze is from Who Moved my Cheese
- references to grafitti in maze?? (e.g. "what would you do if you weren't afraid?")
	- IDEA: grafitti on Room wall = disp_writing()
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
	- or maybe you shrink for 3 turns or as long as you're in a confined space - whichever comes later??
		- (don't want to code every room for being mouse sized)
- maybe 2nd mouse, every once in a while, gets up from his nap at the table near the blacksmith and sneaks off to the bakery
	- bakery very hard to find... go to a corner of the maze and then go 'up'!!
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


##### RANDOM NOTES #####


##########################
### VERSION 3.7x START ###
##########################

Version 3.7x Goals



##########################
### VERSION 3.7y START ###
##########################

Version 3.7y Goals


##########################
### VERSION 3.7z START ###
##########################

Version 3.7z Goals


##########################
### VERSION 3.8q START ###
##########################

Version 3.8q Goals


##########################
### VERSION 3.8u START ###
##########################

Version 3.8u Goals


##########################
### VERSION 3.8r START ###
##########################

Version 3.8r Goals


##########################
### VERSION 4.x START ###
##########################

Version 4.x Goals


##########################
### VERSION 5.x START ###
##########################

Version 5.x Goals


##########################
### VERSION 6.x START ###
##########################

Version 6.x Goals


##########################
### VERSION X.x START ###
##########################


##########################
### VERSION Y.y START ###
##########################

vY.y IDEAS






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
