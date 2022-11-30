from pages.base_page import BasePage
from locators.locators import LoginAndAccountLocators as log


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        self.find_element(log.login).click()
        self.find_element(log.button_login).click()

    def open_account_page(self):
        login = 'hhazzardd@mail.ru'
        password = 'dfMuy4E09I'
        self.open_login_page()
        self.find_element(log.email_login).send_keys(login)
        self.find_element(log.password_login).send_keys(password)
        self.find_element(log.button_enter)
