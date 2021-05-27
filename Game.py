import pygame
import math
from random import randint

def player(refX, refY):

    if playerLookLeft:
        playerImg = spritesheet.subsurface((0,0,RESOLUTION,RESOLUTION))
    else:
        playerImg = spritesheet.subsurface((0,32,RESOLUTION,RESOLUTION))
    playerImg = pygame.transform.scale(playerImg, (RESOLUTION * SCALE, RESOLUTION * SCALE))
    screen.blit(playerImg, (refX*SCALE, refY*SCALE))

def npcGoldy(refX, refY):

    goldyImg = spritesheet.subsurface((5*32,0,RESOLUTION,RESOLUTION))
    goldyImg = pygame.transform.scale(goldyImg, (RESOLUTION * SCALE, RESOLUTION * SCALE))
    screen.blit(goldyImg, (refX*SCALE,refY*SCALE))

def trueDoor(refX, refY):
    trueDoorImg = spritesheet.subsurface((32,2*32,RESOLUTION,RESOLUTION))
    trueDoorImg = pygame.transform.scale(trueDoorImg, (RESOLUTION * SCALE, RESOLUTION * SCALE))
    screen.blit(trueDoorImg, (refX*SCALE,refY*SCALE))

def fakeDoor(refX, refY):
    fakeDoorImg = spritesheet.subsurface((32,2*32,RESOLUTION,RESOLUTION))
    fakeDoorImg = pygame.transform.scale(fakeDoorImg, (RESOLUTION * SCALE, RESOLUTION * SCALE))
    screen.blit(fakeDoorImg, (refX*SCALE, refY*SCALE))

def message(txt, posX, posY):

    text = font.render(txt, True, (255, 255, 255))
    screen.blit(text, (posX*SCALE,posY*SCALE))

def isColliding(x1 , y1 , x2 , y2):
    distance = math.sqrt(((x2+RESOLUTION/2) - (x1+RESOLUTION/2)) ** 2 + ((y2+RESOLUTION/2) - (y1+RESOLUTION/2)) ** 2)
    if distance < 45:
        return True
    else:
        return False

def showHint():

    global hintShowed
    global textHint

    if not hintShowed:
        i = randint(0,9)
        if exitLeft == 1:
            textHint = hintLeft[i]
            hintShowed = True
        else:
            textHint = hintRight[i]
            hintShowed = True

def nextLevel():

    global level
    global textLevel
    global playerX
    global playerY
    global stage
    global counter
    global textCounter
    global exitLeft
    global gameState
    global npcLeft
    global hintShowed

    level += 1
    if level > MAX_LEVEL:
        gameState = "VITORIA"
    textLevel = "Sala" + str(level).rjust(2)

    playerX = playerX0
    playerY = playerY0
    stage = pygame.image.load("stage.png")
    stage = pygame.transform.scale(stage, (WIDTH * SCALE, HEIGHT * SCALE))
    counter = 30
    textCounter = str(counter).rjust(3)
    exitLeft = randint(0, 1)
    npcLeft = randint(0,1)
    hintShowed = False

pygame.init()

spritesheet = pygame.image.load("spritesheet.png")


WIDTH = 512
HEIGHT = 256
SCALE = 2
RESOLUTION = 32

hintLeft = ["esquerda1","esquerda2","esquerda3","esquerda4","esquerda5","esquerda6","esquerda7","esquerda8","esquerda9","esquerda10"]
hintRight = ["direita1","direita2","direita3","direita4","direita5","direita6","direita7","direita8","direita9","direita10"]

stage = pygame.image.load("stage.png")
stage = pygame.transform.scale(stage, (WIDTH*SCALE, HEIGHT*SCALE))
font = pygame.font.SysFont("Consolas", 20)
screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE),0,32)
timer = pygame.time.Clock()
level = 1
MAX_LEVEL = 5
textLevel = "Sala" + str(level).rjust(2)

gameState = "NORMAL"
running = True
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 60
textCounter = str(counter).rjust(3)
exitLeft = randint(0, 1)
npcLeft = randint(0,1)

playerX0 = (WIDTH/2) - (RESOLUTION/2)
playerY0 = 200

playerX = playerX0
playerY = playerY0

goldyX = 100
goldyY = 180

trueDoorX = 0
trueDoorY = 128

fakeDoorX = 0
fakeDoorY = 128

hintShowed = False
textHint = ""

speed = 1
runningCounter = True
playerUp = False
playerDown = False
playerRight = False
playerLeft = False
playerAction = False
playerLookLeft = True

while running:
    if gameState == "NORMAL":
        screen.fill((0, 0, 0))
        screen.blit(stage,(0,0))

        if exitLeft == 1:
            trueDoorX = 176
            fakeDoorX = 306
        else:
            trueDoorX = 306
            fakeDoorX = 176

        if npcLeft == 1:
            goldyX = 100
        else:
            goldyX = 380

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and runningCounter:
                counter -= 1
                if counter > -1:
                    textCounter = str(counter).rjust(3)
                else:
                    gameState = "GAME OVER"
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    playerUp = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    playerDown = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerRight = True
                    playerLookLeft = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerLeft = True
                    playerLookLeft = True
                if event.key == pygame.K_SPACE:
                    playerAction = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    playerUp = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    playerDown = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerRight = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerLeft = False
                if event.key == pygame.K_SPACE:
                    playerAction = False
        if playerUp:
            playerY -= speed
        if playerDown:
            playerY += speed
        if playerRight:
            playerX += speed
        if playerLeft:
            playerX -= speed

        if playerX > 390:
            playerX = 390
        if playerX < 90:
            playerX = 90
        if playerY > (HEIGHT - RESOLUTION):
            playerY = (HEIGHT - RESOLUTION)
        if playerY < 140:
            playerY = 140

        if playerAction:
            if isColliding(playerX, playerY, trueDoorX,trueDoorY):
                nextLevel()
            elif isColliding(playerX, playerY, fakeDoorX, fakeDoorY):
                gameState = "GAME OVER"
            elif isColliding(playerX,playerY, goldyX, goldyY):
                showHint()
                print("dica")

        trueDoor(trueDoorX, trueDoorY)
        fakeDoor(fakeDoorX, fakeDoorY)
        npcGoldy(goldyX, goldyY)
        player(playerX, playerY)

        message(textLevel, 30, 10)
        message(textCounter, WIDTH - 30, 10)

        if hintShowed:
            message(textHint, WIDTH/2 , 10)
    elif gameState == "GAME OVER":
        screen.fill((0,0,0))
        message("Voce perdeu!",WIDTH/2,HEIGHT/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    elif gameState == "VITORIA":
        screen.fill((0, 0, 0))
        message("Voce venceu!", WIDTH / 2, HEIGHT / 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.update()