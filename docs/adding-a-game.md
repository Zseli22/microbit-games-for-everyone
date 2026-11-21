# Adding a game

This page is for someone adding a twelfth program to the collection. The goal is not to make every game identical; it is to make every game predictable for the player.

## Does it fit?

A program belongs here if:

- It can be played on a micro:bit V2.
- It has a complete audio-only path through its menus and results.
- It uses physical controls that can be found by touch.
- It follows the shared control vocabulary, or documents its exceptions clearly.
- It does not depend on the player seeing the LED matrix.
- It can be documented in the same shape as the other games.

A program that is primarily a visual demo, or that needs a phone or computer to play, is a better fit for a different repository.

## Folder and file names

- Folder: `games/<kebab-case-name>/`
- Program: `games/<kebab-case-name>/<CamelCaseName>.py`
- Guide: `games/<kebab-case-name>/README.md`

Examples:

```text
games/simon/Simon.py
games/vibration-challenge/VibrationChallenge.py
games/thirty-six/36.py
```

Avoid spaces in filenames. The micro:bit does not care, but URLs, command lines, and screen readers do.

## The shared control skeleton

Use this as a starting point. It detects the controller once, sets the audio output, and maps the four direction buttons and fire buttons to the same actions as the bare board.

```python
from microbit import *
import speech

controller = pin15.read_digital() == 1

if controller:
    music_pin = pin2
else:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    music_pin = None

def update():
    global up, down, left, right, confirm, secondary
    if controller:
        up = pin8.read_digital() == 0
        down = pin14.read_digital() == 0
        left = pin12.read_digital() == 0
        right = pin13.read_digital() == 0
        confirm = pin15.read_digital() == 0
        secondary = pin16.read_digital() == 0
    else:
        up = pin_logo.is_touched()
        down = pin1.is_touched() or pin2.is_touched()
        left = button_a.is_pressed()
        right = button_b.is_pressed()
        # Button A is both Left and Confirm in this skeleton, and Button B is
        # both Right and Secondary. Choose the mapping that fits the screen.
        confirm = button_a.is_pressed()
        secondary = button_b.is_pressed()
```

Adapt the last four lines to the game. If Button A is "left" in the menu and "confirm" in the game, decide which one the game needs and document it. Do not overload one physical control with two actions in the same state.

### Edge detection

The controller returns a held level: `pin15.read_digital() == 0` is true for as long as Fire 1 is down. If an action should happen once per press, remember the previous state:

```python
was_confirm = False

def pressed(now, before):
    return now and not before
```

Alternatively, use `button_a.was_pressed()` on the bare board, which already remembers a short press. Be consistent within a game.

### Audio

Use `music_pin` everywhere:

```python
audio.play(audio.SoundEffect(freq_start=880, freq_end=880, duration=100), pin=music_pin)
speech.say("Ready.", pin=music_pin)
```

On a bare board, `music_pin` is `None`, which selects the V2's built-in speaker. On the controller, it is the buzzer pin. Do not route audio to pin 0; there is no need to support V1.

### Touch mode

Only call `set_touch_mode` when `controller` is false. On the controller, pins 1 and 2 drive the vibration motor and the buzzer.

### Saves

Only one program can be on the board at a time, so the program can use the simple `save.txt` name. Flashing another program, or reflashing this one, erases the filesystem and the save.

```python
SAVE_FILE = "save.txt"
```

When loading, handle a missing file, an empty file, and malformed data without crashing. Tell the player in the guide that the save is temporary. Do not promise that files can be backed up or kept alongside another game.

Provide an in-game way to delete or reset a save where it makes sense (with a confirmation step). Reflashing the program also clears the filesystem; the `MICROBIT` drive is for `.hex` files, not for browsing MicroPython files.

### Reset and restart

If the game needs to start over, prefer returning to its own start screen over calling `reset()`. A full board reset is disorienting and loses the save state. If you must call `reset()`, say so in the guide.

## Documentation

Copy the shape of an existing guide. At minimum, include:

- A one-sentence description.
- An **At a glance** section: players, controller, speech, save behaviour, difficulty.
- **Before you play**: hardware and setup.
- **Controls**: two tables, bare board and controller. No pin numbers.
- **How to play**: a numbered walkthrough.
- **What you hear**: a table of sound cues and meanings, using note names rather than hertz.
- **Scoring and saves**: how to win and what happens to progress when you flash again.
- **Accessibility notes**: what works well and what is harder.
- **Tips**: optional.

Keep the control tables narrow. Two columns are easier to follow with a screen reader than five.

## Definition of done

A game is ready to merge when:

- [ ] It runs on a micro:bit V2.
- [ ] It runs with a bare board and with the controller, or the guide explains why one is not supported.
- [ ] Every menu item is reachable and announced or given a distinct tone.
- [ ] Every score and result has an audio form.
- [ ] A wrong answer and a correct answer sound different.
- [ ] A destructive action has a confirmation step.
- [ ] It uses `save.txt` if it saves, and the guide says a flash erases it.
- [ ] It follows the control vocabulary, or the exceptions are documented.
- [ ] The guide has no controller pin numbers.
- [ ] The guide has a **What you hear** table with note names, not hertz.
- [ ] The audio-only playtest in [accessibility.md](accessibility.md) has been run.
- [ ] The source compiles with `python -m py_compile`.
- [ ] The top-level README's game list has been updated.

## Review

A review is a conversation about the player's experience, not a style contest. The most useful review notes are of the form:

- "I could not tell whose turn it was."
- "The win sound and the lose sound are too similar."
- "I had to look at the screen to find the menu."
- "The save loaded, but it did not say so."
- "The controller mapping for this action is different from every other game."

Those notes become either fixes or entries in [known-issues.md](known-issues.md).
