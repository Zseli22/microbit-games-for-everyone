# MicroFidget

Seven quick sensory challenges in one menu. A fidget toy, a reaction test, and a small arcade game, all controlled with the bare micro:bit.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 |
| Controller | Not supported |
| Speech | Yes, for menus, descriptions, scores, and results |
| Save | High scores, until another program is flashed |
| Difficulty | Easy to moderate |
| Hardware | micro:bit V2; uses the built-in speaker |

## What it is

MicroFidget is a menu of seven short activities. Some are pure fidgeting: mash a button, shake the board, tap the logo. Some test timing or reactions. Two use the microphone. The last one is a tiny game of keep-up.

Each activity has its own high score, and the board remembers them while MicroFidget stays on the board. The menu speaks the name of each activity, and a shake gives a spoken description.

## Before you play

- Use a micro:bit V2.
- The V2's built-in speaker is used. No headphones or external speaker are needed. Keep the board close, or use it in a quiet room.
- High scores survive a reset or unplug while this program stays installed. Flashing another program, or reflashing this one, erases them.

## Controls

| Action | Control |
| --- | --- |
| Next game | Button A |
| Start the selected game | Button B |
| Hear the description of the selected game | Shake the board |
| Hear the selected game's high score | Touch the logo |
| Reset the selected game's high score | Touch and hold the logo, then turn the display face down |
| Reset all high scores at startup | Hold Button A while the board starts, then follow the spoken prompt |
| Play the same game again after a result | Button B |
| Choose another game after a result | Button A |

There is no controller support in this version. MicroFidget is a bare-board program by design.

## How to play

### The menu

1. On startup, the board says "Select game" and shows a heart.
2. Press **Button A** to move through games 1 to 7. Each press plays a rising menu tone, and the display shows the game number.
3. Stop on a game for about a second. The board speaks its name.
4. **Shake** to hear a description of the game.
5. **Touch the logo** to hear the high score.
6. Press **Button B** to start. A three-two-one countdown plays, then the game begins.

### The seven games

**1. Mash it!**  
Press **Button A** as many times as you can in five seconds. Every press makes a short blip at a random pitch. Your score is the number of presses.

**2. Shake it!**  
Shake the board as hard as you can for five seconds. The pitch rises with the strength of the shake. Your score is the strongest shake the accelerometer registered.

**3. Tap it!**  
Tap the **logo** as many times as you can in five seconds. Each tap makes a short blip. Your score is the number of taps.

**4. Time check.**  
Press **Button A** to hear a reference tone of random length, between one and four seconds. Listen to how long it lasts. Then press and hold **Button A** for what you think is the same length, and release. The board tells you the reference length and your length in milliseconds, then gives you an accuracy percentage. A score of 100 means perfect.

**5. hurry up!**  
This is a reaction test with ten rounds. After a two-second pause, the display brightens and the tone rises through three steps: low, medium, and high. Press **Button A** as soon as you hear the highest step. Your score is the average reaction time in milliseconds, so **lower is better**. Pressing before the highest step adds a 1000 millisecond penalty for that round.

**6. Count and shout!**  
Press **Button A** to start. The board plays between 15 and 40 beeps at random intervals. Count them. After the beeps, a two-tone cue tells you to answer. Make one sound per beep you counted: clap, tap the table, or shout. The microphone stops after three seconds of silence, or you can press **Button A** to finish early. The board tells you how many sounds it detected and how many beeps there really were, then gives you an accuracy percentage.

**7. Micro Pong**  
Keep the marker away from the edges of the display. The marker moves one step at a time along the middle row. Press **Button A** when the marker is on the left side, and **Button B** when it is on the right side. Each good press scores a point and makes the rally a little faster. If the marker reaches an edge, the game ends.

## What you hear

| Sound | Meaning |
| --- | --- |
| A rising tone for each menu step | You moved to the next game |
| Spoken game name | Played about a second after you stop on a game |
| Spoken description | Played when you shake at the menu |
| Spoken high score | Played when you touch the logo at the menu |
| Three-note countdown, then a long high tone | The game is about to start |
| Short blips | A tap or button press registered |
| A rising or falling pitch | Shake strength, or the reaction-test step |
| A two-tone cue in Count and shout | Start making your sounds |
| A short five-note melody | The game ended and your score is being read |
| A longer rising fanfare | You set a new high score |
| Spoken "Press B to play again" | The result is over |

## Scoring and high scores

Each of the seven games has its own high score. For six of them, a higher score is better. For **hurry up!**, a lower reaction time is better; the default high score is 1000 milliseconds. The scores survive a reset or unplug while MicroFidget stays installed. Flashing another program, or reflashing this one, erases them.

At the end of a game, the board scrolls your score and speaks the result. If you beat the high score, it plays the longer fanfare and says "High score." Otherwise it plays the short melody.

### Reset one high score

1. At the menu, select the game.
2. Touch and hold the **logo**. The board scrolls the current high score and speaks it.
3. Keep holding. After a moment it plays three rising tones and says "Face down to confirm reset."
4. Turn the board over so the display faces the table. The score is reset.
5. Press **Button A** or **Button B** instead to cancel.

### Reset all high scores

1. Hold **Button A** while the board starts or while you press reset.
2. The board asks "Reset all high scores to 0?" and shows a pair of scissors.
3. Press **Button A** to arm the reset. It says "Face down to confirm reset."
4. Turn the display face down to confirm, or press **Button B** to cancel.

## Accessibility notes

- The menu is fully spoken, and every game has a spoken name and description.
- The important results are spoken. The display adds numbers and images for sighted players.
- **Shake** is used for descriptions. If shaking is difficult, a sighted helper can read the description from this guide instead.
- **Face down** is used for confirmations. The gesture is deliberate, so it is hard to trigger by accident.
- **Count and shout** needs a reasonably quiet room, because the microphone listens for loud sounds. In a noisy room, the count will be too high.
- **Time check** and **Count and shout** need audible sound. Use the built-in speaker and keep the board close.
- There is no pause. Pressing reset restarts the program.
- The controller is not supported, so all controls are on the board itself.

## Tips

- Use the built-in speaker and keep the board close in a noisy classroom.
- In **Count and shout**, one clean clap per beep is more reliable than shouting a number.
- In **Time check**, count "one thousand and one" style beats in your head to estimate the length.
- In **Micro Pong**, wait until the marker is clearly on the correct side. Pressing at the centre does nothing.
- The high-score reset is intentionally awkward. You cannot wipe a score with a single accidental touch.
