# Cleesh / Dark Castle — Architecture Discussion Transcript

*A conversation on reviewing the Cleesh engine against Infocom and TADS, and designing the grammar-as-data, class-collapse, and JSON-state refactors. July 2026.*

---

## Human

> I am designing an Interactive Fiction engine and game. Please familiarize yourself with the Infocom game engine (link: https://eblong.com/infocom/other/Internal_Secrets_Ko_2019.pdf ) and the TADS game engine (link: https://www.tads.org/t3doc/doc/t3QuickStart.htm ) and then review my own code in the documents/python/dark_castle3 repo. What are the pros and cons of my class-based, obj-oriented approach? What advice do you have on key updates or changes I should make?

---

## Assistant

*(After reading the Infocom internals PDF, the TADS 3 quick start, and the engine: the turn pipeline, class tree, machine system, and the cup_of_tea authoring files.)*

### Cleesh vs. Infocom vs. TADS: Architecture Review

**TLDR:** Your class-based approach is fundamentally sound — you've independently reinvented several of the classic IF architecture patterns (TADS's verify/check/action phases, Infocom's daemon/interrupt system, object-owned verb behavior). The two structural weaknesses are the opposite of what you might expect: it's not the object model, it's (1) the parser, where grammar is hard-coded into engine logic instead of being data, and (2) the combinatorial mixin class explosion (`ContainerFixedSimpleSwitchMach`). I'd also flag two hygiene issues that will bite the web deployment: state mutation inside the interpreter, and pickle-as-save-format.

For grounding: I extracted and read Ko's *Internal Secrets of Infocom Games* (the ZIL/Z-machine internals — object table, syntax entries, PARSER → SYNTAX-CHECK → PERFORM → CLOCKER pipeline) and the TADS 3 quick start, then read your engine: the turn pipeline (`app_main.py`, `interp.py`, `validate.py`, `cmd_exe.py`), the class tree (Invisible → Identity → Error → Writing → ViewOnly → Item/Container/Creature + mixins), the machine system (`mach_class_def.py`), and the cup_of_tea authoring files.

#### Where you converged with the classics (the pros)

**1. Verb methods living on noun objects is the right call.** `getattr(do_noun_obj, action_str)(gs)` in `cmd_exe.py:87` is essentially the TADS model: objects own their behavior, and subclasses override it. Infocom got the same effect procedurally — PERFORM offers each command to a chain of handlers (room first, then indirect object, then direct object, then the generic verb routine as fallback). Your default verb responses on the `Error` base class play exactly the role of Infocom's generic verb action routines: the fallback when no specialized object claims the action. This is genuinely good OO design for IF, and it's the part of your architecture I'd change least.

**2. Your `*_err` validation phase is TADS's verify/check, reinvented.** TADS splits every action into verify (is this action even sensible? — fails silently, no turn) / check (sensible but blocked — fails with a message, may consume a turn) / action (do it). Your `take_err()` returning `(cmd_err, is_att, err_txt)` in `error_class_def.py:127` draws exactly the same distinction: the `is_att` "attemptable error" (too heavy, belongs to the goblin) consumes a turn and still runs machines, while a nonsense command doesn't. Most homebrew IF engines never discover this distinction and their NPCs freeze whenever the player fumbles. Keep this.

**3. The machine system is a solid daemon/fuse/event architecture.** Your Timers are Infocom's interrupts (CLOCKER ticks them each turn), Warnings are counted fuses, and the trigger/condition/result machines are declarative demons. Two details particularly impressed me: `is_valid_reqd` mirrors Infocom's demon-vs-interrupt split (demons run even when the parse fails), and `cmd_override` from `pre_action` machines is Infocom's M-HANDLED — a room-anchored machine gets first crack at a command and can swallow it, which is exactly PERFORM's handler-precedence order. The cond/result composition in `AutoMachMixIn.run_mach()` (lists of conditions ANDed, lists of results sequenced) is more declarative than what most ZIL games did — they wrote imperative routines. Your approach is more like modern data-driven engines, and it feeds your future game-editor vision nicely.

**4. Engine/game separation with a proof point.** Two games sharing the engine, game content in `game_static_gbl.py` / `game_update.py`, an IO buffering layer that already abstracts away the terminal (which is why `web_main.py` works), and a scenario-based regression test harness. Infocom's whole business model was this separation (one interpreter, many story files); you're on the same road.

**5. The `is_*()` identity method pattern.** `identity_class_def.py` — every predicate defaults to `False` on the base class and gets overridden. This is Infocom's attribute flags (TAKEBIT, FLAMEBIT) done politely, and it lets you iterate heterogeneous object lists without `isinstance` checks. Fine choice.

#### The cons

**1. Grammar is entangled with engine code — your biggest architectural debt.** Infocom's key insight (the "biggest mystery" chapter of that PDF) is that syntax entries are *data*: 8-byte records mapping verb + preposition patterns to actions, stored in the story file, separate from the parsing machinery. TADS likewise: grammar lives in declarative `VerbRule` definitions. In Cleesh, adding a verb means editing engine source in at least four places: `syntax_dict` inside `syntax()` (`interp.py:37`), `action_verb_lst`/`syn_verb_lst` (`interp.py:412`), the special-case ladders in `asym_syn()` and `infer_do_noun()`, plus the io word lists. A game can't add a verb without forking the engine — which breaks your own engine/game boundary, and directly conflicts with your rule about not over-customizing shared code. The `prep_verb_lst` block at `interp.py:665` shows the cost: attack/lock/drink each carry bespoke inline logic that Infocom would have expressed as one syntax entry with a GWIM bit ("find me a held weapon") and a LOC byte ("must be HELD").

**2. Combinatorial class explosion.** `WeaponAutoMach`, `ItemTrigMach`, `InvisSwitchMach`, `ContainerFixedSimpleSwitchMach` — every capability pairing needs a hand-written concrete class whose `__init__` threads a dozen positional args to multiple parents (`mach_class_def.py:308` takes **seventeen** positional parameters). TADS has the same mixin idea but the compiler composes classes at object-declaration time, so authors never write the glue. In Python, growth here is quadratic: N capabilities × M base classes. This is the thing that will make the engine feel heavy as Dark Castle grows.

**3. The interpreter mutates game state before validation.** In `interp.py:684-696`, parsing `attack goblin` *draws the weapon* — `remove_item()`/`put_in_hand()` execute inside the interpreter, before `validate()` has decided whether the command is even legal, and the same pattern moves items out of the backpack/worn list at lines 724-741. If validation then fails, inventory has still changed. Infocom is strict about this (parse → checks → PERFORM), and TADS runs implicit actions ("first taking the key") through the *full* action pipeline as real announced actions. The irony is you already own the right mechanism: `ClimbableMixIn.climb()` does `gs.io.insert_cmd_queue(f"go {dir}", 0)` — implicit actions as queued commands. That's the correct pattern; the interpreter's direct mutations are the aberration.

**4. Pickle as both save format and world format — fix before the web.** You already know the fragility (your own note: any shared-class attribute change forces rebuilding both games' pickles). The deeper issue: Infocom saves don't store the world — they diff the *writable memory* against the story file. Static data (descriptions, syntax, code) is never in a save. Your equivalent would be: on save, walk `master_obj_lst` and serialize only mutable state (`{obj_name: {mutable attrs}}`); on load, rebuild the pristine world from `game_update.py` and apply the state. That makes saves survive class refactors, shrinks them, and — critical for the web — removes `pickle.load()` on data a browser touched, which is an arbitrary-code-execution vector.

**5. Bare `except:` blocks swallow authoring bugs.** `interp.py:171`, `validate.py:50`, `cmd_exe.py:110`, and the `buff_f` try/except fallbacks in the machines. A typo'd descript key or a missing `_err` method degrades into a generic message or a debug-buffer note instead of failing loudly. You've clearly been bitten already — validate's except message literally guesses "Did you possibly forget to add the noun obj to the pickle?" Catch `KeyError`/`AttributeError` specifically, and in debug mode re-raise.

**6. The hero is hardcoded into verb methods.** Nearly every verb does `creature = gs.core.hero`. Infocom's WINNER variable exists precisely so `TELL GOBLIN, OPEN DOOR` can run the same action code with a different actor. Some of your methods (like `climb`) already accept a `creature` param — most ignore it. Purely optional if Burt is forever the only actor, but it's cheap to thread through now and expensive later.

**7. Smaller parser gaps** (noting, not urgent): no pronoun support ("take key. examine **it**") — Infocom's THIS-IS-IT is a very small amount of state for a big playability win; no orphaning (Infocom asks "What do you want to take?" and accepts the bare answer "the key" via ORPHAN-MERGE — your inference is good but when it fails the player must retype everything); "take all" is string-prefix special-casing in `app_main` rather than grammar; noun phrases are capped at adjective+noun.

#### What I'd actually do, in order

1. **Extract grammar to data.** Move `syntax_dict`, verb lists, and synonym maps into a declarative structure the engine loads — engine defaults plus a per-game extension dict. This is your syntax-entry table. It unblocks per-game verbs, shrinks `interpreter()` dramatically, and is a prerequisite for the game editor you're planning.
2. **Kill the class explosion with keyword args, then composition.** Step one is mechanical: make constructors keyword-only with defaults, so `game_update.py` reads as self-documenting named fields (you're already writing `# name`-style comments to compensate — that's the signal). Step two: fold the mach combos into a `mach` component attached to a host object rather than inherited, so any object can carry machine behavior without a new class.
3. **Make the interpreter pure.** All implicit actions (draw weapon, remove-worn-first, take-before-lock) become `insert_cmd_queue()` entries. The interpreter's contract becomes: string in, `(case, action_lst)` out, zero state changes.
4. **Split save state from world definition** before serious web work, per #4 above.
5. **Tighten exception discipline** — specific exceptions, re-raise in debug, and a startup lint that cross-checks every `descript_key`/machine message key against `game_static_dict` (that one check would have caught a whole category of your historical bugs).
6. Then, as playability polish: pronouns ("it"), and letting a failed noun-inference ask a question the player can answer with just the noun.

The honest bottom line: for a self-taught project, converging independently on verify/check phases, daemon scheduling, and object-dispatched actions is impressive — those took Infocom and Mike Roberts years to settle. Your object model needed the least help of anything I looked at. The advice above is mostly about pulling *content* (grammar, world state) out of *code*, which is precisely the transition Infocom made when they invented the story file.

---

## Human

> Looking at your recommendations: 3 is underway (already in place for many verbs using hand_manage.py; 5 I agree with... it's on the list but probably a ways out; 6 I've thought about but I was honestly never wowed by Infocom's pronoun support... half the time it didn't really work for me... so that one is a maybe. 1, 2, and 4 are interesting to me. Let's talk about 1 to begin with. I am planning to extract syntax() and the verb lists into separate modules (see static_gbl.py). But I think you are proposing a more significant separation? Please help me understand?

---

## Assistant

Yes — what you're planning (relocating `syntax_dict` and the verb lists into a `static_gbl`-style data module) is a good organizational step, but it's not the separation I was proposing. The difference is between *moving* the grammar and *changing what the grammar is*. Let me try to make the distinction concrete.

### The test that shows the difference

Here's the question that defines the boundary: **could `cup_of_tea` add a `brew` verb without editing any file under `cleesh/` outside its own game directory?**

After your planned move, the answer is still no. The dict would live in a data module, but the interpreter would still contain verb-specific *logic* that the dict doesn't capture. Relocation changes the address of the coupling, not the coupling.

### Where the knowledge about one verb lives today

Take `attack` as the worst case. Its behavior is currently distributed across at least seven places:

1. `known_verb_lst`, `prep_verb_lst`, `var_outcome_verb_lst` in `static_gbl.py` — three parallel lists that must be kept in sync by hand
2. `verb_syn_dict` (hit, kill, poke, clobber...)
3. The `elif word1 in ['attack']:` branch in `interp.py:681` — the draw-a-weapon-if-unarmed logic, the `prep = 'with'` assumption, the fall-back-to-fist logic
4. The take-from-backpack/worn logic further down that same function
5. `attack_err()` on the class side
6. The `attack()` method itself on Creature
7. `score_dict` in the game file

When you move `syntax_dict` into a data module, items 3 and 4 — the interesting parts — stay behind in engine code, because your current `syntax_dict` can't express them. That's the real problem: **the dict's schema is too weak to hold what the interpreter knows.** The special-case code exists precisely because the data can't say it.

### What Infocom's syntax entries teach

Look again at that 8-byte syntax entry from the PDF, because every byte is a lesson:

```
[01 f0 11 00 64 00 39]  "take OBJ from OBJ"
     │  │     │      └─ action to dispatch
     │  │     └─ LOC byte: object must be CARRIED or ON-GROUND
     │  └─ GWIM bit: if object missing, auto-find one with attribute #17
     └─ required preposition
```

The things you handle with bespoke code paths are *columns in their table*:

- Your `hand_mgmt()` moving items from backpack to hand before `drop`? That's the **TAKE bit** — a flag in the row saying "implicitly acquire the object first."
- Your attack-draws-a-weapon logic in `interp.py`? That's the **GWIM bit** — "if the indirect object is missing, search scope for an object with the WEAPON attribute and announce the assumption."
- Your `infer_do_noun()` special cases (`sit` → find the one seat, `doff` → the one worn item)? Also GWIM, per verb pattern.
- Your scattered `assumed_noun_2word_lst` / `prep_verb_lst` / `one_word_convert_lst`? All **derivable** from the patterns themselves — a verb whose only pattern is `V + DO + with + IDO` *is* a prep verb; you shouldn't have to also register it in a list.

Infocom never wrote "if verb is attack, draw weapon." They wrote one generic parser that reads constraint columns, and `attack`'s row set the right bits.

### What this looks like for Cleesh

The proposal is one record per verb that fully describes its surface behavior, something like:

```python
verb_defs = {
    'drop': {
        'patterns'   : [('DO',)],                 # drop <obj>
        'synonyms'   : ['release'],
        'dispatch'   : 'verb_do',
        'do_require' : 'in_hand',                 # replaces hand_mgmt special case
        'infer_do'   : 'hand_item',               # replaces infer_do_noun branch
    },
    'attack': {
        'patterns'   : [('DO', 'with', 'IDO'), ('DO',)],
        'synonyms'   : ['hit', 'kill', 'poke', 'clobber', 'jab'],
        'dispatch'   : 'prep',
        'ido_require': 'in_hand',
        'infer_ido'  : 'held_weapon_else_feature',  # the GWIM rule, named
    },
    'sit': {
        'patterns'   : [('DO',), ('on', 'DO'), ('in', 'DO'), ()],
        'dispatch'   : 'verb_do',
        'infer_do'   : 'unique:is_seat',            # "the one seat in scope"
    },
}
```

Then the engine changes character: `interpreter()`, `infer_do_noun()`, `hand_mgmt()`, and the prep-verb block stop being ladders of `if word1 in ['attack']` and become **generic loops that read the record**. The inference vocabulary (`hand_item`, `unique:is_seat`, `held_weapon_else_feature`) is a small fixed set of engine-implemented strategies — you'd need maybe six to cover everything you do today.

Two important boundaries on this, so it doesn't sound like "turn everything into data":

- **Verb *methods* stay exactly where they are.** `Item.take()`, `Creature.attack()`, the `*_err` validation methods — those are behavior, and objects owning behavior is the part of your architecture I said to keep. The table only describes *surface syntax, inference, and dispatch shape* — the parser's knowledge, not the world's.
- **The strategies stay code.** The table says `'infer_do': 'unique:is_seat'`; the engine implements what "unique" means. Data names the policy, code implements the mechanism.

### The second half: the merge point

The other piece — and this is what makes it "engine architecture" rather than "tidying" — is that the engine should load its default `verb_defs` and then **merge the game's extensions over it**, the same way `gs.io.get_lst(key, 'eng')` already falls through between game and engine dictionaries. So `cup_of_tea/game_file/game_verb_defs.py` could contain:

```python
game_verb_defs = {
    'brew': {
        'patterns' : [('DO',)],
        'synonyms' : ['steep'],
        'dispatch' : 'verb_do',
    },
}
```

...plus a `Kettle` class with a `brew()` method and `brew_err()` in the game's own class file — and the engine never changes. That's the "significant separation": the grammar gets an extension point, not just a new filename. It's exactly the Infocom split — one interpreter (ZIP), many story files each carrying their own syntax entries — and it's why the same interpreter binary could run Zork and Deadline.

### Why this ordering of work pays off

Three downstream effects worth naming:

1. **The parallel lists disappear.** `prep_verb_lst`, `assumed_noun_2word_lst`, `one_word_convert_lst`, `action_verb_lst` become computed properties of `verb_defs` at load time. Every one of those lists is currently a sync bug waiting to happen — a verb added to `syntax_dict` but forgotten in `known_verb_lst` fails silently.
2. **It absorbs your #3 work rather than competing with it.** `hand_mgmt.py`'s hardcoded `['wear', 'drop', 'eat']` and `['drop', 'eat', 'stow']` lists become `do_require: 'in_hand'` flags — the mechanism you built stays, its trigger list moves into the verb record.
3. **It's the foundation for the game editor.** A web editor can emit rows in a table; it cannot emit `elif word1 in ['attack']:` branches in `interp.py`. If the editor vision is real, the grammar has to become data eventually — the only question is whether it happens before or after you've written more special cases.

The honest cost: the migration itself is the hard part, because you have to *discover* the schema by excavating what all those special cases actually do, and a few (the `climb` direction handling, `put`'s in-vs-on preposition matching against the container's `prep` attribute) will resist tidy columns and need either a richer pattern syntax or a documented escape hatch (e.g., a per-verb `custom_proc` hook naming an engine function). I'd expect the schema to go through two or three revisions as you migrate verbs one at a time — which your scenario test harness is well suited to guard.

If this framing lands, a good next step whenever you're ready would be to draft the schema together against your five or six gnarliest verbs (`attack`, `put`, `climb`, `sit`, `exit`) *before* migrating anything — if the schema can express those, the other twenty verbs are easy.

---

## Human

> This is very interesting. As you can maybe tell, I'm in the middle of overhauling interpreter(). At this points I've just finished revamping all the verb_do and verb_prep_do verbs. I'll tackle the one_word and help cases next and then the 'prep' verbs - which as, you point out, are the most muddled at present. I think my first goal is to complete the overhaul. But then I want to come back and take another pass at interpreter() using the grammar-as-data approach you describe. I do want to make games writeable without as much effort as ZIL and TADS demand... but I also want to support customization for those who want to create novel capabilities. One more request on this front - can you please review the dark_castle game - it is much more developed than cup_of_tea - and then review your grammar advice and let me know if seeing dark_castle changes your approach at all?

---

## Assistant

*(After reading dark_castle's `game_update.py` and `game_static_gbl.py`.)*

### Does dark_castle change the grammar advice?

The core proposal survives intact, but dark_castle exposes something I underweighted: **the parser's *output* format is load-bearing game content, and it needs to be stabilized before — or during — your current overhaul, not in the later grammar-as-data pass.**

#### The big new finding: `trig_vals_lst` is coupled to interpreter internals

Your machine triggers match against raw `word_lst` shapes:

```python
goblin_attack_mach = InvisTrigMach(..., [['examine', 'iron_portcullis'], ...
    ['take', 'grimy_axe'], ['open', 'iron_portcullis'], ['go', 'north', 'antechamber'], ...
```

And the file itself records the cost of that coupling. `game_update.py:334` and `:344` show commented-out *old* trigger shapes — `['go', 'east']` became `['go', 'east', 'entrance']` when you merged dir/prep into cmd_lst — meaning your interpreter overhaul forced hand-edits to game content in both games. And you knew it was fragile when you wrote it: the comment at `game_update.py:315` — *"prep case word_lst => trig_vals_lst is erratic. see interp() ln 201, validate() ln 32, & mach_class() ln 72"* — is three files coordinating on an undocumented tuple shape.

It's actually worse than the trig lists alone, because there are **three consumers** of the parsed-command vocabulary: machine triggers, `TrigMixIn.trig_check()`'s case-by-case unpacking, and `score_dict` keys like `('shiny_sword', None)` / `('royal_hedgehog', 'shiny_sword')`. Each has its own slightly different encoding of "a command happened."

So the refinement to my advice: **the first deliverable of grammar-as-data isn't the verb table — it's the normalized command record.** Something as simple as:

```python
Command(verb='give', do_noun=baked_biscuit, prep='to', id_noun=royal_hedgehog, dir=None)
```

with *one* documented matching rule for patterns and wildcards. `cmd_exe`, `validate`, `trig_check`, and `score.disp_score` all consume it; `case`/`word_lst` disappears as a cross-file contract. This matters *right now* because you're mid-overhaul: every `word_lst` shape change you make while revamping the prep verbs will break dark_castle triggers again unless the machines match against a stable schema instead of the interpreter's working format. Infocom parallel: PRSA/PRSO/PRSI were *the* fixed interface — thirty-odd games and fifteen years of parser rewrites never changed what PERFORM consumed. That stability is what let them rewrite PARSER freely.

The pleasant side effect: your wildcard support (`['give', '*', 'royal_hedgehog']`) currently only works for two hardcoded cases in `trig_check`. Against a normalized Command, wildcard matching becomes one generic field-by-field comparison, and things like `['*', '*', 'royal_hedgehog']` ("any command targeting the hedgehog") fall out for free.

#### Two things dark_castle *confirms*

**1. Your customization worry is already solved — by the layer you built, not the parser.** I looked at where dark_castle's novel behavior actually lives: the hedgehog's barter table (`{shiny_sword: {'accept': True, 'give': silver_key}}`), the attack-outcome wildcards (`'shiny_sword_burt_*': 'tgt_death'`), the lever-array puzzle, the sword-glow state machine. **None of it is in the parser.** Every novel capability is expressed as class data + machines reacting to *standard* verbs. That's exactly the Infocom finding — Zork and Deadline share one parser; the games differ in objects and demons. So the grammar table can stay lean: verb registration, surface patterns, inference policy, dispatch target. Game authors who want novel capabilities add classes and machines (your existing extension model); they only touch the grammar table to add a verb *word*. The two goals you named — low-effort authoring *and* deep customization — sit on opposite sides of that boundary, and dark_castle proves the boundary holds.

**2. You already think in pattern-matching data languages.** `trig_vals_lst` wildcards, `attack_dict` patterns like `'weapon_burt_*'`, `score_dict` tuples — you've independently invented three little matching DSLs. The grammar table is a fourth instance of a thing you're demonstrably comfortable with. The refinement is to *unify* their vocabulary (they should all describe commands the same way) rather than invent a fifth dialect.

#### Two adjustments to the original proposal

**Keep `go` special.** Dark_castle's map shows why: pseudo-doors (`'climb'`, `'leap down to the moat'`), two-faced doors (`{gatehouse: foreboding_archway, antechamber: lit_archway}`), `'unreachable'` sentinels. Direction handling is entangled with the world model, not just syntax. Infocom special-cased GO in MAIN-LOOP for the same reason. Don't force it into the generic table — one honest special case beats a schema contorted to absorb it.

**A name-resolution pass would pay for itself.** Not strictly grammar, but dark_castle makes it loud: you pass `'royal_hedgehog_temp'` / `'burt_temp'` placeholder strings into constructors, then patch ~60 lines of real references at `game_update.py:616-680` because conditions are declared before the objects they mention. If conditions/results/machines accepted plain *names* everywhere and a single build-time resolver swapped names for objects after everything is instantiated, the `_temp` convention and the entire reassignment block disappear — and "names as the universal currency in data, resolved at load" is exactly the convention the grammar table, the Command schema, *and* your future web editor all want. It also softens the pickle problem (#4), since name-keyed data serializes trivially.

#### Sequencing, given where you are

Your instinct — finish the overhaul first, grammar pass second — is right, with one amendment: **define the Command record now, as part of the overhaul, not after it.** You're about to rework the prep verbs, which are precisely the case where `word_lst` is "erratic." If the overhauled interpreter emits a normalized Command and `trig_check` matches against it, you fix the muddled prep handling and stop the game-content churn in one motion — and the later grammar-as-data pass becomes a pure input-side refactor that can't break either game's machines. The verb table, the merge point, and the name resolver can all come later at leisure; the Command schema is the piece with a deadline, because it's the piece your current work keeps bumping into.

---

## Human

> For the Command Record... my current intent is to have a few different "shape" commands (e.g. verb_do, verb_prep_do, verb_do_prep_id) with the shape identified as the last string in the action list. I eventually intend to eliminated 'case' (I'm currently consolidating all case types under 'universal'). Does this approach match your recommendation?

---

## Assistant

Halfway. The two moves you're already making — consolidating everything under one case, and making the shape explicit instead of implied — are the right direction. But the shape-tag-in-a-list design stops short of what I'm recommending, and the difference shows up exactly in the three consumers we discussed. Let me draw the line precisely.

### What the shape tag doesn't fix

With `['drop', obj, 'verb_do']` vs `['go', 'north', room, 'verb_prep_do']` vs `['give', obj, 'to', obj2, 'verb_do_prep_id']`, the *discriminator* is now explicit (good), but the *layout* is still positional and shape-dependent. Every consumer still has to know that position 1 means the do_noun in one shape and the prep in another. So `cmd_exe`, `validate`, and `trig_check` keep their per-shape unpacking branches — you've renamed the cases, not eliminated them. Today's `trig_check` is the cautionary tale:

```python
elif case == 'prep':
    trig_key_lst = [word_lst[1], word_lst[2].name, word_lst[0].name]
```

That reordering (`mach_class_def.py:96`) exists *because* the layout is positional — and it's why game authors writing `trig_vals_lst` have to memorize a different element order per shape, which is what your own "erratic" comment complains about. A shape tag makes the branch prettier; it doesn't remove the branch.

### The recommendation: fixed named fields, shapes become *derived*

One record, same slots every time, unused slots are `None`:

```python
@dataclass
class Command:
    verb: str                    # canonical, post-synonym
    do_noun: object = None       # the direct object (a game obj)
    prep: str = None             # 'to', 'with', 'in'...
    id_noun: object = None       # the indirect object
    dir: str = None              # 'north', 'up'... (go/climb only)
```

`drop sword` → `Command('drop', do_noun=sword)`. `give biscuit to hedgehog` → `Command('give', do_noun=biscuit, prep='to', id_noun=hedgehog)`. The shape is no longer a tag anyone maintains — it's *derivable* from which fields are populated, on the rare occasion anything needs it. Consumers stop unpacking and start naming:

```python
# trig_check, entire replacement for the case ladder:
def matches(trig, cmd):
    return all(getattr(cmd, k) == v or v == '*' for k, v in trig.items())
```

And machine triggers in `game_update.py` become order-free and self-documenting:

```python
[{'verb': 'give', 'id_noun': 'royal_hedgehog'}]        # any gift to the hedgehog
[{'verb': 'go', 'dir': 'east'}]                        # no more ['go','east','entrance'] churn
```

An omitted key is automatically a wildcard — more expressive than positional `'*'`, and immune to the interpreter overhauls you're doing right now, because nothing positional exists to shift.

### Where the shapes actually go: into the verb table

Your shapes encode one real fact — **how to dispatch**: `verb_do` calls `do_noun.drop(gs)`, `verb_prep_do` calls `room.go(dir, gs)`, and your prep case calls `id_noun.give(do_noun, gs)` — note that last one dispatches on the *indirect* object (the hedgehog receives, so hedgehog owns `give()`). That's genuinely necessary knowledge, but it's knowledge *about the verb*, not about this particular command. Which is exactly the grammar-as-data claim: the dispatch recipe belongs in the verb's row —

```python
'drop': {'call': 'do_noun.drop(gs)'},          # however you encode it
'go'  : {'call': 'room.go(dir, gs)'},
'give': {'call': 'id_noun.give(do_noun, gs)'}, # dispatch receiver = id_noun
```

— so `cmd_exe` shrinks to: look up verb, call as specified. Put the shape tag on the Command and you'll forever carry both the tag *and* the per-tag branches; put it in the verb definition and the Command record stays pure content.

### Practical path

Your current tagged lists are a fine *transitional* representation — I wouldn't undo work. But I'd set the end-state now: as you rework the remaining prep verbs, have `interpreter()` build the named record internally and derive the tagged list from it at the boundary, then flip consumers over one at a time (`trig_check` first — it's the one bleeding into game content). One test for when you're done: a game author writing a machine trigger or reading `score_dict` should never need to know what order the interpreter emits words in. If that's true, you've built what I was recommending; the shape tags will have quietly become an implementation detail of dispatch, which is where they belong.

---

## Human

> That's a lot to think about but it makes sense. I'll start folding that into my interpreter() update. Now let's talk about recommendation 2, addressing the class explosion. I've been worried about this myself. I've been planning to eliminate mach as a mixin and just attach machines to objects (most already are). But I don't understand the rest of your advice about using key words to reduce the geometric class expansion. How?

---

## Assistant

Good question to push on, because I bundled two different fixes under recommendation 2 and they solve two different halves of the problem. Let me separate them and then show the mechanics, because your machine-attachment plan is one half, and the keyword-arg move is the other.

### The insight: your class explosion is mostly *capability presence*, not *behavior difference*

Look at the interactive family as a matrix:

```
ContainerFixedSimple      ContainerPortableSimple
ContainerFixedLidded      ContainerPortableLidded
ContainerFixedLockable    ContainerPortableLockable
DoorSimple                DoorLockable
```

Ask what actually *differs* between `ContainerFixedSimple` and `ContainerFixedLockable`. Not how any verb behaves — `open()` on a lockable box does the same thing once it's unlocked. What differs is **which capabilities exist**: does it have a lid? a lock? a weight (i.e., can it be carried)? Each subclass is really just a statement of *presence*: "this one has the lock attributes."

Presence is data, not type. That's the whole trick. A capability becomes a cluster of keyword args that default to "absent":

```python
class Container(ViewOnly):
    def __init__(self, name, full_name, root_name, descript_key, *,
                 writing=None,
                 contain_lst=(), max_weight=999, max_obj=999, prep='in',
                 weight=None,        # None => fixed; a number => portable
                 is_open=None,       # None => no lid; True/False => lidded
                 is_locked=None,     # None => not lockable
                 key=None):
```

And your identity methods — the ones the whole engine already dispatches on — stop being subclass overrides and become one-line attribute reads *on this single class*:

```python
def is_item(self):      return self._weight is not None
def is_openable(self):  return self._is_open is not None
def is_lockable(self):  return self._is_locked is not None
```

Nothing downstream changes. `take_err()` already asks `self.is_item()` and produces the "just how do you intend to pick that up?" response; `open_err()` already gates on `is_openable()`. Your error architecture was *built* for capability-absence responses — it just currently learns about absence from the class tree instead of from attributes. Six container classes plus two door classes collapse into `Container` and `Door`, and the matrix can never explode again because a new capability is a new kwarg, not a new row of subclasses.

This is, incidentally, exactly Infocom's design: there is no `LockableContainer` class anywhere in ZIL — there's an object with CONTBIT and LOCKEDBIT set and a `key` property. Attributes as capability flags, one generic engine reading them. You'd be arriving at the same place with nicer syntax.

### The rule for what stays a class

Don't swing to the other extreme (TADS 3's `Thing` is a notorious god-class with dozens of tunable properties, and it's the hardest part of TADS to learn). The dividing line:

- **Same verbs, different capabilities present → keyword args.** Lidded/lockable/portable/has-writing.
- **A verb genuinely behaves differently → subclass.** `Door` (participates in the map), `Seat` (contains a *creature*, has `in_reach_lst`), `Creature`, `Room`, `Food` (`eat()` destroys it) — these earn their classes because they *do* different things, not merely *have* different things.

Your machine family is a clean test of the rule. `InvisAutoMach`, `InvisTrigMach`, and `InvisSwitchMach` share `run_mach()` entirely — they differ only in whether `trig_vals_lst` and `trig_switch` are present. Kwargs:

```python
Machine(name, ..., cond_lst=..., result_lst=...,
        trig_vals_lst=None,   # None => auto-runs every turn
        trig_switch=None)     # set => switch-triggered
```

Three classes become one. But `Timer` and `Warning` *override* `run_mach()` with different logic — behavior difference — so they stay classes. The rule sorts your whole zoo mechanically.

### How this meshes with your machine-attachment plan

Your plan (machines attached to objects rather than mixed in) kills the *other* axis of the explosion — the host × machine cross-products. `ItemTrigMach`, `WeaponAutoMach`, `ContainerFixedSimpleSwitchMach` exist only because a scroll/sword/panel needed to *be* a machine. Attached instead:

```python
kinging_scroll = Item('kinging_scroll', 'Kinging Scroll', 'scroll', 'kinging_scroll',
                      writing=illuminated_letters, weight=1,
                      mach_lst=[scroll_win_mach])
```

The two moves are complementary and multiplicative: attachment removes the host×machine matrix, kwargs remove the capability matrix within each family. Together, my rough count of your `class_std` + `class_mach` + `interactive` concrete classes goes from ~25 to ~10, and — the real prize — the count stops being a function of feature combinations.

### The authoring payoff (and why this feeds the editor)

Compare what `game_update.py` looks like. Today:

```python
crystal_box = ContainerPortableLockable('crystal_box', 'Crystal Box', 'box',
    'crystal_box', calligraphy, 5, ['kinging_scroll_temp'], 1, 5, 'in', False, False, silver_key)
```

Thirteen positional values where `1, 5` means max_weight-then-max_obj and `False, False` means... you have to go look. After:

```python
crystal_box = Container('crystal_box', 'Crystal Box', 'box', 'crystal_box',
    writing=calligraphy, weight=5, prep='in',
    contain_lst=['kinging_scroll_temp'], max_weight=1, max_obj=5,
    is_open=False, is_locked=False, key=silver_key)
```

Self-documenting, order-independent, and every absent capability simply isn't mentioned — which is also why your `Core`/`IO`/`Map` constructors' `# name`-comment scaffolding disappears. And note the editor connection: a web form naturally produces named fields. `{'weight': 5, 'is_locked': False, 'key': 'silver_key'}` *is* a kwargs dict — `Container(**form_data)` — whereas generating correct 13-element positional calls from a form is misery. Same argument as the Command record, one layer down: named fields beat positional encodings everywhere data crosses a boundary.

### Two practical cautions

1. **Pickle churn.** This refactor rewrites `__init__` signatures and instance attributes, so both games' pickles must be rebuilt and both regression suites run — your standard rule, but this is the biggest pickle-breaking change you'll have made, which is also an argument for doing recommendation 4 (state-only saves) in the same era rather than after.
2. **Migrate one family at a time.** Containers first (biggest win, most self-contained), then doors, then the machine collapse, with scenario tests between each. Keep the old class names alive briefly as one-line shims (`def ContainerFixedSimple(*a, **kw): return Container(...)`) if you want game_update.py to migrate on its own schedule — then delete them when both games are converted.

The one-sentence version: **subclasses should mean "behaves differently," and keyword args should mean "has or lacks a capability" — your current tree uses subclasses for both, and that second job is what's exploding it.**

---

## Human

> Can you give me an example of how I consume the kwargs capabilities in a verb method or an error method?

---

## Assistant

*(After reading your actual `open()`, `open_err()`, `OpenableMixIn`, and `LockableMixIn` code.)*

Perfect question to ask against your actual code, because pulling up `open_err()` reveals something delightful: **your error methods are already written in capability-consumption style.** Look at `error_class_def.py:232-250` — `open_err()` never asks "am I a `ContainerFixedLidded`?" It asks `self.is_openable()`, `self.is_container()`, `self.is_lockable()` — pure capability checks. The method bodies barely change. What changes is *where those checks get their answers*.

Even better: you already invented the convention this needs. Look at your own docstring on `interactive_class_def.py:83`:

```python
self._is_unlocked = is_unlocked # True if the door is unlocked, False if the door is locked, None if there is no lock
```

*"None if there is no lock."* That's the whole mechanism — you wrote it and then didn't cash it in. Here's the cash-in.

### Step 1: identity methods read attribute presence

Today `is_openable()` returns `False` on the `Identity` base and the `OpenableMixIn` overrides it to `True` — presence is encoded in *which class you inherited*. Instead, on the collapsed class:

```python
class Container(ViewOnly):
	def __init__(self, name, full_name, root_name, descript_key, *,
			writing=None, contain_lst=(), max_weight=999, max_obj=999, prep='in',
			weight=None,       # None => fixed in place
			is_open=None,      # None => no lid
			is_unlocked=None,  # None => no lock  (your own convention!)
			key=None):
		...

	# *** class identity methods ***
	def is_item(self):
		return self._weight is not None

	def is_openable(self):
		return self._is_open is not None

	def is_lockable(self):
		return self._is_unlocked is not None
```

That's the entire trick. The engine-wide `is_*()` API — everything `interp`, `validate`, machines, and conditions call — keeps working unchanged, because callers never cared *how* the answer was computed.

### Step 2: the error method — unchanged, annotated

Here is your existing `open_err()`, verbatim, with comments showing where each check now resolves:

```python
	def open_err(self, gs):
		creature = gs.core.hero
		if self.err_std(creature, gs):                        # unchanged
			return True, False, ""
		if not self.is_openable() and self.is_container():    # True when is_open=None was passed
			err_txt = (f"The {self.full_name} has no closure. It is always open.")
			return True, False, err_txt                       # <- old ContainerFixedSimple case
		if not self.is_openable() and not self.is_container():
			err_txt = (f"The {self.full_name} cannot be openned.")
			return True, True, err_txt                        # <- plain ViewOnly case
		if self.is_open:                                      # only reachable if lidded
			err_txt = (f"The {self.full_name} is already open.")
			return True, False, err_txt
		if self.is_lockable() and self.is_unlocked == False:  # True only when is_unlocked=False was passed
			err_txt = (f"The {self.full_name} is locked.")
			return True, True, err_txt                        # <- old *Lockable case
		return False, False, ""
```

**Zero body changes.** The six container classes' worth of behavioral variety was always living in these guards; the subclasses were just redundantly re-stating what the attributes already said. Note the nice property of the `None` convention here: `if self.is_open:` naturally falls through when `is_open` is `None`, because the `is_openable()` guard above it already screened that case out.

### Step 3: the verb method — one pattern to know

Your `open()` (`interactive_class_def.py:52`) also survives nearly verbatim, because it already branches on capability for the contents display:

```python
	def open(self, gs, mode=None):
		""" Opens a door or lidded container.
		"""
		if mode is None:
			mode = 'std'

		self.is_open = True

		gs.io.buff_cr()
		gs.io.buff_no_cr("Openned. ")
		if self.is_container():          # already capability-style in your current code
			self.disp_contain(gs)
		gs.io.buff_cr()
		return
```

The one architectural point to hold onto: **`open()` doesn't need its own capability guard, because your pipeline already provides it.** `app_main` runs `validate()` before `cmd_execute()`, so by the time `open()` executes, `open_err()` has certified `is_openable()` is true. That division of labor — *err methods check capabilities, verb methods assume them* — is your existing design, and it's exactly right for this. The only methods that need internal capability branches are ones like `open()`'s contents display or `examine()`'s `disp_cond()`, where behavior *enriches* based on optional capabilities:

```python
	def disp_cond(self, gs):
		if not self.is_openable():       # fixed-open container: no open/closed state to report
			return
		if self.is_open == False:
			gs.io.buff_no_cr(f"The {self.full_name} is closed. ")
			return
		gs.io.buff_no_cr(f"The {self.full_name} is open. ")
```

(That `if not self.is_openable(): return` guard is the one genuinely *new* line this refactor asks of you — methods that previously only existed on lidded classes now exist on all containers and must no-op gracefully when the capability is absent.)

### The payoff test: adding a capability with no new class

Suppose you later want transparent containers (see contents while closed). Today: four new classes (`ContainerFixedLiddedTransparent`...). After:

```python
	# in __init__:              is_transparent=False,
	# new identity method:      def is_see_thru(self): return self._is_transparent

	# in examine() / disp_contain-related logic, one guard changes:
	if not self.is_openable() or self.is_open or self.is_see_thru():
		self.disp_contain(gs)
```

One kwarg, one identity method, one guard edited. `glass_bottle = Container(..., is_open=False, is_transparent=True)`. That's the geometric-to-linear conversion in action.

The summary of "how to consume": **err methods keep doing what they already do — guard on `is_*()` checks — and verb methods keep assuming validation passed; the refactor just moves the source of truth for `is_*()` from "which mixin am I" to "which kwargs were set," which your `None`-means-no-lock convention had already half-built.**

---

## Human

> I'm not familiar with the python 'not None' convention you use above (i.e. return self._weight is not None ). How does this work?

---

## Assistant

This is a small but important Python idiom, and it's worth understanding precisely because the whole kwargs-capability scheme leans on it.

### The pieces

**`None` is a singleton.** There is exactly one `None` object in a running Python program. Every variable set to `None` points to that same single object.

**`is` tests identity, not equality.** `a is b` asks "are these literally the same object in memory?" — not "do they have equal values?" (that's `==`). Because `None` is a singleton, `x is None` is the canonical way to ask "is x the None object?"

**`is not` is the negation.** It's a single two-word operator, not `is (not ...)`. So:

```python
self._weight is not None
```

reads as: "does `_weight` point to something other than the `None` object?" The expression evaluates to a plain `True` or `False`, which is why you can return it directly:

```python
def is_item(self):
	return self._weight is not None   # returns True or False
```

That's the same "return the comparison itself" style you flagged in your own refactoring notes in dump_doc.md (#15) — no `if/else` needed.

### Why not `!= None` or a plain truthiness check?

This is the part that actually matters for your engine. You have three candidate spellings, and two of them have traps:

**1. `if self._weight:` (truthiness) — wrong for your use case.** Python treats `0`, `0.0`, `""`, `[]`, and `False` as falsy. So a truthiness check can't distinguish "capability absent" from "capability present with a falsy value":

```python
zorkmid = Container(..., weight=0.5)   # portable
feather = Container(..., weight=0)     # portable, weightless!

if self._weight:            # WRONG: feather looks fixed-in-place
if self._weight is not None # RIGHT: feather is an item, weight happens to be 0
```

Your `is_open` case is even sharper, because `False` is a *meaningful* value:

```python
paper_bag._is_open = False   # has a lid, currently closed
wooden_shelf._is_open = None # has no lid at all

if self._is_open:             # WRONG: both look "not open" — can't tell closed from lidless
if self._is_open is not None  # RIGHT: bag is openable, shelf is not
```

This is exactly why `None` works as the "absent" sentinel: it occupies a slot *outside* the capability's real value range (`True`/`False`/numbers), so absence never collides with a legitimate value.

**2. `!= None` — works, but non-idiomatic and subtly fragile.** `==`/`!=` can be overridden by classes (`__eq__`), so a sufficiently weird object could answer `x == None` incorrectly. `is` can't be overridden — identity is identity. PEP 8 (the official style guide) is explicit: comparisons to `None` should always use `is` / `is not`. Any linter will flag `!= None`.

**3. `is not None` — the idiom.** Unambiguous, override-proof, and instantly readable to any Python programmer as "the absence check."

### You're already using the pattern

You've been writing half of this idiom all along — every verb method starts with:

```python
if mode is None:
	mode = 'std'
if creature is None:
	creature = gs.core.hero
```

That's the same convention from the other side: `None` as "caller didn't supply this, use the default." The capability scheme just extends it from *method parameters* to *object attributes*: `None` means "this object wasn't given this capability." One mental model, both places.

One habit to adopt alongside it: when `None` is a legal value for an attribute, comparisons elsewhere should stay explicit too — you already do this correctly in `open_err()` with `self.is_unlocked == False` (which is `False` only for a locked thing, never for a lockless one where `is_unlocked` is `None`). Though for full idiom points, the Python-native spelling of that line would be `self.is_unlocked is False` — same reasoning, identity against the `False` singleton — or more conventionally, guard with `is_lockable()` first exactly as you already do.

---

## Human

> Thanks for explaining - I get it now - this will be a big change but a really valuable one. I've been jealous of the flexibility of Infocom's *bit approach - and now I see how to achieve something similar! Last but not least, let's look at 4. I've always meant for state storage in pickles to be a temporary solution... with maybe sqlalchemy as the long-term approach... but I think you are recommending a bigger shift? You are suggesting that I reduce the state file to only the changes from default state?

---

## Assistant

Close, but not quite — I'm recommending a *partition*, not a *diff*. The distinction matters, so let me separate three questions that pickle currently answers all at once: **what** gets saved, **how** it's encoded, and **where** it lives. SQLAlchemy is an answer to "where," but the architectural problem is "what."

### The partition: world definition vs. world state

Everything in your object graph divides cleanly into two kinds of data:

- **Definition** (immutable, owned by code): class structure, descriptions in `game_static_dict`, the map topology, machine cond/result wiring, max_weight, verb behavior. `game_update.py` already *is* this — it rebuilds the pristine world deterministically.
- **State** (mutable, owned by the player's playthrough): where every object currently is (`floor_lst`, `contain_lst`, `hand_lst`, `worn_lst`), `is_open`/`is_unlocked`, every machine's `mach_state`/`is_enabled`, timers, `hero_rm`, `rm_visit_lst`, score, move count, the removed-from-world biscuit.

Today's pickle stores both, entangled — which is exactly why every class refactor invalidates every save, and why the kwargs refactor we just discussed will be maximally painful under the current format. The fix: **a save file contains state only; the definition is rebuilt from code on every load, and the state is applied on top.**

```python
# save: walk master_obj_lst, emit mutable attrs, objects referenced by name
{
  "hero_rm": "gatehouse",
  "move_count": 42,
  "front_gate":   {"is_open": true, "is_unlocked": true},
  "crystal_box":  {"is_open": false, "is_unlocked": false, "contain_lst": ["kinging_scroll"]},
  "burt":         {"hand_lst": ["shiny_sword"], "bkpk_lst": ["rusty_key", "cheese_wedge"], ...},
  "hedgehog_eats_timer": {"mach_state": 2, "is_active": true},
  ...
}

# load: world = build_world()          <- game_update.py, refactored into a callable
#       apply_state(world, saved_dict) <- names resolved back to objects
```

To your actual question — diff vs. full: Infocom saves *were* diffs (XOR of writable memory against the story file), but that was an artifact of 80KB floppies. **You should save the full mutable state of every object, not just changed objects.** A diff needs a reference copy of the defaults to compare against, adds a failure mode (default drifted between versions → diff applies wrong), and buys you nothing you need — the full state of dark_castle is a few KB of JSON. Full-state is dumber, and dumber is correct here.

### Why this beats both pickle *and* the SQLAlchemy plan

**On encoding:** the moment state is names-and-primitives, it's JSON. That gets you, in one move: saves that survive class refactors (new attribute? constructor default applies, old saves simply don't mention it; removed attribute? ignore the stale key with a warning — compare pickle, which hard-fails on both); human-readable saves (debugging a player's stuck game = reading a text file; your scenario tests could assert directly on state); and — decisive for the web — `json.loads()` on user-supplied data is safe, while `pickle.load()` is an arbitrary-code-execution vector. You cannot ship a web game that unpickles anything a browser can influence.

**On SQLAlchemy:** it solves storage, not structure. If you adopt it while still pickling the whole graph, you get a pickle blob in a database column — all the old fragility, plus a dependency. And the opposite extreme (a normalized relational schema: objects table, containment table, machine-state table...) is real work that buys nothing for single-player saves. Once state is a JSON dict, the "where" question becomes trivial and can stay trivial: a file per save slot today; a `TEXT` column keyed by session ID when you go web. If you later want accounts, leaderboards, multiple slots — *that's* when a database earns its place, and the state blob just rides along as one column. My honest advice: you probably never need SQLAlchemy for this; don't let it become a project.

### The web angle — this replaces the per-turn pickle too

Note what `app_main()` does now: load `active_pkl`, run one turn, dump `active_pkl`. Your whole engine is already stateless-per-turn — that's a genuinely web-ready shape you built without the web forcing it. The state-only format slots straight into that loop: load = `build_world()` + `apply_state(session_state)`, run turn, save = `serialize_state()`. Rebuilding the world from `game_update` each turn sounds wasteful but is instantiating a few hundred small objects — microseconds against a human typing commands. And it means the per-turn persistence, the save command, *and* the future web session store are all the same mechanism instead of three.

### What it costs, and the synergies you've already paid for

Three pieces of work:

1. **`game_update.py` becomes `build_world()`** — a function returning `master_obj_lst` instead of a script that writes a pickle at import time. (The pickle write can remain as a thin wrapper during transition.)
2. **`serialize_state()` / `apply_state()`** — the object↔name conversion at the boundary. This is *the same name-resolver* we said recommendation 2 wants for killing the `'_temp'` placeholder strings and the 60-line reassignment block. Build it once, it serves both.
3. **Deciding what's mutable.** Simplest v1: serialize every instance attribute, converting object refs to names. It'll re-save some constants (`max_weight`) harmlessly. If that ever bothers you, graduate to a per-class `_state_attrs` list — but don't start there.

One thing you *don't* have to handle: runtime object creation. Your machines dispense and remove pre-built objects but never mint new ones, so the object roster is fixed at build time and names are stable. That single property is what makes this whole approach easy — worth protecting as a deliberate engine invariant.

Sequencing-wise, this pairs naturally with the kwargs refactor rather than following it: that refactor is the biggest pickle-breaking change you'll ever make, and if state-only saves land first (or together), it's also the *last* save-breaking change you'll ever make. After that, class structure and save files are decoupled permanently — the same split that let Infocom rewrite interpreters for fifteen years without ever invalidating a player's save.

---

## Human

> Believe it or not, I started out trying to save state as json using marshmallow... and ran into huge issues because of all my custom objects... marshmallow treated the hedgehog in the gatehouse as distinct from the hedgehog in the creature definition - and everywhere else. I worked away at this for a while and eventually surrendered and went to pickles because, despite the lack of human readability, that was the native object marshaling format for python - and it worked on the first try. Are you suggesting that I reference all obj by unique names in the json and then convert to obj on turn execution? And if so, how do I ensure I don't run into the same problem I did before?

---

## Assistant

Yes — that's exactly what I'm suggesting, and your marshmallow scar tissue is actually the perfect setup for understanding why it can't recur. What defeated you before wasn't JSON, and it wasn't your custom objects. It was that marshmallow answers a different question than the one you were asking.

### What actually went wrong with marshmallow

Your world is a **graph with shared references**: the one hedgehog object is pointed at by `gatehouse.floor_lst`, by `biscuits_in_hedgehog_hand_cond.creature_obj`, by machine `alert_anchor`s, and so on. Identity — *the same object, everywhere* — is load-bearing.

Marshmallow is built for API payloads, which are **trees serialized by value**. When it meets the hedgehog through `floor_lst`, it expands it into a nested dict. When it meets it again through the condition, it expands another copy. It has no memory of having seen that object before. On deserialization, each nested dict constructs a *fresh instance* — and now you have five hedgehogs that are `==`-ish but not `is`, and mutating one does nothing to the others. (I'd bet you also hit infinite recursion somewhere, because your graph has cycles — `shiny_sword.alert_anchor` is the sword itself.)

Pickle worked on the first try because pickle has a **memo table**: the second time it encounters the same object, it writes a back-reference instead of a copy, and on load it reconstructs the shared structure faithfully. Pickle solves graph identity; marshmallow never tries to.

### Why the name-based approach is immune, structurally

Here's the reframe: pickle and marshmallow are both answers to "how do I turn my objects into bytes and back?" The name-based approach **refuses to round-trip objects at all**. It rests on one invariant:

> **Domain objects are constructed in exactly one place — `build_world()` — and the save file can never cause a construction.**

Serialization never descends *into* a referenced object; it writes the object's name — one flat string token — and stops. Deserialization never *creates* an object; it looks up the already-existing one and mutates its attributes:

```python
def apply_state(registry, state_dict):
	for obj_name, attr_dict in state_dict.items():
		obj = registry[obj_name]          # look up the ONE hedgehog — never construct
		for attr, val in attr_dict.items():
			setattr(obj, attr, decode(val, registry))
```

The duplicate-hedgehog bug required a code path where a serialized representation becomes a new instance. That code path does not exist here. There's nothing to get right at load time — the identity problem was solved earlier, at build time, by the fact that `royal_hedgehog = Creature(...)` runs exactly once. Your test for success is, fittingly, the operator you just learned:

```python
world.gatehouse.floor_lst[1] is registry['royal_hedgehog']   # True — same object, everywhere
```

### The mechanics, using what you already have

**The registry already exists.** `gs.core.str_to_obj_dict` is a name→object map you built for the parser. Two upgrades: it must include *invisible* objects (machines, timers, conditions carry `mach_state`/`is_enabled` — they have state to save; `master_obj_lst` currently excludes them), and it should enforce uniqueness. Cleanest spot: register in the base `Invisible.__init__`, which every object passes through —

```python
if name in gs_registry:
	raise ValueError(f"duplicate object name: {name}")
gs_registry[name] = self
```

— which as a bonus turns "I accidentally reused a name" from a silent lookup bug into a build-time crash.

**The encoder is ~30 lines of your own code — no marshmallow, no library.** One decision to make: how does the decoder know `"royal_hedgehog"` is a reference and not just a string? Don't guess by checking the registry — you'd get bitten, because ordinary strings legitimately collide with names (`descript_key` values often *equal* object names). Mark references explicitly:

```python
def encode(val):
	if val is None or isinstance(val, (bool, int, float, str)):
		return val
	if isinstance(val, list):
		return [encode(v) for v in val]
	if isinstance(val, dict):
		return {encode_key(k): encode(v) for k, v in val.items()}
	return {'$obj': val.name}            # any game object -> name token, full stop

def decode(val, registry):
	if isinstance(val, dict) and '$obj' in val:
		return registry[val['$obj']]     # resolve to the one existing instance
	...  # mirror-image recursion for lists/dicts
```

Two of your data shapes need the small extra care visible above: dict *keys* (the hedgehog's `give_dict` is keyed by object — JSON keys must be strings, so encode keys as `"@shiny_sword"` or similar), and cycles — which, note, simply vanish under this scheme: `shiny_sword.alert_anchor` encodes to `{'$obj': 'shiny_sword'}` and recursion never enters the object, so the cycle that likely blew up marshmallow can't even be expressed.

**Graceful failure replaces hard failure.** A state key for an attribute that no longer exists → log and skip. A `$obj` name not in the registry (save from a version where that object existed) → log and skip. Compare pickle, where either case is an unpicklable file.

The one-sentence summary: your marshmallow attempt failed because you asked a tree-by-value serializer to preserve graph identity; pickle succeeded because it preserves graph identity at the cost of freezing your code structure into the file; the name-registry approach *sidesteps* the graph problem entirely by making the serialized file reference-only and letting `build_world()` — which was always your real source of truth — remain the sole owner of object identity.

---

## Human

> I'm not familiar with the '$obj' naming convention - what does this mean?

---

## Assistant

Nothing — and that's the point worth explaining. `$obj` has no special meaning to Python, JSON, or any library. It's just a dictionary key I made up. The pattern it implements is the real concept: a **tagged wrapper** (sometimes called a sentinel key or type tag).

### The problem it solves

Your encoder turns values into JSON. Most values pass through as themselves — `5` stays `5`, `"verbose"` stays `"verbose"`. But an object reference becomes a name string, and the decoder needs to tell the difference between:

```json
"descript_key": "royal_hedgehog"     <- a genuine string that happens to equal a name
"alert_anchor": ???                  <- a reference that must be resolved to the hedgehog object
```

If both were bare strings, the decoder would have to guess, and it would guess wrong exactly when a plain string collides with an object name — which in your data happens constantly (`descript_key` values, `trig_vals_lst` entries, score keys).

The tagged wrapper removes the guessing by giving references a *shape* that plain data can never have: instead of a bare string, a reference is a one-key dict whose key is a reserved marker:

```json
"descript_key": "royal_hedgehog"            <- string: passes through untouched
"alert_anchor": {"$obj": "royal_hedgehog"}  <- dict with the magic key: resolve via registry
```

The decoder's rule is then purely mechanical — no heuristics:

```python
if isinstance(val, dict) and '$obj' in val:
	return registry[val['$obj']]    # it's a reference
```

### Why the `$`?

Convention, borrowed from the JSON ecosystem: JSON Schema uses `"$ref"`, MongoDB uses `"$set"`/`"$gt"`, several serializers use `"$type"`. The `$` character carries no semantics — it's chosen because it's *unlikely to occur naturally*, which is what makes the tag safe. Your real dictionary keys are Python attribute names and descript keys (`is_open`, `mach_state`, `royal_hedgehog`), and none of them will ever start with `$`. So a dict containing the key `$obj` can only be something your own encoder wrote, never player data or game data that happens to look similar.

You could just as well use `"__ref__"` or `"@@"` or `"OBJ_REF"` — anything works, provided it satisfies the one requirement: **the marker must be impossible to confuse with legitimate data**. Since you control both `encode()` and `decode()`, you're defining a tiny private file-format vocabulary, and this is its only word.

One honest caveat, for completeness: the scheme assumes no *ordinary* dict in your game state has a `$obj` key — true today by construction, since your dict keys are identifiers you author. If you wanted belt-and-suspenders, `decode()` can check `len(val) == 1 and '$obj' in val`, making accidental matches even more far-fetched. In practice the convention is considered collision-proof enough that half the JSON tooling world runs on it.

So when you read my earlier sketch: `{'$obj': val.name}` just means "wrap the name in an envelope that says *this is a reference, resolve me*" — and the `@shiny_sword` sigil I suggested for dict *keys* is the same idea in string-prefix form, used there because JSON object keys must be strings and can't be wrapper dicts.

---

## Human

> Thanks - now I understand the object tagging... but I still don't have a tangible feel for how I would use encoder and decoder... today I start each turn by opening loading the obj master list from the pickle - and I end each turn by saving a new pickle of all the obj (updated or not). How would this work under what you're proposing? Where would the json file / files live?

---

## Assistant

Let me ground this in your actual turn cycle — the change is surgical: two lines at the top of `app_main()` and one at the bottom.

### Your turn cycle today

```python
def app_main(user_input, game_name, root_path_str):
	pkl_str = f"{root_path_str}/cleesh/games/{game_name}/working/active_pkl"
	with open(pkl_str, 'rb') as f:
		master_obj_lst = pickle.load(f)        # <- world AND state, fused
	gs = master_obj_lst[0]

	... the whole turn: interp, validate, machines, cmd_exe ...

	with open(pkl_str, 'wb') as f:
		pickle.dump(master_obj_lst, f)         # <- world AND state, fused
```

### The same cycle under the new scheme

```python
import json
from cleesh.games.dark_castle.game_file.game_update import build_world

def app_main(user_input, game_name, root_path_str):
	state_path = f"{root_path_str}/cleesh/games/{game_name}/working/active_state.json"

	registry, master_obj_lst = build_world()   # 1. pristine world, from code
	gs = master_obj_lst[0]
	with open(state_path) as f:
		apply_state(registry, json.load(f))    # 2. overlay this playthrough's state

	... the whole turn: interp, validate, machines, cmd_exe — UNCHANGED ...

	with open(state_path, 'w') as f:
		json.dump(serialize_state(registry), f, indent=1)   # 3. persist state only
```

Everything between load and save — the entire turn pipeline — doesn't know anything happened. It still operates on live Python objects with shared identity, exactly as it does now. The pickle round-trip is replaced by *rebuild + overlay* on the way in, and *extract state* on the way out.

The two new functions are small. Version 1 of `serialize_state` just dumps every object's `__dict__` through the encoder; `apply_state` is its mirror:

```python
def serialize_state(registry):
	return {name: {attr: encode(val) for attr, val in vars(obj).items()}
			for name, obj in registry.items()}

def apply_state(registry, state):
	for name, attrs in state.items():
		obj = registry.get(name)
		if obj is None:
			continue                        # object from another version: skip, maybe log
		for attr, val in attrs.items():
			setattr(obj, attr, decode(val, registry))
```

(`vars(obj)` returns the instance `__dict__`, so the keys are your underscored attribute names — `_is_open`, `_mach_state` — and `setattr` writes them back identically, bypassing the properties. The gs modules — `core`, `map`, `io`, `score`, `end` — all have names, so they flow through the same registry, which is how `hero_rm`, `move_count`, and `rm_visit_lst` get captured.)

### Where the files live

Your existing directory layout maps over almost one-to-one:

```
cleesh/games/dark_castle/
    game_file/
        game_update.py          <- now defines build_world(); game_pkl DELETED
        game_static_gbl.py      <- unchanged
    working/
        active_state.json       <- replaces active_pkl (the current playthrough)
    saves/
        save_1.json             <- replaces the pickle save slot
```

Note what disappeared: **`game_pkl` has no successor.** Its whole job was to be a frozen copy of the pristine world, and the pristine world is now something you *run* (`build_world()`), not something you store. One consequence you'll feel immediately: the "edit a class → remember to re-run game_update for both games → commit the binary pickle" ritual is gone. `build_world()` executes fresh each turn, so class changes take effect the moment you save the `.py` file, and no binaries live in git.

The lifecycle commands become file operations on JSON:

- **New game / restart:** `serialize_state()` a freshly built world straight into `active_state.json` — the "default state" is just what a pristine build serializes to.
- **`save`:** copy `working/active_state.json` → `saves/save_1.json`.
- **`restore`:** copy it back.

And a debugging bonus that falls out for free: since a new game's state file is the complete default state, `diff <(fresh_state) active_state.json` shows you *exactly* what has changed in a playthrough — which machines have fired, where every object has migrated. That's a view into your game you've literally never had through pickle.

### Two prerequisites, one reassurance

1. **`build_world()` must be a callable, not a script.** Today `game_update.py` builds the world *at import time* and writes the pickle as a side effect. Wrap the construction in a function returning `(registry, master_obj_lst)`; the registry can be as simple as collecting every object as it's constructed (the `Invisible.__init__` registration we discussed, which also gets you duplicate-name detection).
2. **Determinism.** `build_world()` must produce the same world every call — no randomness at build time. Yours already is, as far as I can see; just worth stating as an invariant since the design now leans on it.

The reassurance: **performance is a non-issue.** Building dark_castle is instantiating a few hundred small Python objects — well under a millisecond — and `json.dump` of a few-KB dict is similar. Your current pickle round-trip per turn costs about the same. And when you go to the web, this same shape scales sideways without modification: `active_state.json` becomes a text blob keyed by session ID in whatever store you like, and `build_world()` + `apply_state()` runs per request exactly as it runs per turn today. The stateless-turn architecture you already built is the hard part; this just swaps what flows through it.

Your scenario test harness is the safety net for the migration: it replays command scripts end-to-end, so if the suite passes for both games under the JSON cycle, the swap is proven equivalent to pickle — same commands, same output, same final state.

---

## Human

> so, what goes in game_update vs. what goes in save_1 ?

---

## Assistant

The crisp rule: **`game_update.py` decides what exists; `save_1.json` records what's currently true of it.** Or in the terms we've been using: existence and wiring vs. current values. Let me make that concrete with your actual objects, then flag the one place where v1 blurs the line on purpose.

### The three buckets (you already have all three files)

| File | Owns | Examples from dark_castle |
|---|---|---|
| `game_static_gbl.py` | All prose | `'front_gate': "A massive gate of..."`, help text, score titles |
| `game_update.py` | What exists, what class it is, how it's wired, its starting values | *There is* a `front_gate`, it's a `DoorLockable`, its key is `rusty_key`, it starts closed and locked; the map connects entrance→gatehouse through it; `goblin_attack_mach` watches these six triggers with these conds/results |
| `save_1.json` | The current value of every attribute, this playthrough | `front_gate` is now open and unlocked; the sword is in Burt's hand; `mach_state` of the sword-glow machine is 2; `hero_rm` is `throne_room`; score is 35; the biscuit no longer exists anywhere |

A side-by-side for one object. In `game_update.py` (definition — runs every turn, always the same):

```python
front_gate = DoorLockable('front_gate', 'Front Gate', "gate", 'front_gate',
        rusty_lettering, False, False, rusty_key)   # starts closed, locked
```

In `save_1.json` (state — what a playthrough has done to it):

```json
"front_gate": {
    "_is_open": true,
    "_is_unlocked": true,
    "_key": {"$obj": "rusty_key"},
    ...
}
```

And the load sequence reads: `build_world()` creates the gate closed and locked (as always) → `apply_state()` overwrites those two attributes with this playthrough's truth.

### What the save file can *never* contain, by construction

No matter what's in the JSON, it cannot: create an object, delete an object from the roster, change an object's class, alter a method, add a room to the map's *possibility space*, or change any string in the static dicts. Those live only in code. This is the property that makes the scheme refactor-proof — when you do the kwargs collapse and `front_gate` becomes `Door(..., is_open=False, is_locked=True, key=rusty_key)`, old saves still apply cleanly, because they only ever spoke about attribute values, and the attributes (`_is_open`, `_is_unlocked`) still exist.

(You might ask: the biscuit gets *removed* during play — isn't that a roster change? No: `RemoveObjResult` takes it out of every containment list, but the object still exists in the registry. The save records it as contained-by-nothing. Existence in the roster and presence in the world are different things — and that distinction is exactly why your dispense/remove machinery needs no special handling.)

### The v1 blur, and when to sharpen it

Now the honest wrinkle. Under the v1 "dump all of `__dict__`" approach, `save_1.json` also contains attributes that are *conceptually* definition — `_full_name`, `_max_weight`, the hedgehog's `give_dict`, machine `_trig_vals_lst` — because Python instance attributes don't announce which ones are mutable. So the physical file holds more than the conceptual "state" bucket.

This is mostly harmless: `apply_state` overwrites `_max_weight = 1` with `_max_weight = 1`. But it has one real consequence worth knowing in advance: **a save pins definition-flavored values as of when it was written.** If you rebalance `crystal_box.max_weight` from 1 to 2 in version 3.5, a save from 3.4 will restore the old 1. Whether that's a bug or a feature depends on the attribute — for a puzzle-balance tweak it's annoying; for something like `descript_key` (which your `ChgDescriptResult` machines legitimately mutate during play!) saving it is *required*.

That last example is the interesting one: `descript_key` looks like pure definition, but your own machine system mutates it — the hedgehog's description changes after it's fed. Which proves the line between definition and state can't be drawn by *kind of attribute*; it's drawn by **"can gameplay change this?"** So the graduation path, when the redundancy starts to bother you:

- **v1 (start here):** serialize everything; accept the pinning trade-off. Zero bookkeeping, and `ChgDescriptResult`-style mutations are captured automatically.
- **v2 (if/when needed):** each class declares its playthrough-mutable attributes — `_state_attrs = ('_is_open', '_is_unlocked')` on the collapsed `Container`, `('_mach_state', '_is_enabled')` on `Machine`, etc. — and `serialize_state` walks only those. Saves shrink, rebalances propagate into old saves, and the conceptual partition becomes the physical one.

I'd genuinely start with v1 and let real friction, not principle, trigger v2 — the migration between them is one loop guard in `serialize_state`, and shipping the simple version first gets both games onto refactor-proof, web-safe saves now rather than after another schema debate.

---

## Human

> I think I get it. Let's ponder scale for just a moment. My vision is that someday I have dark_castle on the web as a multi-player game... so many players with many save files... does this work with the json approach?

---

## Assistant

Yes — and it's worth splitting your vision into its two possible meanings, because they scale very differently. The JSON approach handles the first one almost for free, and it's the *only* one of your options that even has a path to the second.

### Meaning 1: many players, each in their own castle

This is "many concurrent single-player sessions" — many saves, one world definition. The architecture we've discussed was quietly designed for exactly this:

- **The world definition ships with the code.** `build_world()` and the static dicts deploy with your app. A thousand players don't have a thousand worlds stored anywhere — they share one definition, rebuilt per request, exactly like a thousand Infocom players shared one story file.
- **Each player is one small state blob.** A few KB of JSON. The only per-player data that exists *anywhere* is that blob.
- **Your turn cycle is already stateless.** `app_main()` takes input, loads state, runs one turn, stores state. That shape scales horizontally with no further thought: any server instance can process any player's turn, because nothing lives in server memory between turns.

The one thing that changes at scale is *where the blob lives*. A directory of files works for you-plus-friends but fails at real concurrency (no atomic writes, no locking, painful backup). The natural evolution:

```
now:        working/active_state.json               (file per playthrough)
soon:       SQLite, one table                        (same blob, now transactional)
web scale:  Postgres                                 (same table, same blob)

saves(user_id, game_name, slot, state_json, turn, updated_at)
```

Note what that is: **one table.** This is where a database finally earns its place in your stack — and why I pushed back on SQLAlchemy-as-architecture earlier. The state blob doesn't get decomposed into relational tables of objects and containment; it stays a JSON document that happens to live in a column. (Postgres's JSONB type will even let you query *into* it — "how many players have fed the hedgehog" is a one-liner, which is a fun analytics door you never had.)

One genuine new problem arrives with the web, and it's small: **the same player submitting from two tabs.** Two turns load the same state, both write, last write silently wins. The standard cheap fix is optimistic locking, and you already have the version number for it — `move_count`:

```sql
UPDATE saves SET state_json = ?, turn = ?
WHERE user_id = ? AND slot = ? AND turn = ?   -- the turn we loaded
```

Zero rows updated → someone else's turn landed first → reject and re-render. That's the entire concurrency story for meaning 1.

For sizing intuition: a turn costs sub-millisecond world-build + sub-millisecond JSON parse + your game logic, dominated utterly by network latency. Text adventures are the cheapest workload on the internet — a $5 VPS with SQLite would genuinely carry thousands of daily players before you thought about Postgres.

### Meaning 2: players in the *same* castle

Shared-world multiplayer — Burt and a second player see each other in the gatehouse — is a different animal, and honestly a different project. The state format is the *least* of it: you'd have one shared blob (or one per region) instead of one per player, and turns applied to it in sequence, MUD-style. JSON-state-in-a-transactional-row supports that fine; the pickle-per-playthrough model never could have.

The real costs live in the engine's single-hero assumptions, and it's worth naming them now only so your refactors don't deepen them: `gs.core.hero` as a global singleton, `gs.map.hero_rm` as *the* location, one IO buffer as *the* output stream (player B needs to see "Burt enters from the south" — output becomes per-observer), and machine visibility anchored to the hero's room. Notice that the first item is exactly recommendation 6 — threading `creature` through verb methods instead of hardcoding the hero — which you rated "maybe." Shared-world play is the scenario that converts it from politeness to prerequisite. I still wouldn't build any of it now; I'd just apply a cheap discipline: when you touch a verb method during the kwargs refactor anyway, prefer `creature` parameters over fresh `gs.core.hero` references, so the assumption gets shallower over time instead of deeper.

The strategic summary: **everything in the JSON plan is load-bearing for both futures.** Session-per-player web play needs nothing beyond a table and an optimistic lock; shared-world play needs major engine work someday, but consumes the same state format, the same registry, the same stateless turn — and would have been flatly impossible on whole-graph pickles. Nothing we've designed this conversation gets thrown away at either scale.

---

## Human

> Thanks - that's helpful. I'm definitely envisioning the many-players-each-in-their-own-castle case. I appreciate all the advice. It is a bit daunting but gives me great insight into where I should be headed!

---

## Assistant

You're welcome — this was a genuinely fun architecture discussion.

On the daunting feeling, two things worth holding onto:

**The order of operations keeps every step small.** Nothing here is a big-bang rewrite:

1. **Now:** finish the interpreter overhaul, folding in the Command record as you go — that's the piece with a deadline, since it stops the `trig_vals_lst` churn.
2. **Next era:** the kwargs class collapse and the JSON state format, ideally in the same window — one combined compatibility break instead of two, and the *last* save-breaking change you'll ever make. Migrate one class family at a time with the scenario harness running on both games between steps.
3. **Later, at leisure:** the grammar-as-data pass, the `_state_attrs` graduation, the saves table. None of it blocks anything else.

**You're closer than the list makes it feel.** The recurring pattern of this whole review was that you'd already half-built the right thing: the `*_err` methods were already capability-consumers, `is_unlocked = None` was already the absence convention, the cmd_queue was already the implicit-action mechanism, and the stateless turn cycle was already web-shaped. Most of this work is cashing in conventions you've already established rather than inventing new ones — and the payoff at the end is an engine where a game author writes a verb table, some objects with named kwargs, and machine triggers with named keys, which is exactly the low-effort authoring you were jealous of ZIL for, without ZIL's learning curve.

Good luck with the interpreter overhaul — and when you're ready to sketch the Command record or start the container collapse, the context is saved.

---

*End of transcript.*
