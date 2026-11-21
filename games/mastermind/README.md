# Mastermind

Break a hidden code. Choose the alphabet size, the code length, and how much feedback you get after each guess.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 |
| Controller | Optional |
| Speech | Yes, for settings and results |
| Save | None |
| Difficulty | Easy to hard, depending on the settings |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

A small Mastermind puzzle. The board picks a secret code from a set of symbols. You build a guess one position at a time and submit it. The board tells you how many symbols are correct, or which positions are right, depending on the feedback style you chose.

The default game uses eight symbols, a four-symbol code, and the simplest feedback. You can make it easier or harder before you start.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- There is no save. Each game starts fresh.

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Left, or start from the menu | Button A |
| Right, or next setting | Button B |
| Up, or increase a value | Touch the logo |
| Down, or decrease a value | Touch pin 1 or pin 2 |
| Submit a guess | Shake the board |

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Left, or start from the menu | Joypad Left |
| Right, or next setting | Joypad Right |
| Up, or increase a value | Joypad Up |
| Down, or decrease a value | Joypad Down |
| Submit a guess | Fire 1 |

## How to play

### Choose the settings

1. On startup, the board says "Welcome to Mastermind" and shows a heart. The first setting (**Available symbols**) is already selected.
2. Press **Button A** (or **Joypad Left**) to start with the current settings. The board says "Begin."
3. Press **Button B** (or **Joypad Right**) to move to the next setting. The board speaks the setting name and its current value.
4. Press **Up** or **Down** to change the current setting. The board speaks the new value.

The three settings are:

| Setting | Range | Default | What it does |
| --- | --- | --- | --- |
| Available symbols | 5 to 15 | 8 | How many different symbols the code can use. Symbols are 0 to 9, then A to E. |
| Length of code | 3 to 5 | 4 | How many symbols are in the secret code. |
| Game difficulty | 0 to 2 | 0 | How much feedback you get after each guess. |

### The feedback styles

**Style 0 — set only.** This is the easier variant. After each guess, the board tells you how many of your symbols appear somewhere in the code. It does not say which positions are right, and you win by finding the correct set of symbols, in any order. One high beep plays for each correct symbol, and a bar appears on the top row.

**Style 1 — per position.** The board checks every position:
- Top row and a high beep: the right symbol in the right place.
- Middle row and a lower beep: the right symbol, but in the wrong place.
- Bottom row and a low buzz: the symbol is not in the code.

This is the clearest style for audio play.

**Style 2 — counts.** The board tells you how many symbols are exactly right and how many are in the code but in the wrong place. It does not say which positions they are. Exact matches play high beeps on the top row; misplaced matches play lower beeps on the middle row.

### Build and submit a guess

1. The first position is selected. Press Up or Down to change its symbol; the display and the symbol's tone confirm the change.
2. Press **Left** or **Right** to move between positions. At the first or last position, the board buzzes instead of wrapping.
3. Press **Up** or **Down** to change the symbol at the selected position. At the lowest or highest symbol, the board buzzes.
4. Shake the board (or press **Fire 1**) to submit.
5. The board shows your whole guess, then gives feedback.
6. If the guess is not correct, you return to editing. The guess stays as you left it, so you can adjust one position at a time.

### The rules

- The secret code uses each symbol at most once.
- Your guess may not contain duplicates. If you submit a duplicate, the board says "No duplicates allowed" and returns you to the guess.
- In styles 1 and 2, you win when every position matches the secret code.
- In style 0, you win when your guess contains the same set of symbols as the code. Order does not matter; that is what makes it the easier variant.
- The board counts your guesses and tells you how many it took.

## What you hear

| Sound | Meaning |
| --- | --- |
| A tone for each symbol | The symbol's pitch: 0 is the lowest, then 1 to 9, then A to E |
| A short low buzz | You hit the first or last position, or the lowest or highest symbol |
| A high beep (C7) and top-row light | An exact match |
| A middle beep (C5) and middle-row light | A correct symbol in the wrong position |
| A low buzz (C3) and bottom-row light | A symbol that is not in the code |
| A neutral face and a low buzz (C3) | No symbols matched at all |
| An X, two low tones, and speech | You submitted duplicates |
| A rising fanfare and speech | You broke the code |
| Spoken setting names and values | While you change the settings |
| Spoken guess count | How many guesses you used |

The symbol tones are a rising scale, so they are easy to follow with practice.

## Scoring and saves

There is no score file. The game reports the number of guesses it took to break the code. A lower number is better.

There is no save. The settings are variables in the program, so pressing reset returns them to their defaults. Choose them again after a reset.

## Accessibility notes

- The settings are spoken, and the feedback has distinct tones. Style 1 is the most informative for audio play; style 2 is a good middle ground.
- On a bare board, submitting a guess requires a shake because every other control is already used. The controller's Fire 1 is the alternative.
- The position and symbol limits buzz instead of wrapping, so you always know when you have reached an end.
- The secret code is never spoken, of course. The feedback is the only clue.
- There is no pause. Pressing reset starts over.
- The duplicate check is spoken, so you are not left wondering why a guess was rejected.

## Tips

- The first guess starts as all 0s. If you need to confirm the 0 tone, press Up and then Down on a position to hear it.
- Start with 5 available symbols and a code length of 3. Increase the symbols before increasing the length.
- Use style 1 first. It tells you exactly which positions are right, which makes the logic much easier to follow.
- In style 1, a middle beep means the symbol belongs somewhere else. Move it rather than replacing it.
- In style 2, keep track of the exact and misplaced counts. A guess with four exact and zero misplaced is a win.
- In style 0, order does not matter. Use it as the easier variant when you want to focus on finding the right symbols.
- Do not repeat a symbol in a guess. The board rejects duplicates, and the secret code has no duplicates either.
