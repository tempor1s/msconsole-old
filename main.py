from src.checkin import CheckIn

def main():
    import sys
    # Get the first arg from command line
    args = sys.argv[1:3]
    # Get the attendence token from args
    try:
        token = args[0]
    except IndexError:
        print('Please add an attendence token after `checkin`. Example: `python3 main.py BRAVE`')
        exit()
    checkin = CheckIn(token)
    checkin.run()

if __name__ == '__main__':
    main()