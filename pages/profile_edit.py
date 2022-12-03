from pages.base_page import BasePage
from locators.locators import UserEdit as user
from locators.locators import LoginAndAccountLocators as log
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ProfileEdit(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        sleep(2)
        self.find_element(log.profile_button).click()
        sleep(2)
        self.find_element(log.button_login).click()

    def open_account_page(self):
        login = 'hhazzardd@mail.ru'
        password = 'dfMuy4E09I'
        self.open_login_page()
        sleep(3)
        self.find_element(log.email_login).send_keys(login)
        self.find_element(log.password_login).send_keys(password)
        sleep(2)
        self.find_element(log.button_enter).click()

    def user_settings(self):
        sleep(2)
        self.find_element(user.profile_button_user).click()
        self.find_element(user.setting_user).click()

    def edit_user_profile(self):
        name = 'Denis'
        surname = 'Fadeev'
        patronymic = 'Olegovich'
        phone = 89106459779
        address = 'street "Pushkina" home "Kolotushkina"'
        self.find_element(user.surname).send_keys(surname)
        self.find_element(user.name).send_keys(name)
        self.find_element(user.patronymic).send_keys(patronymic)
        self.find_element(user.phone).send_keys(phone)
        self.find_element(user.address).send_keys(address)
        self.find_element(user.sex).click()

    def edit_city(self):
        self.find_element(user.search_city).click()
        self.find_element(user.city).click()
        self.find_element(user.button_photo)
        # self.find_element(user.save_edit_button).click()

