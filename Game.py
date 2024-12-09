from tkinter import *
from tkinter import messagebox
import pygame
import pygame.locals 
import config
import spritesheet
import ReplayMenu
import MouseClickChecker

class Game:
    def __init__(self, gridGenerator):
        self.__tiles = []
        self.__mineTiles = []
        self.__emptyTiles = []
        self.__gridGenerator = gridGenerator

    def startGame(self, test = False):
        pygame.init()
        self.__screen = pygame.display.set_mode((config.gridSizeX * config.tileX,
                                               config.gridSizeY * config.tileY))
        self.__screen.fill(config.gameBG)
        pygame.display.set_caption(config.windowName)
        self.__fps = pygame.time.Clock()
        self.__spriteSheet = spritesheet.SpriteSheet()
        self.__mineTrigerred = False
        self.__gridGenerator.executeCommands([self.__tiles, self.__mineTiles, self.__emptyTiles, self.__spriteSheet, self.__screen, self.__fps, test])
        
    def revealOtherTiles(self, x, y):
        for xi in range(x - 1 if x > 0 else 0,x + 2 if x + 2 <= config.gridSizeX else config.gridSizeX):
            for yi in range(y - 1 if y > 0 else 0,y + 2 if y + 2 <= config.gridSizeY else config.gridSizeY):
                self.revealTile(self.__tiles[xi][yi],True, self.__tiles[xi][yi].getClickArea(), xi, yi)

    def revealTile(self, tile, mouseClick, mousePos, x, y):
        if mouseClick == True and tile.checkIfClicked(mousePos) == True:
            self.__mineTrigerred = tile.openTile()
            if not self.__mineTrigerred:
                self.__emptyTiles.remove(tile)
                if tile.getTileType() == '0':
                    self.revealOtherTiles(x,y)


    def showPlayerVictory(self):
        messagebox.showinfo("You won!","You won\nAll empty tiles have been cleared")

    def showPlayerLoss(self):
        for mine in self.__mineTiles:
            mine.revealTile()
            mine.render(self.__screen)
        messagebox.showinfo("You lost", "You lost\nA mine was triggered")
            
    def getMineCount(self):
        return len(self.__mineTiles)

    def getEmptyTileCount(self):
        return sum([len(row) for row in self.__tiles]) - len(self.__mineTiles)

    def getTiles(self):
        return self.__tiles

    def gameloop(self, test = False):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

            leftMouseClick = MouseClickChecker.MouseClickChecker.checkIsMouseClicked()
            mousePos = pygame.mouse.get_pos()
            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.revealTile(self.__tiles[x][y], leftMouseClick, mousePos, x, y)
                    self.__tiles[x][y].render(self.__screen)
            pygame.display.update()
            if not self.__emptyTiles:
                if test:
                    return True;
                self.showPlayerVictory()
                pygame.display.update()
                break
            if self.__mineTrigerred == True:
                if test:
                    return False
                self.showPlayerLoss()
                pygame.display.update()
                break
            self.__fps.tick(60)

    def postGameloop(self, mainMenu):
        self.__replayMenu = ReplayMenu.ReplayMenu()
        response = self.__replayMenu.main(mainMenu)

        while True:
            if pygame.get_init():
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        return False
                    pygame.display.update()
                    self.__fps.tick(60)

            if response == True:
                return True
            else:
                return False

    def manuallyCloseGame(self):
        if pygame.get_init():
            pygame.quit()

    def main(self, mainMenu, test = False):
        replayResponse = True
        while replayResponse:
            self.startGame(test)
            if pygame.get_init():
                self.gameloop()
            if pygame.get_init():
                replayResponse = self.postGameloop(mainMenu)
            elif pygame.get_init():
                pygame.quit()
            else :
                replayResponse = False