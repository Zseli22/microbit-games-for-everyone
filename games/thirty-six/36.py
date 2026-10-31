from microbit import *
import random
import speech
import os
controller=pin15.read_digital()==1
if controller:
    music_pin=pin2
else:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    music_pin=None

def input_state():
    if controller:
        return (pin15.read_digital()==0,pin16.read_digital()==0,
                pin8.read_digital()==0,pin14.read_digital()==0,
                pin12.read_digital()==0,pin13.read_digital()==0,False,False)
    return (button_a.is_pressed(),button_b.is_pressed(),pin_logo.is_touched(),
            pin1.is_touched() or pin2.is_touched(),False,False,
            accelerometer.is_gesture('shake'),accelerometer.is_gesture('face down'))

def p(text):
    speech.pronounce(text,pin=music_pin)

def s(text):
    speech.say(text,pin=music_pin)

def release_a():
    while controller and pin15.read_digital()==0:
        sleep(20)
hand=[]
aside=[]
players=[]
player=0
orig_player=0
total=0
subtract=0
win_tones=[1046,831,659,523,466,415,1175,932,699,587,523,466,1245,1046,831,622,523,415,1397,1175,932,698,587,466,263,294,330,392,523,587,659,784,1047,1175,1319,1568]
d1=Image('00000:00000:00900:00000:00000')
d2=Image('90000:00000:00000:00000:00009')
d3=Image('90000:00000:00900:00000:00009')
d4=Image('90009:00000:00000:00000:90009')
d5=Image('90009:00000:00900:00000:90009')
d6=Image('90009:00000:90009:00000:90009')
faces=[d1, d2, d3, d4, d5, d6]
dice_tones=[523, 587, 659, 699, 784, 880, 988, 1047, 1175, 1319, 1397, 1568, 1760, 1976, 2093]
score_tones=[dice_tones[4],dice_tones[9],dice_tones[5],dice_tones[6],dice_tones[8],dice_tones[11]]
bonus_tones=[262,330,392,523,392,523,659,784,1047,784,415,523,622,831,622,831,1047,1245,1661,1245,466,587,698,932,698,932,1175,1397,1865,1397]
load_tones=[1046,1175,1568]
def t(p,d):
    audio.play(audio.SoundEffect(freq_start=p,freq_end=p,duration=d),pin=music_pin)
def clear_save():
    if 'save.txt' in os.listdir():
        os.remove('save.txt')
def reset_game():
    global player,orig_player,total,subtract
    hand.clear()
    aside.clear()
    players.clear()
    player=0
    orig_player=0
    total=0
    subtract=0
def save_game():
    clear_save()
    with open('save.txt','w') as save:
        save.write(str(players)+'\n')
        save.write(str(player)+'\n')
def restart_game():
    clear_save()
    reset_game()
    start()
    return 'restart'
def active_hand(mode):
    dice=[]
    for die in hand:
        if mode=='keep' and die['kept']==False:
            dice.append(die)
        elif mode=='undo' and die['kept']==True:
            dice.append(die)
    return dice
def sort_hand():
    hand.sort(key=lambda die: (die['kept'], -die['value']))
def hand_total():
    value=0
    for die in hand:
        if die['kept']:
            value+=die['value']
    return value
def aside_total():
    value=0
    for die in aside:
        value+=die
    return value
def clear_roll():
    hand.clear()
def start():
    global player
    p('THER4TIY6 SIH4KS.')
    sleep(1000)
    p('sih7leh4kt - pley3er8rz.')
    while True:
        a,b,u,d,l,r,shake,face=input_state()
        if (l or (not controller and a)) and len(players)<=9:
            display.scroll('H',delay=50)
            t(1568,75)
            t(2093,75)
            players.append({'type':0,'score':36})
        elif (r or (not controller and b)) and len(players)<=9:
            display.scroll('C',delay=50)
            t(784,75)
            t(1046,75)
            players.append({'type':1,'score':36})
        elif ((controller and a) or (not controller and (shake or len(players)==9))) and len(players)>0:
            if len(players)==1:
                p('staa5rtih7nx wah4n pley6er gey8m.')
            else:
                wheel=5
                cloc=0
                while wheel<=555:
                    if cloc==11:
                        cloc=0
                    display.show(Image.ALL_CLOCKS[cloc])
                    cloc+=1
                    t(1046,20)
                    sleep(wheel)
                    wheel+=random.randint(round(wheel*0.08),round(wheel*0.13))
                display.show(Image.SMILE)
                audio.play(audio.SoundEffect(freq_start=1000,freq_end=1000,duration=800,waveform=audio.SoundEffect.WAVEFORM_NOISE),pin=music_pin)
                player=random.randint(0,len(players)-1)
                display.scroll(player+1)
                display.clear()
                s('Player '+str(player+1)+', you go first.')
            release_a()
            if not controller and shake:
                sleep(500)
            return
def load_save():
    global players,player,total,orig_player,subtract
    asked=False
    p('THER4TIY6 SIH4KS.')
    sleep(1000)
    p('wuh6d yuw6 lay5k tuw8 rih7zuw5m yer7 sey5vd gey7m?')
    while True:
        a,b,u,d,l,r,shake,face=input_state()
        if a:
            with open('save.txt','r') as save:
                players=eval(save.readline())
                player=int(save.readline())
            total=0
            orig_player=player
            subtract=0
            clear_roll()
            aside.clear()
            display.show(Image.SMILE)
            for i in range(len(load_tones)):
                t(load_tones[i],75)
            t(2093,400)
            check_score()
            if len(players)>1:
                display.scroll(player+1)
                s('Player '+str(player+1)+', your turn.')
            else:
                p('Gow3 foh6r ih8t.')
            release_a()
            return
        if b:
            display.show(Image.SCISSORS)
            asked=True
            s('Press down to confirm deletion.')
        if (face or (controller and d)) and asked==True:
            clear_save()
            display.show(Image.SKULL)
            t(263,90)
            t(131,90)
            t(65,90)
            sleep(500)
            display.clear()
            return
def roll_dice():
    echo_vol = 255
    speed=random.randint(20,70)
    for i in range(0, random.randint(10,30)):
        blip = random.randint(400,1600)
        display.show(random.choice(faces))
        t(blip,speed)
    while echo_vol > 30:
        echo_lowering = random.randint(10,30)
        echo_vol -= echo_lowering
        audio.play(audio.SoundEffect(freq_start=blip, freq_end=blip, duration=speed, vol_start=echo_vol),pin=music_pin)
    display.clear()
    sleep(800)
    clear_roll()
    for i in range(abs(len(aside)-6)):
        hand.append({'value':random.randint(1,6),'kept':False})
    sort_hand()
    for i in range(len(hand)):
        display.show(faces[hand[i]['value']-1])
        t(dice_tones[hand[i]['value']-1],120)
        sleep(200)
    display.clear()
    sleep(500)
def show_die(die):
    display.show(faces[die['value']-1])
    t(dice_tones[die['value']-1],120)
def keep_die(die):
    die['kept']=True
    display.clear()
    for i in range(2):
        t(dice_tones[die['value']-1]*4,75)
    sleep(400)
def unkeep_die(die):
    die['kept']=False
    sort_hand()
    display.clear()
    for i in range(2):
        t(dice_tones[die['value']-1]*2,75)
    sleep(400)
def commit_kept():
    global total
    total=0
    next_roll=[]
    for die in hand:
        if die['kept']:
            aside.append(die['value'])
        else:
            next_roll.append(die)
    hand[:] = next_roll
    total=aside_total()
def reroll():
    global total,subtract,player,orig_player
    selection=-1
    mode='keep'
    while True:
        current=active_hand(mode)
        a,b,u,d,l,r,shake,face=input_state()
        if (controller and (l or r)) or (not controller and a):
            if len(current)>0:
                if controller and l:
                    if selection<=0:
                        selection=len(current)-1
                    else:
                        selection-=1
                elif selection==len(current)-1:
                    selection=0
                else:
                    selection+=1
                show_die(current[selection])
            sleep(150)
        if b and selection>=0 and len(current)>0:
            die=current[selection]
            if mode=='keep':
                keep_die(die)
            else:
                unkeep_die(die)
            current=active_hand(mode)
            if len(current)==0:
                selection=-1
                if mode=='undo':
                    mode='keep'
                    t(392,75)
                    sleep(200)
            else:
                if selection>=len(current):
                    selection=0
                show_die(current[selection])
        if u:
            total=aside_total()+hand_total()
            display.scroll(total)
            count(total)
        if d and len(active_hand('undo'))>0:
            if mode=='keep':
                mode='undo'
                t(1568,75)
            else:
                mode='keep'
                t(392,75)
            sleep(200)
            selection=-1
        if ((controller and a) or (not controller and shake)) and len(active_hand('undo'))>0:
            commit_kept()
            if len(hand)==0:
                for i in range(len(score_tones)):
                    t(score_tones[i],60)
                display.scroll(total,delay=50)
                count(total)
                aside.clear()
                sleep(500)
                if total<30:
                    orig_player=player
                    state=scoring()
                    if state=='restart':
                        return state
                    while subtract>0:
                        state=next()
                        if state=='restart':
                            return state
                        state=scoring()
                        if state=='restart':
                            return state
                    player=orig_player
                if total>30:
                    state=bonus()
                    if state=='restart':
                        return state
                state=next()
                if state=='restart':
                    return state
            clear_roll()
            return
def count(value):
    if value==0:
        t(131,250)
    while value>0:
        if value>=10:
            t(784,220)
            value-=10
        else:
            t(523,90)
            value-=1
        sleep(160)
def scoring():
    global total,subtract
    old_score=players[player]['score']
    if total>30:
        subtract=aside[0]*len(aside)
    else:
        subtract=abs(30-total)
    while subtract>0 and players[player]['score']>0:
        if len(players)==1 and total>30:
            players[player]['score']+=1
        else:
            players[player]['score']-=1
        subtract-=1
        if players[player]['score']==0:
            display.show(Image.SAD)
            audio.play(audio.SoundEffect(freq_start=2000,freq_end=1000,vol_end=32,duration=1000,shape=audio.SoundEffect.SHAPE_LINEAR),pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=110,freq_end=110,vol_end=255,duration=500),pin=music_pin)
            display.clear()
            p('yow6r aw3t.')
            sleep(800)
            state=next()
            if state=='restart':
                return state
            old_score=players[player]['score']
    audio.play(audio.SoundEffect(freq_start=scale(old_score,from_=(0,36),to=(50,1000)),freq_end=scale(players[player]['score'],from_=(0,36),to=(50,1000)),duration=2000,shape=audio.SoundEffect.SHAPE_LINEAR,vol_end=255),pin=music_pin)
    display.scroll(players[player]['score'],delay=50)
    count(players[player]['score'])
    return 'continue'
def next():
    global player
    if (len(players)==1 and players[player]['score']>=54):
        display.scroll('You win')
        p('yuw6 /hae6v riy5cht dhax8 taa4rgih7t skoh4er. Yuw4 wih3n.')
        for i in range(len(win_tones)):
            t(win_tones[i],40)
        t(2093,1000)
        return restart_game()
    if len(players)>1:
        remaining=0
        winner=-1
        for i in range(len(players)):
            if players[i]['score']>0:
                remaining+=1
                winner=i
        if remaining==1:
            display.scroll('Winner! player'+str(winner+1),delay=50)
            s('The winner is, player '+str(winner+1)+'.')
            for i in range(len(win_tones)):
                t(win_tones[i],40)
            t(2093,1000)
            return restart_game()
    if len(players)==1:
        if players[player]['score']==0:
            display.scroll('You lose',delay=50)
            p('Yuw5 lao7st. Beh5ter7 lah6k neh4kst tay8m.')
            return restart_game()
        p('neh4kst raw7nd.')
    else:
        player = (player + 1) % len(players)
        while players[player]['score']==0:
            player = (player + 1) % len(players)
        display.scroll(player+1)
        s('Player '+str(player+1)+'.')
    save_game()
    return 'continue'
def computer():
    global total,player,orig_player,subtract
    while len(aside)<6:
        sort_hand()
        for die in hand:
            if die['kept']==False and (die['value']==6 or die['value']==5):
                die['kept']=True
        current=active_hand('keep')
        if len(current)>0:
            if (len(active_hand('undo'))==0 and current[0]['value']<5) or ((len(active_hand('undo'))+len(aside)>3) and current[0]['value']==4):
                current[0]['kept']=True
        kept=active_hand('undo')
        for die in kept:
            aside.append(die['value'])
            sleep(400)
            display.show(faces[die['value']-1])
            for i in range(2):
                t(dice_tones[die['value']-1]*4,75)
            display.clear()
        clear_roll()
        sleep(800)
        if len(aside)<6:
            roll_dice()
    if len(aside)==6:
        total=aside_total()
        for i in range(len(score_tones)):
            t(score_tones[i],60)
        display.scroll(total,delay=50)
        count(total)
        aside.clear()
        sleep(500)
        if total<30:
            orig_player=player
            state=scoring()
            if state=='restart':
                return state
            while subtract>0:
                state=next()
                if state=='restart':
                    return state
                state=scoring()
                if state=='restart':
                    return state
            player=orig_player
        if total>30:
            state=bonus()
            if state=='restart':
                return state
        state=next()
        if state=='restart':
            return state
    clear_roll()
    return 'continue'
def check_score():
    for i in range(len(players)):
        display.scroll(players[i]['score'],delay=50)
        count(players[i]['score'])
        sleep(400)
def bonus():
    global player,subtract,orig_player
    display.show(Image.FABULOUS)
    for i in range(len(bonus_tones)):
        t(bonus_tones[i],25)
    display.clear()
    sleep(1200)
    roll_dice()
    target=total-30
    while True:
        matches=0
        for die in hand:
            if die['value']==target:
                die['kept']=True
                matches+=1
        if matches==0:
            break
        for die in active_hand('undo'):
            aside.append(die['value'])
            for i in range(2):
                t(dice_tones[die['value']-1]*4,75)
            sleep(400)
        clear_roll()
        sleep(800)
        if len(aside)<6:
            roll_dice()
    orig_player=player
    if len(aside)>0:
        if len(players)>1:
            state=next()
            if state=='restart':
                return state
        state=scoring()
        if state=='restart':
            return state
        while subtract>0:
            state=next()
            if state=='restart':
                return state
            state=scoring()
            if state=='restart':
                return state
    aside.clear()
    player=orig_player
    return 'continue'
def main():
    while True:
        if players[player]['type']==0:
            a,b,u,d,l,r,shake,face=input_state()
            if a or (not controller and shake):
                roll_dice()
                release_a()
                if len(aside)==5:
                    state=computer()
                else:
                    state=reroll()
                if state=='restart':
                    return state
            elif b:
                check_score()
        elif players[player]['type']==1:
            display.show(Image.ASLEEP)
            sleep(random.randint(800,2000))
            display.clear()
            roll_dice()
            state=computer()
            if state=='restart':
                return state
if 'save.txt' in os.listdir():
    load_save()
    if len(players)==0:
        start()
else:
    start()
while True:
    main()
