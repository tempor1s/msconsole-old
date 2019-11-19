#!/usr/local/bin/python3

import os
import sys
import requests
from lxml import html, etree


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
        """Set email and password fields if file exists, otherwise create creds.txt file and get email and password from user."""
        filename = 'creds.txt'
        # TODO: Rewrite this with .env
        # check if file exists - if it does then set email and password from env, otherwise get email and password from user and create creds.txt file
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                # read email and password from file into a list
                lines = f.read().split('\n')

                self.email = lines[0]
                self.password = lines[1]
        else:
            # create a new file
            with open(filename, 'a+') as f:
                # get the email and password from the user
                email = input(
                    'Enter Makeschool login email (we don\'t store your email or password on a server): ')
                password = input('Enter your Makeschool password: ')
                # set email and password properties
                self.email = email
                self.password = password
                # write the email and the password to the creds.txt file for later use
                f.write(f'{email}\n')
                f.write(f'{password}')

    def login(self):
        """Login to MakeSchool dashboard using email and password."""
        login_url = "https://www.makeschool.com/login"
        self.credentials()
        dashboard = self.s.get(login_url)
        if dashboard.status_code == 200:
            dashboard_html = html.fromstring(dashboard.text)
            hidden_inputs = dashboard_html.xpath(
                r'//form//input[@type="hidden"]')
            form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
            form['user[email]'] = self.email
            form['user[password]'] = self.password
            response = self.s.post(
                'https://www.makeschool.com/login', data=form)
        else:
            print('Retrying to connect to server')
            requests_retry_session().get(login_url)

        # jesus christ
        if 'successfully' in response.text:
            print('Signed in successfully.')
        else:
            # the crednetials are probably wrong
            print('The crendetials entered are incorrect.\n')
            # delete the creds file to start over
            os.remove('creds.txt')
            # recall the login function
            self.login()

    def checkin(self):
        """Checks the user into their class!"""
        # log the user in
        self.login()
        # send a post request to the shortlink with the token provided from cli
        r = self.s.post(f'http://make.sc/attend/{self.token.upper()}')

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
    token = args[0]
    # Create a new instance of CheckIn with the attendence token
    user = CheckIn(token)
    # Checkin
    user.checkin()
