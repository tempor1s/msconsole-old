description = """
See `github repo <https://github.com/tempor1s/make-checkin>`_ for information.
"""

__version__ = '2.1.2'
__maintainer__ = 'Ben Lafferty'
__credits__ = ['Ben Lafferty', 'Gary Frederick']
__license__ = 'MIT'

# Imports for setup to work :)
from setuptools import setup, find_packages

setup(
    name='Make Checkin',
    version=__version__,
    author='Ben Lafferty',
    author_email='benlaugherty@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ms=src.ms:main']
    },
    description="Suite of tools that makes your MakeSchool life easier!"
)
