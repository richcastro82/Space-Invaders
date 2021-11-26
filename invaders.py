import pygame, sys
pygame.init()
width=800
height=800
size=(width, height)
screen=pygame.display.set_mode(size)
fps=30
refresh_rate=pygame.time.Clock()
test_block=pygame.Surface((100,100))
bg=pygame.image.load('Images/Game_BG.png')
but_width=80
but_height=40


class BUTTON:
    def __init__(self, color, x, y, but_width, but_height, text=""):
        self.x=x
        self.y=y
        self.color=color
        self.but_width=but_width
        self.but_height=but_height
        self.text=text



# bg2=pygame.image.load('Images/test.jpg')
# GAME OVER METHOD
def game_over():
    pygame.quit()
    sys.exit()


# PAUSE GAME METHOD
def pause_screen():
    pass


# START SCREEN METHOD
def start_screen():
    pass
    start_game=False
    while start_game==False:
        pygame.display.update()
        refresh_rate.tick(fps)
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    start_game=True



# GAME PLAY
def run_game():
    pass


# MAIN GAME LOOP
def main():

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()

        start_screen()
        pygame.quit()


if __name__=="__main__":
    main()
