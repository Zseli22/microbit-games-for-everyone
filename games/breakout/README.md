# Breakout

Steer a ball around a five by five grid, collect blocks, and keep the ball from falling off the edge. A fast, sonified arcade game.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 |
| Controller | Recommended |
| Speech | No; positions and scores are tones |
| Save | Progress, until another program is flashed |
| Difficulty | Moderate to hard |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

A small arcade game on the micro:bit's 5 by 5 LED matrix. A ball moves around the grid. You influence its direction with tilt or the controller's four direction buttons. Blocks appear; landing on one collects it and scores a point. Every block collected spawns another. Every so often a powerup appears.

If the ball leaves the grid, it starts to fall. A warning arrow shows which edge, and a repeating tone tells you to push it back. While it falls, your health drains. If health reaches zero, you lose a life.

The game is fully sonified: the ball's column and row are played as two tones every time it moves, so you can follow it without the display.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound and the direction buttons give precise control.
- Progress is saved when you lose a life, not continuously. Flashing another program, or reflashing Breakout, erases it. See **Saving** below.

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Steer the ball | Tilt the board |
| Start the game | Button A |
| Read the block positions, then the status | Hold Button A |
| Use a teleport | Button B |

Tilt as if the board were a tray. Tilt the logo end down to move the ball up on the display; tilt it up to move the ball down. Tilt left to move the ball left; tilt right to move it right.

This feels natural in your hand: the logo is at the top, and tilting the top edge down makes the ball roll toward the top of the display. The accelerometer names the gesture from the board's point of view, so the code's "down" gesture is the one that moves the ball up.

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Steer the ball | Joypad Up, Down, Left, Right |
| Start the game | Fire 1 |
| Read the block positions, then the status | Hold Fire 1 |
| Use a teleport | Fire 2 |

The direction buttons match the screen: Up moves the ball up, Down moves it down, Left moves it left, and Right moves it right.

## How to play

1. The board shows your lives. You start with 3.
2. Press **Button A** (or **Fire 1**) to start. Four blocks appear. Each block's position is announced as a column tone followed by a row tone.
3. The ball starts in the centre and moves on a timer. Every move plays its column tone and then its row tone. Blocks are dimly lit; the ball is bright.
4. Tilt or press a direction to influence the next move. The ball still moves randomly, but it is much more likely to move in the direction you chose.
5. Land on a block to collect it. You score 1 point, or 2 while a multiplier is active. A sparkle plays, the block disappears, and a new block spawns with its position announced.
6. Every 100 points earns an extra life.
7. If the ball leaves the grid, it falls. A warning arrow shows the edge, and a repeating tone plays. Push the ball back:
   - If it fell off the top, press **Down** (or lift the top edge).
   - If it fell off the bottom, press **Up** (or lift the bottom edge).
   - If it fell off the left, press **Right** (or lift the left edge).
   - If it fell off the right, press **Left** (or lift the right edge).
   The idea is to push the ball back onto the grid. While it is falling, health drains. If health reaches zero, you lose a life.
8. After a lost life, the ball returns to the centre, the blocks are cleared, health returns to 100, and the score and lives carry over. If you still have lives, the game saves your score, lives, and speed.
9. When you run out of lives, the board resets the program.

### Powerups

When you collect a block, there is a small chance of a powerup. The chance increases as the game speeds up.

| Image | Powerup | Effect |
| --- | --- | --- |
| Christmas tree | Health | Adds 30 health. |
| X | Point multiplier | Adds 25 to the multiplier counter. Each block is worth 2 points while it lasts. |
| Square | Teleport | Adds one teleport. |
| Down arrow | Slow down | Increases the delay between moves for 25 moves, then restores it. |
| Up arrow | Speed up | Decreases the delay between moves for 25 moves, then restores it. |

The multiplier counts down by one on each move. When it reaches zero, a low tone plays. The speed powerups also count down; when the count reaches zero, the original speed returns.

### Stats

Press and hold **Button A** (or **Fire 1**) past the block positions:

- The first part of the hold plays each block's column tone and row tone, one block at a time. This tells you where the blocks are.
- Keep holding, and after the block readout the board reads your health, teleports, multiplier, and speed countdown using scrolling numbers and tone counts.

A quick tap only reads the block positions. Hold through the whole block readout to reach the status screen.

### Teleport

If you have at least one teleport, press **Button B** (or **Fire 2**). The ball jumps to a random block, collects it, and uses one teleport. This is a way to score without steering, and an emergency way to avoid a fall.

## Reading the grid

The five column tones, from left to right, are:

| Column | Tone |
| --- | --- |
| 1 (left) | C5 |
| 2 | D5 |
| 3 (centre) | E5 |
| 4 | F5 |
| 5 (right) | G5 |

The five row tones, from top to bottom, are the same five pitches. A position is announced as **column first, then row**. For example, the top-left corner is 523 then 523; the bottom-right corner is 784 then 784.

Block spawns use the same pattern one octave higher, from C6 to G6. Ball moves use C5 to G5. That is how you tell a new block from the ball.

## What you hear

| Sound | Meaning |
| --- | --- |
| Two tones, normal pitch | The ball moved; column first, then row |
| Two tones, higher pitch | A new block appeared; column first, then row |
| A burst of random high tones and pixels | You collected a block |
| A rising arpeggio | Health powerup |
| A long, busy jingle | Point multiplier |
| A noise sweep | Teleport powerup |
| A falling or rising sweep | Speed up or speed down |
| A repeated warning tone | The ball is falling; push it back |
| Six rising tones | Extra life |
| A low tone and a sad face | You lost a life |
| Counted beeps | A score, health value, or counter, read in hundreds, tens, and ones |
| A very low buzz | Zero |

## Scoring and saving

- Each block is worth 1 point, or 2 while the multiplier is active.
- Every 100 points earns an extra life.
- You start with 3 lives.
- When you lose a life and still have lives left, the game saves your score, lives, and current speed in the program's internal filesystem.
- If you reset or unplug while Breakout stays installed, the game announces the saved score and lives and continues at the saved speed.
- If you run out of lives, the board resets.
- Flashing another program, or reflashing Breakout, erases the save.

The save is written at the end of a life, not after every point. If you unplug the board in the middle of a life, you return to the last saved score when you start Breakout again.

## Accessibility notes

- The grid is sonified with five column tones and five row tones. With practice, you can follow the ball and the blocks by ear.
- The game is fast and spatial, but much of it is carried by the position tones. It is playable if you are comfortable with fast audio games. The controller's direction buttons are easier than tilting.
- The stats readout is the main way to get an overview of the board. Use it often, especially after a new block appears.
- Health is not announced continuously. The falling warning tells you that health is draining; use the stats readout to check the exact value.
- There is no speech. Scores and counters are tone counts, using the hundreds, tens, and ones code.
- The save/resume system means a lost life does not wipe your progress.
- There is no pause. Pressing reset restarts the program and loads the last save.

## Tips

- Use the controller. The direction buttons are much easier than tilting, especially when the ball is falling.
- Read the block positions after each new spawn. The higher-pitched pair is the new block.
- Save a teleport for an emergency. It can rescue a run when the ball is about to fall.
- The multiplier makes every block worth 2 points. Collect as many as you can while it lasts.
- The down-arrow powerup slows the game down. It is often more useful than the up-arrow powerup.
- When the ball falls, push it back toward the centre. Do not press the direction it fell; press the opposite direction.
- The speed slowly increases as you play. The game clamps it at a minimum, so it never becomes impossible.
