import pygame 
import button
import csv
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SIDE_MARGIN = 300
Max_rows = 100
Max_columns = 300
Tile_size = 40
Red = (255,0,0)
Green  = (0,255,0)
current_tile = 0
level = 1





















font = pygame.font.SysFont('Futura', 30)
screen = pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN,SCREEN_HEIGHT),0,32)




#load buttons
img_list = []
for i in range(26):
    if i == 25:
        img = pygame.image.load(f"blocks/{i}.png").convert()
        img = pygame.transform.scale(img,(Tile_size*2.5,Tile_size*4))
        img.set_colorkey((0,0,0))
        img_list.append(img)
    else:
        img = pygame.image.load(f"blocks/{i}.png").convert()

        img = pygame.transform.scale(img,(Tile_size,Tile_size))
        img.set_colorkey((255,255,255))
        img_list.append(img)





def show_buttons():
    button_list = []
    button_row = 0
    button_column = 0
    for i in range(len(img_list)):
        img_button = button.Button(SCREEN_WIDTH+button_column*(40+Tile_size)  + 10,button_row*(60+Tile_size)+ 50,img_list[i],1.3)
        button_list.append(img_button)
        button_column += 1
        if button_column == 4:
            button_row += 1
            button_column = 0

    return button_list 



save_img = pygame.image.load('save_btn.png').convert_alpha()
load_img = pygame.image.load('load_btn.png').convert_alpha()


save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + - 50, save_img, 1)
load_button = button.Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + - 50, load_img, 1)










#background
back_img = pygame.image.load("bg.png")


def background():
    for i in range(4):
        for j in range(4):
            screen.blit(back_img,(i*back_img.get_width()-scroll[0],j*back_img.get_height()-scroll[1]))

def draw_grid():  
    for i in range(Max_rows+1):
        pygame.draw.line(screen,Red,(0,i*Tile_size-scroll[1]),(SCREEN_WIDTH,i*Tile_size-scroll[1]))
    for i in range(Max_columns+1):
        pygame.draw.line(screen,Red,(i*Tile_size-scroll[0],0),(i*Tile_size-scroll[0],SCREEN_HEIGHT))

world_data = []
for i in range(Max_rows):
    
    row = [-1]*Max_columns
    world_data.append(row) 


def draw_world():
    for y,row in enumerate(world_data):
        for x,tile in enumerate(row):
            
            if tile == 25:
                print("yes")
                screen.blit(img_list[tile],(x*(Tile_size)-scroll[0],y*(Tile_size)-scroll[1]))
            if tile >= 0:
                screen.blit(img_list[tile],(x*Tile_size-scroll[0],y*Tile_size-scroll[1]))

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))





scroll =[0,0]
scroll_right = False
scroll_left = False
scroll_up = False
scroll_down = False
running = True

while running:
    screen.fill((100,23,90))
    background()
    draw_grid()
    draw_world()
    
    draw_text(f'Level: {level}', font, (255,255,255), 10, SCREEN_HEIGHT +  - 90)

	
    button_list = show_buttons()
    pygame.draw.rect(screen,Red,(SCREEN_WIDTH,0,SIDE_MARGIN,SCREEN_HEIGHT))
    draw_text('Press UP or DOWN to change level', font,  (255,255,255), 10, SCREEN_HEIGHT +  - 60)


    button_number = 0
    for button_number,i in enumerate(button_list):
        if i.draw(screen) == True:
            current_tile = button_number
            
    







    if scroll_left == True:
        scroll[0] -= 20

    if scroll_right == True:
        scroll[0] += 20
    if scroll_up == True:
        scroll[1] -= 20
    if scroll_down == True:
        scroll[1] += 20

    if save_button.draw(screen):
        with open(f'level{level}_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            for row in world_data:
                writer.writerow(row)
    
    if load_button.draw(screen):
        scroll[0],scroll[1] = 0,0
        with open(f'level{level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)
	
    #mouse position + update the map
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll[0])//  Tile_size
    y = (pos[1] + scroll[1])//Tile_size
    
    if pos[0]< SCREEN_WIDTH and pos[1] <SCREEN_HEIGHT-100:
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1
                
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                scroll_right = True
            if event.key == K_a:
                scroll_left = True
            if event.key == K_s:
                scroll_down = True
            if event.key == K_w:
                scroll_up =  True

        if event.type == pygame.KEYUP:
            if event.key == K_a:
              
                scroll_left = False
            if event.key == K_d:
                scroll_right = False
            if event.key == K_s:
                scroll_down = False
            if event.key == K_w:
                scroll_up =  False
            
        if event.type == QUIT:
            running = False
            pygame.quit()

    pygame.display.update()
    clock.tick(120)



