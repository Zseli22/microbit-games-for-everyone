from microbit import *
import random
import speech
import os
c=pin15.read_digital()==1
if c:
    mp=pin2
else:
    pin1.set_touch_mode(pin1.CAPACITIVE)
    pin2.set_touch_mode(pin2.CAPACITIVE)
    mp=None
def q():
    if c:
        return (pin15.read_digital()==0,pin16.read_digital()==0,
                pin8.read_digital()==0,pin14.read_digital()==0,
                pin12.read_digital()==0,pin13.read_digital()==0,False,False)
    return (button_a.is_pressed(),button_b.is_pressed(),pin_logo.is_touched(),
            pin1.is_touched() or pin2.is_touched(),False,False,
            accelerometer.is_gesture('shake'),accelerometer.is_gesture('face down'))
def release_a():
    while c and pin15.read_digital()==0:
        sleep(20)
NUMBER_TONES=[392,523,587,659,699,784,880,988,1047,1175,1319,1397,1568]
PLUS_TONES=[587,699,880,1047,1319]
CODES='0123456789abc'
FULL_DECK=list('01'+''.join(CODES[i]*i for i in range(2,13))+'jjjkkkllldefghi')
players=[]
deck=[]
player=0
ph='setup'
oi=0
re=False
freeze_img=Image('90009:09090:00900:09090:90009')
flip3_img=Image('09990:00090:00990:00090:09990')
second_img=Image('09990:90009:90009:90009:09990')
times2_img=Image.DIAMOND
bank_tones=[1175,1568,1760,1976,2349]
complete_tones=[1319,1568,2637,2093,2349,3136]
load_tones=[1046,1175,1568]
win_tones=[1046,831,659,523,466,415,1175,932,699,587,523,466,1245,1046,831,622,523,415,1397,1175,932,698,587,466,263,294,330,392,523,587,659,784,1047,1175,1319,1568]
flip7_win_tones=[587,698,932,1047,1175,1397,1865]
def w(effect):
    audio.play(effect,pin=mp)
def t(p,d):
    w(audio.SoundEffect(freq_start=p,freq_end=p,duration=d))
def p(text):
    speech.pronounce(text,pin=mp)
def s(text):
    speech.say(text,pin=mp)
def clear_save():
    if 'save.txt' in os.listdir():
        os.remove('save.txt')
def reset_round():
    global re
    re=False
    for x in players:
        x['h']=[]
        x['l']=''
        x['e']=False
def reset_game():
    global player,ph,oi,re
    players.clear()
    deck[:] = []
    player=0
    ph='setup'
    oi=0
    re=False
def save_game():
    with open('save.txt','w') as save:
        save.write(str((players,''.join(deck),(player,ph[0],oi,re))))
def shuffle_feedback():
    blip=300
    for i in range(3):
        while blip<1800:
            blip+=random.randint(round(blip*0.05),round(blip*0.1))
            t(blip,30)
            display.show(Image.ALL_CLOCKS[scale(blip,from_=(300,2000),to=(0,11))])
        blip=300
    display.clear()
    sleep(1000)
def rebuild_deck(play_feedback=True):
    deck[:] = FULL_DECK[:]
    for x in players:
        for card in x['h']:
            if card in deck:
                deck.remove(card)
    if play_feedback:
        shuffle_feedback()
def draw_from_deck():
    if len(deck)==0:
        rebuild_deck()
    card=random.choice(deck)
    deck.remove(card)
    return card
def next_active(index):
    start=index
    while True:
        if not players[index]['e']:
            return index
        index=(index+1)%len(players)
        if index==start:
            return -1
def N(x):
    values=[]
    for card in x['h']:
        value=CODES.find(card)
        if value>=0:
            values.append(value)
    return values
def R(x):
    h=x['h']
    nums=N(x)
    total=0
    for value in nums:
        total+=value
    for card in h:
        value='defgh'.find(card)
        if value>=0:
            total+=(value+1)*2
    if 'i' in h:
        total*=2
    if len(nums)==7:
        total+=15
    return total
def card_key(card):
    value=CODES.find(card)
    if value>=0:
        return (0,value)
    value='defgh'.find(card)
    if value>=0:
        return (1,(value+1)*2)
    if card=='i':
        return (2,0)
    if card=='l':
        return (3,0)
    return (4,0)
def sort_hand(x):
    x['h'].sort(key=card_key)
def count(value):
    if value==0:
        t(131,250)
    while value>=100:
        t(1175,320)
        value-=100
        sleep(160)
    while value>=10 and value<=100:
        t(784,220)
        value-=10
        sleep(160)
    while value>=1 and value<10:
        t(523,90)
        value-=1
        sleep(160)
def has_second(x):
    return 'l' in x['h']
def cpu_should_bank(index):
    x=players[index]
    if has_second(x):
        return False
    total=R(x)
    score=x['s']
    unique=len(N(x))
    high=0
    for i,x in enumerate(players):
        if i!=index and x['s']>high:
            high=x['s']
    if high>=180:
        return score+total>high
    if high>=score+40 or high>=120:
        return total>=25 and unique>=5
    return total>=25 and unique>=3
def show_number(value,fast=False):
    show_mark(CODES[value])
    t(NUMBER_TONES[value],90 if fast else 120)
def show_mark(card):
    value=CODES.find(card)
    if value>=0:
        display.show(value if value<10 else 'X' if value==10 else 'J' if value==11 else 'Q')
    else:
        value='defgh'.find(card)
        if value>=0:
            display.show((value+1)*2 if value<4 else 'X')
        elif card=='i':
            display.show(times2_img)
        elif card=='j':
            display.show(freeze_img)
        elif card=='k':
            display.show(flip3_img)
        elif card=='l':
            display.show(second_img)
def show_card(card,fast=False):
    value=CODES.find(card)
    if value>=0:
        show_number(value,fast)
    else:
        value='defgh'.find(card)
        if value>=0:
            display.show('+')
            t(PLUS_TONES[value],90)
            sleep(120)
            show_number((value+1)*2,True)
        elif card=='i':
            display.show(times2_img)
            for tone in [784,988,1175]:
                t(tone,70)
        elif card=='j':
            display.show(freeze_img)
            w(audio.SoundEffect(freq_start=1200,freq_end=1200,duration=280,waveform=audio.SoundEffect.WAVEFORM_NOISE))
        elif card=='k':
            display.show(flip3_img)
            for _ in range(3):
                blip=random.randint(200,500)
                w(audio.SoundEffect(freq_start=blip,freq_end=blip*2,duration=120,vol_start=0,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR))
                sleep(80)
        elif card=='l':
            display.show(second_img)
            for tone in complete_tones:
                t(tone,100)
def S(index):
    display.show(index+1)
    s('player '+str(index+1))
def announce_round_points(index,banked=False):
    sleep(300)
    total=R(players[index])
    display.scroll(total,delay=50)
    count(total)
    if banked:
        for tone in bank_tones:
            t(tone,60)
def V(value):
    display.scroll(value,delay=50)
    count(value)
def view_tones(on):
    t(784 if on else 988,70)
    t(988 if on else 784,70)
def view_cards(index,target=False):
    x=players[index]
    hand=x['h']
    view_tones(True)
    while (pin_logo.is_touched() if not c else pin8.read_digital()==0):
        sleep(20)
    if len(hand)==0:
        V(R(players[index]))
        view_tones(False)
        return
    pos=-1
    display.clear()
    while True:
        a,b,u,d,l,r,_,_=q()
        if ((not c and a) or l or r):
            pos=(pos-1 if l else pos+1)%len(hand)
            show_card(hand[pos])
            sleep(120)
        elif b:
            V(R(players[index]))
            sleep(200)
            if pos>=0:
                show_mark(hand[pos])
            else:
                display.clear()
        elif u:
            view_tones(False)
            while (pin_logo.is_touched() if not c else pin8.read_digital()==0):
                sleep(20)
            return
        elif target and d:
            V(x['s'])
            sleep(200)
            if pos>=0:
                show_mark(hand[pos])
            else:
                display.clear()
def second_chance_used():
    display.show(second_img)
    w(audio.SoundEffect(freq_start=1600,freq_end=120,waveform=audio.SoundEffect.WAVEFORM_NOISE,duration=1000,shape=audio.SoundEffect.SHAPE_LINEAR))
def C():
    for x in players:
        V(x['s'])
        sleep(150)
def choose_from_targets(targets):
    if len(targets)==1:
        return targets[0]
    selection=0
    s('choose player')
    display.show(targets[selection]+1)
    speech.say(str(targets[selection]+1),speed=60,pin=mp)
    while True:
        a,b,u,d,l,r,_,_=q()
        if (not c and a) or l or r:
            selection=(selection-1 if l else selection+1)%len(targets)
            display.show(targets[selection]+1)
            speech.say(str(targets[selection]+1),speed=60,pin=mp)
            sleep(100)
        elif (not c and b) or (c and a):
            display.show(Image.YES)
            release_a()
            return targets[selection]
        elif u:
            view_cards(targets[selection],True)
            display.show(targets[selection]+1)
        elif d:
            V(players[targets[selection]]['s'])
def target_list(second=False):
    targets=[]
    for i,x in enumerate(players):
        if not x['e'] and (not second or not has_second(x)):
            targets.append(i)
    return targets
def choose_target(targets,mode,index):
    if players[index]['t']==1:
        if len(targets)>1 and index in targets:
            targets=[target for target in targets if target!=index]
        if mode=='freeze':
            return max(targets,key=lambda x:players[x]['s'])
        return max(targets,key=cpu_target)
    return choose_from_targets(targets)
def cpu_target(index):
    x=players[index]
    nums=N(x)
    return (max(nums) if nums else -1,len(nums),x['s'])
def end_player_round(index):
    players[index]['e']=True
def trigger_flip7(index):
    global re
    x=players[index]
    display.show(Image.FABULOUS)
    for tone in flip7_win_tones:
        t(tone,70)
    t(2093,400)
    x['s']+=R(x)
    announce_round_points(index)
    sleep(300)
    V(x['s'])
    re=True
    x['e']=True
    for y in players:
        if y is not x and not y['e']:
            y['s']+=R(y)
            y['e']=True
def force_flip_three(target):
    x=players[target]
    pending=[]
    for _ in range(3):
        if x['e'] or re:
            break
        forced_card=draw_from_deck()
        if forced_card=='j' or forced_card=='k':
            show_card(forced_card)
            sleep(250)
            pending.append(forced_card)
        else:
            result=apply_card(target,forced_card)
            if result=='round_end':
                return result
            if x['e']:
                break
        sleep(250)
    if x['e'] or re:
        return 'continue'
    for action in pending:
        result=apply_card(target,action)
        if result=='round_end':
            return result
        if x['e']:
            break
    return 'continue'
def apply_card(index,card):
    x=players[index]
    show_card(card)
    sleep(250)
    if card in CODES:
        if card in x['h']:
            if has_second(x):
                x['h'].remove('l')
                second_chance_used()
                sleep(250)
                return 'continue'
            display.show(Image.SKULL)
            w(audio.SoundEffect(freq_start=196,freq_end=196,duration=600,vol_end=255))
            w(audio.SoundEffect(freq_start=139,freq_end=139,duration=600,vol_end=255))
            end_player_round(index)
            return 'ended'
        x['h'].append(card)
        sort_hand(x)
        x['l']=card
        if len(N(x))==7:
            trigger_flip7(index)
            return 'round_end'
        return 'continue'
    if card in 'defghi':
        x['h'].append(card)
        sort_hand(x)
        x['l']=card
        return 'continue'
    if card=='l':
        if not has_second(x):
            x['h'].append(card)
            sort_hand(x)
            x['l']=card
            return 'continue'
        targets=target_list(True)
        if len(targets)==0:
            return 'continue'
        target=choose_target(targets,'second',index)
        if target>=0 and target!=index:
            y=players[target]
            y['h'].append('l')
            sort_hand(y)
            s('second chance. player '+str(target+1))
        return 'continue'
    if card=='j':
        targets=target_list()
        target=choose_target(targets,'freeze',index)
        s('freeze player '+str(target+1))
        y=players[target]
        y['s']+=R(y)
        announce_round_points(target)
        sleep(300)
        V(y['s'])
        end_player_round(target)
        return 'ended' if target==index else 'continue'
    if card=='k':
        targets=target_list()
        target=choose_target(targets,'flip3',index)
        s('flip three. player '+str(target+1))
        return force_flip_three(target)
    return 'continue'
def D(index,fast=False):
    blip=random.randint(200,500)
    w(audio.SoundEffect(freq_start=blip,freq_end=blip*2,duration=160,vol_start=0,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR))
    display.show(Image.ARROW_S)
    if fast:
        sleep(60)
    else:
        sleep(150)
    card=draw_from_deck()
    display.clear()
    if fast:
        sleep(120)
    else:
        sleep(300)
    result=apply_card(index,card)
    if fast:
        sleep(120)
    else:
        sleep(250)
    if players[index]['l']!='':
        show_mark(players[index]['l'])
    return result
def end_round():
    high=max(x['s'] for x in players)
    leaders=[i for i,x in enumerate(players) if x['s']==high]
    if high>=200 and len(leaders)==1:
        display.scroll('Winner! player',delay=100)
        display.scroll(leaders[0]+1)
        s('The winner is, player '+str(leaders[0]+1)+'.')
        for tone in win_tones:
            t(tone,40)
        t(2093,1000)
        clear_save()
        reset_game()
        start()
        return 'restart'
    if high>=200 and len(leaders)>1:
        s('tie. another round.')
    start_round()
    save_game()
    return 'continue'
def finish_turn():
    global player
    n=next_active((player+1)%len(players))
    if re or n<0:
        return end_round()
    player=n
    S(player)
    sleep(200)
    save_game()
    return 'continue'
def bank_current():
    x=players[player]
    x['s']+=R(x)
    announce_round_points(player,True)
    sleep(300)
    V(x['s'])
    end_player_round(player)
    return finish_turn()
def cpu_turn():
    display.show(Image.ASLEEP)
    sleep(random.randint(700,1600))
    display.clear()
    if cpu_should_bank(player):
        return bank_current()
    result=D(player)
    if result=='round_end':
        return end_round()
    return finish_turn()
def opening_step():
    global oi,ph,player
    while oi < len(players):
        index=oi
        oi+=1
        if players[index]['e']:
            continue
        player=index
        S(player)
        if D(index,True)=='round_end':
            return end_round()
        return 'continue'
    ph='turn'
    player=next_active(0)
    if player<0:
        return end_round()
    S(player)
    save_game()
    return 'continue'
def start_round():
    global ph,oi,player
    reset_round()
    ph='opening'
    oi=0
    player=0
def start():
    global player
    p('FLIH5P SEH4VAX7N.')
    sleep(1000)
    p('sih7leh4kt - pley3er8rz.')
    while True:
        a,b,u,d,l,r,sh,_=q()
        if (l or (not c and a)) and len(players)<=9:
            display.scroll('H',delay=50)
            t(1568,75)
            t(2093,75)
            players.append({'t':0,'s':0,'h':[],'l':'','e':False})
        elif (r or (not c and b)) and len(players)<=9:
            display.scroll('C',delay=50)
            t(784,75)
            t(1046,75)
            players.append({'t':1,'s':0,'h':[],'l':'','e':False})
        elif ((c and a) or (not c and (sh or len(players)==10))) and len(players)>1:
            rebuild_deck(False)
            player=0
            start_round()
            release_a()
            if not c and sh:
                sleep(500)
            return
def load_save():
    global players,deck,player,ph,oi,re
    asked=False
    p('FLIH5P SEH4VAX7N.')
    sleep(1000)
    p('wuh6d yuw6 lay5k tuw8 rih7zuw5m yer7 sey5vd gey7m?')
    while True:
        a,b,u,d,l,r,_,f=q()
        if a:
            with open('save.txt','r') as save:
                data=eval(save.read())
            players[:]=data[0]
            deck=list(data[1])
            player,ph,oi,re=data[2]
            ph='opening' if ph=='o' else 'turn'
            display.show(Image.SMILE)
            for tone in load_tones:
                t(tone,75)
            t(2093,400)
            C()
            S(player)
            release_a()
            return
        elif b:
            display.show(Image.SCISSORS)
            asked=True
            p('aa5r yuw5 shuh7er6? Ter6n miy7 ah7psay7 daw4n tax6 kax7nfer8m.')
        if (f or (c and d)) and asked==True:
            clear_save()
            display.show(Image.SKULL)
            t(263,90)
            t(131,90)
            t(65,90)
            sleep(500)
            display.clear()
            return
def main():
    while True:
        if ph=='opening':
            state=opening_step()
            if state=='restart':
                return
        else:
            if players[player]['e']:
                state=finish_turn()
                if state=='restart':
                    return
                continue
            if players[player]['t']==1:
                state=cpu_turn()
                if state=='restart':
                    return
            else:
                if players[player]['l']!='':
                    show_mark(players[player]['l'])
                else:
                    display.show(Image.HEART)
                a,b,u,d,l,r,sh,_=q()
                if a or (not c and sh):
                    result=D(player)
                    release_a()
                    if result=='round_end':
                        state=end_round()
                    else:
                        state=finish_turn()
                    if state=='restart':
                        return
                elif b:
                    state=bank_current()
                    if state=='restart':
                        return
                elif u:
                    view_cards(player)
                    sleep(300)
                elif d:
                    C()
                    sleep(400)
if 'save.txt' in os.listdir():
    load_save()
    if len(players)==0:
        start()
else:
    start()
while True:
    main()
