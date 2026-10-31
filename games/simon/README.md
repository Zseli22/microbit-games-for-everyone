# Simon

Repeat a growing sequence of four tones and directions. A memory game that works entirely by ear.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 |
| Controller | Optional |
| Speech | Yes, for comments after a mistake |
| Save | None |
| Difficulty | Moderate to hard |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

Simon plays a sequence of four tones, each paired with a direction and a bar of light on the display. You repeat the sequence by pressing the matching direction. Each successful round adds another step and speeds up a little. A mistake ends the run.

There are four modes: normal, random, reverse, and tricky. The mode changes how the sequence is built or how you have to answer it.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound and the vibration motor gives a short buzz on a wrong answer.
- There is no save. Each run starts fresh.

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Start a run | Button B (Right) |
| Change mode | Button A (Left) |
| Make the sequence faster | Touch the logo (Up) |
| Make the sequence slower | Touch pin 1 or pin 2 (Down) |
| Enter Up | Touch the logo |
| Enter Down | Touch pin 1 or pin 2 |
| Enter Left | Button A |
| Enter Right | Button B |

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Start a run | Joypad Right |
| Change mode | Joypad Left |
| Make the sequence faster | Joypad Up |
| Make the sequence slower | Joypad Down |
| Enter a direction | The matching direction button |

Press and hold a direction until you hear its tone. Release when the board has acknowledged it. A very short tap can be missed.

## How to play

1. On startup, the board plays a short demo: Up, Right, Down, Left.
2. At the menu, use **Up** and **Down** to set the speed. The default is the slowest setting. Up makes it faster; Down brings it back toward the default.
3. Use **Left** to change the mode. There are four modes, in this order:
   - **Normal** — one new tone is added each round.
   - **Random** — the whole sequence is replaced with a new random sequence each round. It is not cumulative.
   - **Reverse** — you hear the sequence forward and must enter it backwards.
   - **Tricky** — fake tones are inserted into the middle of the sequence. You must ignore them.
4. Press **Right** to start. The first sequence is one tone.
5. Listen to the sequence. Each tone is paired with a bar of light: Up is the top bar, Right is the right column, Down is the bottom bar, Left is the left column.
6. Repeat the sequence by pressing or holding the matching directions in order. Each correct press plays its tone and shows its bar.
7. If the whole sequence is correct, the board adds a step, speeds up, and plays the longer sequence.
8. If you press the wrong direction, the board plays a low buzz, vibrates if a controller is attached, and speaks a short comment. The run ends.

### The four modes in detail

**Normal.** The sequence grows by one random tone each round. This is the classic Simon game.

**Random.** The sequence length grows, but the contents are re-randomized every round. You cannot rely on remembering the previous round; listen to the whole sequence each time.

**Reverse.** The board plays the sequence forward. You enter it in reverse order. On the next round, the board adds a new tone to the original order and plays the whole thing forward again.

**Tricky.** From the third tone onward, the board may insert up to one fake for every three real tones. A fake is a full square on the display and a low A2 tone. It appears in the middle of the sequence, never as the first or last tone. Do not press anything for a fake; skip it. When you complete the round, the fakes are replaced with the real tones for the next round.

### Mode and speed tips

The mode is shown as a bar in one of four positions and played as a tone. It is not spoken, because speech cannot be interrupted and a spoken name would make every mode change slower. From a fresh start, the mode is Normal. Press **Left** once for Random, twice for Reverse, three times for Tricky, and four times to return to Normal.

The speed setting is remembered for the session. A failed run resets the current speed to the default, but your menu setting is still there when you start again.

## What you hear

| Sound | Meaning |
| --- | --- |
| Highest tone, top bar | Up |
| Second tone, right column | Right |
| Lowest tone, bottom bar | Down |
| Third tone, left column | Left |
| Very low A2 tone, full square | A fake in Tricky mode; ignore it |
| Short high beep | Speed increased |
| Short lower beep | Speed decreased |
| A tone when the mode changes | The mode's bar-position tone; the name is not spoken, so switching stays fast |
| A low buzz for about a second | You pressed the wrong direction |
| A short vibration | Wrong answer on the controller |
| Spoken comment | A reaction to your run; the comments get more impressed as the sequence gets longer |

The four direction tones are close together, especially Down and Left. A quiet room helps.

## Scoring and saves

There is no save. Your score is the length of the sequence you completed. The board does not scroll a number; the spoken comment tells you how well you did. A long sequence earns a more impressed comment.

Pressing reset starts a new run from the menu.

## Accessibility notes

- The game is designed for audio memory. The four directions have distinct tones and distinct positions on the display.
- The mode name is the main gap: it is not spoken. Use the press-count method above, or ask a sighted helper which bar is lit.
- The controller makes the directions physical and gives a vibration on a mistake. It is the easier input if you find the touch pins hard to locate.
- Press and hold each direction until you hear the tone. A quick tap may not register.
- There is no pause. Pressing reset ends the run.

## Tips

- Leave the speed at the default until you can reliably complete five or six steps.
- In Reverse mode, repeat the sequence backwards silently in your head before you start pressing.
- In Tricky mode, the fake is much lower than the four real tones. If a tone sounds like a buzz rather than a musical note, skip it.
- The mode stays the same after a failed run. If you want to go back to Normal, press Left until the top bar appears and you hear the highest mode tone, or press Left four times from a known mode.
