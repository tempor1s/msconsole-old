import re
username = 'test343!_$&^ffg'
username1 = 'gary123'


def is_valid(string):

    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if(regex.search(string) == None):
        return True

    else:
        return False
