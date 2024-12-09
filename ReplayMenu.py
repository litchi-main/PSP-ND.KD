from tkinter import *
import pygame

class ReplayMenu:
    def __init__(self) -> None:
        pass

    def setPositiveResponse(self):
        self.__response = True
        self.__replayWindow.quit()
        self.__replayWindow.destroy()

    def setNegativeResponse(self):
        self.__response = False
        self.__replayWindow.quit()
        self.__replayWindow.destroy()

    def main(self, mainMenu):
        pygame.quit()
        self.__replayWindow = Toplevel(mainMenu)
        self.__replayWindow.wm_attributes('-topmost', 'true')
        self.__replayWindow.protocol("WM_DELETE_WINDOW", self.setNegativeResponse)
        Label(self.__replayWindow, text = "Play again?").pack(fill = 'x')
        buttonFrame = Frame(self.__replayWindow)
        Button(buttonFrame, text = "Yes", command = self.setPositiveResponse).pack(fill = 'x')
        Button(buttonFrame, text = "No", command = self.setNegativeResponse).pack(fill = 'x')
        buttonFrame.pack(fill = 'x')
        self.__replayWindow.mainloop()
        return self.__response