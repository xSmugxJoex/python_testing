import allure

from pages.help_page import HelpPage

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
