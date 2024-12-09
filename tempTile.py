from sqlite3 import InterfaceError
import BaseTile

class tempTile(BaseTile.BaseTile):
    name = "tempTile"

    def interface (self,x,y,spriteSheet):
        super().__init__(x,y,'0',spriteSheet)
        return self

    def __init__(self):
        pass

    def openTile(self):
        pass