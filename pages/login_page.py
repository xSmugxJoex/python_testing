from pages.base_page import BasePage
from locators.locators import LoginAndAccountLocators as log
from time import sleep
import json
from functools import lru_cache


class AccountLogin:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.open_file()
        self.login = self.data['login']
        self.password = self.data['password']

    def open_file(self):
        with open(self.filename, 'r') as accountfiles:
            return json.load(accountfiles)


account = AccountLogin('../account.txt')

login = account.login
password = account.password

@lru_cache(maxsize=None)
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        sleep(2)
        self.find_and_click(log.profile_button)
        self.find_and_click(log.button_login)

    def open_account_page(self):
        self.open_login_page()
        self.find_and_input(login, log.email_login)
        self.find_and_input(password, log.password_login)
        self.find_and_click(log.button_enter)

    def verify_account(self):
        verify = self.find_element(log.verifi_login)
        return verify.text

    def logins_verify(self, login, password):
        self.open_login_page()
        self.find_element_error(log.email_login).send_keys(login)
        sleep(2)
        self.find_element_error(log.password_login).send_keys(password)
        self.find_and_click(log.button_enter)

    def verify_account_error(self):
        verify = self.find_element(log.error_login)
        return verify.text
