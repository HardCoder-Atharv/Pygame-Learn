import pygame, sys 
 
clock = pygame.time.Clock()
 
from pygame.locals import * 
pygame.init() 
 
pygame.display.set_caption('Pygame Window') 

WINDOW_SIZE = (1400,800) 
transformation_size = 70
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) 
 
player_image = pygame.image.load('player.png').convert()
player_image.set_colorkey((255,255,255))


grass_image = pygame.image.load('grass.png')
dirt_image = pygame.image.load('dirt.png')
grass_modified = pygame.transform.scale(grass_image,(transformation_size,transformation_size))
dirt_modified = pygame.transform.scale(dirt_image,(transformation_size,transformation_size))



moving_up = False
moving_right = False
moving_left = False
player_transformed = pygame.transform.scale(player_image,(50,60))
player_location = [50,50]
player_y_momentum = 0
 
player_rect = pygame.Rect(50,50,player_transformed.get_width(),player_transformed.get_height())
test_rect = pygame.Rect(100,100,100,50)


#game map:
game_map = [
    
    ['','','','','','','','','1','1','1','1','1','1','','','','','','','','','','','',''],
    ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1'],
            
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

tile_size = 70
grass = []
dirt =[]



def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect,movement,tiles):
    collision_types = {'top':  False,'bottom' : False,'right' : False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0]>0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True

        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect,collision_types






def create_map(tiles,start,end):
    
    y = 0
    for row in game_map:
        x= 0 
        if y* tile_size <= end:

            if game_map[x][y] == '0':
                surf.blit(dirt_modified,(x*tile_size,start + y*tile_size))
                tiles.append(pygame.Rect(x* tile_size,start +y*tile_size,transformation_size,transformation_size))
            if game_map[x][y]== '1':
                surf.blit(grass_modified,(x*tile_size,y*tile_size+start,transformation_size,transformation_size))
                tiles.append(pygame.Rect())
            x+= 1
        y += 1




        


            



    pass


def create_map(tiles):
    

    
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            


            if tile == '0':
                surf.blit(dirt_modified,(x*tile_size,600+ y*tile_size))
                tiles.append(pygame.Rect(x*tile_size,600+y*tile_size,transformation_size,transformation_size))
            if tile == '1':
                surf.blit(grass_modified,(x*tile_size,400+y*tile_size))
                tiles.append(pygame.Rect(x*tile_size,400+y*tile_size,transformation_size,transformation_size))
            
            x += 1
        y += 1
    

flip_right = False
flip_left = False


acll = 0
while True: 
    
    surf = pygame.transform.scale(screen,(1400,800))
    surf.fill((146,244,255))
    surf.blit(player_transformed,(player_rect.x,player_rect.y))

    tiles = []
    create_map(tiles)
    
    
    
    



    player_movement = [0,0]




    
    
    player_y_momentum += 1.8
    player_movement[1] += player_y_momentum
    
    
    if moving_right == True:
        player_movement[0] += 5
    if moving_left == True:
        player_movement[0] -= 5
    if player_y_momentum > 55:
        player_y_momentum = 55
    
 


   

    player_rect,collisions= move(player_rect,player_movement,tiles)
    
    if collisions['bottom']:
        if moving_up == True:
            player_y_momentum = -35
        else:
            player_y_momentum = 0









    
  
    
    screen.blit(surf,(0,0))
    


    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == KEYDOWN:
            if event.key == K_RIGHT: 
                moving_right = True
                
                
            if event.key == K_LEFT:
                moving_left = True
                player_transformed = pygame.transform.flip(player_transformed,True,False)
            if event.key == K_UP:
                moving_up = True    
        if event.type == KEYUP:
            if event.key == K_UP:
                moving_up = False
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
 
    pygame.display.update() 
    clock.tick(100) 