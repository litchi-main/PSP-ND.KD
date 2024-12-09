import pygame
from TileFactories import EmptyTileFactory
from TileFactories import tempTileFactory
from TileFactories import MineFactory
import config
import MouseClickChecker
import random
from NameGetter import NameGetter

class GridGenerator():
    def generateTempTiles(self):
        for x in range(config.gridSizeX):
            self.__tiles.append([])
            for y in range(config.gridSizeY):
                self.__tiles[x].append(tempTileFactory.tempTileFactory().Create(x,y,self.__spriteSheet))

    def markTilesAsHidden(self, x, y):
        for xi in range(x - 1 if x > 0 else 0,x + 2 if x + 2 <= config.gridSizeX else config.gridSizeX):
            for yi in range(y - 1 if y > 0 else 0,y + 2 if y + 2 <= config.gridSizeY else config.gridSizeY):
                dummyCounter = [1]
                self.setTile(xi,yi,dummyCounter,self.__emptyTiles,self.generateEmptyTile)
                self.__startingTileCount += 1
        return (self.__tiles[x][y], x, y)

    def markStartingTiles(self, mousePos):
        self.__startingTileCount = 0
        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if self.__tiles[x][y].checkIfClicked(mousePos):
                    return self.markTilesAsHidden(x,y)


    def generateEmptyTile(self, x, y):
        self.__tiles[x][y] = EmptyTileFactory.EmptyTileFactory().Create(x,y,self.__spriteSheet)

    def generateMine(self, x, y):
        self.__tiles[x][y] = MineFactory.MineFactory().Create(x,y,self.__spriteSheet)

    def setTile(self, x, y, count, arr, tileGenerator):
        count[0] -= 1
        tileGenerator(x,y)
        arr.append(self.__tiles[x][y])

    def setTileToMine(self, x, y):
        self.setTile(x, y, self.__mineTileCount, self.__mineTiles, self.generateMine)

    def setTileToEmpty(self, x, y):
        self.setTile(x, y, self.__emptyTileCount, self.__emptyTiles, self.generateEmptyTile)

    def randomizeOneTile(self, baseTiles, x, y):
        tileType = random.choices(baseTiles, weights = (1.0 / self.__mineTileCount[0], 1.0 / self.__emptyTileCount[0]))[0]
        if tileType == 'mine':
            self.setTileToMine(x, y)
        else:
            self.setTileToEmpty(x, y)

    def randomizeTiles(self):
        baseTiles = '0', 'mine'
        self.__mineTileCount = [config.mineLimit]
        self.__emptyTileCount = [config.gridSizeX * config.gridSizeY - self.__mineTileCount[0] - self.__startingTileCount]

        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if NameGetter.getName(self.__tiles[x][y]) == config.EmptyName:
                    pass
                elif self.__mineTileCount[0] > 0 and self.__emptyTileCount[0] > 0:
                    self.randomizeOneTile(baseTiles, x, y)
                elif self.__mineTileCount[0] != 0:
                    self.setTileToMine(x, y)
                else :
                    self.setTileToEmpty(x, y)

                    
    def numerizeTile(self, x, y):
        count = 0
        for xi in range(x - 1 if x > 0 else 0,x + 2 if x + 2 <= config.gridSizeX else config.gridSizeX):
            for yi in range(y - 1 if y > 0 else 0,y + 2 if y + 2 <= config.gridSizeY else config.gridSizeY):
                if NameGetter.getName(self.__tiles[xi][yi]) == config.MineName:
                    count += 1
        count = str(count)
        self.__tiles[x][y].changeTile(count)

    def numerizeEmptyTiles(self):
        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                if NameGetter.getName(self.__tiles[x][y]) == config.EmptyName:
                    self.numerizeTile(x, y)


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


    def linkTilesToGame(self, gameAllTiles, gameMineTiles, gameEmptyTiles):
        self.__tiles = gameAllTiles
        self.__mineTiles = gameMineTiles
        self.__emptyTiles = gameEmptyTiles

    def clearTiles(self):
        self.__tiles.clear()
        self.__mineTiles.clear()
        self.__emptyTiles.clear()

    def action(self, params):
        random.seed()
        self.linkTilesToGame(params[0], params[1], params[2])
        self.clearTiles()

        self.__spriteSheet = params[3]
        self.generateTempTiles()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    return

            leftMouseClick = MouseClickChecker.MouseClickChecker.checkIsMouseClicked()
            mousePos = pygame.mouse.get_pos()
            if params[6] == True:
                leftMouseClick = True
                mousePos = (0, 0)
            if leftMouseClick == True or params[6] == True:
                pressedTile = self.markStartingTiles(mousePos)
                self.randomizeTiles()
                self.numerizeEmptyTiles()
                self.revealTile(pressedTile[0],leftMouseClick,mousePos,pressedTile[1],pressedTile[2])
                break

            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.__tiles[x][y].render(params[4])
            pygame.display.update()
            params[5].tick(60)