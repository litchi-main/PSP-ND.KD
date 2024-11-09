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
        self.surface = self.spriteHidden
        self.rect = self.spriteHidden.get_rect()
        self.rect.center = (x * config.tileX + config.tileX/2, 
                            y * config.tileY + config.tileY/2)

    def changeTile(self, tileType):
        self.tileType = tileType
        self.spriteRevealed = self.spriteSheet.getSpriteByName(tileType)

    def render(self, window):
        window.blit(self.surface, self.rect)
