# Composer

Build, play, and save your own melodies on the micro:bit. A small monophonic sequencer with notes, note lengths, rests, and tempo.

## At a glance

| Item | Detail |
| --- | --- |
| Players | 1 |
| Controller | Optional |
| Speech | Yes, for menus, counts, and tempo |
| Save | Tunes, until another program is flashed |
| Difficulty | Moderate |
| Hardware | micro:bit V2, or the micro:bit with the controller |

## What it is

Composer lets you place notes one at a time, set how long each note lasts, add rests, change the octave, and set the tempo. You can play the sequence back in a loop and save it to the board. Several sequences can be stored, loaded, edited, and deleted while Composer stays installed.

It is monophonic: one note sounds at a time. That keeps the interface simple and the memory small.

## Before you play

- Use a micro:bit V2.
- On a bare board, the V2's built-in speaker provides the sound. No headphones or external speaker are needed.
- With the controller, the buzzer provides the sound.
- Sequences survive a reset or unplug while Composer stays installed. Flashing another program, or reflashing Composer, erases them. The filesystem is not normally visible as a drive; see [flashing-and-saving.md](../../docs/flashing-and-saving.md).

## Controls

### Bare micro:bit

| Action | Control |
| --- | --- |
| Previous note, lower value, or earlier sequence | Touch pin 1 |
| Next note, higher value, or later sequence | Touch pin 2 |
| Action A: add a note, add a rest, or lower the tempo | Button A |
| Action B: switch to length mode, delete, or raise the tempo | Button B |
| Shift: enter or leave the shift menu | Touch the logo |
| Play or stop; save while in shift mode | Turn the display face down |

### Kitronik :GAME Controller

| Action | Control |
| --- | --- |
| Previous note, lower value, or earlier sequence | Joypad Left |
| Next note, higher value, or later sequence | Joypad Right |
| Action A: add a note, add a rest, or lower the tempo | Fire 1 |
| Action B: switch to length mode, delete, or raise the tempo | Fire 2 |
| Shift: enter or leave the shift menu | Joypad Up |
| Play or stop; save while in shift mode | Joypad Down |

The controls change meaning with the current mode. The tables below explain each mode.

## How to play

### Starting up

- If the board has saved sequences, it starts in the **sequence menu** and says "Select sequence."
- If there are no saved sequences, it starts in **pitch mode** and says "Creating new sequence."

### The sequence menu

The display shows the selected sequence number, or a plus sign for a new sequence.

| Action | What it does |
| --- | --- |
| Previous or next | Move through the saved sequences and the new-sequence slot. The number is spoken. |
| Action A (Button A or Fire 1) | Load the selected sequence, or start a new one. The board says "Loaded" or "Creating new sequence." |
| Action B (Button B or Fire 2) | Ask to delete the selected sequence. The board asks for a downward confirmation. |
| Face down or Joypad Down | Confirm the deletion. The sequence is removed and a low three-note phrase plays. |
| Any other button or a shake | Cancel the deletion. The board says "Cancelled." |
| Shake, or tap Shift on the controller | Hear how many notes are in the sequence and its tempo in BPM. |

You cannot delete the new-sequence slot; it is not a saved sequence.

### Pitch mode

This is where you choose the note.

- The display shows the note name, such as C4 or F#5.
- **Previous** and **Next** move down and up one semitone. Each change plays the note.
- **Action A** adds the current note to the sequence, with the current length. The board shows a tick and plays a short high beep.
- **Action B** switches to **length mode**.
- **Face down** (or **Joypad Down**) starts or stops looped playback.
- **Shift** (the logo or Joypad Up) opens the **shift menu**.

The note range is C2 to B7, six octaves. A new sequence starts on C4.

### Length mode

This is where you choose how long the note lasts.

- The display shows a number from 1 to 16. This is the number of ticks.
- **Previous** and **Next** change the length, and the note is previewed at the new length.
- **Action A** adds the current note with the current length.
- **Action B** returns to **pitch mode**.
- **Face down** (or **Joypad Down**) starts or stops looped playback.
- **Shift** opens the **shift menu**.

A tick is one unit of the current tempo. With the default four ticks per beat, a length of 4 is one beat and a length of 1 is a quarter beat. Longer notes use more ticks.

### The shift menu

The display shows a question mark. This menu holds the actions that do not fit on the main screen.

| Action | What it does |
| --- | --- |
| Previous | Move the current note down one octave. |
| Next | Move the current note up one octave. |
| Action A | Add a rest with the current length. |
| Action B | Delete the last note or rest. The board plays the last few notes as confirmation. |
| Shift again | Return to pitch mode. |
| Shake | Enter **tempo mode**. |
| Face down or Joypad Down | Save the sequence and return to the menu. |

Saving an existing sequence overwrites it. Saving a new sequence adds it to the first free slot.

### Tempo mode

The display scrolls the tempo and a repeated click plays so you can hear the beat.

| Action | What it does |
| --- | --- |
| Action A | Lower the tempo by 1 BPM, down to 40. |
| Action B | Raise the tempo by 1 BPM, up to 320. |
| Shift, or Joypad Down | Stop the click, return to pitch mode, and speak the new tempo. |

The tempo is saved with the sequence.

## What you hear

| Sound | Meaning |
| --- | --- |
| A musical note | The note you selected, or the note being added |
| A short high beep | A note or rest was added |
| A short beep when switching to length mode | The board is now editing note length |
| A short beep when switching to pitch mode | The board is now editing pitch |
| A short higher beep when opening shift | The shift menu is open |
| A rising four-note fanfare | The sequence was saved |
| A low three-note phrase | A sequence was deleted |
| A repeated click | Tempo mode; the click follows the BPM |
| Spoken sequence numbers | While moving through the menu |
| Spoken "Loaded" or "Creating new sequence" | After choosing a menu item |
| Spoken note count and BPM | When you ask for sequence information |
| Spoken "N BPM" | When you leave tempo mode |

The note names are shown on the display but are not spoken. Speech is reserved for menus and counts; speaking every note would make editing slow. You navigate by pitch and by semitone steps.

## Saving and loading

- Each saved sequence stores its tempo and its list of notes. A note looks like `C4:4` or `F#5:2`: the note name, then a colon, then the length in ticks. A rest looks like `R:4`.
- Sequences live in Composer's internal filesystem while Composer stays installed. They survive a reset or unplug, but flashing another program or reflashing Composer erases them.
- The files are not normally visible on the `MICROBIT` drive. A specialised tool such as the Mu editor may be able to extract them, but treat that as best-effort.
- There is no reliable way to keep a backup alongside another game, because only one program fits on the board.

## Accessibility notes

- The menu, sequence numbers, note counts, and tempo are spoken. Deletion is confirmed with a deliberate second action.
- Note names are shown, not spoken, because speech cannot be interrupted and speaking every note would make editing slow. You can still compose by ear: each semitone step plays the new pitch, and the shift menu jumps by an octave.
- Playback loops until you stop it. Press the same control again to stop.
- On a bare board, play, stop, and save use the face-down gesture. On the controller, Joypad Down is easier.
- There is no undo beyond deleting the last note in the shift menu.
- There is no polyphony. If you want chords, you need a different program.

## Tips

- Start with a simple scale or a familiar tune. Add one note at a time and play it back often.
- Use the shift menu to jump octaves instead of pressing Next many times.
- Add a rest at the end if you want a gap before the loop repeats.
- Set the tempo last. A slow tempo makes it easier to hear each note while composing.
- Save before you experiment. Loading a saved sequence is the easiest way to undo a big change.
- Delete the last note with Action B in the shift menu; it is the closest thing to an undo.
- If the board has no sequences, it goes straight to pitch mode. Save once to create the first sequence, and the menu will appear next time.
