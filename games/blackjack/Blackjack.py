from microbit import *
import random,speech,os
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
full_deck=[]
full_deck.extend([0]*16)
for i in range(1,10):
    full_deck.extend([i]*4)
deck=[]
hand=[]
dealer_hand=[]
total=0
dealer_total=0
tones=[1319, 1397, 587, 659, 699, 784, 880, 988, 1047, 1175]
win_tones=[587,698,932,1047,1175,1397,1865]
lose_tones=[262,247,233,220]
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
    global decrease, increase, confirm, alt, status
    if controller==False:
        increase=pin_logo.is_touched()
        decrease=pin1.is_touched() or pin2.is_touched()
        confirm=button_a.is_pressed()
        alt=button_b.is_pressed()
        status=accelerometer.is_gesture('down')
    elif controller==True:
        status=pin8.read_digital()==0
        decrease=pin12.read_digital()==0
        increase=pin13.read_digital()==0
        confirm=pin15.read_digital()==0
        alt=pin16.read_digital()==0

def shuffle():
    global full_deck,deck
    deck.clear()
    for i in range(3):
        blip=300
        while blip<1800:
            blip+=random.randint(round(blip*0.05),round(blip*0.1))
            audio.play(audio.SoundEffect(freq_start=blip,freq_end=blip,duration=30),pin=music_pin)
            display.show(Image.ALL_CLOCKS[scale(blip,from_=(300,2000), to=(0,11))])
    deck=full_deck[:]
    display.clear()
    sleep(1000)
def hand_value(cards):
    value=0
    aces=0
    for card in cards:
        if card==0:
            value+=10
        elif card==1:
            aces+=1
            value+=11
        else:
            value+=card
    while value>21 and aces>0:
        value-=10
        aces-=1
    return value

def draw(mode=0):
    global hand,dealer_hand,deck,tones,total,dealer_total
    blip=random.randint(200,500)
    if mode==0:
        audio.play(audio.SoundEffect(freq_start=blip,freq_end=blip*2,duration=200,vol_start=0,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR),pin=music_pin)
        display.show(Image.ARROW_S)
    elif mode>0:
        audio.play(audio.SoundEffect(freq_start=blip//2,freq_end=blip,duration=200,vol_start=0,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR),pin=music_pin)
        display.show(Image.ARROW_N)
    card=random.choice(deck)
    deck.remove(card)
    if mode==0:
        hand.append(card)
    elif mode>0:
        dealer_hand.append(card)
    display.clear()
    sleep(600)
    if mode<2:
        show(card,fast=False)
    if mode==0:
        total=hand_value(hand)
    else:
        dealer_total=hand_value(dealer_hand)
    sleep(300)
    display.clear()
def show(value=-1,fast=False):
    if value==0:
        display.show('X')
    elif value==1:
        display.show('A')
    else:
        display.show(value)
    if fast==True:
        audio.play(audio.SoundEffect(freq_start=tones[value],freq_end=tones[value],duration=100),pin=music_pin)
    else:
        audio.play(audio.SoundEffect(freq_start=tones[value],freq_end=tones[value],duration=200),pin=music_pin)

def main():
    global deck,hand,dealer_hand,total,dealer_total,tones,win_tones,lose_tones
    coins=100
    bet=10
    modified_bet=10
    blackjack=False
    double=False
    state='waiting'
    speech.pronounce('leh4ts pley7 blae3kjae8k.',pin=music_pin)
    while True:
        update()
        if state=='waiting':
            display.show(Image.HEART)
            if confirm==True:
                if len(deck)<=10:
                    shuffle()
                draw(0)
                draw(1)
                draw(0)
                draw(2)
                display.scroll(total,delay=50)
                speech.say('You have '+str(total)+'.',pin=music_pin)
                if total==10 or total==11:
                    if bet*2>coins:
                        display.show(Image.ANGRY)
                        speech.pronounce('yuw5 duw7 naa4t /hae6v ih6nah7f mah8niy6 tax7 dah7bax8l daw5n.',pin=music_pin)
                    else:
                        speech.pronounce('wuh8d yuw6 lay5k tax7 dah5bax8l daw7n?',pin=music_pin)
                        double=True
                if total==21:
                    display.show(Image.FABULOUS)
                    speech.pronounce('blae3kjae5k..',pin=music_pin)
                    blackjack=True
                    state='dealer'
                else:
                    state='hit'
            elif alt==True:
                if len(deck)<=10:
                    display.show(Image.CLOCK12)
                    speech.pronounce('Dhax7 deh4k ih6z ax7baw6t tax7 biy7 riy7shah4fax8ld.',pin=music_pin)
                else:
                    speech.pronounce('dhax7 deh4k kax6ntey5nz,',pin=music_pin)
                    for i in range(len(deck)):
                        show(deck[i],fast=True)
                        sleep(200)
                    display.clear()
                    sleep(500)
            if increase==True and bet+5<=coins:
                if bet==1:
                    bet+=4
                elif bet+5>coins:
                    bet=coins
                else:
                    bet+=5
                audio.play(audio.SoundEffect(freq_start=scale(bet,from_=(0,100),to=(300,1600)),freq_end=scale(bet,from_=(0,100),to=(300,1600)),duration=100),pin=music_pin)
                if bet==coins:
                    display.show(Image.SCISSORS)
                    speech.pronounce('ao5l ih8n.',pin=music_pin)
                sleep(200)
            elif decrease==True and bet>1:
                if bet==5:
                    bet-=4
                else:
                    bet-=5
                audio.play(audio.SoundEffect(freq_start=scale(bet,from_=(0,100),to=(300,1600)),freq_end=scale(bet,from_=(0,100),to=(300,1600)),duration=100),pin=music_pin)
                if bet==1:
                    display.show(1)
                    speech.pronounce('wah5n koy8n.',pin=music_pin)
                sleep(200)
            elif status==True:
                display.scroll(coins,delay=50)
                speech.say('You have '+str(coins)+' coins.',pin=music_pin)
                display.scroll(bet,delay=50)
                speech.say('You are betting '+str(bet)+'.',pin=music_pin)
        elif state=='hit':
            if double==True:
                display.show('!')
            else:
                display.show('?')
            if confirm==True:
                draw(0)
                display.scroll(total,delay=50)
                speech.say(str(total)+'.',pin=music_pin)
                if total>21:
                    display.show(Image.SKULL)
                    audio.play(audio.SoundEffect(freq_start=98,freq_end=98,duration=220,vol_end=255),pin=music_pin)
                    audio.play(audio.SoundEffect(freq_start=69,freq_end=69,duration=220,vol_end=255),pin=music_pin)
                    speech.pronounce('bah3stih8d.',pin=music_pin)
                    state='lose'
                    sleep(300)
                if double==True or total==21:
                    state='dealer'
            elif alt==True:
                if double==True:
                    speech.pronounce('now5 dah6bax7lih8nx.',pin=music_pin)
                    double=False
                elif double ==False:
                    state='dealer'
            elif increase==True:
                for i in range(len(hand)):
                    show(hand[i],fast=False)
                    sleep(250)
                sleep(500)
                show(dealer_hand[0],fast=False)
        elif state=='dealer':
            display.scroll(dealer_total,delay=50)
            speech.say('I have, '+str(dealer_total)+'.',pin=music_pin)
            while dealer_total<17:
                draw(1)
                display.scroll(dealer_total,delay=50)
                speech.say(str(dealer_total)+'.',pin=music_pin)
            if dealer_total>=17 and dealer_total<=21:
                speech.say('I stand.',pin=music_pin)
                state='check'
            if dealer_total>21:
                display.show(Image.SKULL)
                audio.play(audio.SoundEffect(freq_start=98,freq_end=98,duration=220,vol_end=255),pin=music_pin)
                audio.play(audio.SoundEffect(freq_start=69,freq_end=69,duration=220,vol_end=255),pin=music_pin)
                speech.pronounce('bah3stih8d.',pin=music_pin)
                sleep(300)
                state='win'
        elif state=='check':
            if total==dealer_total:
                display.show(Image.MEH)
                speech.pronounce('ih7ts ax8 puh4sh.',pin=music_pin)
                sleep(300)
                state='over'
            elif dealer_total>total:
                state='lose'
            elif total>dealer_total:
                state='win'
        elif state=='lose':
            if double==True:
                coins-=bet*2
            else:
                coins-=bet
            display.show(Image.SAD)
            for i in range(len(lose_tones)):
                audio.play(audio.SoundEffect(freq_start=lose_tones[i],freq_end=lose_tones[i],duration=110),pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=208,freq_end=208,duration=400),pin=music_pin)
            sleep(300)
            state='over'
        elif state=='win':
            modified_bet=bet
            if double==True:
                modified_bet*=2
            if blackjack==True:
                modified_bet=round(modified_bet*1.5)
            coins+=modified_bet
            display.show(Image.HAPPY)
            for i in range(len(win_tones)):
                audio.play(audio.SoundEffect(freq_start=win_tones[i],freq_end=win_tones[i],duration=70),pin=music_pin)
            audio.play(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=400),pin=music_pin)
            sleep(200)
            state='over'
        elif state=='over':
            hand.clear()
            dealer_hand.clear()
            total=0
            dealer_total=0
            blackjack=False
            double=False
            display.scroll(coins,delay=50)
            speech.say('You now have '+str(coins)+' coins.',pin=music_pin)
            if coins==0:
                reset()
            if bet>coins:
                bet=5*(coins//5)
                display.scroll(bet,delay=50)
                speech.say('Your bet is now down to,'+str(bet)+'.',pin=music_pin)
            state='waiting'
main()