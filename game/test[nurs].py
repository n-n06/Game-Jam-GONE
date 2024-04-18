import pygame
from spriteclasses import Player, Door, Wall
from interaction import Interactable
from lighting import Dim, Light
from menu import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))


bg = pygame.transform.scale(pygame.image.load('images/background.png'), (1280, 720))

clock = pygame.time.Clock()

player = Player(screen, (50,600))
door = Door(screen, (600,60))

notebook = Interactable(1, (195, 280, 250, 120), (255,255,255), room="room1", item="notebook")
puddle = Interactable(1, (950, 280, 200, 200), (255,255,255), room="room1", item="puddle")

lantern = Light(screen, (220,220,220), 25, (player.rect.x + 97, player.rect.y + 152))
wall = Wall((0,0), (750,200))
dim = Dim(screen)


bgm_channel = pygame.mixer.Channel(0)
sfx_channel = pygame.mixer.Channel(1)



game_menu(bgm_channel, sfx_channel, "main")


def scene1():
    run = True
    while run:
        screen.blit(bg, (0,0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if notebook.rect.colliderect(player.rect):
                        notebook.enable = True
                    if puddle.rect.colliderect(player.rect):
                        puddle.enable = True
                    if door.rect.colliderect(player.rect):
                        door.open_door(sfx_channel)
                if event.key == pygame.K_ESCAPE:
                    game_menu(bgm_channel, sfx_channel, "pause")
                

        pygame.draw.rect(screen, (255,255,255), wall.rect)
        keys = pygame.key.get_pressed()
  
        player.move(keys, lantern)
 

        door.blit()
        player.blit()



        dim.darken(150)

        lantern.blit((100,100,100), size=5)

        notebook.interaction(player, screen, keys)
        puddle.interaction(player, screen, keys)

        pygame.display.update()
scene1()