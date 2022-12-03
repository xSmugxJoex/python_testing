from pages.login_page import LoginPage


class TestAccountPage:
    def test_open_login_page(self, driver):
        log_account = LoginPage(driver)
        log_account.open_login_page()
        log_account.open_account_page()
