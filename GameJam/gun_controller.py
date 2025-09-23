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
    angle_degrees = 0
    mx,my = pygame.mouse.get_pos()
    if mx - gun_img_rect.x > 0:
    
        angle_radian = math.atan((-my+gun_img_rect.y)/(mx-gun_img_rect.x))
    if mx - gun_img_rect.x < 0:
    
        angle_radian = 3.14- math.atan((+my-gun_img_rect.y)/(mx-gun_img_rect.x)) 
        
    angle_degrees = math.degrees(angle_radian)
    pygame.draw.line(screen,(123,123,234),(0,gun_img_rect.y),(700,gun_img_rect.y))
    pygame.draw.line(screen,(123,123,234),(gun_img_rect.x,0),(gun_img_rect.x,700))
    gun_rotate_img = pygame.transform.rotate(gun_img,angle_degrees)
    screen.blit(gun_rotate_img,(gun_img_rect.x-(gun_img.get_width())/2,gun_img_rect.y -(gun_img.get_height())/2))


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    pygame.display.update()



