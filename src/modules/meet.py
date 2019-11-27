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


class Meet(object):
    def __init__(self):
        # TODO: implement this :)
        pass
    
    def run(self):
        pass
