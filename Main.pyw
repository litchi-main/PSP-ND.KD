from tkinter import *
from GridGenerator.GridGenerator import GridGenerator
from GridGenerator.GridGenerateCommand import GridGenerateCommand
from GridGenerator.Invoker import Invoker
import config
import Game
import os

class Main:
    def play(self):
        self.__window.withdraw()
        gridGenerator = GridGenerator()
        gridGenerateCommand = GridGenerateCommand(gridGenerator)
        invoker = Invoker()
        invoker.storeCommand(gridGenerateCommand)
        game = Game.Game(invoker)
        game.main(self.__window)
        self.__window.deiconify()

    def __init__(self):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

        self.__window = Tk()
        self.__window.title(config.windowName)
        self.__window.minsize(config.menuWindowX, config.menuWindowY)
        self.__window.resizable(False, False)

        self.__playButton = Button(self.__window, text = "Play", command = self.play)
        self.__playButton.pack(fill = "both", expand = True)

        self.__exitButton = Button(self.__window, text = "Exit", command = self.__window.destroy)
        self.__exitButton.pack(fill = "both", expand = True)

        self.__window.mainloop()

Main()