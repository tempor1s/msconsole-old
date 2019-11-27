"""Meet CLI module"""

__doc__ = """
This Module allows the user to check what conference rooms are
available at given time.

Usage:
    meet
    meet <time>
    meet -h|--help
    meet -v|--version
Options:
    <time>  Optional time argument.
    -h --help  Show help screen.
    -v --version  Show version.
"""
__maintainer__ = 'Tasfia Addrita'
__credits__ = ['Ben Lafferty', 'Gary Frederick', 'Tasfia Addrita']
__license__ = 'MIT'
__version__ = '1.0.0'

# build in modules
import sys
import os

# external modules
from docopt import docopt
import requests


# class hello(object):
#     def __init__(self, option):
#         self.option = option


class Meet:
    def __init__(self):
        # TODO: implement this :)
        pass


def say_hello(name):
    return("Hello {}!".format(name))


if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    if arguments['<time>']:
        print(say_hello(arguments['<time>']))
    elif arguments['<hello>']:
        pass
    elif not len(sys.argv) > 1:
        print(__doc__)
    else:
        print('Not an option check option list --help')
