import json
import pygame
import config

class SpriteSheet:
    def __init__(self):
        self.sheet = pygame.image.load(config.spriteSheet).convert()
        data = open(config.spriteData,"r")
        self.data = json.loads(data.read())
        data.close()
        
    def getSprite(self, x, y, width, height, Ox, Oy):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet, (Ox,Oy), (x,y,width,height))
        return sprite

    def getSpriteByName(self, name):
        return self.getSprite(self.data[name]['x'], 
                              self.data[name]['y'], 
                              self.data[name]['width'], 
                              self.data[name]['height'], 
                              self.data[name]['Ox'],
                              self.data[name]['Oy'])