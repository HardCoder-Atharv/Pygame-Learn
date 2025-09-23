import pygame 
from pygame.locals import *
pygame.init()
import random


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,700),0,32)
running = True
particles = []

while running:
    screen.fill((123,34,233))
    mx,my = pygame.mouse.get_pos()
    particles.append([[mx,my],[random.randint(0,50)//10-1,random.randint(-2,2)],random.randint(5,20)])
    
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.3
        pygame.draw.circle(screen,(255,255,255),particle[0],8,int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    for event in pygame.event.get():
        if event.type ==QUIT:
            running = False
            pygame.quit()

    pygame.display.update()

    clock.tick(60)



