import abc

class BaseCommand(metaclass=abc.ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractclassmethod
    def execute(self, params):
        pass