import pygame
import math
from random import randint

def player(refX, refY):

    playerImg = spritesheet.subsurface((0,0,RESOLUTION,RESOLUTION))
    playerImg = pygame.transform.scale(playerImg, (RESOLUTION * SCALE, RESOLUTION * SCALE))
    screen.blit(playerImg, (refX, refY))

def trueDoor(refX, refY):
    trueDoorImg = ""
    screen.blit(trueDoorImg, (refX,refY))

def fakeDoor(refX, refY):
    fakeDoorImg = ""
    screen.blit(fakeDoorImg, (refX, refY))

def message(txt, posX, posY):

    text = font.render(txt, True, (255, 255, 255))
    screen.blit(text, (posX*SCALE,posY*SCALE))

def isColliding(x1 , y1 , x2 , y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 45:
        return True
    else:
        return False

def openDoor():
    return False

pygame.init()

spritesheet = pygame.image.load("spritesheet.png")


WIDTH = 512
HEIGHT = 256
SCALE = 2
RESOLUTION = 32
stage = pygame.image.load("stage.png")
stage = pygame.transform.scale(stage, (WIDTH*SCALE, HEIGHT*SCALE))
font = pygame.font.SysFont("Consolas", 20)
screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE),0,32)
timer = pygame.time.Clock()

gameState = "NORMAL"
running = True
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 30
textCounter = str(counter).rjust(3)
exitLeft = randint(0, 1)

playerX = 150*SCALE
playerY = 170*SCALE
speed = 1
playerUp = False
playerDown = False
playerRight = False
playerLeft = False
playerAction = False

while running:
    if gameState == "NORMAL":
        screen.fill((0, 0, 0))
        screen.blit(stage,(0,0))
        if exitLeft == 1:
            pygame.draw.rect(screen, (0, 0, 255), (176*SCALE, 128*SCALE, RESOLUTION*SCALE, RESOLUTION*SCALE), 0)
            pygame.draw.rect(screen, (255, 0, 0), (306*SCALE, 128*SCALE, RESOLUTION*SCALE, RESOLUTION*SCALE), 0)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (176*SCALE, 128*SCALE, RESOLUTION*SCALE, RESOLUTION*SCALE), 0)
            pygame.draw.rect(screen, (0, 0, 255), (306*SCALE, 128*SCALE, RESOLUTION*SCALE, RESOLUTION*SCALE), 0)

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
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
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerLeft = True
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

        if playerX > (WIDTH - RESOLUTION)*SCALE:
            playerX = (WIDTH - RESOLUTION)*SCALE
        if playerX < 0:
            playerX = 0
        if playerY > (HEIGHT - RESOLUTION)*SCALE:
            playerY = (HEIGHT - RESOLUTION)*SCALE
        if playerY < 0:
            playerY = 0

        player(playerX, playerY)
        message(textCounter, WIDTH - 30, 10)
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