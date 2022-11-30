from selenium.webdriver.common.by import By


class LoginAndAccountLocators:
    login = (By.ID, 'mobile-profile-button')
    button_login = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/button[2]')
    email_login = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[1]/div/div/div[1]/input')
    password_login = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[2]/div/div/div[1]/input')
    button_enter = (By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/button[1]')
