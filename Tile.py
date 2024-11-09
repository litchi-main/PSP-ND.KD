from tkinter import *
import config
from abc import ABC, abstractmethod

class Tile:
    @abstractmethod
    def onPressDo(self):
        pass

    def __init__(self, gameGrid, x, y):
        photo = PhotoImage(file = 'resources/Mine.png') #PhotoImage(width = config.tileX, height = config.tileY)
        self.clickArea = Button(gameGrid, width = config.tileX, height= config.tileY command = self.onPressDo)
        self.clickArea.grid(column = x, row = y)

class EmptyTile(Tile):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)

    def onPressDo(self):
        self.clickArea.config(state = "disabled", relief = "groove")

class Mine(Tile):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)

    def onPressDo(self):
        photo = PhotoImage(file = config.minePhoto)
        self.clickArea.configure(state = "disabled", relief = "groove", image = photo)