# Flip 7

The Flip 7 card game: collect unique numbers, use action cards, and bank before you bust. First to 200 wins.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 2 to 10, any mix of humans and computers |
| Controller | Optional |
| Speech | Yes, for players, actions, and the winner |
| Save | Yes, until another program is flashed |
| Difficulty | Moderate |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

Flip 7 is a card game about pressing your luck. Each player builds a hand of number cards. On your turn you either hit once or bank. A duplicate number busts you unless you have a Second Chance. Action cards add points, double your total, freeze players, force extra draws, or protect you. If you collect seven different number cards, you get a 15-point bonus, every other active player banks their hand, and the round ends immediately.

When a round ends, a player with 200 or more points and the highest score wins. If two or more players are tied at 200 or more, another round decides it.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- You need at least two players. Add humans, computers, or both.
- The game saves after each turn and each round. If you stop in the middle of a turn, you return to the end of the previous turn. Flashing another program, or reflashing Flip 7, erases the save.

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
| Hit: draw a card | Button A, or shake the board | Fire 1 |
| Bank: score your hand and sit out the round | Button B | Fire 2 |
| View your cards | Touch the logo | Joypad Up |
| Hear every player's score | Touch pin 1 or pin 2 | Joypad Down |
| Confirm deletion on the load screen | Turn the display face down | Joypad Down |

### Choosing a target (Freeze, Flip Three, or duplicate Second Chance)

| Action | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| Next (or previous) target | Button A (next) | Joypad Left or Right |
| Confirm the highlighted target | Button B | Fire 1 |
| View the highlighted target's cards | Touch the logo | Joypad Up |
| Hear the highlighted target's score | Touch pin 1 or pin 2 | Joypad Down |

Note that on a bare board, **Button A cycles targets and Button B confirms**, which is reversed from the usual turn controls.

### In the card viewer

| Action | Control |
| --- | --- |
| Move through the cards | Button A (next), or Joypad Left and Right |
| Hear the hand total | Button B, or Fire 2 |
| Leave the viewer | Touch the logo, or Joypad Up |
| Hear the viewed player's score (while choosing a target) | Touch pin 1 or pin 2, or Joypad Down |

## How to play

### Set up the players

1. The board announces "Flip 7" and says "Select players."
2. Press **Button A** (or **Joypad Left**) to add a human. The display shows H and plays a high two-note phrase.
3. Press **Button B** (or **Joypad Right**) to add a computer. The display shows C and plays a lower two-note phrase.
4. Add between 2 and 10 players.
5. Shake the board (or press **Fire 1**) to start. The beginning of a round deals one card to each player automatically. On a bare board, the game starts automatically when 10 players have been added.

### A turn

1. The board shows the last card you drew, or a heart if you have no cards yet.
2. Choose one action:
   - **Hit:** Button A, shake the board, or press **Fire 1**. Draw one card.
   - **Bank:** Button B (or **Fire 2**). Add your hand total to your score and sit out the rest of the round.
3. After your action, the turn passes to the next active player. If you hit and do not bust or flip seven, your turn still ends after that one card.
4. If you draw a number card that you already have, you bust unless you have a Second Chance. A bust scores nothing for the round, and the turn passes on.
5. The round continues around the table until every player has banked, been frozen, or busted. Then scores are added and a new round begins.
6. At the end of a round, a player with 200 or more points and the highest score wins. If two or more players are tied at 200 or more, another round is played.

### The cards

| Card | Effect |
| --- | --- |
| Number 0 to 12 | Adds its face value to your hand. A duplicate number busts you. |
| +2, +4, +6, +8, +10 | Adds that many points. |
| ×2 | Doubles your hand total, including the + cards. |
| Freeze | The target banks their current hand and sits out the round. You may target yourself. |
| Flip Three | The target must draw three cards immediately. After they resolve, the turn passes to the player after you. |
| Second Chance | Protects you from one duplicate number. If you already have one, give the new one to another player who does not have one (if everyone else already has one, it is discarded). |

If a Freeze or Flip Three is drawn during a Flip Three, it is resolved after the three cards are drawn. If a player flips seven during that resolution, the round ends immediately and every other active player banks their hand.

### How the deck is made

The deck has 94 cards:

- One 0 and one 1.
- Two 2s, three 3s, four 4s, and so on up to twelve 12s.
- Three Freeze cards, three Flip Three cards, and three Second Chance cards.
- One each of +2, +4, +6, +8, and +10.
- One ×2 card.

The board shows 0 to 9 as themselves, 10 as **X**, 11 as **J**, and 12 as **Q**. Action cards use simple patterns, and every card has a tone. The display cannot show colour, so the marks and tones carry the information.

### Scoring a hand

Add the values of your number cards, then add the + cards, then double the total if you have a ×2. If you have seven different number cards, add 15.

For example:

- 3, 7, 9 = 19 points.
- 3, 7, +6 = 16 points.
- 3, 7, ×2 = 20 points.
- 3, 7, +6, ×2 = 32 points.
- Seven different number cards = the sum of the numbers, plus any + cards, doubled if you have ×2, plus 15.

Freeze, Flip Three, and Second Chance have no point value of their own.

### Viewing your cards

The card viewer is the main non-visual way to inspect a hand.

1. Touch the logo (or press **Joypad Up**) to open it.
2. Use **Button A** to step forward (or **Joypad Left and Right** to move backward and forward) through the cards. Each card is shown and played as a tone.
3. Press **Button B** (or **Fire 2**) to hear the hand total.
4. Touch the logo (or press **Joypad Up**) again to leave.

The viewer also opens while you are choosing a target for an action card. There, the board says "Choose player" and announces the first eligible player. Cycle targets with **Button A** (or **Joypad Left and Right**), confirm with **Button B** (or **Fire 1**), inspect the highlighted player's cards with the logo (or **Joypad Up**), and hear their score with pin 1 or pin 2 (or **Joypad Down**).

### All scores

Touch pin 1 or pin 2 (or press **Joypad Down**) to hear every player's score. Each score is scrolled and counted with tones.

### Computer players

Computer players take their turns automatically. They decide whether to hit or bank based on their hand total, how many unique numbers they have, and the leader's score. They never bank while holding a Second Chance, and they take more risk when a leader is far ahead or close to 200, pushing for more cards or trying to pass the leader instead of banking early.

## Reading the cards and numbers

| Mark | Meaning |
| --- | --- |
| 0 to 9 | The number card |
| X | 10 |
| J | 11 |
| Q | 12 |
| + then a number | A +2, +4, +6, +8, or +10 card (on the resting turn display between draws, only the value mark is shown) |
| Diamond | ×2 |
| X pattern | Freeze |
| 3 pattern | Flip Three |
| Circle pattern | Second Chance |

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
| Spoken "Flip 7" | The title |
| High two-note phrase | A human player was added |
| Lower two-note phrase | A computer player was added |
| A rising draw sound and a down arrow | A card is being drawn |
| A tone for each number card | Its value, from 0 to 12 |
| A plus sign, a tone, then the number tone | A + card |
| A diamond and three tones | ×2 |
| An X pattern and a noise burst | Freeze |
| A 3 pattern and three blips | Flip Three |
| A circle pattern and a six-note celebration melody | Second Chance drawn |
| A descending noise sweep | Second Chance blocked a duplicate number |
| A skull and two low tones | A bust |
| Counted round points, a rising bank phrase, then counted total score | You banked |
| A celebration image and a fanfare | Flip 7: seven unique numbers |
| A fanfare and speech | The winner |
| Spoken player numbers | Whose turn it is, or the highlighted target |
| Spoken "freeze player N", "flip three player N", "second chance player N" | Freeze, Flip Three, or a transferred duplicate Second Chance resolved |

The individual card values are not spoken. Use the viewer to hear them one at a time.

## Scoring and saving

- Each turn is one action: hit once or bank.
- Number cards are worth their face value.
- + cards add 2, 4, 6, 8, or 10.
- ×2 doubles the total of number cards and + cards.
- Seven different number cards add 15, every other active player banks their hand, and the round ends.
- Freeze banks the target's current hand and removes them from the round.
- At the end of a round, the highest score of 200 or more wins. A tie at 200 or more triggers another round.
- The game saves after each turn and each round in its internal filesystem. It stores the players, the remaining deck, the current player, the phase, the opening-player index, and whether the round has ended. Flashing another program, or reflashing Flip 7, erases the save.
- On startup, if a save exists, the board asks "Would you like to resume your saved game?"
  - **Button A** (or **Fire 1**) loads it.
  - **Button B** (or **Fire 2**) asks to delete it. Turn the display face down (or press **Joypad Down**) to confirm.
- Loading reads every player's score and announces whose turn it is.

The save is written at the end of a turn or a round. If you stop in the middle, the current turn's card is not saved.

The deck carries over between rounds. It is rebuilt only when it runs out, so the remaining cards are predictable if you track them.

## Accessibility notes

- Speech announces the players, action cards, and the winner. The card values are tones and marks, not spoken words.
- The card viewer is the key accessibility feature. Use it to inspect your hand and hear the total.
- Scores and totals are counted with hundreds, tens, and ones. Learn the code above.
- The controller gives each action a separate physical button. It is the easier input for a group.
- There is no solo mode. You need at least two players.
- There is no pause. Pressing reset returns to the last save while Flip 7 stays installed.
- A Freeze banks the target's hand, so freezing the leader is a strong move. A Flip 7 ends the round and banks every other active player.

## Tips

- Bank at four or five unique numbers, or when your total is strong. Do not wait for seven unless you have a Second Chance.
- Second Chance is best used early, while you still have room to draw. It protects you from one duplicate.
- Flip Three is a gamble. It can complete a hand or bust you.
- Freeze the leader, especially when they are close to 200.
- In the final stretch, check the scores. If you are ahead, bank; if you are behind, you may need to push.
- Use the viewer to check your total before banking. The display only shows the last card.
- The deck carries over between rounds, so tracking the cards that have gone is useful. Do not try to count every card perfectly; track the numbers in your own hand and the cards that have hurt you.
