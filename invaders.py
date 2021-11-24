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


def main():
    clock.tick(fps)
    pygame.display.update()
    SCREEN.fill((100,100,100))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()



if __name__=="__main__":
    main()
