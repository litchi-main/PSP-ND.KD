import pygame
import config
from abc import ABC, abstractmethod

class BaseTile(ABC, pygame.sprite.Sprite): 
    def __init__(self,x,y,tileType,spriteSheet):
        super().__init__()
        self._spriteSheet = spriteSheet
        self._tileType = tileType
        self._spriteHidden = self._spriteSheet.getSpriteByName('hidden')
        self._spriteRevealed = self._spriteSheet.getSpriteByName(tileType)
        self._currentSprite = self._spriteHidden
        self._clickArea = self._spriteHidden.get_rect()
        self._clickArea.center = (x * config.tileX + config.tileX/2, 
                            y * config.tileY + config.tileY/2)
        self._isRevealed = False
        self._pos = (x, y)

    def changeTile(self, tileType):
        self._tileType = tileType
        self._spriteRevealed = self._spriteSheet.getSpriteByName(tileType)

    def revealTile(self):
        self._currentSprite = self._spriteRevealed
        self._isRevealed = True

    @abstractmethod
    def openTile(self):
        pass

    def checkIfClicked(self, mousePos):
        if self._isRevealed == False:
            if type(mousePos).__name__ == 'tuple':
                return self._clickArea.collidepoint(mousePos)
            elif type(mousePos).__name__ == 'Rect':
                return self._clickArea.colliderect(mousePos)
            else:
                return False
        else:
            return False

    def getTileType(self):
        return self._tileType

    def getClickArea(self):
        return self._clickArea

    def isRevealed(self):
        return self._isRevealed

    def getPos(self):
        return self._pos

    def render(self, window):
        window.blit(self._currentSprite, self._clickArea)
