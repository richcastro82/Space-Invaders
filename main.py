# RICHARD CASTRO
# NOVEMBER 2021
# SPACE INVADERS

# GAME VARIABLES
fps=30
width=800
height=800
Enemies=[]
maxLasers=3
ShipSpeed=1
LaserSpeed=1
heroWidth=100
heroHeight=100

# GAME INITIALIZE
import pygame, sys
pygame.init()
size=(width, height)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)

# IMPORT GRAPHICS
bg=pygame.image.load('images/Game_BG.png')
heroImage=pygame.image.load('graphics/hero.png')
greenImage=pygame.image.load("graphics/pixel_ship_green_small.png")
redImage=pygame.image.load("graphics/pixel_ship_red_small.png")
blaster=pygame.mixer.Sound("fx/hero_laser.wav")

# LEVEL MAPPING
Level1=[0,1,0,2,0,1,0,2]
Level2=[]
Level3=[]

# GENERAL SHIP CLASS
class Ships:
    # INITIAL CLASS
    def __init__(self, x, y, width, height, color, image, health, healthLoc):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color=color
        self.Image=image
        self.lasers=[]
        self.health = health
        self.healthLoc=healthLoc
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)

    # DRAW SHIPS CLASS
    def drawShip(self):
        self.shipRect=pygame.Rect(self.x, self.y, self.width, self.height)
        self.healthRect=pygame.Rect(self.x, self.y+self.healthLoc, self.health, 4)
        screen.blit(self.Image, self.shipRect)
        if self.health>=50:
            pygame.draw.rect(screen, (0,255,0), self.healthRect)
        if self.health<50 and self.health>25:
            pygame.draw.rect(screen, (0,0,255), self.healthRect)
        if self.health<=25 and self.health>0:
            pygame.draw.rect(screen, (255,0,0), self.healthRect)

    # SHIP LASER CLASS
    def drawLasers(self, laser, blaster, playSound):
        self.lasers.append(laser)
        if playSound==True:
            pygame.mixer.Sound.play(blaster)

    # MOVE SHIP LASER CLASS
    def moveLasers(self):
        for laser in self.lasers:
            if laser.y > 0 and laser.y < height:
                pygame.draw.rect(screen, self.color, laser)
            else:
                self.lasers.remove(laser)

    # REMOVE ENEMIES CLASS
    def remove(self, Enemy):
        Enemies.remove(Enemy)



def drawBoard():
    point=10
    for item in Level1:
        if item ==1:
            Enemies.append(Ships(point,0,75,75, (0,255,0), greenImage, 75, -20))
        if item ==2:
            Enemies.append(Ships(point,0,75,75, (0,255,0), redImage, 75, -10))
        else:
            pass
        point+=100



def enemyLasers():
    for enemy in Enemies:
        eLaser=pygame.Rect(100,100, 4, 10)
        enemy.lasers.append(eLaser)
        for laser in enemy.lasers:
            pygame.draw.rect(screen, (255,0,0), eLaser)


def playerMovement(Hero):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and Hero.x<width-heroWidth: #right
        Hero.x+=1*ShipSpeed
    if keys[pygame.K_LEFT] and Hero.x>1: #LEFT
        Hero.x-=1*ShipSpeed
    if keys[pygame.K_UP] and Hero.y>500: #right
        Hero.y-=1*ShipSpeed
    if keys[pygame.K_DOWN] and Hero.y<height-heroWidth: #LEFT
        Hero.y+=1*ShipSpeed



def main():
    clock.tick(fps)
    Hero=Ships(width//2-heroWidth//2, height-200-heroHeight//2, heroWidth, heroHeight, (255,0,0), heroImage, 100, 110)
    drawBoard()
    enemyLasers()
    playSound=False
    while True:
        pygame.display.update()
        screen.blit(bg, (0,0))
        Hero.drawShip()
        for Enemy in Enemies:
            if Enemy.health>0:
                Enemy.drawShip()
                Enemy.y+=.05
            if Enemy.y>height:
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
        playerMovement(Hero)

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
