import pygame, sys
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
but_width=80
but_height=40
hero=pygame.image.load('graphics/hero.png')


# BUTTON CLASS
class BUTTON:
    def __init__(self, color, x, y, but_width, but_height, text=""):
        self.x=x
        self.y=y
        self.color=color
        self.but_width=but_width
        self.but_height=but_height
        self.text=text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.but_width, self.but_height), 0)
        if self.text!="":
            font=pygame.font.SysFont('comicsans', 20)
            text=font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x+(self.but_width/2-text.get_width()/2), self.y+(self.but_height/2-text.get_height()/2 ) ))

# SHIP CLASS
class SHIPS:
    def __init__(self, ship_x, ship_y, ship_size):
        self.ship_x=ship_x
        self.ship_y=ship_y
        self.ship_size=ship_size

    def draw(self):
        ship=pygame.Rect(self.ship_x, self.ship_y, self.ship_size, self.ship_size)
        screen.blit(hero, ship)

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
    # hero_x=375
    # hero_y=650
    # hero_size=20
    HER=SHIPS(375,650,20)
    while True:
        # hero_x+=1
        # hero_ship=pygame.Rect(hero_x,hero_y,hero_size, hero_size)
        pygame.mixer.music.stop()
        pygame.display.update()
        refresh_rate.tick(fps)
        screen.blit(game_bg, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    HER.ship_x+=10
                if event.key==pygame.K_LEFT:
                    HER.ship_x-=10
        HER.draw()


        # screen.blit(hero, hero_ship)

# MAIN GAME LOOP
def main():


        start_screen()
        run_game()
        game_over()



if __name__=="__main__":
    main()
