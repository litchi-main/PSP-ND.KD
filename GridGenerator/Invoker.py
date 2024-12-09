class Invoker():
    def __init__(self):
        self._commands = []

    def storeCommand(self, command):
        self._commands.append(command)

    def executeCommands(self, params):
        for command in self._commands:
            command.execute(params)