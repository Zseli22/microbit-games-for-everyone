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
increase_limit=False
decrease_limit=False
show_limit=False
show_total=False
show_scores=False
previous_add_human=False
previous_add_computer=False
previous_start_game=False
previous_action_a=False
previous_action_b=False
previous_increase_limit=False
previous_decrease_limit=False
previous_show_limit=False
previous_show_total=False
previous_show_scores=False

def update():
    global add_human,add_computer,start_game,roll_action,bank_action
    global increase_limit,decrease_limit,show_limit,show_total,show_scores
    global previous_add_human,previous_add_computer,previous_start_game
    global previous_action_a,previous_action_b,previous_increase_limit,previous_decrease_limit
    global previous_show_limit,previous_show_total,previous_show_scores
    if controller==False:
        add_human=button_a.is_pressed()
        add_computer=button_b.is_pressed()
        start_game=accelerometer.is_gesture('shake')
        roll_action=button_a.is_pressed()
        bank_action=button_b.is_pressed()
        increase_limit=pin_logo.is_touched()
        decrease_limit=pin1.is_touched() or pin2.is_touched()
        show_limit=accelerometer.is_gesture('face down')
        show_total=pin_logo.is_touched()
        show_scores=pin1.is_touched() or pin2.is_touched()
    else:
        add_human=pin12.read_digital()==0
        add_computer=pin13.read_digital()==0
        start_game=pin15.read_digital()==0
        roll_action=pin15.read_digital()==0
        bank_action=pin16.read_digital()==0
        increase_limit=pin8.read_digital()==0
        decrease_limit=pin14.read_digital()==0
        show_limit=pin16.read_digital()==0
        show_total=pin8.read_digital()==0
        show_scores=pin14.read_digital()==0

    add_human_pressed=add_human and not previous_add_human
    add_computer_pressed=add_computer and not previous_add_computer
    start_game_pressed=start_game and not previous_start_game
    roll_action_pressed=roll_action and not previous_action_a
    bank_action_pressed=bank_action and not previous_action_b
    increase_limit_pressed=increase_limit and not previous_increase_limit
    decrease_limit_pressed=decrease_limit and not previous_decrease_limit
    show_limit_pressed=show_limit and not previous_show_limit
    show_total_pressed=show_total and not previous_show_total
    show_scores_pressed=show_scores and not previous_show_scores
    previous_add_human=add_human
    previous_add_computer=add_computer
    previous_start_game=start_game
    previous_action_a=roll_action
    previous_action_b=bank_action
    previous_increase_limit=increase_limit
    previous_decrease_limit=decrease_limit
    previous_show_limit=show_limit
    previous_show_total=show_total
    previous_show_scores=show_scores
    return (add_human_pressed,add_computer_pressed,start_game_pressed,
            roll_action_pressed,bank_action_pressed,increase_limit_pressed,
            decrease_limit_pressed,show_limit_pressed,show_total_pressed,
            show_scores_pressed)

def play_sound(effect,wait=True):
    audio.play(effect,wait=wait,pin=music_pin)

def announce_title():
    speech.pronounce('TAA4SAH8P.',pin=music_pin)
    sleep(1000)
green=Image('99999:00000:00000:00000:00000')
yellow=Image('00000:00000:99999:00000:00000')
red=Image('00000:00000:00000:00000:99999')
images=[green,yellow,red]
faces=[0,0,0,1,1,2]
hand=[]
players=[]
player=0
total=0
final_round=False
complete_tones=[1319,1568,2637,2093,2349,3136]
last_tones=[392,523,659,784,0,659]
win_tones=[1046,831,659,523,466,415,1175,932,699,587,523,466,1245,1046,831,622,523,415,1397,1175,932,698,587,466,263,294,330,392,523,587,659,784,1047,1175,1319,1568]
load_tones=[1046,1175,1568]
limit=100
def clear_save():
    if 'save.txt' in os.listdir():
        os.remove('save.txt')
def reset_game():
    global player,total,final_round
    hand.clear()
    players.clear()
    player=0
    total=0
    final_round=False
def save_game():
    global players,limit,player,final_round
    clear_save()
    with open('save.txt','w') as save:
        save.write(str(players)+'\n')
        save.write(str((limit,player,final_round))+'\n')
        save.close()
def top_player():
    best=0
    for i in range(1,len(players)):
        if players[i]['score']>players[best]['score']:
            best=i
    return best
def start():
    global player,limit
    announce_title()
    speech.pronounce('sih7leh4kt - pley3er8rz.',pin=music_pin)
    while True:
        add_human_pressed,add_computer_pressed,start_game_pressed,_,_,increase_limit_pressed,decrease_limit_pressed,show_limit_pressed,_,_=update()
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
        elif increase_limit_pressed:
            limit+=10
            play_sound(audio.SoundEffect(freq_start=scale(limit,from_=(50,400),to=(300,1500)),freq_end=scale(limit,from_=(50,400),to=(300,1500)),duration=100))
            sleep(200)
        elif decrease_limit_pressed and limit>50:
            limit-=10
            play_sound(audio.SoundEffect(freq_start=scale(limit,from_=(50,400),to=(300,1500)),freq_end=scale(limit,from_=(50,400),to=(300,1500)),duration=100))
            sleep(200)
        if show_limit_pressed:
            display.scroll(limit,delay=50)
            speech.say('You are playing to,'+str(limit)+'.',pin=music_pin)
        elif ((start_game_pressed and controller) or
              ((accelerometer.is_gesture('shake') or len(players)==10) and not controller)) and len(players)>0:
            if len(players)==1:
                speech.pronounce('staa5rtih7nx wah4n pley6er gey8m.',pin=music_pin)
            else:
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
    global players,player,total,limit,final_round
    asked=False
    announce_title()
    speech.pronounce('wuh6d yuw6 lay5k tuw8 rih7zuw5m yer7 sey5vd gey7m?',pin=music_pin)
    while True:
        _,_,_,action_a_pressed,action_b_pressed,_,down_pressed,_,_,_=update()
        if action_a_pressed:
            with open('save.txt','r') as save:
                players=eval(save.readline())
                limit,player,final_round=eval(save.readline())
                save.close()
            total=0
            display.show(Image.SMILE)
            for i in range(len(load_tones)):
                play_sound(audio.SoundEffect(freq_start=load_tones[i],freq_end=load_tones[i],duration=75))
            play_sound(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=400))
            check_score()
            display.scroll(limit,delay=50)
            speech.say('You are playing to,'+str(limit)+'.',pin=music_pin)
            if len(players)==1:
                speech.pronounce('gow3 foh5r ih7t. ',pin=music_pin)
            else:
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
    global hand,faces,total,complete_tones,images
    echo_vol = 255
    speed=random.randint(20,70)
    for i in range(0, random.randint(10,30)):
        blip = random.randint(400,1600)
        display.show(random.choice(images))
        play_sound(audio.SoundEffect(freq_start=blip, freq_end=blip, duration=speed))
    while echo_vol > 30:
        echo_lowering = random.randint(10,30)
        echo_vol -= echo_lowering
        play_sound(audio.SoundEffect(freq_start=blip, freq_end=blip, duration=speed, vol_start=echo_vol))
    display.clear()
    sleep(800)
    hand.clear()
    for i in range(abs((total%10)-10)):
        hand.append(random.choice(faces))
    hand.sort()
    for i in range(len(hand)):
        if hand[i]==0:
            display.show(green)
            play_sound(audio.SoundEffect(freq_start=1047,freq_end=1047,duration=120))
        elif hand[i]==1:
            display.show(yellow)
            play_sound(audio.SoundEffect(freq_start=523,freq_end=523,duration=120))
        elif hand[i]==2:
            display.show(red)
            play_sound(audio.SoundEffect(freq_start=263,freq_end=263,duration=120))
        sleep(200)
    display.clear()
    sleep(500)
    if hand.count(0)==0 and hand.count(2)>=1:
        display.show(Image.SAD)
        play_sound(audio.SoundEffect(freq_start=196,freq_end=196,duration=600,vol_end=255))
        play_sound(audio.SoundEffect(freq_start=139,freq_end=139,duration=600,vol_end=255))
        next()
        return
    for i in range(hand.count(0)):
        total+=1
        hand.remove(0)
    if len(hand)==0:
        display.show(Image.SMILE)
        for i in range(len(complete_tones)):
            play_sound(audio.SoundEffect(freq_start=complete_tones[i],freq_end=complete_tones[i],duration=90))
def bank():
    global total,player,limit
    display.clear()
    for i in range(total):
        players[player]['score']+=1
        if i<25:
            display.set_pixel(i%5,(i//5),9)
        play_sound(audio.SoundEffect(freq_start=scale(players[player]['score'],from_=(0,limit),to=(300,1500)),freq_end=scale(players[player]['score'],from_=(0,limit),to=(300,1500)),duration=100))
    display.scroll(players[player]['score'],delay=50)
    count(players[player]['score'])
    next()
def count(value):
    if value==0:
        play_sound(audio.SoundEffect(freq_start=131,freq_end=131,duration=250))
    while value>=100:
        play_sound(audio.SoundEffect(freq_start=1175,freq_end=1175,duration=320))
        value-=100
        sleep(160)
    while value>=10 and value<100:
        play_sound(audio.SoundEffect(freq_start=784,freq_end=784,duration=220))
        value-=10
        sleep(160)
    while value>=1 and value<10:
        play_sound(audio.SoundEffect(freq_start=523,freq_end=523,duration=90))
        value-=1
        sleep(160)
def check_score():
    for i in range(len(players)):
        display.scroll(players[i]['score'],delay=50)
        count(players[i]['score'])
        sleep(400)
def win_game(winner):
    display.scroll('Winner! player',delay=100)
    display.scroll(winner+1)
    speech.say('The winner is, player '+str(winner+1)+'.',pin=music_pin)
    for i in range(len(win_tones)):
        play_sound(audio.SoundEffect(freq_start=win_tones[i], freq_end=win_tones[i], duration=40))
    play_sound(audio.SoundEffect(freq_start=2093, freq_end=2093, duration=1000))
    clear_save()
    reset_game()
    start()
def next():
    global limit,player,total,final_round
    other_best=0
    for i in range(len(players)):
        if i!=player and players[i]['score']>other_best:
            other_best=players[i]['score']
    if players[player]['score'] >= limit and len(players)==1:
        display.scroll('you win')
        speech.pronounce('yuw6 /hae6 riy4cht dhax8 taa4rgih6t skoh4r. Yuw4 wih3n.',pin=music_pin)
        for i in range(len(win_tones)):
            play_sound(audio.SoundEffect(freq_start=win_tones[i], freq_end=win_tones[i], duration=40))
        play_sound(audio.SoundEffect(freq_start=2093, freq_end=2093, duration=1000))
        clear_save()
        reset_game()
        start()
        return
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
            winner=top_player()
            win_game(winner)
            return
    if len(players)==1:
        speech.pronounce('neh4kst raw7nd.',pin=music_pin)
    else:
        player=(player+1)%len(players)
        display.scroll(player+1)
        speech.say('Player '+str(player+1)+'.',pin=music_pin)
    total=0
    save_game()
def main():
    global total
    while True:
        if players[player]['type']==0:
            display.show(str(total%10))
            _,_,_,roll_pressed,bank_pressed,_,_,_,show_total_pressed,show_scores_pressed=update()
            if roll_pressed:
                roll_dice()
            elif bank_pressed and total>0:
                bank()
                total=0
            elif show_total_pressed:
                display.scroll(total,delay=50)
                count(total)
            elif show_scores_pressed:
                check_score()
                sleep(600)
        elif players[player]['type']==1:
            display.show(Image.ASLEEP)
            sleep(random.randint(1000,3000))
            display.clear()
            leader=top_player()
            lead=players[leader]['score']
            score=players[player]['score']
            if final_round or lead-score>=20:
                if (score+total>lead or total//10>=4) and total%10>5:
                    bank()
                else:
                    roll_dice()
            else:
                if total%10>7:
                    bank()
                else:
                    roll_dice()
if 'save.txt' in os.listdir():
    load_save()
    if len(players)==0:
        start()
else:
    start()
main()
