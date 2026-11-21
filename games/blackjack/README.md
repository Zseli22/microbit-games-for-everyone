# Blackjack

Play blackjack against the dealer, with betting, doubling down, and an audio card-counting aid.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 against the dealer |
| Controller | Optional |
| Speech | Yes, for totals, results, and coins |
| Save | None |
| Difficulty | Easy to moderate |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

A small blackjack game. You start with 100 coins and a bet of 10. Beat the dealer's hand without going over 21. You can raise or lower the bet, double down on 10 or 11, and ask the board to read the remaining deck. The dealer's play follows the usual rule: draw until 17, then stand.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- The game does not save. Restarting the program starts you again with 100 coins.

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Raise the bet | Touch the logo |
| Lower the bet | Touch pin 1 or pin 2 |
| Deal, hit, or accept a double | Button A |
| Stand, or decline a double | Button B |
| Hear your coins and current bet (while betting) | Hold the board with the logo end pointing down |
| Hear the remaining deck (while betting) | Button B |

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Raise the bet | Joypad Right |
| Lower the bet | Joypad Left |
| Deal, hit, or accept a double | Fire 1 |
| Stand, or decline a double | Fire 2 |
| Hear your coins and current bet (while betting) | Joypad Up |
| Hear the remaining deck (while betting) | Fire 2 |

The logo-down gesture means the top of the board, where the logo is, points toward the floor. It is not the same as turning the display face down.

During a hand, the control that raises the bet (the logo, or Joypad Right) shows your cards and the dealer's visible card instead. The table lists it as "Raise the bet" because that is its role while you are betting.

## How to play

### Betting

1. The board says "Let's play blackjack" and shows a heart.
2. **Raise** or **lower** the bet. The bet starts at 10 and moves in steps of 5. It can also be 1, and it can be all of your coins.
3. Each change plays a tone whose pitch rises with the bet. If you reach all-in, the board shows scissors and says "All in." If you reach one coin, it shows 1 and says "One coin."
4. **Hold the logo end down** (or press **Joypad Up**) to hear your coins and the current bet.
5. Press **Button B** (or **Fire 2**) while betting to hear the remaining deck. If ten or fewer cards are left, the board says the deck is about to be reshuffled. Otherwise it plays every remaining card as a tone and shows its value. This is a card-counting aid.
6. Press **Button A** (or **Fire 1**) to deal.

### The deal

- You and the dealer each get two cards. One dealer card stays hidden.
- Your total is scrolled and spoken.
- If your first two cards total 21, you have blackjack. The board celebrates, and the dealer plays.
- If your first two cards total 10 or 11, the board offers a double down. Press **Button A** (or **Fire 1**) to double and take exactly one more card. Press **Button B** (or **Fire 2**) to decline and play normally.
- If you cannot afford to double, the board says so and does not offer it.

### Your turn

- **Hit:** Button A (or **Fire 1**). You get another card. Your new total is scrolled and spoken. Reaching exactly 21 passes straight to the dealer.
- **Stand:** Button B (or **Fire 2**). The dealer plays.
- **Show your hand:** Touch the logo (or press **Joypad Right**). The board plays each of your cards, then the dealer's visible card.
- If you go over 21, you bust and lose the hand.

### The dealer's turn

The dealer's total (including the hidden card) is scrolled and spoken. The dealer draws until reaching at least 17, then stands. If the dealer goes over 21, you win.

### The result

- **You win:** your bet is added to your coins. A natural blackjack pays one and a half times the bet, rounded to the nearest coin. A doubled hand pays twice the bet.
- **You lose:** the bet is subtracted. A doubled hand loses twice the bet.
- **Push:** your total equals the dealer's. Your coins do not change.
- Your new coin total is scrolled and spoken.

If your coins reach zero, the board resets the program and starts over with 100 coins. If your bet is larger than your remaining coins, it is lowered to the next multiple of five down (or 1 coin if you have fewer than five).

## Card values

| Card | Value |
| --- | --- |
| X (ten, jack, queen, king) | 10 |
| A (ace) | 1 or 11, whichever is better |
| 2 to 9 | Face value |

The deck has 52 cards: sixteen ten-value cards and four each of ace through nine. It is reshuffled when ten or fewer cards remain.

## What you hear

| Sound | Meaning |
| --- | --- |
| A rising shuffle sound and spinning clock images | The deck is being shuffled |
| A short rising swoosh | You draw a card |
| A lower rising swoosh | The dealer draws a card |
| A tone for each card | The card's value: the ace is highest, then the ten, then 9 down to 2 |
| A tone that rises with the bet | You raised or lowered the bet |
| A long rising fanfare | You won a hand |
| A falling four-note phrase and a low tone | You lost a hand |
| Two very low tones | A bust |
| Spoken totals | Your hand, the dealer's hand, and your coins |
| Spoken "Blackjack", "Busted", "I stand", "It's a push" | The state of the hand |

The dealer's hidden card is not shown or announced during your turn. Its value is included when the dealer's total is announced at the start of the dealer's turn.

## Scoring and saves

There is no save. Coins persist only while the program is running. Restarting the board or reflashing the game starts you again with 100 coins.

The game calls a full board reset when your coins reach zero. That is intentional.

The dealer's natural 21 is revealed on the dealer's turn rather than ending the hand immediately.

## Accessibility notes

- Every total and result is spoken. The cards also have distinct tones, so you can follow the deal without the display.
- The "show your hand" action reads your cards one at a time, then the dealer's visible card.
- The status gesture announces your coins and bet. On a bare board it is a logo-down hold; on the controller it is Joypad Up.
- The card-counting aid reads the entire remaining deck. It is a strong advantage, but it is also a lot of tones; use it when you want it.
- The game is playable without sight. The main gap is that the hidden dealer card is only revealed when the dealer plays, which is the normal rule.
- There is no pause. Pressing reset restarts the program and resets your coins.

## Tips

- Keep the bet small until you know the deck. The deck is finite, and the count changes as cards are dealt.
- Double down on 10 or 11 only when you can afford the extra bet and the deck looks favourable.
- Use the status gesture before a big bet so you know exactly how many coins you have.
- When the board says the deck is about to be reshuffled, the next deal starts a fresh deck.
- The dealer stands on 17 through 21, including a soft 17. Plan around that.
