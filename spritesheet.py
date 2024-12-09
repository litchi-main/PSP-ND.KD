import json
import pygame
import config

class SpriteSheet:
    def __init__(self):
        self.__sheet = pygame.image.load(config.spriteSheet).convert()
        data = open(config.spriteData,"r")
        self.__data = json.loads(data.read())
        data.close()
        
    def getSprite(self, x, y, width, height, Ox, Oy):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.__sheet, (Ox,Oy), (x,y,width,height))
        return sprite

    def getSpriteByName(self, name):
        return self.getSprite(self.__data[name]['x'], 
                              self.__data[name]['y'], 
                              self.__data[name]['width'], 
                              self.__data[name]['height'], 
                              self.__data[name]['Ox'],
                              self.__data[name]['Oy'])