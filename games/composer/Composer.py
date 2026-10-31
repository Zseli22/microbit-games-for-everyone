from microbit import *
import music, os, speech

controller = False
if pin15.read_digital() == 1:
    controller = True

if controller == False:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    music_pin = None
else:
    music_pin = pin2

# Controller mapping: pin 12/13 adjust values, pin 8 shifts, pin 14 is the
# context-sensitive special action, and pins 15/16 act as buttons A/B.
previous = False
next_item = False
action_a = False
action_b = False
shift = False
special = False
shift_pressed = False
special_pressed = False
previous_shift = False
previous_special = False

def update():
    global previous, next_item, action_a, action_b, shift, special
    global shift_pressed, special_pressed, previous_shift, previous_special
    if controller == False:
        previous = pin1.is_touched()
        next_item = pin2.is_touched()
        action_a = button_a.is_pressed()
        action_b = button_b.is_pressed()
        shift = pin_logo.is_touched()
        special = False
    else:
        previous = pin12.read_digital() == 0
        next_item = pin13.read_digital() == 0
        action_a = pin15.read_digital() == 0
        action_b = pin16.read_digital() == 0
        shift = pin8.read_digital() == 0
        special = pin14.read_digital() == 0

    shift_pressed = shift and not previous_shift
    special_pressed = special and not previous_special
    previous_shift = shift
    previous_special = special

def is_face_down():
    return accelerometer.is_gesture('face down') or special_pressed


notes = []
note_names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
for i in range(2, 8):
    for j in range(len(note_names)):
        notes.append(str(note_names[j]) + str(i))

note_index = 24  # Start on C4
sequence = []
ticks = 1        # Default note length
mode = 'pitch'
playing = False
tempo = 120

editing_seq_index = None

def parse_index_from_filename(fn):
    if fn.startswith("seq") and fn.endswith(".txt"):
        return int(fn[3:-4])
    return -1 # Return an invalid index if the filename is wrong

def get_sorted_sequences():
    sequence_files = []
    for f in os.listdir():
        if f.startswith("seq") and f.endswith(".txt"):
            sequence_files.append(f)
    sequence_files.sort(key=parse_index_from_filename)
    return sequence_files

def find_next_free_index(sorted_files):
    for i, filename in enumerate(sorted_files):
        file_index = parse_index_from_filename(filename)
        if i != file_index:
            return i
    return len(sorted_files)
def save_sequence_to_index(idx, tempo_val, seq):
    filename = "seq{}.txt".format(idx)
    with open(filename, "w") as f:
        f.write(str(int(tempo_val)) + "\n")
        f.write(",".join(seq))

def load_sequence_simple(filename):
    with open(filename, "r") as f:
        tempo_str = f.readline().strip()
        seq_str = f.readline().strip()

    loaded_tempo = int(tempo_str)
    
    if seq_str:
        loaded_sequence = seq_str.split(',')
    else:
        loaded_sequence = []

    return loaded_tempo, loaded_sequence


def play_note():
    if mode == 'pitch':
        display.show(notes[note_index], wait=False, clear=True)
    elif mode == 'length':
        display.show(ticks, wait=False, clear=True)
    music.play(str(notes[note_index]) + ':' + str(ticks), wait=False, pin=music_pin)


seq_files = get_sorted_sequences() 
current_seq_id = 0                  

if seq_files:
    mode = "menu"
    speech.say('Select sequence.', pin=music_pin)
else:
    mode = "pitch"
    speech.say('Creating new sequence.', pin=music_pin)


while True:
    update()

    if mode == "menu":
        if current_seq_id < len(seq_files):
            display.show(str(current_seq_id))
        else:
            display.show("+") 

        if previous and current_seq_id > 0:
            current_seq_id -= 1
            speech.say("{}".format(current_seq_id), pin=music_pin)
            sleep(250)

        elif next_item and current_seq_id < len(seq_files):
            current_seq_id += 1
            if current_seq_id < len(seq_files):
                speech.say("{}".format(current_seq_id), pin=music_pin)
            else:
                speech.say("New sequence.", pin=music_pin)
            sleep(250)

        elif action_a:
            if current_seq_id == len(seq_files): 
                sequence = []
                tempo = 120
                editing_seq_index = None
                speech.say('Creating new sequence.', pin=music_pin)
            else: 
                filename = seq_files[current_seq_id]
                tempo, sequence = load_sequence_simple(filename)
                editing_seq_index = current_seq_id
                speech.say('Loaded.', pin=music_pin)
            mode = "pitch"
            music.set_tempo(bpm=tempo)
            playing = False
            sleep(200)
            continue

        elif action_b and current_seq_id < len(seq_files): # Delete
            speech.say("Press down to delete.", pin=music_pin)
            sleep(500)
            while is_face_down() is False:
                update()
                if action_a or action_b or accelerometer.is_gesture("shake"):
                    speech.say("Cancelled.", pin=music_pin)
                    sleep(200)
                    break
            else:
                os.remove(seq_files[current_seq_id])
                seq_files = get_sorted_sequences() 
                if current_seq_id >= len(seq_files):
                    current_seq_id = len(seq_files)
                music.pitch(263,duration=75, pin=music_pin)
                music.pitch(131,duration=75, pin=music_pin)
                music.pitch(65,duration=75, pin=music_pin)

        elif (accelerometer.is_gesture("shake") or (controller and shift_pressed)) and current_seq_id < len(seq_files): # Get info
            filename = seq_files[current_seq_id]
            t, s = load_sequence_simple(filename)
            display.scroll(str(len(s)), delay=50)
            speech.say("{} notes.".format(len(s)), pin=music_pin)
            display.scroll(str(t), delay=50)
            speech.say("{} B P M.".format(t), pin=music_pin)
            sleep(500)

    elif mode == 'pitch':
        if previous and note_index > 0:
            note_index -= 1
            play_note()
            sleep(120)
        elif next_item and note_index < len(notes) - 1:
            note_index += 1
            play_note()
            sleep(120)
        elif action_b:
            mode = 'length'
            music.pitch(1000, duration=30, wait=False, pin=music_pin)
            display.show('L')
            sleep(200)

    elif mode == 'length':
        if previous and ticks > 1:
            ticks -= 1
            music.stop()
            sleep(20)
            play_note()
            sleep(300)
        elif next_item and ticks < 16:
            ticks += 1
            music.stop()
            sleep(30)
            play_note()
            sleep(300)
        elif action_b:
            mode = 'pitch'
            music.pitch(500, duration=30, wait=False, pin=music_pin)
            display.show('P', wait=False)
            sleep(200)

    if mode in ('pitch', 'length'):
        if action_a: # Add note to sequence
            sequence.append(notes[note_index] + ':' + str(ticks))
            music.pitch(2000, duration=30, wait=False, pin=music_pin)
            display.show(Image.YES)
            sleep(500)

        if is_face_down() and len(sequence) > 0: # Play/Stop
            if not playing:
                playing = True
                music.pitch(2000, duration=120, pin=music_pin)
                display.show(Image.MUSIC_QUAVERS)
                sleep(200)
                music.play(sequence, wait=False, loop=True, pin=music_pin)
            else:
                music.stop()
                display.clear()
                playing = False
                sleep(500)

        if shift_pressed:
            mode = 'shift'
            music.pitch(1500, duration=100, wait=False, pin=music_pin)
            display.show('?')
            sleep(300)
            continue

    if mode == 'shift':
        if previous and note_index - 12 >= 0: # Octave down
            note_index -= 12
            play_note()
            sleep(120)
        elif next_item and note_index + 12 < len(notes): # Octave up
            note_index += 12
            play_note()
            sleep(120)
        elif action_a: 
            sequence.append('R:' + str(ticks))
            music.pitch(250, duration=30, wait=False, pin=music_pin)
            display.show('R')
            sleep(500)
        elif action_b and len(sequence) > 0: # Delete last note
            sequence.pop()
            display.show(Image.SCISSORS)
            music.play(sequence[-4:], pin=music_pin)
            sleep(300)
        elif shift_pressed: 
            mode = 'pitch'
            display.show('P', wait=False)
            music.pitch(750, duration=100, wait=False, pin=music_pin)
            sleep(300)
        elif accelerometer.is_gesture('shake'): 
            mode = 'set_tempo'
            sleep(200)

        elif is_face_down(): 
            if editing_seq_index is None: 
                new_idx = find_next_free_index(seq_files)
                save_sequence_to_index(new_idx, tempo, sequence)
            else: 
                filename = seq_files[editing_seq_index]
                idx_num = parse_index_from_filename(filename)
                save_sequence_to_index(idx_num, tempo, sequence)
            
            music.pitch(1046,duration=75, pin=music_pin); music.pitch(1175,duration=75, pin=music_pin); music.pitch(1568,duration=75, pin=music_pin); music.pitch(2093,duration=180, pin=music_pin)
            mode = "menu"
            playing = False
            seq_files = get_sorted_sequences() 
            sleep(300)

    elif mode == 'set_tempo':
        display.scroll(tempo, delay=70, wait=False)
        if not playing:
            music.set_tempo(bpm=tempo)
            music.play(['G5:1','R:1','R:1','R:1'], loop=True, wait=False, pin=music_pin)
            playing = True
        
        if action_a and tempo > 40:
            tempo -= 1
            music.set_tempo(bpm=tempo)
            sleep(50)
        elif action_b and tempo < 320:
            tempo += 1
            music.set_tempo(bpm=tempo)
            sleep(50)
        if shift_pressed or (controller and special_pressed): #
            music.stop()
            playing = False
            mode = 'pitch'
            music.pitch(1568, duration=100, wait=False, pin=music_pin)
            speech.say(str(tempo)+' B P M.', pin=music_pin)
            sleep(300)
