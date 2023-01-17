from pages.base_page import BasePage
from locators.locators import LoginAndAccountLocators as log
from locators.locators import Help
from time import sleep
import json


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


class HelpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        sleep(3)
        self.find_and_click(log.profile_button)
        self.find_and_click(log.button_login)

    def open_account_page(self):
        self.open_login_page()
        self.find_and_input(login, log.email_login)
        self.find_and_input(password, log.password_login)
        self.find_and_click(log.button_enter)

    def open_help_logo(self):
        self.find_and_click(Help.menu)
        self.find_and_click(Help.help_button)
        sleep(3)
        self.switch_to_windows(1)
        self.find_and_click(Help.registration_and_login)

    def check_logo_reg(self):
        check_logo = self.find_element(Help.logo_reg_adn_log)
        return check_logo.text

    def how_the_actual_works(self):
        self.find_and_click(Help.menu)
        self.find_and_click(Help.help_button)
        sleep(3)
        self.switch_to_windows(1)
        self.find_and_click(Help.registration_and_login)
        self.find_and_click(Help.how_the_actual_works)

    def check_logo_how(self):
        check_logo = self.find_element(Help.logo_htaw)
        return check_logo.text

    def problems(self):
        self.find_and_click(Help.menu)
        self.find_and_click(Help.help_button)
        sleep(3)
        self.switch_to_windows(1)
        self.find_and_click(Help.registration_and_login)
        self.find_and_click(Help.problems)

    def check_logo_probl(self):
        check_logo = self.find_element(Help.logo_probl)
        return check_logo.text

    def forgot_pass(self):
        self.find_and_click(Help.menu)
        self.find_and_click(Help.help_button)
        sleep(3)
        self.switch_to_windows(1)
        self.find_and_click(Help.registration_and_login)
        self.find_and_click(Help.forgot_pass)

    def check_logo_forgot_pass(self):
        check_logo = self.find_element(Help.logo_pass)
        return check_logo.text
