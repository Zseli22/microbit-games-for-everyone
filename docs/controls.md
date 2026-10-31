# Controls

This page is the shared vocabulary for the collection. Each game guide has its own control tables; this page explains the names and how the two input devices relate.

## The two ways to play

### Bare micro:bit V2

- **Button A** and **Button B** on the front of the board.
- **The logo** at the top. It is touch-sensitive.
- **Touch pin 1** and **touch pin 2**. These are the large holes at the bottom edge, labelled 1 and 2. Most games treat either one as the same control; Composer uses them separately.
- **Shake** the board.
- **Tilt** the board up, down, left, or right.
- **Turn the display face down** so the LED matrix faces the table.

The V2's built-in speaker is the sound output. No external speaker or headphone connection is required.

### Kitronik :GAME Controller

The controller has four separate direction buttons arranged in a diamond, two fire buttons, a piezo buzzer, and a vibration motor. The direction buttons are not a joystick or a sliding pad; they are four similar-looking buttons that can technically be pressed at the same time.

```text
                 micro:bit edge connector
                        (top edge)

                       [ Joypad Up ]

        [ Joypad Left ]          [ Joypad Right ]

                      [ Joypad Down ]

              [ Fire 1 ]      [ Fire 2 ]

     Buzzer on the board, vibration motor inside
```

- **Joypad Up**, **Joypad Down**, **Joypad Left**, **Joypad Right** — the four direction buttons.
- **Fire 1** — usually the primary action: confirm, deal, roll, start, submit.
- **Fire 2** — usually the secondary action: stand, bank, back, stats, keep.
- **Buzzer** — the sound output. The controller-aware games use it automatically.
- **Vibration motor** — used by Simon for a wrong answer and by Vibration Challenge for the signal itself.

The controller-aware games detect the controller once, at startup. Plug the micro:bit into the controller before powering on or pressing reset, and do not hold Fire 1 while the board starts. MicroFidget is the exception; it does not use the controller.

## The shared conventions

| Player action | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| Primary / confirm | Button A, or shake where noted | Fire 1 |
| Secondary / back | Button B | Fire 2 |
| Up / increase / previous | Touch the logo | Joypad Up |
| Down / decrease / next | Touch pin 1 or pin 2 | Joypad Down |
| Left | Button A | Joypad Left |
| Right | Button B | Joypad Right |
| Play, stop, or save in Composer | Turn the display face down | Joypad Down, or turn it face down |

These are conventions, not rules. A game may use the directions differently, and some games use shake or tilt because the motion is part of the game.

## Per-game quick matrix

The game guide is always authoritative. This table is for comparing the games at a glance.

| Game | Bare micro:bit | Kitronik :GAME Controller |
| --- | --- | --- |
| MicroFidget | A = next game; B = start; shake = hear description; logo = high score; logo then face down = reset score | Not supported |
| Simon | Logo = Up; touch pin 1 or 2 = Down; A = Left; B = Right; B at the menu = start | Joypad directions; Joypad Right at the menu = start |
| Blackjack | Logo = raise bet; touch pin 1 or 2 = lower bet; A = deal or hit; B = stand; logo pointing down = hear coins and bet | Joypad Right = raise; Joypad Left = lower; Fire 1 = deal or hit; Fire 2 = stand; Joypad Up = status |
| Mastermind | A = Left; B = Right; logo = Up; touch pin 1 or 2 = Down; shake = submit | Joypad directions; Fire 1 = submit |
| Vibration Challenge | A = start or lock in; B = hear score and lives | Fire 1 = start or lock in; Fire 2 = hear score and lives |
| Composer | Touch pin 1 = previous; touch pin 2 = next; A = action A; B = action B; logo = shift; face down = play, stop, or save | Joypad Left = previous; Joypad Right = next; Fire 1 = action A; Fire 2 = action B; Joypad Up = shift; Joypad Down = play, stop, or save |
| Breakout | Tilt = steer; A = start and stats; B = teleport | Joypad = steer; Fire 1 = start and stats; Fire 2 = teleport |
| Zombie Dice | A = add human or roll; B = add computer or bank; shake = start; logo = turn stats; touch pin 1 or 2 = all scores | Joypad Left = add human; Joypad Right = add computer; Fire 1 = start or roll; Fire 2 = bank; Joypad Up = turn stats; Joypad Down = all scores |
| Tossup | A = add human or roll; B = add computer or bank; shake = start; logo = increase limit or show total; touch pin 1 or 2 = decrease limit or all scores; face down = hear limit | Joypad Left = add human; Joypad Right = add computer; Fire 1 = start or roll; Fire 2 = bank or hear limit; Joypad Up = increase limit or total; Joypad Down = decrease limit or all scores |
| 36 | A = add human, roll, or cycle dice; B = add computer, show scores, or keep; shake = start or commit; logo = total; touch pin 1 or 2 = toggle undo | Joypad Left or Right = add player or cycle dice; Fire 1 = start, roll, or commit; Fire 2 = keep or show scores; Joypad Up = total; Joypad Down = toggle undo |
| Flip 7 | A = add human or hit; B = add computer or bank; shake = start; logo = view cards; touch pin 1 or 2 = all scores | Joypad Left = add human; Joypad Right = add computer; Fire 1 = start or hit; Fire 2 = bank; Joypad Up = view cards; Joypad Down = all scores |

## Developer reference

This section is for people editing the code. It is the only place in the repository where controller pin numbers appear. The pin map comes from the Kitronik :GAME Controller datasheet for product 5644:

<https://cdn.robotshop.com/media/k/ktr/rb-ktr-68/pdf/game-controller-micro-bit-datasheet.pdf>

### Pin map

The :GAME Controller is active-low: a pressed button reads `0`, and an idle button reads `1`.

| Controller control | micro:bit pin | Notes |
| --- | --- | --- |
| Joypad Up | 8 | Active-low digital input |
| Joypad Down | 14 | Active-low digital input |
| Joypad Left | 12 | Active-low digital input |
| Joypad Right | 13 | Active-low digital input |
| Fire 1 | 15 | Active-low digital input; also high when idle, which is how the games detect the controller |
| Fire 2 | 16 | Active-low digital input |
| Piezo buzzer | 2 | Audio output |
| Vibration motor | 1 | PWM/analog output |

The controller also breaks out power and ground on the edge pads. Check the current Kitronik datasheet for the exact expansion-pad labels, because they have changed between revisions.

### Detection

Every controller-aware program starts with:

```python
controller = False
if pin15.read_digital() == 1:
    controller = True
```

Fire 1 is pulled high when idle, so a connected controller makes pin 15 read `1`. The detection happens once, before the main loop. If a bare board's pin 15 floats high, the program can mistake it for a controller. The fix, if it becomes a problem, is a pull-down resistor or a more robust detection check.

### Audio routing

```python
if controller == False:
    music_pin = None
else:
    music_pin = pin2
```

When `music_pin` is `None`, the V2's built-in speaker is used. When a controller is attached, audio goes to the piezo buzzer on pin 2. The programs do not route audio to pin 0.

### Touch mode

Programs that use the touch pins call:

```python
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
```

Only do this when no controller is attached. On the controller, pin 1 is the vibration motor and pin 2 is the buzzer, so setting capacitive touch mode would break the hardware output.

### Gestures

- `accelerometer.is_gesture('face down')` means the LED matrix is facing the table.
- `accelerometer.is_gesture('down')` means the logo end is pointing down. Blackjack uses this for its status gesture.
- `accelerometer.is_gesture('up')`, `'left'`, and `'right'` are tilt directions relative to the logo. Breakout uses them to steer.
- Shake is `accelerometer.is_gesture('shake')`.
