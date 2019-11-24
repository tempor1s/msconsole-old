from setuptools import setup, find_packages

description = """
See `github repo <https://github.com/tempor1s/make-checkin>`_ for information.
"""

VERSION = '1.2.4'

setup(
    name='Make Checkin',
    version=VERSION,
    author='Ben Lafferty',
    author_email='benlaugherty@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['checkin=checkin.command_line:main']
    },
    description='A CLI application that allows you to checkin to a MakeSchool class.'
)