import BaseTile

class Mine(BaseTile.BaseTile):
    def interface(self,x,y,spriteSheet):
        super().__init__(x,y,'mine',spriteSheet)
        return self

    def __init__(self):
        pass

    def openTile(self):
        self.revealTile()
        return True