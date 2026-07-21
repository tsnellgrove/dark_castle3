To Do List - Dark Castle v3


# *** GIT BRANCH TEMPLATE *** #

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


# *** BIG PICTURE ***
- DONE: machincs / classes / error subsystem
- DONE: story updates
- DONE: test harness
- TBD: interpreter updates
- TBD: db back end (sqlalchemy)
- TBD: web site
- TBD: ECS (UI & App tasks w/ DynamoDB back end)
- TBD: CI/CD
- TBD: remaining foundation features: light, food, drink, sleep, etc
- TBD: get test player feedback
- TBD: expand adventure!

*** major updates in separate git merges ***
- DONE: mvps
- DONE: implement full set of cardinal directions + u & d
- DONE: automated / unit & acceptance testing
	- DONE: introduce rand_mode
	- DONE: introduce verbose and brief commands
- TBD: major interpreter update!
	- TBD: address 'Do What I Mean' in interp() now?
- TBD: new AWS account
- TBD: webify
- TBD: live updates with git- TBD: food
- TBD: drink
- TBD: sleep
- TBD: day / night
- TBD: turn lantern into actual light (?)
	- IDEA: once an item, perhaps Landtern should be found on shelf (it's from Willy after all)
	- IDEA: lean in on TADS approach
- TBD: expand castle
- TBD: db back end
- TBD: liquids
- TBD: transparency
- TBD: fire / heat


*** major updates in separate git merges ***


############################
### START CLEESH VERSION 3.9.3 / DARK CASTLE VERSION 3.4.2 ###
############################

- INPROC: interpreter update
	- INPROC: pre-branch work
		- INPROC: gather and organize interp notes


*** Structured Interpreter Notes ***

- INPROC: initial branch goals:
	- DONE: create a version just for interp() updates and gather all interp updates there!!
	- DONE: full review of to-do list
	- DONE: org to-do list
	- DONE: read research
	- DONE: re-org research
	- TBD: get started!
	- IDEA: global verb synonyms
	- IDEA: noun synonyms (different than abreviations)
	- TBD: prepositions
		- IDEA: simple prep verbs ('sit_in')
	- TBD: plurals
	- TBD: pronouns
	- TBD: do what the player means
	- TBD: sentence structure
	- TBD: curse words
	- TBD: tactical fixes
	- TBD: new commands
	- TBD: deep dive review of Believed to be Done items


- DONE: branch research:
	- DONE: read => https://medium.com/swlh/zork-the-great-inner-workings-b68012952bdc
	- DECISION: my goal will be Zork 285 (each word = 1 part of speech) with PREP option
		- IMPLICATION: unlike ZIL, I will not recognize multiple parts of speech per word
	- DONE: read z-machine history
	- DONE: read ZIL article: https://intfiction.org/t/recreating-zork-285-in-zil/53841/2
	- DONE: read i-fiction ZIL write-up
	- DONE: work on zork 285 word list
		- DONE: review buzz and directions
		- DONE: review verbs
		- DONE: establish my synonyms for congruent verbs
		- DONE: document dark_castle words
		- DONE: compare lists and consider changes
		- DONE: plan universal verb synonym updates
	- DONE: read inner workers review of ZIL interpreter
	- DONE: re-read my initial ideas so I can mentally map them to zil approach
	- DONE: plan future usage
		- DONE: obj attributes
			- DONE: doc zil attributes
			- DONE: doc dc implementation of zil attribs
			- DONE: doc zil attribs to be part of interp branch scope
		- DONE: obj properties
			- DONE: read obj properties
			- DONE: document zil obj properties
			- DONE: doc dc implementation of zil properties
			- DONE: doc zil property abilities to implement in dc this branch
		- DONE: plan new words and word updates: congruent, update, new from zork 285 / zork-1 r88
			- DONE: review zil new words and choose branch scope
			- DONE: my own list (below)
			- DONE: doc word updates (new or change) for this branch in to-do
	- DONE: document good information sources found so far
		- zork history: https://medium.com/@r.ajdnik/zork-the-great-underground-empire-cda94623861c
		- (*) zork: inner workings: https://medium.com/swlh/zork-the-great-inner-workings-b68012952bdc
		- cmd list: https://zork.fandom.com/wiki/Command_List#:~:text=Command%20List%20%7C%20Zork%20Wiki%20%7C%20Fandom,(item)%20at%20(location)
		- game control cmds: http://tigerteched.pbworks.com/w/page/30980745/Zork#
		- (*) zork 285: https://intfiction.org/t/recreating-zork-285-in-zil/53841
		- studies in zil pt1: https://the-rosebush.com/2024/08/studies-of-zil-part-1/#sdfootnote4sym
		- (*) studies in zil pt2: https://the-rosebush.com/2025/07/studies-of-zil-part-2-how-does-zil-work-anyway/#170f5270-9bcd-4e56-be5a-869c2029cfc5-link
		- (*) internal secrets (web): https://ifsecrets.blogspot.com/2019/02/introduction.html
		- (*) internal secrets (pdf): https://eblong.com/infocom/other/Internal_Secrets_Ko_2019.pdf#
		- (*) zork inform 7 port: https://i7-dungeon.sourceforge.net/source_0.html
		- (*) google gemini search: "complete zork zil syntax table"
		- (*) google gemini search: "how did prepositions work in infocom games?"
		- google gemini search: "what was Zork 1-R88"
		- (*) github - historicalsouce: https://github.com/historicalsource/zork1/blob/master/gsyntax.zil
		- (*) github - jeffnyman: https://github.com/jeffnyman/zork1/blob/main/syntax.zil
		- (*) github - heasm66 1: https://github.com/jeffnyman/zork1/blob/main/syntax.zil
		- github - heasm66 2: https://github.com/heasm66/mdlzork/blob/master/zork_285/doc/zork285_06.md
		- github - heasm66 3: https://github.com/heasm66/mdlzork/blob/master/zork_285/defs.zil
		- github - heasm66 4: https://github.com/heasm66/mdlzork/tree/master/zork_285/doc
	- DONE: post-research - reorg branch doc 


- DONE: big picture goals / scope
	- DONE: research zil code in order to understand how more advanced parsers work
	- DONE: articulate big picture goals
		- IDEA: enable greater flexibility of words and sentence structure
		- IDEA: align zil approach with cleesh's object class-based system
		- IDEA: aim for easy game coding - most of the work should be done by cleesh!
			- IDEA: "good tools make easy things easy and hard things possible"
	- DONE: articulate specific branch features
		- IDEA: differentiate between verbs and actions
		- IDEA: embrace the zil notion of syntax to enable natural sentence structure
		- IDEA: enable multiple adjectives per noun
		- IDEA: enable synonyms for nouns and verbs
		- IDEA: enable class-specific verbs (e.g. 'doff')
		- IDEA: enable noun-specific cmd_str_lst replacement: "enter castle" => "go n"
		- IDEA: enable errors and mach run perform at do-noun and id-noun level (??)
		- IDEA: consistent way to deal with pronuns
		- IDEA: consistent way to deal with plurals (use 'qty of' for water, tea, & glass)
		- IDEA: enhanced get-what-i-mean
		- IDEA: deal with curse words
		- IDEA some tactical fixes
		- IDEA: a few new cmds
	- DONE: document zil capabilities that are out of scope to this cleesh branch
		- EX: most multiples (inclulding use of "and")
		- EX: orphanned ambiguous command completion
		- EX: "then" and "." as command queue indicators
		- EX: ask <actor> for / about <topic>, tell / say to <actor> <cmd>, '<actor>, <cmd>' ?
		- EX: titles (with periods after them) [e.g. mr. , dr. , etc.]
		- EX: numbers (e.g. GET ONE FRUIT)
		- EX: extended ALL and EXCEPT / BUT
		- EX: adverbs (CAREFULLY, QUIETLY, SLOWLY, QUICKLY, and BRIEFLY)
		- EX: OOPS, UNDO, advanced AGAIN
		- EX: words as multiple parts of speech (.e.g 'back' as prep and adj)?
		- EX: execute code from do-noun & io-noun response loop?
		- EX: 'part-of' concept
	- DONE: basic zork approach:
		- 1. READ → raw text input
		- 2. LEX → split into dictionary words
		- 3. PARSE → match grammar pattern
		- 4. Action routine executes
		- 5. EPARSE if grammar match fails
		- IDEA: pursue formal LEX (str => lst)=> PARSE (syn, OIA, & syntax) => execution (do it) plan
	- DONE: propose updated parser process:
		- 0. copy user_input_str => cmd_str
			- 0a. cmd_str => clear white space and convert to lower
			- 0b. cmd_str => cmd_str_lst
		- 1. elim buzz words
		- 2. convert verb synonyms
		- 3. address non-verb-noun cmds (non-interp, tru1word, convert_1word, help, go [?])
		- 4. identify  verb, do-noun clause, prep, and id-noun clauses
			- 4a. error if no verb or verb not known or verb count > 1
			- 4b. create scope_lst and noun_syn_lst
				- 3b1. convert cmd_str_lst to root nouns using noun_syn_lst
			- 4c. in scope_lst, for do-noun clause
				- 3c1. find noun in scope_lst
				- 3c2. validate adj (error if not found?) and removed
				- 3c3. identify do-noun
				- 3c4. if no noun or > 1 noun => err
			- 4d. in scope_lst, if id-noun clause exists
				- 3d1. find noun in scope_lst
				- 3d2. validate adj (error if not found?) and remove
				- 3d3. identify id-noun
				- 3d4. if no noun or > 1 noun => err
			- 4e. identify each non-buzz prep
			- 4f. if verb is on class_spec_vrb_lst, check if do-noun supports it
				- 3f1. if yes, proceed; else, std err
		- 5. use syntax with verb, do-noun, id-noun, and prep to identify action
			- 5a. apply Get What I Mean (GWIM) if the id-noun is missing
			- 5b. error if GWIM retruns 0 or > 1
		- 6. response loop:
			- 6a. check id-noun for do-noun / action specific errors
			- 6b. check do-noun for id-noun / action specific errors
			- 6c. execute action (passing in do-noun & id-noun)
		- 7. introduce new words
		- 8. add new in-scope zil capabilities


*** GET STARTED: STRUCTURED TO-DOS ***

- DONE: create new interp_feature git branch
	- DONE: 'git branch' to confirm *master
	- DONE: 'git branch <FEATURE_NAME>' to create new branch
	- DONE: 'git branch' to confirm new branch exists but that master is still checked out
	- DONE: 'git checkout <FEATURE_NAME>' to switch focus to branching_test branch
	- DONE: 'git branch' to confirm new branch is now in focus
	- DONE: Publish Branch via VS Code button
	- DONE: confirm new branch on GitHub
	- DONE: update doc TBDs to DONEs
	- DONE: <CMD><OPT>S (to save all files)
	- DONE: 'git add .' to add files to be committed
	- DONE: 'git commit -m "doc updates"
	- DONE: 'git push" to push updates to origin (GitHub)
	- DONE: confirm new branch on GitHub is now ahead of master

- 0) copy user_input_str => cmd_str [CANCEL] => refactor existing
	- 0a. cmd_str => clear white space and convert to lower
	- 0b. cmd_str => cmd_str_lst

- 1) elim buzz words [CANCLE] => refactor existing

- 2) convert verb synonyms [DONE]
	- DONE: add univeral verb synonyms
	- DONE: create test scenario for standard verb synonyms
	- DONE: work with q to fix scenario rename feature (option 7)
	- DONE: rename newest dc scenario to '00E_entrance_verb_syn_test'
	- DONE: review / org remaining verb syn to-dos
	- DONE: move remaining verb syn ideas to appropriate section of plan
		- IDEA: converting verbs to actions:
			- IDEA: many verbs have universal synonyms that can be immediatel converted in LEX:
				- EXAMPLE: 'don' => wear()
			- IDEA: there are also class-specific verbs that must check the noun in PARSE:
				- EXAMPLE: 'remove', 'doff' => take()
			- IDEA: then there is idiomatic prepositional usage captured in SYNTAX:
				- EXAMPLE: 'put on' => wear()
			- IDEA: there are obj-specific verbs that are checked during DO/IO/A execution:
				- EXAMPLE: 'enter castle' => execution swap 'go north' (executed via verb 'go')
	- DONE: remove 'kick' from verb_syn_lst (due to 'kick with fist')
	- DONE: fix scenario test / remove 'kick' from it

- 4. identify  verb, do-noun clause, prep, and id-noun clauses - refactor [INPROC]
	- 4 aa. deal with special case of zero or one-word commands: [DONE]
		- 4.aa.1 if len(user_input_lst) == 0 ==> return err [DONE]
		- 4.aa.2 if len(user_input_lst) == 1: [INPROC]
			- if help or tru_1word => return word1 & type [DONE]
			- if word1 in one_word_only_lst and len(user_input_lst) > 1 ==> return err [DONE]
			- create syntax routine and call from interp() [DONE]
				- create function [DONE]
					- IDEA: generate input_syntax_lst and compare to syntax_lst to determ input_action
					- EXAMPLE: input_verb = 'look' => input_syntax_lst = [look, at, do_noun]
					- EXAMPLE: [look, at, do_noun] => {[look, at, do_noun] : [examine, input_do]}
				- if word1 in convert_lst => convert to multi-word [DONE]
					- create new validate routine for case == 'action_2word' [DONE]
					- create new cmd_exe() routine for case == 'action_2word' [DONE]
					- create new mach_class routine in trig_check case == 'action_2word' [DONE]
					- test updated case [DONE]
					- clean-up comments [DONE]
					- rest of convert_lst [DONE]
					- clean up comments in interp() [DONE]
				- if word1 in travel_lst => syntax routine [DONE]
					- add hero_dir to syntax_dict [DONE]
					- add hero_dir post_processing to syntax() [DONE]
					- add 'action_dir' case and * case check * to validate() [DONE]
					- add 'action_dir' case to cmd_exe() [DONE]
					- add 'action_dir' case to trig_check() in mach_class() [DONE]
					- add travel_lst call [DONE]
					- initial testing => err [DONE]
					- fix getting misc_err_0 instead of dir_err_0 [DONE]
					- test new case [DONE]
					- clean up comments in case calls [DONE]
					- clean up comments in interp() [DONE]
				- ensure reserved words (hero_rm_obj, hero_obj, hero_dir) aren't in input [DONE]
				- if word1 in assumed_noun_lst => how to handle assumed do_noun?? [DONE]
				- refactor interp() code for readability [DONE]
	- 4__ error cases [DONE]
		- 4.aa.3 if word1 in full_verb_lst and len(user_input_lst) == 1 ==> return err
		- 4.aa.4 if word1 not in full_verb_lst and len(user_input_lst) == 1 ==> return err
	- 4a. error if no verb or verb not known or verb count > 1 [DONE]
		- 4a.1 update errors [DONE]
		- 4a.2 run sceario tests [DONE]
		- 4a.3 fix scenario tests [DONE]
	- DONE: 2word 'go' case => syntax / action_dir case
	- DONE: refactor syntax
		- DONE: pass do_noun_str to syntax()
		- DONE: test
		- DONE: migrate assumed to syntax
		- DONE: auto test & fix
		- DONE: manual test & fix
		- DONE: clean-up comments
		- DONE: refactor assumed section (consolideate exit?, leave error till later?)
	- DONE: sort out 'climb':
		- IDEA: prep_no_do verb case => syntax action_dir
		- DONE: review climb case in detail (including app_main() )
		- DONE: move non-up-down err to climb_err()
			- DONE: test
			- DONE: fix
		- DONE: syntax call
		- DONE: update case => action_dir
		- DONE: move 'go <dir>' to a call from climb() [may require app_main calls rework]
			- DONE: update naming: prep => direction, word1 == 'climb' => world1 != 'go'
			- DONE: move app_main() 'climb' routine
				- DONE: move app_main() 'climb' routine to just after cmd_exe() call
				- DONE: may need to convert skip_inc => decr_inc()
				- DONE: create gs.core.decr_inc()
				- DONE: clean up comments			
			- DONE: migrate app_main() 'climb' routine to climb()
				- DONE: create cmd_queue gs.io attrib
				- DONE: in app_main(), replace all cmd_queue calls w/ gs.io.cmd_queue
				- DONE: elim gs.io.prepen_cmd_queue() and clean up comments
				- DONE: migrate cmd_queue add and decr_inc set to climb()
				- DONE: clean-up comments
		- DONE: move assumed_dir case to central assumed handling
			- IDEA: similar to 1-word assumed verbs
			- IDEA: migrate ungiven direction choice to syntax - or that does that just distrib code?
			- IDEA: ask Q what she thinks
			- DONE: in interp() change ('climb', 'do_noun') syntax call to match user_input_lst
			- DONE: review
			- DONE: clean-up
			- DONE: decide if "climb down" should be supported => not now
		- DONE: elim legacy cases
			- DONE: comment out prep_no_do case in validate(), cmd_exe(), and trig_chk()
			- DONE: understand case == 'action_dir' in trig_check()
			- DONE: comment out go case in validate(), cmd_exe(), and trig_chk()
			- DONE: test
			- DONE: clean up comments in validate(), cmd_exe(), and trig_chk()
		- DONE: planning
			- DONE: document 'go' and 'climb' interp() flow
			- DONE: big picture flow changes
			- IDEA: big picture target flow
				- pre-process (str => lst, clean-up, universal synonym substitution) [DONE]
				- elim universal errors (too long, no verb, no verb, > 1 verb) [DONE]
				- meta_cmds special cases ('help' & 'tru_1word')
				- 1-word special cases (convert, dir, and infer)
				- action_dir universal case
					- identify verb, do_noun, id_noun, & preps => syntax
					- syntax: txt_lst => action_lst (elim too long cases here)
					- process action_lst => validate / cmd_exe pipeline
	- DONE: big picture updates
		- DONE: move too-long error to top (exception for help)
		- DONE: 'tru_1word' + 'help => 'meta_cmds'
			- DONE: add error for user_input_lst[0] == 'help' and len(user_input_lst) > 2
			- DONE: combine 'help' and 'tru_1word' cases under 'meta_cmds' case in interp()
			- DONE: combine syntax call for meta_cmds (elim len constraints)
				- DONE: updat syntax call
				- DONE: troubleshoot
				- DONE: clean-up comments
		- DONE: tactical tuning
			- DONE: separate 'help' from meta_cmd_lst
			- DONE: clean up convert & travel; use elif; unify return call (if case is not None)
			- DONE: syntx [input_dir, verb, do_noun] > [input_verb, do_noun, prep_dir_opt, id_noun]
			- DONE: clean-up comments
			- DONE: add 'dir' cmd to 'too long' err ?
		- DONE: combine 1-word convert, dir, infer, & 1-word err into 1 syntax call block
	- DONE: synergize 'go' and 'climb' commands
		- DONE: tighten up initial error cases
		- DONE: simplify 'climb' syntax call - pt1
	- DONE: fix 'action_dir' case in trig_chk() => [verb, dir, do_noun]
	- DONE: review 2word_verb case and syntax call
		- DONE: convert 2word case to 2word_action
		- DONE: elim 2word case
		- DONE: elim '2word' in interp(), validate(), cmd_exe(), & trig_chk()
		- DONE: test
		- DONE: clean-up comments
	- DONE: verb vs. action
		- DONE: introduce a new non_action_verb_lst ("sit")
		- DONE: implement "sit in chair", "sit on chair"
		- DONE: more sit testing
		- DONE: address "Can't use 'Enter'" error
		- DONE: "Sit what" err => "Sit where"
		- DONE: review / refactor noun_handling()
			- DONE: review noun_handling() for 2word case
			- DONE: review noun_handling() for prep case
			- DONE: update existing test scenarios as needed if no longer pass
			- DONE: refactor noun_handling()
			- DONE: clean up comments
			- DONE: review cleaned-up noun_handling()
			- DONE: re-refactor noun_handling()
			- DONE: embed root_word_count() in noun_handling() [no need for function]
			- DONE: refactor root_word_count section
			- DONE: clean-up
			- DONE: in interp() islice => slice
			- DONE: clean up comments (including import)
		- DONE: implement "sit" and "climb" w/ do_noun infer
			- IDEA: if != 1: "What do you want to sit on / climb?"
			- IDEA: if 1: "(the <do_noun>)"
			- DONE: infer sit
			- TBD: infer climb
				- IDEA: use similar function to infer_seat() to infer_climable()
				- IDEA: then within interp, can infer direction
				- IDEA: from within interp, can also call infer_climbable() for "climb_<dir> case
				- DONE: write climbable_infer() function
				- DONE: call climbable_infer() from syntax()
				- DONE: need to fix error from return without update of user_input_lst; obj => txt
				- DONE: create test_stepladder
				- DONE: add test_stepladder to Entrance and validte "climb" response
				- DONE: fix scenario failure
				- DONE: review interp() and elim comments
				- DONE: investigate better way to deal w/ noun infer of non-2word
				- DONE: call infer_climbable() from interp() to deal w/ "climb up" / "climb down"
				- DONE: check scenarios
			- DONE: refactor sit() 
				- DONE: update to match climb()
				- DONE: elim ladder and test_chair; run scenario test
				- DONE: return to test state
				- DONE: develop rigorous 'sit' test:
				- DONE: infer tests, 1 seat:
					'sit' => infer_seat() | now: {WORKS!!!}
					'sit in' => infer_seat() | now: {WORKS!!!}
					'sit on' => infer_seat() | now: {WORKS!!!}
					'sit into' => infer_seat() | now: {WORKS!!!}
					'sit down' => infer_seat() | now: {WORKS!!!}
					'sit down in' => infer_seat() | now: {WORKS!!!}
					'sit down on' => infer_seat() | now: {WORKS!!!}
					'sit down into' | now: {WORKS!!!}
				- DONE: seat_obj given:
					'sit <x>' | now: {WORKS!!!}
					'sit in <x>' | now: {WORKS!!!}
					'sit on <x>' | now: {WORKS!!!}
					'sit into <x>' | now: {WORKS!!!}
					'sit down <x>' | now: {WORKS!!!}
					'sit down in <x>' | now: {WORKS!!!}
					'sit down on <x>' | now: {WORKS!!!}
					'sit down into <x>' | now: {What??"}
				- DONE: infer tests, 0 seats:
					'sit' => infer_seat() | now: "Where do you want to sit?"
					'sit in' => infer_seat() | now: "Where do you want to sit?"
					'sit on' => infer_seat() | now: "Where do you want to sit?"
					'sit into' => infer_seat() | now: "Where do you want to sit?"
					'sit down' => infer_seat() | now: "Where do you want to sit?"
					'sit down in' => infer_seat() | now: "Where do you want to sit?"
					'sit down on' => infer_seat() | now: "Where do you want to sit?"
					'sit down into <x>' | now: "Where do you want to sit?"
				- DONE: infer tests, 2 seats:
					'sit' => infer_seat() | now: "Where do you want to sit?"
					'sit in' => infer_seat() | now: "Where do you want to sit?"
					'sit on' => infer_seat() | now: "Where do you want to sit?"
					'sit into' => infer_seat() | now: "Where do you want to sit?"
					'sit down' => infer_seat() | now: "Where do you want to sit?"
					'sit down in' => infer_seat() | now: "Where do you want to sit?"
					'sit down on' => infer_seat() | now: "Where do you want to sit?"
					'sit down into' | now: "Where do you want to sit?"
				- DONE: run rigorous test for all cases
				- DONE: clean up comments
				- CANCEL: update infer_seat() and call to handle count = 0 diff from = 2 ??
				- DONE: update to pass scenario test
			- DONE: solve 'sit down in/on chair' => syntax
				- DONE: create specific 'sit' entries for syntax()
				- DONE: create prep list
				- DONE: call new prep_lst from multi-word 'sit' case in interp()
				- DONE: add dir_cmd_lst
				- DONE: handle verb cases
				- DONE: create do_noun_clause w/ no preps and send to noun_handling
				- DONE: create id_noun_clause w/ no preps and send to noun_handling
				- DONE: create infer call for no do_noun
				- DONE: standardize 1-word case of 'sit'
				- DONE: call syntax
				- DONE: update syntax map to address all test cases
				- DONE: test
				- DONE: elim 'sit' fix from 1-word
				- DONE: test and update test results
				- DONE: refactor sit() case
				- DONE: abstract infer_do_noun() into separate function
				- DONE: clean up comments
				- DONE: update syntax case to new 'universal' format; set for uni if no case
				- DONE: clean up comments
				- DONE: make sit the native seat() method w/ 'enter' as universal synonym
					- DONE: create sit_err() method in err()
					- DONE: create sit() method in seat()
					- DONE: update syntax in interp()
					- DONE: make 'enter' a universal synonym for 'sit'
					- DONE: make 'exit' a universal synonym for 'stand'
					- DONE: manual test
					- DONE: scenario test
					- DONE: fix scenario test if needed
				- DONE: create new sit scenario test
			- DONE: generalize one_word_convert_lst => sit case
				- DONE: first pass update (messy!)
				- DONE: 'jump' and 'stand' => one-word cmds with 'no noun' err if do_noun_count > 0
				- DONE: 'jump' and 'stand' => infer_do_noun => hero
				- DONE: syntax support for 'jump up', 'jump down', 'stand up'
				- DONE: add 'examine' to intake list
				- DONE: 'look' => 2-word cmd; 'look <X>' => 'examine <X>; infer_do_noun => room
				- DONE: syntax support for 'look at', 'look in'
				- DONE: 'inventory' => 2-word cmd; 'i <X>' => 'examine <X>; infer_do_noun => hero
				- DONE: clean up comments!
				- DONE: create new static lists for action_verb_lst and non_action_verb_lst
				- CANCEL: migrate global syn directly to syntax for clarity / flexibility
					- IDEA: no, would need to repeat all associated prep entries
				- DONE: test for scenario errors
		- DONE: handle synonyms
			- DONE: embed symetric syns in syntax (lik zork does)
				- DONE: define action, non_action, verb_syn in interp()
				- DONE: verb_lst = action + non_action + verb_syn
				- DONE: ('leap', 'verb_syn') : 'jump'
				- DONE: add 'verb_syn' to forbiden word lst
				- DONE: check for syn; if exist, replace verb_lst
				- DONE: add print() line to show before / after verb_syn replacement
				- DONE: comment out 'leap' in global
				- DONE: test
				- DONE: symetric syns for remain active verbs (not including 'enter' / 'exit')
				- DONE: symetric synonym syntax call check => case != 'error' (not err msg)
				- DONE: sort out 'inventory'
					- DONE: 'inventory' => one_word cmd
					- DONE: 'list' = sym syn of 'inventory'
			- DONE: create cond_syn() routine to inspect action_lst after syntax call
				- CANCEL: inventory case (too complicated - see above)
					- CANCEL: if not do_noun.is_receptacle(): error = "nothing to look within"
					- CANCEL: elif not do_noun.is_closed(): error = "{do_noun.f_n} is closed"
					- CANCEL: else: action_lst[0] = 'examine'
					- CANCEL: interp() syntax 'look at', 'inventory' => inventory
					- CANCEL: universal syn 'ist' => inventory
				- IDEA: some syns should only be true under certain circumstances
					- EXAMPLE: 'enter' == 'sit' if do_noun is_seat
					- EXAMPLE: 'take' = 'doff' if do_noun is_garment
				- IDEA: cond_syn() takes action_lst evaluates, and replaces verb if appropriate
					- IDEA: need to re-do class verbs to be most specific (e.g. 'doff' and 'sit')
					- IDEA: then equate general verbs with specific in cond_syn()
					- IDEA: benefit is that err never runs for general verb if swapped to specfic
				- DONE: asymetric synonyms - 'enter'
					- DONE: update enter_err() in error()
					- DONE: create asym_syn(action_lst, gs) function in interp()
					- DONE: returns case, action_lst
					- IDEA: options are 1) no change, 2) 'error', ["err_txt"], 3) new_case, new_al
					- DONE: disable global syn for enter => sit
					- DONE: add 'enter' to action_verb lst
					- DONE: test
				- DONE: asymetric syn - 'exit'
					- DONE: update exit_err() in error()
					- DONE: disable global syn for exit => stand
					- DONE: add 'exit' to action_verb list
					- DONE: if exist, add symetric syns to syntax (gen purpose)
					- DONE: add infer do_noun entry for 'exit'
					- DONE: add syntax entry for 'exit' (see legacy code)
					- DONE: in asym_syn(), if 'exit' and do_noun_obj.is_seat() => stand
					- DONE: manual test
					- DONE: scenario test
		- INPROC: extend new interp() structure
			- DONE: generalize 2word cases => sit case
				- DONE: need routine for hand mgmt
					- IDEA: should be independent fom interp() due to do_noun_exe() and id_noun_exe()
					- IDEA: should be post x_err() and pre_action() because changes game world
					- DONE: create hand_mgmt(case, word_lst, gs) function in hand_mgmt module
					- DONE: add same cmds in interp() (with only 'wear' enabled)
					- DONE: in app_main(), import hand_mgmt() from hand_mgmt
					- DONE: call from app_main() just before cmd_exe()
				- DONE: wear
					- DONE: update hand_mgmt() for 'wear'
					- DONE: disable global syn for don => wear
					- DONE: add wear to interp() action_verb list
					- DONE: add base ('wear', 'do_noun') entry to syntax
					- DONE: add symetric syn 'don' to syntax (also add 'don' to interp() syn_verb_lst)
					- DONE: add infer do_noun entry for 'wear' (if in_hand)
					- DONE: in asym_syn(), add conditional syn if exist (gen purpose)
					- DONE: manual test (including hand_mgmt() of garment in bkpk)
					- DONE: scenario test
					- DONE: clean up comments in static_gbl
				DONE: reformat action_lst
					- IDEA: action_lst = [verb_str, do_noun_obj, prep_str, id_noun_obj, type]
					- IDEA: prep_str can be dir, do_prep, or id_prep
					- IDEA: type = 'verb_do', 'verb_do_prep', 'verb_do_id', 'verb_do_prep_id', 'error'
					- IDEA: check for prep errors in x_err() by passing prep_str to method
						- EXAMPLE: 'put sword in table' => 'can't put anything inside the table'
						- EXAMPLE: 'stand on basket' => 'The basket has no surface to stand on'
					- IDEA: some methods will need to be updated to pass prep_str
					- DONE: update existing action_lst w/ type
					- DONE: review aync_syn() routine => fix 'exit'
					- DONE: auto test
					- DONE: manual test
					- DONE: clean up comments in validate(), cmd_exe(), and trig_chk()
				- DONE: in interp(), linke tst_mode to debug mode
				- DONE: doff
					- DONE: create doff()
						- DONE: create doff() method
						- DONE: create doff_err() method
						- DONE: remove garment refs from take()
					- DONE: Introduce doff as cmd (see 'wear' template above)
						- DONE: update hand_mgmt() as needed for new_verb
						- DONE: disable global syn for new_verb
						- DONE: add new_verb to interp() action_verb list
						- DONE: add base ('new_verb', 'do_noun') entries to syntax
						- DONE: add new_verb symetric syns to syntax and syn_verb_lst
						- DONE: add infer do_noun entry for new_verb as needed
						- DONE: in asym_syn(), add conditional syn as needed
						- DONE: manual test (including symetric syn, infer, asym syn, and hand_mgmt)
						- DONE: scenario test
						- DONE: clean up item.doff(), error.doff_err(), static_gbl
				- DONE: 'take'
					- DONE: update hand_mgmt() as needed for new_verb
					- DONE: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
						- DONE: 'remove' and others as symetric syn for 'take'
					- DONE: add infer do_noun entry for new_verb as needed
					- DONE: in asym_syn(), add conditional syn as needed
						- DONE: if verb_str = 'take' and do_noun in worn_lst: asym syn of 'doff' 
					- DONE: manual test (including symetric syn, infer, asym syn, and hand_mgmt)
					- DONE: scenario test (doff)
					- DONE: fix scenario ('Taken') 
					- DONE: clean up comments in static_gbl, item.take()
				- DONE: 'drop'
					- DONE: update hand_mgmt() as needed for new_verb
					- DONE: disable global syn for new_verb ('release')
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- DONE: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including symetric syn, infer, asym syn, and hand_mgmt)
					- DONE: had to move hand_mgmt() to before validate() in app_main()
					- DONE: scenario test
					- NA: fix scenario as needed
					- DONE: clean up comments in static_gbl, hang_mgmt(), app_main()
				- DONE: long-term fix for hand_mgmt() kludge
					- IDEA: hand_mgmt() innate problem: world state changes but cmd_exe() might not run
						- EXAMPLE: 'eat biscuit' moves biscuit from bkpk to hand even if eat_err()
					- IDEA: this was true when hand-state was baked into interp() as well
					- IDEA: problem exists even if we didn't run actions from do & id nouns
					- IDEA: 1 solution is sit down and bake hand mgmt features into verb() & verb_err()
						- IDEA: actually - there will be a lot of these - maybe create auto routines?
					- CANCEL: rigorous ealiminat-hand_mgmt() approach would require:
						- CANCEL: update wear() & wear_err() for garment in bkpk
						- CANCEL: update drop() & drop_err() for item in bkpk or garment worn
						- CANCEL: update eat() & eat_err() for food in bkpk or food worn
						- CANCEL: update stow() & stow_err() for garment worn
						- CANCEL: will also need to do for all prep_verbs... hm...
					- IDEA: alt, just update verb_err() and move hand_mgmt() back to cmd_exe()
						- DONE: decide approach: update verb_err() & move hand_mgmt() back to cmd_exe()
						- DONE: adjust wear_err() for bkpk (was already in place!)
						- DONE: adjust drop_err() for bkpk or worn
						- DONE: move hand_mgmt() back to just before cmd_exe()
						- DONE: manual test
						- DONE: scenario test
						- DONE: clean-up comments in drop_err(), hand_mgmt(), app_main()
				- DONE: 'eat'
					- DONE: update hand_mgmt() as needed for new_verb
					- DONE: update *_err() to pass validate if hand_mgmt() will fix when called
					- DONE: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- DONE: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including symetric syn, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- DONE: fix scenario as needed
					- DONE: clean up comments in static_gbl, eat_err() ['wear', 'drop', 'eat']
				- DONE: 'stow'
					- DONE: update hand_mgmt() as needed for new_verb
					- DONE: update *_err() to pass validate if hand_mgmt() will fix when called
					- NA: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- DONE: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including symetric syn, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- DONE: fix scenario as needed
					- DONE: clean up comments in static_gbl
				- DONE: 'read'
					- NA: update hand_mgmt() as needed for new_verb
					- NA: update *_err() to pass validate if hand_mgmt() will fix when called
					- DONE: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- NA: add infer do_noun entry for new_verb as needed
					- DONE: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including symetric syn, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- NA: fix scenario as needed
					- DONE: clean up comments in static_gbl, writing.examine()
				- DONE: 'open'
					- DONE: check ZIL list for sym_syn and prep variants
					- NA: update hand_mgmt() as needed for new_verb
					- NA: update *_err() to pass validate if hand_mgmt() will fix when called
					- NA: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add prep variants for new_verb to syntax
					- NA: add new_verb symetric syns to syn_verb_lst
					- NA: add new_verb symetric syns to syntax
					- NA: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- NA: fix scenario as needed
					- NA: clean up comments in static_gbl
				- DONE: go back and add ZIL sym_syn and prep variants to migrated verbs
				- DONE: 'close'
					- DONE: check ZIL list for sym_syn and prep variants
					- NA: update hand_mgmt() as needed for new_verb
					- NA: update *_err() to pass validate if hand_mgmt() will fix when called
					- NA: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add prep variants for new_verb to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst ('shut')
					- DONE: add new_verb symetric syns to syntax ('shut')
					- NA: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
						-DONE: test 'close bag' while in bkpk
					- DONE: scenario test
					- NA: fix scenario as needed
					- NA: clean up comments in static_gbl
				- DONE: 'push'
					- DONE: check ZIL list for sym_syn and prep variants
					- NA: update hand_mgmt() as needed for new_verb
					- NA: update *_err() to pass validate if hand_mgmt() will fix when called
					- DONE: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add prep variants for new_verb to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- NA: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- NA: fix scenario as needed
					- DONE: clean up comments in static_gbl
				- DONE: 'pull'
					- DONE: check ZIL list for sym_syn and prep variants
					- NA: update hand_mgmt() as needed for new_verb
					- NA: update *_err() to pass validate if hand_mgmt() will fix when called
					- NA: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add prep variants for new_verb to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- NA: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
					- DONE: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- NA: fix scenario as needed
					- NA: clean up comments in static_gbl
			- DONE: asym_syn for 'push' and 'pull'
				- DONE: add is_pushable() and is_pullable() identity_class()
				- DONE: assign is_pushable() and is_pullable to switch classes
				- DONE: create move_err() method like enter_err()
					- DONE: if is_item: 'Moving the do_noun reveales nothing'
					- DONE: if not (is_pushable or is_pullable): 'You can't move the do_noun'
				- DONE: add 'move' to non_action_verb_lst
				- DONE: add 'roll' and 'slide' as sym_syn_verbs
				- DONE: add 'move' to syntax
				- DONE: add 'roll' and 'slide' to syntax
				- DONE: add 'move' as asym_syn => 'push' or 'pull'
					- DONE: if is_pushable => push
					- DONE: if is_pullable => pull
					- DONE: if do_noun is_pushable & is_pullable > 'err', "How exact want to move?"
				- DONE: manual test
				- DONE: scenario test
			- DONE: solve 'list x' => 'inv is 1-word cmd' w/ user_input_lst[0] in err
			- DONE: clean-up legacy 2-word code
				- DONE: comment out code in interp()
				- DONE: comment out code in validate(), cmd_exe(), and trig_chk()
				- DONE: scenario test
				- DONE: clean-up code in interp(), validate(), cmd_exe(), and trig_chk()
			- DONE: fix 2-word debug cmds
				- IDEA: i've removed 2word_action but I never migrated get_weight, capacity, where_is
				- DONE: create debug_cmd_lst = ['get_weight', 'capacity', 'where_is']
				- DONE: add debug_cmd_lst to verbs_lst
				- DONE: add get_weight, capacity, where_is to syntax (bottom)
				- DONE: add early err check if verb_cmd_lst[0] in debug_cmd_lst and not is_debug
				- DONE: manual test
				- DONE: scenario test
				- DONE: comment out last '2word_case'
				- DONE: comment out verb_infer syntax entry
			- DONE: implement supplied do vs. infferred do vs. * syntax do *
				- IDEA: as much as possible, syntax() should represent what interp thinks user meant
				- DONE: 'inventory'
				- DONE: manual test
				- DONE: scenario test
				- DONE: it works but it's a mess! refactor and see if I still want this
				- DONE: manual test
				- DONE scenario test
				- DONE: commit
				- DONE: clean up comments and re-commit
				- DONE: refactor do_noun collection to call out 'inventory' case at top; clean up vars
				- DONE: 'jump'
				- DONE: 'stand'
				- DONE: comment out one_word_only err
				- DONE: manual test
				- DONE: scenario test
				- DONE: commit
				- DONE: clean up comments and re-commit
				- DONE: review var assignment - comment unneeded
				- DONE: clean up comments
				- IDEA: what if I elim the no-do_noun-inferred-err and just err in syntax if do req?
					- IDEA: leaning against this because it's helpful to signal "examine what?"
					- DONE: final decision => keep no-input-do verbs separate to enable "X what?"
				- DONE: update verb spreadsheet => one_word only => syntax do
			- DONE: make a spreadsheet of all 2word verbs (columns include has *_err, has method)
				- DONE: add hand_mgmt() column
					- DONE: start table
					- DONE: complete up to 'open'
					- DONE: pull and push
					- DONE: read
					- DONE: sit
					- DONE: stand
					- DONE: complete table
		- INPROC: direction verbs
			- DONE: generalize 'go':
				- DONE: base version
					- DONE: check ZIL list for sym_syn and prep variants: go, walk, run, proceed, step
					- NA: update hand_mgmt() as needed for new_verb
					- NA: update *_err() to pass validate if hand_mgmt() will fix when called
					- DONE: disable global syn for new_verb
					- DONE: add new_verb to interp() action_verb list
					- DONE: add base ('new_verb', 'do_noun') entries to syntax
					- DONE: add prep variants for new_verb to syntax
					- DONE: add new_verb symetric syns to syn_verb_lst
					- DONE: add new_verb symetric syns to syntax
					- NA: add infer do_noun entry for new_verb as needed
					- NA: in asym_syn(), add conditional syn as needed
				- DONE: create new verb_do_prep case
					- DONE: update validate()
					- DONE: update cmd_exe()
					- DONE: update trig_chk()
				- DONE: testing
					- DONE: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
					- DONE: scenario test
					- DONE: fix scenario as needed
					- DONE: clean comments in static_gbl, interp(), validate(), cmd_exe(), trig_chk()
				- DONE: verb infer
					- DONE: create infer_verb()
					- DONE: call infer_verb()
					- DONE: define dir_lst and enable new interp if word1 in verb_lst + dir_lst
					- DONE: disable legacy interpreter
					- DONE: add 'go' as non-do cmd
					- DONE: manual test
					- DONE: scenario test
					- DONE: comment out old 'go' code including legacy syntax code
					- DONE: comment out old go_err() for non-dir preps
					- DONE: clean up interp() & go_err()
					- DONE: comment out action_dir case
					- DONE: update verb table with 'go'
					- CANCEL: if verb in ['go'] => infer dir ???
					- DONE: generalize travel case? (infer verb?)
						- DONE: update verb spreadsheet
				- DONE: enter
					- DONE: asym syn for 'enter door'
						- DONE: create get_door_dir() in map
						- DONE: create is_door() identity and assign to door classes
						- DONE: in asym_syn(), if is_door and in_room, call get_door_dir => go dir rm
						- DONE: manual test
						- DONE: scenario test
						- DONE: clean up comments in interp()
					- DONE: enable enter for paths?
						- DONE: decide if this is desired => yes
						- DONE: create Pathway() class with is_pathway() identity
						- DONE: in dc game_update() import Pathway from base_class()
						- DONE: change pathway_obj classes to Pathway()
						- DONE: update 'enter' condition in asym_syn to include paths
						- DONE: manual test (will also test map door dict case)
							- DONE: fix crash on 'enter portcullis' from throne_room (wrong hero_rm?)
						- DONE: scenario test
					- DONE: infer seat / door if no seat and only 1 door/pathway in room
						- DONE: create infer_do() routine for 'enter'
						- IDEA: prefer doors over pathways
						- IDEA: prefer seat_obj over door_obj if 1 of each available
						- IDEA: always assume in-room before out of room
						- DONE: manual test
						- DONE: scenario test
						- NA: clean up comments in interp()
					- DONE: update verb table with 'enter'
					- DONE: 'in' / 'go in'
						- DONE: 'in' => 'go in' via verb_infer()
						- DONE: create prep_phrase_convert()
							- DONE: after prep, before do, if prep > 0:
								- DONE: similar to sym_syn() but includes verb & preps
								- DONE: 'go in' => 'enter'
							- CANCEL: 'go in' => 'go in seat / door' via do_infer()
							- CANCEL: 'go in do_noun' => 'enter do_noun' via syntax()
							- IDEA: 'enter do_noun' => sit / 'go dir' via asym_syn
						- DONE: test manually
						- DONE: test scenario
						- DONE update verb table with 'in' & prep_phrase_convert
					- DONE: 'get in' => 'enter'
						- DONE: 'get do_noun' => 'take do_noun'
							- DONE: 'get' to non_action verb
							- DONE: in syntax: 'get' => 'take'
							- DONE: manual test
							- DONE: scenario test
							- DONE: update verb table
						- DONE: 'get in' => 'enter'
							- DONE: add 'get in' => 'enter' in prep_phrase_convert in syntax
							- DONE: manual test
							- DONE: scenario test
							- DONE: update verb table
							- DONE: clean up interp()
					- DONE: clean up existing code:
						- DONE: enter_err() in err()
						- DONE: enter() in seat()
				- DONE: exit
					- DONE: create depart() as method of room?
						- IDEA: if only one exit, depart via that exit
						- IDEA: what would a depart action do other really do other than call go()?
						- IDEA: if nothing, then keep logic in asym_syn
						- DONE: make depart a sym_syn of exit()
						- DONE: manual test
						- DONE: scenario test
						- DONE: update verb table w/ 'depart'			
					- DONE: in map, create is_only_1_exit, dir_str = gs.map.only_exit_dir(room, gs)
					- DONE: asym_syn 'exit room' (w/ only 1 exit) => 'go towards exit'
						- DONE: update asym_syn w/ call to map.only_exit_dir()
						- DONE manual test for 'exit room'
						- DONE: scenario test
					- DONE: infer room if no do_nuon
						- DONE: if contained => seat, else hero_rm
						- DONE: manual test
						- DONE: scenario test
						- DONE: update verb table with 'exit'
					- DONE: 'get out' => 'exit'
						- DONE: add syntax entry
						- DONE: test manual
						- DONE: test scenario
						- DONE: update verb table w/ 'get out'	
					- DONE: 'go out' => 'enter'
						- DONE: 'go out' => 'enter' via prep_phrase_convert syntax lookup
						- DONE: test manual
						- DONE: test scenario
						- DONE: update verb table with 'go out'
					- DONE: 'out' => 'go out'
						- DONE: 'out' => 'go out' via verb_infer()
						- DONE: test manual
						- DONE: test scenario
						- DONE: update verb table with 'out'
					- DONE: clean up existing code:
						- CANCEL: exit_err() in err()
						- DONE: exit() in seat()
			- DONE: interp() structure review
				- DONE: convert do_enter_seat key to do_sit_seat key
				- DONE: convert do_exit_container key to do_stand_container key
				- DONE: consolidate user_cmd assembly
				- DONE: in interp() sentence analysis - consider combining dir & prep
					- DONE: review, comment, and refactor core infer proc loop
					- DONE: consolidate dir & do_prep
					- DONE: manual test
					- DONE: scenario test
					- DONE: clean up comments
				- DONE: convert format from verb_do_prep => verb_prep_do (matches real usage)
			- DONE: claude ideas
				- DONE: consistent use of prep_lst
				- DONE: create intransitive_verb_lst
				- DONE: function to perform bool-based cmd analysis
				- DONE: scenario test
				- DONE: manual test
				- DONE: clean-up comments
				- DONE: transfer to Claude clone
				- DONE: get additional Claude thoughts - especially on climb()
			- DONE: generalize 'climb':
				- DONE: climb ideas
					- IDEA: reference Claude updates for 'climb' in do_infer()
					- IDEA: simplify climbable atribs: auto gen success & fail climb messages?
						- IDEA: or maybe fail is just baked into obj?
					- IDEA: keep climb() as action to enable message (??)
					- CANCEL: via asym_syn, 'go up <rm_obj>' => 'climb <obj>' if climbable obj exists
					- CANCEL: should climb => go in asym_syn ???
					- IDEA: if verb in ['go', 'climb'] => infer dir
				- DONE: discovery
					- DONE: in error():
						- DONE: review climb_err() - capture notes and output examples
							- NOTE: replace self.err_dir w/ if creature_climb_dir_do_err in, buff_s()
					- DONE: in base():
						- DONE: review climb() - capture notes and output examples
							- NOTE: buff_s(self.discript_dir) => buff_s(creature_climb_dir_do_success)
						- DONE: review ClimbableMixIn:
							- NOTE: elim attribs
						- DONE: review ClimbableViewOnly
							- NOTE: elim attribs
					- DONE: in game_update()		
						- DONE: review 2x tree
							NOTE: elim descript attribs
					- DONE: in interp()
						- NOTE: update syntax
						- NOTE: update infer_do and migrate climb_infer
						- NOTE: comment out climb_infer
						- NOTE: create infer_prep() and migrate up_or_down code
						- NOTE: call infer_prep() from interp() post infer_do()
						- NOTE: comment out syntax up_or_down and hero_dir
						- NOTE: add 'climb' to action verb
						- NOTE: comment out legacy interp climb code
						- NOTE: make asym_syn for 'go up' => 'climb up obj' if exactly 1 climbable obj
						- NOTE: in validate(), cmd_exe(), and trig_chk(), elim case = action_dir
				- DONE: pre-climb claude code to-do:
					- DONE: ask why claude made changes with no planning
					- DONE: back out existing changes
					- DONE: switch to sonnet 5 high effort
					- DONE: ask about planning mode
					- DONE: propose changes and ask for feedback
						- DONE: what do my proposed changes tell you about my coding approach?
						- DONE: what am i missing here?
						- DONE: what would an expert do?
					- DONE: initial implementation plan with claude
				- DONE: 'climb'
					- DONE: simplify climb() command:
						- CLAUDE: in base()
							- DONE: ClimbableMixIn => remove attribs
							- DONE: ClimbableViewOnly => remove attribs
							- DONE: climb():buff_s(self.de_dir) > buff_s(creature_climb_dir_do_success)
							- DONE: climb(): valid_dir_chk() pre buff custom or default success message
						- CLAUDE: in game_static_gbl():
							- DONE: update both tree climb descript keys
								- DONE: creature_climb_dir_do_err
								- DONE: creature_climb_dir_do_success
						- CLAUDE: in game_update():
							- DONE: update both tree obj => elim attribs
						- CLAUDE: in error():
							- DONE: replace self.err_dir w/ if creature_climb_dir_do_err in, buff_s()
						- DONE: test
							- DONE: manual test
							- DONE: scenario test
							- DONE: fix scenario test
							- DONE: clean comments: game_update, game_static_gbl, climb_err(), climb()
					- DONE: planning with Claude
						- DONE: direct Claude to prod repo
						- DONE: discuss syntax sym_syn and elim of hero_dir
						- DONE: refine phase 2 plan
						- DONE: discuss how commits work
					- CLAUDE: update basic climb parsing in interpreter()
						- DONE: sym_syn
							- DONE: check ZIL list & google for sym_syn and prep variants
							- DONE: disable global syn for new_verb
						- NA: hand_mgmt
							- NA: update hand_mgmt() as needed for new_verb
							- NA: update *_err() to pass validate if hand_mgmt() will fix on call
						- CLAUDE: add to new interp() processing:
							- DONE: add new_verb to interp() action_verb list
							- DONE: add new_verb symetric syns to syn_verb_lst
							- DONE: comment out legacy interp climb code
						- CLAUDE: syntax:
							- DONE: add base ('new_verb', 'do_prep_noun') entries to syntax
							- DONE: add prep variants for new_verb to syntax
							- DONE: add new_verb symetric syns to syntax
							- DONE: comment out old syntax entries
							- TOM: comment out syntax up_or_down
						- CLAUDE: testing
							- DONE: manual testing
							- DONE: scenario testion
					- DONE: advanced climb() features in interpreter():
						- CLAUDE: infer_do:
							- DONE: add infer do_noun entry for new_verb as needed
							- DONE: migrate stand-alone climb_infer and comment out
							- DONE: comment out infer_do_noun in sytax (??)
						- CLAUDE: infer_prep:
							- DONE: create infer_prep() and migrate up_or_down code
							- DONE: call infer_prep() from interp() post infer_do()
							- DONE: comment out syntax up_or_down and hero_dir	
						- CLAUDE: in asym_syn(), add conditional syn as needed
							- DONE: 'go up' => 'climb up obj' if exactly 1 climbable obj
							- DONE: create gs.io.repeat_str flag to avoid 'go' infinite loop
						- CLAUDE: finalize with Claude:
							- DONE: move move_decr() from climb() to insert_cmd_queue() ?
							- DONE: in infer_prep(), update default err_txt & move 'which way' to else
							- DONE: final review of ui - am I infering too much; 'climb down tree' case
						- CANCEL: fix climb() => go() kludge
							- CANCEL: call room-transition routine (room_class_def.py:304-328)
							- IDEA: need to re-process in case there is a trap door
						- CANCEL: allow do w/ 'go' => 'go n from entrance' (infer do vs. syntax)
					- CLAUDE: testing
						- DONE: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
						- DONE: scenario test
						- NA: fix scenario as needed
					- CLAUDE: case clean-up
						- DONE: in validate() => elim action_dir case
						- DONE: in cmd_exe() => elim action_dir case
						- DONE: in trig_chk() => elim action_dir case
					- CLAUDE: close out
						- DONE: clean up all comments
						- DONE: manual test
						- DONE: scenario test
					- DONE:
						- CLAUDE: fix cup_of_tea error
						- TOM: update verb table
		- TOM: fable strategic thinking session
			- DONE: share links with fable for Infocom and modern IF
			- DONE: ask fable to review my code
			- DONE: ask for +/- on my class-based, obj-oriented code and advice on key updates to make
		- INPROC: post fable immediate updates
			- DONE: refactor go()
				- IDEA: treat go() as special because
					- IDEA: only verb to be inferable
					- IDEA: will never have user-provided do, id, or prep
					- IDEA: never searches local room for scope
					- IDEA: is used frequently => address first
				- DECISION: keep dir as prep; continue to use verb_prep_do for go()
				- DONE: separate go and infer_verb and deal with before main processing
				- DONE: skip rest of do_noun, prep, and id_noun processing
				- DONE: but make sure to still run asym_syn() due to climb()
				- DONE: fix issues:
					- DONE: move verb_syn call above is_go = True
					- DONE: fix climb() cmd
					- DONE: clean up comments
					- FINDING: need 'prep_phrase_convert' for go()
					- FINDING: go() and other intransitive verbs share most of the same issues
				- DONE: revised strategy
					- DONE: accept verb_infer as in-line special exception
					- DONE: back out special go() case
					- DONE: skip do_noun and id_noun for all instransitive verbs
					- CANCEL: maybe dedicated syntax call ??? (and asym ???)
					- DONE: declare do_noun_str and id_noun_str at top
				- DONE: test manually
				- DONE: test scenarios
				- DONE: clean up interpreter()
				- DONE: clean up infer_verb()
				- DONE: review updates with Opus
				- DONE: commit
				- DONE: in verb table, move infer_verb column to notes column
				- DONE: in verb table, add column for intransitive_verb_lst
			- DONE: understand and implement keyword usage for the action_list
				- DONE: understand where class Command() lives and how assigned in Syntax
				- DONE: understand temp adaptor phase A - including dispatch table
				- DONE: understand phase B
				- DONE: ask about meta cmds, help, and error messages
				- DONE: decide on order of operations
		- INPROC: finish verbs
			- DONE: review notes finalize verb_do and verb_prep_do
				- DONE: jump
					- IDEA: custom 'jump' result will freq depend on rm (e.g. 'jump' => moat)
					- DONE: 'jump' => associate with Room class instead of Creature class??
						- DONE: add jump() method to Room()
						- DONE: comment out jump() for Creature()
						- DONE: update syntax to convert jump do to 'hero_rm'
						- DONE: update entrance jump mach trigger
						- DONE: manual test
						- DONE: scenario test
						- DONE: clean up comments in creature(), room(), and syntax()
						- DONE: update verb table
					- CANCEL: allow prep phrase 'jump in moat' => 'enter moat' ???
					- CANCEL: 'jump' => 'jump <room>'
			- TBD: method-ize meta commands and call them via shapes (meta, meta_arg)
				- TBD: exclude from validate(), chk_trig(), score()
			- TBD: methodize help and call via shapes (meta_arg)
				- TBD: exclude from validate(), chk_trig(), score()
			- TBD: return parse_err and eliminate 'error' case
			- TBD: convert prep case to verb_do_prep_id and verb_id_prep_do shapes
				- TBD: address hand mgmt in hand_manage()
				- TBD: fix 'blank' first attrib in noun_handling() call
				- TBD: 'put on' as syntax syn for 'wear'
				- TBD: need to signal diff between surface and cont ('put on' vs. 'put in')
				- IDEA: 4th 'prep_in' term added to action_lst to be checked in syntax??
				- TBD: consider not passing verb or prep to syntax as independent attribs
				- TBD: weapon updates
					- TBD: add 'wield' for weapon class; take() => wield() if obj.is_weapon()
					- TBD: add 'sheathe' for weapon class; stow() => sheathe if obj.is_weapon()
					- TBD: sort out weapon state buffers in hand_manage()
					- TBD: elim / integrate app_main() weapon tracking via wield & hand_mgmt
					- TBD: standardize weapon draw on attack
			- TBD: create stool() obj == seat() ('sit in/on') + platform()  ('stand on')
			- TBD: update verb spreadsheet
			- TBD: phase a (see Claude)
			- TBD: phase b (see Claude)
		- TBD: future claude collaboration ideas
			- TBD: full language scenario suite
			- TBD: web site
			- TBD: database
		- TBD: elim meta_cmd_lst / 'one_word_convert_lst' in static_gbl
				- TBD: <word_x>
					- TBD: check ZIL list for sym_syn and prep variants
					- TBD: update hand_mgmt() as needed for new_verb
					- TBD: update *_err() to pass validate if hand_mgmt() will fix when called
					- TBD: disable global syn for new_verb
					- TBD: add new_verb to interp() action_verb list
					- TBD: add base ('new_verb', 'do_noun') entries to syntax
					- TBD: add prep variants for new_verb to syntax
					- TBD: add new_verb symetric syns to syn_verb_lst
					- TBD: add new_verb symetric syns to syntax
					- TBD: add infer do_noun entry for new_verb as needed
					- TBD: in asym_syn(), add conditional syn as needed
					- TBD: manual test (including sym_syn, prep, infer, asym syn, and hand_mgmt)
					- TBD: scenario test
					- TBD: fix scenario as needed
					- TBD: clean up comments in static_gbl
					- TBD: clean up action_dir case in validate(), cmd_exe(), and trig_chk()
			- TBD: update verb spreadsheet
		- TBD: one-word debug commands
			- TBD: update verb spreadsheet
		- TBD: additional updates post migration
			- TBD: update help() cmd to give a limited list of verbs ?
			- TBD: in doc section, call out interp asym: more permissive >> less permissive
			- TBD: consider including bkpk in infer_do_noun() scope (e.g. if crown in bkpk, wear it)
			- TBD: global refactor
			- TBD: simplify do_noun_obj vs. do_noun_str being converted back and forth
			- TBD: clean up comments
		- TBD: document 'someday maybe' verbs (e.g. 'slide under') in spreadsheet
		- TBD: update existing test scenarios as needed if no longer pass
		- TBD: create language test game for language (or plan now, avoid more nouns till later?)
			- TBD: create spiral rooms w/ diagonal paths
			- TBD: create colored doors
			- TBD: populate with test view-only obj, seats (first 4 of 9 rooms only)
			- TBD: populate with test items, food, garments, writing, buttons, levers
			- TBD: scenario test for all 2word verbs:
		- TBD: re-do multiples w/ positional approach; support 'and', ',', and multiple except
		- TBD: verbs, hand_mgmt, symetric syn, infer, asymetric syn
			- Room 1: (list obj)
				- TBD: take()
				- TBD: drop()
				- TBD: stow()
				- TBD: wear()
				- TBD: doff()
				- TBD: eat()
				- TBD: read()
				- TBD: push()
				- TBD: pull()
			- Room 2: (1 chair)
				- TBD: sit()
				- TBD: open()
				- TBD: close()
			- Room 3: (2 chairs?)
				- TBD: sit()
	- TBD: review / unify all interp() update notes
	- TBD: document new interp() approach
		- TBD: credit zork and bolggers
		- IDEA: 3 things I learned from zork: 
			1) verbs vs. actions
			2) syntax: blunt but effective - language is idiomatic; lack of gen prep rules
			3) actions on nouns
		- IDEA: trends i didn't follow:
			1) class system vs. flat w/ attribute bits
			2) retained preps


		- TBD: nouns
			- TBD: simplify noun clause sent to noun_handling()
			- TBD: enable multiple adjectives
			- TBD: improve noun_handling errors
			- TBD: check for action (err or cond_syn or mach) in do & id pre verb action
			- TBD: doc idea of replacing climb_err txt with climb obj action error


		- TBD: create separate full_verb_lst vs. full_action_lst
		- TBD: refactor cmd_exe() help & meta
			- TBD: create help() method where 'help' is verb and 'option' is prep
			- TBD: create meta() method where cmd = verb
			- TBD: updeate cmd_exe() to parse meta_cmd_lst options
		- TBD: review and implement over-arching interp() org
			- TBD: review by hand
			- TBD: discuss with Q
			- IDEA:
				- process / clean (txt)
				- identify verb, dir (txt)
				- identify do_noun, id_noun, & preps (txt / rm)
					- dis-ambugate nouns (rm)
				- call syntax: verb => action (txt)
					- fill in infferable terms (rm)
				- hand-manip (rm)
				- run action => err or execution (rm)

		- TBD: support 'climb up' and 'climb down' w/ no do_noun (i.e. search for climbable obj)
	- TBD: consolidate case = 'error' and [err_txt] into syntax
	- TBD: clean-up weapon_disp in app_main() module => weapon() class
	- TBD: clean-up multipls functions in app_main() module
	- TBD: sort out 2word
		- IDEA: above go / climb special cases




	- 4.a.0 review and refactor interp() [INPROC]
		- 4.a.0.i review base interp() code [DONE]
		- 4.a.0.ii create main interp() routine that calls others (e.g. clean-up and 1-word) [INPROC]
		- 4.a.0.iii extract hand management to an external hand_manage() function [TBD]
		- 4.a.0.iv extract prep_verb hand mgmt to hand_manage() [TBD]
		- 4.a.0.v deep review of noun_handling() [TBD]
	- TBD: create new scenario test
		- TBD: test for reserved syntax words


	- 4.a.1 update noun attributes [TBD]
		- resarch and finalize eliminating obj-as-mach approach
		- add list attribs for syn_lst, adj_lst, invis_lst
			- how to introduce optional attribs?
			- discuss plan w/ Q
	- 4b. create scope_lst and noun_syn_lst
		- 3b1. convert cmd_str_lst to root nouns using noun_syn_lst
	- 4c. in scope_lst, for do-noun clause
		- 3c1. find noun in scope_lst
		- 3c2. validate adj (error if not found?) and removed
		- 3c3. identify do-noun
		- 3c4. if no noun or > 1 noun => err
	- 4d. in scope_lst, if id-noun clause exists
		- 3d1. find noun in scope_lst
		- 3d2. validate adj (error if not found?) and remove
		- 3d3. identify id-noun
		- 3d4. if no noun or > 1 noun => err
	- 4e. identify each non-buzz prep
	- 4f. if verb is on class_spec_vrb_lst, check if do-noun supports it
		- 3f1. if yes, proceed; else, std err

	- TBD: post noun-sorted-out verb updates:
		- TBD: climb & go:
			- IDEA: create unified action_dir syntax call
			- TBD: 'climb' <dir> => syntax => 'climb' <dir> <rm>
			- TBD <rm> specific error in climb_err()
			- IDEA: enables local rm override for Tree

		- DONE: plan for class-specific verb synonyms 
			- IDEA: examples:
				'doff' => (garment class) => take
				'jab', 'hack', 'slash' => (weapon class) => attack
			- TBD: in static_gbl: cond_verb_syn_lst
			- TBD: chk_class_syn() method in ViewOnly
			- IDEA: updates for Invisible class
				- IDEA: attrib == suptd_vrb_lst
				- IDEA: method == chk_class_spec_vrb()
			- IDEA: the challenge here is that we need to ask the noun about the verb
			- IDEA: PARSE is supposed to identify the verb and noun(s)
			- IDEA: SYNTAX is supposed to convert the verb, noun(s), and prep(s) in an action
			- IDEA: so between PARSE and SYNTAX i need a routine to check class-specific verb synonyms
			- IDEA: see 4f
		- TBD: create Zork and DC verb / class / synonym list
			- TBD: understand which zork verbs will be relevant to dc
			- IDEA: verb list org
				- IDEA: master verb list is in cleesh static_gbl
				- IDEA: class_spec_syn_lst lives in verb method as attrib


- 5. use syntax with verb, do-noun, id-noun, and prep to identify action
	- 5a. apply Get What I Mean (GWIM) if the id-noun is missing
	- 5b. error if GWIM retruns 0 or > 1

	- TBD: also need a plan for syntax_verbs:
		- EXAMPLE: 'sit on' / 'sit in' => (syntax checks for seat class) => enter
		- IDEA: in this case, we don't want to replace 'sit' with 'enter' at the start
		- IDEA: instead, we convert to enter via SYNTAX routine
		- IDEA: so 'sit chair', 'sit in chair', 'sit on chair' all => enter chair
		- IDEA: but 'sit to chair' and 'sit with chair' => error
		- IDEA: 'sit' only = 'enter' when accompanied by prep = 'in' or 'on'


- 6. execution loop:
	- 6a. check id-noun for do-noun / action specific errors
	- 6b. check do-noun for id-noun / action specific errors
	- 6c. execute action (passing in do-noun & id-noun)

	- TBD: decide about verb synonyms for specific obj??
		- EXAMPLE: 'enter' / 'go in' on 'castle' => action = "go north"
		- EXAMPLE: 'exit' / 'out' on 'gatehouse' ('exit' w/out noun => room) => action = "go sounth"
		- EXAMPLE: 'enter' / 'go in' on 'moat' => action = "go east / go west"
		- EXAMPLE: 'enter' / 'go in' on 'path' => action = "go southwest"


- 6.5. optimize:
	- 6.5a. skip "of" and word before (e.g. "one of", "piece of")
	- 6.5b. sort out rand_mode on one_word_secret_lst and alos debug_verb_lst


- 7. introduce new words
	- INPROC: list of words to add this branch
		- IDEA: prep = to, at, on, in
		- IDEA: this
		- IDEA: walk in, look at, look in
		- IDEA: enter / in (doors, viewonly, rooms)
		- IDEA: exit / out (doors, viewonly, rooms)
		- IDEA: xyzzy
		- IDEA: curse
	- TBD: Curse Words
		- TBD: implement curse warning / ending at Interpreter() level

	- TBD: expand verb method assignment for classes
		- EXAMPLE: add 'enter' as method for door class
		- EXAMPLE: add 'enter' and 'exit' as methods for room (?)
		- EXAMPLE: have a '2 state' switch that can change via 'move', 'push', or 'pull' => chair
	- TBD: re-institue remove() verb for Garment; 'take' as synonym (???)
		- worn obj take() => "You're already wearing it" (no, take should always be 'into hand')
		- obj on floor remove() => "Taken" (i.e. is synonym)


- 8. add new in-scope zil capabilities


*** RAW TO-DOS ***

- INPROC: additional list of zil attrib abilities to bring to dc
	- IDEA: differentiate between container & surface class (contbit vs. surfacebit)
	- IDEA: attrib to not display desc (ndescbit) because it will be described by room
	- IDEA: has the obj been touched / room been entered? (touchbit)
	- IDEA: don't use articles w/ obj description attrib (narticlebit)
	- IDEA: obj is plural and desc treat it as such (pluralbit)
	- IDEA: an ad-hoc way to make a given object the default noun in a cmd (kludegegit)
	- IDEA: obj is a body part [e.g. fist] (partbit)

- INPROC: list of zil properties to bring to dc
	- IDEA: IN / OUT (aka enter / exit); for rooms w/ 1 exit and viewonly (e.g. "castle")
	- IDEA: SYNONYM => syn_lst attrib
	- IDEA: ADJECTIVE => adj_lst attrib
	- IDEA: ACTION => how to trigger from noun? mach_lst ? Also maybe err_lst ?
	- IDEA: GENERIC => way to make noun the default do_noun ? What if more than 1?

- INPROC: machine encapsulation
	- IDEA: achieve greater standardization by encapsulating all modular machines in obj
	- IDEA: this way, obj themselves are never actually obj
	- IDEA: greater standardization and fewer classes
	- DONE: review existing machs nouns: big_rock, kinging_scroll, shiny_sword
	- DONE: review existing switch nouns: throne
	- TBD: make decision

- INPROC: new attribs needed for obj:
	- IDEA: syn_lst
	- IDEA: adj_lst
	- IDEA: err_dict [method required to read dict w/ wildcards / class {e.g. is_weapon}]
	- IDEA: enable run of machs based on io-noun, do-noun, and action (???)

- INPROC:
	- DECISION: does updated interpreter require updated perform flow?
	- FINDING: dc today = pre_action, cmd_exe, post_action, auto_action
	- FINDING: infocom = player, player_rm, verb_pre_act, id_act (include id cont), do_act, verb_act
	- TBD: decide whether / how to update perform loop
	- TBD: consider idea of separate obj, ind-obj, and verb error routines

- INPROC:
	- DECISION: do i want to incorporate any of these zil ideas?
		- TBD: look-inside action that only shows contents?
		- TBD: use of vehicles?
		- TBD: us of universal obj predicates (chk routines); e.g. chk_lit() ?
		- TBD: goto rountine (enable teleportation to another room)
		- TBD: ability to light things on fire

- INPROC: additional ideas
	- TBD: create enter cmd for doors / portals?
	- TBD: set 'exit' / 'out' for rooms with only 1 door?
	- TBD: exapnd on use of "look at / in / on", "go in / on", etc.
	- TBD: separate rooutine for help? remove from known_verb_lst ?
	- IDEA: zork treats directions as their own part of speech - should i do the same?
	- IDEA: in zork, the mapping for in, out, enter, and exit are set in room...
	- IDEA: if not set in room, i'll need some way to interpret them, with "()"s

- TBD: noun synonyms
	- TBD: sort out noun synonyms (with local awareness and game assignmet)
	- TBD: error and synonmy option for nouns?
	- TBD: should synonyms be an obj attribute?? => noun synonyms
	- TBD: need to enable a rich set of game-specific synonyms!
		- TBD: make 'apparatus' a synonym for control_panel
		- TBD: add '* apparatus' as trigger to goblin_attack_mach
	- note zil approach of separate adjectives & synonyms (can have multiple adj)
	- interp() refacto shoud be based on objects (contents of rooom)
	- each obj should have noun syns (in place of root_word)
	- noun synonyms (list in place of base_name)

Preposition Handling:
- DONE: unlock => 'unlock with' prep  command
- TBD: default prep behavior = try command with obj in hand
- IDEA: in interp(), what about making prep check similar to put() for all prep verbs
	- IDEA: could have a prep attribute for each prep verb
	- IDEA: in interp(), have a list of all possible preps and use list to break sentence
- DONE: gracefully deal with uneeded preposition usage (e.g. "push on button")
	- DONE: syntax will solve this
- Interp deep dive including better solution to prep checking ('put in' vs. 'put on')
	- DONE: syntax will solve this

Sentence Structure:
- TBD: implment syntax concept using preps
- if user input has multiple obj, determine noun vs. dir_obj from prep usage (i.e. to vs with)
- IDEA: prep_no_do (prep no direct-object verbs):
	- DOC: format = '<verb> <prep> <noun>' (e.g. 'climb up tree')
	- FINDING: climb requires a method because not every ViewOnly obj can be climbed
	- FINDING: this is true even when the climb direction is available in io.map()
	- IDEA: this is not true for 'sit in chair' (i.e. any chair should support sitting)
	- IDEA: but it's worth noting that the sentence structure is the same
	- IDEA: ideally, ['sit in', 'sit on'] would just become abreviations for 'enter'
	- IDEA: but if this is not possible, a sit() method could be created similar to climb()
	- DONE: syntax will solve this

Plurals:
- TBD: interpreter - should all nouns be singular? 
- TBD: solve articles for innate plurals (e.g Water, Tea => "qty of water" ???)
	- TBD: requires noun-adj strings longer than 2
	- PLAN: use 'qt of' / 'collection of' / 'the junk mail' for all plurals
- IDEA: convert plurals to singulars for this???
- CANCEL: (given that there is water in the game maybe all singlulars is impossible?)
- CANCEL: sort out approach to plurals
	- 1) perhaps this becomes a ViewOnly attribute??? (don't like this - way too many un-used cases of attribute)
	- 2) possibly ItemPlural class inherits from Item and has method is_plural() which returns True ??
	- 3) could just have a plural_tuning_lst in the txt_handling() module that checks for known plurals as a one-off?
		- Note: the problem with defining plurals in classes is, what if I want to establish plurals for a non-obj (e.g. a path)
	- Maybe apply 'xxy' prefix on text list if plural??

Pronouns:
	- Do I need a gs.Gramarian class to deal w/ recurring display issues around pronouns and plurals?
	- e.g. pronoun_tobe(creature) => 'You are' or 'The <creature.full_name> is'
	- e.g. article_plural(obj) => 'a Grimy Axe' or 'Water' or 'an Apple'
	- maybe plural_dict is a local dict in the Gramarian class?
	- Or maybe a better class name is just Display (???)
	- Division of labor: player text => commands == Interp; obj => player response == Output
	- could put some recurring dispaly routines here (obj_lst => str_lst and such) ??
	- Display could also hold buffer commands???
	- Another possible class name == Output ???
	- Leaning towards Output... this helps distinguish from all the verb-linked Disp methods

Do What the Player Means:
- TBD: special case of guessing what player means if they don't specify in full
	- TBD: how should this work? Should they need to be aware of what's in their hand?
	- TBD: default to key-like obj for lock / unlock activity?
	- TBD: review inform flags used for (Get What I Mean)
	- TBD: how to implement?
	- TBD: should be based on class => create Key class, is_key() method
- TBD: updates on this theme
	- TBD: now that hand is de-emphasized, need a better system for guessing what obj player means
	- TBD: should be mostly based on class
- TBD: assume that item in hand will be used for activity (e.g. attack)

Believed to be Done:
- TBD?: fix progromatic usage of "a" vs "an" (e.g. "There is a Iron Portcullis to the north")
- DONE: change backpack and worn lists to include 'a' and 'an'
- IDEA: maybe a txt_handling() module with a disp_lst() func that takes care of 
	- DONE: "x", "x & y", "x, y, & z"; 
	- DONE: 'a' or 'an'; 
- DONE: Can 'a' vs. 'an' be fixed?
- DONE: basic interp features: 'take all', 'again', 'wait'
	- DONE: more abreviations: 'g' = 'again', 'z' = 'wait'
	- DONE: enable 'take all'
	- DONE: enable "take all", "drop all"
- DONE: create 'jump' command with same response as Zork ('Whee!' I think?)
- DONE: randomize description of Burt shown during 'inventory'
	- DONE: randomize frequent responses (e.g. "in your spell book you see...")
- DONE?: address 'I can't see a x_y' error
	- IDEA: need a better way to error on 'x'_'y' != obj.name
	- IDEA: maybe if '_' in noun, buff: "I don't see that"
- DONE?: consider introducing str_to_obj_dict in Core
	- IDEA: (enable ease of entrance.examine(gs) in startup() )

Tactical Fixes for Existing Code / Features:
- TBD: get multiples code out of app_main() [see climb() coding]
- TBD: remove rand_mode from one_word_secret_lst ?
- TBD: word_lst assignment:
	- prep case word_lst => trig_vals_lst is erratic
		- (see interp() ln 201, validate() ln 32, & mach_class() ln 72)
- TBD: fix interp() prep_verb noun vs. dirobj nomenclature once and for all!
	IDEA: swap to meth_noun_str and attrib_noun_str ??
- TBD: sort out 'can't drop fist or brass_lantern issue
- TBD: drop node 3 (portable_containers in containers) disp???
	- TBD: can burt know about node 3 items he hasn't 'seen' in this game?
	- TBD: play through Zork kitchen to test out
- TBD?: can I store variables in static_dict strings? (in f-string format)
- TBD?: can I return method errors based on verb method
	- EXAMPLE: (e.g. "Burt, what kind of person would try to attack a Throne?")
- TBD: convert words like 'look' to 2word in interp(), rather than cmd(), if possible

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




############################
### END CLEESH VERSION 3.9.3 / DARK CASTLE VERSION 3.4.2 ###
############################


*********************
*** SOMEDAY MAYBE ***
*********************


*** tactical bug backlog ***
- TBD: provide better error on attempt to interact with an item you can see on ground when in tree
	- INFO: issue is that 'x' shows drop_rm contents but no other cmd is aware of obj outside room

*** structural ***
- TBD: maybe call disp_weapon from within cmd_exe() instead of in app_main() due to score??
	- EXAMPLE: 1) get sword from hedgehog, 2) attack goblin 'with sword' from bkpk
- TBD: should burt auto-draw weapon when attacked (e.g. 'go n' near goblin)?
	- IDEA: add 'draw_weapon' call into attack()
- TBD: should burt auto-draw weapon when for moat case?
- TBD: create a wearabel portable container and test lvl 2 with prep & 2_word
	- IDEA: simple wearable portable container would be a "fanny pack"
	- TBD: create class for wearable portable container
	- TBD: instantiate "fanny pack"
	- TBD: test basic functionality
	- TBD: test functionality with all in-scope 2_word & prep verbs
	- TBD: test whether game can distinguish between 'pack' and 'pack'
- TBD: leverage app_main() cmd_queue for 'again' command ?
- TBD: enable use of 'and' with action multiples ?
- TBD: enable use of 'from' with action multiples ??
- TBD: consider other possible uses for **kwargs; google "when to use kwargs in python"
- TBD: find a good use for TravelResult !!
- TBD: at end of story-driven updates, elim "##" error messages in error()
- TBD: sort out local buffering in standard errors?
- TBD: update validate() to move debug error indicators to pre rather than post			

*** decision about UI ***
- TBD: search on obj nouns and ensure always capitalized (???)
- TBD: how to handle obj.full_name capital cases?
- TBD: Add handle as an attrib of door? Could pull handle to open? door would have open direction
- TBD: investigate enabling init_desc attrib for items in containers (e.g. certificate)
- TBD: instantiate obj in hero inventory

*** known cleesh tech issues ***
- TBD: improve drink verb resevoir_lst error via undrinkable_dict error
	- IDEA: custom error for each non-liquid

*** new content / story ideas ***
- IDEA: Royal Hedgehog valor:
	- IDEA: caprecious and messy sort of valor
	- IDEA: sort that shows up two hours late and three sheets to the wind 
	- IDEA: (but is ready and willing to save the day)
- TBD: tune goblin text
	- TBD: maybe add a faded poster of ancient and unreasonable regulations to the antechamber wall?
- IDEA: maybe the hedgehog should act differently once you get & wear the crown?
- IDEA: at some point, perhaps Burt must knight the loyal hedgehog ?
- IDEA: meet the wizard from Enchanter who is searching for a scroll
- IDEA: puzzle based on 4 weights to weigh 40 lbs math puzzle
- IDEA: After winning game Burt can wander around the castle and see everone turned back to human?
- IDEA: In the Library there is a locked magical book ('The Future and Once King')
	- IDEA: is "still being writtin" according to the dragon librarian
	- IDEA: After winning the game, Burt can come back, find it unlocked, and read it
	- IDEA: (it's the back story for DC I; replaces magic scroll concept)
- IDEA: how to get another ruby: put another nut in hollow and come back 3 turns later (squirrel)

*** extend adventure / puzzle ideas ***
- muster room / main_hall antechamber is north of Gatehouse
	- puzzle TBD
- east of muster room = storage closet (TBD)
	- maybe secret passage from here to kitchens to north?
- west of muster room = passage way to gate and stone bridge over moat w/ path beyond
	- but bridge is shattered and cannot be crossed
	- can see lightening-struck tree leaning against tower to north
- North of muster room = main_hall
	- as soon as player enters main hall, baby roc swoops down and steals random obj and burt flees south
	- player must cary big_rock - roc tries to take - collapses - and flees west to nest
	- player is now free to investigate main hall and se/sw passages (roc no longer steals from burt)
	- CANCEL: baby roc flies from tower to tower west-east-west continuously
- cleared main_hall
	- baby roc now hiding in nest
	- main_hall has caved in so can only explore south half of room
	- 5 more passages (2 east, 2 west, 1 north) from main hall (kitchens mid-east door)
		- kitechens have garlic (for vampire)
		- workshop is maybe mid-west; has hammer (for vampire); sword sharpened here by badger?
	- NOTE: for this to work I'll need to embrace the other 4 cardinal dir
	- CANCLE: north is separately obstructed - player can slip through debris w/ no items?
- south-east of main_hall goes to wizard's tower / astronomy
	- Probably weight / pulley problem to solve here (zorkmid is key item)
	- Wizard himself has been converted into a kindly owl
	- was in love with gardener (now Otter) but can't get to her because window is closed
	- Maybe has key to garden shed, love letters, and something else useful (potion ?)
	- Access to room has useful astronomy-themed tool (telescope ??)
	- can see layout of castle from here including weather vane on top of round room
	- see village as well - cecily maybe? Or pub window at least
	- possibly even see weather vane well enough to see that it locks and how to get there?
- south-west of main_hall goes to catapult_tower
	- stairs to tower have collapsed
	- can get to top and catapult via tree (see tree climbing)
	- baby roc has made it's nest here atop some kind of platform / scafolding
	- if player tries to climb platform, roc appears and thwarts
	- all stolen items go to roc nest
	- roc really just wants to escape - looks towards west window freq; calls for mama
	- can't escape because lightening-struck tree is leaning against west window
- player can climb tree
	- tree = room with no floor
	- if jump => moat and die
	- if drop item => moat and vanish
	- hollow with some mcguffin half way up
	- higher up gives access to 2nd floor of tower, roof
	- from roof can view castle, weather vane, and fire items past cinch pts w/ help of telescope
	- telescope can give angle. Might need potion of parabolic motion knowledge to solve angle and force?
	- possibly even see weather vane well enough to see that it locks and how to get there?
	- player can also go further west on big_branch (hollow height)
	- if player goes west far enough tree will tip over away from tower
	- if player just holds on, they landly softly on the shore across moat and tree crushes them
	- they need to jump from tree when it is half way over, then run south to dodge
	- the tree now acts as a bridge across the moat
	- also, the roc immediately flies out and player can recover items from nest and get new item (?)
	- (what if player chops tree with axe ??? easter egg? )
- game_trail leads south along west bank of moat from tree crash and arrives at far end of stone bridge
	- west from here leads gazebo and sun dial (?)
- north of gazebo = garden
	- otter lives here and pines for owl
	- if palyer frees owl (maybe otter needs to help with this) otter will help player
	- owl flies to garden and otter embraces him => otter helps player / allows to enter shed
	- garden_shed is also here
- in garden_shed 
	- shed key in wizard tower with love letters
	- player finds stakes (for vampire)
- south of gazebo = grave_yard
	- has time-based puzzles
	- Mausoleum with writing that only opens at specific time shown by sundial (?)
	- potion must be made here under full moon
	- tombstone with useful writing of some sort (again, should be time-based puzzle)
- North of main_hall is round_room which spins like Zork II
	- actually, this is where Willy got the idea (since he is the adventurer)
	- he got sick of people constantly bugging him for answers to problems so he installed the round rm
	- spin can only be disabled by getting to round room roof (how?) and locking weather vane
- Beyond round room is whole rest of castle
	- antechamber holds goblin
		- entrance to antechamber (or nearby) should be a cinch point
		- makes it impossible to bring sword
		- Burt will need to balista sword and other neeeded goods to courtyard
	- library with book_dragon
	- courtyard
		- great tree of bright castle (in decay)
		- ducklings in courtyard imprint on burt; turn out to be bathing nymphs?
	- cathedral / oratory holds vampiire

TBD: Introduce multi-room puzzle
- IDEA: trigger in one room, switch in 2nd room, effect in 3rd room

TBD: New Room Update
- IDEA: convert Moat to actual rooms?
	- IDEA: Create on_the_moat room that e, w, d lead to 
	- IDEA: unarmed players get one turn before croc attacks
	- IDEA: no floor to room (items drop down several rooms)

*** new story ideas ***

*** Awesome Words to Use ***
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


*** future big structural improvements ***
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

- IDEA: module triggers [FUTURE]
	- IDEA: Modular Triggers? (named after intent; match cond, result, & mach)
	- IDEA: Establish switch triggers such that timer as trigger is more natural
	- TBD: update cleesh engine version build

- TBD: mod-mach bug ideas [FUTURE]
	- TBD: auto_static_behavior for goblin? each turn - maybe should be a standard function??
		EXAMPLE: "the goblin is eyeing you coldly"
	- TBD: Do we really need to test for goblin in antechamber??? (will the goblin ever move)
	- TBD: should hedgehog_distracted_mach just be replaced by a Creature class attribute?
	- IDEA: Can we create a general purpose Dispenser machine - for use with Crown and Broach?
		- IDEA: would also be useful for control_panel
	- TBD: broaden hedgehog response to interacting with sword (e.g. "pull sword" should trigger)
- TBD: update cleesh engine version build

- TBD: debug ideas: [FUTURE]
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

- TBD: in mk_def_pkl(), sort out more elegant assignment process for self referenced obj [FUTURE]
	- EXAMPLE: re-assigning goblin to goblin_mach after goblin Creature instantiation
	- ANALYSIS: basic problem pattern = obj => obj_mach => obj_cond / obj_result => obj
	- IDEA: pass/link obj to obj_con/obj_result innately (not explicitly) as part of call/assignment?
	- TBD: update cleesh engine version build

- TBD: enable general case of player interaction in-game, from web_main() [e.g. "what is your name?"]
	- IDEA: need to reconsider how to present backstory...
	- IDEA: web_main is framework for all games - "floating scroll" won't work (think of space game)
		- IDEA: ARGH!!!! I just realized I CAN'T do this in gs.end ....
	- IDEA: except for in web_main(), there is no interactive option
		- IDEA: everything is bulk beffered, then presented to player for input back in web_main()
		- IDEA: input is ONLY collected in web_main() which is *HUGE* pain for backstory interaction
		- IDEA: I need to move backsotry interaction back to web_main() and pass is_bkstry with it
		- IDEA: then pull 'read_bkstry_str' and 'backstory' from static_gbl() using game_name & path
		- IDEA: need a function in file_io() to pull descriptions from static_gbl(); re-usable
	- TBD: create player_interact() in /app_main
		- TBD: player_interact() = 3 func: get_player_confirm(), [get_player_int(), get_player_str()]
		- TBD: create is_interact attrib in gs.core (default = False)
		- TBD: in gs.end() set core.is_interact=True, retrn interact_str, interact_type to app_main()

TBD: Refactor app_main() modules
- TBD: refactor remaining app_main chain: pre_action, cmd_exe, post_action, auto_action
- TBD: use __getattr__ and __setattr__ methods to make dict accessible as obj
- TBD: refactor GameState & dicts in static_gbl() with dunder methods ( __getattr__ and __setattr__ )
	- LINK: see: https://stackoverflow.com/questions/10761779/when-to-use-getattr
	- TBD: create dict_class_def.py w/ StaticDict and __getattr___ (and s__setattr__ for future tools)

TBD: Enable Verb Methods for Machines
- IDEA: enable silent run mode for verb methods so that I can use them in result_exe()
- IDEA: start with Item.take() => TakeResult



*** TO REVIEW ***

*** modular machine updates ***
- TBD: make 'disable post run' a standard feature / attrib of modular machines
	- IDEA: attrib => is_run_once

*** refactor Creature ***
- TBD: sort out whole 'fist' / 'sharp_teeth' un-armed attack issue in Creature class
	- Sort out the wierd thing where unarmed attack is represented by first item in feature_lst
- TBD: consider how to surface 'not_attackable' txt in game_static_gbl
	- UPDATE: is_attackable checked in error() - maybe good enough?
- TBD: does creature_state really have any value? Maybe build hedgehog state machine before pulling the plug on this one
- TBD: Could simplify 'give', remove description updates from give, and instead implement them as part of state machine?

- TBD: should it be possible to show() an obj of class Writing or ViewOnly ??
	- TBD: enable 'show writing to creature' is writing is on an item Burt is holding

- TBD: make creature obj data more atomic
	- TBD: create weapon() method to provide adj & adv (vs reading weapon_dict via attack() )
		- IDEA: obj should be a black-box
	- TBD: same idea for 'can't attack error' for attack() in invisible(); should be creature() meth

- IDEA: Distracted state & description as creature attribute; inhibits 'show', 'give', attack 'commands'
	- "The creature too distracted to notice what you are showing them"
	- "You think better of attacking the distracted creature"
- IDEA: Creature state is linked to descript; e.g. hedgehog_descript_1
- IDEA: machine result changes Creature State; State machine itself changes creature attributes based on state
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

- TBD: figure out 'behind' prep for case of control panel in alcove behind goblin

- non-humanoid monster could be a special weapon description case (fun new puzzle idea)???
- DONE: Consider having size values for items and capaicty limits on containers & backpack (should the crystal box really hold an axe?)
	- This becomes important for 'take' capacity as well in shrinking puzzle (??)
	- encumberance (post Burt as object?)
	- implement carying capacity / container cappacity; Also carry restriction passages, etc..
- DONE: make goblin hand contents examinable (e.g. Grimy Axe)




*** ARCHITECTURE ***
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


*** Introduce Interupts ***
- triggered by time value
- commands run independently of player choices (e.g. day turns to night, moon comes out, etc.)


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


*** DC2 PUZZLE IDEAS ***
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
