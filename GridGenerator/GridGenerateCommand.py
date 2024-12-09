from GridGenerator import BaseCommand

class GridGenerateCommand(BaseCommand.BaseCommand):

    def execute(self, params):
        self._receiver.action(params)