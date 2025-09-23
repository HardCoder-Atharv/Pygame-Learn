import pygame 
from particles_syss import Particle_System
from particles_syss import *

from pygame.locals import *
pygame.init()
import random



clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,700),0,32)
running = True
ps = Particle_System(
        surface = screen,
        pos_getter = pygame.mouse.get_pos,
        color = (random.randint(20,100),random.randint(100,150),random.randint(100,200)),
        radius_range = (5,20),
        vel_range_x = (-1, 4),
        vel_range_y = (-2, 2),
        decay = 0.3
    )
while running:
    screen.fill((123,34,233))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    ps.emit()
    ps.update_and_draw()
    pygame.display.update()
    clock.tick(100)

pygame.quit()
