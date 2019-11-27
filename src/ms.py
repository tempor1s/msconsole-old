"""ms is a module wrapper for the toolkit suite"""

__doc__ = """
Usage:
    ms
    ms <module> [<args>...]
    ms -h|--help
    ms -v|--version
    ms -l|--list
Options:
    <module>      Optional module argument (name of module)
    -h --help     Show help screen
    -v --version  Show version

Sub-Modules:
    links
"""

__maintainer__ = 'Ben Lafferty'
__credits__ = ['Ben Lafferty', 'Gary Frederick']
__license__ = 'MIT'
__version__ = '2.1.0'

from sys import argv
import argparse

from docopt import docopt, DocoptExit

# for handeling all the modules
from src import modules_handler


class MSConsole(object):
    def __init__(self):
        self.args = docopt(__doc__, version=__version__, options_first=True)

    def run(self):
        # Retrieve the module to execute.
        module_name = self.args.pop('<module>')
        if module_name is None:
            raise DocoptExit()

        module_name = module_name.capitalize()

        # Retrieve the module arguments.
        module_args = self.args.pop('<args>')
        if module_args is None:
            module_args = {}

        # After 'poping' '<module>' and '<args>', what is left in the args dictionary are the global arguments.

        # Retrieve the class from modules_handler
        try:
            module_class = getattr(modules_handler, module_name)
        # if class doesn't exist, print unknown module and docstring
        except AttributeError:
            # TODO: Colors!
            print('Unknown Module \n')
            raise DocoptExit()

        # pass in module_args and args
        module = module_class(module_args, self.args)
        # execute the module
        module.execute()


def main():
    """Entrypoint to run the application."""
    # pass command line args into MSConsole class and run it
    console = MSConsole()
    console.run()
