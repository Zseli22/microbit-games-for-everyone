from microbit import *
import random,music,os

controller = False
if pin15.read_digital() == 1:
    controller = True

if controller == False:
    music_pin = None
else:
    music_pin = pin2

# Controller up follows the board's down gesture because both move y upward
# on the display's coordinate system in this game.
ball={'x':2, 'y':2}
main_timer=0
score=0
lives=3
health=100
speed=1800
original_speed=0
coord_tones=[523,587,659,699,784]
all_coords=[]
spaces=[]
for i in range(5):
    for j in range(5):
        all_coords.append({'x':j,'y':i})
blocks=[]
state='waiting'
multiply=0
speed_active=False
speed_countdown=0
teleport=0
extra_life_tones=[1319,1568,2637,2093,2349,3136]
point_multiplier_tones=[262,330,392,523,392,523,659,784,1047,784,415,523,622,831,622,831,1047,1245,1661,1245,466,587,698,932,698,932,1175,1397,1865,1397]
health_increase_tones=[698,880,1047,1397,784,988,1175,1568,880,1109,1319,1760]
def move():
    global ball
    if accelerometer.is_gesture('down') or (controller and pin8.read_digital() == 0):
        choices=[0,0,0,2,3]
    elif accelerometer.is_gesture('up') or (controller and pin14.read_digital() == 0):
        choices=[1,1,1,2,3]
    elif accelerometer.is_gesture('left') or (controller and pin12.read_digital() == 0):
        choices=[0,1,2,2,2]
    elif accelerometer.is_gesture('right') or (controller and pin13.read_digital() == 0):
        choices=[0,1,3,3,3]
    else:
        choices=[0,1,2,3]
    direction=random.choice(choices)
    if direction==0:
        ball['y']-=1
    elif direction==1:
        ball['y']+=1
    elif direction==2:
        ball['x']-=1
    elif direction==3:
        ball['x']+=1
    if ball['x'] not in range(5) or ball['y'] not in range(5):
        if ball['x'] not in range(5) and ball['y'] not in range(5):
            display.show(Image.SNAKE)
            audio.play(audio.SoundEffect(freq_start=random.randint(250,500),freq_end=random.randint(1000,3000),duration=1000,waveform=audio.SoundEffect.WAVEFORM_NOISE,shape=audio.SoundEffect.SHAPE_LINEAR,vol_start=0,vol_end=255), pin=music_pin)
            ball['x']=2
            ball['y']=2
        else:
            falling()

def falling():
    global ball,main_timer,health,speed,state
    warning=-1
    health_timer=0
    loops=0
    properties=[(Image('99999:00000:00000:00000:00000'),1800,'up'),(Image('00000:00000:00000:00000:99999'),1200,'down'),(Image('90000:90000:90000:90000:90000'),1400,'right'),(Image('00009:00009:00009:00009:00009'),1600,'left')]
    if ball['y']==-1:
        warning=0
    elif ball['y']==5:
        warning=1
    elif ball['x']==-1:
        warning=2
    elif ball['x']==5:
        warning=3
    health_timer=running_time()
    main_timer=running_time()
    while health>0:
        if running_time()-health_timer>=speed//scale(health,from_=(0,300),to=(15,5)):
            if loops%2==0:
                display.show(properties[warning][0])
                music.pitch(properties[warning][1],duration=-1,wait=True,pin=music_pin)
            else:
                display.clear()
                music.stop()
            loops+=1
            if running_time()-main_timer>=speed//3:
                health-=2
                main_timer=running_time()
            health_timer=running_time()
        if accelerometer.is_gesture(properties[warning][2]):
            music.stop()
            move()
            return
        if controller and ((properties[warning][2] == 'up' and pin14.read_digital() == 0) or
                           (properties[warning][2] == 'down' and pin8.read_digital() == 0) or
                           (properties[warning][2] == 'left' and pin12.read_digital() == 0) or
                           (properties[warning][2] == 'right' and pin13.read_digital() == 0)):
            music.stop()
            move()
            return
    if health<=0:
        state='gameover'
def spawn_block():
    global ball,blocks,all_coords,spaces,coord_tones,speed
    spaces=all_coords[:]
    if len(blocks)>0:
        for i in range(len(blocks)):
            spaces.remove(blocks[i])
    spaces.remove(ball)
    blocks.append(random.choice(spaces))
    display.set_pixel(blocks[-1]['x'],blocks[-1]['y'],6)
    music.pitch((coord_tones[blocks[-1]['x']])*2,duration=speed//16,wait=True,pin=music_pin)
    sleep(50)
    music.pitch((coord_tones[blocks[-1]['y']])*2,duration=speed//16,wait=True,pin=music_pin)
    sleep(300)

def count(sifer=0):
    if sifer==0:
        audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=250), pin=music_pin)
    while sifer>=100:
        audio.play(audio.SoundEffect(freq_start=1175,freq_end=1175,duration=320), pin=music_pin)
        sifer-=100
        sleep(160)
    while sifer>=10 and sifer<100:
        audio.play(audio.SoundEffect(freq_start=784,freq_end=784,duration=220), pin=music_pin)
        sifer-=10
        sleep(160)
    while sifer>=1 and sifer<10:
        audio.play(audio.SoundEffect(freq_start=523,freq_end=523,duration=90), pin=music_pin)
        sifer-=1
        sleep(160)

def make_powerup():
    global lives,multiply,health,speed_active,speed_countdown,original_speed,teleport,ball,speed,extra_life_tones,point_multiplier_tones,health_increase_tones
    if speed_active==True:
        powerup=random.randint(0,2)
    else:
        powerup=random.randint(0,4)
    if powerup==0:
        display.show(Image.XMAS)
        for i in range(len(health_increase_tones)):
            audio.play(audio.SoundEffect(freq_start=health_increase_tones[i],freq_end=health_increase_tones[i],duration=50), pin=music_pin)
        health+=30
        sleep(300)
    elif powerup==1:
        display.show('X')
        for i in range(len(point_multiplier_tones)):
            audio.play(audio.SoundEffect(freq_start=point_multiplier_tones[i],freq_end=point_multiplier_tones[i],duration=30), pin=music_pin)
        multiply+=25
        sleep(300)
    elif powerup==2:
        display.show(Image.SQUARE)
        audio.play(audio.SoundEffect(freq_start=random.randint(250,500),freq_end=random.randint(1000,3000),duration=400,waveform=audio.SoundEffect.WAVEFORM_NOISE,shape=audio.SoundEffect.SHAPE_LINEAR,vol_start=0,vol_end=255), pin=music_pin)
        teleport+=1
        sleep(300)
    elif powerup==3:
        original_speed=speed
        display.show(Image.ARROW_S)
        audio.play(audio.SoundEffect(freq_start=700,freq_end=50,duration=700,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR,fx=audio.SoundEffect.FX_VIBRATO), pin=music_pin)
        speed+=random.randint(int(speed*0.2),int(speed*0.4))
        speed_active=True
        speed_countdown=25
    elif powerup==4:
        original_speed=speed
        display.show(Image.ARROW_N)
        audio.play(audio.SoundEffect(freq_start=100,freq_end=1000,duration=700,shape=audio.SoundEffect.SHAPE_LINEAR,vol_end=200,fx=audio.SoundEffect.FX_WARBLE), pin=music_pin)
        speed-=random.randint(int(speed*0.2),int(speed*0.4))
        speed_active=True
        speed_countdown=-25

def process():
    global ball,blocks,score,multiply,lives,extra_life_tones
    echo=0
    music.stop()
    for i in range(len(blocks)):
            if ball==blocks[i]:
                display.clear()
                if multiply>0:
                    score+=2
                else:
                    score+=1
                echo=255
                while echo>0:
                    blip=random.randint(1200,4000)
                    display.set_pixel(random.randint(0,4),random.randint(0,4),random.randint(1,9))
                    audio.play(audio.SoundEffect(freq_start=blip,freq_end=blip,duration=30,vol_start=echo), pin=music_pin)
                    echo-=random.randint(20,40)
                blocks.remove(ball)
                if score>0 and (score%100==0) or (multiply>0 and score%100==1):
                    display.show(Image.FABULOUS)
                    for i in range(len(extra_life_tones)):
                        audio.play(audio.SoundEffect(freq_start=extra_life_tones[i],freq_end=extra_life_tones[i],duration=120), pin=music_pin)
                    lives+=1
                powerup=random.randint(0,speed//100)
                if powerup==0:
                    make_powerup()
                spawn_block()

def main():
    global ball,main_timer,score,lives,health,speed,blocks,coord_tones,state,multiply,speed_active,speed_countdown,original_speed,teleport
    while True:
        if state=='waiting':
            display.show(lives)
            if button_a.is_pressed() or (controller and pin15.read_digital() == 0):
                display.clear()
                for i in range(4):
                    spawn_block()
                audio.play(audio.SoundEffect(freq_start=2093,freq_end=2093,duration=200), pin=music_pin)
                main_timer=running_time()
                state='playing'
        elif state=='playing':
            if button_a.is_pressed() or (controller and pin15.read_digital() == 0):
                for i in range(len(blocks)):
                    music.pitch((coord_tones[blocks[i]['x']])*2,duration=speed//16,wait=True,pin=music_pin)
                    sleep(50)
                    music.pitch((coord_tones[blocks[i]['y']])*2,duration=speed//16,wait=True,pin=music_pin)
                    sleep(300)
                if button_a.is_pressed() or (controller and pin15.read_digital() == 0):
                    display.scroll(health,delay=50)
                    count(health)
                    sleep(500)
                    display.show(teleport)
                    count(teleport)
                    sleep(500)
                    if multiply>0:
                        display.show('X')
                        for i in range(len(point_multiplier_tones)):
                            audio.play(audio.SoundEffect(freq_start=point_multiplier_tones[i],freq_end=point_multiplier_tones[i],duration=30), pin=music_pin)
                        sleep(200)
                        display.scroll(multiply,delay=50)
                        count(multiply)
                    if speed_active==True:
                        if speed_countdown>0:
                            display.show(Image.ARROW_S)
                            audio.play(audio.SoundEffect(freq_start=700,freq_end=50,duration=700,vol_end=255,shape=audio.SoundEffect.SHAPE_LINEAR,fx=audio.SoundEffect.FX_VIBRATO), pin=music_pin)
                        elif speed_countdown<0:
                            display.show(Image.ARROW_N)
                            audio.play(audio.SoundEffect(freq_start=100,freq_end=1000,duration=700,shape=audio.SoundEffect.SHAPE_LINEAR,vol_end=200,fx=audio.SoundEffect.FX_WARBLE), pin=music_pin)
                        sleep(200)
                        display.scroll(abs(speed_countdown),delay=50)
                        count(abs(speed_countdown))
                    display.clear()
                    sleep(200)
                main_timer=running_time()
            if (button_b.is_pressed() or (controller and pin16.read_digital() == 0)) and teleport>0:
                display.show(Image.TRIANGLE_LEFT)
                audio.play(audio.SoundEffect(freq_start=random.randint(200,500),freq_end=random.randint(1000,3000),duration=400,shape=audio.SoundEffect.SHAPE_LINEAR,waveform=audio.SoundEffect.WAVEFORM_NOISE), pin=music_pin)
                destroy=random.choice(blocks)
                ball['x']=destroy['x']
                ball['y']=destroy['y']
                process()
                teleport-=1
            if running_time()-main_timer>=speed:
                move()
                process()
                if ball['x'] in range(5) and ball['y'] in range(5):
                    display.clear()
                    display.set_pixel(ball['x'],ball['y'],9)
                    for i in range(len(blocks)):
                        display.set_pixel(blocks[i]['x'],blocks[i]['y'],6)
                    music.pitch(coord_tones[ball['x']],duration=speed//16,wait=True,pin=music_pin)
                    sleep(50)
                    music.pitch(coord_tones[ball['y']],duration=speed//16,wait=True,pin=music_pin)
                if speed_active==False:
                    if speed>500:
                        speed-=random.randint(int(speed*0.0075),int(speed*0.015))
                    else:
                        speed+=random.choice([-2,0,1])
                if multiply>0:
                    multiply-=1
                    if multiply==0:
                        audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=300), pin=music_pin)
                if speed_active==True:
                    if speed_countdown>0:
                        speed_countdown-=1
                    elif speed_countdown<0:
                        speed_countdown+=1
                    elif speed_countdown==0:
                        audio.play(audio.SoundEffect(freq_start=131,freq_end=131,duration=300), pin=music_pin)
                        speed_active=False
                        speed=original_speed
                main_timer=running_time()
        elif state=='gameover':
            display.show(Image.NO)
            music.pitch(125,duration=500,pin=music_pin)
            display.clear()
            sleep(1200)
            ball={'x':2,'y':2}
            blocks=[]
            multiply=0
            health=100
            teleport=0
            speed_active=False
            speed_countdown=0
            lives-=1
            if speed<=450:
                speed=450
            display.scroll(score,delay=50)
            count(score)
            sleep(500)
            count(lives)
            if lives>0:
                if 'save.txt' in os.listdir():
                    os.remove('save.txt')
                with open('save.txt','w') as save:
                    save.write(str((score,lives,speed)))
                    save.close()
            else:
                if 'save.txt' in os.listdir():
                    os.remove('save.txt')
                reset()
            state='waiting'
if 'save.txt' in os.listdir():
    with open('save.txt','r') as save:
        datastr=save.read()
        save.close()
    score,lives,speed=eval(datastr)
    display.scroll(score,delay=50)
    count(score)
    sleep(500)
    count(lives)
main()
