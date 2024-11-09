from tkinter import *
import config
import Tile

class Game:
    def closeGame(self):
        geometry = self.window.winfo_geometry().split("+")
        self.parent.geometry("0x0+" + geometry[1] + "+" + geometry[2])
        self.parent.deiconify()
        self.window.destroy()

    def createGameGrid(self):
        self.gameGrid = Frame(self.window)
        self.minePhoto = PhotoImage(file = config.minePhoto)
        for x in range(config.gridSizeX):
            for y in range(config.gridSizeY):
                Tile.Mine(self.gameGrid, x, y, self.minePhoto)
        self.gameGrid.pack()

    def __init__(self, parentWindow):
        self.parent = parentWindow
        self.window = Toplevel(self.parent)
        #self.window.minsize(config.gridSizeX * config.tileX, config.gridSizeY * config.tileY)
        self.window.resizable(False,False)
        self.parent.withdraw()
        self.window.protocol(name = "WM_DELETE_WINDOW", func = self.closeGame)

        self.createGameGrid()

        self.window.mainloop()