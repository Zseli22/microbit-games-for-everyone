from microbit import *
import random
import music
import speech
import os
accelerometer.set_range(8)
menu_tones=[523, 587, 659, 699, 784, 880, 988, 1047, 1175, 1319, 1397, 1568, 1760, 1976, 2093]
score_tones=[523,784,1175,1319,1047]
high_score_tones=[523,784,1175,1319,1568,1760,1175,1480,1760,2349,1319,1480,1661,1976,2637]
menu=['Mash it!','Shake it!','Tap it!','Time check.','hurry up!','Count and shout!','Micro Pong']
descriptions=['preh4s dhax7 - ey3y8 - bah7tax5n ae5z kwih4kliy6 ae6z yuw7 kae8n.','shey4k dhax7 yuw3nih5t ae6z /haa4rd ae6z yuw7 kae8n.','tae4p dhax7 low3gow5 ae5z meh4niy6 tay5mz ae6z yuw7 kae8n.','preh5s - ey3y8 - tax8 pley5 dhax7 reh4frax6ns tow8n, dheh4n, /how3ld dhax7 bah7tax5n foh5r ae5z lao4nx ae5z yuw6 thih5nxk dhax8 saw6nd lae7stih8d.','weh6n yuw6 /hiy4er dhax7 ther4d - /hay3ax7st tow4n, preh5s dhiy7 ey3 bah5tax8n. dhax7 gey5m lae4sts teh3n raw8ndz.','kaw4nt dhax7 nah5mber6 ax7v tow3nz yuw5 /hiy4er, dheh4n, mey4k ae6z meh5niy6 saw4ndz ih6ntax6 dhax7 may3krax6fow7n.','tray4 tax7 kiy5p dhax6 bao5l frax6m fao4lih6nx ao6f dhax7 say4dz ax6v dhax7 skriy4n bay7 /hih5tih6nx ih6t leh4ft oh6r ray4t wih6dh dhax7 bah4tax7nz.']
high_scores=[0]*len(menu)
high_scores[4]=1000
timer=0
score=0
game=0
blip=0

def save():
    global high_scores
    if 'save.txt' in os.listdir():
        os.remove('save.txt')
    with open('save.txt','w') as f:
        for i in range(len(high_scores)):
            f.write(str(high_scores[i])+' ')
        f.close()
def reset_all():
    global high_scores
    asked=False
    speech.say('Re set all high scores to 0?')
    while True:
        display.show(Image.SCISSORS)
        if button_a.is_pressed() and asked==False:
            asked=True
            speech.say('Face down to confirm re set.')
        if button_b.is_pressed():
            return
        if accelerometer.is_gesture('face down') and asked==True:
            os.remove('save.txt')
            for i in range(len(high_scores)):
                high_scores[i]=0
            high_scores[4]=1000
            display.show(Image.SKULL)
            speech.say('complete.')
            sleep(150)
            return

def countdown():
    tones=[523,523,523]
    numbers=[3,2,1]
    for i in range(len(numbers)):
        display.show(numbers[i])
        audio.play(audio.SoundEffect(freq_start=tones[i],freq_end=tones[i],duration=200),wait=False)
        sleep(800)
    display.show(0)
    audio.play(audio.SoundEffect(freq_start=1046,freq_end=1046,duration=700),wait=False)
def gameover():
    global score,high_scores,score_tones,high_score_tones,game
    if game<3 or game==6:
        audio.play(audio.SoundEffect(freq_start=125,freq_end=125,duration=500,vol_end=255),wait=False)
        display.show(Image.NO)
    sleep(1500)
    if (score>high_scores[game] and game!=4) or (score<high_scores[game] and game==4):
        display.show(Image.HAPPY)
        for i in range(len(high_score_tones)):
            audio.play(audio.SoundEffect(freq_start=high_score_tones[i],freq_end=high_score_tones[i],duration=75))
        speech.pronounce('/hay3 skoh2r.')
        high_scores[game]=score
        save()
    else:
        display.show(Image.SMILE)
        for i in range(len(score_tones)):
            audio.play(audio.SoundEffect(freq_start=score_tones[i],freq_end=score_tones[i],duration=75))
    display.scroll(score)
    if game==0:
        speech.say('You pressed the button, '+str(score)+', times.')
    elif game==1:
        speech.say('The maximum strength was, '+str(score)+'.')
    elif game==2:
        speech.say('You tapped the lowgo,'+str(score)+', times. ')
    if game==3:
        speech.say('Your timing was '+str(score)+'percent accurate.')
    if game==4:
        speech.say('Your average re action time was, '+str(score)+' milly secnds.')
    if game==5:
        speech.say('You were'+str(score)+' percent accurate.')
    if game==6:
        speech.say('Your score is, '+str(score)+'.')
    score=0
    speech.say('Press - B - to play again.')
    display.show(Image.HEART)

def main():
    global game,menu,menu_tones,timer,high_scores
    if 'save.txt' in os.listdir():
        with open('save.txt','r') as f:
            datastr=f.read()
            f.close()
        data=datastr.split()
        for i in range(len(data)):
            if data[i].find('.')>=0:
                high_scores[i]=float(data[i])
            else:
                high_scores[i]=int(data[i])
        sleep(150)
        if button_a.is_pressed():
            reset_all()
    game=-1
    speech.say('Select - game.')
    display.show(Image.HEART)
    while True:
        if game>=0:
            display.show(game)
        if button_a.is_pressed():
            if game==len(menu)-1:
                game=0
            else:
                game+=1
            audio.play(audio.SoundEffect(freq_start=menu_tones[game],freq_end=menu_tones[game],duration=30))
            timer=running_time()
            sleep(200)
        if button_b.is_pressed() and game>=0:
            countdown()
            playing()
            gameover()
        if accelerometer.is_gesture('shake') and game>=0:
            speech.pronounce(descriptions[game])
        if pin_logo.is_touched() and game>=0:
            display.scroll(high_scores[game])
            speech.say('High score, '+str(high_scores[game])+'.')
            sleep(300)
            while pin_logo.is_touched():
                for i in range(3):
                    display.show(Image.SCISSORS)
                    audio.play(audio.SoundEffect(freq_start=850,freq_end=1650,duration=180,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR))
                speech.say('Face down to confirm re set.')
                while True:
                    if accelerometer.is_gesture('face down'):
                        if game==4:
                            high_scores[game]=1000
                        else:
                            high_scores[game]=0
                        speech.say('complete.')
                        display.show(Image.SKULL)
                        sleep(200)
                        save()
                        break
                    if button_a.is_pressed() or button_b.is_pressed():
                        break
                
        if running_time()-timer in range(1000,1050):
            speech.say(menu[game])
def playing():
    global game,timer,score,blip
    if game==0:
        timer=running_time()
        while True:
            if running_time()-timer >5000:
                return()
            if button_a.was_pressed():
                blip=random.randint(500,3000)
                audio.play(audio.SoundEffect(freq_start=blip,freq_end=blip,duration=20),wait=False)
                score+=1
    elif game==1:
        timer=running_time()
        while True:
            music.pitch(scale(score,from_=(1000,15000),to=(110,1760)))
            if running_time()-timer >5000:
                music.stop()
                return()
            if accelerometer.get_strength()>score:
                score=accelerometer.get_strength()
    elif game==2:
        touched=False
        timer=running_time()
        while True:
            if running_time()-timer >5000:
                return()
            if pin_logo.is_touched():
                touched=True
            if touched==True:
                if pin_logo.is_touched():
                    pass
                if pin_logo.is_touched()==False:
                    blip=random.randint(500,3000)
                    audio.play(audio.SoundEffect(freq_start=blip,freq_end=blip,duration=20))
                    score+=1
                    touched=False
    elif game==3:
        touched=False
        state='play'
        while True:
            display.show(Image.HEART)
            if state=='play':
                if button_a.is_pressed():
                    length=random.randint(1000,4000)
                    display.show(Image.MUSIC_QUAVER)
                    music.pitch(440,duration=length,wait=True)
                    state='record'
            elif state=='record':
                if button_a.is_pressed():
                    if touched==False:
                        timer=running_time()
                        touched=True
                    elif touched==True:
                        display.show(Image.MUSIC_CROTCHET)
                        music.pitch(440,duration=20,wait=False)
                if button_a.is_pressed()==False and touched==True:
                    result=running_time()-timer
                    score=100-(round(abs(100-(result/length*100)),2))
                    speech.say('The reference tone was '+str(length)+'milly secnds long, ')
                    speech.say('and you held the button for '+str(result)+' milly secnds.')
                    return
    elif game==4:
        sleep(2000)
        reactions=[]
        blip=random.randint(300,1800)
        state='low'
        timer=running_time()
        while True:
            while len(reactions)<10:
                if state=='low':
                    display.show(Image('33333\n'*5))
                    music.pitch(220,duration=20,wait=False)
                    if running_time()-timer>1000:
                        music.stop()
                        state='medium'
                        timer=running_time()
                elif state=='medium':
                    display.show(Image('66666\n'*5))
                    music.pitch(440,duration=20,wait=False)
                    if button_a.is_pressed():
                        music.stop()
                        state='early'
                    if running_time()-timer>blip:
                        music.stop()
                        timer=running_time()
                        state='high'
                elif state=='high':
                    display.show(Image('99999\n'*5))
                    music.pitch(880,duration=20,wait=False)
                    if button_a.is_pressed():
                        music.stop()
                        state='correct'
                elif state=='correct':
                    reactions.append(running_time()-timer)
                    display.show(Image.YES)
                    audio.play(audio.SoundEffect(freq_start=1319,freq_end=1319,duration=50))
                    audio.play(audio.SoundEffect(freq_start=1760,freq_end=1760,duration=50))
                    display.show(Image.ASLEEP)
                    sleep(800)
                    blip=random.randint(300,1800)
                    timer=running_time()
                    state='low'
                elif state=='early':
                    display.show(Image.ANGRY)
                    audio.play(audio.SoundEffect(freq_start=110,freq_end=110,duration=300,vol_end=255))
                    display.show(Image.ASLEEP)
                    sleep(800)
                    reactions.append(1000)
                    blip=random.randint(300,1800)
                    timer=running_time()
                    state='low'
            result=0
            for i in range(len(reactions)):
                result+=reactions[i]
            score=int(result/len(reactions))
            return
    elif game==5:
        result=0
        length=random.randint(15,40)
        state='play'
        while True:
            display.show(Image.HEART)
            if state=='play':
                if button_a.is_pressed():
                    for i in range(length):
                        display.show(Image.MUSIC_CROTCHET)
                        music.pitch(500+(10*i), duration=100)
                        display.clear()
                        sleep(random.randint(150,800))
                    sleep(1500)
                    audio.play(audio.SoundEffect(freq_start=1000,freq_end=1000,duration=75))
                    audio.play(audio.SoundEffect(freq_start=2000,freq_end=2000,duration=75))
                    state='record'
                    timer=running_time()
            elif state=='record':
                if microphone.is_event(SoundEvent.LOUD):
                    timer=running_time()
                    display.show(Image.MUSIC_CROTCHET)
                    result+=1
                    music.pitch(500+(10*result),duration=100)
                    sleep(200)
                if running_time()-timer>3000 or button_a.is_pressed():
                    audio.play(audio.SoundEffect(freq_start=2000,freq_end=2000,duration=75))
                    audio.play(audio.SoundEffect(freq_start=1000,freq_end=1000,duration=75))
                    sleep(1500)
                    speech.say('I detected'+str(result)+' sounds, and the correct number was '+str(length)+'.')
                    score=100-(round(abs(100-(result/length*100)),2))
                    return
    elif game==6:
        blip=0
        length=400
        touched=False
        display.show(Image('00500:00500:00000:00500:00500'))
        sleep(2000)
        timer=running_time()
        blip=2
        display.set_pixel(blip,2,9)
        audio.play(audio.SoundEffect(freq_start=784,freq_end=784,duration=30),wait=False)
        while True:
            if button_a.is_pressed() and blip<2 and touched==False:
                touched=True
                timer=running_time()
                audio.play(audio.SoundEffect(freq_start=523,freq_end=523,duration=30),wait=False)
                score+=1
                length-=random.randint(round(length*0.01),round(length*0.04))
            if button_b.is_pressed() and blip>2 and touched==True:
                touched=False
                timer=running_time()
                audio.play(audio.SoundEffect(freq_start=784,freq_end=784,duration=30),wait=False)
                score+=1
                length-=random.randint(round(length*0.01),round(length*0.04))
            if running_time()-timer>length:
                if touched==False:
                    if blip>0:
                        display.set_pixel(blip,2,0)
                        blip-=1
                        display.set_pixel(blip,2,9)
                        timer=running_time()
                    else:
                        display.set_pixel(blip,2,0)
                        audio.play(audio.SoundEffect(freq_start=2000,freq_end=1000,duration=1000,shape=audio.SoundEffect.SHAPE_LINEAR))
                        return
                elif touched==True:
                    if blip<4:
                        display.set_pixel(blip,2,0)
                        blip+=1
                        display.set_pixel(blip,2,9)
                        timer=running_time()
                    else:
                        display.set_pixel(blip,2,0)
                        audio.play(audio.SoundEffect(freq_start=2000,freq_end=1000,duration=1000,shape=audio.SoundEffect.SHAPE_LINEAR))
                        return
                if blip==2:
                    audio.play(audio.SoundEffect(freq_start=659,freq_end=659,duration=30),wait=False)
                else:
                    audio.play(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=10),wait=False)
main()