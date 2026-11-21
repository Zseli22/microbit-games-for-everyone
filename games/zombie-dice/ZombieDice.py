from microbit import *
import random
import speech
import os

controller=False
if pin15.read_digital()==1:
    controller=True

if controller==False:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    music_pin=None
else:
    music_pin=pin2

add_human=False
add_computer=False
start_game=False
roll_action=False
bank_action=False
turn_stats=False
score_stats=False
previous_add_human=False
previous_add_computer=False
previous_start_game=False
previous_action_a=False
previous_action_b=False
previous_turn_stats=False
previous_score_stats=False

def update():
    global add_human,add_computer,start_game,roll_action,bank_action,turn_stats,score_stats
    global previous_add_human,previous_add_computer,previous_start_game,previous_action_a,previous_action_b
    global previous_turn_stats,previous_score_stats
    if controller==False:
        add_human=button_a.is_pressed()
        add_computer=button_b.is_pressed()
        start_game=accelerometer.is_gesture('shake')
        roll_action=button_a.is_pressed()
        bank_action=button_b.is_pressed()
        turn_stats=pin_logo.is_touched()
        score_stats=pin1.is_touched() or pin2.is_touched()
    else:
        add_human=pin12.read_digital()==0
        add_computer=pin13.read_digital()==0
        start_game=pin15.read_digital()==0
        roll_action=pin15.read_digital()==0
        bank_action=pin16.read_digital()==0
        turn_stats=pin8.read_digital()==0
        score_stats=pin14.read_digital()==0

    add_human_pressed=add_human and not previous_add_human
    add_computer_pressed=add_computer and not previous_add_computer
    start_game_pressed=start_game and not previous_start_game
    roll_action_pressed=roll_action and not previous_action_a
    bank_action_pressed=bank_action and not previous_action_b
    turn_stats_pressed=turn_stats and not previous_turn_stats
    score_stats_pressed=score_stats and not previous_score_stats
    previous_add_human=add_human
    previous_add_computer=add_computer
    previous_start_game=start_game
    previous_action_a=roll_action
    previous_action_b=bank_action
    previous_turn_stats=turn_stats
    previous_score_stats=score_stats
    return (add_human_pressed,add_computer_pressed,start_game_pressed,
            roll_action_pressed,bank_action_pressed,turn_stats_pressed,
            score_stats_pressed)

def play_sound(effect,wait=True):
    audio.play(effect,wait=wait,pin=music_pin)
def announce_title():
    speech.pronounce('ZAA4MBIY7 DAY8S.',pin=music_pin)
    sleep(1000)
full_cup=['green','green','green','green','green','green','yellow','yellow','yellow','yellow','red','red','red']
hand=[]
green_faces=['brain','brain','brain','runner','runner','shotgun']
yellow_faces=['brain','brain','runner','runner','shotgun','shotgun']
red_faces=['brain','runner','runner','shotgun','shotgun','shotgun']
players=[]
player=0
brains=0
shotguns=0
cup=full_cup[:]
final_round=False
bank_tones=[1175,1568,1760,1976,2349]
limit=13
last_tones=[392,523,659,784,0,659]
win_tones=[1046,831,659,523,466,415,1175,932,699,587,523,466,1245,1046,831,622,523,415,1397,1175,932,698,587,466,263,294,330,392,523,587,659,784,1047,1175,1319,1568]
load_tones=[1046,1175,1568]
def clear_save():
    if 'save.txt' in os.listdir():
        os.remove('save.txt')
def reset_turn():
    global brains,shotguns,cup
    hand.clear()
    brains=0
    shotguns=0
    cup=full_cup[:]
def reset_game():
    global player,final_round
    reset_turn()
    players.clear()
    player=0
    final_round=False
def save_game():
    clear_save()
    with open('save.txt','w') as save:
        save.write(str(players)+'\n')
        save.write(str((player,final_round))+'\n')
        save.close()
def top_score():
    best=players[0]['score']
    for i in range(1,len(players)):
        if players[i]['score']>best:
            best=players[i]['score']
    return best
def restart_game():
    clear_save()
    reset_game()
    start()
    return 'restart'
def start():
    global player
    announce_title()
    speech.pronounce('sih7leh4kt - pley3er8rz.',pin=music_pin)
    while True:
        add_human_pressed,add_computer_pressed,start_game_pressed,_,_,_,_=update()
        if add_human_pressed and len(players)<=9:
            display.scroll('H',delay=50)
            play_sound(audio.SoundEffect(freq_start=1568,freq_end=1568,duration=75))
            play_sound(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=75))
            players.append({'type':0,'score':0,'final_done':False})
        elif add_computer_pressed and len(players)<=9:
            display.scroll('C',delay=50)
            play_sound(audio.SoundEffect(freq_start=784, freq_end=784, duration=75))
            play_sound(audio.SoundEffect(freq_start=1046,freq_end=1046,duration=75))
            players.append({'type':1,'score':0,'final_done':False})
        elif ((start_game_pressed and controller) or
              ((accelerometer.is_gesture('shake') or len(players)==10) and not controller)) and len(players)>1:
            wheel=5
            cloc=0
            while wheel<=555:
                    if cloc==11:
                        cloc=0
                    display.show(Image.ALL_CLOCKS[cloc])
                    cloc+=1
                    play_sound(audio.SoundEffect(freq_start=1046,freq_end=1046,duration=20))
                    sleep(wheel)
                    wheel+=random.randint(round(wheel*0.08),round(wheel*0.13))
            display.show(Image.SMILE)
            play_sound(audio.SoundEffect(freq_start=1000,freq_end=1000,duration=800,waveform=audio.SoundEffect.WAVEFORM_NOISE))
            player=random.randint(0,len(players)-1)
            display.scroll(player+1)
            display.clear()
            speech.say('Player '+str(player+1)+', you go first.',pin=music_pin)
            return
def load_save():
    global players,player,final_round
    asked=False
    announce_title()
    speech.pronounce('wuh6d yuw6 lay5k tuw8 rih7zuw5m yer7 sey5vd gey7m?',pin=music_pin)
    while True:
        _,_,_,action_a_pressed,action_b_pressed,_,down_pressed=update()
        if action_a_pressed:
            with open('save.txt','r') as save:
                players=eval(save.readline())
                player,final_round=eval(save.readline())
                save.close()
            reset_turn()
            display.show(Image.SMILE)
            for i in range(len(load_tones)):
                play_sound(audio.SoundEffect(freq_start=load_tones[i],freq_end=load_tones[i],duration=75))
            play_sound(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=400))
            check_score()
            display.scroll(player+1)
            speech.say('Player '+str(player+1)+', your turn.',pin=music_pin)
            return
        if action_b_pressed:
            display.show(Image.SCISSORS)
            asked=True
            speech.say('Press down to confirm deletion.',pin=music_pin)
        if (accelerometer.is_gesture('face down') or (controller and down_pressed)) and asked==True:
            clear_save()
            display.show(Image.SKULL)
            play_sound(audio.SoundEffect(freq_start=263,freq_end=263,duration=90))
            play_sound(audio.SoundEffect(freq_start=131,freq_end=131,duration=90))
            play_sound(audio.SoundEffect(freq_start=65,freq_end=65,duration=90))
            sleep(500)
            display.clear()
            return
def roll_dice():
    global brains,shotguns
    while len(hand)!=3:
        blip=random.randint(200,800)
        display.clear()
        play_sound(audio.SoundEffect(freq_start=blip,freq_end=blip*4,vol_start=0,vol_end=255,duration=120,shape=audio.SoundEffect.SHAPE_LINEAR,waveform=audio.SoundEffect.WAVEFORM_NOISE))
        sleep(200)
        if len(cup)==0:
            cup.extend(full_cup)
        choice=random.choice(cup)
        hand.append(choice)
        cup.remove(choice)
        if choice=='green':
            display.scroll('G',delay=50)
            play_sound(audio.SoundEffect(freq_start=1047,freq_end=1047,waveform=audio.SoundEffect.WAVEFORM_TRIANGLE,duration=150))
        elif choice=='yellow':
            display.scroll('Y',delay=50)
            play_sound(audio.SoundEffect(freq_start=523,freq_end=523,waveform=audio.SoundEffect.WAVEFORM_SQUARE,duration=150))
        elif choice=='red':
            display.scroll('R',delay=50)
            play_sound(audio.SoundEffect(freq_start=131,freq_end=131,waveform=audio.SoundEffect.WAVEFORM_SAWTOOTH,duration=150))
        sleep(150)
    sleep(600)
    display.clear()
    values=[]
    for i in range(3):
        dice_tone=audio.SoundEffect()
        if hand[i]=='green':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_TRIANGLE
            values.append(random.choice(green_faces))
        elif hand[i]=='yellow':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_SQUARE
            values.append(random.choice(yellow_faces))
        elif hand[i]=='red':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_SAWTOOTH
            values.append(random.choice(red_faces))
        blip=random.randint(400,1600)
        echo_vol=255
        while echo_vol > 60:
            echo_lowering=random.randint(30,60)
            echo_vol -= echo_lowering
            dice_tone.freq_start=blip
            dice_tone.freq_end=blip
            dice_tone.shape=audio.SoundEffect.SHAPE_LINEAR
            dice_tone.duration=random.randint(25,90)
            dice_tone.vol_start=echo_vol
            play_sound(dice_tone)
        sleep(300)
    sleep(600)
    new_hand=[]
    for i in range(len(values)):
        dice_tone=audio.SoundEffect()
        dice_tone.shape=audio.SoundEffect.SHAPE_LINEAR
        if hand[i]=='green':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_TRIANGLE
        elif hand[i]=='yellow':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_SQUARE
        elif hand[i]=='red':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_SAWTOOTH
        if values[i]=='brain':
            display.show(Image.PACMAN)
            dice_tone.freq_start=1047
            dice_tone.freq_end=2093
            dice_tone.duration=300
            play_sound(dice_tone)
            brains+=1
        elif values[i]=='runner':
            display.show(Image.STICKFIGURE)
            dice_tone.duration=15
            dice_tone.vol_end=255
            for _ in range(2):
                dice_tone.freq_start=523
                dice_tone.freq_end=523
                play_sound(dice_tone)
                sleep(50)
                dice_tone.freq_start=748
                dice_tone.freq_end=748
                play_sound(dice_tone)
                sleep(50)
            new_hand.append(hand[i])
        elif values[i]=='shotgun':
            display.show(Image.SKULL)
            dice_tone.freq_start=263
            dice_tone.freq_end=132
            dice_tone.duration=300
            play_sound(dice_tone)
            shotguns+=1
        display.clear()
        sleep(600)
    hand[:]=new_hand
def bank():
    players[player]['score']+=brains
    display.scroll(players[player]['score'],delay=50)
    for i in range(players[player]['score']):
        play_sound(audio.SoundEffect(freq_start=1976,freq_end=1976,duration=75))
        play_sound(audio.SoundEffect(freq_start=2637,freq_end=2637,duration=300),wait=False)
        sleep(110)
    sleep(200)
    display.show(Image.HAPPY)
    for i in range(len(bank_tones)):
        play_sound(audio.SoundEffect(freq_start=bank_tones[i],freq_end=bank_tones[i],duration=40))
    play_sound(audio.SoundEffect(freq_start=3136,freq_end=3136,duration=600))
    display.clear()
    return next()
def next():
    global player,final_round
    other_best=0
    for i in range(len(players)):
        if i!=player and players[i]['score']>other_best:
            other_best=players[i]['score']
    if not final_round and players[player]['score'] >= limit:
        for i in range(len(last_tones)):
            play_sound(audio.SoundEffect(freq_start=last_tones[i], freq_end=last_tones[i], duration=140))
        play_sound(audio.SoundEffect(freq_start=784, freq_end=784, duration=800))
        speech.pronounce('fay4nax7l raw3nd. eh3vriy6wah7n /hae6z wah4n moh5r ter4n tax8 biy6t dhih7s skoh8r. ih6f now6 wah5n kae4n, yuw4 wih3n.',pin=music_pin)
        final_round=True
        players[player]['final_done']=True
    elif final_round:
        players[player]['final_done']=True
        if players[player]['score'] > other_best and any(not p['final_done'] for p in players):
            for i in range(len(last_tones)):
                play_sound(audio.SoundEffect(freq_start=last_tones[i], freq_end=last_tones[i], duration=140))
            play_sound(audio.SoundEffect(freq_start=784, freq_end=784, duration=800))
            speech.pronounce('dhax7 reh4ker6d /hae7z bih7n biy3tax8n. dhax7 rih7mey4nih7nx pley5er8rz /hae7v ax8 chae6ns tax8 biy5t dhih7s nuw3 skoh4r - ae7nd kley4m vih3ktax6riy8.',pin=music_pin)
    if final_round:
        done=True
        for i in range(len(players)):
            if players[i]['final_done']==False:
                done=False
                break
        if done:
            winner=max(range(len(players)), key=lambda i: players[i]['score'])
            display.scroll('Winner! player',delay=100)
            display.scroll(winner+1)
            speech.say('The winner is, player '+str(winner+1)+'.',pin=music_pin)
            for i in range(len(win_tones)):
                play_sound(audio.SoundEffect(freq_start=win_tones[i], freq_end=win_tones[i], duration=40))
            play_sound(audio.SoundEffect(freq_start=2093, freq_end=2093, duration=1000))
            return restart_game()
    player = (player + 1) % len(players)
    display.scroll(player+1)
    speech.say('Player '+str(player+1)+'.',pin=music_pin)
    reset_turn()
    save_game()
    return 'continue'
def check_stats():
    dice_tone=audio.SoundEffect()
    display.show(Image.PACMAN)
    for i in range(brains):
        play_sound(audio.SoundEffect(freq_start=1047,freq_end=1047,waveform=audio.SoundEffect.WAVEFORM_TRIANGLE,duration=150))
    display.scroll(brains,delay=100)
    display.show(Image.SKULL)
    for i in range(shotguns):
        play_sound(audio.SoundEffect(freq_start=131,freq_end=131,waveform=audio.SoundEffect.WAVEFORM_SAWTOOTH,duration=150))
    display.scroll(shotguns,delay=100)
    display.show(Image.STICKFIGURE)
    sleep(500)
    for i in range(len(hand)):
        if hand[i]=='green':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_TRIANGLE
        elif hand[i]=='yellow':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_SQUARE
        elif hand[i]=='red':
            dice_tone.waveform=audio.SoundEffect.WAVEFORM_SAWTOOTH
        dice_tone.duration=15
        dice_tone.vol_end=255
        for _ in range(2):
            dice_tone.freq_start=523
            dice_tone.freq_end=523
            play_sound(dice_tone)
            sleep(50)
            dice_tone.freq_start=748
            dice_tone.freq_end=748
            play_sound(dice_tone)
            sleep(50)
        sleep(400)
    display.scroll(len(hand))
def check_score():
    for i in range(len(players)):
        display.scroll(players[i]['score'],delay=50)
        for j in range(players[i]['score']):
            play_sound(audio.SoundEffect(freq_start=1976,freq_end=1976,duration=75))
            play_sound(audio.SoundEffect(freq_start=2637,freq_end=2637,duration=300),wait=False)
            sleep(110)
        sleep(200)
def main():
    while True:
        if players[player]['type']==0:
            display.show(Image.HEART)
            _,_,_,roll_pressed,bank_pressed,turn_stats_pressed,score_stats_pressed=update()
            if roll_pressed:
                roll_dice()
            if shotguns>=3:
                display.show(Image.SAD)
                play_sound(audio.SoundEffect(freq_start=196,freq_end=196,duration=600,vol_end=255))
                play_sound(audio.SoundEffect(freq_start=139,freq_end=139,duration=600,vol_end=255))
                state=next()
                if state=='restart':
                    return
            elif bank_pressed and brains>0:
                state=bank()
                if state=='restart':
                    return
            elif turn_stats_pressed:
                check_stats()
            elif score_stats_pressed:
                check_score()
                sleep(600)
        elif players[player]['type']==1:
            display.show(Image.ASLEEP)
            sleep(random.randint(1000,3000))
            display.clear()
            if final_round:
                if players[player]['score']+brains>top_score():
                    state=bank()
                    if state=='restart':
                        return
                else:
                    roll_dice()
            else:
                if shotguns==2 and brains>1:
                    state=bank()
                    if state=='restart':
                        return
                elif shotguns<=1 or brains<=1:
                    roll_dice()
            if shotguns>=3:
                display.show(Image.ANGRY)
                play_sound(audio.SoundEffect(freq_start=196,freq_end=196,duration=600,vol_end=255))
                play_sound(audio.SoundEffect(freq_start=139,freq_end=139,duration=600,vol_end=255))
                state=next()
                if state=='restart':
                    return
if 'save.txt' in os.listdir():
    load_save()
    if len(players)==0:
        start()
else:
    start()
while True:
    main()
