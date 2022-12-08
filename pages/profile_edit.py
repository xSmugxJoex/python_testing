from pages.base_page import BasePage
from locators.locators import UserEdit as user
from locators.locators import LoginAndAccountLocators as log
from time import sleep

name = 'Denis.'
surname = 'Fadeev'
patronymic = 'Olegovich'
phone = '89106459779'
address = 'street "Pushkina" home "Kolotushkina"'


class ProfileEdit(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.base_url)
        sleep(2)
        self.find_and_click(log.profile_button)
        sleep(2)
        self.find_and_click(log.button_login)

    def open_account_page(self):
        login = 'hhazzardd@mail.ru'
        password = 'dfMuy4E09I'
        self.open_login_page()
        self.find_and_input(login, log.email_login)
        self.find_and_input(password, log.password_login)
        self.find_and_click(log.button_enter)

    def user_settings(self):
        self.find_and_click(user.profile_button_user)
        self.find_and_click(user.setting_user)

    def edit_user_profile(self):
        self.find_element(user.surname).clear()
        self.find_and_input(surname, user.surname)
        self.find_element(user.name).clear()
        self.find_and_input(name, user.name)
        self.find_element(user.patronymic).clear()
        self.find_and_input(patronymic, user.patronymic)
        self.find_element(user.phone).clear()
        self.find_and_input(phone, user.phone)
        self.find_element(user.address).clear()
        self.find_and_input(address, user.address)
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
        sleep(2)
        self.find_and_click(user.photo_enter)

    def verify_photo(self):
        verify_photo = self.find_element(user.verify_button_remove)
        return verify_photo

    def verify_email(self):
        verify_email = self.find_element(user.email)
        return verify_email.text
