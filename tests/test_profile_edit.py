import allure

from pages.profile_edit import ProfileEdit

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
        with allure.step('Verify avatar'):
            edit_profile.verify_photo()
        assert edit_profile.verify_photo() is not None

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
