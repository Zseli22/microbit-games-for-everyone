from microbit import *
import random
import music
import speech
tones=[440,330,220,262,110]
colors=[Image('99999:00000:00000:00000:00000'),Image('00009:00009:00009:00009:00009'),Image('00000:00000:00000:00000:99999'),Image('90000:90000:90000:90000:90000'),Image.SQUARE]

comments=['keh4er tax7 teh5st yix7r meh4tax7l ax8gehn?',
          'waa6ch dhax5 siy4kwax4ns, kaa3piy5 dhax6 siy7kwax8ns. ih5ts naa4t raa4kih6t say7ax8ns.',
         'iy5vax7n ay3, ax8 tay6niy7 ser4kih6t boh6rd, kae7n stih2l dih7fiy8t yuw8.',
         'per7/hae5ps ay6 shuh7d gow7 ax8 lih8tax8l slow4er7 foh7r yuw7 neh7kst tay8m.',
         'ae7nd dhae3ts wax7t /hae7pax8nz tax8 dhow5z /huw7 dow4nt pey6 ax7teh3nshax8n.']
verygood_comments=['yuw6 dih6d kway4t weh5l, bah7t dow6nt leh8t ih8t geh7t tax7 yix8r /heh5d.',
'ay7m staa5rtih6nx tax7 siy5 sah6m pax5teh3nshax6l ih7n yuw8.',
'mey6 ay6 kao4l dhae6t bih7gih5ner7 z lahk?',
'yuw7 waa6cht - dhax5 siy4kwax4ns, yuw5 kaa3piy5d dhax6 siy7kwax8ns. bah5t yuw4 stih3l dih5dax6nt ih6mpreh7s miy8.']
state='waiting'
mode=0
modes=['normal', 'random', 'reverse', 'tricky']
tone=-1
sequence=[]
leftovers=[]
speed=600
saved_speed=600
correct=False
current=-1
controller=False
if pin15.read_digital()==1:
    controller=True
if controller==False:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    music_pin=None
elif controller==True:
    music_pin=pin2
def update():
    global up, down, left, right
    if controller==False:
        up=pin_logo.is_touched()
        down=pin1.is_touched() or pin2.is_touched()
        left=button_a.is_pressed()
        right=button_b.is_pressed()
    elif controller==True:
        up=pin8.read_digital()==0
        down=pin14.read_digital()==0
        left=pin12.read_digital()==0
        right=pin13.read_digital()==0

def main():
    global state,mode,tone,sequence,speed,correct,current,saved_speed,leftovers
    while True:
        update()
        if state=='waiting':
            if up==True:
                if len(sequence)>0:
                    if sequence[current]==0:
                        while up:
                            display.show(colors[0])
                            music.pitch(tones[0],duration=75,wait=False,pin=music_pin)
                            sleep(75)
                            update()
                        correct=True
                    else:
                        state='fail'
                else:
                    if saved_speed>200:
                        music.pitch(1760,duration=50,wait=True,pin=music_pin)
                        sleep(200)
                        saved_speed-=50
            if right==True:
                if len(sequence)>0:
                    if sequence[current]==1:
                        while right:
                            display.show(colors[1])
                            music.pitch(tones[1],duration=75,wait=False,pin=music_pin)
                            sleep(75)
                            update()
                        correct=True
                    else:
                        state='fail'
                else:
                    speed=saved_speed
                    state='game'
            if down==True:
                if len(sequence)>0:
                    if sequence[current]==2:
                        while down:
                            display.show(colors[2])
                            music.pitch(tones[2],duration=75,wait=False,pin=music_pin)
                            sleep(75)
                            update()
                        correct=True
                    else:
                        state='fail'
                else:
                    if saved_speed<600:
                        music.pitch(880,duration=50,wait=True,pin=music_pin)
                        sleep(200)
                        saved_speed+=50
            if left==True:
                if len(sequence)>0:
                    if sequence[current]==3:
                        while left:
                            display.show(colors[3])
                            music.pitch(tones[3],duration=75,wait=False,pin=music_pin)
                            sleep(75)
                            update()
                        correct=True
                    else:
                        state='fail'
                else:
                    if mode==len(modes)-1:
                        mode=0
                    else:
                        mode+=1
                    display.show(colors[mode])
                    music.pitch(tones[mode],duration=200,wait=True,pin=music_pin)
                    display.clear()
            else:
                music.stop()
                display.clear()
                if correct==True:
                    correct=False
                    current+=1
                    while current<len(sequence) and sequence[current]==4:
                        current+=1
                    if current==len(sequence):
                        if mode==2:
                            sequence.reverse()
                        if mode==3:
                            replace=0
                            for i in range(len(sequence)):
                                if sequence[i]==4:
                                    sequence[i]=leftovers[replace]
                                    replace+=1
                            leftovers.clear()
                            replace=0
                        sleep(700)
                        if speed>=90:
                            speed-=random.randint(15,20)
                        state='game'
        if state=='game':
            if mode!=1:
                tone=random.randint(0,3)
                sequence.append(tone)
            if mode==1:
                sequence.append(random.randint(0,3))
                for i in range(len(sequence)):
                    if len(sequence)>0:
                        sequence[i]=random.randint(0,3)
            if mode==3 and len(sequence)>=3:
                leftovers.clear()
                max_fakes=len(sequence)//3
                num_fakes=random.randint(0,max_fakes)
                eligible=[i for i in range(1,len(sequence)-1) if sequence[i]!=4]
                if num_fakes>len(eligible):
                    num_fakes=len(eligible)
                fake_positions=[]
                eligible_copy=eligible[:]
                for i in range(num_fakes):
                    idx=random.choice(eligible_copy)
                    eligible_copy.remove(idx)
                    fake_positions.append(idx)
                fake_positions.sort()
                for idx in fake_positions:
                    leftovers.append(sequence[idx])
                    sequence[idx]=4
            for i in range(len(sequence)):
                display.show(colors[sequence[i]])
                music.pitch(int(tones[sequence[i]]),duration=int(speed*0.9),wait=True,pin=music_pin)
                display.clear()
                sleep(speed*0.1)
            if mode==2:
                sequence.reverse()
            current=0
            while current<len(sequence) and sequence[current]==4:
                current+=1
            state='waiting'
        if state=='fail':
            if controller==True:
                pin1.write_analog(700)
            music.pitch(55,duration=1200, wait=True,pin=music_pin)
            if controller==True:
                pin1.write_analog(0)
            if len(sequence)<8:
                speech.pronounce(random.choice(comments),pin=music_pin)
            elif len(sequence)>=8:
                speech.pronounce(random.choice(verygood_comments),pin=music_pin)
            sequence=[]
            speed=600
            display.clear()
            state='waiting'
speed=130
sequence=[0,1,2,3]
for i in range(len(sequence)):
    display.show(colors[sequence[i]])
    music.pitch(int(tones[sequence[i]]),duration=int(speed*0.9),wait=True,pin=music_pin)
    display.clear()
    sleep(speed*0.1)
sequence=[]
speed=600
main()