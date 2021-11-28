import pygame, sys
from invaders import screen, hero
hero_laser=pygame.mixer.Sound("fx/hero_laser.wav")
green_enemy=pygame.image.load("graphics/pixel_ship_green_small.png")
red_enemy=pygame.image.load("graphics/pixel_ship_red_small.png")
blue_enemy=pygame.image.load("graphics/pixel_ship_blue_small.png")
enemy_laser=pygame.mixer.Sound("fx/enemy_laser.wav")

HEIGHT=800
WIDTH=800
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
        self.ship_x=ship_x
        self.ship_y=ship_y
        self.ship_size=ship_size
        self.health=health

    def draw_hero(self):
        ship=pygame.Rect(self.ship_x, self.ship_y, self.ship_size, self.ship_size)
        screen.blit(hero, ship)

    def shoot_laser(self):
        pygame.mixer.Sound.play(hero_laser)
        hero_blaster=pygame.image.load('graphics/pixel_laser_red.png')
        hero_rect=pygame.Rect(self.ship_x,(self.ship_y-50),40,40)






    def draw_enemy_green(self):
        green_ship=pygame.Rect(self.ship_x, self.ship_y, self.ship_size, self.ship_size)
        if green_ship.y<HEIGHT:
            self.ship_y+=1
            screen.blit(green_enemy, green_ship)
            # pygame.mixer.Sound.play(enemy_laser)
        # enemy_blaster=pygame.image.load('graphics/pixel_laser_red.png')
        # enemy_rect=pygame.Rect(self.ship_x-(self.ship_size/2),(self.ship_y+50),40,40)
        # screen.blit(enemy_blaster, enemy_rect)

    def draw_enemy_red(self):
        red_ship=pygame.Rect(self.ship_x, self.ship_y, self.ship_size, self.ship_size)
        self.ship_y+=1
        screen.blit(red_enemy, red_ship)
        pygame.mixer.Sound.play(enemy_laser)
        enemy_blaster=pygame.image.load('graphics/pixel_laser_yellow.png')
        enemy_rect=pygame.Rect(self.ship_x-(self.ship_size/2),(self.ship_y+50),40,40)
        screen.blit(enemy_blaster, enemy_rect)

    def draw_enemy_blue(self):
        blue_ship=pygame.Rect(self.ship_x, self.ship_y, self.ship_size, self.ship_size)
        self.ship_y+=1
        screen.blit(blue_enemy, blue_ship)
        pygame.mixer.Sound.play(enemy_laser)
        enemy_blaster=pygame.image.load('graphics/pixel_laser_green.png')
        enemy_rect=pygame.Rect(self.ship_x-(self.ship_size/2),(self.ship_y+50),40,40)
        screen.blit(enemy_blaster, enemy_rect)
