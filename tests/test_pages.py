import allure

from pages.login_page import LoginPage
from pages.profile_edit import ProfileEdit
from pages.me_and_beloved_page import MeAndBeloved
from pages.lot_page import CheckLot
from pages.help_page import HelpPage


@allure.feature('Authentication')
class TestAccountPage:
    @allure.story('Login Page')
    def test_open_login_page(self, driver):
        log_account = LoginPage(driver)
        with allure.step('Open Home Page'):
            log_account.open_login_page()
        with allure.step('Login'):
            log_account.open_account_page()
        with allure.step(f'Check account verify{log_account.verify_account()}'):
            log_account.verify_account()
        assert 'hhazzardd' in log_account.verify_account()


@allure.feature('Profile')
class TestProfileEdit:
    @allure.story('Edit profile')
    def test_edit_profile(self, driver):
        edit_profile = ProfileEdit(driver)
        with allure.step('Open Home Page'):
            edit_profile.open_login_page()
        with allure.step('Login'):
            edit_profile.open_account_page()
        with allure.step('Step settings'):
            edit_profile.user_settings()
        with allure.step('Edit city'):
            edit_profile.edit_city()
        with allure.step('Edit profile'):
            edit_profile.edit_user_profile()
        with allure.step('Edit photo'):
            edit_profile.photo_edit()

    @allure.story('Verify email')
    def test_verify_email(self, driver):
        verify_email = ProfileEdit(driver)
        with allure.step('Open Home Page'):
            verify_email.open_login_page()
        with allure.step('Login'):
            verify_email.open_account_page()
        with allure.step('Step settings'):
            verify_email.user_settings()
        with allure.step('Verify email'):
            verify_email.verify_email()
        assert 'hhazzardd@mail.ru' in verify_email.verify_email()


@allure.feature('Buy, check and remove ring')
class TestCheckBuyRing:
    @allure.story('Check ring')
    def test_verify_ring(self, driver):
        verify_text_ring = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            verify_text_ring.open_login_page()
        with allure.step('Login'):
            verify_text_ring.open_account_page()
        with allure.step('Open auction'):
            verify_text_ring.open_me_and_beloved()
        with allure.step('Use filter'):
            verify_text_ring.edit_filter()
        with allure.step('Verify name tot'):
            verify_text_ring.verify_ring()
        assert 'КОЛЬЦО ЗОЛОТОЕ С КОРУНДОМ. СССР 583 ПРОБА' in verify_text_ring.verify_ring()

    @allure.story('Buy ring')
    def test_add_cart(self, driver):
        add_cart = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            add_cart.open_login_page()
        with allure.step('Login'):
            add_cart.open_account_page()
        with allure.step('Open auction'):
            add_cart.open_me_and_beloved()
        with allure.step('Use filter'):
            add_cart.edit_filter()
        with allure.step('Add cart lot'):
            add_cart.add_cart()
        with allure.step(f'Check price lot: {add_cart.verify_price_ring()}'):
            add_cart.verify_price_ring()
        assert '₽14,500.00' in add_cart.verify_price_ring()

    @allure.story('Check cart')
    def test_check_color_cart_1(self, driver):
        check_color_1 = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            check_color_1.open_login_page()
        with allure.step('Login'):
            check_color_1.open_account_page()
        with allure.step(f'Verify remove: {check_color_1.verify_cart()}'):
            check_color_1.verify_cart()
        assert check_color_1.verify_cart() == 'rgba(211, 47, 47, 1)', 'Cart is empty!'

    @allure.story('Remove ring')
    def test_remove_all(self, driver):
        remove = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            remove.open_login_page()
        with allure.step('Login'):
            remove.open_account_page()
        with allure.step('Remove all lot'):
            remove.remove_all()
        with allure.step(f'Verify remove: {remove.verify_remove_all()}'):
            remove.verify_remove_all()
        assert 'All items have been removed' in remove.verify_remove_all()


@allure.feature('Check my lot')
class TestCheckLot:
    @allure.story('Check lot name')
    def test_check_lot_name(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot name:'):
            check_lot.check_lot_item()
        assert 'Винтажная бутылка(ДИПЛОМНЫЙ ПРОЕКТ!)' in check_lot.check_lot_name()

    @allure.story('Check lot price')
    def test_check_lot_price(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot price: {check_lot.check_lot_price()}'):
            check_lot.check_lot_item()
        assert '₽8,000,000' in check_lot.check_lot_price()

    @allure.story('Check lot tag 1')
    def test_check_lot_tag_1(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot tag 1: {check_lot.check_lot_tag_1()}'):
            check_lot.check_lot_item()
        assert 'ретро' in check_lot.check_lot_tag_1()

    @allure.story('Check lot tag 2')
    def test_check_lot_tag_2(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot tag 2: {check_lot.check_lot_tag_2()}'):
            check_lot.check_lot_item()
        assert 'редкость' in check_lot.check_lot_tag_2()


@allure.feature('Help Page')
class TestHelpPage:
    @allure.story('Registration and Login')
    def test_check_logo_help_page(self, driver):
        help_page = HelpPage(driver)
        with allure.step('Open Home Page'):
            help_page.open_login_page()
        with allure.step('Login'):
            help_page.open_account_page()
        with allure.step('Open Registration and Login'):
            help_page.open_help_logo()
        with allure.step(f'Verify logo: {help_page.check_logo_reg()}'):
            help_page.check_logo_reg()
        assert 'Registration and Login' in help_page.check_logo_reg()

    @allure.story('How the auction works')
    def test_how_the_actual_works(self, driver):
        how = HelpPage(driver)
        with allure.step('Open Home Page'):
            how.open_login_page()
        with allure.step('Login'):
            how.open_account_page()
        with allure.step('Open How the auction works'):
            how.how_the_actual_works()
        with allure.step(f'Verify logo: {how.check_logo_how()}'):
            how.check_logo_how()
        assert 'How the auction works' in how.check_logo_how()

    @allure.story('Problems logging into your account')
    def test_problems(self, driver):
        probl = HelpPage(driver)
        with allure.step('Open Home Page'):
            probl.open_login_page()
        with allure.step('Login'):
            probl.open_account_page()
        with allure.step('Problems'):
            probl.problems()
        with allure.step(f'Verify logo: {probl.check_logo_probl()}'):
            probl.check_logo_probl()
        assert 'Problems logging into your account' in probl.check_logo_probl()

    @allure.story('Forgot your password?')
    def test_forgot_pass(self, driver):
        passwd = HelpPage(driver)
        with allure.step('Open Home Page'):
            passwd.open_login_page()
        with allure.step('Login'):
            passwd.open_account_page()
        with allure.step('Forgot your password?'):
            passwd.forgot_pass()
        with allure.step(f'Verify logo: {passwd.check_logo_forgot_pass()}'):
            passwd.check_logo_forgot_pass()
        assert 'Forgot your password?' in passwd.check_logo_forgot_pass()
