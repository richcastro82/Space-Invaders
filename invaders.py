# Richard Castro
# November 2021
# Space Invaders

import sys, os, pygame, time

#game settings
width=600
height=600
SIZE=(width, height)
fps=30


#game initialize
pygame.init()
TEXT=pygame.font.Font(None, 24)
clock=pygame.time.Clock()
SCREEN=pygame.display.set_mode(SIZE)



def home_screen():
    HOME_SCREEN_BG=pygame.image.load('')
    START_BUTTON=
    QUIT_BUTTON=
    start_game=False
    while (start_game==False):
        
    # 3. quit method
    # 4. start game method
    # 5. loop it all

def play_game():
    SCREEN.fill((100,100,100))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
    # 1. calling elements
    # 2. updating game screen
    # 3. game rules


def main():
    clock.tick(fps)
    pygame.display.update()
    home_screen()
    play_game()





if __name__=="__main__":
    main()
