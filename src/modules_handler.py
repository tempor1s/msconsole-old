from docopt import docopt

from src.modules.checkin import CheckInModule, __doc__ as checkin_doc
from src.modules.meet import MeetModule, __doc__ as meet_doc
from src.modules.links import LinksModule, __doc__ as links_doc
from src.modules.brute import BruteForcer, BruteParser, __doc__ as brute_doc
from src.modules.library import LibraryModule, __doc__ as library_doc
from src.modules.shell import ShellModule, __doc__ as console_doc


class AbstractModule(object):
    """Base class for the modules"""

    def __init__(self, module_args, global_args):
        """
        Initialize the modules.
        :param module_args: arguments of the module
        :param global_args: arguments of the program
        """
        self.args = docopt(self.__doc__, argv=module_args)
        self.global_args = global_args

    def execute(self):
        """Execute the modules"""
        raise NotImplementedError


class Links(AbstractModule):
    # Links modules docstring
    # TODO: Comments and documentation
    __doc__ = links_doc

    def execute(self):
        print(self.__doc__)
        if self.args['<class_code>']:
            print(self.args['<class_code>'])


class Checkin(AbstractModule):
    # Checkin modules docstring
    # TODO: Comments and documentation
    __doc__ = checkin_doc

    def execute(self):
        if self.args['<token>']:
            checkin = CheckInModule(self.args['<token>'])
            checkin.run()
        else:
            print(self.__doc__)


class Brute(AbstractModule):
    # Brute modules docstring
    # TODO: Comments and documentation
    __doc__ = brute_doc

    def execute(self):
        # TODO: Implement
        print('Not yet implemented! :)')


class Library(AbstractModule):
    # Library modules docstring
    # TODO: Comments and documentation
    __doc__ = library_doc

    def execute(self):
        # TODO: Implement
        print('Not yet implemented! :)')


class Shell(AbstractModule):
    # Shell modules docstring
    # TODO: Comments and documentation
    __doc__ = console_doc

    def execute(self):
        # TODO: Implement
        shell = ShellModule()
        shell.run()


class Meet(AbstractModule):
    # Shell modules docstring
    # TODO: Comments and documentation
    __doc__ = meet_doc

    def execute(self):
        # TODO: Implement
        print('Not yet implemented :)')