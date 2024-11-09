from tkinter import *
import pygame 
import config
import Tile
import spritesheet

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.gridSizeX * config.tileX,
                                               config.gridSizeY * config.tileY))
        self.screen.fill(config.gameBG)
        pygame.display.set_caption(config.windowName)
        self.fps = pygame.time.Clock()
        self.spriteSheet = spritesheet.SpriteSheet()

        
    def main(self):
        self.tiles = []
        for x in range(config.gridSizeX):
            self.tiles.append([])
            for y in range(config.gridSizeY):
                self.tiles[x].append(Tile.Tile(x,y,'empty',self.spriteSheet))
        while True:
            print("I LIVE")
            for x in range(config.gridSizeX):
                for y in range(config.gridSizeY):
                    self.tiles[x][y].render(self.screen)
            pygame.display.update()
            self.fps.tick(60)