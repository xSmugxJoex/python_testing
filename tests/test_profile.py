from pages.profile_edit import ProfileEdit


class TestProfileEdit:
    def test_edit_profile(self, driver):
        edit_profile = ProfileEdit(driver)
        edit_profile.open_login_page()
        edit_profile.open_account_page()
        edit_profile.user_settings()
        edit_profile.edit_user_profile()
        edit_profile.edit_city()
        edit_profile.photo_edit()

    def test_verify_email(self, driver):
        verify_email = ProfileEdit(driver)
        verify_email.open_login_page()
        verify_email.open_account_page()
        verify_email.user_settings()
        verify_email.verify_email()
        assert 'hhazzardd@mail.ru' in verify_email.verify_email()

