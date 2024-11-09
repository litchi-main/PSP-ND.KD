from tkinter import *
from tkinter import messagebox
import config
from abc import ABC, abstractmethod

class Tile:
    @abstractmethod
    def onPressDo(self):
        pass

    def __init__(self, gameGrid, x, y):
        self.hiddenPixel = PhotoImage(width=1, height=1)
        self.clickArea = Button(gameGrid, 
                                width = config.tileX, 
                                height = config.tileX, 
                                command = self.onPressDo, 
                                image = self.hiddenPixel,
                                activebackground = '#000000', 
                                background= 'white')
        self.clickArea.grid(column = x, row = y)

class EmptyTile(Tile):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)

    def onPressDo(self):
        self.clickArea.configure(state = "disabled", relief = "groove")
        messagebox.showerror("xd", "lmao")

class Mine(Tile):
    def __init__(self, grid, x, y, photo):
        super().__init__(grid, x, y)
        self.photo = photo

    def onPressDo(self):
        self.clickArea.configure(relief = "sunken", image = self.photo, command = 0)