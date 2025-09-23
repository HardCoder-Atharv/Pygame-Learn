
import pygame
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000,800),0,32)
player = pygame.Rect(100,100,100,200)

tiles = [pygame.Rect(500,500,50,100),pygame.Rect(700,500,50,100)]
time = pygame.time.Clock()
player_img = pygame.image.load('player.png')
transformed_player = pygame.transform.scale(player_img,(100,100))

move_right = False
move_left = False
move_up = False
move_down = False




def is_collide(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)

    return hit_list


def update_move(rect,movement,tiles):
    rect.x += movement[0]
    collisions = is_collide(rect,tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left  = tile.right

    rect.y += movement[1]
    collisions = is_collide(rect,tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top  = tile.bottom

    return rect













while True:
    movement = [0,0]
    screen.fill((100,34,30))
    
    print(player.x,player.y)
    



    
    for tile in tiles:
        pygame.draw.rect(screen,(200,30,40),tile)
    pygame.draw.rect(screen,(100,100,50),player)

    if move_right == True:
        movement[0] += 5

    if move_left == True:
        movement[0] -= 5

    if move_up == True:
        movement[1] -= 5

    if move_down == True:
        movement[1] += 5
    player =  update_move(player,movement,tiles)
    screen.blit(transformed_player,(player.x,player.y))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==   KEYDOWN:
            if event.key == K_RIGHT:
                move_right = True
                print('h')
            if event.key == K_LEFT:
                move_left = True
                print('h')
            if event.key == K_UP:
                move_up = True
            if event.key == K_DOWN:
                move_down = True
                print('h')


        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_right = False
                print('h')
            if event.key == K_LEFT:
                move_left = False
                print('h')
            if event.key == K_UP:
                move_up = False
            if event.key == K_DOWN:
                move_down = False
                print('h')
        if event.type == QUIT:
    
    
    
            pygame.quit()
    time.tick(60)


