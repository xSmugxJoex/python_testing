import allure

from pages.login_page import LoginPage

@allure.feature('Authentication')
@allure.story('Login')
class TestAccountPage:
    def test_open_login_page(self, driver):
        log_account = LoginPage(driver)
        with allure.step('Open Home Page'):
            log_account.open_login_page()
        with allure.step('Login'):
            log_account.open_account_page()
        with allure.step('Check account verify'):
            log_account.verify_account()
        assert 'hhazzardd' in log_account.verify_account()
