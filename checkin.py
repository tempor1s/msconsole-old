#!/usr/bin/env python3
import os
import re
import sys
import requests
from lxml import html, etree
from getpass import getpass
from platform import platform, system

# set the UNIX password file path
password_path = '/Library/Keychains/'
# grab each users home directory
home = os.path.expanduser('~')
# set the keychain path
keychain = home + password_path
# check to see if file exists
macOS = 'darwin'
linux = 'linux'


class CheckIn(object):
    """CheckIn is a class that allows you to checkin to your MakeShool classes using a CLI"""

    def __init__(self, token):
        """
        Params:
            token: str - The login token for that class
        """
        self.email = None
        self.password = None
        self.token = token
        self.s = requests.Session()  # masters/PHD student named this variable
        self.creds_path = keychain + 'creds.txt'

    def requests_retry_session(self, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
        """Retry requesting session
        Keyword arguments:
            retries -- limit of retries before fatal error
            backoff_factor -- time limit before creating new request
            status_forcelist -- force retry request status code list
            session -- established connection between client and server
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
        """Login to MakeSchool dashboard using email and password."""
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
            print(f'Signed in successfully. Make School Email: {email[0]}')
        else:
            # the crednetials are probably wrong
            print('The crendetials entered are incorrect.\n')
            # delete the creds file to start over
            os.remove(self.creds_path)
            # recall the login function
            self.login()

    def checkin(self):
        """Checks the user into their class!"""
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
            print('Request succeeded. Banner message is as followed:\n')
            print(banner_message, '\n')
        else:
            print('Something went wrong, please try again :(')


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
    user.checkin()
