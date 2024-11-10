from msilib import sequence
import random
from tkinter import *
import pygame
import pygame.locals 
import config
import Tile
import spritesheet
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.gridSizeX * config.tileX,
                                               config.gridSizeY * config.tileY))
        self.screen.fill(config.gameBG)
        pygame.display.set_caption(config.windowName)
        self.fps = pygame.time.Clock()
        self.spriteSheet = spritesheet.SpriteSheet()
        random.seed()
        self.mouseClicked = False

    def checkIsMouseClicked(self):
        if self.mouseClicked == False:
            if pygame.mouse.get_pressed()[0] == True:
                self.mouseClicked = True
                return True
            else:
                return False
        else:
            if pygame.mouse.get_pressed()[0] == False:
                self.mouseClicked = False
            return False

    def revealTile(self, tile, mouseClick, mousePos, x, y):
        if mouseClick == True:
            if tile.checkIfClicked(mousePos) == True:
                tile.revealTile()
                if tile.getTileType() == '0':
                    
                    for xi in range(x - 1 if x > 0 else 0,x + 2 if x + 2 <= config.gridSizeX else config.gridSizeX):
                        for yi in range(y - 1 if y > 0 else 0,y + 2 if y + 2 <= config.gridSizeY else config.gridSizeY):
                            self.revealTile(self.tiles[xi][yi],True, self.tiles[xi][yi].getClickArea(), xi, yi)

        
    def generateTiles(self):
        self.tiles = []

        for x in range(config.gridSizeX):
            self.tiles.append([])
            for y in range(config.gridSizeY):
                self.tiles[x].append(Tile.Tile(x,y,'0',self.spriteSheet))

    def markStartingTiles(self, mousePos):
        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if self.tiles[x][y].checkIfClicked(mousePos):
                    for xi in range(x - 1 if x > 0 else 0,x + 2 if x + 2 <= config.gridSizeX else config.gridSizeX):
                        for yi in range(y - 1 if y > 0 else 0,y + 2 if y + 2 <= config.gridSizeY else config.gridSizeY):
                            self.tiles[xi][yi].changeTile('hidden')


    def randomizeTiles(self):
        baseTiles = '0', 'mine'
        mineLimit = config.mineLimit
        totalTiles = config.gridSizeX * config.gridSizeY
        emptyTiles = totalTiles - mineLimit

        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if mineLimit > 0 and emptyTiles > 0:
                    if self.tiles[x][y].getTileType() == 'hidden':
                        emptyTiles -= 1
                        self.tiles[x][y].changeTile('0')
                    else:
                        tileType = random.choices(baseTiles,weights = (1.0 / mineLimit, 1.0 / emptyTiles))[0]
                        if tileType == 'mine':
                            mineLimit -= 1
                        else:
                            emptyTiles -= 1
                        self.tiles[x][y].changeTile(tileType)
                elif mineLimit == 0:
                    self.tiles[x][y].changeTile('0')
                else :
                    self.tiles[x][y].changeTile('mine')


    def numerizeEmptyTiles(self):
        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if self.tiles[x][y].getTileType() == '0':
                    count = 0
                    for xi in range(x - 1 if x > 0 else 0,x + 2 if x + 2 <= config.gridSizeX else config.gridSizeX):
                        for yi in range(y - 1 if y > 0 else 0,y + 2 if y + 2 <= config.gridSizeY else config.gridSizeY):
                            if self.tiles[xi][yi].getTileType() == 'mine':
                                count += 1
                    count = str(count)
                    self.tiles[x][y].changeTile(count)

    def preGameloop(self):
        print("pregame")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit() 

            leftMouseClick = self.checkIsMouseClicked()
            mousePos = pygame.mouse.get_pos()
            print(type(self.tiles[0][0].getClickArea()).__name__)
            if leftMouseClick == True:
                self.markStartingTiles(mousePos)
                self.randomizeTiles()
                self.numerizeEmptyTiles()
                break

            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.tiles[x][y].render(self.screen)
            pygame.display.update()
            self.fps.tick(60)
            

    def gameloop(self):
        print("main game")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit() 
                    

            leftMouseClick = self.checkIsMouseClicked()
            mousePos = pygame.mouse.get_pos()
            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.revealTile(self.tiles[x][y], leftMouseClick, mousePos, x, y)
                    self.tiles[x][y].render(self.screen)
            pygame.display.update()
            self.fps.tick(60)

    def main(self):
        self.generateTiles()
        self.preGameloop()

        self.gameloop()

