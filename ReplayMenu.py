from tkinter import *
import pygame

class ReplayMenu:
    def __init__(self) -> None:
        pass

    def setPositiveResponse(self):
        self.responseGot = True
        self.response = True
        self.replayWindow.quit()
        self.replayWindow.destroy()

    def setNegativeResponse(self):
        self.responseGot = True
        self.response = False
        self.replayWindow.quit()
        self.replayWindow.destroy()


    def main(self, mainMenu):
        pygame.quit()
        self.replayWindow = Toplevel(mainMenu)
        self.replayWindow.wm_attributes('-topmost', 'true')
        Label(self.replayWindow, text = "Play again?").pack(fill = 'x')
        buttonFrame = Frame(self.replayWindow)
        Button(buttonFrame, text = "Yes", command = self.setPositiveResponse).pack(fill = 'x')
        Button(buttonFrame, text = "No", command = self.setNegativeResponse).pack(fill = 'x')
        buttonFrame.pack(fill = 'x')
        self.replayWindow.mainloop()
        return self.response