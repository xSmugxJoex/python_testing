from pages.me_and_beloved_page import MeAndBeloved


class TestCheckBuyRing:
    def test_add_cart(self, driver):
        add_cart = MeAndBeloved(driver)
        add_cart.open_login_page()
        add_cart.open_account_page()
        add_cart.open_me_and_beloved()
        add_cart.edit_filter()
        add_cart.edit_filter_2()
        add_cart.add_cart()
        add_cart.verify_price_ring()
        assert '₽6,875.00' in add_cart.verify_price_ring()
