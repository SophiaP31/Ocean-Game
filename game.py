#Sophia Padilla #Sap8ht

#Overview: we will make an underwater/ocean themed game where the user plays a fish/turtle/mermaid and has to
#collect shells, and avoid being eaten by sharks

#Required Features:
# User Input: user will move around using up,down keys
# Graphics: We will put an ocean-like background image, we will also use images for the players(fish) and shells and rocks,etc.
# Start screen: we will make a start screen with instructions

#Optional Features: (choose 4)
#collectables: the user will collect shells which will increase the score
#enemies: every once in a while a shark will appear and try to eat the user
#health bar: if the shark or rocks touches the user, the health bar will go down, game ends when health is at zero
#scrolling level: the screen will scroll from right to left making it appear as if the user is swimming
#sounds: there will be sounds for when the user collects coins, and bad sound when it touches something/loses health

#timeline
#checkpoint 1 get a rough outline
#checkpoint 2 get it all working
#final make it pretty



import pygame
import gamebox, sys
import random
import urllib, os.path
#
# if 'urlretrieve' not in dir(urllib):
#     from urllib.request import urlretrieve as _urlretrieve
# else:
#     _urlretrieve = urllib.urlretrieve
# pygame.init()


camera = gamebox.Camera(1024, 576)
score= 0
scoreboard=gamebox.from_text(750,10,"SCORE:  "+str(score) ,"Arial", 20,"white")
fish = gamebox.from_image(350, 300, 'f3.png')
fish.scale_by(0.1)
underline = gamebox.from_color(350,350,"black",100,20)
evan = gamebox.from_image(500,300,'Esub (2).png')
evan.scale_by(0.3)
lineE = gamebox.from_color(500,400,"black", 100, 20)
zayn = gamebox.from_image(650,300,'Zzsub.png')
zayn.scale_by(0.3)
lineZ = gamebox.from_color(650,400,"black", 100, 20)
dimitri = gamebox.from_image(800,300,'ddsub.png')
dimitri.scale_by(0.4)
lineD = gamebox.from_color(800,400,"black", 100,20)


r1= gamebox.from_image(100, 600, 'r1.png')
        # gamebox.from_color(250, 600, 'black', 50, 100),
        # gamebox.from_color(400, 600, 'black', 70, 30),
r2= gamebox.from_image(600, 600, 'r2.png')


r1.scale_by(0.5)
r2.scale_by(0.25)
rocks= [r1,r2]

shark =gamebox.from_image(1500,camera.y,"s1.png")
shark.scale_by(0.07)

#shark = gamebox.from_color(800,camera.y,"grey",50,50)

floor=gamebox.from_color(0,600,"black",1600,20)
#box.wait_before_flap = 0
ticks= 0
show_splash=True
health = [
    gamebox.from_color(0,0,"red",50,50),
    gamebox.from_color(50,0,"red",50,50),
    gamebox.from_color(100,0,"red",50,50)
    ]
healthbar= gamebox.from_text(25,50,"Health", "Arial", 20, "red")
shells = []
for i in range(30):
    shells.append(gamebox.from_image(
        random.randrange(camera.left, camera.right),
        random.randrange(camera.y, camera.bottom),
        "shell.png"
    ))
for shell in shells:
    shell.scale_by(0.07)
    for x in shells:
        if shell.touches(x):
            shell.move_to_stop_overlapping(x)
    for rock in rocks:
        if shell.touches(rock):
            shell.move_to_stop_overlapping(rock)


bc1 = gamebox.from_image(camera.x, camera.y,"bc1 (1).png")
bc2 = gamebox.from_image(camera.x + 1024, camera.y,"bc2 (1).png")



# #SOUND EFFECTS
bad = gamebox.load_sound("popsound.wav")
bubbles = gamebox.load_sound("badnoise.wav")

youlose = gamebox.from_text(camera.x,camera.y,"Oh No! You lose!","Arial",50,"white")


x=0 #grace period
#start screen with instructions
def splash(keys):
    global show_splash, ticks, box

    camera.draw(bc1)
    camera.draw(bc2)
    bc1.x -= 10
    bc2.x -= 10
    if bc1.right < camera.left:
        # rock.y -= 600
        bc1.x += 2048
    if bc2.right < camera.left:
        # rock.y -= 600
        bc2.x += 2048
    for rock in rocks:
        camera.draw(rock)
        rock.x -=10
        if rock.right < camera.left:
            rock.x +=1400


    directions = gamebox.from_text(camera.x, camera.y+100, "Press space to start", "Arial", 20, 'black')
    more_directions= gamebox.from_text(camera.x,camera.y-100," Try to collect as many shells as possible. Avoid the sharks! Don't swim off the screen!""", "Arial", 20,"black")
    names=gamebox.from_text(camera.x, camera.y-200, "Type the first letter of your name to choose your player", "Arial",20,"black")
    GAMENAME=gamebox.from_text(camera.x,camera.y+200, "UNDERWATER ADVENTURES","Arial",60,"black")

    camera.draw(more_directions)
    camera.draw(directions)
    camera.draw(fish)
    camera.draw(underline)
    camera.draw(evan)
    camera.draw(dimitri)
    camera.draw(zayn)
    camera.draw(names)
    camera.draw(GAMENAME)
    camera.draw(healthbar)

    if pygame.K_f in keys:
        underline.x = 350
        underline.y = 350
        box = fish
    if pygame.K_e in keys:
        underline.x  = 500
        underline.y = 375
        box = evan
    if pygame.K_z in keys:
        underline.x  = 650
        underline.y = 375
        box = zayn
    if pygame.K_d in keys:
        underline.x  = 800
        underline.y = 375
        box = dimitri

    camera.draw(underline)
    if pygame.K_SPACE in keys:
        show_splash = False


    camera.display()


def tick(keys):


    if show_splash:
        splash(keys)
        return
    else:
        camera.draw(bc1)
        camera.draw(bc2)
        bc1.x -= 10
        bc2.x -= 10
        if bc1.right < camera.left:
            # rock.y -= 600
            bc1.x += 2048
        if bc2.right < camera.left:
            # rock.y -= 600
            bc2.x += 2048

        global ticks
        global score
        global scoreboard
        ticks += 1
        global x
        x += 1


        for i in health:
            camera.draw(i)

        #camera.draw(oceanfloor)
        # if box.touches(camera.bottom):
        #     box.y -=5
        # if box.touches(camera.top):
        #     box.y +=5
        #if box.right < camera.left:
            #box.x +=5
        # if box.x < 1000:
        #     box.x +=5


        # time = gamebox.from_text(0, 0, str(ticks // 30), "Arial", 20, "red")
        # time.top = camera.top
        # time.right = camera.right
        # camera.draw(time)



    #SHARK

        shark.x -= 3
        if shark.y > box.y:
            shark.y -= 3
        if shark.y < box.y:
            shark.y += 3
        shark.speedx *= 0.95
        shark.speedy *= 0.95

        if shark.right < camera.left:
            shark.x = 2000

        if shark.touches(box,-30,-30) and x>60:
            health.pop()
            x=0
            bad.play()


        shark.move_speed()
        camera.draw(shark)



    #SHELLS

        for shell in shells:
            camera.draw(shell)

        for shell in shells:
            if box.touches(shell):
                shell.x +=1500
                shell.y = random.randrange(camera.y,camera.bottom)
                score += 1
                scoreboard = gamebox.from_text(750, 10, "SCORE:  " + str(score), "Arial", 20, "white")
                bubbles.play()
                #shells.append(gamebox.from_color(800,random.randrange(camera.y,camera.bottom),"yellow",20,20))

        for shell in shells:
            camera.draw(shell)
            shell.x -= 10
            if shell.right < camera.left:
                # rock.y -= 600
                shell.x += 1500
                shell.y = random.randrange(camera.top, camera.bottom)
        for shell in shells:
            for rock in rocks:
                if shell.touches(rock):
                    shell.move_to_stop_overlapping(rock)

    #ROCKS
        for rock in rocks:
            camera.draw(rock)
            rock.x -= 10
            if rock.right < camera.left:
                # rock.y -= 600
                rock.x += 1600
                #rock.scale_by(0.1,0.25)

        #
        # if (box.touches(r1,-50,-50) or box.touches(r2,-50,-50)) and x>60:
        #     health.pop()
        #     x=0
        #
        # if box.touches(r1,-50,-50):
        #     bad.play()
        #
        #
        # if box.touches(r2,-50,-50):
        #     bad.play()


#FISH

        #box.x -= 10
        if pygame.K_RIGHT in keys:
            box.x += 15
        if pygame.K_LEFT in keys:
            box.x -= 15
        if pygame.K_UP in keys:
            box.y -= 10
        if pygame.K_DOWN in keys:
            box.y += 10
        # if box.x==0:
        #     camera.draw(youlose)
        #     gamebox.pause()


        if box.right < camera.left:
            camera.draw(youlose)
            gamebox.pause()
        if box.left > camera.right:
            camera.draw(youlose)
            gamebox.pause()
        if box.bottom < camera.top:
            camera.draw(youlose)
            gamebox.pause()
        if box.top > camera.bottom:
            camera.draw(youlose)
            gamebox.pause()

        box.move_speed()
        camera.draw(box)

        camera.draw(healthbar)
        camera.draw(scoreboard)

        if health == []:
            camera.draw(youlose)
            gamebox.pause()



        # usually camera.display() should be the last line of the tick method
        camera.display()

# keep this line the last one in your program
gamebox.timer_loop(30, tick)


#fix shark so that it doesnt bounce up and down at the end
#coins
#doesn't end when fish goes off screen

