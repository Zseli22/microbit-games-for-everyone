# Micro:bit Games for Everyone

Eleven games and toys for the BBC micro:bit V2, built to be played by ear, by touch, or on screen. Blind, low-vision, and sighted players use the same program. Ten of the eleven also support the optional [Kitronik :GAME Controller](https://kitronik.co.uk/products/5644-game-controller). MicroFidget is deliberately bare-board only.

These are MicroPython programs, not MakeCode blocks. You load them with the official micro:bit Python Editor or with a `.hex` file built by that editor.

The games are documented below. Known issues and rules notes are in [docs/known-issues.md](docs/known-issues.md).

## Choose a game

- **[MicroFidget](games/micro-fidget/README.md)** — seven quick sensory challenges: mash, shake, tap, match a tone, test your reactions, count sounds, and keep a rally going. One player. Bare board only. Speech, tones, and the microphone.
- **[Simon](games/simon/README.md)** — repeat a growing sequence of four tones. One player. Controller optional. Tones and a short spoken comment after a mistake.
- **[Blackjack](games/blackjack/README.md)** — play blackjack against the dealer, with betting, doubling down, and a card-counting aid. One player. Controller optional. Speech and card tones.
- **[Mastermind](games/mastermind/README.md)** — break a hidden code, with three feedback styles and adjustable difficulty. One player. Controller optional. Speech and tones.
- **[Vibration Challenge](games/vibration-challenge/README.md)** — match the strength of a vibration. One player. Controller heavily recommended. Haptics, or pitch on a bare board.
- **[Composer](games/composer/README.md)** — build, play, and save your own melodies on the board. One player. Controller optional. Speech for menus and counts.
- **[Breakout](games/breakout/README.md)** — steer a ball around a 5 by 5 grid, collect blocks, and survive the falling ball. One player. Controller recommended. A sonified arcade game.
- **[Zombie Dice](games/zombie-dice/README.md)** — the push-your-luck dice game with humans and computer opponents. Two to ten players. Controller optional. Speech, dice tones, and saved games.
- **[Tossup](games/tossup/README.md)** — a push-your-luck dice game: collect green dice, avoid red, and bank before you bust. One to ten players. Controller optional. Speech, dice tones, and saved games.
- **[36](games/thirty-six/README.md)** — a six-dice game where you aim for 30, and going over 30 lets you attack the next player. One to ten players. Controller optional. Speech, tone counts, and saved games.
- **[Flip 7](games/flip-7/README.md)** — the Flip 7 card game with humans and computer opponents. Two to ten players. Controller optional. Speech, card tones, and saved games.

## What you need

- A **micro:bit V2**. All eleven programs use V2-only features such as `audio`, `speech`, or the microphone. They will not run on V1.
- A **USB data cable** (not a charge-only cable).
- A browser for the [micro:bit Python Editor](https://python.microbit.org).
- Optional: a **Kitronik :GAME Controller** (product 5644) and two AA batteries. It provides the four direction buttons, two fire buttons, a piezo buzzer, and a vibration motor. The controller powers the micro:bit.

No headphones or external speaker are needed. The V2's built-in speaker is the default output. With the controller attached, sound comes from the controller's buzzer.

## Install a game

1. Open [python.microbit.org](https://python.microbit.org) in a browser.
2. Open the game's `.py` file in the editor. You can use the editor's **Open** button, or copy the text and paste it into the code area.
3. Connect the micro:bit with the USB cable.
4. Press **Send to micro:bit**. The editor builds a `.hex`, flashes it, and the program starts.
5. If you want a `.hex` file to keep, use the editor's save/download option. You can drag that `.hex` onto the `MICROBIT` drive later.

A `.py` file, including one named `main.py`, cannot simply be copied onto the board and run. The program has to be embedded in the runtime by the editor or by a `.hex`. The `MICROBIT` drive is a flashing target for `.hex` files, not a folder you can browse for the program source.

**Only one program can be on the board at a time.** Flashing another game replaces the current one and erases the current program's filesystem, including its save. You cannot keep several games or several saves on one board.

## Powering on and off

- **Turn the board off:** hold the reset button for about three seconds.
- **Turn it back on:** press the reset button quickly.
- **Restart the current program:** press the reset button quickly. This does not erase the save.
- **Replace the program:** flash a new `.hex`. This erases the old program and its filesystem.

## Using the Kitronik :GAME Controller

The controller has four separate direction buttons in a diamond, not a joystick or a sliding pad. They are similar-looking buttons and can technically be pressed at the same time, which is different from a normal D-pad. The labels used here are based on the Kitronik documentation:

- **Joypad Up**, **Joypad Down**, **Joypad Left**, **Joypad Right** — the four direction buttons.
- **Fire 1** and **Fire 2** — the two fire buttons.
- **Buzzer** — the piezo sounder on the board.
- **Vibration motor** — the motor inside the controller.

In general, **Fire 1** is the primary action (confirm, deal, roll, start) and **Fire 2** is the secondary action (stand, bank, back, stats). The direction buttons mirror the touch controls on a bare board. Each game has its own control table, because a few games use the directions differently.

The controller-aware games detect the controller once, at startup. Plug the micro:bit into the controller before you power on or press reset, and do not hold **Fire 1** while the board starts. Those games use Fire 1 to detect the controller.

Ten of the eleven games support the controller. **MicroFidget does not**, by design; it is a bare-board program.

## Using a bare micro:bit

The bare board gives you these controls:

- **Button A** and **Button B** on the front.
- **The logo** at the top of the board. On V2 it is touch-sensitive.
- **Touch pin 1** and **touch pin 2**. These are the large holes labelled 1 and 2 at the bottom edge. In most games, either one acts as the same control; Composer uses them separately.
- **Shake** the board.
- **Tilt** the board up, down, left, or right.
- **Turn the display face down** so the LED matrix faces the table.

The LED grid is **5 by 5 single-colour LEDs**. It cannot show colour. Games use positions, bars, letters, simple patterns, and tones. When a game talks about green, yellow, and red dice, those are die types shown as **G**, **Y**, and **R** or as bars in different rows, not as coloured lights.

The V2's built-in speaker is the sound output. No pin 0 connection or headphone adapter is required. On the controller, sound goes to the buzzer instead.

## Sound, speech, and vibration

The games use three kinds of feedback:

- **Speech** — menus, totals, results, and instructions in words. The micro:bit's voice is small and robotic, and speech cannot be interrupted once it starts. The programs therefore use it sparingly: mostly for menus, player announcements, totals, and results, not for every note or mode change.
- **Tones** — pitches and short melodies. Tones carry information quickly: a card's value, a column and row on the grid, a score counted in hundreds, tens, and ones, or a correct or wrong answer.
- **Vibration** — on the controller, the motor can signal a wrong answer or, in Vibration Challenge, the strength to match.

Each game guide has a **What you hear** section. Those sections use note names such as C5 and G5 rather than frequencies in hertz, because the sounds are musical notes.

## Saves and the one-program limit

Only one program can be stored on the board at a time. Its save lives in that program's filesystem, in the board's flash memory. It survives a reset or unplugging while that program stays installed.

**Flashing a new program erases the old program and its entire filesystem, including its save.** This is why there is no way to keep several games or several saves on one board.

Games that keep progress:

- **MicroFidget** keeps high scores.
- **Breakout** keeps score, lives, and speed after a lost life.
- **Zombie Dice**, **Tossup**, **36**, and **Flip 7** keep a game in progress.
- **Composer** keeps your saved tunes.

Games without a save start fresh each time: Simon, Blackjack, Mastermind, and Vibration Challenge.

The `MICROBIT` drive is not a normal window into the filesystem. It is used for flashing `.hex` files. To inspect or back up MicroPython files, you need a specialised tool such as the Mu editor's files pane. Even then, treat saves and Composer tunes as temporary: the next flash will erase them.

Most games that save let you delete or reset progress from their menu or startup prompt. You can also clear any save by flashing the program again or flashing another program, which replaces the filesystem.

## Accessibility design

The collection follows a few simple rules:

- Every important state has a sound or a spoken message.
- The display is monochrome and is never the only channel for information.
- Menus announce what you selected; some use tones only to stay fast.
- Destructive actions ask for confirmation.
- The controller is optional, but it is the easier input for games that need several buttons at once.
- Saves are temporary by nature, and the documentation says so instead of implying that files can be managed like a computer.

The full checklist, including the intentional trade-offs, is in [docs/accessibility.md](docs/accessibility.md).

## Repository layout

```text
.
├── README.md                  This file
├── LICENSE
├── docs/
│   ├── controls.md            Shared control vocabulary and the controller map
│   ├── accessibility.md       Design rules, checklist, and audio-only playtest
│   ├── flashing-and-saving.md Install, one-program limit, and save behaviour
│   ├── adding-a-game.md       How to add another program to the collection
│   └── known-issues.md        Remaining bugs and rules notes
├── games/
│   ├── micro-fidget/          MicroFidget.py + README.md
│   ├── simon/                 Simon.py + README.md
│   ├── blackjack/             Blackjack.py + README.md
│   ├── mastermind/            Mastermind.py + README.md
│   ├── vibration-challenge/   VibrationChallenge.py + README.md
│   ├── composer/              Composer.py + README.md
│   ├── breakout/              Breakout.py + README.md
│   ├── zombie-dice/           ZombieDice.py + README.md
│   ├── tossup/                Tossup.py + README.md
│   ├── thirty-six/            36.py + README.md
│   └── flip-7/                Flip7.py + README.md
```

## Troubleshooting

- **The board shows nothing and makes no sound.** Check that it is a V2. Press the reset button quickly to wake it. If it still does nothing, connect USB and check the cable.
- **There is a picture but no sound.** The V2 built-in speaker is used on a bare board. Check that it is not covered and that the room is quiet enough. On the controller, check the batteries and the buzzer.
- **The controller is not detected.** Unplug the micro:bit from the controller, reseat it firmly, replace the batteries if needed, and press reset. Do not hold Fire 1 while it starts.
- **The board turns off when I hold reset.** That is intentional: holding reset for about three seconds powers it down. Press reset quickly to turn it back on.
- **My save disappeared.** It was erased by flashing a new program or reflashing the same one. That is expected.
- **I cannot find the save file on the MICROBIT drive.** The drive is for flashing `.hex` files, not for browsing the MicroPython filesystem. Use Mu or another specialised tool if you need to inspect it, and expect the next flash to erase it.
- **A game restarts by itself.** Some games call `reset()` deliberately when you run out of coins or lives. If it happens at another time, connect to the REPL (the interactive Python prompt) and read the error.

## Contributing

New games are welcome if they follow the shared control vocabulary and the accessibility checklist. Start with [docs/adding-a-game.md](docs/adding-a-game.md). Please do not put controller pin numbers in a game's README; use the button names. The pin map is kept in one place, [docs/controls.md](docs/controls.md), for people editing the code.

## License

MIT. See [LICENSE](LICENSE).

The Kitronik :GAME Controller is a product of Kitronik Ltd. This project is not affiliated with or endorsed by Kitronik or the Micro:bit Educational Foundation.
