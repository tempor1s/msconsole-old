import requests
from selenium import webdriver
from getpass import getpass
from threading import Thread
from verify import is_valid
from selenium.webdriver.common.keys import Keys
import time
import os

# set driver path
driver = os.getcwd() + '/chromedriver'


class Bot(object):
    def __init__(self):
        self.email = None
        self.password = None
        self.token = None
        self.driver = webdriver.Chrome(driver)

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
        driver = self.driver
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
        time.sleep(2)

    def bruteforce(self, path='./wordlist/words.txt'):
        with open(path, "r") as file:
            word = file.read().split('\n')

    def checkin(self):
        # find access token path
        access_token = self.driver.find_element_by_xpath("//*[@id='token']")
        # clear the form before filling
        access_token.clear()
        # fill the token
        access_token.send_keys(self.token)
        # find submit
        submit = self.driver.find_element_by_xpath(
            "//*[@id='form']/div/div/button")
        # IM HERE!
        submit.click()


def get_email():
    email = input('Email: ')
    return email


def get_pass():
    password = getpass()
    return password


def get_token():
    token = input('Token: ')
    return token


if __name__ == "__main__":
    # grab the users email address
    email = get_email()
    # grab the users password
    pw = get_pass()
    # get the access token
    token = get_token()
    # instantiate the users bot
    user = Bot()
    # set the user email
    user.set_email(email)
    # set the user password
    user.set_password(pw)
    # set the user token
    user.set_token(token)
    # login
    user.login()
    # check in
    user.checkin()
