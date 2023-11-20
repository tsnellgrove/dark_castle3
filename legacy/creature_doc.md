Dark Castle v3
Creature Documenation
Mar 24, 2022


*** CREATURE IDEAS ***


*** Creature Method Philosopy ***

* Over-Arching Approach *
I'm thinking through two different approaches to creatures. In one approach - I'll call it the "primatives" approach - I declare that each creature has wants and fears (e.g. the hedgehog wants the biscuits, the goblin fears the shiny sword). Under the primatives approach the creatures have innate personalities and the role of creature methods like 'show', 'give', and 'attack' are just to expose those personalities. This is attractive in that it makes the creatures more real and gives general guidance for their future behaviors. However, I'm not sure it's realistic. Dark Castle is not a life simulator... there is no ecosystem or food chain (I mean really, the castle has been abandoned for generations - what have they all been eating??). And the creature's wants and fears are quite idiosyncratic... the goblin is an autocrat who wants to prevent passage to the throne room or any rejuvination of the castle... the hedgehog, along with loving biscuits, is the keeper of Bright Castle's spirit and wants to see it restored. These are not easy desires to model in a simple python object!

The other approach I'm considering - I'll call it the "mechanical" approach - is that a creature is wholy defined by its methods. There is no attempt to track and expose a creature's inner desires - their actions are their all - like early impressionism, their surface is their whole. I find this a little unsatisfying - but I also think it's much more implementable. So at least for version 3.x this is the approach I'll take. Perhaps in version 4.x I'll find away to capture the hedgehog's inner yearnings in code ;-D

So, based on the mechanical approach, creatures have three standard interaction methods:

- 'Show' is meant to be informational in nature. The Player will learn something about the Creature - what it desires and fears - based on its response to the item shown. Therefore the show() method provides only a text response. It is possible that showing an item to a Creature could provoke an action response (e.g. running away) but this is outside the standard use case and should be implemented via a Modular Machine. Ideally, show() would take creature_state into account.

- 'Give' is meant to enable barter and trade. If the Player gives an item to a Creature - particularly if that creature has shown interest in the item via show() - then the player can reasonably hope for some other useful item in return. Therefore the give() method provides a text response, removes an item from Burt's hand, and places a new item in Burt's hand. It's possible that give() could trigger a more advanced sequence of actions from a Creature but this is outside the scope of the method and should be implemented via a Modular Machine. Because give() can fulfill a creature's needs it also has the power to change the creature's mood and therefore update their description.

- The 'Attack' method is a bit more complex and is intended to enable combat between Burt and creatures. The intent in Dark Castle is for combat to be a purely logical exercise... so if you attack a Creature with the correct weapon you will always win. Burt's "weapon" is whatever he is holding in his hand. If Burt's hand is empty he attacks with his Fist. For a given Creature and burt_weapon, attack() generates a result_code - which has options like 'creature_flee', 'creature_death', and 'burt_death' - and a response_key - which is the static_dict[] key to the attack's description. As, with the other Creature methods, it's easy to imagine attack() provoking a more complex response than these outcomes - but those are outside the scope of the method and should be implemented via a Modular Machine.

- 'attack_burt' is an awkward 'hidden' verb that enables a creature to proactively attack Burt. Among other things, this work-around highlights that Burt should really be an object himself - rather than an amorphous set of attributes distributed across game state. But this will not be a minor undertaking - so for now, we have the attack_burt() method - which enables 'attack' to remain a 2word command without requiring a 'burt' object to exist. Code-wise, 'attack_burt' is identical to 'attack' with some minor text differences ("You charge..." vs. "You attempt to parry..."). In general, the idea is that when Burt is being attacked he is on the defensive and likely needs the right weapon just to parry.

*** Creature Class Attributes ***

- Class:
	- inherits from ViewOnly
	- inherited attributes: name, full_name, root_name, descript_key, writing

- Unique Attributes v2:
	- creature_state
		for Goblin = None
	- mach_obj_lst
		for Goblin: 
			1) attack if player interacts with room obj
			2) watch player with malicious glare each turn in room (???)
		For Hedgehog: 
			1) attack_warning?
	- show_item_dict # {{item : 'response_key'}}
		- for Goblin: scared of sword
	- give_item_dict
		{{item : {'response_key' : response_key, 'accept_item' : accept_item, 'give_item' : give_item, 'new_descript_key' : new_descript_key}}
		- for Goblin: scared of sword
	- attack_creature_dict
		{burt_weapon : result_code, result_text_key}
		(will need to implement default weapon code)
	- attack_burt_dict
		{burt_weapon : result_code, result_text_key}
		for when the golin attacks burt for wandering into the north side of the room
	- creature_items_lst
		for Goblin: Note and Axe for Goblin
		Key for Hedgehog
	- dead_creature_obj
		
- Methods:
	- Show (default response = "the <creature> is not interested in the <item>")
	- Give (default response = "the <creature> is not interested in the <item>")
	- Attack (default response = 'dodge')


