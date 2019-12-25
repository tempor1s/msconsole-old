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
    * _login() - logs a user in with credentials
"""

__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# Built-in Python Modules
import sys

# external Python Modules
try:
    from PyInquirer import style_from_dict, Token, prompt
    import requests
    import keyring
except ImportError as e:
    sys.stdout.write(str(e))

# local Python Modules
import src.utils.http


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


def _check_credentials(key):
    if _get_email(key) and _get_password(_get_email(key)):
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
                  
def _login(s, key, email, password):
     """Login to MakeSchool dashboard using email and password."""
        # makeschool login url to post and get from
        login_url = "https://www.makeschool.com/login"
        # get the login HTML
        dashboard = s.get(login_url)

        # check to see if the response is ok
        if dashboard.status_code == 200:
            # parse the HTML returing the dashboard document
            dashboard_html = html.fromstring(dashboard.text)
            # Grab hidden form fileds by looking through HTML XPath
            hidden_inputs = dashboard_html.xpath(
                r'//form//input[@type="hidden"]')
            # inside the form look for name and value fields to get authenticity token
            form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
            # set the form email value
            form['user[email]'] = email
            # set the form password value
            form['user[password]'] = password
            # setup post request to login url with new data inserted into form
            response = s.post(login_url, data=form)
        else:
            # otherwise retry connection to server
            print('\x1b[1;31m' + 'Retrying to connect to server')
            try:
                # HTTP retransmission to same urls
                retransmission(session=s).get(login_url)
            # if there is a connection error request the user to try a new url
            # the url has changed in some way - we have to update
            except ConnectionError:
                print('Bad url request, try a different one by setting login url')
            # catastrophic error, no idea what to do with this just bail
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                print(e)
                sys.exit(1)

        # if the login was successful
        if 'successfully' in response.text:
            # Print that we signed in successfully.
            print('\x1b[1;32m' + 'Signed in successfully.' + '\x1b[0m' + '\n')
            # GraphQL query to get current users name and student email
            query = "{ currentUser {name studentEmail} }"
            # make request to makeschool and drill down to currentUser from data response
            currentUser = graph_query(self.s, query)['data']['currentUser']
            # print the users name and MS email so that they know they logged in successfully
            print('Name: {}'.format(currentUser['name']))
            print('MS Email: {}\n'.format(currentUser['studentEmail']))
        else:
            # the credentials are probably wrong
            print('The credentials entered are incorrect.\n')
            _create_creds()
            _login()
