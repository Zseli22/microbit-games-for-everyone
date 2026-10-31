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

The board gives you a reference strength three times. Then it plays a test strength once. You decide whether the test is the same as the reference. If it is close, you score; if it is not, you lose a life.

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
4. Wait through a short pause.
5. The test pulse plays for about a second. **Press Fire 1 (or Button A) during the test pulse** to lock in your answer. You do not have to wait for the pulse to end; pressing stops it.
6. The board compares the test with the reference:
   - **Exact match:** 10 points.
   - **Close match:** 5 points.
   - **Too far away:** you lose a life.
7. If you are correct, the difficulty increases a little and you go back to step 1.
8. If you lose all 3 lives, the game ends and your score is read out.
9. Every 5 exact matches earns an extra life. They do not have to be in a row.

### What "close" means

The board treats a test as correct if it is within 100 steps of the reference, on a scale from 0 to 1023. An exact match is worth 10 points; anything else within 100 is worth 5.

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
| Three pulses | The reference strength |
| One longer pulse | The test strength |
| A short pause | Get ready to answer |
| Rising three-note phrase and a happy face | Correct |
| Two low tones and a sad face | Wrong; you lost a life |
| Six rising tones and a celebration image | Extra life |
| A long falling sweep and a noise burst | Game over |
| Counted beeps | The score, then the lives |
| A short vibration on the controller | The reference or test pulse itself |

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
- Do not wait for the test pulse to finish. Press as soon as you have a sense of it; the press itself locks in the value.
- Late in a good run, a value that is not exactly the reference can still be within the 5-point range. Listen for how close it feels, not just whether it matches.
