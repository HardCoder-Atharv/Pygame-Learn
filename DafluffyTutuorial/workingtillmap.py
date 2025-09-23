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
player_transformed = pygame.transform.scale(player_image,(30,60))
player_location = [50,50]
player_y_momentum = 0
 
scroll = [0,0] 




player_rect = pygame.Rect(50,50,player_transformed.get_width(),player_transformed.get_height())
test_rect = pygame.Rect(100,100,100,50)

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')

    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')

#game map:


tile_size = 70
grass = []
dirt =[]







# global animation_frames
# animation_frames = {}


# def load_animation(path,frame_durations):
#     global animation_frames
#     animation_name = path.split('/')[-1]
#     animation_frame_data =  []
#     n = 0
#     for frame in frame_durations:
#         animation_frame_id = animation_name + '_' + str(n)
#         img_loc = path + '/' + animation_frame_id +'.png'
#         animation_image = pygame.image.load(img_loc).convert()
#         animation_image.set_colorkey((255,255,255))
#         animation_frames[animation_frame_id] = animation_image.copy()
#         for i in range(frame):
#             animation_frame_data.append(animation_frame_id)
#         print(n)
#         n += 1
#     return animation_frame_data

# animation_database =  {}
# animation_database['run'] = load_animation('player_animations/run',[7,7])
# animation_database['idle'] = load_animation('player_animations/idle',[7,7,50])

# player_action = 'idle'
# player_flip = False
# player_frame = 0

# def change_action(action_variable,frame,new_variable):
#     if action_variable != new_variable:
#         frame = 0

#     return action_variable,frame


# print(animation_frames,animation_database)
# player_action = 'idle'















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
        for tile in row:
            if y* tile_size <= end:

                if tile == '2':
                    surf.blit(dirt_modified,(x*tile_size - scroll[0],start + y*tile_size- scroll[1]))
                    tiles.append(pygame.Rect(x* tile_size  ,start +y*tile_size,transformation_size,transformation_size))
                if tile== '1':
                    surf.blit(grass_modified,(x*tile_size-scroll[0],y*tile_size+start-scroll[1],transformation_size,transformation_size))
                    tiles.append(pygame.Rect(x* tile_size ,start +y*tile_size,transformation_size,transformation_size))
                x+= 1
        y += 1




        


            



    



    


flip_right = False
flip_left = False


acll = 0
while True: 
    
    surf = pygame.transform.scale(screen,(1400,800))
    surf.fill((146,244,255))
    

    tiles = []
    create_map(tiles,100,1000)
    
    
    
    
    



    player_movement = [0,0]



    scroll[0] += (player_rect.x - scroll[0]-552)/30
    scroll[1] += (player_rect.y - scroll[1]-350)/30
    
    
    player_y_momentum += 1.8
    player_movement[1] += player_y_momentum
    
    
    if moving_right == True:
        player_movement[0] += 7
    if moving_left == True:
        player_movement[0] -= 7
    if player_y_momentum > 55:
        player_y_momentum = 55
    
 
    # if player_movement[0] > 0:
    #     player_action,player_frame = change_action(player_action,player_frame,'run')
    #     player_flip = False
    # if player_movement[0] < 0:
    #     player_action,player_frame = change_action(player_action,player_frame,'run')
    #     player_flip = True


    # if player_movement[0] == 0:
    #     player_action,player_frame = change_action(player_action,player_frame,'idle')

    player_rect,collisions= move(player_rect,player_movement,tiles)
    
    if collisions['bottom']:
        if moving_up == True:
            player_y_momentum = -45
        else:
            player_y_momentum = 0



   



    
   
    

    
    
    surf.blit(pygame.transform.flip(player_transformed,False,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
    
    screen.blit(surf,(0,0))
    
    

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == KEYDOWN:
            if event.key == K_d: 
                moving_right = True
                
                
            if event.key == K_a:
                moving_left = True
                player_transformed = pygame.transform.flip(player_transformed,True,False)
            if event.key == K_w:
                moving_up = True    
        if event.type == KEYUP:
            if event.key == K_w:
                moving_up = False
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
                player_transformed = pygame.transform.flip(player_transformed,True,False)
 
    pygame.display.update() 
    clock.tick(60) 