# Zombie Dice

The push-your-luck dice game: roll brains, dodge shotguns, and bank before you bust. Play with friends or computer opponents.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 2 to 10, any mix of humans and computers |
| Controller | Optional |
| Speech | Yes, for players, turns, and the winner |
| Save | Yes, until another program is flashed |
| Difficulty | Easy |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

Zombie Dice is a press-your-luck game. On your turn, you roll three dice. Brains are points, shotguns are danger, and runners go back into the cup. Keep rolling to collect more brains, or bank what you have before the third shotgun ends your turn and takes the unbanked brains with it.

The first player to reach 13 points triggers the final round. Everyone else gets one more turn, and the highest score wins.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- You need at least two players. Add humans, computers, or both.
- The game saves after each turn. If you stop in the middle of a turn, you return to the end of the previous turn. Flashing another program, or reflashing Zombie Dice, erases the save.

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Add a human player | Button A |
| Add a computer player | Button B |
| Start the game | Shake the board |
| Roll the dice | Button A |
| Bank your brains | Button B |
| Hear your turn stats | Touch the logo |
| Hear every player's score | Touch pin 1 or pin 2 |

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Add a human player | Joypad Left |
| Add a computer player | Joypad Right |
| Start the game | Fire 1 |
| Roll the dice | Fire 1 |
| Bank your brains | Fire 2 |
| Hear your turn stats | Joypad Up |
| Hear every player's score | Joypad Down |

## How to play

### Set up the players

1. The board announces "Zombie Dice" and says "Select players."
2. Press **Button A** (or **Joypad Left**) to add a human. The display shows H and plays a high two-note phrase.
3. Press **Button B** (or **Joypad Right**) to add a computer. The display shows C and plays a lower two-note phrase.
4. Add between 2 and 10 players.
5. Shake the board (or press **Fire 1**) to start. A wheel spins, then the board announces which player goes first.

On a bare board, the game can also start automatically when nine players have been added. You can still add a tenth player if you are quick, but the automatic start is there for large groups.

### A turn

1. The board shows a heart when it is your turn.
2. Press **Button A** (or **Fire 1**) to roll.
3. Three dice come out of the cup. Each die is green, yellow, or red, announced by a tone and a letter on the display.
4. Each die shows a face:
   - **Brain** — set aside. It is worth one point if you bank.
   - **Runner** — goes back into the cup and may be rolled again.
   - **Shotgun** — set aside. Three shotguns end your turn.
5. After the roll, choose:
   - **Roll again:** Button A (or **Fire 1**). The runners and any new dice are rolled.
   - **Bank:** Button B (or **Fire 2**). Your brains are added to your score, and the turn passes to the next player. You can only bank if you have at least one brain.
6. If you roll a third shotgun, you bust. You lose all the brains you have not banked, and the turn passes on.
7. When a player reaches 13 points, the final round begins. Every other player gets one more turn. The highest score wins.

### The dice

There are 13 dice in the cup:

| Die type | Dice | Faces |
| --- | --- | --- |
| Green | 6 | 3 brains, 2 runners, 1 shotgun |
| Yellow | 4 | 2 brains, 2 runners, 2 shotguns |
| Red | 3 | 1 brain, 2 runners, 3 shotguns |

Green is safest, red is most dangerous. The board cannot show colour, so the display shows **G**, **Y**, or **R**, and a different waveform and tone identify the type.

### Turn stats

Touch the logo (or press **Joypad Up**) to hear the current turn:

- The board shows a brain icon and plays one high tone per brain, then scrolls the count.
- It shows a skull and plays one low tone per shotgun, then scrolls the count.
- It shows a runner and plays a footstep for each die still in your hand, then scrolls the count.

This is the main way to check your progress without reading the display.

### All scores

Touch pin 1 or pin 2 (or press **Joypad Down**) to hear every player's score. For each player, the board scrolls the score and plays one high beep per point.

### Computer players

Computer players take their turns automatically. They bank when they have two shotguns and more than one brain; otherwise they roll. In the final round, they bank if banking would beat the current leader.

## What you hear

| Sound | Meaning |
| --- | --- |
| Spoken "Zombie Dice" | The title |
| High two-note phrase | A human player was added |
| Lower two-note phrase | A computer player was added |
| Wheel clicks and a noise burst | The starting player is being chosen |
| A noise sweep, then a die-type tone | The dice are rolling; green is a triangle, yellow a square, red a sawtooth |
| A rising tone and a Pac-Man image | A brain |
| Footstep pairs and a running figure | A runner |
| A descending tone and a skull | A shotgun |
| Two very low tones and a sad face | You rolled the third shotgun and busted |
| A rising high beep for each point | Brains are being banked |
| A happy face and a five-note fanfare | The bank is complete |
| A six-note phrase and speech | The final round begins |
| A long fanfare and speech | The winner |
| Spoken player numbers | Whose turn it is |
| Spoken load prompt | A saved game is available |

## Scoring and saving

- Each banked brain is one point.
- Unbanked brains are lost on a bust.
- The first player to reach 13 points starts the final round.
- After the final round, the highest score wins. If two players tie, the earliest player in the list wins.
- The game saves after each turn in its internal filesystem. It stores the players, their scores, the current player, and whether the final round has started. Flashing another program, or reflashing Zombie Dice, erases the save.
- On startup, if a save exists, the board asks "Would you like to resume your saved game?"
  - **Button A** (or **Fire 1**) loads it.
  - **Button B** (or **Fire 2**) asks to delete it. Turn the display face down (or press **Joypad Down**) to confirm.
  - Any other action leaves the save alone.
- Loading announces each player's score and whose turn it is.

The save is written at the end of a turn. If you stop in the middle, the current turn's unbanked brains are not saved.

## Accessibility notes

- Speech announces the players, whose turn it is, the final round, and the winner.
- Individual dice faces are icons plus tones, not spoken words. Learn the mappings above, or use the turn stats to hear the counts.
- The three die types use different waveforms as well as different pitches, so they are distinguishable by ear. The display uses G, Y, and R.
- The turn-stats and all-scores actions give you the numbers without the display.
- The controller gives every action its own physical button. It is the easier input for a group.
- There is no solo mode. You need at least two players.
- There is no pause. Pressing reset returns to the last save.

## Tips

- Bank early if you have two shotguns. The third one ends the turn and takes your brains.
- Brains only count when you bank. A big roll is tempting, but a bust gives you nothing.
- Green dice are safer; red dice are riskier. If the cup is low on green dice, be more careful.
- Use turn stats after every roll until you can track the shotguns by ear.
- In the final round, check the leader's score. If you are ahead, bank; if you are behind, you may need to push.
- Computer players are cautious with two shotguns. They will bank rather than risk a third.
