from microbit import *
import random, music
import audio

controller = False
if pin15.read_digital() == 1:
    controller = True

if controller == False:
    music_pin = None
else:
    music_pin = pin2

confirm = False
check = False

def update():
    global confirm, check
    if controller == False:
        # was_pressed() is better here because it remembers a press
        # even if it happened during a short blocking call
        confirm = button_a.was_pressed()
        check = button_b.was_pressed()
    else:
        confirm = (pin15.read_digital() == 0)
        check = (pin16.read_digital() == 0)

def wait_release():
    # Mainly useful for controller mode, where buttons are read as held/not held
    if controller == False:
        return
    while True:
        update()
        if not confirm and not check:
            break
        sleep(10)

def vibrate(power=1023, duration=100):
    pin1.write_analog(power)
    sleep(duration)
    pin1.write_analog(0)

def play_value(value, duration):
    step = 20
    start = running_time()

    if controller:
        pin1.write_analog(value)
        while running_time() - start < duration:
            update()
            if confirm:
                pin1.write_analog(0)
                return True
            sleep(step)
        pin1.write_analog(0)
    else:
        music.pitch(value, wait=False, pin=music_pin)
        while running_time() - start < duration:
            update()
            if confirm:
                music.stop()
                return True
            sleep(step)
        music.stop()

    return False
def count(sifer=0):
    if sifer == 0:
        audio.play(audio.SoundEffect(freq_start=131, freq_end=131, duration=250), pin=music_pin)
        return

    while sifer >= 100:
        audio.play(audio.SoundEffect(freq_start=1175, freq_end=1175, duration=320), pin=music_pin)
        sifer -= 100
        sleep(160)

    while sifer >= 10:
        audio.play(audio.SoundEffect(freq_start=784, freq_end=784, duration=220), pin=music_pin)
        sifer -= 10
        sleep(160)

    while sifer >= 1:
        audio.play(audio.SoundEffect(freq_start=523, freq_end=523, duration=90), pin=music_pin)
        sifer -= 1
        sleep(160)

extra_life_tones = [1319, 1568, 2637, 2093, 2349, 3136]

state = 'waiting'
score = 0
lives = 3
reference = 0
value = 0
low_range = 900
wrong_threshold = 200
correct_probability = 35
length = 1000
perfect_answers = 0

while True:
    update()

    if state == 'waiting':
        display.show(lives)

        if check:
            display.scroll(str(score), delay=50)
            count(score)
            sleep(250)
            count(lives)
            wait_release()

        elif confirm:
            display.clear()
            wait_release()
            state = 'reference'

    elif state == 'reference':
        reference = random.randint(low_range, 1023)

        for i in range(3):
            if controller == True:
                vibrate(reference, 250)
            else:
                music.pitch(reference, duration=250, pin=music_pin)
            sleep(300)

        sleep(1500)
        update()
        state = 'game'

    elif state == 'game':
        probability = random.randint(0, 99)

        if probability < correct_probability:
            value = reference
        else:
            value = random.randint(0, 1023)
            while abs(value - reference) <= wrong_threshold:
                value = random.randint(0, 1023)

        if play_value(value, length):
            state = 'check'
        else:
            sleep(100)

    elif state == 'check':
        if abs(value - reference) > 100:
            display.show(Image.NO)
            audio.play(audio.SoundEffect(freq_start=131, freq_end=131, duration=300, vol_end=255), pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=104, freq_end=104, duration=300, vol_end=255), pin=music_pin)
            sleep(500)

            lives -= 1
            if lives == 0:
                state = 'gameover'
            else:
                state = 'waiting'

        else:
            display.show(Image.HAPPY)
            audio.play(audio.SoundEffect(freq_start=1047, freq_end=1047, duration=75), pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=1568, freq_end=1568, duration=75), pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=2093, freq_end=2093, duration=400), pin=music_pin)

            if value == reference:
                points = 10
                perfect_answers += 1
                if perfect_answers == 5:
                    display.show(Image.FABULOUS)
                    for i in range(len(extra_life_tones)):
                        audio.play(audio.SoundEffect(
                            freq_start=extra_life_tones[i],
                            freq_end=extra_life_tones[i],
                            duration=120
                        ), pin=music_pin)
                    lives += 1
                    perfect_answers = 0
            else:
                points = 5

            score += points

            display.scroll(str(points), delay=50)
            count(points)

            if low_range > 200:
                low_range -= 20
            if length > 300:
                length -= 20
            if correct_probability > 11:
                correct_probability -= 2
            if wrong_threshold > 30:
                wrong_threshold -= 10

            state = 'waiting'

    elif state == 'gameover':
        display.show(Image.SAD)
        audio.play(audio.SoundEffect(freq_start=2093, freq_end=262, duration=1300, vol_end=255), pin=music_pin)
        audio.play(audio.SoundEffect(freq_start=30, freq_end=30, waveform=audio.SoundEffect.WAVEFORM_NOISE, duration=1000), pin=music_pin)

        display.scroll(str(score), delay=50)
        count(score)

        score = 0
        lives = 3
        low_range = 900
        perfect_answers = 0
        wrong_threshold = 200
        correct_probability = 35
        length = 1000
        state = 'waiting'