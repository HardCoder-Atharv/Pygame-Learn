import pygame
import sys
from pygame.locals import *
pygame.init()
WINDOW_SIZE = (1400,800)
screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()
player = pygame.image.load("player.png")

moving_right = False
moving_left = False
player_location= [50,50]


velocity_y = 0
test_rect = pygame.Rect(100,100,50,50)
scaled_image = pygame.transform.scale(player,(50,60))

acceleration_t = 130  
boost_up = False
boost_down = False 

    
transformation_size = 70
grass_image = pygame.image.load('grass.png')
dirt_image = pygame.image.load('dirt.png')
grass_modified = pygame.transform.scale(grass_image,(transformation_size,transformation_size))
dirt_modified = pygame.transform.scale(dirt_image,(transformation_size,transformation_size))

 
    


               

               


        



game_map = [['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

tile_size = 70
grass = []
dirt =[]





def create_map():
    

    
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            
            if tile == '0':
                print('done')
                screen.blit(dirt_modified,(x*tile_size,500+  y*tile_size))
                dirt.append(pygame.Rect(x*tile_size,500+y*tile_size,transformation_size,transformation_size))
            if tile == '1':
                screen.blit(grass_modified,(x*tile_size,400+y*tile_size))
                grass.append(pygame.Rect(x*tile_size,400 +y*tile_size,transformation_size,transformation_size))
            
            x += 1
        y += 1

 






       
          
               


while True:
   
    screen.fill((123,234,233))







    screen.blit(scaled_image,player_location)
    create_map()
    tiles = grass + dirt

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    
    if boost_up == True:
        print('upboost')
        acceleration_t += 1

    if boost_down == True:
        acceleration_t -= 1 
        print('boost_down')   
         
         
    
    velocity_y += acceleration_t * 0.01
    
    if velocity_y > 0 :
        player_location[1] += velocity_y *0.2
    if velocity_y < 0:
        player_location[1]+= velocity_y * 1   
    if player_location[1] >= screen.get_height()-scaled_image.get_height():
        velocity_y = -30
        print("hi")
        
    player_rect = pygame.Rect(player_location[0],player_location[1],scaled_image.get_width(),scaled_image.get_height())

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen,(0,0,128),test_rect)
    else:
        pygame.draw.rect(screen,(0,0,0),test_rect)

    
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
           
        
            
        if event.type == KEYDOWN:
            
    
            if event.key == K_w:
                print("up")
                boost_up = True

            if event.key == K_s:
                boost_down = True
                print("down")
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT: 
                moving_left = True
                
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
                
   
    pygame.display.update()
    clock.tick(60)