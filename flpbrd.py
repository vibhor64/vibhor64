from math import trunc
import random 
import sys 
import pygame
from pygame.locals import * 

fps = 32
sw = 289
sh = 511
screen = pygame.display.set_mode((sw, sh))
groundy = sh * 0.8
game_sprites = {}
game_sounds = {}
player = 'gallery/sprites/bird.png'
backgroud = 'gallery/sprites/background.png'
pipe = 'gallery/sprites/pipe.png'

def welcomeScreen():
    playerx = int(sw/5)
    playery = int((sh - game_sprites['player'].get_height())/2)
    messagex = int((sw - game_sprites['message'].get_width())/2)
    messagey = int(sh * 0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else: 
                screen.blit(game_sprites['background'], (0, 0))
                screen.blit(game_sprites['player'], ( playerx, playery ))
                screen.blit(game_sprites['message'], (messagex, messagey ))
                screen.blit(game_sprites['base'], (basex, groundy))
                pygame.display.update()
                FPSCLOCK.tick(fps)

def mainGame():
    score = 0
    playerx = int(sw/5)
    playery = int(sw/2)
    basex = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [
        {'x' : sw + 200, 'y' : newPipe1[0]['y']},
        {'x' : sw + 200 + (sw/2), 'y' : newPipe2[0]['y']}
    ]

    lowerPipes = [
        {'x': sw+200, 'y':newPipe1[1]['y']},
        {'x': sw+200+(sw/2), 'y':newPipe2[1]['y']},
    ]

    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = -1

    playerFlapAccV = -8 # vel while flapping
    playerFlapped = False

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccV
                    playerFlapped = True
                    game_sounds['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = playerx + game_sprites['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + game_sprites['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                game_sounds['point'].play()

        if playerVelY < playerMaxVelY and not playerFlapAccV:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = game_sprites['player'].get_height()
        playery = playery + min(playerVelY, groundy - playerHeight - playery)

        # move pipes to left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # add a new pipe when first one almost exits
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # remove the pipes exiting the screen
        if upperPipes[0]['x'] < - game_sprites['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        
        screen.blit(game_sprites['base'], (basex, groundy))
        screen.blit(game_sprites['base'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0

        for digit in myDigits:
            width += game_sprites['numbers'][digit].get_width()
        Xoffset = (sw - width)/2

        for digit in myDigits:
            screen.blit(game_sprites['numbers'][digit], (Xoffset, sw*0.12))
            Xoffset += game_sprites['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(fps)



def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > groundy - 25 or playery<0:
        game_sounds['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = game_sprites['pipe'][0].get_height()
        if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x'] < game_sprites['pipe'][0].get_width()):
            game_sounds['hit'].play()
            return True
        
    for pipe in lowerPipes:
        pipeHeight = game_sprites['pipe'][1].get_height()
        if (playery + game_sprites['player'].get_height()) > pipe['y'] and abs(playerx - pipe['x'] < game_sprites['pipe'][0].get_width()):
            game_sounds['hit'].play()
            return True

    
    return False




def getRandomPipe():
    pipeHeight = game_sprites['pipe'][0].get_height()
    offset = sh/3
    y2 = offset + random.randrange(0, int(sh - game_sprites['base'].get_height() - 1.2*offset))
    pipeX = sw + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x' : pipeX, 'y' : -y1},
        {'x' : pipeX, 'y' : y2}
        
    ]
    return pipe 



if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird By Vibhor')
    game_sprites['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),

    )

    game_sprites['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    game_sprites['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    game_sprites['pipe'] =(pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(), 180), 
    pygame.image.load(pipe).convert_alpha())
    game_sprites['background'] = pygame.image.load('gallery/sprites/background.png').convert()
    game_sprites['player'] = pygame.image.load('gallery/sprites/bird.png').convert_alpha()
    
    
    
    game_sounds['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    game_sounds['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    game_sounds['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    game_sounds['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    game_sounds['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    while True:
        welcomeScreen()
        mainGame()