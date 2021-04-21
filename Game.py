import pygame
from random import randint

def player( playerX, playerY):
    playerImg = pygame.Surface((32, 32))
    screen.blit(playerImg, (playerX, playerY))

def message(txt):

    text = fonte.render(txt, True, (255,255,255))
    screen.blit(text, (WIDTH/2,HEIGHT/2))

pygame.init()

WIDTH = 800
HEIGHT = 600
fonte = pygame.font.SysFont("comicsansms", 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

gameState = "NORMAL"
running = True
saidaAEsquerda = randint(0, 1)

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
        screen.fill((0, 255, 0))
        if saidaAEsquerda == 1:
            pygame.draw.rect(screen, (0, 0, 255), (302, 180, 64, 64), 0)
            pygame.draw.rect(screen, (255, 0, 0), (482, 180, 64, 64), 0)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (302, 180, 64, 64), 0)
            pygame.draw.rect(screen, (0, 0, 255), (482, 180, 64, 64), 0)

        for event in pygame.event.get():
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
    elif gameState == "GAME OVER":
        screen.fill((0,0,0))
        message("Voce perdeu!")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.update()