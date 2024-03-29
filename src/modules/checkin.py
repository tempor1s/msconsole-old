#!/usr/bin/env python3

# TODO: Since this command and others are all going to use credentials, create a system to be able to store them application wide
__doc__ = """
This Module allows the user checkin to their class from the
command line.

It is assumed that the first argument given to this command is an
attendence token.

This tool accepts user credentials on first use. Depending on your os
the credentials are stored in the proper credentials directory and
encrypted with the users native os password encryption algorithm.

This script requires that `requests` and `lxml` be installed within the Python
environment you are running this script in.

If imported into another file the module contains the following
functions:

    * credentials - the main function of the script
    * _create_creds - Stores password in keychain
    * login - given credentials it logs a user in through url (https://makeschool.com/login)
    * checkin - checks a user into their class
    * _get_banner_message - gets the makeschool banner message from html
    * run - runs everything together and allows a user to check into their class

Usage:
    checkin
    checkin <token>
    checkin -h|--help
    checkin -v|--version
Options:
    <token>  Optional token argument.
    -h --help  Show help screen.
    -v --version  Show version.
"""
__maintainer__ = 'Ben Lafferty'
__credits__ = ['Ben Lafferty', 'Gary Frederick', 'Tasfia Addrita']
__license__ = 'MIT'
__version__ = '1.2.9'

# Standard Python modules
from getpass import getpass  # CLI hidden input functionality
from urllib3.util.retry import Retry  # HTTP retransmission functionality
from platform import system
import sys                   # System-specific parameters and functions.
import os                    # Miscellaneous OS interfaces.
import re                    # regular expression functions


# External Python modules
import requests
from lxml import html, etree
from requests.adapters import HTTPAdapter  # import HTTPAdapter module
import keyring
from docopt import docopt

# Local Python modules.
from src.utils.credential import _set_email, _set_password, _get_password, _get_email, _create_creds, _check_credentials
# for coloring the banner message depending on the message
from src.utils.colors import check_banner_message
# for querying makeschools general graphql
from src.utils.graphql import graph_query
from src.utils.http import retransmission  # for http get retransmission request


class CheckInModule(object):
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
        self.email = None  # users dashboard login
        self.token = token  # attendence token
        self.key = 'key'
        self.s = requests.Session()  # instantiate the request session

    def login(self):
        """Login to MakeSchool dashboard using email and password."""
        # makeschool login url to post and get from
        login_url = "https://www.makeschool.com/login"
        # get the login HTML
        dashboard = self.s.get(login_url)

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
            form['user[email]'] = _get_email(self.key)
            # set the form password value
            form['user[password]'] = _get_password(_get_email(self.key))
            # setup post request to login url with new data inserted into form
            response = self.s.post(login_url, data=form)
        else:
            # otherwise retry connection to server
            print('\x1b[1;31m' + 'Retrying to connect to server')
            t0 = time.time()
            try:
                response = retransmission(session=self.s).get(login_url)
            except Exception as x:
                print('It failed :(', x.__class__.__name__)
            # if there is a connection error request the user to try a new url
            # the url has changed in some way - we have to update
            except ConnectionError:
                print('Bad url request, try a different one by setting login url')
            # catastrophic error, no idea what to do with this just bail
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                print(e)
                sys.exit(1)
            else:
                print('It eventually worked', response.status_code)
            finally:
                t1 = time.time()
                print('Took', t1 - t0, 'seconds')

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
            _create_creds(self.key)
            self.login()

    def checkin(self):
        """Checks the user into their class! Requires the session to be logged in."""
        # send a post request to the shortlink with the token provided from cli
        response = self.s.get(f'http://make.sc/attend/{self.token.upper()}')
        # check to make sure the request succeeded
        if response.status_code == 200:
            # Get the colored banner_message and print it to console
            banner_message = self._get_banner_message(response.text)
            print(banner_message)
        else:
            # something went wrong so print red message
            print('\x1b[1;31m' +
                  'Something went wrong, please try again :(' + '\x1b[0m')

    # get the banner message from reponse text
    def _get_banner_message(self, response_text):
        # create a tree out of the raw html
        dashboard_html = html.fromstring(response_text)
        # the xpath to the banner message
        xpath = r'//*[@id="js-header"]/div[3]/div/text()'
        # the dashboard message
        banner_message = dashboard_html.xpath(xpath)[0].strip()
        # color the banner message and return it
        return check_banner_message(banner_message)

    def run(self):
        """Run mashes all of the functions togther and checks the user into their class."""
        # get the users creds
        _check_credentials(self.key)
        # log the user in
        self.login()
        # check the user in
        self.checkin()
