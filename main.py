#!/usr/local/bin/python3

import os
import sys
import requests
from lxml import html
from verify import is_valid
from dotenv import load_dotenv
load_dotenv()


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
        filename = '.env'
        if os.path.exists(filename):
            self.email = os.getenv('EMAIL')
            self.password = os.getenv('PASSWORD')
        else:
            with open(filename, 'a+') as f:
                # TODO: Change the wording here because we are braindead
                email = input('Enter Makeschool login email (we don\'t store your email or password): ')
                password = input('Enter your Makeschool password: ')
                f.write(f'EMAIL={email}\n')
                f.write(f'PASSWORD={password}')

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
        
    def checkin(self):
        """Checks the user into their class!"""
        self.login()
        r = self.s.post(f'http://make.sc/attend/{self.token.upper()}')
        
        if r.status_code == 200:
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
