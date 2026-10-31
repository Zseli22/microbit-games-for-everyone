from microbit import *
import random,speech
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
controller=False
if pin15.read_digital()==1:
    controller=True
if controller==False:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    music_pin=None
elif controller==True:
    music_pin=pin2
symbols=[('0',523),('1',587),('2',659),('3',699),('4',784),('5',880),('6',988),('7',1046),('8',1175),('9',1319),('A',1397),('B',1568),('C',1760),('D',1976),('E',2093)]
code=[]
player_code=[]
history=[]
win_tones=[587,698,932,1047,1175,1397,1865]
def update():
    global up, down, left, right, confirm
    if controller==False:
        up=pin_logo.is_touched()
        down=pin1.is_touched() or pin2.is_touched()
        left=button_a.is_pressed()
        right=button_b.is_pressed()
        confirm=accelerometer.is_gesture('shake')
    elif controller==True:
        up=pin8.read_digital()==0
        down=pin14.read_digital()==0
        left=pin12.read_digital()==0
        right=pin13.read_digital()==0
        confirm=pin15.read_digital()==0
def show(value=0):
    global symbols
    display.show(symbols[value][0])
    audio.play(audio.SoundEffect(freq_start=symbols[value][1],freq_end=symbols[value][1],duration=120),pin=music_pin)
def main():
    global symbols,code,player_code,win_tones,history
    settings=[{'name': 'ax7vey5lax6bax8l sih6mbax6lz?', 'current': 8, 'minimum': 5, 'maximum': len(symbols)},{'name': 'leh4nxth ax7v kow6d?', 'current': 4, 'minimum': 3, 'maximum': 5},{'name': 'gey5m dih7fih6kax6ltiy6?', 'current': 0, 'minimum': 0, 'maximum': 2}]
    result=0
    wrong_place=0
    turns=0
    selection=0
    state='waiting'
    speech.pronounce('weh4lkah6m tax8 mae4ster6may8nd.',pin=music_pin)
    while True:
        update()
        if state=='waiting':
            display.show(Image.HEART)
            if left==True:
                state='setup'
            elif right==True:
                if selection==len(settings)-1:
                    selection=0
                else:
                    selection+=1
                speech.pronounce(settings[selection]['name'],pin=music_pin)
                speech.say(str(settings[selection]['current'])+'.',pin=music_pin)
            elif up==True and settings[selection]['current'] < settings[selection]['maximum']:
                settings[selection]['current']+=1
                speech.say(str(settings[selection]['current'])+'.',pin=music_pin)
            elif down==True and settings[selection]['current']>settings[selection]['minimum']:
                settings[selection]['current']-=1
                speech.say(str(settings[selection]['current'])+'.',pin=music_pin)
        elif state=='setup': 
            code.clear()
            turns=0
            available_indices = list(range(settings[0]['current']))
            for _ in range(settings[1]['current']):
                chosen_index = random.choice(available_indices)
                code.append(chosen_index)
                available_indices.remove(chosen_index)
            player_code = [0] * settings[1]['current']
            selection=0
            speech.pronounce('bih5gih3n.',pin=music_pin)
            state='game'
        elif state=='game':
            if left==True or right==True or up==True or down==True:
                if (left==True and selection==0) or (right==True and selection==settings[1]['current']-1) or (down==True and player_code[selection]==0) or (up==True and player_code[selection]==settings[0]['current']-1):
                    audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=200),pin=music_pin)
                    sleep(100)
                elif left==True:
                    selection-=1
                elif right==True:
                    selection+=1
                elif down==True:
                    player_code[selection]-=1
                elif up==True:
                    player_code[selection]+=1
                show(player_code[selection])
                sleep(120)
            if confirm==True:
                state='check'
        elif state=='check':
            for i in range(len(player_code)):
                show(player_code[i])
                sleep(100)
            display.clear()
            sleep(500)
            if len(player_code) != len(set(player_code)):
                display.show(Image.NO)
                audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=70,vol_end=255),pin=music_pin)
                audio.play(audio.SoundEffect(freq_start=104,freq_end=104,duration=130,vol_end=255),pin=music_pin)
                speech.pronounce('now5 duw4plih5kax7ts ax8law4d.',pin=music_pin)
                state='game'
            else:
                turns+=1
                for i in range(settings[1]['current']):
                    if settings[2]['current']==0:
                        if code.count(player_code[i])>0:
                            result+=1
                    elif settings[2]['current']>0:
                        if code.count(player_code[i])>0:
                            if player_code[i]==code[i]:
                                result+=1
                                if settings[2]['current']==1:
                                    display.set_pixel(i,0,9)
                                    audio.play(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=300),pin=music_pin)
                            else:
                                wrong_place+=1
                                if settings[2]['current']==1:
                                    display.set_pixel(i,2,9)
                                    audio.play(audio.SoundEffect(freq_start=523,freq_end=523,duration=300),pin=music_pin)
                        else:
                            if settings[2]['current']==1:
                                display.set_pixel(i,4,9)
                                audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=300),pin=music_pin)
                if result==0 and wrong_place==0:
                    display.show(Image.MEH)
                    audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=300),pin=music_pin)
                    state='game'
                else:
                    if settings[2]['current']!=1:
                        for i in range(result):
                            audio.play(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=300),pin=music_pin)
                            display.set_pixel(i,0,9)
                        for i in range(wrong_place):
                            display.set_pixel(i+result,2,9)
                            audio.play(audio.SoundEffect(freq_start=523,freq_end=523,duration=300),pin=music_pin)
                if result==settings[1]['current']:
                    state='win'
                else:
                    state='game'
                result=0
                wrong_place=0
        elif state=='win':
            speech.pronounce('yuw5 faw3nd may6 kow8d.',pin=music_pin)
            display.clear()
            display.show(Image.HAPPY)
            for i in range(len(win_tones)):
                audio.play(audio.SoundEffect(freq_start=win_tones[i],freq_end=win_tones[i],duration=70),pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=400),pin=music_pin)
            display.clear()
            sleep(500)
            display.scroll(turns,delay=50)
            speech.say('It took you, '+str(turns)+', guesses.',pin=music_pin)
            display.clear()
            selection=0
            sleep(300)
            state='waiting'
main()