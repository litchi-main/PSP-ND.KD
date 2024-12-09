from tkinter import *
import Game
from GridGenerator.GridGenerator import GridGenerator
from GridGenerator.Invoker import Invoker
from GridGenerator.GridGenerateCommand import GridGenerateCommand
import config
from NameGetter import NameGetter

class WinConditionTest:
    def introduceTest():
        print("Win Condition Test")

    def testDisplay():
        gridGenerator = GridGenerator()
        gridGenerateCommand = GridGenerateCommand(gridGenerator)
        invoker = Invoker()
        invoker.storeCommand(gridGenerateCommand)
        for i in range(5):
            game = Game.Game(invoker)
            game.startGame(True)
            for row in game.getTiles():
                for tile in row:
                    if NameGetter.getName(tile) == config.EmptyName:
                        game.revealTile(tile,True,tile.getClickArea(),tile.getPos()[0], tile.getPos()[1])
            hasWon = game.gameloop(True)
            game.manuallyCloseGame()
            print("")
            print ("Test nr. " + str(i + 1) + ": " + str("passed" if hasWon else "failed"))
            print ("Details: CPU has " + str("Won" if hasWon else "Lost") + " the game")
            
