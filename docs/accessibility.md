# Accessibility

The collection is built for blind and low-vision players first, and for sighted players on the same hardware. This page explains the design rules, gives a checklist for reviewing a game, and describes an audio-only playtest.

## Principles

### 1. Sound is a first-class output, not an afterthought

A game should not merely "also make a noise". The sounds should carry the information a sighted player gets from the display: whose turn it is, what card was drawn, how many points were scored, whether an answer was right, and what the menu selection is.

Speech is used for words, menus, totals, and results. Tones are used for fast feedback and for information that has a natural pitch mapping, such as a column on a grid or a card value. Vibration is used where the controller can provide it.

### 2. Speech is used sparingly, because it cannot be interrupted

Once the micro:bit starts speaking, it must finish the phrase. A talkative menu would make every mode change slow. The programs therefore use speech for the things that matter: titles, player announcements, totals, results, and a few short comments. On-screen names, mode changes, and note previews often use a tone instead, so the player can keep moving.

### 3. Touch is a first-class input

The bare board's buttons, logo, and touch pins are findable without looking. The controller's four direction buttons and two fire buttons are even easier to find. A game should not require a gesture that is hard to perform reliably, and when it does, the guide should say so.

### 4. The display is monochrome and never the only channel

The LED grid is 5 by 5 single-colour LEDs. It cannot show colour. If the display uses a position, a bar, a letter, or a shape to mean something, there must be a sound or spoken equivalent. This is why Simon's four display bars are also four distinct tones, and why Flip 7's card marks are announced with tones and can be inspected one at a time.

### 5. Consistent controls reduce memory load

Fire 1 confirms. Fire 2 goes back or performs the secondary action. The direction buttons mirror the bare-board directions. When a game breaks the convention, the guide says so in the control table.

### 6. Destructive actions are deliberate

Resetting a high score, deleting a saved game, or wiping a sequence requires a confirmation that is different from the action that opened the prompt. The confirmation is usually "turn the display face down" or "press Joypad Down", and any other button cancels.

### 7. Saves are temporary

Only one program fits on the board at a time. A save lives in that program's filesystem and is erased when another program is flashed. The documentation should say this plainly instead of implying that saves can be managed like files on a computer.

### 8. Document the intentional trade-offs

An honest "this part is harder without sight" is more useful than an overstated claim. The trade-offs and the remaining real bugs are listed below and tracked in [known-issues.md](known-issues.md).

## Review checklist

Use this when adding a game or reviewing an existing one.

### Menus and navigation

- [ ] Every menu item can be identified without seeing the display.
- [ ] The current selection is announced or given a distinct tone when it changes.
- [ ] Menus wrap around, or the guide explains where they stop.
- [ ] There is a way back to the menu without unplugging the board.
- [ ] The game says what it is waiting for.

### Controls

- [ ] Every action has a physical control that can be found by touch.
- [ ] No action requires colour vision.
- [ ] No action requires reading text on the LED matrix.
- [ ] No action requires precise timing beyond what the game is about.
- [ ] If shake is required, the guide explains why and suggests the controller if it helps.
- [ ] If tilt is required, the guide explains why and suggests the controller if it helps.
- [ ] The controller mapping follows the shared vocabulary, or the exception is documented.
- [ ] The bare-board mapping follows the shared vocabulary, or the exception is documented.

### Feedback

- [ ] A correct answer has a distinct sound.
- [ ] A wrong answer has a distinct sound.
- [ ] A lost life or a bust has a distinct sound.
- [ ] A win has a distinct sound.
- [ ] Scores and totals can be read without the display.
- [ ] The sound cues are documented in a "What you hear" table.
- [ ] The tones are distinguishable at the micro:bit's volume.
- [ ] Speech is reserved for things that are worth waiting for.

### State and saves

- [ ] The game can be restarted without unplugging the board.
- [ ] A saved game announces that it is loading.
- [ ] A save can be cleared by reflashing the program.
- [ ] The guide says that flashing another program erases the save.
- [ ] A failed save produces an understandable message, not a silent crash.

### Hardware

- [ ] The game runs on a micro:bit V2.
- [ ] The game works with the V2's built-in speaker.
- [ ] The game works with the controller's buzzer.
- [ ] The game works with the controller's vibration motor where it uses it.
- [ ] The game does not set touch mode on pins that the controller uses for output.

## Audio-only playtest

This is the test that matters most. It takes about ten minutes per game.

1. **Prepare.** Use the V2's built-in speaker. If you are using the controller, plug the micro:bit in and power it on.
2. **Cover the display.** Put the board in a case, or place a piece of card over the LED matrix. Do not peek.
3. **Start the game.** Can you tell that it started? Can you tell what it is waiting for?
4. **Use every menu item.** Can you reach each one, identify it, and get back?
5. **Play a complete round.** Can you tell whose turn it is, what happened, and what your options are?
6. **Check the score.** Can you read the score, the lives, or the total without looking?
7. **Trigger a mistake.** Is the failure sound distinct from the success sound?
8. **Save, reset, and resume.** Does the game tell you what it loaded?
9. **Repeat with the controller.** Is every action reachable? Is anything easier or harder?
10. **Write down every moment you had to look.** Each one is either a bug to fix or a limitation to document.

A sighted helper can run the same script and compare notes. The goal is not to make the two experiences identical; it is to make the audio-only experience complete.

## Intentional trade-offs and real gaps

These are design choices or known limitations, not reasons to avoid the games.

| Area | What to expect |
| --- | --- |
| MicroFidget | Bare-board only by design; the controller does not fit the microphone and fidget games. |
| Vibration Challenge | The controller is heavily recommended. Without it, the strength becomes a pitch, which is a different experience. |
| Simon | The four modes are identified by a display bar and a tone, not a spoken name, so switching stays fast. |
| Composer | Note names are shown, not spoken; speaking every note would make editing slow. Navigate by pitch and semitone/octave steps. |
| Mastermind | On a bare board, shake is the submit control because every other input is already used. The controller's Fire 1 is the alternative. |
| Mastermind | Feedback style 0 is deliberately easier: you need the right set of symbols, not the right order. |
| 36 | Going over 30 attacks the next player with extra dice. Passing a leftover penalty to the next player is intentional. |
| Breakout | Fast and spatial, but fully sonified. It is playable if you are comfortable with fast audio games; the controller is the easier input. |
| Dice and card games | Individual faces are shown as letters, bars, or patterns and announced with tones, not spoken words, to keep turns quick. The stats or viewer actions give the counts. |
| All games | There is no pause. Most games only advance when you act; Breakout moves on a timer, but a pause was not part of the design. |
| All games | Speech is robotic and cannot be interrupted. The phonetic spellings in the source are tuned for it. |
| All games | Only one program and one save fit on the board. Flashing another program erases both. |

The remaining real bugs are listed in [known-issues.md](known-issues.md).

## Language

- Use "blind and low-vision players", not "the blind" as a noun.
- Say "a sighted player" rather than "a normal player".
- Describe what a control does, not what it looks like: "the large hole labelled 1", not "the left pad".
- Avoid "just", "simply", and "obviously". They add nothing and can make a hard step feel like a failure.
- Put the action first: "Press Fire 1 to deal", not "To deal, Fire 1 should be pressed".
- Keep sentences short. Screen readers pause at punctuation, not at line breaks.
