import sys
import pygame
import math
from random import randint


def spriteList(refX0, refY0, nSprites):

    sprites = []
    for i in range(0, nSprites):
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
        if playerImgIndex >= len(playerSpritesLeft)-1:
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
    if npcGoldyImgIndex >= len(npcGoldySpritesLeft)-1:
        npcGoldyImgIndex = 0.0

    if npcLeft == 1:
        goldyImg = npcGoldySpritesRight[int(npcGoldyImgIndex)]
    else:
        goldyImg = npcGoldySpritesLeft[int(npcGoldyImgIndex)]

    screen.blit(goldyImg, (refX*SCALE, refY*SCALE))


def door(refX, refY, openDoor, isOpen, closeDoor):

    global doorIdleImgIndex
    global doorOpenImgIndex
    global openTrue
    global isOpenTrue
    global openFake
    global isOpenFake
    global animationDoorEnd

    if openDoor or isOpen or closeDoor:
        if openDoor:
            doorOpenImgIndex += 0.05
            if doorOpenImgIndex >= len(doorOpenSprites)-1:
                doorOpenImgIndex = len(doorOpenSprites)-1
                if openTrue:
                    openTrue = False
                    isOpenTrue = True
                elif openFake:
                    openFake = False
                    isOpenFake = True
        if closeDoor:
            doorOpenImgIndex -= 0.05
            if doorOpenImgIndex <= 0:
                doorOpenImgIndex = 0
                animationDoorEnd = True
        doorImg = doorOpenSprites[int(doorOpenImgIndex)]
    else:

        doorIdleImgIndex += 0.05
        if doorIdleImgIndex >= len(doorIdleSprites) - 1:
            doorIdleImgIndex = 0.0
        doorImg = doorIdleSprites[int(doorIdleImgIndex)]

    screen.blit(doorImg, (refX*SCALE, refY*SCALE))


def message(txt, posX, posY):

    text = font.render(txt, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (posX*SCALE, posY*SCALE)
    screen.blit(text, textRect)


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
        if exitLeft == 1:
            i = randint(0, len(hintLeft) - 1)
            textHint = hintLeft[i]
            hintLeft.remove(textHint)
            hintShowed = True
        else:
            i = randint(0, len(hintRight) - 1)
            textHint = hintRight[i]
            hintRight.remove(textHint)
            hintShowed = True


def nextLevel():

    global level
    global gameState

    level += 1
    if level > MAX_LEVEL:
        changeGameStateAndSoundtrack("VICTORY")

    newLevel(level)


def newGame():

    global level
    global hintRight
    global hintLeft
    global runningCounter

    runningCounter = True
    level = 1
    hintRight = databaseRight
    hintLeft = databaseLeft
    newLevel(level)


def newLevel(refLevel):

    global textLevel
    global playerX
    global playerY
    global stage
    global counter
    global textCounter
    global runningCounter
    global exitLeft
    global npcLeft
    global hintShowed
    global playerImgIndex
    global npcGoldyImgIndex
    global doorIdleImgIndex
    global playerUp
    global playerDown
    global playerRight
    global playerLeft
    global playerAction
    global playerLookLeft

    textLevel = "Sala" + str(refLevel).rjust(2)

    playerX = playerX0
    playerY = playerY0
    playerUp = False
    playerDown = False
    playerRight = False
    playerLeft = False
    playerAction = False
    playerLookLeft = True
    playerImgIndex = 0.0
    npcGoldyImgIndex = 0.0
    doorIdleImgIndex = 0.0
    counter = 60 - (refLevel - 1) * COUNTER_REDUCTION
    if counter < COUNTER_MIN:
        counter = COUNTER_MIN
    runningCounter = True
    textCounter = str(counter).rjust(3)
    exitLeft = randint(0, 1)
    npcLeft = randint(0, 1)
    hintShowed = False


def changeGameStateAndSoundtrack(refGameState):

    global gameState

    gameState = refGameState
    playSoundtrack(refGameState)


def playSoundtrack(refGameState):

    for sound in soundtrack:
        sound.stop()

    if refGameState == "MENU":
        soundtrack[0].play(-1)
    elif refGameState == "GAME":
        soundtrack[1].play(-1)
    elif refGameState == "GAME OVER":
        sfx[0].play(0)
        soundtrack[2].play(-1)
    elif refGameState == "VICTORY":
        soundtrack[3].play(-1)


pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Bonny e as Portas Mágicas")
pygame.display.set_icon(pygame.image.load("res/image/icon.png"))

spritesheet = pygame.image.load("res/image/spritesheet.png")

WIDTH = 160
HEIGHT = 96
SCALE = 6
RESOLUTION = 32

databaseLeft = ["Ao começar um jogo de xadrez, a rainha fica à esquerda ou à direita do rei?",
                "Para que lado a torre de pisa se inclina?",
                "Qual hemisfério do cérebro  atua no raciocínio lógico?",
                "Qual lado começamos a leitura de um livro?",
                "Se você move seu braço direito, que lado do seu cérebro é ativado?",
                "O oposto de direita é esquerda, a porta é o oposto do oposto de esquerda.",
                "Em Resident Evil 7 Ethan Winters perde qual mão?",
                "A pílula azul em matrix, da ignorância abençoada, está em qual mão?",
                "Na saga Harry Potter, qual olho Alastor Moody, Olho-Tonto, perdeu?",
                "Rachel Amber, de Life is strange, usa o brinco de penas em qual orelha?",
                "Não quero ajudar você dessa vez. Boa sorte!",
                "Hidari",
                "Em 'Alice no país das maravilhas', qual dos olhos do Chapeleiro Maluco é verde?",
                "Zuko, de 'Avatar', tem qual lado do rosto queimado?",
                "She-ra ergue sua espada com qual das mãos?",
                "Gauche"]

databaseRight = ["Em qual mão a estátua da liberdade está segurando a tocha?",
                 "Qual hemisfério do cérebro humano atua na parte esquerda do corpo?",
                 "Qual hemisfério do cérebro atua na função da imaginação?",
                 "Alemanha fica à direita ou à esquerda da Bélgica?",
                 "O Sol nasce em qual direção?",
                 "Em qual dos olhos fica a cicatriz do protagonista de God of War?",
                 "Qual a mão que Anakin Skywalker perde em Star Wars Ep 2?",
                 "De qual lado começamos a ler um mangá?",
                 "Que mão é colocada no peito durante o hino?",
                 "Qual a última tecla direcional do código Konami?",
                 "Não quero ajudar você dessa vez. Boa sorte!",
                 "Migi",
                 "Donna Beneviento, de 'Resident Evil', tem qual lado do rosto infectado?",
                 "Qual a posição da espada na estátua da Mãe Rússia, em Moscou?",
                 "Finn, de 'Hora da Aventura' perde qual braço",
                 "Droite"]

hintLeft = []
hintRight = []

soundtrack = [pygame.mixer.Sound("res/audio/menu.mp3"), pygame.mixer.Sound("res/audio/level.mp3"),
              pygame.mixer.Sound("res/audio/gameover.mp3"), pygame.mixer.Sound("res/audio/happyend.mp3")]

sfx = [pygame.mixer.Sound("res/audio/scream.mp3")]

stage = pygame.image.load("res/image/stage.png")
stage = pygame.transform.scale(stage, (WIDTH*SCALE, HEIGHT*SCALE))
menu = pygame.image.load("res/image/menu.png")
menu = pygame.transform.scale(menu, (WIDTH*SCALE, HEIGHT*SCALE))
gameOver = pygame.image.load("res/image/gameover.png")
gameOver = pygame.transform.scale(gameOver, (WIDTH*SCALE, HEIGHT*SCALE))
credit = pygame.image.load("res/image/credits.png")
credit = pygame.transform.scale(credit, (WIDTH*SCALE, HEIGHT*SCALE))
font = pygame.font.SysFont("Consolas", 20)
screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE), 0, 32)
timer = pygame.time.Clock()
level = 1
MAX_LEVEL = 15
textLevel = "Sala" + str(level).rjust(2)

gameState = "MENU"
running = True
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 60
COUNTER_REDUCTION = 4
COUNTER_MIN = 5
textCounter = str(counter).rjust(3)
exitLeft = randint(0, 1)
npcLeft = randint(0, 1)

selectedTrueDoor = False
selectedFakeDoor = False

openTrue = False
openFake = False

isOpenTrue = False
isOpenFake = False

closeTrue = False
closeFake = False

animationDoorEnd = False

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
doorOpenSprites = spriteList(0, 96, 9)
doorIdleImgIndex = 0.0
doorOpenImgIndex = 0.0

doorPosXLeft = 41
doorPosXRight = 85
doorPosY = 33

trueDoorX = doorPosXLeft
trueDoorY = doorPosY

fakeDoorX = doorPosXRight
fakeDoorY = doorPosY

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

playSoundtrack(gameState)

while running:
    if gameState == "MENU":

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
                        newGame()
                        changeGameStateAndSoundtrack("GAME")
                    elif arrowY == 32:
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.blit(menu, (0, 0))
        arrow(arrowX, arrowY)

    elif gameState == "GAME":
        arrowImgIndex = 0.0

        if exitLeft == 1:
            trueDoorX = doorPosXLeft
            fakeDoorX = doorPosXRight
        else:
            trueDoorX = doorPosXRight
            fakeDoorX = doorPosXLeft

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
                    changeGameStateAndSoundtrack("GAME OVER")
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
                selectedTrueDoor = True
                gameState = "ANIMATION DOOR"
            elif isColliding(playerX, playerY, fakeDoorX, fakeDoorY):
                selectedFakeDoor = True
                gameState = "ANIMATION DOOR"
            elif isColliding(playerX, playerY, goldyX, goldyY):
                showHint()

        screen.blit(stage, (0, 0))
        door(trueDoorX, trueDoorY, openTrue, isOpenTrue, closeTrue)
        door(fakeDoorX, fakeDoorY, openFake, isOpenFake, closeFake)
        npcGoldy(goldyX, goldyY)
        player(playerX, playerY)

        message(textLevel, 10, 5)
        message(textCounter, WIDTH - 20, 5)

        if hintShowed:
            message(textHint, WIDTH/2, HEIGHT - 5)

    elif gameState == "ANIMATION DOOR":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        runningCounter = False
        doorIdleImgIndex = 0.0
        if selectedTrueDoor:
            playerX = trueDoorX
            playerY = trueDoorY + 10
            playerImgIndex = 0.0
            selectedTrueDoor = False
            openTrue = True

        if selectedFakeDoor:
            playerX = fakeDoorX
            playerY = fakeDoorY + 10
            playerImgIndex = 0.0
            selectedFakeDoor = False
            openFake = True

        if isOpenTrue or isOpenFake:
            if playerY > doorPosY:
                playerY -= speed
                playerMoved = True
            elif playerY <= doorPosY:
                if isOpenTrue:
                    isOpenTrue = False
                    closeTrue = True
                elif isOpenFake:
                    isOpenFake = False
                    closeFake = True

        if animationDoorEnd:
            if closeTrue:
                animationDoorEnd = False
                closeTrue = False
                gameState = "GAME"
                nextLevel()
            elif closeFake:
                animationDoorEnd = False
                closeFake = False
                changeGameStateAndSoundtrack("GAME OVER")

        screen.blit(stage, (0, 0))
        door(trueDoorX, trueDoorY, openTrue, isOpenTrue, closeTrue)
        door(fakeDoorX, fakeDoorY, openFake, isOpenFake, closeFake)
        npcGoldy(goldyX, goldyY)
        if playerY > doorPosY:
            player(playerX, playerY)

    elif gameState == "GAME OVER":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    changeGameStateAndSoundtrack("MENU")
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(gameOver, (0, 0))
        arrow(32, 50)

    elif gameState == "VICTORY":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    changeGameStateAndSoundtrack("MENU")
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(credit, (0, 0))
        arrow(33, 63)

    pygame.display.update()

pygame.display.quit()
