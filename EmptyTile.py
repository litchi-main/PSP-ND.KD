import BaseTile

class EmptyTile(BaseTile.BaseTile):
    def interface (self,x,y,spriteSheet):
        super().__init__(x,y,'0',spriteSheet)
        return self

    def __init__(self):
        pass

    def openTile(self):
        self.revealTile()
        return False