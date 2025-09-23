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


grass_image = pygame.image.load('dirtimg1.png').convert()
grass_image.set_colorkey((255,255,255))
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




player_rect = pygame.Rect(200,50,player_transformed.get_width(),player_transformed.get_height())
test_rect = pygame.Rect(100,100,100,50)
    
import csv

with open("level0_data.csv", newline="") as f:
    reader = csv.reader(f)
    data_as_list = [[int(value) for value in row] for row in reader]

print(data_as_list)

def load_map(path):
    f = open(path + '.csv','r')
    data = f.read()
    f.close()
    data = data.split('\n')

    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map



#game map:


tile_size = 70
grass = []
dirt =[]





#Animation Stuff:
class Animation():
    
    def __init__(self,entity,path,name,img_number,frames,size,location):
        self.entity = entity
        self.path = path
        self.img_number = img_number
        self.name = name
        self.frames = frames
        self.size = size
        self.location = location
        
        self.imgs_loaded = [pygame.image.load(self.path+self.name+str(i)+".png").convert() for i in range(self.img_number)]
        self.transformed_images = []
        for i in range(len(self.imgs_loaded)):
            self.imgs_loaded[i].set_colorkey((255,255,255))
            self.transformed_images.append(pygame.transform.scale(self.imgs_loaded[i],self.size))
    
        self.idx = 0
        self.frame = 0


    def update(self):
        self.frame += 1
        if self.frame >= self.frames:
            self.idx = (self.idx+1)%len(self.transformed_images)
            self.frame = 0
    def get_image(self):
        image = self.transformed_images[self.idx]
        return image
    






player_run = Animation("player","player_animations/run/","run_",2,5,(player_transformed.get_width(),player_transformed.get_height()),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
player_idle = Animation("player","player_animations/idle/","idle_",3,6,(player_transformed.get_width(),player_transformed.get_height()),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
        
player_jump = Animation("player","player_animations/jump/","jump_",7,10,(player_transformed.get_width()+10,player_transformed.get_height()+5),(player_rect.x-scroll[0],player_rect.y-scroll[1]))






















def load_animation(path,name,img_number,frames,size,location):
    global start_frame,idx
    
    imgs_loaded = [pygame.image.load(path+name+str(i)+".png").convert() for i in range(img_number)]
    transformed_images = []
    for i in range(len(imgs_loaded)):
        imgs_loaded[i].set_colorkey((255,255,255))
        transformed_images.append(pygame.transform.scale(imgs_loaded[i],size))
    start_frame += 1
    if start_frame >= frames:
        idx = (idx +1)% len(transformed_images)
        start_frame = 0
    
    surf.blit(transformed_images[idx],location)

















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







img_list = []
for i in range(25):
    img = pygame.image.load(f"blocks/{i}.png").convert()
    img = pygame.transform.scale(img,(tile_size,tile_size))
    img.set_colorkey((255,255,255))
    img_list.append(img)





def draw_world():
    for y,row in enumerate(data_as_list):
        for x,tile in enumerate(row):
         
            if tile >= 0:
                
                surf.blit(img_list[tile],(x*tile_size-scroll[0],y*tile_size-scroll[1]))
                tiles.append(pygame.Rect(x* tile_size , y*tile_size,transformation_size,transformation_size))


        


            



    



    


flip_right = False
flip_left = False
jump = False

acll = 0
while True: 
    print(player_rect.x,player_rect.y)
    surf = pygame.transform.scale(screen,(1400,800))
    surf.fill((146,244,255))
    

    tiles = []
    draw_world()
    
    
    
    
    



    player_movement = [0,0]



    scroll[0] += (player_rect.x - scroll[0]-552)/30
    scroll[1] += (player_rect.y - scroll[1]-350)/30
    
    
    player_y_momentum += 1.8
    player_movement[1] += player_y_momentum
    
    
    
    
    if moving_right == True:
        player_movement[0] += 8
        
        
    if moving_left == True:
        player_movement[0] -= 8
        
    if player_y_momentum > 55:
        player_y_momentum = 55
    

    if moving_left or moving_right:
        current_anim = player_run

    else:
        current_anim = player_idle

    
    


        
    current_anim.update()
    surf.blit(current_anim.get_image(),
          (player_rect.x - scroll[0], player_rect.y - scroll[1])) 
   
    player_rect,collisions= move(player_rect,player_movement,tiles)
    
    if collisions['bottom']:
        if moving_up == True:
            player_y_momentum = -45
        else:
            player_y_momentum = 0

    



    
   
    

    
    
    
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