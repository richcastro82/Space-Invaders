# RICHARD CASTRO
# DECEMBER 2021
# SPACE INVADERS GAME BUILT WITH PYGAME


#########################################################
##  1. Start menu buttons do not work.                 ##
##  2. Change the size of KingCastro on start menu.    ##
##  3. Create a pause function from run_game().        ##
#########################################################


# IMPORT LIBRARIES
import pygame, sys
from rules import *

# INITIALIZE THE GAME SETTINGS
pygame.init()
game_bg=pygame.image.load('images/Game_BG.png')
start_bg=pygame.image.load('images/start_bg.jpg')
hero=pygame.image.load('graphics/hero.png')
hero_blaster=image.load('graphics/pixel_laser_red.png')
hero_laser=pygame.mixer.Sound("fx/hero_laser.wav")
enemy_laser=pygame.mixer.Sound("fx/enemy_laser.wav")

fps=30
user_speed=10
size=(800,800)
screen=pygame.display.set_mode(size)
refresh_rate=pygame.time.Clock()
test_block=pygame.Surface((100,100))


# GAME OVER FUNCTION
def game_over():
    start_screen()
    # pygame.quit()
    # sys.exit()

# PAUSE GAME FUNCTION
def pause_screen():
    pass

# START SCREEN FUNCTION
def start_screen():
    pygame.mixer.music.load("fx/intro.mp3")
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

def draw_gui():
    font=pygame.font.SysFont('comicsans', 20)
    lives="3 lives"
    level="Level 1"
    level_display=BUTTON((20,10,100), 50, 750, 50, 50, level)
    lives_display=BUTTON((20,10,100), 700, 750, 50, 50, lives)
    lives_display.draw(screen)
    level_display.draw(screen)

# GAME PLAY
def run_game():
    pygame.mixer.music.stop()
    HERO=SHIPS(375,650,20)

    # MAIN GAME LOOP
    while True:
        pygame.display.update()
        refresh_rate.tick(fps)
        screen.blit(game_bg, (0,0))
        draw_gui()
        HERO.draw_hero()

        # CLOSE GAME WINDOW FUNCTION
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()

        # PLAYER INPUT CONTROLS
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: #right
            HERO.ship_x+=1*user_speed
        if keys[pygame.K_LEFT]: #LEFT
            HERO.ship_x-=1*user_speed
        if keys[pygame.K_SPACE]:
            HERO.shoot_laser()



# MAIN GAME FUNCTION
def main():
        start_screen()
        run_game()
        game_over()


if __name__=="__main__":
    main()
