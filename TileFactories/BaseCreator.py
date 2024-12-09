import abc

class BaseCreator(metaclass = abc.ABCMeta):
    def __init__(self):
        self.product = self._factoryMethod()

    @abc.abstractclassmethod
    def _factoryMethod(self):
        pass

    def Create(self, x,y,spriteSheet):
        return self.product.interface(x,y,spriteSheet)