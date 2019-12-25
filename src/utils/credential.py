"""
System wide credentials functionality

These modules accepts user credentials on first use. Depending on your os
the credentials are stored in the proper credentials directory and
encrypted with the users native os password encryption algorithm.

This script requires that `keyring` be installed within the Python
environment you are running this script in.

If imported into another file the module contains the following
functions:

    * _check_credentials - checks if the credentials already exists
    * _create_creds - creates email and password in keychain
    * _set_password - stores passowrd to keychain
    * _set_email - stores email to keychain
    * _get_password - gets password from keychain
    * _get_email - gets username from keychain
"""

__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# Built-in Python Modules
import sys

# external Python Modules
try:
    from PyInquirer import style_from_dict, Token, prompt
    import keyring
except ImportError as e:
    sys.stdout.write(str(e))

# local Python Modules


def _set_password(username, pw):
    """
    Sets the password to the keychain
    """
    keyring.set_password('mspass', username, pw)


def _set_email(key, email):
    """
    Sets the email to the keychain
    """
    keyring.set_password('msemail', key, email)


def _get_password(email):
    """
    gets the password from the keychain
    """
    keyring.get_password('mspass', email)


def _get_email(key):
    """
    gets the eamil from the keychain
    """
    keyring.get_password('msemail', key)


def _check_credentials(key, email):
    if _get_email(key) and _get_password(email):
            return True
        # else the password keychain doesn't exist so lets set it
        else:
           _create_creds(key)


def _create_creds(key):
    creds = [
        {
            'type': 'input',
            'name': 'email',
            'message': 'What is your email'
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'What is your password'
        }
    ]
    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })
    new_credentials = prompt(creds, style=style)
    try:
        email = new_credentials['email']
        password = new_credentials['password']
        _set_email(key, email)
        _set_password(email, password)
        print('\x1b[1;32m' + "Password stored successfully." +  # green
                  '\x1b[0m')
    except keyring.errors.PasswordSetError as error:
        sys.stdout.write(str(error))
        print('\x1b[1;31m' + "Failed to store password." +  # red
                  '\x1b[0m')


