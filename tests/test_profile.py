from pages.profile_edit import ProfileEdit


class TestProfileEdit:
    def test_edit_profile(self, driver):
        edit_profile = ProfileEdit(driver)
        edit_profile.open_login_page()
        edit_profile.open_account_page()
        edit_profile.user_settings()
        edit_profile.edit_user_profile()

