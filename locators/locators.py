from selenium.webdriver.common.by import By


class LoginAndAccountLocators:
    profile_button = (By.XPATH, '//div[@class="appToolbar_b3450 scroll-lock-padding"]/button[2]' or '//div[@class="ma-0"]/div[2]/div/button[2]')
    button_login = (By.XPATH, '//div[@class="buttons_eda00"]/button[2]')
    email_login = (By.XPATH, '//div[@class="inputWithPrefix_98cbc"]/input[1]')
    password_login = (By.XPATH, '//div[@data-test="auth/password"]/div[1]/div[1]/div[1]/input')
    button_enter = (By.XPATH, '//span[text()="Log In"]')
    verifi_login = (By.XPATH, '//div[@class="container_00e12 profileButton_b3450"]/button/span[text()]')
    error_login = (By.XPATH, '//div[@class="inputContainer_98cbc"]/div[2]/label[text()]')



class UserEdit:
    profile_button_user = (By.XPATH, '//*[@id="desktop-profile-button"]/button')
    setting_user = (By.XPATH, '//div[@data-test="profile-menu/profile"]')
    surname = (By.CSS_SELECTOR, 'div.userName_007ce :nth-child(2) .input_98cbc')
    name = (By.XPATH, '//div[@data-test="profile/basic/first-name"]/div/div/div/input')
    patronymic = (By.CSS_SELECTOR, 'div.userName_007ce :nth-child(3) .input_98cbc')
    phone = (By.CSS_SELECTOR, 'div.phones_007ce .input_98cbc')
    button_verify = (By.CSS_SELECTOR, 'div.standardPadding_8e048 .form_007ce .text_a30a1')
    address = (By.XPATH, '//div[@data-test="profile/basic/address"]/div/div/div/input')
    search_city = (By.ID, 'citySearch')
    city = (By.CSS_SELECTOR, '.list_516bf :nth-child(1) .listItem_516bf')
    enter_city = (By.CSS_SELECTOR, 'div.buttons_0218e .button_a30a1')
    sex = (By.ID, 'select-gender0')
    button_photo = (By.XPATH, '//div[@class="avatarButton_007ce"]/div/button')
    photo = (By.XPATH, '//div[@class="avatarButton_007ce"]/div/input')
    photo_enter = (By.XPATH, '//div[@class="wrapper_517a5"]/div[2]/button[2]')
    save_edit_button = (By.XPATH, '//div[@class="standardPadding_8e048"]/div/button')
    email = (By.CSS_SELECTOR, 'div.card_8e048 .standardPadding_8e048 .email_007ce')
    verify_button_remove = (By.XPATH, '//button[@data-test="profile/basic/avatar-remove-button" and @data-rpl-input="true"]')
    photo_acc = (By.CSS_SELECTOR, 'div.avatar_007ce')

class CheckLot:
    search_lot = (By.ID, 'desktop-search-field')
    button_search = (By.XPATH, '//div[@id="desktop-search-string"]/button[2]')
    lot_name_button = (By.CSS_SELECTOR, 'div.wrapper_d828a .itemTitle_d828a')
    lot_name = (By.CSS_SELECTOR, 'div.lotContent_f5313 .titleText_aa41c')
    lot_price = (By.CSS_SELECTOR, 'div.lotContent_f5313 .priceAndButtons_3521f .price_3521f')
    lot_tag_1 = (By.XPATH, '//div[@class="slider_7811c"]/a[1]/span[text()]')
    lot_tag_2 = (By.XPATH, '//div[@class="slider_7811c"]/a[2]/span[text()]')

class MeAndBeloved:
    meandbeloved = (By.XPATH, '//div[@class="content_c4076"]/div[1]/div[1]/div/button[3]')
    rings = (By.XPATH, '//div[@class="row_13785"]/div[1]/a[7]')
    fixedprice = (By.ID, 'type2')
    size = (By.PARTIAL_LINK_TEXT, '16,5')
    input_ring = (By.XPATH, '//div[@class="innerContainer_98cbc"]/div[1]/div[1]/input')
    button_show = (By.XPATH, '//div[@sticky-side="bottom"]/div/button')
    ring_show = (By.XPATH, '//div[@class="wrapper_d828a"]/a[1]')
    ring_verify_text = (By.XPATH, '//div[@class="title_aa41c"]/div[2][text()]')
    button_add_cart = (By.XPATH, '//button[@title="Add to cart"]')
    next_cart = (By.XPATH, '//div[@data-test="functional-menu/cart"]')
    remove_menu = (By.CSS_SELECTOR, 'div.sidePanelContent_701f0 :nth-child(3)')
    select_ring = (By.XPATH, '//div[@class="box_13ea3"][1]')
    total_price = (By.XPATH, '//div[@class="standardPadding_8e048"]/div[2]/div[text()]')
    remove_all = (By.XPATH,  '//div[@class="selectAll_6dca5"]/button')
    verify_remove_all = (By.XPATH, '//span[@class="text_bff57"][text()]')
    empty_cart = (By.XPATH, '//div[@id="desktop-cart-button"]/button/span')


class Help:
    menu = (By.ID, 'desktop-functional-menu-button')
    help_button = (By.XPATH, '//div[@class="container_3afc8 functionalMenu_65c00"]/a[4]/div')
    registration_and_login = (By.CSS_SELECTOR, 'div.container .section a')
    logo_reg_adn_log = (By.XPATH, './/main/div/h1[text()]')
    how_the_actual_works = (By.CSS_SELECTOR, 'li.section .section-inner')
    logo_htaw = (By.XPATH, '//article/div/h1[text()]')
    problems = (By.XPATH, '//li[2]/a')
    logo_probl = (By.XPATH, '//main/article/div/h1[text()]')
    forgot_pass = (By.XPATH, '//li[3]/a')
    logo_pass = (By.XPATH, '//main/article/div/h1[text()]')



