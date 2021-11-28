###############################################
##            RICHARD CASTRO                 ##
##            DECEMBER 2021                  ##
##   SPACE INVADERS GAME BUILT WITH PYGAME   ##
###############################################


# IMPORT LIBRARIES
import pygame, sys
from rules import *


# INITIALIZE THE GAME SETTINGS
pygame.init()
game_bg=pygame.image.load('images/Game_BG.png')
start_bg=pygame.image.load('images/start_bg.jpg')
hero=pygame.image.load('graphics/hero.png')
enemy_laser=pygame.mixer.Sound("fx/enemy_laser.wav")

fps=30
user_speed=10
WIDTH=800
HEIGHT=800
size=(WIDTH, HEIGHT)
screen=pygame.display.set_mode(size)
refresh_rate=pygame.time.Clock()
test_block=pygame.Surface((100,100))
ship_WIDTH=90


# GAME OVER FUNCTION
def game_over():
    start_screen()
    # pygame.quit()
    # sys.exit()

# INTERFACE OVERLAY
def draw_gui():
    font=pygame.font.SysFont('comicsans', 20)
    lives="3 lives"
    level="Level 1"
    level_display=BUTTON((20,10,100), 50, 750, 100, 50, level)
    lives_display=BUTTON((20,10,100), 650, 750, 100, 50, lives)
    lives_display.draw(screen)
    level_display.draw(screen)

# PAUSE GAME FUNCTION
def pause_screen():
    pass

# START SCREEN FUNCTION
def start_screen():

    pygame.mixer.music.load("fx/intro.mp3")
    pygame.mixer.music.play(1)
    START_BUT=BUTTON((136,225,85), 330, 500, 150, 50, "Start Game")
    QUIT_BUT=BUTTON((136,225,85), 330, 580, 150, 50, "Quit Game")
    start_game=False
    screen.blit(start_bg, (0,0))
    START_BUT.draw(screen)
    QUIT_BUT.draw(screen)
    while start_game==False:
        pygame.display.update()
        refresh_rate.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    start_game=True
            pos=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if START_BUT.mouseOver(pos):
                    start_game=True
                if QUIT_BUT.mouseOver(pos):
                    pygame.quit()

# GAME PLAY
def run_game():
    pygame.mixer.music.stop()
    HERO=SHIPS(375,650,20)
    GREEN=SHIPS(50,100,25)
    RED=SHIPS(150,-2,25)
    BLUE=SHIPS(350,-100,45)
    # MAIN GAME LOOP
    while True:
        pygame.display.update()
        refresh_rate.tick(fps)
        screen.blit(game_bg, (0,0))
        draw_gui()
        HERO.draw_hero()
        GREEN.draw_enemy_green()
        # RED.draw_enemy_red()
        # BLUE.draw_enemy_blue()

        # CLOSE GAME WINDOW FUNCTION
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()

        # PLAYER INPUT CONTROLS
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and HERO.ship_x<WIDTH-ship_WIDTH: #right
            HERO.ship_x+=1*user_speed
        if keys[pygame.K_LEFT] and HERO.ship_x>1: #LEFT
            HERO.ship_x-=1*user_speed
        if keys[pygame.K_UP] and HERO.ship_y>500: #right
            HERO.ship_y-=1*user_speed
        if keys[pygame.K_DOWN] and HERO.ship_y<HEIGHT-ship_WIDTH: #LEFT
            HERO.ship_y+=1*user_speed
        if keys[pygame.K_SPACE]:
            HERO.shoot_laser()

# MAIN GAME FUNCTION
def main():
        start_screen()
        run_game()
        game_over()


if __name__=="__main__":
    main()
