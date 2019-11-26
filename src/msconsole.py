from src.checkin import CheckIn
from sys import argv


class MSConsole(object):
    def __init__(self, argv):
        # Get all arguments except for the function name
        self.args = argv[1:]

    def run(self):
        try:
            # The command that is being passed to msconsole
            command = self.args[0]

            # check the command
            if command.lower() == 'checkin':
                self._checkin_command()
            elif command.lower() == 'help':
                self._help_command()
            else:
                print('Please enter a valid command.')
            # If no command was provided then print out a list of all the commands
        except IndexError:
            print('Command List:')
            # checkin command
            print('     checkin - Checks you into your Make School class.')
            print('     help - Get more information on how to run a command.')
            exit()

    def _checkin_command(self):
        try:
            token = self.args[1]
        except IndexError:
            # Tell them the the correct usage.
            print(
                'Please add an attendence token after `checkin`. Example: `ms checkin BRAVE`')
            exit()
        # check the user into their class
        checkin = CheckIn(token)
        checkin.run()

    def _help_command(self):
        # try to get the command that they pass in
        try:
            command = self.args[1]

            if command.lower() == 'checkin':
                # TODO: Implement checkin help command
                print(
                    'Please add an attendence token after `checkin`. Example: `ms checkin BRAVE`')
                pass
            else:
                print('Please enter a valid command to get help from.')
        except IndexError:
            # TODO: Implement better help command
            print('Please add a command after `help`. Example: `ms help checkin`')
            pass

# For homebrew
def main():
    # pass command line args into MSConsole class
    console = MSConsole(argv)
    # run the command
    console.run()