from pages.base_page import BasePage
from locators.locators import MeAndBeloved as mab
from locators.locators import LoginAndAccountLocators as log
from time import sleep


class MeAndBeloved(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        #sleep(2)
        self.find_element(log.profile_button).click()
       # sleep(2)
        self.find_element(log.button_login).click()

    def open_account_page(self):
        login = 'hhazzardd@mail.ru'
        password = 'dfMuy4E09I'
        self.open_login_page()
       # sleep(3)
        self.find_element(log.email_login).send_keys(login)
        self.find_element(log.password_login).send_keys(password)
      #  sleep(2)
        self.find_element(log.button_enter).click()

    def open_me_and_beloved(self):
        # self.find_element(mab.check_box_man)
       # sleep(3)
        self.find_element(mab.meandbeloved).click()
       # sleep(3)
        self.find_element(mab.rings).click()

    def edit_filter(self):
       # sleep(10)
        self.find_element(mab.fixedprice).click()
        self.find_element(mab.size).click()
        # self.scroll_page()

    def edit_filter_2(self):
        #self.actions_chains(mab.mens)
        self.find_element(mab.mens).click()
        self.find_element(mab.country_russia).click()
        self.find_element(mab.button_show).click()

    def add_cart(self):
       # sleep(5)
        self.find_element(mab.ring_show).click()
        self.find_element(mab.button_add_cart).click()
        self.find_element(mab.button_cart_ring).click()

    def verify_price_ring(self):
        price_ring = self.find_element(mab.total_price)
        return price_ring.text
