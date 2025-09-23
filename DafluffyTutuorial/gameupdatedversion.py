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

acceleration_t = 100  
boost_up = False
boost_down = False 

 
transformation_size = 50
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

tile_size = 60
grass = []
dirt =[]





def create_map():
    

    
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            
            if tile == '0':
                
                screen.blit(dirt_modified,(x*tile_size,500+  y*tile_size))
                dirt.append(pygame.Rect(x*tile_size,500+y*tile_size,transformation_size,transformation_size))
            if tile == '1':
                screen.blit(grass_modified,(x*tile_size,400+y*tile_size))
                grass.append(pygame.Rect(x*tile_size,400 +y*tile_size,transformation_size,transformation_size))
            
            x += 1
        y += 1








def is_collide(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            
            hit_list.append(tile)
    print(hit_list)
    return hit_list



def update_move(rect,movement,tiles):
    rect.x += movement[0]
    collisions = is_collide(rect,tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
            print('col')
        if movement[0] < 0:
            rect.left  = tile.right
            print('coll')

    rect.y += movement[1]
    collisions = is_collide(rect,tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top - 20
            
            print('collide')
       

    return rect















       
          
               
dummy_player = pygame.Rect(0,0,scaled_image.get_width()-5,scaled_image.get_height()-20)

while True:
    movement = [0,0]
   
    screen.fill((123,234,233))
    
    


 
    



    movement[1]+=2
    print(dummy_player.x,dummy_player.y)
    pygame.draw.rect(screen,(123,56,79),dummy_player)
    
    create_map()
    tiles = grass + dirt
    if moving_right == True:
        
        movement[0]+= 2
    if moving_left == True:
        
        movement[0] -= 2
    
    
    dummy_player = update_move(dummy_player,movement,tiles)
    screen.blit(scaled_image,(dummy_player.x,dummy_player.y))
    
         
    
    velocity_y += acceleration_t * 0.01
    
    if velocity_y > 0 :
        dummy_player.y += velocity_y *0.2
    if velocity_y < 0:
        dummy_player.y += velocity_y * 1   
    if dummy_player.y >= screen.get_height()-scaled_image.get_height():
        velocity_y = -30
        print("hi")
        
    
    
    
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