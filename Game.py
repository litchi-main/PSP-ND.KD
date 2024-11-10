import random
from tkinter import *
from tkinter import messagebox
import pygame
import pygame.locals 
import config
import Tile
import spritesheet
import ReplayMenu

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
        self.mineTrigerred = False

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
                if tile.getTileType() == 'mine':
                    self.mineTrigerred = True
                else :
                    self.emptyTiles.remove(tile)
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
                    return (self.tiles[x][y], x, y)

    def setTile(self, x, y, count, arr, type):
        count -= 1
        self.tiles[x][y].changeTile(type)
        arr.append(self.tiles[x][y])

    def randomizeTiles(self):
        baseTiles = '0', 'mine'
        mineTileCount = config.mineLimit
        emptyTileCount = config.gridSizeX * config.gridSizeY - mineTileCount
        self.mineTiles = []
        self.emptyTiles = []

        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if mineTileCount > 0 and emptyTileCount > 0:
                    if self.tiles[x][y].getTileType() == 'hidden':
                        self.setTile(x, y, emptyTileCount, self.emptyTiles, '0')
                    else:
                        tileType = random.choices(baseTiles,weights = (1.0 / mineTileCount, 1.0 / emptyTileCount))[0]
                        if tileType == 'mine':
                            self.setTile(x, y, mineTileCount, self.mineTiles, 'mine')
                        else:
                            self.setTile(x, y, emptyTileCount, self.emptyTiles, '0')
                elif mineTileCount == 0:
                    self.setTile(x, y, emptyTileCount, self.emptyTiles, '0')
                else :
                    self.setTile(x, y, mineTileCount, self.mineTiles, 'mine')


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

    def showPlayerVictory(self):
        messagebox.showinfo("You won!","You won\nAll empty tiles have been cleared")

    def showPlayerLoss(self):
        for mine in self.mineTiles:
            mine.revealTile()
            mine.render(self.screen)
        messagebox.showinfo("You lost", "You lost\nA mine was triggered")

    def preGameloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

            leftMouseClick = self.checkIsMouseClicked()
            mousePos = pygame.mouse.get_pos()
            if leftMouseClick == True:
                pressedTile = self.markStartingTiles(mousePos)
                self.randomizeTiles()
                self.numerizeEmptyTiles()
                self.revealTile(pressedTile[0],leftMouseClick,mousePos,pressedTile[1],pressedTile[2])
                break

            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.tiles[x][y].render(self.screen)
            pygame.display.update()
            self.fps.tick(60)
            

    def gameloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

            leftMouseClick = self.checkIsMouseClicked()
            mousePos = pygame.mouse.get_pos()
            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.revealTile(self.tiles[x][y], leftMouseClick, mousePos, x, y)
                    self.tiles[x][y].render(self.screen)
            pygame.display.update()
            if not self.emptyTiles:
                self.showPlayerVictory()
                pygame.display.update()
                break
            if self.mineTrigerred == True:
                self.showPlayerLoss()
                pygame.display.update()
                break
            self.fps.tick(60)

    def postGameloop(self, mainMenu):
        self.replayMenu = ReplayMenu.ReplayMenu()
        self.response = self.replayMenu.main(mainMenu)

        while True:
            if pygame.get_init():
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        return False
                    pygame.display.update()
                    self.fps.tick(60)

            if self.response == True:
                return True
            else:
                return False

    def main(self, mainMenu):
        self.generateTiles()
        self.preGameloop()
        if pygame.get_init():
            self.gameloop()
        if pygame.get_init():
            return self.postGameloop(mainMenu)
        if pygame.get_init():
            pygame.quit()
        return False

