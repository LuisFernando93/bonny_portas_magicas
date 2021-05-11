import pygame
import math
from random import randint

def player(playerX, playerY):

    playerImg = pygame.Surface((32, 32))
    screen.blit(playerImg, (playerX, playerY))

def message(txt, posX, posY):

    text = font.render(txt, True, (255, 255, 255))
    screen.blit(text, (posX,posY))

def isColliding(x1 , y1 , x2 , y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < 32:
        return True
    else:
        return False

pygame.init()

WIDTH = 965
HEIGHT = 600
#stage = pygame.image.load("stage.png")
font = pygame.font.SysFont("Consolas", 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

gameState = "NORMAL"
running = True
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 10
textCounter = str(counter).rjust(3)
exitLeft = randint(0, 1)

playerX = 384.0
playerY = 284.0
speed = 0.8
playerUp = False
playerDown = False
playerRight = False
playerLeft = False
playerAction = False

while running:
    if gameState == "NORMAL":
        screen.fill((0, 124, 0))
        #screen.blit(stage,(0,0))
        if exitLeft == 1:
            pygame.draw.rect(screen, (0, 0, 255), (302, 180, 64, 64), 0)
            pygame.draw.rect(screen, (255, 0, 0), (482, 180, 64, 64), 0)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (302, 180, 64, 64), 0)
            pygame.draw.rect(screen, (0, 0, 255), (482, 180, 64, 64), 0)

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

        if playerX > 768:
            playerX = 768
        if playerX < 0:
            playerX = 0
        if playerY > 568:
            playerY = 568
        if playerY < 0:
            playerY = 0

        player(playerX, playerY)
        message(textCounter, 700, 30)
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