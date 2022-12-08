import allure

from pages.login_page import LoginPage
from pages.profile_edit import ProfileEdit
from pages.me_and_beloved_page import MeAndBeloved
from pages.lot_page import CheckLot
from pages.help_page import HelpPage

@allure.feature('Authentication')
@allure.story('Login')
class TestAccountPage:
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
@allure.story('Edit profile')
class TestProfileEdit:
    def test_edit_profile(self, driver):
        edit_profile = ProfileEdit(driver)
        with allure.step('Open Home Page'):
            edit_profile.open_login_page()
        with allure.step('Login'):
            edit_profile.open_account_page()
        with allure.step('Step settings'):
            edit_profile.user_settings()
        with allure.step('Edit profile'):
            edit_profile.edit_user_profile()
        with allure.step('Edit city'):
            edit_profile.edit_city()
        with allure.step('Edit photo'):
            edit_profile.photo_edit()
        with allure.step('Verify photo'):
            edit_profile.verify_photo()
        assert True in edit_profile.verify_photo()


    def test_verify_email(self, driver):
        verify_email = ProfileEdit(driver)
        verify_email.open_login_page()
        verify_email.open_account_page()
        verify_email.user_settings()
        verify_email.verify_email()
        assert 'hhazzardd@mail.ru' in verify_email.verify_email()


class TestCheckBuyRing:
    def test_verify_ring(self, driver):
        verify_text_ring = MeAndBeloved(driver)
        verify_text_ring.open_login_page()
        verify_text_ring.open_account_page()
        verify_text_ring.open_me_and_beloved()
        verify_text_ring.edit_filter()
        verify_text_ring.verify_ring()
        assert 'КОЛЬЦО ЗОЛОТОЕ С КОРУНДОМ. СССР 583 ПРОБА' in verify_text_ring.verify_ring()

    def test_add_cart(self, driver):
        add_cart = MeAndBeloved(driver)
        add_cart.open_login_page()
        add_cart.open_account_page()
        add_cart.open_me_and_beloved()
        add_cart.edit_filter()
        add_cart.add_cart()
        add_cart.verify_price_ring()
        assert '₽14,500.00' in add_cart.verify_price_ring()

    def test_remove_all(self, driver):
        remove = MeAndBeloved(driver)
        remove.open_login_page()
        remove.open_account_page()
        remove.remove_all()
        remove.verify_remove_all()
        assert 'All items have been removed' in remove.verify_remove_all()


class TestCheckLot:
    def test_check_lot_name(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert 'Винтажная бутылка(ДИПЛОМНЫЙ ПРОЕКТ!)' in check_lot.check_lot_name()

    def test_check_lot_price(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert '₽8,000,000' in check_lot.check_lot_price()

    def test_check_lot_tag_1(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert 'ретро' in check_lot.check_lot_tag_1()

    def test_check_lot_tag_2(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert 'редкость' in check_lot.check_lot_tag_2()


class TestHelpPage:
    def test_check_logo_help_page(self, driver):
        help_page = HelpPage(driver)
        help_page.open_login_page()
        help_page.open_account_page()
        help_page.open_help_logo()
        help_page.check_logo_reg()
        assert 'Registration and Login' in help_page.check_logo_reg()

    def test_how_the_actual_works(self, driver):
        how = HelpPage(driver)
        how.open_login_page()
        how.open_account_page()
        how.how_the_actual_works()
        how.check_logo_how()
        assert 'How the auction works' in how.check_logo_how()

    def test_problems(self, driver):
        probl = HelpPage(driver)
        probl.open_login_page()
        probl.open_account_page()
        probl.problems()
        probl.check_logo_probl()
        assert 'Problems logging into your account' in probl.check_logo_probl()

    def test_forgot_pass(self, driver):
        passwd = HelpPage(driver)
        passwd.open_login_page()
        passwd.open_account_page()
        passwd.forgot_pass()
        passwd.check_logo_forgot_pass()
        assert 'Forgot your password?' in passwd.check_logo_forgot_pass()