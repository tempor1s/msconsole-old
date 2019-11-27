"""Calendar CLI module"""

__doc__ = """
Usage:
    calendar
    calendar <time>
    calendar -h|--help
    calendar -v|--version
Options:
    <time>  Optional time argument.
    -h --help  Show help screen.
    -v --version  Show version.
"""
__maintainer__ = 'Tasfia Addrita'
__credits__ = ['Ben Lafferty', 'Gary Frederick', 'Tasfia Addrita']
__license__ = 'MIT'

# build in modules
import sys
import os

# external modules
from docopt import docopt


class hello(object):
    def __init__(self, option):
        self.option = option


def say_hello(name):
    return("Hello {}!".format(name))


if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    if arguments['<time>']:
        print(say_hello(arguments['<time>']))
    elif arguments['<hello>']
    elif not len(sys.argv) > 1:
        print(__doc__)
    else:
        print('Not an option check option list --help')
