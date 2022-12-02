from selenium.webdriver.common.by import By


class LoginAndAccountLocators:
    profile_button = (By.ID, 'desktop-profile-button')
    button_login = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/button[2]')
    email_login = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[1]/div/div/div[1]/input')
    password_login = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[2]/div/div/div[1]/input')
    button_enter = (By.XPATH, '//span[text()="Log In"]')


class UserEdit:
    profile_button_user = (By.XPATH, '//*[@id="desktop-profile-button"]/button')
    setting_user = (By.XPATH, '//*[@id="app"]/div/div[6]/div[2]/div/div/div[3]/div/i')
    surname = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]/input')
    name = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/input')
    patronymic = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/input')
    phone = (By.XPATH, '//*[@id="app"]/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/input')
    button_verify = (By.XPATH, '//*[@id="app"]/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/button')
    address = (By.XPATH, '//*[@id="app"]/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/input')
    search_city = (By.ID, 'citySearch')
    city = (By.XPATH, '/html/body/div[11]/div/div/div[2]/div/ul/li[1]/button/div[1]/div[1]')
    sex = (By.ID, 'select-gender0')
    # photo =
    button_photo = (By.XPATH, '//*[@id="app"]/div/div[5]/div[3]/div/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/button')
    save_edit_button = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/button')