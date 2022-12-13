import allure

from pages.me_and_beloved_page import MeAndBeloved

@allure.feature('Buy, check and remove ring')
class TestCheckBuyRing:
    @allure.story('Check ring')
    def test_verify_ring(self, driver):
        verify_text_ring = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            verify_text_ring.open_login_page()
        with allure.step('Login'):
            verify_text_ring.open_account_page()
        with allure.step('Open auction'):
            verify_text_ring.open_me_and_beloved()
        with allure.step('Use filter'):
            verify_text_ring.edit_filter()
        with allure.step('Verify name tot'):
            verify_text_ring.verify_ring()
        assert 'КОЛЬЦО ЗОЛОТОЕ С КОРУНДОМ. СССР 583 ПРОБА' in verify_text_ring.verify_ring()

    @allure.story('Buy ring')
    def test_add_cart(self, driver):
        add_cart = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            add_cart.open_login_page()
        with allure.step('Login'):
            add_cart.open_account_page()
        with allure.step('Open auction'):
            add_cart.open_me_and_beloved()
        with allure.step('Use filter'):
            add_cart.edit_filter()
        with allure.step('Add cart lot'):
            add_cart.add_cart()
        with allure.step(f'Check price lot: {add_cart.verify_price_ring()}'):
            add_cart.verify_price_ring()
        assert '₽14,500.00' in add_cart.verify_price_ring()

    @allure.story('Check cart')
    def test_check_color_cart_1(self, driver):
        check_color_1 = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            check_color_1.open_login_page()
        with allure.step('Login'):
            check_color_1.open_account_page()
        with allure.step(f'Verify remove: {check_color_1.verify_cart()}'):
            check_color_1.verify_cart()
        assert check_color_1.verify_cart() == 'rgba(211, 47, 47, 1)', 'Cart is empty!'

    @allure.story('Remove ring')
    def test_remove_all(self, driver):
        remove = MeAndBeloved(driver)
        with allure.step('Open Home Page'):
            remove.open_login_page()
        with allure.step('Login'):
            remove.open_account_page()
        with allure.step('Remove all lot'):
            remove.remove_all()
        with allure.step(f'Verify remove: {remove.verify_remove_all()}'):
            remove.verify_remove_all()
        assert 'All items have been removed' in remove.verify_remove_all()
