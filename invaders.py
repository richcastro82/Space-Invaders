# RICHARD CASTRO
# DECEMBER 2021
# SPACE INVADERS GAME BUILT WITH PYGAME


# IMPORT LIBRARIES
import pygame, sys
from rules import *

# INITIALIZE THE GAME SETTINGS
pygame.init()
width=800
height=800
size=(width, height)
screen=pygame.display.set_mode(size)
fps=30
refresh_rate=pygame.time.Clock()
test_block=pygame.Surface((100,100))
game_bg=pygame.image.load('Images/Game_BG.png')
start_bg=pygame.image.load('Images/start_bg.jpg')
hero=pygame.image.load('graphics/hero.png')


# GAME OVER METHOD
def game_over():
    pygame.quit()
    sys.exit()

# PAUSE GAME METHOD
def pause_screen():
    pass

# START SCREEN METHOD
def start_screen():
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play(1)
    START_BUT=BUTTON((0,220,0), 330, 500, 150, 50, "Start Game")
    QUIT_BUT=BUTTON((0,220,0), 330, 580, 150, 50, "Quit Game")
    start_game=False
    while start_game==False:
        pygame.display.update()
        refresh_rate.tick(fps)
        screen.blit(start_bg, (0,0))
        START_BUT.draw(screen)
        QUIT_BUT.draw(screen)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    start_game=True

# GAME PLAY
def run_game():
    # 1. create level display
    # 2. create lives display
    HERO=SHIPS(375,650,20)
    while True:
        pygame.mixer.music.stop()
        pygame.display.update()
        refresh_rate.tick(fps)
        # 1. paint the lives on top left of SCREEN
        # 2. paint the level on top right of screen
        screen.blit(game_bg, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()
            # 1. lock ship movement to x:600-800 and y:0-800
            # 2. make movement fluid
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    HERO.ship_x+=10
                if event.key==pygame.K_LEFT:
                    HERO.ship_x-=10
        HERO.draw_hero()

# MAIN GAME LOOP
def main():

        start_screen()
        run_game()
        game_over()



if __name__=="__main__":
    main()
