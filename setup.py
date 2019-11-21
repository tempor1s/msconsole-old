from distutils.core import setup

setup(
    name='Make Checkin',
    version='1.0.0',
    author='Ben Lafferty',
    author_email='benlaugherty@gmail.com',
    packages=['checkin'],
    scripts=['checkin.py'],
    license='LICENSE',
    description='A CLI application that allows you to checkin to a MakeSchool class.',
    long_description=open('README.md').read()
)