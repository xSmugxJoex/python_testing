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
    phone = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/input')
    button_verify = (By.XPATH, '//*[@id="app"]/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/button')
    address = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div[1]/input')
    search_city = (By.ID, 'citySearch')
    city = (By.XPATH, '/html/body/div[11]/div/div/div[2]/div/ul/li[1]/button/div[1]/div[1]')
    sex = (By.ID, 'select-gender0')
    button_photo = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/button')
    photo = (By.XPATH, '//*[@id="file"]')
    photo_enter = (By.XPATH, '/html/body/div[10]/div/div/div[2]/div/div[2]/button[2]')
    save_edit_button = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/button')
    email = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div')

class CheckLot:
    search_lot = (By.ID, 'desktop-search-field')
    button_search = (By.XPATH, '//*[@id="desktop-search-string"]/button[2]')
    lot_name_button = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[2]/div/a')
    lot_name = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/div[2]/div[1]/div[2]')
    lot_price = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div[2]/b')
    lot_tag_1 = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[2]/a[1]')
    lot_tag_2 = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[2]/a[2]/span')

class MeAndBeloved:
    meandbeloved = (By.XPATH, '//*[@id="app"]/div/div[5]/div[1]/div[1]/div/button[3]')
    rings = (By.XPATH, '//*[@id="app"]/div/div[5]/div[1]/div[3]/div/div/div[1]/div[1]/a[7]')
    fixedprice = (By.ID, 'type2')
    size = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[5]/div/div[4]/label')
    mens = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[6]/div/div[1]/div')
    check_box_man = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[6]/header/span')
    country_russia = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[7]/div/div[1]/label')
    button_show = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div[3]/div/button')
    ring_show = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[2]/div/a/div[1]')
    button_add_cart = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/button[2]')
    button_cart_ring = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/button[2]')
    select_ring = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div')
    total_price = (By.XPATH, '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]')



