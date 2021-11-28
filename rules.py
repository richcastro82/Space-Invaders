import pygame, sys
from invaders import screen, hero


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

    def draw_hero(self):
        ship=pygame.Rect(self.ship_x, self.ship_y, self.ship_size, self.ship_size)
        screen.blit(hero, ship)

    def shoot_laser(self):
        pygame.mixer.Sound.play(hero_laser)
        # 1. find the hero ship x position
        # 2. send laser graphic from that x position up -1 until off screen
