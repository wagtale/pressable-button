import pygame
from pygame.locals import *
import bt
import playsound
from playsound import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("button")

#load images
button_up_img = pygame.image.load('img/button_up.png').convert_alpha()
button_down_img = pygame.image.load('img/button_down.png').convert_alpha()

#add button to space
button_up = bt.Button(0,0,button_up_img)
button_down = bt.Button(0,0,button_down_img)



run = True
while run:

    clock.tick(fps)


    screen.fill((255,255,255))

    if pygame.mouse.get_pressed()[0] == 1:
            button_down.draw(screen)
       
    else:
            button_up.draw(screen)

    if pygame.mouse.get_pressed()[0] == 1:
            pygame.mixer.music.load("assets/sfx_hit.wav")
            pygame.mixer.music.play()
    

    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
                        run = False
    pygame.display.update()                    
pygame.quit()