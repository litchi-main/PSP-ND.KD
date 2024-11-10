from tkinter import *
import config
import Game

class Menu:
    def play(self):
        self.window.withdraw()
        while True:
            game = Game.Game()
            replay = game.main(self.window)
            if replay == False:
                break
        self.window.deiconify()

    def __init__(self):
        self.window = Tk()
        self.window.title(config.windowName)
        self.window.minsize(config.menuWindowX, config.menuWindowY)
        self.window.resizable(False, False)

        self.playButton = Button(self.window, text = "Play", command = self.play)
        self.playButton.pack(fill = "x")

        self.exitButton = Button(self.window, text = "Exit", command = self.window.destroy)
        self.exitButton.pack(fill = "x")

        self.window.mainloop()

Menu()