from tkinter import *
import Game
from GridGenerator.GridGenerator import GridGenerator
from GridGenerator.Invoker import Invoker
from GridGenerator.GridGenerateCommand import GridGenerateCommand
import config

class TileGenerationTest:
    def introduceTest():
        print ("Tile generation test")

    def testDisplay():
        gridGenerator = GridGenerator()
        gridGenerateCommand = GridGenerateCommand(gridGenerator)
        invoker = Invoker()
        invoker.storeCommand(gridGenerateCommand)
        for i in range(5):
            game = Game.Game(invoker)
            game.startGame(True)
            game.manuallyCloseGame()
            print ("")
            print ("Test nr. " + str(i + 1) + ": " + str("passed" if game.getMineCount() == config.mineLimit and game.getEmptyTileCount() == config.gridSizeX * config.gridSizeY - config.mineLimit else "failed"))
            print ("Details: MineLimit - " + str(config.mineLimit) + " GameMineCount - " + str(game.getMineCount()))
            print ("Details: EmptyDefault - " + str(config.gridSizeX * config.gridSizeY - config.mineLimit) + " GameEmptyCount - " + str(game.getEmptyTileCount()))
            