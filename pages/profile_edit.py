from pages.base_page import BasePage
from locators.locators import UserEdit as user
from locators.locators import LoginAndAccountLocators as log
from time import sleep

name = 'Denis.'
surname = 'Fadeev'
patronymic = 'Olegovich'
phone = 89106459779
address = 'street "Pushkina" home "Kolotushkina"'


class ProfileEdit(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        # sleep(2)
        self.find_and_click(log.profile_button)
        # sleep(2)
        self.find_and_click(log.button_login)

    def open_account_page(self):
        login = 'hhazzardd@mail.ru'
        password = 'dfMuy4E09I'
        self.open_login_page()
        # sleep(3)
        self.find_element(log.email_login).send_keys(login)
        self.find_element(log.password_login).send_keys(password)
        # sleep(2)
        self.find_and_click(log.button_enter)

    def user_settings(self):
        # sleep(2)
        self.find_and_click(user.profile_button_user)
        self.find_and_click(user.setting_user)

    def edit_user_profile(self):
        self.find_element(user.surname).clear()
        self.find_element(user.surname).send_keys(surname)
        self.find_element(user.name).clear()
        self.find_element(user.name).send_keys(name)
        self.find_element(user.patronymic).clear()
        self.find_element(user.patronymic).send_keys(patronymic)
        self.find_element(user.phone).clear()
        self.find_element(user.phone).send_keys(phone)
        self.find_element(user.address).clear()
        self.find_element(user.address).send_keys(address)
        self.find_and_click(user.sex)
        self.find_and_click(user.save_edit_button)

    def edit_city(self):
        self.find_and_click(user.search_city)
        self.find_and_click(user.city)

    def photo_edit(self):
        self.find_and_click(user.button_photo)
        # sleep(3)
        self.find_pic(user.photo).send_keys(
            '/home/iiqipii/Desktop/project/python_testing/profile_photo.jpeg'
        )
        # self.find_and_input('/home/iiqipii/Desktop/project/python_testing/profile_photo.jpeg', user.photo)
        sleep(2)
        self.find_and_click(user.photo_enter)
        # sleep(2)

    def verify_email(self):
        verify_email = self.find_element(user.email)
        return verify_email.text
