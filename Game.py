import sys
import pygame
import math
from random import randint


def spriteList(refX0, refY0, nSprites):

    sprites = []
    for i in range(0, (nSprites-1)):
        sprite = spritesheet.subsurface((refX0 + 32*i, refY0, RESOLUTION, RESOLUTION))
        sprite = pygame.transform.scale(sprite, (RESOLUTION * SCALE, RESOLUTION * SCALE))
        sprites.append(sprite)
    return sprites


def arrow(refX, refY):

    global arrowImgIndex

    arrowImgIndex += 0.06
    if arrowImgIndex >= len(arrowSprites):
        arrowImgIndex = 0

    arrowImg = arrowSprites[int(arrowImgIndex)]
    screen.blit(arrowImg, (refX * SCALE, refY * SCALE))


def player(refX, refY):

    global playerImgIndex
    global playerMoved

    if playerMoved:
        playerImgIndex += 0.2
        if playerImgIndex >= len(playerSpritesLeft):
            playerImgIndex = 0.0
        playerMoved = False

    if playerLookLeft:
        playerImg = playerSpritesLeft[int(playerImgIndex)]
    else:
        playerImg = playerSpritesRight[int(playerImgIndex)]

    screen.blit(playerImg, (refX*SCALE, refY*SCALE))


def npcGoldy(refX, refY):

    global npcGoldyImgIndex

    npcGoldyImgIndex += 0.1
    if npcGoldyImgIndex >= len(npcGoldySpritesLeft):
        npcGoldyImgIndex = 0.0

    if npcLeft == 1:
        goldyImg = npcGoldySpritesRight[int(npcGoldyImgIndex)]
    else:
        goldyImg = npcGoldySpritesLeft[int(npcGoldyImgIndex)]

    screen.blit(goldyImg, (refX*SCALE, refY*SCALE))


def trueDoor(refX, refY):

    global doorIdleImgIndex

    doorIdleImgIndex += 0.05
    if doorIdleImgIndex >= len(doorIdleSprites):
        doorIdleImgIndex = 0.0

    trueDoorImg = doorIdleSprites[int(doorIdleImgIndex)]
    screen.blit(trueDoorImg, (refX*SCALE, refY*SCALE))


def fakeDoor(refX, refY):

    global doorIdleImgIndex

    doorIdleImgIndex += 0.08
    if doorIdleImgIndex >= len(doorIdleSprites):
        doorIdleImgIndex = 0.0

    fakeDoorImg = doorIdleSprites[int(doorIdleImgIndex)]
    screen.blit(fakeDoorImg, (refX*SCALE, refY*SCALE))


def message(txt, posX, posY):

    text = font.render(txt, True, (255, 255, 255))
    screen.blit(text, (posX*SCALE, posY*SCALE))


def isColliding(x1, y1, x2, y2):

    distance = math.sqrt(((x2+RESOLUTION/2) - (x1+RESOLUTION/2)) ** 2 + ((y2+RESOLUTION/2) - (y1+RESOLUTION/2)) ** 2)
    if distance < 20:
        return True
    else:
        return False


def showHint():

    global hintShowed
    global textHint

    if not hintShowed:
        i = randint(0, 9)
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
    global playerImgIndex
    global npcGoldyImgIndex
    global doorIdleImgIndex

    level += 1
    if level > MAX_LEVEL:
        gameState = "VITORIA"
    textLevel = "Sala" + str(level).rjust(2)

    playerX = playerX0
    playerY = playerY0
    playerImgIndex = 0.0
    npcGoldyImgIndex = 0.0
    doorIdleImgIndex = 0.0
    stage = pygame.image.load("stage.png")
    stage = pygame.transform.scale(stage, (WIDTH * SCALE, HEIGHT * SCALE))
    counter = 30
    textCounter = str(counter).rjust(3)
    exitLeft = randint(0, 1)
    npcLeft = randint(0, 1)
    hintShowed = False


pygame.init()

spritesheet = pygame.image.load("spritesheet.png")


WIDTH = 160
HEIGHT = 96
SCALE = 6
RESOLUTION = 32

hintLeft = ["esquerda1", "esquerda2", "esquerda3", "esquerda4", "esquerda5", "esquerda6", "esquerda7", "esquerda8", "esquerda9", "esquerda10"]
hintRight = ["direita1", "direita2", "direita3", "direita4", "direita5", "direita6", "direita7", "direita8", "direita9", "direita10"]

stage = pygame.image.load("stage.png")
stage = pygame.transform.scale(stage, (WIDTH*SCALE, HEIGHT*SCALE))
menu = pygame.image.load("menu.png")
menu = pygame.transform.scale(menu, (WIDTH*SCALE, HEIGHT*SCALE))
font = pygame.font.SysFont("Consolas", 20)
screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE), 0, 32)
timer = pygame.time.Clock()
level = 1
MAX_LEVEL = 5
textLevel = "Sala" + str(level).rjust(2)

gameState = "MENU"
running = True
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 60
textCounter = str(counter).rjust(3)
exitLeft = randint(0, 1)
npcLeft = randint(0, 1)

arrowSprites = spriteList(0, 4*32, 6)
arrowImgIndex = 0.0

arrowX = 90
arrowY = 18

playerSpritesLeft = spriteList(0, 0, 5)
playerSpritesRight = spriteList(0, 32, 5)
playerImgIndex = 0.0
playerMoved = False

playerX0 = (WIDTH/2) - (RESOLUTION/2)
playerY0 = 60

playerX = playerX0
playerY = playerY0

npcGoldySpritesLeft = spriteList(160, 0, 6)
npcGoldySpritesRight = spriteList(160, 32, 6)
npcGoldyImgIndex = 0.0

goldyX = 8
goldyY = 59

doorIdleSprites = spriteList(0, 64, 12)
doorIdleImgIndex = 0.0

trueDoorX = 0
trueDoorY = 33

fakeDoorX = 0
fakeDoorY = 33

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
    if gameState == "MENU":
        screen.blit(menu, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    arrowY = 18
                if event.key == pygame.K_DOWN:
                    arrowY = 32
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if arrowY == 18:
                        gameState = "NORMAL"
                    elif arrowY == 32:
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        arrow(arrowX, arrowY)

    elif gameState == "NORMAL":
        screen.blit(stage, (0, 0))

        if exitLeft == 1:
            trueDoorX = 41
            fakeDoorX = 85
        else:
            trueDoorX = 85
            fakeDoorX = 41

        if npcLeft == 1:
            goldyX = 8
        else:
            goldyX = 120

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
                if event.key == pygame.K_UP:
                    playerUp = True
                elif event.key == pygame.K_DOWN:
                    playerDown = True
                if event.key == pygame.K_RIGHT:
                    playerRight = True
                    playerLookLeft = False
                elif event.key == pygame.K_LEFT:
                    playerLeft = True
                    playerLookLeft = True
                if event.key == pygame.K_SPACE:
                    playerAction = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    playerUp = False
                elif event.key == pygame.K_DOWN:
                    playerDown = False
                if event.key == pygame.K_RIGHT:
                    playerRight = False
                elif event.key == pygame.K_LEFT:
                    playerLeft = False
                if event.key == pygame.K_SPACE:
                    playerAction = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if playerUp:
            playerY -= speed
            playerMoved = True
        if playerDown:
            playerY += speed
            playerMoved = True
        if playerRight:
            playerX += speed
            playerMoved = True
        if playerLeft:
            playerX -= speed
            playerMoved = True

        if playerX > 108:
            playerX = 108
        if playerX < 20:
            playerX = 20
        if playerY > (HEIGHT - RESOLUTION):
            playerY = (HEIGHT - RESOLUTION)
        if playerY < 36:
            playerY = 36

        if playerAction:
            if isColliding(playerX, playerY, trueDoorX, trueDoorY):
                nextLevel()
            elif isColliding(playerX, playerY, fakeDoorX, fakeDoorY):
                gameState = "GAME OVER"
            elif isColliding(playerX, playerY, goldyX, goldyY):
                showHint()
                print("dica")

        trueDoor(trueDoorX, trueDoorY)
        fakeDoor(fakeDoorX, fakeDoorY)
        npcGoldy(goldyX, goldyY)
        player(playerX, playerY)

        message(textLevel, 10, 5)
        message(textCounter, WIDTH - 20, 5)

        if hintShowed:
            message(textHint, WIDTH/2, 5)
    elif gameState == "GAME OVER":
        screen.fill((0, 0, 0))
        message("Voce perdeu!", WIDTH/2, HEIGHT/2)
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

pygame.display.quit()
