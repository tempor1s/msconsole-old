from src.checkin import CheckIn
from sys import argv

# Main function that packages everything together
# TODO: Convert all of these functions into a class with a run command.
def main():
    # Get all args excluding script name
    args = argv[1:]

    try:
        # The command that is being passed to msconsole
        command = args[0]

        # check the command
        if command.lower() == 'checkin':
            checkin_command(args)
        elif command.lower() == 'help':
            help_command(args)
        else:
            print('Please enter a valid command.')
        # If no command was provided then print out a list of all the commands
    except IndexError:
        print('Command List:')
        # checkin command
        print('     checkin - Checks you into your Make School class.')
        print('     help - Get more information on how to run a command.')
        exit()

# get more information on a given command
def help_command(args):
    # try to get the command that they pass in
    try:
        command = args[1]

        if command.lower() == 'checkin':
            # TODO: Implement checkin help command
            print(
                'Please add an attendence token after `checkin`. Example: `ms checkin BRAVE`')
            pass
        else:
            print('Please enter a valid command to get help from.')
    except IndexError:
        # TODO: Implement better help command
        print('Please add a command after `help`. Example: `ms help checkin`')
        pass

# command to check you into a MakeSchool class
def checkin_command(args):
    # try to get token passed in
    try:
        token = args[1]
    except IndexError:
        # Tell them the the correct usage.
        print('Please add an attendence token after `checkin`. Example: `ms checkin BRAVE`')
        exit()
    # check the user into their class
    checkin = CheckIn(token)
    checkin.run()


if __name__ == '__main__':
    main()
