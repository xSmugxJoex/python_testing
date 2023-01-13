import allure
import pytest
from pages.login_page import LoginPage

ANY_LOGIN = [
    {'email': 'mail@mail', 'passwrd': 'ygguy'},
    {'email': '@mail.com', 'passwrd': 'OJ*uhugf'},
    {'email': 'mail.com', 'passwrd': 'g7g5f'}
]


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


@allure.feature('Authentication')
@pytest.mark.parametrize('creds', ANY_LOGIN)
class TestAccountPageError:
    @allure.story('Login Page')
    def test_open_login_page(self, driver, creds):
        log_account = LoginPage(driver)
        with allure.step('Open Home Page'):
            log_account.open_login_page()
        with allure.step('Login'):
            log_account.logins_verify(login=creds['email'], password=creds['passwrd'])
        with allure.step(f'Check account verify{log_account.verify_account_error()}'):
            log_account.verify_account_error()
        assert 'Sorry, this e-mail address is not valid' in log_account.verify_account_error()
