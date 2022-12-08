from pages.help_page import HelpPage


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

