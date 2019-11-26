"""msconsole is a module wrapper for the toolkit suite"""

# built in modules
from sys import argv
import argparse

# external modules

# local modules
from src.checkin import CheckIn

# TODO: convert options to arguments using argparse - DRY
"""Example Arguments

    addArgumentCall('-t', '--title', action='store_true',
                        help="Search JUST the exploit title (Default is description and source code).")
    addArgumentCall('-j', '--json', action='store_true',
                        help='Show result in JSON format.')
    addArgumentCall('-m', '--mirror', action='store_true',
                        help='Mirror (aka copies) search result exploit files to the subdirectory with your search query name.')
    addArgumentCall('-c', '--count', nargs=1, type=int, default=10,
                        help='Search limit. Default 10.')
    if LOCAL_SEARCH_AVAILABLE:
        addArgumentCall('-l', '--local', action='store_true',
                        help='Perform search in the local database instead of searching online.')
        addArgumentCall('-u', '--update', action='store_true',
                        help='Update getsploit.db database. Will be downloaded in the script path.')
"""

# TODO: rename __file__ to fit the command ms (ms.py) - so there aren't any name clashes


class MSConsole(object):
    # TODO: Documentation for this class
    def __init__(self, argv):
        # Get all arguments except for the function name
        self.args = argv[1:]

    def run(self):
        try:
            # The command that is being passed to msconsole
            command = self.args[0]

            # check the command and run a command respectivly
            if command.lower() == 'checkin':
                self._checkin_command()
            elif command.lower() == 'help':
                self._help_command()
            # if their command doesnt any of our current commands.
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
        # check the user into their class by creating an instance of CheckIn and running it.
        checkin = CheckIn(token)
        checkin.run()

    def _help_command(self):
        # try to get the command that they pass in
        try:
            command = self.args[1]

            # check the command against commands we already have
            if command.lower() == 'checkin':
                # TODO: Implement descriptive help checkin command with examples and syntax
                print(
                    'Please add an attendence token after `checkin`. Example: `ms checkin BRAVE`')
                pass
            elif command.lower() == 'help':
                # TODO: Implement descriptive help for help command
                pass
            else:
                print('Please enter a valid command to get help from.')
        except IndexError:
            # TODO: Implement more descriptive help command
            print('Please add a command after `help`. Example: `ms help checkin`')
            pass

def main():
    """Homebrew entry point."""
    # pass command line args into MSConsole class and run it
    console = MSConsole(argv)
    console.run()
