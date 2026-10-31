# Flashing and saves

This is the long version of the install instructions. The short version is in the top-level [README](../README.md).

## Check the board

All eleven programs need a **micro:bit V2**. The V2 has a built-in speaker, a microphone, and a touch-sensitive logo. The V1 does not support the modules these programs use.

You also need a **USB data cable**. Some cables only carry power and will not show the `MICROBIT` drive.

You do **not** need headphones or an external speaker. The V2's built-in speaker is the default output. With the controller attached, sound comes from the controller's buzzer.

## One program at a time

The board can hold only one program at a time. The program's save lives in the same flash filesystem.

**Flashing a new program replaces the old program and erases its filesystem, including its save.** This is true whether you flash a different game or the same game again. There is no way to keep several games or several saves on one board.

## Install from the Python Editor

This is the supported route for the `.py` files in this repository.

1. Open [python.microbit.org](https://python.microbit.org) in a browser.
2. Open the game's `.py` file in the editor. You can use the editor's **Open** button, or copy the text and paste it into the code area.
3. Connect the micro:bit with the USB cable.
4. Press **Send to micro:bit**. The editor builds a `.hex`, flashes it, and the program starts.
5. If you want a `.hex` file to keep, use the editor's save/download option. You can drag that `.hex` onto the `MICROBIT` drive later.

The editor is a web app. Its accessibility varies with the browser and screen reader, and the code area is a text editor, so use your usual reading and editing commands. The **Send to micro:bit** button is a normal button. If the editor is difficult to use, ask a sighted helper to send the file once, or use a `.hex` that someone else built.

## Install from a `.hex`

1. Plug the micro:bit into the computer with the USB cable.
2. Wait for a drive called `MICROBIT` to appear.
3. Copy the `.hex` file onto the `MICROBIT` drive.
4. The yellow LED on the back of the board blinks while the file copies.
5. The board restarts and the program begins.

Do not unplug the board while the yellow LED is blinking. Wait for it to stop.

The `MICROBIT` drive is a flashing target for `.hex` files. It is **not** a normal window into the MicroPython filesystem.

## Why copying a `.py` does not work

A `.py` file, including one named `main.py`, cannot simply be copied onto the board and run. The program has to be embedded in the runtime by the editor or by a `.hex`. Copying a `.py` to the `MICROBIT` drive only puts a file in the drive's staging area; it does not install the program.

Use the editor's **Send to micro:bit** button or a prebuilt `.hex`.

## Powering on and off

- **Turn the board off:** hold the reset button for about three seconds.
- **Turn it back on:** press the reset button quickly.
- **Restart the current program:** press the reset button quickly. This does not erase the save.
- **Replace the program:** flash a new `.hex`. This erases the old program and its filesystem.

## Saves

Games that keep progress write a save file in the board's internal filesystem:

- **MicroFidget** keeps high scores.
- **Breakout** keeps score, lives, and speed after a lost life.
- **Zombie Dice**, **Tossup**, **36**, and **Flip 7** keep a game in progress.
- **Composer** keeps your saved tunes.

Simon, Blackjack, Mastermind, and Vibration Challenge have no save.

A save survives a reset or unplugging while the same program stays installed. It is erased when you flash another program or reflash the same one.

### Clearing a save

Reflash the program. That replaces the program and its filesystem, so the game starts fresh. There is no normal file manager on the `MICROBIT` drive for deleting the save on its own.

### Backing up Composer tunes

The filesystem is not exposed as a normal drive. A specialised tool such as the Mu editor's files pane may be able to read the files, but this is best-effort. Treat Composer tunes as temporary: the next flash will erase them. If a tune matters, write it down or recreate it after the flash.

## Controller setup

1. Slide the micro:bit into the controller's edge connector. It should seat firmly.
2. Insert two AA batteries.
3. Power on the controller.
4. Press the micro:bit's reset button once, so the game detects the controller at startup.

Do not hold **Fire 1** while the board starts. The games use Fire 1 to detect the controller, and holding it can make the board think no controller is attached.

If the game does not respond to the direction buttons or fire buttons, unplug the micro:bit, reseat it, and reset. The detection happens once, at startup, not continuously.

For controller-aware games, the buzzer is used for sound, so you do not need a separate speaker. The vibration motor is used by Simon and Vibration Challenge. MicroFidget does not use the controller and still uses the built-in speaker.

## Troubleshooting

### The `MICROBIT` drive does not appear

- Try a different USB cable. Charge-only cables are common.
- Try a different USB port.
- Check that the board is a V2 and that it powers on.
- On Windows, open File Explorer and look under "This PC". If it still does not appear, open Disk Management.

### The `.hex` copies but the game does not start

- Press the reset button quickly.
- Check that the file finished copying; wait for the yellow LED to stop blinking.
- Rebuild the `.hex` with a V2 runtime, or send the `.py` again from the editor.

### The `.py` is on the drive but nothing runs

This is expected. A `.py` file is not a program until the editor embeds it in a `.hex`. Use **Send to micro:bit**.

### There is no sound on a bare board

- The V2 built-in speaker is the output. Check that it is not covered and that the room is quiet enough.
- Check the program's volume, if it has one.
- With the controller, check the batteries and the buzzer. MicroFidget does not support the controller.

### The controller is not detected

- Reseat the micro:bit.
- Replace the batteries.
- Press reset after plugging in.
- Check that the board is a V2 and that the program supports the controller (MicroFidget does not).

### The save disappeared

That is expected after flashing a program. The new program has a new filesystem. If you flash the same game again, it also starts fresh.

### I cannot find the save file

The `MICROBIT` drive is for `.hex` files, not for browsing the MicroPython filesystem. Use Mu or another specialised tool if you need to inspect it, and expect the next flash to erase it.

### The board resets itself

Some games call `reset()` on purpose when you run out of coins or lives. If it happens at another time, connect to the REPL (the interactive Python prompt on the board) and read the error.
