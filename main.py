# RICHARD CASTRO
# NOVEMBER 2021
# SPACE INVADERS

width=800
height=800
fps=30
ShipSpeed=1
LaserSpeed=1
heroWidth=100
heroHeight=100
maxLasers=3
Level1=[1,1,1,1,1,1,1,1]
Enemies=[]

import pygame, sys
pygame.init()
size=(width, height)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)

bg=pygame.image.load('images/Game_BG.png')
heroImage=pygame.image.load('graphics/hero.png')
greenImage=pygame.image.load("graphics/pixel_ship_green_small.png")
redImage=pygame.image.load("graphics/pixel_ship_red_small.png")
blaster=pygame.mixer.Sound("fx/hero_laser.wav")


class Ships:
    def __init__(self, x, y, width, height, color, image, health=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color=color
        self.Image=image
        self.lasers=[]
        self.health = health
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)

    def drawShip(self):
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)
        self.healthRect=pygame.Rect(self.x, self.y+self.height+10, self.health, 4)
        screen.blit(self.Image, self.shipRect)
        pygame.draw.rect(screen, (0,255,0), self.healthRect)

    def drawEnemy(self):
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.Image, self.shipRect)

    def drawLasers(self, Herolaser, blaster, playSound):
        self.lasers.append(Herolaser)
        if playSound==True:
            pygame.mixer.Sound.play(blaster)

    def moveLasers(self):
        for laser in self.lasers:
            if laser.y > 0 and laser.y < height:
                pygame.draw.rect(screen, self.color, laser)
            else:
                self.lasers.remove(laser)
    def remove(self, Enemy):
        Enemies.remove(Enemy)


def main():
    clock.tick(fps)
    Hero=Ships(width//2-heroWidth//2, height-200-heroHeight//2, heroWidth, heroHeight, (255,0,0), heroImage)
    point=10
    for item in Level1:
        if item ==1:
            Enemies.append(Ships(point,0,75,75, (0,255,0), greenImage))
        if item ==2:
            Enemies.append(Ships(point,0,75,75, (0,255,0), redImage))
        else:
            pass
        point+=100
    playSound=False
    while True:
        pygame.display.update()
        screen.blit(bg, (0,0))
        Hero.drawShip()
        for Enemy in Enemies:
            if Enemy.health>0:
                Enemy.drawEnemy()
                Enemy.y+=.05
            if Enemy.y>height:
                print('Hero HIT!')
                Enemy.remove(Enemy)
                Hero.health-=10

        Hero.moveLasers()
        for laser in Hero.lasers:
            laser.y-=1
            for Enemy in Enemies:
                if Enemy.shipRect.colliderect(laser):
                    Enemy.health-=10
                    Hero.lasers.remove(laser)

        # PLAYER INPUT CONTROLS
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and Hero.x<width-heroWidth: #right
            Hero.x+=1*ShipSpeed
        if keys[pygame.K_LEFT] and Hero.x>1: #LEFT
            Hero.x-=1*ShipSpeed
        if keys[pygame.K_UP] and Hero.y>500: #right
            Hero.y-=1*ShipSpeed
        if keys[pygame.K_DOWN] and Hero.y<height-heroWidth: #LEFT
            Hero.y+=1*ShipSpeed
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    Herolaser=pygame.Rect(Hero.x+Hero.width//2, Hero.y, 10,40)
                    Hero.drawLasers(Herolaser, blaster, playSound)
                if event.key==pygame.K_o:
                    if playSound == False:
                        playSound=True
                    else:
                        playSound=False


if __name__=="__main__":
    main()
