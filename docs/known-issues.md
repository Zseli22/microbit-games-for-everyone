# Known issues

This page records the bugs fixed during the final review and the intentional design choices that are sometimes mistaken for defects. The game guides and [accessibility.md](accessibility.md) explain the choices in context.

All eleven programs compile with `python -m py_compile`. Flip 7 and the other games have been tested on hardware where noted; this page does not list any open bugs.

## Fixed in this revision

### K-01 — Blackjack could mis-score hands with more than one ace

**Status:** fixed.

The old ace adjustment only checked the first card. A hand where the first card was not an ace could bust even though a later ace should have counted as 1.

The copy now computes the hand value from all the cards, counting aces as 11 and reducing them to 1 while the total is over 21. The dealer uses the same function.

### K-02 — Tossup counted exactly 100 as ten tens

**Status:** fixed.

The count loop used `while value > 100`, so a score of exactly 100 was read as ten middle beeps instead of one high beep. It now uses `>= 100`.

### K-03 — Flip 7 counted exactly 100 as ten tens

**Status:** fixed.

The same off-by-one in the count loop is fixed. A score of exactly 100 is now one high beep.

### K-04 — Flip 7 did not follow the original turn structure

**Status:** fixed.

The original game gives each player one action per turn. This version used to let the current player keep hitting until they banked or busted.

The copy now works like this:

- On your turn you either hit once or bank. After the action, the turn passes to the next active player.
- A Freeze banks the target's current hand before removing them from the round.
- A Flip 7 adds the 15-point bonus, banks every other active player's hand, and ends the round.
- A Flip 3 resolves its three cards, then the turn passes to the player after the player who played it.

The file is slightly smaller than before, so it still fits the filesystem limit.

### K-05 — Tossup deleted saved games on the controller without confirmation

**Status:** fixed.

In `load_save()`, the confirmation check unpacked the wrong control index on the controller, binding deletion confirmation to Fire 2 instead of Joypad Down. Pressing Fire 2 asked to delete and immediately confirmed on the same loop tick. It now binds to Joypad Down as documented.

### K-06 — Zombie Dice could drop runner dice and play the wrong die waveform

**Status:** fixed.

When a runner rolled ahead of a brain or shotgun in the same three-die roll, the reveal loop removed the first die in `hand` (the runner) and kept a later die instead, while also playing the runner's waveform for subsequent dice. The loop now resolves each die by index and keeps the exact runner dice in `hand`. Yellow cup draws also use the square waveform consistently.

### K-07 — Blackjack and Mastermind set capacitive touch mode before controller detection

**Status:** fixed.

Both scripts called `pin1.set_touch_mode(pin1.CAPACITIVE)` and `pin2.set_touch_mode(pin2.CAPACITIVE)` at startup before checking for the controller. Those top-level calls have been removed so touch mode is only enabled on a bare board.

### K-08 — Blackjack betting could block all-in bets or drop the bet to zero

**Status:** fixed.

Raising the bet could not reach all-in whenever the coin count was not a multiple of five, and losing down to 1 to 4 coins set the bet to 0. Betting now steps cleanly to all-in and down to 1, and post-loss bet reduction floors at 1 coin.

### K-09 — Bare-board player setup auto-started at nine players instead of ten

**Status:** fixed.

Zombie Dice, Tossup, 36, and Flip 7 checked for 9 players instead of 10 in the bare-board auto-start condition, preventing a tenth player from being added on a bare board. All four now auto-start at 10 players.

### K-10 — Final-round record announcements and Tossup bust flow

**Status:** fixed.

In Tossup and Zombie Dice, the final-round "record has been beaten" announcement triggered whenever any player ended a turn at or above the base target, even without beating the leader. Both now announce only when a player beats the highest other score while at least one player still has a turn left. Tossup also returns immediately after a bust so ending the final round on a bust no longer plays the all-green chime at the start of the next game.

### K-11 — Display, speed, and audio polish fixes

**Status:** fixed.

- **Breakout:** Losing a life during a speed powerup now restores `original_speed` before clamping and saving.
- **Composer:** Entering tempo mode stops active melody playback so the metronome click always starts, and the BPM scrolls on entry and change rather than restarting every loop.
- **Flip 7:** The Second Chance card now uses a distinct circle pattern instead of duplicating `×2`'s diamond, and target selection announces the initially highlighted player.
- **36:** An exact knockout with no leftover penalty no longer plays a flat sweep for the next player's unchanged score.
- **Vibration Challenge:** Buffered Button A presses during the reference pulses are cleared before test pulses begin.

## Not defects

These are intentional and are explained in the relevant guides:

- **Breakout's speed climbs past the comeback floor during a life.** The game keeps speeding up until it becomes hard to keep up with; losing a life eases the speed back to give you a chance at a comeback.

- **36's bonus and leftover-penalty behaviour.** Going over 30 rolls extra dice and attacks the next player. A leftover penalty passing to the next player is part of the design; you can take someone down with you.
- **Mastermind feedback style 0.** It is the easier variant: you need the correct set of symbols, not the correct order.
- **Mastermind's shake-to-submit on a bare board.** Every other bare-board control is already used.
- **Simon's modes and Composer's note names are not spoken.** Speech cannot be interrupted, and speaking every change would make the games slow.
- **MicroFidget has no controller support.** The microphone and fidget games are bare-board experiences.
- **Vibration Challenge without the controller uses pitch.** The controller is heavily recommended, but the fallback is deliberate.
- **Dice and card faces use tones rather than speech.** This keeps turns quick; the stats and viewer actions give the counts.
- **Flip 7's deck carries over between rounds.** It is rebuilt only when it runs out, so a player who tracks the cards can predict what remains.
- **Blackjack's dealer natural is revealed on the dealer's turn.** The hand does not end early when the dealer has 21. This casual version is accepted as it is.
- **No pause.** Most games only advance when you act. Breakout moves on a timer, but a pause was not part of its design.
- **One program and one save.** Flashing another program erases the current program and its filesystem. This is a hardware and runtime limit, not a bug.

## How to report a new issue

Include:

- The game and the version or commit.
- Whether a controller was attached.
- What you did, what you expected, and what happened.
- Whether the display was covered (for an accessibility issue).
- The error text from the REPL, if you can connect to it.

Add the issue to this file if you are working in the repository, or open an issue on GitHub once the repository is published.
