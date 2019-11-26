from src.checkin import CheckIn

def main():
    import sys
    # Get the first arg from command line
    args = sys.argv[1:3]
    # Get the attendence token from args
    try:
        token = args[0]
    except IndexError:
        print('Please add an attendence token after `checkin`. Example: `checkin BRAVE`')
        exit()
    user = CheckIn(token)
    user.run()

if __name__ == '__main__':
    main()