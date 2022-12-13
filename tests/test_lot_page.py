import allure

from pages.lot_page import CheckLot

@allure.feature('Check my lot')
class TestCheckLot:
    @allure.story('Check lot name')
    def test_check_lot_name(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot name:'):
            check_lot.check_lot_item()
        assert 'Винтажная бутылка(ДИПЛОМНЫЙ ПРОЕКТ!)' in check_lot.check_lot_name()

    @allure.story('Check lot price')
    def test_check_lot_price(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot price: {check_lot.check_lot_price()}'):
            check_lot.check_lot_item()
        assert '₽8,000,000' in check_lot.check_lot_price()

    @allure.story('Check lot tag 1')
    def test_check_lot_tag_1(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot tag 1: {check_lot.check_lot_tag_1()}'):
            check_lot.check_lot_item()
        assert 'ретро' in check_lot.check_lot_tag_1()

    @allure.story('Check lot tag 2')
    def test_check_lot_tag_2(self, driver):
        check_lot = CheckLot(driver)
        with allure.step('Open site'):
            check_lot.open_site()
        with allure.step(f'Verify lot tag 2: {check_lot.check_lot_tag_2()}'):
            check_lot.check_lot_item()
        assert 'редкость' in check_lot.check_lot_tag_2()
