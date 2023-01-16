from pages.base_page import BasePage
from locators.locators import MeAndBeloved as mab
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


account = AccountLogin('/home/qip/Desktop/projects/python_testing/account.txt')

login = account.login
password = account.password


class MeAndBeloved(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        sleep(2)
        self.find_element(log.profile_button).click()
        sleep(2)
        self.find_element(log.button_login).click()

    def open_account_page(self):
        self.open_login_page()
        self.find_and_input(login, log.email_login)
        self.find_and_input(password, log.password_login)
        self.find_element(log.button_enter).click()

    def open_me_and_beloved(self):
        sleep(3)
        self.find_element(mab.meandbeloved).click()
        sleep(3)
        self.find_element(mab.rings).click()

    def edit_filter(self):
        self.find_and_click(mab.fixedprice, time=3)
        self.find_and_click(mab.size, time=3)
        self.find_element(mab.input_ring).send_keys('КОЛЬЦО ЗОЛОТОЕ С КОРУНДОМ. СССР 583 ПРОБА')
        sleep(3)
        self.find_and_click(mab.button_show)
        sleep(3)
        self.find_and_click(mab.ring_show)

    def add_cart(self):
        sleep(3)
        self.find_and_click(mab.button_add_cart)
        sleep(3)
        self.find_and_click(Help.menu)
        self.find_and_click(mab.next_cart)
        sleep(5)
        self.find_and_click(mab.select_ring)

    def verify_cart(self):
        color_cart = self.color_verify(mab.empty_cart, 'background-color')
        return color_cart

    def remove_all(self):
        self.find_and_click(Help.menu)
        sleep(3)
        self.find_and_click(mab.remove_menu)
        self.find_and_click(mab.remove_all)

    def verify_remove_all(self):
        remove_all = self.find_element(mab.verify_remove_all)
        return remove_all.text

    def verify_ring(self):
        veryfi_text = self.find_element(mab.ring_verify_text)
        return veryfi_text.text

    def verify_price_ring(self):
        price_ring = self.find_element(mab.total_price)
        return price_ring.text
