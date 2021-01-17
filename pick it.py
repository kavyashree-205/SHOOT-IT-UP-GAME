
import pygame
import sys
import random
import math
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Shoot It Up!!")
#load the background
back_ground=pygame.image.load("pick the right/background1.jpg")

#load the flying animals
bear=pygame.image.load("pick the right/bear.png")
bearx=270
beary=50
speed_bear=0.1

bird=pygame.image.load("pick the right/bird.png")
birdx=270
birdy=120
speed_bird=0.125

message=pygame.image.load("pick the right/message.png")
messagex=270
messagey=190
speed_message=0.15

list_animals=[bear,bird,message]
animal=random.choice(list_animals)
animalx=270
animaly=470
speed_animal=0

heart=pygame.image.load("pick the right/like.png")
heartx=0
hearty=470
speed_heart=0.35
heart_state="ready"
pygame.display.set_icon(heart)

win=3
loose=3
loosex=358
loosey=5
#function for loading bear
def f_bear(x,y):
    screen.blit(bear,(bearx,beary))

def f_bird(x,y):
    screen.blit(bird,(birdx,birdy))
    
def f_message(x,y):
    screen.blit(message,(messagex,messagey))

def f_animal(a,b):
    screen.blit(animal,(animalx,animaly))
    
def fire(x,y):
    global heart_state
    heart_state="fire"
    screen.blit(heart,(x+16,y+10))
def is_collision(animal):
    distance_b=math.sqrt(pow((bearx-heartx),2)+pow((beary-hearty),2))
    distance_bi=math.sqrt(pow((birdx-heartx),2)+pow((birdy-hearty),2))
    distance_m=math.sqrt(pow((messagex-heartx),2)+pow((messagey-hearty),2))
    if animal is bear:
        if distance_b<27:
            return True
        
        if distance_bi<27 or distance_m<27:
            return False
            
    elif animal is bird:
        if distance_bi<27:
            return True

        if distance_b<27 or distance_m<27:
            return False        

    elif animal is message:
        if distance_m<27:
            return True
      
        if distance_b<27 or distance_bi<27:
            return False
        
font=pygame.font.Font("freesansbold.ttf",40)
font1=pygame.font.Font("freesansbold.ttf",70)
def show_win():
    show=font1.render("You Won !!!",True,(0,0,0))
    show_rect=show.get_rect()
    show_rect.center=(300,300)
    screen.blit(show,show_rect)

def show_lost():
    lost=font1.render("Game Over !!!",True,(0,0,0))
    lost_rect=lost.get_rect()
    lost_rect.center=(300,300)
    screen.blit(lost,lost_rect)

def show_life(x,y):
    show1=font.render("Your life : "+str(loose),True,(0,0,0))
    screen.blit(show1,(x,y))

   
while True:
    screen.fill((137, 230, 255))
    screen.blit(back_ground,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed_animal=-0.15
            if event.key==pygame.K_RIGHT:
                speed_animal=0.15
            if event.key==pygame.K_SPACE:
                if heart_state=="ready":
                    heartx=animalx
                    fire(heartx,hearty)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                speed_animal=0
            
    animalx=animalx+speed_animal
    if animalx<=0:
        speed_animal=0
    elif animalx>=536:
        speed_animal=0
    
#moving of bear             
    bearx=bearx+speed_bear
    if bearx>=536:
        speed_bear=-0.1
    elif bearx<=0:
        speed_bear=0.1
#moving of bird
    birdx=birdx-speed_bird
    if birdx<=0:
        speed_bird=-0.125
    elif birdx>=536:
        speed_bird=0.125
#moving id message
    messagex=messagex+speed_message
    if messagex>=536:
        speed_message=-0.15
    elif messagex<=0:
        speed_message=0.15
#moving of heart
    if hearty<=0:
        hearty=470
        heart_state="ready"
    if heart_state=="fire":
        fire(heartx,hearty)
        hearty=hearty-speed_heart
        
    collision=is_collision(animal)
    if collision==True:
        heart_state="ready"
        hearty=470
        win=win-1
        if animal is bear:
            bearx=beary=1000
            animal=bird
            f_bear(bearx,beary)
            f_animal(animalx,animaly)
        elif animal is bird:
            birdx=birdy=1000
            animal=message
            f_bear(birdx,birdy)
            f_animal(animalx,animaly)
        elif animal is message:
            messagex=messagey=1000
            animal=bear
            f_bear(messagex,messagey)
            f_animal(animalx,animaly)
          
    if collision==False:
        heart_state="ready"
        hearty=470
        loose=loose-1
        if loose==0:
            bearx=beary=messagex=messagey=birdx=birdy=1000
            f_bear(bearx,beary)
            f_bird(birdx,birdy)
            f_message(messagex,messagey)
 
    #calling bear function to load in screen continuesly
    f_bear(bearx,beary)
    f_bird(birdx,birdy)
    f_message(messagex,messagey)
    f_animal(animalx,animaly)
    show_life(loosex,loosey)
    if win==0:
        show_win()
    if loose==0:
        show_lost()
    pygame.display.update()
    
    