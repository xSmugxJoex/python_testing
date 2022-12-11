from pages.base_page import BasePage
from locators.locators import CheckLot as lot
from time import sleep


class CheckLot(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_site(self):
        self.driver.get(self.base_url)

    def check_lot_item(self):
        self.find_and_click(lot.search_lot)
        sleep(2)
        self.find_element(lot.search_lot).send_keys('Винтажная бутылка(ДИПЛОМНЫЙ ПРОЕКТ!)')
        self.find_and_click(lot.button_search)
        self.find_and_click(lot.lot_name_button)

    def check_lot_name(self):
        checking_lot_name = self.find_element(lot.lot_name)
        return checking_lot_name.text

    def check_lot_price(self):
        checking_lot_price = self.find_element(lot.lot_price)
        return checking_lot_price.text

    def check_lot_tag_1(self):
        checking_lot_tag_1 = self.find_element(lot.lot_tag_1)
        return checking_lot_tag_1.text

    def check_lot_tag_2(self):
        checking_lot_tag_2 = self.find_element(lot.lot_tag_2)
        return checking_lot_tag_2.text
