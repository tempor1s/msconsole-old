# For running msconsole through python locally. Mostly for test purposes.
from src.ms import MSConsole
from sys import argv

if __name__ == '__main__':
    # Create an instance of MSConsole and run it
    console = MSConsole(argv)
    console.run()
