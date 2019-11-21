#!/usr/bin/env python3

"""Checkin.py

This Module allows the user checkin to their class from the
command line.

It is assumed that the first argument enterd in the CLI
is a valid class token.

This tool accepts user credentials on first use. Depending on your os
the credentials are stored in the proper credentials directory and 
encrypted with the users native os password encryption algorithm.

This script requires that `requests` and `lxml` be installed within the Python
environment you are running this script in.

If imported into another file the module contains the following
functions:

    * requests_retry_session - returns the column headers of the file
    * credentials - the main function of the script
    * login - given a credentials file logs a user in thorugh url (https://makeschool.com)
    * checkin - 
    * _check_banner_message -
    * _get_keychain - 
    * _encypt - 

"""
import os
import re
import sys
import requests
from lxml import html, etree
from getpass import getpass
from platform import system
from requests.adapters import HTTPAdapter  # import HTTPAdapter module
from requests.packages.urllib3.util.retry import Retry  # import Retry module


class CheckIn(object):
    """CheckIn is a class that allows you to checkin to your MakeShool classes using a CLI"""

    def __init__(self, token):
        """ The constructor for the CheckIn class

        :sparam token: MakeSchool attendance token
            :type: string
        :attribute email:
            :type: string
        :attribute password:
            :type: string
        :attribute s:
            :type: Requests Session Object
        :creds_path:
            :type: string
        """
        self.email = None
        self.password = None
        self.token = token
        self.s = requests.Session()  # masters/PHD student named this variable
        self.creds_path = self._get_keychain() + 'creds.txt'
        self.checkin()

    def requests_retry_session(self, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
        """Performs HTTP/HTTPS GET retransmission request.

        :param retries: URL path for the request. Should begin with a slash.
            :type: int
        :param backoff_factor: HTTP GET parameters.
            :type: float
        :param status_forcelist: The time of the first request (None if no
            retries have occurred).
            :type: tuple(int)
        :param session: The time of the first request (None if no
            retries have occurred).
            :type: Request Session Object
        """
        session = self.s
        retry = Retry(
            total=retries,  # retry limit
            read=retries,  # retry limit again
            connect=retries,  # retry limit andddd again
            backoff_factor=backoff_factor,  # wait time
            status_forcelist=status_forcelist,  # status code auto retry list
        )
        adapter = HTTPAdapter(max_retries=retry)  # start reconnection
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def credentials(self):
        """Performs HTTP/HTTPS GET retransmission request.

        :param retries: URL path for the request. Should begin with a slash.
            :type: int
        :param backoff_factor: HTTP GET parameters.
            :type: float
        :param status_forcelist: The time of the first request (None if no
            retries have occurred).
            :type: tuple(int)
        :param session: The time of the first request (None if no
            retries have occurred).
            :type: Request Session Object
        """
        if os.path.exists(self.creds_path):
            # if the the file exists open it in read only mode and set the credentials
            with open(self.creds_path, 'r') as f:
                # read email and password from file into a list
                lines = f.read().split('\n')
                self.email = lines[0]
                self.password = lines[1]
        else:
            # create a new file
            with open(self.creds_path, 'a+') as f:
                # get the email and password from the user
                email = input(
                    'Enter Makeschool login email (we don\'t store your email or password on a server): ')
                password = getpass('Password: ')
                # set email and password properties
                self.email = email
                self.password = password
                # write the email and the password to the creds.txt file for later use
                f.write(f'{email}\n')
                f.write(f'{password}')

    def login(self):
        """Login to MakeSchool dashboard using email and password.

        :param retries: URL path for the request. Should begin with a slash.
            :type: int
        :param backoff_factor: HTTP GET parameters.
            :type: float
        :param status_forcelist: The time of the first request (None if no
            retries have occurred).
            :type: tuple(int)
        :param session: The time of the first request (None if no
            retries have occurred).
            :type: Request Session Object
        """
        login_url = "https://www.makeschool.com/login"  # login url
        self.credentials()  # get the users credentials
        dashboard = self.s.get(login_url)  # get the login HTML
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
            form['user[email]'] = self.email
            # set the form password value
            form['user[password]'] = self.password
            # setup post request to login url with new data inserted into form
            response = self.s.post(login_url, data=form)
        else:
            # otherwise retry connection to server
            print('Retrying to connect to server')
            try:
                # HTTP retransmission to same urls
                requests_retry_session().get(login_url)
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
            # Get HTML tree representation from text
            html_tree = html.fromstring(response.text)
            # Get <HEAD> element from HTML tree
            root = html_tree.xpath('/html/head')
            # Get the text content in the <HEAD> element
            content = root[0].text_content()
            # Regex pattern for getting email
            pattern = r'[\w\.-]+@[\w\.-]+'
            # Get the email from the <HEAD> content using the regex pattern
            email = re.findall(pattern, content)
            # Send the user a message letting them know they singed in successfully, and print out their Make School email
            print(
                '\x1b[1;32m' + 'Signed in successfully.' + '\x1b[0m' + '\n' + f'Make School Email: {email[0]}' + '\n')
        else:
            # the crednetials are probably wrong
            print('The crendetials entered are incorrect.\n')
            # delete the creds file to start over
            os.remove(self.creds_path)
            # recall the login function
            self.login()

    def checkin(self):
        """Checks the user into their class!

        :param retries: URL path for the request. Should begin with a slash.
            :type: int
        :param backoff_factor: HTTP GET parameters.
            :type: float
        :param status_forcelist: The time of the first request (None if no
            retries have occurred).
            :type: tuple(int)
        :param session: The time of the first request (None if no
            retries have occurred).
            :type: Request Session Object
        """

        # log the user in
        self.login()
        # send a post request to the shortlink with the token provided from cli
        r = self.s.get(f'http://make.sc/attend/{self.token.upper()}')
        # create a tree out of the raw html
        dashboard_html = html.fromstring(r.text)
        # the xpath to the banner message
        xpath = r'//*[@id="js-header"]/div[3]/div/text()'
        # the dashboard message
        banner_message = dashboard_html.xpath(xpath)[0].strip()
        # check to make sure the request succeeded
        if r.status_code == 200:
            # Get the colored banner_message and print it to console
            banner_message = self._check_banner_message(banner_message)
            print(banner_message)
        else:
            # something went wrong so print red message
            print('\x1b[1;31m' +
                  'Something went wrong, please try again :(' + '\x1b[0m')

    # helper funcs
    def _check_banner_message(self, banner_message):
        """Checks the user into their class!

        :param retries: URL path for the request. Should begin with a slash.
            :type: int
        :param backoff_factor: HTTP GET parameters.
            :type: float
        :param status_forcelist: The time of the first request (None if no
            retries have occurred).
            :type: tuple(int)
        :param session: The time of the first request (None if no
            retries have occurred).
            :type: Request Session Object
        """
        message = None
        # check the message so that we can change the color :)
        if 'You code is not related to any class.' == banner_message:
            message = '\033[93m' + banner_message + '\x1b[0m' + '\n'  # yellow
        elif 'You are not registered for this class.' == banner_message:
            message = '\x1b[1;31m' + banner_message + '\x1b[0m' + '\n'  # red
        elif 'You need to be connected to Make School Wi-Fi to check-in.' == banner_message:
            message = '\x1b[1;31m' + banner_message + '\x1b[0m' + '\n'  # red
        elif 'You have already checked in for this class.' == banner_message:
            message = '\x1b[1;32m' + banner_message + '\x1b[0m' + '\n'  # green
        elif 'You have checked in present for this class.' == banner_message:
            message = '\x1b[1;32m' + banner_message + '\x1b[0m' + '\n'  # green
        else:
            message = '\033[93m' + banner_message + '\x1b[0m' + '\n'  # yellow

        return message

    def _get_keychain(self):
        """Checks the user into their class!

        :param retries: URL path for the request. Should begin with a slash.
            :type: int
        :param backoff_factor: HTTP GET parameters.
            :type: float
        :param status_forcelist: The time of the first request (None if no
            retries have occurred).
            :type: tuple(int)
        :param session: The time of the first request (None if no
            retries have occurred).
            :type: Request Session Object
        """

        macOS = 'darwin'
        linux = 'linux'
        windows = None  # we dont support :( sorry
        os_name = system().lower()
        if os_name in linux or os_name == linux:
            # Linux
            # for now store the users password file in documents
            password_path = '/Documents'
            # grab each users home directory
            home = os.path.expanduser('~')
            # keychain path
            keychain = home + password_path
            # return the keychain
            return keychain
        elif os_name in macOS or os_name == macOS:
            # MAC OS X
            # set the UNIX password file path
            password_path = '/Library/Keychains/'
            # grab each users home directory
            home = os.path.expanduser('~')
            # set the keychain path
            keychain = home + password_path
            # return the keychain
            return keychain

    def _encrypt(self, file):
        """Excrptys the credentials files"""
        pass


if __name__ == "__main__":
    # Get the first arg from command line
    args = sys.argv[1:3]
    # Get the attendence token from args
    try:
        token = args[0]
    except IndexError:
        print('Please add an attendence token after the script. Example: `python3 main.py BRAVE`')
        exit()
    # Create a new instance of CheckIn with the attendence token
    user = CheckIn(token)
    # Checkin
