import pygame 
import math
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000,700),0,32)
gun_img = pygame.image.load("gun.png")
gun_img_rect = gun_img.get_rect(center = (100,200))



running = True
while running:
    screen.fill((123,45,200))

    mx,my = pygame.mouse.get_pos()
    angle_radian = math.atan((-my+gun_img_rect.y)/(mx-gun_img_rect.x))
    angle_degrees = math.degrees(angle_radian)

    gun_rotate_img = pygame.transform.rotate(gun_img,angle_degrees)
    rotated_gun_rect = gun_rotate_img.get_rect(center = gun_img_rect.center)
    screen.blit(gun_rotate_img,(100,200))


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    pygame.display.update()



