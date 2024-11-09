from tkinter import *
from tkinter import messagebox
import config
from abc import ABC, abstractmethod

class Tile:
    @abstractmethod
    def onPressDo(self):
        pass

    def makeInactive(self, bgColor):
        self.clickArea.config(command = 0, 
                              activebackground = bgColor,

                              bg = bgColor,
                              relief = "groove")

    def __init__(self, gameGrid, x, y):
        self.hiddenPixel = PhotoImage(width=1, height=1)
        self.clickArea = Button(gameGrid, 
                                width = config.tileX, 
                                height = config.tileX, 
                                command = self.onPressDo, 
                                image = self.hiddenPixel,
                                bg = config.tileBG)
        self.clickArea.grid(column = x, row = y)

class EmptyTile(Tile):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)

    def onPressDo(self):
        self.makeInactive(config.tileBG)

class Mine(Tile):
    def __init__(self, grid, x, y, photo):
        super().__init__(grid, x, y)
        self.photo = photo

    def onPressDo(self):
        messagebox.showerror("HA", "YOU LOST")
        self.makeInactive('red')