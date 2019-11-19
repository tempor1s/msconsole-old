#!/usr/local/bin/python3

import os
import sys
import requests
from lxml import html


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

    def credentials(self):
        """Set email and password fields if file exists, otherwise create .env file and get email and password from user."""
        filename = 'creds.txt'
        # TODO: Rewrite this
        # check if file exists - if it does then set email and password from env, otherwise get email and password from user and create .env file
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
                # write the email and the password to the .env file for later use
                f.write(f'{email}\n')
                f.write(f'{password}')

    def login(self):
        """Login to MakeSchool dashboard using email and password."""
        self.credentials()
        dashboard = self.s.get("https://www.makeschool.com/login")
        dashboard_html = html.fromstring(dashboard.text)
        hidden_inputs = dashboard_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
        form['user[email]'] = self.email
        form['user[password]'] = self.password
        response = self.s.post(
            'https://www.makeschool.com/login', data=form)
        
        # jesus christ
        if 'successfully' in response.text:
            print('Signed in successfully.')
        else:
            # the crednetials are probably wrong
            print('The crendetials entered are incorrect.\n')
            # delete the creds file to start over
            os.remove('creds.txt')
            # recall the credentials function
            self.login()

    def checkin(self):
        """Checks the user into their class!"""
        # log the user in
        self.login()
        # send a post request to the shortlink with the token provided from cli
        r = self.s.post(f'http://make.sc/attend/{self.token.upper()}')

        # check to see if the login was successful
        print('Success. You are now attending the class :)')
        


if __name__ == "__main__":
    # Get the first arg from command line
    args = sys.argv[1:3]
    # Get the attendence token from args
    token = args[0]
    # Create a new instance of CheckIn with the attendence token
    user = CheckIn(token)
    # Checkin
    user.checkin()