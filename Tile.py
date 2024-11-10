import pygame
import config
from abc import ABC, abstractmethod

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,tileType,spriteSheet):
        super().__init__()
        self.spriteSheet = spriteSheet
        self.tileType = tileType
        self.spriteHidden = self.spriteSheet.getSpriteByName('hidden')
        self.spriteRevealed = self.spriteSheet.getSpriteByName(tileType)
        self.currentSprite = self.spriteHidden
        self.clickArea = self.spriteHidden.get_rect()
        self.clickArea.center = (x * config.tileX + config.tileX/2, 
                            y * config.tileY + config.tileY/2)
        self.isRevealed = False

    def changeTile(self, tileType):
        self.tileType = tileType
        self.spriteRevealed = self.spriteSheet.getSpriteByName(tileType)

    def revealTile(self):
        self.currentSprite = self.spriteRevealed
        self.isRevealed = True

    def checkIfClicked(self, mousePos):
        if self.isRevealed == False:
            if type(mousePos).__name__ == 'tuple':
                return self.clickArea.collidepoint(mousePos)
            elif type(mousePos).__name__ == 'Rect':
                return self.clickArea.colliderect(mousePos)
            else:
                return False
        else:
            return False

    def getTileType(self):
        return self.tileType

    def getClickArea(self):
        return self.clickArea

    def render(self, window):
        window.blit(self.currentSprite, self.clickArea)
