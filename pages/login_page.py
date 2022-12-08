from pages.base_page import BasePage
from locators.locators import LoginAndAccountLocators as log
from time import sleep

login = 'hhazzardd@mail.ru'
password = 'dfMuy4E09I'


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
        sleep(2)
        self.find_and_input(password, log.password_login)
        self.find_and_click(log.button_enter)

    def verify_account(self):
        verify = self.find_element(log.verifi_login)
        return verify.text

