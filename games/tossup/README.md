# Tossup

A push-your-luck dice game: collect green dice, avoid red, and bank before you bust.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 to 10, any mix of humans and computers |
| Controller | Optional |
| Speech | Yes, for players, the target, turns, and the winner |
| Save | Yes, until another program is flashed |
| Difficulty | Easy to moderate |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

Each turn you roll a pool of dice. Green dice add one point each to your unbanked total. Yellow dice do nothing. Red dice are dangerous: if a roll contains no green die and at least one red die, you bust and lose the points you have not banked.

You can bank at any time to add your unbanked total to your score. The first player to reach the target score triggers the final round; the highest score wins. In a solo game, reach the target to win.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- You can play solo or with up to 10 players.
- The game saves after each turn. If you stop in the middle of a turn, you return to the end of the previous turn. Flashing another program, or reflashing Tossup, erases the save.

## Controls

### Setup

| Action | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| Add a human player | Button A | Joypad Left |
| Add a computer player | Button B | Joypad Right |
| Start the game | Shake the board | Fire 1 |
| Raise the target by 10 | Touch the logo | Joypad Up |
| Lower the target by 10 | Touch pin 1 or pin 2 | Joypad Down |
| Hear the target | Turn the display face down | Fire 2 |

### During a turn

| Action | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| Roll the dice | Button A | Fire 1 |
| Bank your points | Button B | Fire 2 |
| Hear the unbanked total | Touch the logo | Joypad Up |
| Hear every player's score | Touch pin 1 or pin 2 | Joypad Down |

## How to play

### Set up the players and the target

1. The board announces "Tossup" and says "Select players."
2. Press **Button A** (or **Joypad Left**) to add a human. The display shows H and plays a high two-note phrase.
3. Press **Button B** (or **Joypad Right**) to add a computer. The display shows C and plays a lower two-note phrase.
4. Add between 1 and 10 players.
5. Set the target score. The default is 100. Touch the logo (or press **Joypad Up**) to raise it by 10; touch pin 1 or pin 2 (or press **Joypad Down**) to lower it by 10, down to a minimum of 50.
6. Turn the display face down (or press **Fire 2**) to hear the current target.
7. Shake the board (or press **Fire 1**) to start. If there is more than one player, a wheel spins and the board announces who goes first. If there is one player, it says "Starting one player game." On a bare board, the game starts automatically when 10 players have been added.

### A turn

1. The display shows the last digit of your unbanked total.
2. Press **Button A** (or **Fire 1**) to roll. The number of dice depends on your total:
   - At 0, you roll 10 dice.
   - At 1, you roll 9.
   - At 2, you roll 8.
   - This continues down to 1 die at 9.
   - At 10, you are back to 10 dice, and the pattern repeats for 20, 30, and so on.
3. Each six-sided die has three green faces, two yellow faces, and one red face:
   - **Green** adds 1 point. The display shows a bar at the top.
   - **Yellow** does nothing. The display shows a bar in the middle.
   - **Red** is dangerous. The display shows a bar at the bottom.
4. If the roll has **no green die and at least one red die**, you bust. You lose the unbanked total and the turn passes on.
5. If the roll has at least one green die, every green die adds 1 point. Red dice in the same roll do not bust you.
6. If the roll has only yellow dice, nothing happens. You can roll again.
7. Press **Button B** (or **Fire 2**) to bank. Your unbanked total is added to your score, and the turn passes on. You can only bank if your total is above zero.
8. The next roll uses a fresh pool of dice. Leftover yellow and red dice are not kept.

### The target and the final round

- In a solo game, reach the target score to win.
- In a multiplayer game, the first player to reach the target starts the final round. Every other player gets one more turn, then the highest score wins.
- If two players tie for the highest score, the earliest player in the list wins.

### Hearing the numbers

Touch the logo (or press **Joypad Up**) to hear your unbanked total. Touch pin 1 or pin 2 (or press **Joypad Down**) to hear every player's score.

## Reading the dice and the score

The display cannot show colour, so the three die types use bar positions and tones:

| Die type | Display | Tone |
| --- | --- | --- |
| Green | Top bar | C6 |
| Yellow | Middle bar | C5 |
| Red | Bottom bar | C4 |

Scores and totals are counted with three tones:

| Tone | Value |
| --- | --- |
| High beep (D6) | 100 |
| Middle beep (G5) | 10 |
| Low beep (C5) | 1 |
| Very low buzz (C3) | Zero |

For example, 34 is three middle beeps and four low beeps. 120 is one high beep and two middle beeps.

## What you hear

| Sound | Meaning |
| --- | --- |
| Spoken "Tossup" | The title |
| High two-note phrase | A human player was added |
| Lower two-note phrase | A computer player was added |
| Wheel clicks and a noise burst | The starting player is being chosen |
| A run of random tones with a fading echo | The dice are rolling |
| A tone for each die | Its type: green C6, yellow C5, red C4 |
| Six-note celebration melody and a smile | Every die in the roll was green |
| Two low tones and a sad face | You busted |
| A rising tone for each point, then counted beeps | You banked |
| A six-note phrase and speech | The final round begins, or the score to beat is raised |
| A fanfare and speech | A player won |
| Spoken target | When you ask for the target |
| Spoken player numbers | Whose turn it is |
| Counted beeps | A score or total |

## Scoring and saving

- Green die: 1 point.
- Yellow die: no effect.
- Red die: bust only if the roll has no green die.
- Bank: add the unbanked total to your score.
- Solo: reach the target to win.
- Multiplayer: first to the target starts the final round; highest score wins.
- The game saves after each turn in its internal filesystem. It stores the players, their scores, the target, the current player, and whether the final round has started. Flashing another program, or reflashing Tossup, erases the save.
- On startup, if a save exists, the board asks "Would you like to resume your saved game?"
  - **Button A** (or **Fire 1**) loads it.
  - **Button B** (or **Fire 2**) asks to delete it. Turn the display face down (or press **Joypad Down**) to confirm.

## Accessibility notes

- Speech announces the players, the target, whose turn it is, the final round, and the winner.
- The three die types are distinguished by bar position and tone, not colour.
- Scores and totals are counted with hundreds, tens, and ones. Learn the code above.
- The controller gives each action its own physical button. It is the easier input.
- There is no pause. Pressing reset returns to the last save while Tossup stays installed.
- The save is temporary: flashing another program erases it.

## Tips

- The pool shrinks as your unbanked total grows, so the risk of a red bust rises. Bank before the pool gets too small.
- A total of 8 or 9 is tempting, but you are rolling only one or two dice. Banking earlier is safer.
- Reds only bust you when the roll has no green die. A single green die in the roll protects the whole roll.
- Yellow-only rolls are wasted turns, not busts. Roll again.
- In the final round, check the leader's score. If you are ahead, bank; if you are behind, you may need to push.
- In a solo game, a lower target makes a shorter game. Raise it when you want a longer run.
