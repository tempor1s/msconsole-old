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

class Bot(object):
    def __init__(self):
        self.email = None  # user email
        self.password = None  # user password
        self.token = None  # access token
        self.chrome_path = os.getcwd() + '/chromedriver'  # chrome driver path
        # self.options = Options()
        # self.options.set_headless(headless=True)
        self.chrome_driver = webdriver.Chrome(
            self.chrome_path)

    def set_token(self, token):
        self.token = token

    def set_email(self, email):
        self.email = email

    def set_password(self, pw):
        if is_valid(pw):
            self.password = pw
        else:
            return False

    def login(self):

        # email XPath
        email_x_path = "//*[@id='user_email']"
        # password XPath
        password_x_path = "//*[@id='new_user']/label[2]/input"
        # login XPath
        login_x_path = "//*[@id='new_user']/input[3]"
        # set the driver
        driver = self.chrome_driver
        # the dashboard
        dashboard = driver.get("https://www.makeschool.com/dashboard")
        # find email field and fill
        email_field = driver.find_element_by_xpath(email_x_path)
        # clear the email field before filling
        email_field.clear()
        # fill the email field with users credentials
        email_field.send_keys(self.email)
        # find password field and fill
        password_field = driver.find_element_by_xpath(
            password_x_path)
        # clear the password field before filling
        password_field.clear()
        # fill the password field
        password_field.send_keys(self.password)
        # find login button
        login_button = driver.find_element_by_xpath(
            login_x_path)
        # click the button to submit the data
        login_button.click()
        time.sleep(20)

    def bruteforce(self, path='./wordlist/words.txt'):
        with open(path, "r") as file:
            word = file.read().split('\n')

    def checkin(self):
        # find access token path
        access_token = self.chrome_driver.find_element_by_xpath(
            "//*[@id='token']")
        # clear the form before filling
        access_token.clear()
        # fill the token
        access_token.send_keys(self.token)
        # find submit
        submit = self.chrome_driver.find_element_by_xpath(
            "//*[@id='form']/div/div/button")
        # IM HERE!
        submit.click()