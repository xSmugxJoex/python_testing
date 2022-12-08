from pages.me_and_beloved_page import MeAndBeloved


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
