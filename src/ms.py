"""ms is a module wrapper for the toolkit suite"""

__doc__ = """
Usage:
    ms
    ms <checkin>
    ms <calendar>
    ms <console>
    ms <library>
    ms <link>
    ms -h|--help
    ms -v|--version
Options:
    <checkin>  Optional checkin argument.
    <calendar> Optional calendar argument.
    <console>  Optional console argument.
    <library>  Optional library argument.
    <link>     Optional link argument.
    -h --help  Show help screen.
    -v --version  Show version.
"""

__maintainer__ = 'Ben Lafferty'
__credits__ = ['Ben Lafferty', 'Gary Frederick']
__license__ = 'MIT'
__version__ = '2.1.0'

from sys import argv
import argparse

import docopt

from src.modules.checkin import CheckIn, __doc__ as checkin_doc
from src.modules.calendar import Calender, __doc__ as calendar_doc
from src.modules.links import Links, __doc__ as links_doc
from src.modules.brute import BruteForcer, BruteParser, __doc__ as brute_doc


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
    """Entrypoint to run the application."""
    # pass command line args into MSConsole class and run it
    console = MSConsole(argv)
    console.run()
