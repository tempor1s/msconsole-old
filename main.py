#!/usr/local/bin/python3

import re
import os
import sys
import time
import requests
from lxml import html
from getpass import getpass
from verify import is_valid
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process, ProcessError
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()


class CheckIn(object):
    def __init__(self, token):
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.token = token
        self.s = requests.Session()  # masters/PHD student named this variable

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def login(self):
        dashboard = self.s.get("https://www.makeschool.com/login")
        dashboard_html = html.fromstring(dashboard.text)
        hidden_inputs = dashboard_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
        form['user[email]'] = self.email
        form['user[password]'] = self.password
        response = self.s.post(
            'https://www.makeschool.com/login', data=form)
        
    def checkin(self):
        self.login()
        r = self.s.post(f'http://make.sc/attend/{self.token.upper()}')
        
        if r.status_code == 200:
            print('Success. You are now attending the class :)')


############## Helper Functions ##################

def get_email():
    email = input('Email: ')
    return email


def get_pass():
    password = getpass()
    return password


def get_token():
    token = input('Token: ')
    return token


############## Helper Functions ##################
if __name__ == "__main__":
    # Get the first arg from command line
    args = sys.argv[1:3]
    # Get the attendence token from args
    token = args[0]
    # Create a new instance of CheckIn with the attendence token
    user = CheckIn(token)
    # Checkin
    user.checkin()
