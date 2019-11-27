"""Calendar CLI module"""


__doc__ = """
Usage:
    calendar.py
    calendar.py <time>
    calendar.py -h|--help
    calendar.py -v|--version
Options:
    <time>  Optional time argument.
    -h --help  Show help screen.
    -v --version  Show version.
"""
__author__ = 'Tasfia Addrita'  # main contributor
__latest_editor__ = 'Tasfia Addrita'  # last user to edit document
__date__ = 'November 27, 2019'  # last date edited
__version__ = 0.1  # version number

# build in modules
import sys
import os

# external modules
from docopt import docopt
import requests

# class hello(object):
#     def __init__(self, option):
#         self.option = option


# def say_hello(name):
#     return("Hello {}!".format(name))


if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    if arguments['<time>']:
        print(say_hello(arguments['<time>']))
    elif not len(sys.argv) > 1:
        print(__doc__)
    else:
        print('Not an option check option list --help')
