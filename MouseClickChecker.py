import pygame

class MouseClickChecker:

    @staticmethod
    def checkIsMouseClicked():
        if not hasattr(MouseClickChecker.checkIsMouseClicked, "mouseClicked"):
            mouseClicked = False

        if mouseClicked == False:
            if pygame.mouse.get_pressed()[0] == True:
                mouseClicked = True
                return True
            else:
                return False
        else:
            if pygame.mouse.get_pressed()[0] == False:
                mouseClicked = False
            return False

