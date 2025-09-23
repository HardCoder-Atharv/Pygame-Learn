import pygame 
import math
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000,700),0,32)
gun_img = pygame.image.load("gun.png")
gun_img_rect = gun_img.get_rect(center = (300,300))
gun_img.set_colorkey((255,255,255))
gun_img = pygame.transform.scale(gun_img,(100,100))


running = True
while running:
    screen.fill((123,45,200))

    mx,my = pygame.mouse.get_pos()
    if mx != gun_img_rect.x:
    
        angle_radian = math.atan((-my+gun_img_rect.y)/(mx-gun_img_rect.x))
    angle_degrees = math.degrees(angle_radian)

    gun_rotate_img = pygame.transform.rotate(gun_img,angle_degrees)
    screen.blit(gun_rotate_img,(300-gun_img.get_width()/2,300 ))


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    pygame.display.update()



