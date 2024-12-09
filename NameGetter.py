class NameGetter():
    def __init__(self):
        pass

    @staticmethod
    def getName(someObject):
        return someObject.__class__.__name__