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
            text=font.render(self.text, 1, (255,255,255))
            screen.blit(text, (self.x+(self.but_width/2-text.get_width()/2), self.y+(self.but_height/2-text.get_height()/2 ) ))

    def mouseOver(self, pos):
        if pos[0]>self.x and pos[0]<self.x+self.but_width:
            if pos[1]>self.y and pos[1]<self.y+self.but_height:
                return True
        return False

# SHIP CLASS
class SHIPS:
    def __init__(self, ship_x, ship_y, ship_size, health=100):
        self.x=ship_x
        self.y=ship_y
        self.size=ship_size
        self.health=health
        self.ship_image=None
        self.ship_laser=None

    def draw_ship(self, ship_image):
        ship=pygame.Rect(self.x, self.y, self.size, self.size)
        screen.blit(ship_image, ship)
