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
fps=30
user_speed=10
WIDTH=800
HEIGHT=800
size=(WIDTH, HEIGHT)
screen=pygame.display.set_mode(size)
refresh_rate=pygame.time.Clock()
test_block=pygame.Surface((100,100))
ship_WIDTH=90

# IMPORT GRAPHICS AND SOUND
game_bg=pygame.image.load('images/Game_BG.png')
start_bg=pygame.image.load('images/start_bg.jpg')
hero=pygame.image.load('graphics/hero.png')
blaster=pygame.image.load('graphics/pixel_laser_red.png')
hero_laser=pygame.mixer.Sound("fx/hero_laser.wav")
e_ship=pygame.image.load("graphics/pixel_ship_green_small.png")
e_blaster=pygame.image.load('graphics/pixel_laser_red.png')
e_laser=pygame.mixer.Sound("fx/enemy_laser.wav")



def shoot_laser(Hero_Blasters):
    blast=pygame.Rect(self.x, self.y, self.size, self.size)
    # pygame.mixer.Sound.play(laser)
    # screen.blit(blaster, blast)
    screen.blit(blast, Hero_Blasters)

# GAME OVER FUNCTION
def game_over():
    pygame.quit()
    sys.exit()

# INTERFACE OVERLAY
def draw_gui():
    font=pygame.font.SysFont('comicsans', 20)
    lives=3
    level=1
    lives_label=font.render(f"Lives: {lives}", 1, (255,255,255))
    screen.blit(lives_label,(10,765))
    level_label=font.render(f"Lives: {level}", 1, (255,255,255))
    screen.blit(level_label,(700,765))
    # level_display=BUTTON((20,10,100), 50, 750, 100, 50, level)
    # lives_display=BUTTON((20,10,100), 650, 750, 100, 50, lives)
    # lives_display.draw(screen)
    # level_display.draw(screen)

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
    Hero_Blasters=[]

    # MAIN GAME LOOP
    while True:
        pygame.display.update()
        refresh_rate.tick(fps)
        screen.blit(game_bg, (0,0))
        draw_gui()
        HERO.draw_ship(hero)
        GREEN.draw_ship(e_ship)


        # CLOSE GAME WINDOW FUNCTION
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()


        if keys[pygame.K_SPACE]:
            # HERO.shoot_laser(blaster, hero_laser)
            hero_blasts=pygame.Rect(100,400,50,50)
            Hero_Blasters.append(hero_blasts)
            shoot_laser(Hero_Blasters)


# MAIN GAME FUNCTION
def main():
        start_screen()
        run_game()
        game_over()


if __name__=="__main__":
    main()
