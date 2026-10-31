# 36

A six-dice push-your-luck game. Aim for a total of 30, because under is a loss and over 30 lets you attack the next player.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 to 10, any mix of humans and computers |
| Controller | Optional |
| Speech | Yes, for players, turns, and results |
| Save | Yes, until another program is flashed |
| Difficulty | Moderate; the scoring takes a round to learn |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

Each player starts with 36 points. On your turn you roll six dice, keep the ones you want, and re-roll the rest. When all six are kept, the total decides what happens. Exactly 30 is safe. Under 30 costs you the shortfall. Over 30 starts a bonus round in which extra dice are subtracted from the next player's score.

In a multiplayer game, you are trying to be the last player with points left. In a solo game, you are trying to reach 54 points.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- The game supports solo play and games with up to 10 players.
- The game saves after each turn. If you stop in the middle of a turn, you return to the end of the previous turn. Flashing another program, or reflashing 36, erases the save.

## Controls

### Setup

| Action | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| Add a human player | Button A | Joypad Left |
| Add a computer player | Button B | Joypad Right |
| Start the game | Shake the board | Fire 1 |

### During a turn

| Action | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| Roll, or commit the kept dice | Button A to roll; Shake to commit | Fire 1 |
| Cycle through the dice | Button A | Joypad Left or Right |
| Keep the selected die | Button B | Fire 2 |
| Show every player's score | Button B, when not re-rolling | Fire 2, when not re-rolling |
| Show the current total | Touch the logo | Joypad Up |
| Switch between keep mode and undo mode | Touch pin 1 or pin 2 | Joypad Down |

The same physical control has two roles in some places. Button B (or Fire 2) keeps a die while you are re-rolling, and shows all scores when you are not. Button A (or Fire 1) rolls at the start of a turn, and commits the kept dice during a re-roll.

## How to play

### Set up the players

1. The board announces "Thirty-Six" and says "Select players."
2. Press **Button A** (or **Joypad Left**) to add a human. The display shows H and plays a high two-note phrase.
3. Press **Button B** (or **Joypad Right**) to add a computer. The display shows C and plays a lower two-note phrase.
4. Add between 1 and 10 players.
5. Shake the board (or press **Fire 1**) to start. If there is more than one player, a wheel spins and the board announces who goes first. If there is one player, it says "Starting one player game." On a bare board, the game can also start automatically when nine players have been added.

### A turn

1. Press **Button A** (or **Fire 1**) to roll all six dice. Each die is shown and played as a tone.
2. Choose which dice to keep:
   - **Cycle** through the unkept dice with Button A (or Joypad Left and Right).
   - **Keep** the selected die with Button B (or **Fire 2**). It is removed from the re-roll pool and added to your kept dice.
   - **Undo a keep:** touch pin 1 or pin 2 (or press **Joypad Down**) to switch to undo mode. The board plays a short high beep. Cycle to a kept die and press Button B (or **Fire 2**) to return it to the pool. Press the same control again to switch back to keep mode.
3. Shake the board (or press **Fire 1**) to commit the kept dice. The unkept dice are re-rolled. You must have kept at least one die before you can commit.
4. Repeat steps 2 and 3 until all six dice are kept. The round then scores automatically.
5. The board announces the total, the score change, and whose turn is next.

### The scoring rule

Your total is the sum of all six kept dice.

| Total | Result |
| --- | --- |
| Exactly 30 | Safe. Your score does not change. |
| Under 30 | You lose the difference. A total of 24 costs 6 points. |
| Over 30 | A bonus round starts. Extra dice are subtracted from the next player's score in a multiplayer game, or added to your score in a solo game. |

### The bonus round

The bonus round starts only after all six dice are kept, and only if the final total is over 30.

1. The board rolls a fresh set of six dice. The dice you kept are not reused.
2. The target number is **your total minus 30**. For example, a total of 34 has a target of 4.
3. Every die showing the target is kept aside. The other dice are re-rolled, and you keep every new match. This repeats until a roll produces no match.
4. The bonus value is **the target number times the number of matching dice**.
5. In a multiplayer game, that value is **subtracted from the next player's score**, not yours. If it takes them below zero, they are out, and any leftover passes to the player after them. This is intentional: a big overshoot can take someone down with you.
6. In a solo game, the same value is **added to your score**, because there is no opponent to attack.

Examples:

- Your total is 34, so the target is 4. Over the bonus rolls you collect three 4s. The bonus is 4 × 3 = 12. The next player loses 12 points.
- Your total is 36, so the target is 6. You collect two 6s. The bonus is 12 points to the next player.
- Your total is 31, so the target is 1. You collect one 1. The bonus is 1 point.
- If no die matches the target, the bonus does nothing.

The bonus is an attack, not a penalty on you. In a solo game it is a reward instead.

### Losing points and passing the leftover

If a penalty is larger than your remaining score, you are knocked out. The leftover is subtracted from the next player. This is intentional: a bad round can ruin someone else's score as well as your own.

### Winning

- **Multiplayer:** players start at 36. A player whose score reaches 0 is out. The last player with points left wins.
- **Solo:** you start at 36. Reach 54 points to win. If your score reaches 0, you lose.

### The current total

Touch the logo (or press **Joypad Up**) to hear the current sum of kept and unkept dice. The unkept dice will change when you re-roll, so this is a provisional total, not the final score.

### All scores

Press **Button B** (or **Fire 2**) when you are not re-rolling to hear every player's score. Each score is scrolled and counted with tones.

## Reading the numbers

Scores and totals are counted with two tones:

| Tone | Value |
| --- | --- |
| Middle beep (G5) | 10 |
| Low beep (C5) | 1 |
| Very low buzz (C3) | Zero |

For example, 34 is three middle beeps and four low beeps. There is no hundreds tone; the scores stay below 100.

## What you hear

| Sound | Meaning |
| --- | --- |
| A run of dice faces and tones | The dice are rolling |
| A tone for each die | Its value, from 1 to 6 |
| Two high tones | A die was kept |
| Two lower tones | A die was unkept |
| A short high beep | Switched to undo mode |
| A short low beep | Switched back to keep mode |
| A rising sweep | Your score changed; the pitch moves from the old score to the new one |
| A long celebratory jingle, then more dice | The bonus round is starting |
| A descending sweep and a low tone | A player was knocked out |
| A fanfare and speech | A player won |
| Spoken "next round" or a player number | The turn is passing |
| Counted beeps | A score or total |

## Scoring and saving

- Start at 36 points.
- Exactly 30: no change.
- Under 30: lose the shortfall.
- Over 30: roll extra dice for the target (total minus 30). The bonus is the target times the number of matches. In multiplayer it is subtracted from the next player; in solo it is added to your score.
- A leftover penalty passes to the next player when someone is knocked out. This is intentional.
- Solo: reach 54 to win, or 0 to lose.
- Multiplayer: last player with points above 0 wins.
- The game saves after each turn in its internal filesystem. It stores the players, their scores, and the current player. Flashing another program, or reflashing 36, erases the save.
- On startup, if a save exists, the board asks "Would you like to resume your saved game?"
  - **Button A** (or **Fire 1**) loads it.
  - **Button B** (or **Fire 2**) asks to delete it. Turn the display face down (or press **Joypad Down**) to confirm.

## Accessibility notes

- Speech announces the players, the turn changes, when a player is out, and the winner.
- Dice values are tones and faces, not spoken words. The tone for each die tells you its value.
- Scores and totals are counted as tens and ones. Learn the two-tone code above.
- The controller gives each action a separate physical button. It is the easier input; the bare-board layout uses Button B for two different things depending on the phase.
- The keep/undo mode is announced with a short high or low beep, so you know which mode you are in.
- The scoring rule is unusual. Read the bonus examples above before your first game.
- There is no pause. Pressing reset returns to the last save while 36 stays installed.

## Tips

- Aim for exactly 30. It is the only total that changes nothing.
- Going over 30 is an attack on the next player. A higher target is worth more per match, so a total close to 36 can be a strong attack.
- In a solo game, the same bonus adds to your score, so a controlled overshoot is a way to climb toward 54.
- Keep at least one die before committing. Committing with no new keeps just re-rolls the same number of dice.
- Use undo mode to fix a mistaken keep before you commit.
- In multiplayer, survival matters more than a big score. Do not take a risk that could take you to zero unless you can take someone with you.
- Check the current total before committing. It includes unkept dice, so treat it as a preview, not a promise.
