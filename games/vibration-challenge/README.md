# Vibration Challenge

Match the strength of a vibration. With the controller, you feel it; without one, you hear the same strength as a pitch.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 |
| Controller | Strongly recommended |
| Speech | No; score and lives are read as tone counts |
| Save | None |
| Difficulty | Easy at first, then harder |
| Hardware | micro:bit V2 and the Kitronik :GAME Controller (heavily recommended), or a bare micro:bit V2 |

## What it is

The board gives you a reference strength three times. Then it plays a continuous stream of test pulses, one after another. Ignore pulses that do not match, and press the button during a pulse that matches the reference. If it matches or is close enough, you score; if it is too far away, you lose a life.

With the controller, both signals are vibrations from the motor. Without the controller, both signals are tones, and the strength becomes pitch. The game is the same; the sensation is different.

## Before you play

- Use a micro:bit V2.
- The controller is heavily recommended. It provides the vibration motor and the buzzer.
- Without the controller, the V2's built-in speaker plays the pitch. The "vibration" is then a tone.
- There is no save. Each session starts with 3 lives and 0 points.

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Start a round, or lock in your answer | Button A |
| Hear the score and remaining lives | Button B |

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Start a round, or lock in your answer | Fire 1 |
| Hear the score and remaining lives | Fire 2 |

## How to play

1. The board shows your remaining lives. You start with 3.
2. Press **Fire 1** (or **Button A**) to begin a round.
3. The board gives the reference strength three times, with a short gap between each pulse.
4. Wait through a short pause (about 1.5 seconds).
5. The board begins playing a **continuous stream of test pulses**, one after another, with a brief gap between each pulse. Each pulse is either the exact reference or a random wrong strength.
6. **Ignore pulses that do not match.** Letting a pulse finish without pressing carries no penalty; the next test pulse simply plays.
7. When you feel or hear a pulse that matches the reference, **press Fire 1 (or Button A) during that pulse** to lock in your answer. Pressing stops the pulse immediately.
8. The board compares the locked-in pulse with the reference:
   - **Exact match:** 10 points.
   - **Close match:** 5 points.
   - **Too far away:** you lose a life.
9. After a correct answer, the board scrolls and tone-counts the points you earned (10 or 5), increases the difficulty slightly, and returns to step 1.
10. Every 5 exact matches earns an extra life. They do not have to be in a row.
11. If you lose all 3 lives, the game ends, your final score is read out, and the session resets.

### What "close" means

The board treats a locked-in pulse as correct if it is within 100 steps of the reference, on a scale from 0 to 1023. An exact match is worth 10 points; anything else within 100 is worth 5.

Early in a run, wrong pulses are kept at least 200 steps away from the reference, so every correct answer is an exact 10-point match. That gap shrinks by 10 after each correct answer, so 5-point close matches only become possible after 11 correct answers.

### How the difficulty increases

After each correct answer:

- The reference strength can be lower. At first it is between 900 and 1023; over time the lower end drops toward 200.
- The test pulse gets shorter, from about one second down to about a third of a second.
- The chance that the test is exactly the reference drops.
- Wrong test values get closer to the reference, so they are harder to tell apart.

The game gets harder only when you succeed. A wrong answer costs a life but does not increase the difficulty.

## Reading the score and lives

There is no speech. The board counts the score and lives with tones:

| Tone | Value |
| --- | --- |
| High beep (D6) | 100 |
| Middle beep (G5) | 10 |
| Low beep (C5) | 1 |
| Very low buzz (C3) | Zero |

For example:

- A score of 35 is three middle beeps and five low beeps.
- A score of 120 is one high beep and two middle beeps.
- A score of 0 is one very low buzz.

When you press the stats button, the board reads the **score** first, then the **lives**.

The display also scrolls the number and shows the lives, for sighted players.

## What you hear and feel

| Signal | Meaning |
| --- | --- |
| Three short pulses | The reference strength |
| A short pause | Get ready for the test stream |
| Repeated longer pulses | Test pulses; ignore non-matches and press during a match |
| Rising three-note phrase (C6, G6, C7) and a happy face | Correct, followed by tone-counted points (10 or 5) |
| Two low tones (C3, G#2) and an X | Wrong; you lost a life |
| Six-note celebration melody and a celebration face | Extra life |
| A long falling sweep (C7 to C4), a noise burst, and a sad face | Game over |
| Counted beeps | Points earned, or your score then remaining lives |
| Vibration pulses on the controller | The reference and test strengths |

With the controller, the strength is the **intensity** of the vibration, not its pitch. With a bare board, the strength is the **pitch** of the tone.

## Scoring and saves

- Exact match: 10 points.
- Close match: 5 points.
- Wrong: no points and one life lost.
- Extra life: every 5 exact matches.
- The game ends at 0 lives. The score is read out, then the game resets to 3 lives and 0 points.

There is no save. Restarting the program starts a fresh session.

## Accessibility notes

- This is the most tactile game in the collection. With the controller, it needs no screen and no speech; the motor is the whole signal.
- Without the controller, it becomes a pitch-matching game. It is still playable, but the name is misleading. A quiet room helps you hear the pitch.
- The score and lives are tone counts, not speech. Learn the hundreds, tens, and ones code above. The stats button reads score first, then lives.
- Pressing the answer button during the test pulse stops the pulse. You do not need to time the press to the end.
- There is no pause. Pressing reset ends the session.

## Tips

- Hold the controller firmly. The motor is inside the case, and a loose grip makes small differences harder to feel.
- In bare-board mode, listen to the pitch, not the volume. The tone's frequency is the strength.
- Use the stats button before you start if you are not sure how many lives you have.
- Do not rush to press on the first test pulse. You can let as many wrong pulses pass as you need until a matching one comes around.
- Once you recognize a match, press right away during that pulse; pressing stops it and locks in your answer.
- Late in a good run (after 11 correct answers), a non-exact pulse can still land within the 5-point close range. Listen or feel for how close it is, not just whether it is exact.
